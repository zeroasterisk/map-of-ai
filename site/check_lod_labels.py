#!/usr/bin/env python3
"""GATE (LOD pilot): at every lod level the rendered text in atlas.html?tilesrc=1&lod=N has NO overlapping text boxes,
every event dot lies inside its own country's polygon, and every event text box stays inside the plate.
Also prints per-level counts of visible text + events for the Deep Learning Basin (the density evidence).
Run: /tmp/pwvenv/bin/python site/check_lod_labels.py [--zmax 4]  (exit 1 on failure)"""
import argparse, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_tiles import serve, SITE, PLATE

JS = """() => {
  const vis = t => t.getClientRects().length > 0;
  const ts = [...document.querySelectorAll('svg#map text')].filter(vis).filter(t => t.textContent.trim()).filter(t => !/^(band-code|band-label|ocean-label|title|title-sub)$/.test(t.getAttribute('class') || ''));   // legend/ocean stacks are deliberate, pre-existing
  const bb = t => { const b = t.getBBox(); return {x: b.x, y: b.y, r: b.x + b.width, b: b.y + b.height, s: t.textContent, c: t.getAttribute('class'), f: t.dataset.for, e: t.dataset.ev}; };
  const B = ts.map(bb); const ov = [];
  for (let i = 0; i < B.length; i++) for (let j = i + 1; j < B.length; j++) { const a = B[i], b = B[j];
    if (a.e && a.e === b.e) continue; if (a.f && a.f === b.f && !a.e && !b.e) continue;   // lines of one label block
    if (a.x < b.r - .3 && b.x < a.r - .3 && a.y < b.b - .3 && b.y < a.b - .3) ov.push([a.c, a.s, b.c, b.s]); }
  const pt = document.querySelector('svg#map').createSVGPoint();
  const inFill = (p, x, y) => { pt.x = x; pt.y = y; return p.isPointInFill(pt); };
  const dots = [...document.querySelectorAll('.kev-dot')].filter(vis); const bad = [];
  for (const d of dots) { const land = document.querySelector(`.country[data-id="${d.dataset.for}"] path.cland`); if (!inFill(land, +d.getAttribute('cx'), +d.getAttribute('cy'))) bad.push(d.dataset.ev); }
  const W = 1800, H = 700; const out = B.filter(b => b.e && (b.x < 0 || b.r > W || b.y < 0 || b.b > H)).map(b => b.s);
  const count = {}; for (const b of B) count[b.c] = (count[b.c] || 0) + 1;
  const evs = new Set(B.filter(b => b.e).map(b => b.e)).size;
  return {overlaps: ov, dots_outside: bad, off_plate: out, count, events: evs, texts: B.length, curated: window.LOD_CURATED};
}"""

ap = argparse.ArgumentParser(); ap.add_argument("--zmax", type=int, default=4); ap.add_argument("--port", type=int, default=8795); a = ap.parse_args()
from playwright.sync_api import sync_playwright
httpd = serve(SITE, a.port); fails = []; summary = {}
try:
    with sync_playwright() as p:
        b = p.chromium.launch()
        for lod in range(a.zmax + 1):
            pg = b.new_page(viewport={"width": PLATE[0], "height": PLATE[1]}, device_scale_factor=1)
            errs = []; pg.on("pageerror", lambda e: errs.append(str(e)))
            pg.goto(f"http://127.0.0.1:{a.port}/atlas.html?tilesrc=1&lod={lod}", wait_until="networkidle")
            pg.wait_for_selector("#shapes .continent"); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(1200)
            if errs: fails.append(f"lod{lod}: JS errors {errs}")
            r = pg.evaluate(JS); pg.close()
            print(f"lod{lod}: {r['texts']} visible text nodes, {r['events']} events; by class {json.dumps(r['count'])}")
            if r["overlaps"]: fails.append(f"lod{lod}: {len(r['overlaps'])} text overlaps: {r['overlaps'][:6]}")
            if r["dots_outside"]: fails.append(f"lod{lod}: event dots outside their country: {r['dots_outside']}")
            if r["off_plate"]: fails.append(f"lod{lod}: event text off the plate: {r['off_plate']}")
            summary[lod] = {"texts": r["texts"], "events": r["events"], "count": r["count"]}
        print("curated out (did not fit, hover-card only):", json.dumps(r["curated"]))
        b.close()
finally:
    httpd.shutdown()
(SITE.parent / "docs" / "screens" / "lod_labels_summary.json").write_text(json.dumps(summary, indent=1) + "\n")
print("LOD LABEL GATE:", "FAIL\n  " + "\n  ".join(fails) if fails else "PASS")
sys.exit(1 if fails else 0)
