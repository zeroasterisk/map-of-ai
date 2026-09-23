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
    atlas.html's FINE rows use). Phase 4c-A: the lanes only decide OWNERSHIP; the drawn borders are a Voronoi partition
    of the free land from seeded jittered hex-grid sites (pitch SITE_PITCH), each site owned by its lane, with ridges
    between different owners displaced by seeded midpoint noise + Chaikin smoothing (organic_slice). Cells tile the
    free land, so containment in the continent and zero overlap with every other country are true by construction;
    both neighbours share each ridge polyline exactly (no gaps). A connectivity pass keeps every country in one piece.
    The Antecedent Isles are an archipelago: whole isles are assigned to the country whose time_range is nearest
    the isle's authored year (a lane cut through a 30-unit islet would make unreadable slivers).
 C. Event placement for events atlas.html could not place at lod4 (exported at X(year) × country centroid, all
    stacked on one point): x = X(year) (clamped into the country polygon when the polygon does not reach that x —
    only happens on the log-compressed isles axis), y = a deterministic greedy non-overlap walk down the polygon's
    vertical chord at that x (start fraction from a hash of the event id, golden-ratio steps, first position ≥ MIN_SEP
    plate units from every other event of the plate wins; otherwise the farthest one). No randomness.
 D. `class` property on point features (landmark / country / continent / fact) for the sampler.
 Phase 4c:
 C'. Display-text dedupe: hint/tag tokens that repeat a same-country event name (or a nearby summit) are dropped from the
    exported label (data/ untouched; hints re-sourced from entities.json each run); an event whose name repeats a
    lower-lod summit within 80 units gets `dedup` and the symbol-event layers hide its text (dot and fact stay).
 F. Lobes: a country whose events need x = X(year) outside its polygon grows an organic lobe (noisy box ∩ continent)
    from same-continent neighbours; donors are never emptied/halved/split/holed, their atlas-placed events are carved
    out. Modified atlas polygons carry `layout: "lobe"` + `geom_atlas` (pristine geometry, restored on re-run).
    Atlas-placed events > 2 units off X(year) whose country now has a chord there are re-walked (chord layout).

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

from shapely.geometry import Point, Polygon, MultiPolygon, LineString, box, mapping, shape
from shapely.ops import unary_union, polylabel

REPO = Path(__file__).resolve().parent.parent
SITE = REPO / "site"
DATA = SITE / "v2" / "data"

# ---- plate ↔ lng/lat (scripts/export_geojson.py)
X0, Y0, UNITS_PER_DEG, LAT_SCALE = 900.0, 525.0, 50.0, 1.8      # LAT_SCALE: Phase 4c task E (export_geojson.py)
to_lnglat = lambda x, y: [round((x - X0) / UNITS_PER_DEG, 5), round(-(y - Y0) * LAT_SCALE / UNITS_PER_DEG, 5)]
to_plate = lambda lng, lat: (lng * UNITS_PER_DEG + X0, -lat * UNITS_PER_DEG / LAT_SCALE + Y0)

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
SITE_PITCH = 20.0                          # Voronoi site pitch (plate units) for organic_slice borders (task 4c-A)
SITE_JITTER = 0.6                          # jitter as a fraction of the pitch
RIDGE_AMP = 3.0                            # max midpoint-displacement amplitude (units) on a Voronoi ridge
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


def noisy_line(p0, p1, amp, seed, min_seg=6.0):
    """Seeded midpoint displacement (roughness 0.5) of the segment p0→p1: perpendicular displacement of the midpoint by
    ±amp, recursing until segments are < min_seg units. Deterministic in (p0, p1, amp, seed). Returns a coordinate list."""
    def h(*parts):
        return int(hashlib.sha1("|".join(str(round(v, 3)) if isinstance(v, float) else str(v) for v in parts).encode()).hexdigest()[:8], 16) / 0xFFFFFFFF
    def rec(a, b, amp, depth):
        dx, dy = b[0] - a[0], b[1] - a[1]
        L = math.hypot(dx, dy)
        if L < min_seg or depth > 8 or amp < 0.15:
            return [b]
        m = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
        d = (h(seed, depth, a, b) * 2 - 1) * amp
        m = (m[0] - dy / L * d, m[1] + dx / L * d)
        return rec(a, m, amp * 0.5, depth + 1) + rec(m, b, amp * 0.5, depth + 1)
    return [p0] + rec(p0, p1, amp, 0)


def chaikin(pts, n=2):
    """Chaikin corner cutting, endpoints fixed (so shared ridge endpoints still meet). n passes."""
    for _ in range(n):
        if len(pts) < 3:
            return pts
        out = [pts[0]]
        for a, b in zip(pts, pts[1:]):
            out.append((0.75 * a[0] + 0.25 * b[0], 0.75 * a[1] + 0.25 * b[1]))
            out.append((0.25 * a[0] + 0.75 * b[0], 0.25 * a[1] + 0.75 * b[1]))
        out.append(pts[-1])
        pts = out
    return pts


def organic_slice(free, missing, seed):
    """Task 4c-A. Same lane topology as lane_slice (x-columns at every X(span) edge, equal horizontal lanes per column,
    north→south by band) but the borders are ORGANIC: a Voronoi partition of the free land from seeded jittered sites.
    Sites are sown on a hex grid (pitch SITE_PITCH units) over the free land; every site belongs to the country whose
    straight lane contains it, so the lane topology (west→east by time, north→south by band) is kept while every shared
    border becomes a polyline of Voronoi edges between jittered sites. Every cell is (voronoi ∩ free), the cells tile
    `free`, so containment in the continent and zero overlap are true by construction and both neighbours of an edge
    share it exactly (no gaps). Noise is sha1(seed, i, j): deterministic. Returns {id: geometry}."""
    from shapely.geometry import MultiPoint, LineString
    from shapely.ops import voronoi_diagram, polygonize
    spans = {k["id"]: (X(k_span(k)[0]), X(k_span(k)[1])) for k in missing}
    x_lo, y_lo, x_hi, y_hi = free.bounds
    xs = sorted({x for s in spans.values() for x in s} | {x_lo, x_hi})
    cols = []            # (xa, xb, active countries, ymin, ymax)
    for xa, xb in zip(xs, xs[1:]):
        if xb - xa < 1e-6:
            continue
        active = [k for k in missing if spans[k["id"]][0] <= xa + 1e-6 and spans[k["id"]][1] >= xb - 1e-6]
        strip = clean(free.intersection(box(xa, -1e9, xb, 1e9)))
        if active and not strip.is_empty:
            cols.append((xa, xb, active, strip.bounds[1], strip.bounds[3]))

    def owner(x, y):
        for xa, xb, active, ymin, ymax in cols:
            if xa - 1e-6 <= x <= xb + 1e-6:
                h = (ymax - ymin) / len(active)
                return active[min(len(active) - 1, max(0, int((y - ymin) // h)))]["id"]
        return None

    pitch = SITE_PITCH
    sites, own = [], []
    rows = int((y_hi - y_lo) / (pitch * 0.866)) + 2
    ncol = int((x_hi - x_lo) / pitch) + 2
    for j in range(rows):
        for i in range(ncol):
            jx = h01(f"{seed}:{i}:{j}:x") - 0.5
            jy = h01(f"{seed}:{i}:{j}:y") - 0.5
            x = x_lo + (i + 0.5 * (j % 2)) * pitch + jx * pitch * SITE_JITTER
            y = y_lo + j * pitch * 0.866 + jy * pitch * SITE_JITTER
            if not free.contains(Point(x, y)):
                continue
            o = owner(x, y)
            if o is None:
                continue
            sites.append((x, y))
            own.append(o)
    # every country gets ≥ 1 site: fall back to the lane's representative point
    for k in missing:
        if k["id"] not in own:
            for xa, xb, active, ymin, ymax in cols:
                if k in active:
                    h = (ymax - ymin) / len(active)
                    i = active.index(k)
                    cell = clean(free.intersection(box(xa, ymin + i * h, xb, ymin + (i + 1) * h)))
                    if not cell.is_empty:
                        p = cell.representative_point()
                        sites.append((p.x, p.y))
                        own.append(k["id"])
                        break
    env = box(x_lo - 50, y_lo - 50, x_hi + 50, y_hi + 50)
    # connectivity pass on the plain cells: a country's sites must form ONE adjacency component; smaller components are
    # relabelled to the neighbouring country they touch most (deterministic order), so no country ends up in two pieces
    cells = list(voronoi_diagram(MultiPoint(sites), envelope=env).geoms)
    cell_of = [Polygon()] * len(sites)
    for cell in cells:
        rp = cell.representative_point()
        idx = min(range(len(sites)), key=lambda n: (sites[n][0] - rp.x) ** 2 + (sites[n][1] - rp.y) ** 2)
        cell_of[idx] = clean(cell.intersection(free))
    adj = {n: set() for n in range(len(sites))}
    for n in range(len(sites)):
        for m in range(n + 1, len(sites)):
            if cell_of[n] is None or cell_of[m] is None or cell_of[n].is_empty or cell_of[m].is_empty:
                continue
            if cell_of[n].intersection(cell_of[m]).length > 0.5:
                adj[n].add(m)
                adj[m].add(n)
    for _ in range(6):
        changed = False
        for kid in sorted({o for o in own}):
            mine = [n for n in range(len(sites)) if own[n] == kid]
            comps, seen = [], set()
            for s in mine:
                if s in seen:
                    continue
                comp, stack = set(), [s]
                while stack:
                    v = stack.pop()
                    if v in comp:
                        continue
                    comp.add(v)
                    stack.extend(w for w in adj[v] if own[w] == kid and w not in comp)
                seen |= comp
                comps.append(comp)
            if len(comps) <= 1:
                continue
            comps.sort(key=lambda c: (-sum(cell_of[n].area for n in c), min(c)))
            for comp in comps[1:]:
                touch = {}
                for n in comp:
                    for w in adj[n]:
                        if own[w] != kid:
                            touch[own[w]] = touch.get(own[w], 0) + cell_of[n].intersection(cell_of[w]).length
                if touch:
                    new_owner = max(sorted(touch), key=lambda o: touch[o])
                    for n in comp:
                        own[n] = new_owner
                    changed = True
        if not changed:
            break
    ridges = voronoi_diagram(MultiPoint(sites), envelope=env, edges=True)
    # ridges between two sites of the SAME country are dropped (no border there); the rest get seeded midpoint noise,
    # keyed by the ridge's own (sorted) endpoints so both neighbours share one polyline
    noisy = []
    tree_pts = sites
    def lines_of(g):
        if g.geom_type == "LineString":
            return [g]
        return [l for sub in getattr(g, "geoms", []) for l in lines_of(sub)]
    for seg in lines_of(ridges):
        c = list(seg.coords)
        for p0, p1 in zip(c, c[1:]):
            m = ((p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2)
            near = sorted(range(len(tree_pts)), key=lambda n: (tree_pts[n][0] - m[0]) ** 2 + (tree_pts[n][1] - m[1]) ** 2)[:2]
            if len(near) == 2 and own[near[0]] == own[near[1]]:
                continue
            a, b = sorted([p0, p1])
            L = math.hypot(b[0] - a[0], b[1] - a[1])
            amp = min(RIDGE_AMP, 0.15 * L)
            pts = noisy_line(a, b, amp, f"{seed}:ridge:{round(a[0], 2)}:{round(a[1], 2)}:{round(b[0], 2)}:{round(b[1], 2)}", min_seg=4.0)
            noisy.append(LineString(chaikin(pts, 3)))
    boundary = [free.boundary] if free.geom_type == "Polygon" else [g.boundary for g in free.geoms]
    faces = list(polygonize(unary_union(boundary + noisy)))
    parts = {k["id"]: [] for k in missing}
    for face in faces:
        rp = face.representative_point()
        if face.area < 1e-6 or not free.buffer(1e-6).contains(rp):
            continue
        idx = min(range(len(sites)), key=lambda n: (sites[n][0] - rp.x) ** 2 + (sites[n][1] - rp.y) ** 2)
        parts[own[idx]].append(face)
    out = {kid: clean(unary_union(ps)) if ps else Polygon() for kid, ps in parts.items()}
    # noise can pinch off a tiny enclave: hand slivers (< 4 % of the country) to the neighbour that touches them most
    for kid, g in list(out.items()):
        if g.geom_type != "MultiPolygon":
            continue
        big = max(g.geoms, key=lambda p: p.area)
        keep = [big]
        for p in g.geoms:
            if p is big:
                continue
            if p.area >= 0.04 * g.area:
                keep.append(p)
                continue
            best = max((o for o in out if o != kid), key=lambda o: out[o].intersection(p.buffer(0.01)).length, default=None)
            if best is not None:
                out[best] = clean(unary_union([out[best], p]))
            else:
                keep.append(p)
        out[kid] = clean(unary_union(keep))
    return out


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


def norm_text(s):
    import re
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def token_matches_event(tok, events, max_lod):
    """True when a hint/tag token names an event of lod ≤ max_lod in the same country: equal after normalisation (years
    stripped from the token), or one contains the other with ≥ 5 chars. 'Winter 1974' vs 'First AI winter' does not
    match (neither contains the other) — only genuine repeats are dropped."""
    import re
    t = norm_text(re.sub(r"\b(1[6-9]|20)\d\d\b", "", tok))
    if len(t) < 3:
        return False
    for e in events:
        if int(e.get("lod", 4)) > max_lod:
            continue
        n = norm_text(e["name"])
        if t == n or (len(t) >= 5 and (t in n or n in t)):
            return True
    return False


def organic_box(x0, y0, x1, y1, seed):
    """A rectangle whose four edges are seeded midpoint-displaced + Chaikin-smoothed curves (task 4c-F lobes): the
    lobe is subtracted from the donor and unioned into the receiver, so both share the identical noisy edge."""
    amp = min(RIDGE_AMP, 0.2 * (y1 - y0), 0.2 * (x1 - x0))
    corners = [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
    ring = []
    for i in range(4):
        a, b = corners[i], corners[(i + 1) % 4]
        ring += chaikin(noisy_line(a, b, amp, f"{seed}:{i}", min_seg=4.0), 2)[:-1]
    return Polygon(ring).buffer(0)


def grow_lobes(all_polys, continents, parent_of, ev_x, prot_pts):
    """Task 4c-F. For every country whose events need an x = X(year) outside the polygon's x-extent, grow a contiguous
    LOBE from the neighbouring land of the same continent: continent ∩ [x_target, edge] ∩ a y-band. Candidate bands
    (deterministic order): the country's own edge chord, then every donor's chord centre at x_target; heights from
    the events' stacking need down to 9 units. A donor keeps its largest piece; slivers it would be cut into go to
    the lobe; a donor is never emptied below 50 % of its area, and its atlas-placed events (± MIN_SEP) are carved out
    of the lobe. The first band whose merged polygon is ONE piece and covers every needed x wins.
    Returns (changed {id: geometry}, log rows)."""
    log, changed = [], {}
    chord_at = lambda g, x: LineString([(x, g.bounds[1] - 1), (x, g.bounds[3] + 1)])
    for kid in sorted(all_polys):
        xs = ev_x.get(kid, [])
        if not xs:
            continue
        for side in ("W", "E"):
            g = all_polys[kid]
            bx0, by0, bx1, by1 = g.bounds
            need = [x for x in xs if (x < bx0 - 0.5 if side == "W" else x > bx1 + 0.5)]
            need = [x for x in need if not g.intersects(chord_at(g, x))]
            if not need:
                continue
            xt = (min(need) - INSET - 1) if side == "W" else (max(need) + INSET + 1)
            cont = continents[parent_of[kid]]
            span = (xt, bx0 + 6) if side == "W" else (bx1 - 6, xt)
            strip = clean(cont.intersection(box(span[0], -1e9, span[1], 1e9)))
            if strip.is_empty:
                log.append((kid, side, round(xt), "no land in continent at that x"))
                continue
            edge = g.intersection(box(bx0, -1e9, bx0 + 8, 1e9) if side == "W" else box(bx1 - 8, -1e9, bx1, 1e9))
            centres = [(edge.bounds[1] + edge.bounds[3]) / 2]
            tline = chord_at(cont, xt)
            for did in sorted(all_polys):
                if did != kid and parent_of.get(did) == parent_of[kid]:
                    ch = all_polys[did].intersection(tline)
                    if not ch.is_empty:
                        centres.append((ch.bounds[1] + ch.bounds[3]) / 2)
            # coastal corridors (a strip hugging the continent's north / south coast never splits an interior donor)
            cch = cont.intersection(tline)
            if not cch.is_empty:
                centres += [cch.bounds[1] + 7.0, cch.bounds[3] - 7.0]
            h0 = max((edge.bounds[3] - edge.bounds[1]) / 2, 9.0, (len(need) * MIN_SEP + 2 * INSET) / 2)
            holes = [Point(px, py).buffer(MIN_SEP) for (px, py, owner) in prot_pts if owner != kid and strip.intersects(Point(px, py))]
            accepted = None
            for yc in centres:
                h = h0
                while h >= 6.0 and accepted is None:
                    lobe = clean(strip.intersection(organic_box(span[0], yc - h, span[1], yc + h, f"{kid}:{side}:{round(yc)}:{round(h, 1)}")))
                    # a band that misses the country's own edge chord gets a NECK along the edge so the union stays one piece
                    ey0, ey1 = edge.bounds[1], edge.bounds[3]
                    if yc + h < ey0 or yc - h > ey1:
                        nx = (bx0 - 14, bx0 + 6) if side == "W" else (bx1 - 6, bx1 + 14)
                        neck = organic_box(nx[0], min(yc - h, ey0 + 4), nx[1], max(yc + h, ey1 - 4), f"{kid}:{side}:neck:{round(yc)}")
                        lobe = clean(unary_union([lobe, clean(strip.intersection(neck))]))
                    if holes and not lobe.is_empty:
                        lobe = clean(lobe.difference(unary_union(holes)))
                    if lobe.is_empty:
                        h *= 0.8
                        continue
                    donors, ok = {}, True
                    for did, dg in all_polys.items():
                        if did == kid or parent_of.get(did) != parent_of[kid] or not dg.intersects(lobe):
                            continue
                        nd = clean(dg.difference(lobe))
                        n_holes = lambda gg: len(gg.interiors) if gg.geom_type == "Polygon" else sum(len(p.interiors) for p in gg.geoms)
                        if nd.is_empty or nd.area < 0.5 * dg.area or n_holes(nd) > n_holes(dg):
                            ok = False          # never empty, halve, or punch a hole through a donor
                            break
                        if nd.geom_type == "MultiPolygon" and dg.geom_type != "MultiPolygon":
                            big = max(nd.geoms, key=lambda p: p.area)
                            slivers = [p for p in nd.geoms if p is not big]
                            if sum(p.area for p in slivers) > 0.1 * dg.area:
                                ok = False
                                break
                            lobe = clean(unary_union([lobe] + slivers))
                            nd = big
                        donors[did] = nd
                    if ok:
                        merged = clean(unary_union([g, lobe]))
                        if merged.geom_type == "Polygon" and all(merged.intersects(chord_at(cont, x)) for x in need):
                            accepted = (merged, donors, lobe)
                    h *= 0.8
                if accepted:
                    break
            if accepted is None:
                log.append((kid, side, round(xt), "no lobe (would split / consume a donor)"))
                continue
            merged, donors, lobe = accepted
            all_polys[kid] = merged
            changed[kid] = merged
            for did, nd in donors.items():
                all_polys[did] = nd
                changed[did] = nd
            log.append((kid, side, round(xt), f"lobe {lobe.area:.0f} u² from {sorted(donors)}"))
    return changed, log


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
    for f in ctry_fc["features"]:                       # 4c-F lobes modify atlas polygons: restore the pristine export first
        if "geom_atlas" in f["properties"]:
            f["geometry"] = f["properties"].pop("geom_atlas")
            f["properties"].pop("layout", None)
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
        polys = isle_assign(cont, missing) if cont.geom_type == "MultiPolygon" and cid == "antecedent-isles" else organic_slice(free, missing, cid)
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
    existing_overlap = {}
    for i, a_id in enumerate(ids):
        for b_id in ids[i + 1:]:
            if a_id in existing and b_id in existing and all_polys[a_id].intersects(all_polys[b_id]):
                existing_overlap[frozenset((a_id, b_id))] = all_polys[a_id].intersection(all_polys[b_id]).area
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

    # ---- F. lobes: every event's X(year) must be inside its country's x-extent (target: 0 events > 2 units off)
    ev_x, prot = {}, []
    for f in ev_fc["features"]:
        p = f["properties"]
        if p["kind"] == "event" and p["country"] in all_polys:
            ev_x.setdefault(p["country"], []).append(X(p["year"]))
            if p.get("placed") and p.get("layout") != "chord":
                prot.append((p["x"], p["y"], p["country"]))
    lobed, lobe_log = grow_lobes(all_polys, continents, parent_of, ev_x, prot)
    for kid in lobed:
        if kid in generated:
            generated[kid] = all_polys[kid]
    # atlas polygons changed by a lobe: write back, keeping the pristine geometry for idempotent re-runs
    for f in ctry_fc["features"]:
        kid = f["properties"]["id"]
        if kid in lobed and kid in existing:
            f["properties"]["geom_atlas"] = f["geometry"]
            f["geometry"] = geom_lnglat(all_polys[kid])
            f["properties"]["layout"] = "lobe"
            f["properties"]["area"] = round(all_polys[kid].area, 1)
    # re-check gates after lobes (containment + overlap over EVERY pair touched by a lobe)
    for kid in lobed:      # a lobe is continent ∩ …, so it can only inherit the atlas polygon's own coastline slop (≤ 0.25 u²)
        before = existing[kid].difference(continents[parent_of[kid]]).area if kid in existing else 0.0
        report["outside_max_units2"] = max(report["outside_max_units2"], all_polys[kid].difference(continents[parent_of[kid]]).area - before)
    for a_id in sorted(lobed):
        for b_id in ids:
            if a_id == b_id or not all_polys[a_id].intersects(all_polys[b_id]):
                continue
            ov = all_polys[a_id].intersection(all_polys[b_id]).area
            if ov > report["overlap_max_units2"] and not (a_id not in generated and b_id not in generated and ov <= existing_overlap.get(frozenset((a_id, b_id)), 0) + 1e-6):
                report["overlap_max_units2"], report["overlap_worst_pair"] = ov, (a_id, b_id)

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
    # 4c-F: atlas-placed events > 2 units off X(year) whose country now has a chord at X(year) are re-walked too
    for f in ev_fc["features"]:
        p = f["properties"]
        if p["kind"] != "event" or not p.get("placed") or p.get("layout") == "chord":
            continue
        poly = all_polys.get(p["country"])
        xx = X(year_of.get(p["id"], p["year"]))
        if poly is not None and abs(p["x"] - xx) > 2 and poly.intersects(LineString([(xx, poly.bounds[1] - 1), (xx, poly.bounds[3] + 1)])):
            redo.add(p["id"])
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

    # ---- 4c-C. dedupe display text: hint/tag tokens that repeat an event name of the same country (the event keeps its
    # label; the hint is display-only). Hints show at z 4.5–6 next to lod ≤ 2 events, tags at z 6–8.5 next to lod ≤ 3
    # events and all events from z 7.5; a token is dropped when it names an event that is visible in that band.
    # The AlexNet summit (range.geojson, lod 1) vs the AlexNet event (lod 3): the summit wins at z < 7.5 (the event
    # is lod 3 so it only appears from z 6); the event keeps its label at z ≥ 6 where the summit label is its
    # neighbour 48 units away — dedupe by dropping the event's name from the hint/tag only (data untouched).
    ev_by_country = {}
    for f in ev_fc["features"]:
        p = f["properties"]
        if p["kind"] == "event":
            ev_by_country.setdefault(p["country"], []).append(p)
    range_fc = load("range.geojson")
    summits = [f["properties"] for f in range_fc["features"] if f["properties"]["kind"] == "summit"]

    def summits_near(kid):
        g = all_polys.get(kid)
        return [s for s in summits if g is not None and g.buffer(40).contains(Point(s["x"], s["y"]))]
    hint_dropped, tag_dropped = [], []
    for f in lab_fc["features"]:
        p = f["properties"]
        if p["kind"] != "country":
            continue
        evs = ev_by_country.get(p["ref"], [])
        meta = countries_meta.get(p["ref"], {})
        for field, max_lod, dropped in (("hint", 2, hint_dropped), ("tag", 3, tag_dropped)):
            raw = meta.get(field) or ""                     # always re-sourced from entities.json (idempotent)
            if not raw:
                continue
            sep = " · " if " · " in raw else (" → " if " → " in raw else "\x00")
            keep = []
            for tok in raw.split(sep):
                if token_matches_event(tok, evs + summits_near(p["ref"]), max_lod):
                    dropped.append((p["ref"], tok.strip()))
                else:
                    keep.append(tok)
            if not keep and field == "hint":                # never blank a hint: keep the first token
                keep = raw.split(sep)[:1]
            p[field] = sep.join(keep)                       # a fully-deduped tag becomes "" (style filter hides it)
    # event whose name repeats a nearby summit's name (range.geojson, e.g. 'AlexNet' event vs 'AlexNet GPUs' summit):
    # the lower lod wins; the loser gets dedup=<winner> and the symbol-event layers filter it out (dot + fact stay)
    ev_dedup = []
    for f in ev_fc["features"]:
        p = f["properties"]
        p.pop("dedup", None)
        if p["kind"] != "event":
            continue
        n = norm_text(p["name"])
        for s in summits:
            ns = norm_text(s["name"])
            if (n == ns or (len(n) >= 5 and n in ns)) and int(s.get("lod", 2)) <= int(p.get("lod", 4)) \
                    and math.hypot(s["x"] - p["x"], s["y"] - p["y"]) < 80:
                p["dedup"] = f"summit:{s['name']}"
                ev_dedup.append((p["id"], s["name"]))
                break
    print(f"dedupe (4c-C): hint tokens dropped {len(hint_dropped)} {hint_dropped[:6]}…; tag tokens dropped {len(tag_dropped)}; "
          f"events deduped against summits {ev_dedup}")

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
    off = [(f["properties"]["id"], round(f["properties"]["x"] - X(f["properties"]["year"]), 1)) for f in ev_fc["features"]
           if f["properties"]["kind"] == "event" and abs(f["properties"]["x"] - X(f["properties"]["year"])) > 2]
    print(f"lobes (4c-F): {len(lobed)} polygons changed; {len(lobe_log)} requests: " + "; ".join(f"{k}/{s}@{x}: {msg}" for k, s, x, msg in lobe_log))
    print(f"events > 2 units off X(year): {len(off)} {off[:10]}")
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
