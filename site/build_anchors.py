#!/usr/bin/env python3
"""Bake site/anchors.json: one plate-unit anchor point + bbox per continent and country, for ?place=<id> deep links
in index.html. Same geometry and the same fill-centroid rule atlas.html uses to place its labels (a 3-unit sample grid
over the polygon's bbox, keeping points inside the fill), so a ?place= link lands where the label sits.
Usage: PLAYWRIGHT_BROWSERS_PATH=... LD_LIBRARY_PATH=... /tmp/pwvenv/bin/python site/build_anchors.py"""
import json, threading
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from playwright.sync_api import sync_playwright

SITE = Path(__file__).resolve().parent
JS = """() => {
  const svg = document.querySelector('#map svg') || document.querySelector('svg'); const pt = svg.createSVGPoint();
  const cen = p => { const b = p.getBBox(); let sx = 0, sy = 0, n = 0;
    for (let x = b.x; x <= b.x + b.width; x += 3) for (let y = b.y; y <= b.y + b.height; y += 3) { pt.x = x; pt.y = y; if (p.isPointInFill(pt)) { sx += x; sy += y; n++; } }
    const r = v => Math.round(v * 10) / 10;
    return {x: r(n ? sx / n : b.x + b.width / 2), y: r(n ? sy / n : b.y + b.height / 2), bbox: [r(b.x), r(b.y), r(b.x + b.width), r(b.y + b.height)]}; };
  const out = {};
  document.querySelectorAll('#shapes .continent').forEach(g => { const p = g.querySelector('path.land'); if (p) out[g.dataset.id] = Object.assign({level: 'continent'}, cen(p)); });
  document.querySelectorAll('#countries .country').forEach(g => { const p = g.querySelector('.cland'); if (p) out[g.dataset.id] = Object.assign({level: 'country', parent: g.dataset.parent}, cen(p)); });
  return out; }"""

class Quiet(SimpleHTTPRequestHandler):
    def log_message(self, *a, **k): pass
httpd = ThreadingHTTPServer(("127.0.0.1", 8797), partial(Quiet, directory=str(SITE))); httpd.daemon_threads = True
threading.Thread(target=httpd.serve_forever, daemon=True).start()
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1800, "height": 900})
    errs = []; pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.goto("http://127.0.0.1:8797/atlas.html", wait_until="networkidle"); pg.wait_for_selector("#shapes .continent"); pg.wait_for_timeout(800)
    assert not errs, errs
    anchors = pg.evaluate(JS); b.close()
httpd.shutdown()
ent = json.loads((SITE / "entities.json").read_text())
ids = {e["id"] for k in ("continents", "countries") for e in ent[k]}
missing = sorted(ids - set(anchors)); extra = sorted(set(anchors) - ids)
(SITE / "anchors.json").write_text(json.dumps({"plate": [1800, 700], "anchors": anchors}, separators=(",", ":"), sort_keys=True) + "\n")
print(f"anchors.json: {len(anchors)} anchors; in entities.json but not drawn (no ?place= target): {missing}; drawn but not in entities.json: {extra}")
for k, v in sorted(anchors.items()): print(f"  {k:28s} {v['level']:9s} x={v['x']:7.1f} y={v['y']:6.1f} bbox={v['bbox']}")
