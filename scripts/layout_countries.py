#!/usr/bin/env python3
"""
scripts/layout_countries.py — Phase 4b: data-driven layout for the v2 (MapLibre) renderer.

Runs AFTER scripts/export_geojson.py and post-processes site/v2/data/{countries,labels,events}.geojson in place:

 B. Polygons for every spatial country. atlas.html's fineCell rule only draws a country where its parent continent
    owns the country's sub_band rows in the authoring GRID; 9 spatial countries (the three Antecedent Isles, four on
    the Cybernetic Shore, critics-tundra, expert-systems-country) claim rows their continent never occupies, so they
    had no polygon. Here the FREE land of each continent (continent minus its existing country polygons) is split
    among the missing countries by LANE SLICING: x-columns at every X(start)/X(end) of the missing countries (the
    same piecewise time axis as atlas.html, AXES.md §1), and inside each column the free strip is cut into equal
    horizontal lanes, one per country active in that column, ordered north→south by band (N1a … S2c — the order
    atlas.html's FINE rows use). Every piece is (free ∩ column ∩ lane), so containment in the continent and zero
    overlap with every other country are true by construction. Existing atlas.html polygons are kept untouched.
    The Antecedent Isles are an archipelago: whole isles are assigned to the country whose time_range is nearest
    the isle's authored year (a lane cut through a 30-unit islet would make unreadable slivers).
 C. Event placement for events atlas.html could not place at lod4 (exported at X(year) × country centroid, all
    stacked on one point): x = X(year) (clamped into the country polygon when the polygon does not reach that x —
    only happens on the log-compressed isles axis), y = a deterministic greedy non-overlap walk down the polygon's
    vertical chord at that x (start fraction from a hash of the event id, golden-ratio steps, first position ≥ MIN_SEP
    plate units from every other event of the plate wins; otherwise the farthest one). No randomness.
 D. `class` property on point features (landmark / country / continent / fact) for the sampler.

Deterministic: same inputs → byte-identical outputs. Idempotent: features this script generated carry
`layout: "lane"` (countries/labels) or `layout: "chord"` (events) and are recomputed on every run.
Nothing is invented: names / years / text come from site/entities.json only.

Usage:  /home/node/agent/venvs/mapai/bin/python scripts/layout_countries.py [--check]
        --check  verify only (every spatial country has a polygon inside its continent, 0 overlaps, every
                 chord-placed event inside its country, no two events on one point); exit 1 on failure.
"""
import argparse
import datetime
import hashlib
import json
import math
import sys
from pathlib import Path

from shapely.geometry import Point, Polygon, MultiPolygon, box, mapping, shape
from shapely.ops import unary_union, polylabel

REPO = Path(__file__).resolve().parent.parent
SITE = REPO / "site"
DATA = SITE / "v2" / "data"

# ---- plate ↔ lng/lat (scripts/export_geojson.py)
X0, Y0, UNITS_PER_DEG = 900.0, 525.0, 50.0
to_lnglat = lambda x, y: [round((x - X0) / UNITS_PER_DEG, 5), round(-(y - Y0) / UNITS_PER_DEG, 5)]
to_plate = lambda lng, lat: (lng * UNITS_PER_DEG + X0, -lat * UNITS_PER_DEG + Y0)

# ---- X axis: atlas.html (AXES.md §1) — piecewise 1943–74 1×, 1974–2006 1.5×, 2006–17 3×, 2017–present 6×; pre-1943 log
_now = datetime.date.today()
PRESENT = _now.year + (_now.month - 1) / 12          # JS: getFullYear() + getMonth()/12 (getMonth is 0-based)
W, PAD_L, PAD_R, ARCH_W = 1800, 24, 200, 150
SEG = [[1943, 1974, 1], [1974, 2006, 1.5], [2006, 2017, 3], [2017, PRESENT, 6]]
_mainW = W - PAD_L - PAD_R - ARCH_W
_units = sum((b - a) * k for a, b, k in SEG)
PX_PER_UNIT = _mainW / _units
E_COAST = PRESENT - 0.06


def x_main(y):
    x = PAD_L + ARCH_W
    for a, b, k in SEG:
        if y <= a:
            return x
        x += (min(y, b) - a) * k * PX_PER_UNIT
        if y <= b:
            return x
    return x


def x_arch(y):
    d = max(1, 1943 - y)
    t = math.log(d + 1) / math.log(1943 - 1600 + 1)
    return PAD_L + ARCH_W - 14 - t * (ARCH_W - 34)


def X(year):
    return x_main(year) if year >= 1943 else x_arch(year)


BAND_ORDER = ["N1a", "N1b", "N2a", "N2b", "Ca", "Cb", "S1a", "S1b", "S2a", "S2b", "S2c"]   # atlas.html FINE rows, north→south
ISLE_YEARS = [1666, 1847, 1900, 1934]      # atlas.html ISLES authored years (west→east)
MIN_SEP = 6.0                              # plate units between event points (REFACTOR_PLAN §2.7)
INSET = 1.5                                # keep chord points this far inside the polygon edge
BIOME_TINT = {"highland": "#b66b30", "grassland": "#c5a64c", "forest": "#558828", "jungle": "#0f7562",
              "wetland": "#2d7eb7", "harbour": "#af974c", "mixed": "#7155b8"}


def load(name):
    return json.loads((DATA / name).read_text())


def dump(name, fc):
    (DATA / name).write_text(json.dumps(fc, ensure_ascii=False, separators=(",", ":")) + "\n")


def geom_plate(geojson_geom):
    """GeoJSON (lng/lat) → shapely in plate units (x right, y down)."""
    g = shape(geojson_geom)
    from shapely.ops import transform
    return transform(lambda lng, lat, z=None: to_plate(lng, lat), g).buffer(0)


def geom_lnglat(g):
    """shapely plate → GeoJSON geometry in lng/lat (rounded like export_geojson.py)."""
    def ring(coords):
        r = [to_lnglat(x, y) for x, y in coords]
        return r
    if g.geom_type == "Polygon":
        return {"type": "Polygon", "coordinates": [ring(g.exterior.coords)] + [ring(i.coords) for i in g.interiors]}
    return {"type": "MultiPolygon", "coordinates": [[ring(p.exterior.coords)] + [ring(i.coords) for i in p.interiors] for p in g.geoms]}


def clean(g):
    """Drop slivers / lines from a geometry, keep polygonal parts only."""
    g = g.buffer(0)
    if g.is_empty:
        return g
    if g.geom_type == "GeometryCollection":
        g = unary_union([p for p in g.geoms if p.geom_type in ("Polygon", "MultiPolygon")])
    if g.geom_type == "MultiPolygon":
        parts = [p for p in g.geoms if p.area > 0.5]
        g = MultiPolygon(parts) if len(parts) > 1 else (parts[0] if parts else Polygon())
    return g


def band_key(k):
    subs = k.get("sub_band") or []
    return (min((BAND_ORDER.index(s) for s in subs if s in BAND_ORDER), default=99), k["start"], k["id"])


def k_end(k):
    return E_COAST if k["end"] == "present" else float(k["end"])


def k_span(k):
    """Lane x-span of a country = its time_range widened to cover its own events' years (events a few months before
    the registered start / after the end exist in data/; the lane must reach X(year) for them)."""
    yrs = [ev["year"] for ev in k.get("events", [])]
    return min([k["start"]] + yrs), max([k_end(k)] + yrs)


def lane_slice(free, missing):
    """Split `free` among `missing` countries (sorted north→south by band). Returns {id: geometry}."""
    spans = {k["id"]: (X(k_span(k)[0]), X(k_span(k)[1])) for k in missing}
    xs = sorted({x for s in spans.values() for x in s} | {free.bounds[0], free.bounds[2]})
    parts = {k["id"]: [] for k in missing}
    for xa, xb in zip(xs, xs[1:]):
        if xb - xa < 1e-6:
            continue
        active = [k for k in missing if spans[k["id"]][0] <= xa + 1e-6 and spans[k["id"]][1] >= xb - 1e-6]
        if not active:
            continue
        strip = clean(free.intersection(box(xa, -1e9, xb, 1e9)))
        if strip.is_empty:
            continue
        ymin, ymax = strip.bounds[1], strip.bounds[3]
        h = (ymax - ymin) / len(active)
        for i, k in enumerate(active):
            piece = clean(strip.intersection(box(xa, ymin + i * h, xb, ymin + (i + 1) * h)))
            if not piece.is_empty:
                parts[k["id"]].append(piece)
    return {kid: clean(unary_union(ps)) if ps else Polygon() for kid, ps in parts.items()}


def isle_assign(continent, missing):
    """Archipelago: every country gets ≥ 1 whole isle. Pass 1 (narrowest time range first): each country takes the
    unassigned isle nearest its range; pass 2: remaining isles go to the country whose range is nearest their year."""
    isles = sorted(continent.geoms, key=lambda p: p.centroid.x)
    dist = lambda k, yr: max(0, k["start"] - yr, yr - k_end(k))
    out = {k["id"]: [] for k in missing}
    free_idx = list(range(len(isles)))
    for k in sorted(missing, key=lambda k: (k_end(k) - k["start"], k["id"])):
        if not free_idx:
            break
        i = min(free_idx, key=lambda i: (dist(k, ISLE_YEARS[i]), -ISLE_YEARS[i]))
        out[k["id"]].append(isles[i])
        free_idx.remove(i)
    for i in free_idx:
        best = min(missing, key=lambda k: (dist(k, ISLE_YEARS[i]), k["start"]))
        out[best["id"]].append(isles[i])
    return {kid: clean(unary_union(ps)) if ps else Polygon() for kid, ps in out.items()}


def chord_intervals(poly, x):
    """y-intervals of the vertical chord of `poly` at x, inset by INSET from the top/bottom of each interval."""
    from shapely.geometry import LineString
    line = LineString([(x, poly.bounds[1] - 1), (x, poly.bounds[3] + 1)])
    inter = poly.intersection(line)
    segs = [inter] if inter.geom_type == "LineString" else [g for g in getattr(inter, "geoms", []) if g.geom_type == "LineString"]
    segs = [s for s in segs if not s.is_empty and len(s.coords) >= 2]
    out = []
    for s in segs:
        ys = [c[1] for c in s.coords]
        a, b = min(ys) + INSET, max(ys) - INSET
        if b > a:
            out.append((a, b))
    return out


def h01(s):
    return int(hashlib.sha1(s.encode()).hexdigest()[:8], 16) / 0xFFFFFFFF


def place_event(poly, year, eid, taken):
    """x = X(year) clamped into the polygon's x-extent; y = greedy walk along the vertical chord at x (start fraction
    from a hash of the id, golden-ratio steps). If no chord position is ≥ MIN_SEP from every taken point, x is nudged
    in ±1-unit steps (up to ±2·MIN_SEP) — a point that is distinct beats one that is exactly on the year line.
    Returns (x, y, dx, min_dist)."""
    x0 = X(year)
    bx0, _, bx1, _ = poly.bounds
    xc = min(max(x0, bx0 + INSET), bx1 - INSET)
    f = h01(eid)
    best = None     # (d, x, y)
    offsets = [0] + [s * k for k in range(1, int(2 * MIN_SEP) + 1) for s in (1, -1)]
    for off in offsets:
        x = xc + off
        if x < bx0 + INSET or x > bx1 - INSET:
            continue
        ivs = chord_intervals(poly, x)
        total = sum(b - a for a, b in ivs)
        if total <= 0:
            continue
        for i in range(48):
            t = (f + i * 0.6180339887) % 1.0 * total
            y = None
            for a, b in ivs:
                if t <= b - a:
                    y = a + t
                    break
                t -= b - a
            if y is None:
                y = ivs[-1][1]
            d = min((math.hypot(x - tx, y - ty) for tx, ty in taken), default=1e9)
            if d >= MIN_SEP:
                return x, y, x - x0, d
            if best is None or d > best[0]:
                best = (d, x, y)
    if best is None:
        p = poly.representative_point()
        return p.x, p.y, p.x - x0, 0.0
    d, x, y = best
    return x, y, x - x0, d


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    ent = json.loads((SITE / "entities.json").read_text())
    countries_meta = {k["id"]: k for k in ent["countries"]}
    cont_fc, ctry_fc, lab_fc, ev_fc = load("continents.geojson"), load("countries.geojson"), load("labels.geojson"), load("events.geojson")
    continents = {f["properties"]["id"]: geom_plate(f["geometry"]) for f in cont_fc["features"]}
    # drop what a previous run generated (idempotent)
    ctry_fc["features"] = [f for f in ctry_fc["features"] if f["properties"].get("layout") != "lane"]
    lab_fc["features"] = [f for f in lab_fc["features"] if f["properties"].get("layout") != "lane"]
    existing = {f["properties"]["id"]: geom_plate(f["geometry"]) for f in ctry_fc["features"]}
    next_fid = max(f.get("id") or 0 for fc in (cont_fc, ctry_fc, lab_fc, ev_fc) for f in fc["features"]) + 1
    report = {"generated": [], "overlap_max_units2": 0.0, "outside_max_units2": 0.0, "multipolygon": [], "no_polygon": []}

    # ---- B. missing country polygons, per continent
    spatial = [k for k in ent["countries"] if k.get("spatial")]
    by_parent = {}
    for k in spatial:
        if k["id"] not in existing:
            by_parent.setdefault(k["parent_id"], []).append(k)
    generated = {}
    for cid, missing in sorted(by_parent.items()):
        cont = continents[cid]
        have = [g for kid, g in existing.items() if countries_meta.get(kid, {}).get("parent_id") == cid]
        free = clean(cont.difference(unary_union(have))) if have else cont
        missing.sort(key=band_key)
        polys = isle_assign(cont, missing) if cont.geom_type == "MultiPolygon" and cid == "antecedent-isles" else lane_slice(free, missing)
        for k in missing:
            g = polys[k["id"]]
            if g.is_empty:
                report["no_polygon"].append(k["id"])
                continue
            generated[k["id"]] = g
            if g.geom_type == "MultiPolygon":
                report["multipolygon"].append((k["id"], len(g.geoms)))
            report["generated"].append((k["id"], cid, round(g.area, 1)))
    # ---- gates: containment in continent, zero overlap with every other country of the plate
    all_polys = dict(existing, **generated)
    parent_of = {kid: countries_meta.get(kid, {}).get("parent_id") for kid in all_polys}
    for kid, g in generated.items():
        out = g.difference(continents[parent_of[kid]]).area
        report["outside_max_units2"] = max(report["outside_max_units2"], out)
    ids = sorted(all_polys)
    worst = ("", "", 0.0)
    for i, a_id in enumerate(ids):
        for b_id in ids[i + 1:]:
            if a_id not in generated and b_id not in generated:
                continue      # existing×existing pairs are atlas.html's own seams, judged there
            ga, gb = all_polys[a_id], all_polys[b_id]
            if not ga.intersects(gb):
                continue
            ov = ga.intersection(gb).area
            if ov > worst[2]:
                worst = (a_id, b_id, ov)
    report["overlap_max_units2"] = worst[2]
    report["overlap_worst_pair"] = worst[:2]

    # ---- write countries + labels for the generated ones
    ctry_by_id = {f["properties"]["id"]: f for f in ctry_fc["features"]}
    for kid, g in generated.items():
        meta = countries_meta[kid]
        tint = BIOME_TINT.get(meta.get("biome", "mixed"), "#7c6f8c")
        ctry_fc["features"].append({"type": "Feature", "id": next_fid, "geometry": geom_lnglat(g), "properties": {
            "id": kid, "kind": "country", "name": meta["name"], "parent": meta["parent_id"], "subtitle": meta.get("subtitle", ""),
            "biome": meta.get("biome", "mixed"), "tint": tint, "status": meta.get("status", ""), "start": meta.get("start"), "end": meta.get("end"),
            "area": round(g.area, 1), "layout": "lane"}})
        next_fid += 1
        big = max(g.geoms, key=lambda p: p.area) if g.geom_type == "MultiPolygon" else g
        p = polylabel(big, tolerance=0.5)
        lab_fc["features"].append({"type": "Feature", "id": next_fid, "geometry": {"type": "Point", "coordinates": to_lnglat(p.x, p.y)}, "properties": {
            "id": f"label:{kid}", "kind": "country", "class": "country", "ref": kid, "parent": meta["parent_id"], "name": meta["name"], "subtitle": meta.get("subtitle", ""),
            "tag": meta.get("tag") or "", "hint": meta.get("hint") or "", "span": f"{meta.get('start', '')}–{meta.get('end', '')}", "year": None, "lod": 1,
            "rank": 100 + int(1e5 / max(g.area, 1)), "one_line": meta.get("summary60", ""), "x": round(p.x, 1), "y": round(p.y, 1), "layout": "lane"}})
        next_fid += 1
    ctry_fc["features"].sort(key=lambda f: (f["properties"]["parent"], f["properties"]["id"]))
    for f in lab_fc["features"]:
        f["properties"]["class"] = {"continent": "continent", "ocean": "continent", "country": "country"}.get(f["properties"]["kind"], "fact")

    # ---- C. events: chord placement for everything atlas.html did not place
    year_of = {ev["id"]: ev["year"] for k in ent["countries"] for ev in k.get("events", [])}
    # atlas-placed events that share a point with an earlier atlas-placed event are re-walked too (the later id loses)
    seen_pts, redo = set(), set()
    for f in sorted(ev_fc["features"], key=lambda f: f["properties"]["id"]):
        p = f["properties"]
        if not p.get("placed") or p.get("layout") == "chord":
            continue
        key = (p["x"], p["y"])
        if key in seen_pts:
            redo.add(p["id"])
        seen_pts.add(key)
    fixed = lambda p: p.get("placed") and p["id"] not in redo and p.get("layout") != "chord"
    taken = [(f["properties"]["x"], f["properties"]["y"]) for f in ev_fc["features"] if fixed(f["properties"])]
    moved, dx_over, crowded, outside_ev, no_poly_ev = 0, [], [], [], []
    for f in sorted(ev_fc["features"], key=lambda f: (f["properties"]["year"], f["properties"]["id"])):
        p = f["properties"]
        p["class"] = "landmark"
        if fixed(p):
            continue
        poly = all_polys.get(p["country"])
        if poly is None:
            no_poly_ev.append(p["id"])
            continue
        x, y, dx, d = place_event(poly, year_of.get(p["id"], p["year"]), p["id"], taken)
        taken.append((x, y))
        f["geometry"] = {"type": "Point", "coordinates": to_lnglat(x, y)}
        p["x"], p["y"], p["layout"] = round(x, 1), round(y, 1), "chord"
        p["dx"] = round(dx, 1)
        moved += 1
        if abs(dx) > 0.5:
            dx_over.append((p["id"], round(dx, 1)))
        if d < MIN_SEP:
            crowded.append((p["id"], round(d, 1)))
        if not poly.buffer(0.01).contains(Point(x, y)):
            outside_ev.append(p["id"])
    # no two events on one point (0.1-unit rounding, the deep-link precision)
    seen, dup = {}, []
    for f in ev_fc["features"]:
        key = (f["properties"]["x"], f["properties"]["y"])
        if key in seen:
            dup.append((seen[key], f["properties"]["id"]))
        seen[key] = f["properties"]["id"]
    # events placed by atlas.html: how many sit inside their country polygon (informational)
    inside_prev = sum(1 for f in ev_fc["features"] if f["properties"].get("placed") and f["properties"]["country"] in all_polys
                      and all_polys[f["properties"]["country"]].buffer(0.5).contains(Point(f["properties"]["x"], f["properties"]["y"])))
    n_prev = sum(1 for f in ev_fc["features"] if f["properties"].get("placed"))

    # ---- report
    n_spatial = len(spatial)
    n_poly = sum(1 for k in spatial if k["id"] in all_polys)
    print(f"spatial countries {n_spatial}: with polygon {n_poly} (existing {sum(1 for k in spatial if k['id'] in existing)}, generated {len(generated)}); no polygon: {report['no_polygon']}")
    for kid, cid, area in report["generated"]:
        print(f"  + {kid:34s} in {cid:24s} area {area:8.1f} units²  {'MULTIPOLYGON' if any(m[0] == kid for m in report['multipolygon']) else ''}")
    print(f"containment: max area outside parent continent {report['outside_max_units2']:.6f} units²")
    print(f"overlap (generated × any): max pairwise intersection {report['overlap_max_units2']:.6f} units² {report['overlap_worst_pair'] if report['overlap_max_units2'] > 0 else ''}")
    print(f"events: chord-placed {moved}; |x-X(year)| > 0.5: {len(dx_over)} {dx_over[:12]}; min-sep < {MIN_SEP}: {len(crowded)} {crowded[:8]}; outside polygon: {outside_ev}; no polygon: {no_poly_ev}; duplicate points: {dup}")
    print(f"atlas-placed events inside their country polygon (±0.5): {inside_prev}/{n_prev}")
    ok = (not report["no_polygon"] and report["outside_max_units2"] < 1e-6 and report["overlap_max_units2"] < 1e-6
          and not outside_ev and not no_poly_ev and not dup)
    if a.check:
        print("layout check:", "PASS" if ok else "FAIL")
        sys.exit(0 if ok else 1)
    dump("countries.geojson", ctry_fc)
    dump("labels.geojson", lab_fc)
    dump("events.geojson", ev_fc)
    print(f"wrote countries.geojson ({len(ctry_fc['features'])}), labels.geojson ({len(lab_fc['features'])}), events.geojson ({len(ev_fc['features'])})")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
