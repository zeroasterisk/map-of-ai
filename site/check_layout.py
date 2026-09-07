#!/usr/bin/env python3
"""Headless layout check for site/index.html (P2-T1-RENDER v2 review gate).

Serves site/ locally, renders it in headless Chromium (Playwright), then asserts:
  1. no two distinct continents' land fills overlap at pixel level (grid-sampled isPointInFill on
     every pair whose bounding boxes intersect), and every pair keeps >= GAP px of sea between them;
  2. no two continents' label text bounding boxes (getBBox) overlap;
  3. every mainland label line sits inside its own continent's land fill.
Also writes a screenshot. Usage:
  PLAYWRIGHT_BROWSERS_PATH=... python3 site/check_layout.py [--url URL] [--shot out.png]
Exit code 0 = all checks pass.
"""
import argparse
import http.server
import json
import sys
import threading
from pathlib import Path

from playwright.sync_api import sync_playwright

GAP = 4  # px of sea required between two different landmasses

JS = r"""
(GAP) => {
  const svg = document.getElementById('map');
  const pt = svg.createSVGPoint();
  const conts = [...document.querySelectorAll('#shapes .continent')].map(g => ({
    id: g.dataset.id, lands: [...g.querySelectorAll('path.land')] }));
  const bb = e => { const b = e.getBBox(); return {x: b.x, y: b.y, r: b.x + b.width, b: b.y + b.height}; };
  const inter = (a, b) => a.x < b.r && b.x < a.r && a.y < b.b && b.y < a.b;
  const inFill = (p, x, y) => { pt.x = x; pt.y = y; return p.isPointInFill(pt); };
  const fillOverlaps = [], gapViolations = [], bboxOverlaps = [];
  for (let i = 0; i < conts.length; i++) for (let j = i + 1; j < conts.length; j++) {
    for (const A of conts[i].lands) for (const B of conts[j].lands) {
      const a = bb(A), b = bb(B);
      if (!inter(a, b)) continue;
      bboxOverlaps.push([conts[i].id, conts[j].id]);
      const x0 = Math.max(a.x, b.x) - GAP, x1 = Math.min(a.r, b.r) + GAP, y0 = Math.max(a.y, b.y) - GAP, y1 = Math.min(a.b, b.b) + GAP;
      let both = 0, near = 0;
      const saved = B.style.strokeWidth; B.style.strokeWidth = (2 * GAP) + 'px';
      for (let x = x0; x <= x1; x += 1) for (let y = y0; y <= y1; y += 1) {
        if (!inFill(A, x, y)) continue;
        if (inFill(B, x, y)) both++;
        else { pt.x = x; pt.y = y; if (B.isPointInStroke(pt)) near++; }
      }
      B.style.strokeWidth = saved;
      if (both) fillOverlaps.push({a: conts[i].id, b: conts[j].id, px: both});
      if (near) gapViolations.push({a: conts[i].id, b: conts[j].id, px: near});
    }
  }
  // labels
  const texts = [...document.querySelectorAll('#labels text')];
  const groups = {};
  texts.forEach(t => (groups[t.dataset.for] = groups[t.dataset.for] || []).push(t));
  const labelOverlaps = [];
  const ids = Object.keys(groups);
  for (let i = 0; i < ids.length; i++) for (let j = i + 1; j < ids.length; j++)
    for (const ta of groups[ids[i]]) for (const tb of groups[ids[j]]) if (inter(bb(ta), bb(tb))) labelOverlaps.push([ids[i], ids[j], ta.textContent, tb.textContent]);
  // label inside own land (mainland only)
  const outside = [];
  for (const c of conts) {
    if (c.lands.length !== 1) continue;
    for (const t of groups[c.id] || []) {
      const b = bb(t); const corners = [[b.x, b.y], [b.r, b.y], [b.x, b.b], [b.r, b.b], [(b.x + b.r) / 2, (b.y + b.b) / 2]];
      const bad = corners.filter(([x, y]) => !inFill(c.lands[0], x, y));
      if (bad.length) outside.push({id: c.id, text: t.textContent, corners_outside: bad.length});
    }
  }
  const vb = svg.viewBox.baseVal;
  // clip cells (structural guarantee; cells may be concave): pixel-sampled — no point inside cell A may lie inside
  // cell B or within GAP px of B's edge. Cells are cloned into the SVG as invisible polygons to use isPointInFill/Stroke.
  const cells = [...document.querySelectorAll('clipPath polygon')].map(p => { const q = p.cloneNode(); q.setAttribute('fill', 'none'); q.setAttribute('stroke', 'none'); svg.appendChild(q); return {id: p.parentNode.id.replace('clip-', ''), el: q, pts: p.getAttribute('points').split(' ').map(s => s.split(',').map(Number))}; });
  const cellClashes = [];
  for (let i = 0; i < cells.length; i++) for (let j = i + 1; j < cells.length; j++) {
    const A = cells[i], B = cells[j];
    const xa = A.pts.map(p => p[0]), ya = A.pts.map(p => p[1]), xb = B.pts.map(p => p[0]), yb = B.pts.map(p => p[1]);
    const box = {x: Math.max(Math.min(...xa), Math.min(...xb)) - GAP, r: Math.min(Math.max(...xa), Math.max(...xb)) + GAP, y: Math.max(Math.min(...ya), Math.min(...yb)) - GAP, b: Math.min(Math.max(...ya), Math.max(...yb)) + GAP};
    if (box.x > box.r || box.y > box.b) continue;
    B.el.style.strokeWidth = (2 * GAP) + 'px'; let bad = 0;
    for (let x = box.x; x <= box.r; x += 1) for (let y = box.y; y <= box.b; y += 1) { pt.x = x; pt.y = y; if (A.el.isPointInFill(pt) && (B.el.isPointInFill(pt) || B.el.isPointInStroke(pt))) bad++; }
    if (bad) cellClashes.push([A.id, B.id, bad]);
  }
  cells.forEach(c => c.el.remove());
  return {continents: conts.length, labels: texts.length, cells: cells.length, cellClashes, bboxOverlaps, fillOverlaps, gapViolations, labelOverlaps, outside, viewBox: [vb.width, vb.height]};
}
"""


def serve(root: Path, port: int):
    handler = lambda *a, **k: http.server.SimpleHTTPRequestHandler(*a, directory=str(root), **k)  # noqa: E731
    httpd = http.server.ThreadingHTTPServer(("127.0.0.1", port), handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", default=None)
    ap.add_argument("--shot", default="/tmp/map-of-ai.png")
    ap.add_argument("--port", type=int, default=8791)
    a = ap.parse_args()
    url = a.url
    httpd = None
    if not url:
        httpd = serve(Path(__file__).resolve().parent, a.port)
        url = f"http://127.0.0.1:{a.port}/"
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1600, "height": 900})
        pg.goto(url, wait_until="networkidle")
        pg.wait_for_selector("#shapes .continent")
        pg.evaluate("document.fonts.ready")
        pg.wait_for_timeout(800)
        res = pg.evaluate(JS, GAP)
        pg.screenshot(path=a.shot, full_page=True)
        html = pg.content()
        b.close()
    if httpd:
        httpd.shutdown()
    for k in ("continents", "labels", "cells", "viewBox"):
        print(f"{k}: {res[k]}")
    for k in ("cellClashes", "bboxOverlaps", "fillOverlaps", "gapViolations", "labelOverlaps", "outside"):
        print(f"{k} ({len(res[k])}): {json.dumps(res[k], ensure_ascii=False)}")
    ok = res["continents"] == 10 and res["cells"] == 9 and not res["cellClashes"] and not res["fillOverlaps"] and not res["gapViolations"] and not res["labelOverlaps"] and not res["outside"]
    print("screenshot:", a.shot)
    print("build marker present:", "P2-T1-RENDER v2" in html)
    print("RESULT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
