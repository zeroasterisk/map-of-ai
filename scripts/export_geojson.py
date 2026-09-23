#!/usr/bin/env python3
"""
scripts/export_geojson.py — Phase 4a: export the atlas.html renderer's geometry + entities as GeoJSON for the
MapLibre v2 renderer (site/v2/).

Outputs (all in site/v2/data/):
  continents.geojson  10 continent land polygons (MultiPolygon for the Antecedent Isles) + label anchors
  countries.geojson   36 spatial country polygons (fineTrace lanes from the live DOM)
  labels.geojson      point features for continent / country / ocean labels (anchor = atlas.html's own label position
                      when it has one, else anchors.json fill centroid)
  events.geojson      304 dated events (kind=event) at the plate x/y atlas.html placed their dot (lod4 layout), or
                      x=X(year) at the country centroid for the few atlas.html could not place
  range.geojson       Silicon Range summits (kind=summit) and passes (kind=pass) at their cairn / col-mark plate
                      positions, plus the range title (kind=range)

Geometry source is the LIVE renderer: atlas.html?tilesrc=1&lod=4 is loaded in headless Chromium (Playwright,
Google Fonts blocked so the run is offline and deterministic) and the polygon `d` strings, event dots, cairns and
pass marks are read from the DOM. SVG paths are M/L(/Z) polylines except the isles (cubic Béziers), which are
flattened with 8 segments per curve. Nothing is invented: names, years, one_lines, lods come from
site/entities.json (built from data/ by build_entities_json.py).

Coordinate mapping (REFACTOR_PLAN §3.2, concrete choice — plate units → MapLibre lng/lat):
    lng = (x - 900) / 50           x in [0, 1800]  →  lng in [-18, 18]
    lat = -(y - 525) / 50          y in [0, 1050]  →  lat in [-10.5, 10.5]   (y grows down, lat grows up)
so 1 plate unit = 0.02°. The plate sits in a box centred on the equator: Web-Mercator vertical stretch is
1/cos(lat) = 1.017 at the plate's top/bottom edge (|lat| 10.5°) and ≤ 1.008 over the land band (y 330–890), i.e.
< 1 % anisotropy where anything is drawn — negligible for placement/density. The inverse is used by
site/v2/index.html for the ?x=&y= deep links and by tests/sample_frames.py --target v2.
Scale: at MapLibre zoom z, 1° of longitude = 512·2^z/360 CSS px, so 1 plate unit (0.02°) = 0.028444·2^z px:
    z 3.0 → 0.228 px/unit · z 4.5 → 0.644 · z 6.0 → 1.82 · z 7.5 → 5.15 · z 8.5 → 10.3.
This is exactly the ratio §2.4 assumes (z0 "whole 1800-unit plate fits in 412 px", z1 ≈ 636 units wide), so the
semantic zoom numbers 3.0 / 4.5 / 6.0 / 7.5 are used as MapLibre zooms 1:1 — no offset. Footprints on a 412×892
phone: z0 ≈ 1810×3920 plate units, z1 ≈ 640×1385, z2 ≈ 226×490, z3 ≈ 80×173; overzoom cap 8.5 ≈ 40×87.

Each feature carries: id, kind (continent|country|event|summit|pass|ocean|range), name, year, lod, rank, one_line
and, for polygons, biome + palette tint. rank = symbol-sort-key (lower wins placement).

Usage:  PLAYWRIGHT_BROWSERS_PATH=… LD_LIBRARY_PATH=… /home/node/agent/venvs/mapai/bin/python scripts/export_geojson.py [--port 8996]
"""
import argparse
import json
import re
import sys
import threading
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SITE = REPO / "site"
OUT = SITE / "v2" / "data"

PLATE_W, PLATE_H = 1800, 1050
X0, Y0, UNITS_PER_DEG = 900.0, 525.0, 50.0
LAT_SCALE = 1.8     # Phase 4c task E: vertical exaggeration of the land band for the v2 export (portrait framing); the
                    # renderer inverts it (site/v2/index.html toPlate) so ?x=&y= deep links still round-trip


def to_lnglat(x, y):
    return [round((x - X0) / UNITS_PER_DEG, 5), round(-(y - Y0) * LAT_SCALE / UNITS_PER_DEG, 5)]


# atlas.html BIOME tints (v11) — same palette as the SVG wash / legend swatches
BIOME_TINT = {
    "highland": "#b66b30", "grassland": "#c5a64c", "forest": "#558828", "jungle": "#0f7562",
    "wetland": "#2d7eb7", "harbour": "#af974c", "mixed": "#7155b8",
}

_NUM = re.compile(r"[-+]?(?:\d+\.\d*|\.\d+|\d+)(?:[eE][-+]?\d+)?")


def parse_path(d, curve_segments=8):
    """Parse an SVG path (M/L/C/Q/Z, absolute) into a list of rings [[x, y], …]. Curves are flattened."""
    rings, cur, pos = [], [], None
    tokens = re.findall(r"[MLCQZmlcqz]|" + _NUM.pattern, d)
    i, cmd = 0, None
    while i < len(tokens):
        t = tokens[i]
        if t in "MLCQZmlcqz":
            cmd = t
            i += 1
            if cmd in "Zz":
                if cur:
                    rings.append(cur)
                    pos = cur[0]
                    cur = []
                continue
        else:
            if cmd is None:
                i += 1
                continue
        if cmd in "Mm":
            x, y = float(tokens[i]), float(tokens[i + 1])
            i += 2
            if cur:
                rings.append(cur)
            cur = [[x, y]]
            pos = [x, y]
            cmd = "L"  # implicit lineto after moveto
        elif cmd in "Ll":
            x, y = float(tokens[i]), float(tokens[i + 1])
            i += 2
            cur.append([x, y])
            pos = [x, y]
        elif cmd in "Cc":
            p1 = [float(tokens[i]), float(tokens[i + 1])]
            p2 = [float(tokens[i + 2]), float(tokens[i + 3])]
            p3 = [float(tokens[i + 4]), float(tokens[i + 5])]
            i += 6
            for k in range(1, curve_segments + 1):
                s = k / curve_segments
                u = 1 - s
                cur.append([u ** 3 * pos[0] + 3 * u * u * s * p1[0] + 3 * u * s * s * p2[0] + s ** 3 * p3[0],
                            u ** 3 * pos[1] + 3 * u * u * s * p1[1] + 3 * u * s * s * p2[1] + s ** 3 * p3[1]])
            pos = p3
        elif cmd in "Qq":
            p1 = [float(tokens[i]), float(tokens[i + 1])]
            p2 = [float(tokens[i + 2]), float(tokens[i + 3])]
            i += 4
            for k in range(1, curve_segments + 1):
                s = k / curve_segments
                u = 1 - s
                cur.append([u * u * pos[0] + 2 * u * s * p1[0] + s * s * p2[0],
                            u * u * pos[1] + 2 * u * s * p1[1] + s * s * p2[1]])
            pos = p2
        else:
            i += 1
    if cur:
        rings.append(cur)
    out = []
    for r in rings:
        if len(r) < 3:
            continue
        if r[0] != r[-1]:
            r = r + [r[0]]
        out.append(r)
    return out


def rings_to_geometry(rings):
    """Rings from one `d` → Polygon / MultiPolygon in lng/lat. Each ring is treated as its own outer ring (the
    renderer's polyPath loops are disjoint outers; holes do not occur in this plate)."""
    polys = [[[to_lnglat(x, y) for x, y in r]] for r in rings]
    if len(polys) == 1:
        return {"type": "Polygon", "coordinates": polys[0]}
    return {"type": "MultiPolygon", "coordinates": polys}


def ring_area_centroid(r):
    a = cx = cy = 0.0
    for (x1, y1), (x2, y2) in zip(r, r[1:]):
        c = x1 * y2 - x2 * y1
        a += c
        cx += (x1 + x2) * c
        cy += (y1 + y2) * c
    if abs(a) < 1e-9:
        return 0.0, r[0][0], r[0][1]
    return abs(a) / 2, cx / (3 * a), cy / (3 * a)


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *a, **k):
        pass


DOM_JS = r"""() => {
  const q = s => [...document.querySelectorAll(s)];
  const num = v => +v;
  const out = {continents: [], countries: [], events: {}, cairns: [], passMarks: [], thrTitle: null, ocean: [], clabels: {}, klabels: {}, X: {}};
  for (const g of q('#shapes .continent')) out.continents.push({id: g.dataset.id, d: q(`#shapes .continent[data-id="${g.dataset.id}"] path.land`).map(p => p.getAttribute('d'))});
  for (const g of q('#countries .country')) out.countries.push({id: g.dataset.id, parent: g.dataset.parent, d: g.querySelector('path.cland').getAttribute('d')});
  for (const c of q('#kevents4 .kev-dot')) out.events[c.dataset.ev] = {x: num(c.getAttribute('cx')), y: num(c.getAttribute('cy')), country: c.dataset.for};
  for (const p of q('#threads .thr-cairn')) { const m = /M([\d.]+),([\d.]+)/.exec(p.getAttribute('d')); out.cairns.push([+m[1], +m[2]]); }
  for (const p of q('#threads .thr-pass-mark')) { const m = /M([\d.]+),([\d.]+)/.exec(p.getAttribute('d')); out.passMarks.push([+m[1] + 1.4, +m[2] + 2.2]); }
  const tt = document.querySelector('#thread-labels .thr-title'); if (tt) out.thrTitle = {x: num(tt.getAttribute('x')), y: num(tt.getAttribute('y')), s: tt.textContent};
  for (const t of q('.ocean-label')) out.ocean.push({s: t.textContent, x: num(t.getAttribute('x')), y: num(t.getAttribute('y'))});
  for (const t of q('#labels text')) { const f = t.dataset.for; if (!f) continue; (out.clabels[f] = out.clabels[f] || []).push({x: num(t.getAttribute('x')), y: num(t.getAttribute('y')), s: t.textContent, cls: t.getAttribute('class')}); }
  for (const t of q('#klabels text')) { const f = t.dataset.for; if (!f) continue; (out.klabels[f] = out.klabels[f] || []).push({x: num(t.getAttribute('x')), y: num(t.getAttribute('y')), s: t.textContent, cls: t.getAttribute('class')}); }
  const ENT = window.ENTITIES; const T = ENT.threads[0];
  out.milestoneX = T.milestones.map(m => ({name: m.name, x: m._x !== undefined ? m._x : X(m.year), top: m._top, by: m._by}));   // m._x = summit x after the east-coast clamp (atlas.html MX)
  out.passX = (T.passes || []).map(p => ({name: p.name, x: X(p.year)}));
  for (const k of ENT.countries) for (const e of (k.events || [])) out.X[e.id] = X(e.year);
  return out;
}"""


def dump_dom(port):
    from playwright.sync_api import sync_playwright
    httpd = ThreadingHTTPServer(("127.0.0.1", port), partial(QuietHandler, directory=str(SITE)))
    httpd.daemon_threads = True
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    try:
        with sync_playwright() as p:
            b = p.chromium.launch()
            pg = b.new_page(viewport={"width": PLATE_W, "height": PLATE_H})
            pg.route(re.compile(r"^https?://(?!127\.0\.0\.1)"), lambda r: r.abort())   # offline: no Google Fonts
            pg.goto(f"http://127.0.0.1:{port}/atlas.html?tilesrc=1&lod=4", wait_until="networkidle")
            # poll with evaluate: rAF-driven waits (wait_for_selector / wait_for_function) stall on this heavy SVG page
            # under SwiftShader (frames take seconds), while plain evaluate returns immediately
            import time as _t
            t0 = _t.time()
            while pg.evaluate("document.querySelectorAll('#kevents4 .kev-dot').length") == 0:
                if _t.time() - t0 > 60:
                    raise RuntimeError("atlas.html did not render #kevents4 .kev-dot within 60 s")
                pg.wait_for_timeout(500)
            pg.wait_for_timeout(800)
            dom = pg.evaluate(DOM_JS)
            b.close()
    finally:
        httpd.shutdown()
    return dom


def feat(geom, **props):
    return {"type": "Feature", "id": props.get("_fid"), "geometry": geom, "properties": {k: v for k, v in props.items() if k != "_fid"}}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8996)
    a = ap.parse_args()
    ent = json.loads((SITE / "entities.json").read_text())
    registry = {c["id"]: c for c in json.loads((SITE / "registry.json").read_text())["continents"]}   # all 10 continents (entities.json carries only the 6 with data/ yamls)
    anchors = json.loads((SITE / "anchors.json").read_text())["anchors"]
    dom = dump_dom(a.port)
    OUT.mkdir(parents=True, exist_ok=True)
    fid = [0]

    def nid():
        fid[0] += 1
        return fid[0]

    cont_by_id = {cid: dict(registry[cid], **{k: v for k, v in next((c for c in ent["continents"] if c["id"] == cid), {}).items() if v not in (None, "None", "")}) for cid in registry}
    ctry_by_id = {k["id"]: k for k in ent["countries"]}
    # ---- continents (labels.json is the frozen copy of the same `d`; the DOM is authoritative for the isles' 4 paths)
    continents, labels = [], []
    lands_frozen = {l["id"]: l["d"] for l in json.loads((SITE / "labels.json").read_text())["lands"]}
    for c in dom["continents"]:
        rings = [r for d in c["d"] for r in parse_path(d)]
        if c["id"] in lands_frozen and len(c["d"]) == 1 and lands_frozen[c["id"]] != c["d"][0]:
            print(f"warn: {c['id']} DOM path differs from labels.json (using DOM)", file=sys.stderr)
        meta = cont_by_id.get(c["id"], {})
        area = sum(ring_area_centroid(r)[0] for r in rings)
        continents.append(feat(rings_to_geometry(rings), _fid=nid(), id=c["id"], kind="continent", name=meta.get("name", c["id"]),
                               subtitle=meta.get("subtitle", ""), biome=meta.get("biome", "mixed"), tint=BIOME_TINT.get(meta.get("biome", "mixed"), "#7c6f8c"),
                               start=meta.get("start"), end=meta.get("end"), area=round(area, 1)))
    # continent label anchor = fill centroid (anchors.json, the same rule atlas.html uses for inside labels; the SVG's
    # outside-with-leader labels have no MapLibre equivalent). rank = area order (largest first).
    for i, f in enumerate(sorted(continents, key=lambda f: -f["properties"]["area"])):
        c, meta = f["properties"], cont_by_id.get(f["properties"]["id"], {})
        an = anchors.get(c["id"], {})
        lx, ly = an.get("x", 0), an.get("y", 0)
        labels.append(feat({"type": "Point", "coordinates": to_lnglat(lx, ly)}, _fid=nid(), id=f"label:{c['id']}", kind="continent", ref=c["id"],
                           name=meta.get("name", c["id"]), subtitle=meta.get("subtitle", ""), span=f"{meta.get('start', '')}–{meta.get('end', '')}",
                           year=None, lod=0, rank=10 + i, one_line=meta.get("summary60", ""), x=round(lx, 1), y=round(ly, 1)))
    # ---- countries
    countries = []
    country_centroid = {}
    for k in dom["countries"]:
        rings = parse_path(k["d"])
        meta = ctry_by_id.get(k["id"], {})
        big = max(rings, key=lambda r: ring_area_centroid(r)[0])
        area, cx, cy = ring_area_centroid(big)
        country_centroid[k["id"]] = (cx, cy)
        countries.append(feat(rings_to_geometry(rings), _fid=nid(), id=k["id"], kind="country", name=meta.get("name", k["id"]), parent=k["parent"],
                              subtitle=meta.get("subtitle", ""), biome=meta.get("biome", "mixed"), tint=BIOME_TINT.get(meta.get("biome", "mixed"), "#7c6f8c"),
                              status=meta.get("status", ""), start=meta.get("start"), end=meta.get("end"), area=round(area, 1)))
        rows = [r for r in dom["klabels"].get(k["id"], []) if r["cls"] == "kname"]
        if rows:
            lx = sum(r["x"] for r in rows) / len(rows)
            ly = sum(r["y"] for r in rows) / len(rows) - 1
        else:
            an = anchors.get(k["id"], {})
            lx, ly = an.get("x", cx), an.get("y", cy)
        labels.append(feat({"type": "Point", "coordinates": to_lnglat(lx, ly)}, _fid=nid(), id=f"label:{k['id']}", kind="country", ref=k["id"], parent=k["parent"],
                           name=meta.get("name", k["id"]), subtitle=meta.get("subtitle", ""), tag=meta.get("tag") or "", hint=meta.get("hint") or "",
                           span=f"{meta.get('start', '')}–{meta.get('end', '')}", year=None, lod=1, rank=100 + int(1e5 / max(area, 1)),
                           one_line=meta.get("summary60", ""), x=round(lx, 1), y=round(ly, 1)))
    # ---- ocean labels (two two-line blocks in atlas.html → one feature each)
    oc = dom["ocean"]
    blocks = {}
    for o in oc:
        blocks.setdefault(round(o["x"]), []).append(o)
    for bx, rows in blocks.items():
        name = " ".join(r["s"] for r in rows)
        ly = sum(r["y"] for r in rows) / len(rows) - 4
        labels.append(feat({"type": "Point", "coordinates": to_lnglat(rows[0]["x"], ly)}, _fid=nid(), id=f"ocean:{name.lower().replace(' ', '-')}", kind="ocean",
                           name=name, year=None, lod=0, rank=5, one_line="", x=rows[0]["x"], y=round(ly, 1)))
    # ---- events
    events, unplaced = [], []
    for k in ent["countries"]:
        for e in k.get("events", []):
            pos = dom["events"].get(e["id"])
            if pos:
                x, y, placed = pos["x"], pos["y"], True
            else:
                cx, cy = country_centroid.get(k["id"], (dom["X"][e["id"]], 0))
                x, y, placed = dom["X"][e["id"]], cy, False
                unplaced.append(e["id"])
            lod = int(e.get("lod", 4))
            rank = 1000 * lod + int((e["year"] - 1940) * 2)   # headline (lod 3) before artefact (lod 4); older first within a lod
            events.append(feat({"type": "Point", "coordinates": to_lnglat(x, y)}, _fid=nid(), id=e["id"], kind="event", name=e["name"], year=e["year"],
                               yr=str(int(e["year"])), lod=lod, rank=rank, one_line=e.get("one_line", ""), country=k["id"], parent=k.get("parent_id"),
                               placed=placed, x=round(x, 1), y=round(y, 1)))
    # ---- Silicon Range summits + passes
    T = ent["threads"][0]
    rng = []
    cairns = sorted(dom["cairns"])
    for m in T["milestones"]:
        mx = next((mm["x"] for mm in dom["milestoneX"] if mm["name"] == m["name"]), None)
        cand = min(cairns, key=lambda c: abs(c[0] - mx)) if cairns and mx is not None else None
        if cand and abs(cand[0] - mx) < 3:
            x, y = cand[0], cand[1]
        else:
            x, y = mx, cairns[0][1] if cairns else 600
            print(f"warn: no cairn within 3 units of summit {m['name']} at x={mx}", file=sys.stderr)
        lod = int(m.get("lod", 2))
        rng.append(feat({"type": "Point", "coordinates": to_lnglat(x, y)}, _fid=nid(), id=f"summit:{m['name']}", kind="summit", name=m.get("label") or m["name"],
                        year=m["year"], yr=str(int(m["year"])), lod=lod, rank=500 + 100 * lod + int(2030 - m["year"]), one_line=m.get("one_line", ""),
                        elev=m.get("elev", ""), thread=T["id"], x=round(x, 1), y=round(y, 1)))
    marks = sorted(dom["passMarks"])
    for p in T.get("passes", []):
        px = next((pp["x"] for pp in dom["passX"] if pp["name"] == p["name"]), None)
        cand = min(marks, key=lambda c: abs(c[0] - px)) if marks and px is not None else None
        x, y = (cand if cand and abs(cand[0] - px) < 20 else (px, marks[0][1] if marks else 640))
        rng.append(feat({"type": "Point", "coordinates": to_lnglat(x, y)}, _fid=nid(), id=f"pass:{p['name']}", kind="pass", name=p.get("label") or p["name"],
                        year=p["year"], yr=str(int(p["year"])), lod=3, rank=3000 + int(2030 - p["year"]), one_line=p.get("spec", ""), thread=T["id"],
                        x=round(x, 1), y=round(y, 1)))
    # range title: atlas.html draws `.thr-title` only at lod0 (hidden at lod≥1 by CSS), so the lod4 DOM has none — anchor
    # the title at the ridge line midway along the range (mean of the summit cairns), where the SVG sets it at lod0
    sx = [f["properties"]["x"] for f in rng if f["properties"]["kind"] == "summit"]
    sy = [f["properties"]["y"] for f in rng if f["properties"]["kind"] == "summit"]
    if dom["thrTitle"]:
        tx, ty = dom["thrTitle"]["x"], dom["thrTitle"]["y"] - 3
    else:
        tx, ty = (min(sx) + max(sx)) / 2, sum(sy) / len(sy) + 22
    rng.append(feat({"type": "Point", "coordinates": to_lnglat(tx, ty)}, _fid=nid(), id=f"range:{T['id']}", kind="range",
                    name=(T.get("short_name") or T["name"]).upper(), year=None, lod=0, rank=8, one_line=T.get("subtitle", ""), thread=T["id"],
                    x=round(tx, 1), y=round(ty, 1)))

    def write(name, feats):
        fc = {"type": "FeatureCollection", "generated_by": "scripts/export_geojson.py", "crs_note": "lng=(x-900)/50 lat=-(y-525)*1.8/50 (plate units, 1 unit = 0.02° lng, 0.036° lat; LAT_SCALE 1.8 = Phase 4c task E)",
              "features": feats}
        (OUT / name).write_text(json.dumps(fc, ensure_ascii=False, separators=(",", ":")) + "\n")
        print(f"{name}: {len(feats)} features")

    write("continents.geojson", continents)
    write("countries.geojson", countries)
    write("labels.geojson", labels)
    write("events.geojson", events)
    write("range.geojson", rng)
    if unplaced:
        print(f"events atlas.html could not place at lod4 (exported at X(year) × country centroid): {sorted(set(unplaced))}")
    # glyph coverage: every codepoint used by any label must be inside a generated range (build_glyphs.js)
    used = {ord(ch) for f in labels + events + rng for v in f["properties"].values() if isinstance(v, str) for ch in v}
    ok = lambda cp: cp < 2304 or 8192 <= cp < 8704 or 9472 <= cp < 9728
    bad = sorted(cp for cp in used if not ok(cp))
    if bad:
        print("warn: codepoints outside generated glyph ranges:", [hex(c) + chr(c) for c in bad])


if __name__ == "__main__":
    main()
