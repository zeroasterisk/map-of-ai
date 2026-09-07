#!/usr/bin/env python3
"""Headless layout gate for site/index.html (P2-T1-RENDER v3 precision pass).

Serves site/ locally (or takes --url), renders in headless Chromium (Playwright), then asserts on the
RENDERED geometry (isPointInFill / getBBox on the live SVG — never on the authoring polygons):

  1. landmass gap — for EVERY pair of distinct continents' land paths (no bbox pre-filter): no point of A's
     fill lies inside B's fill, and no point of A's fill lies within GAP px of B's fill. Implemented by
     sampling every 1 px over A's bbox and testing B with a temporary stroke of 2*GAP px (isPointInStroke).
     The closest approach per pair is also reported (min over samples of distance-to-B, binary searched).
  2. label vs label — no two continents' text bboxes come within LABEL_GAP px of each other.
  3. label vs land — inside labels: the whole text bbox (with INSIDE_MARGIN) is inside the OWN fill;
     every label (inside or outside): no text bbox (with LABEL_GAP) touches a FOREIGN land fill.
  4. leader lines — every outside label has a leader whose land end is inside the owning fill and whose
     text end is not inside any land fill.
  5. font floor — no label text has font-size < MIN_FONT; no label carries data-unfit.
  6. ruler numerals — adjacent tick labels have >= RULER_GAP px of clear space (bboxes measured).

Writes a screenshot. Usage:
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

GAP = 12          # px of sea required between two different landmasses (rendered fills)
LABEL_GAP = 6     # px between label boxes / between a label and a foreign coast
INSIDE_MARGIN = 5 # px of own land required around an inside label
MIN_FONT = 12     # px floor for any label glyph
RULER_GAP = 6     # px between adjacent ruler numerals
BUILD_MARKER = "P2-T1-RENDER v3"

JS = r"""
(cfg) => {
  const {GAP, LABEL_GAP, INSIDE_MARGIN, MIN_FONT, RULER_GAP} = cfg;
  const svg = document.getElementById('map');
  const pt = svg.createSVGPoint();
  const conts = [...document.querySelectorAll('#shapes .continent')].map(g => ({
    id: g.dataset.id, lands: [...g.querySelectorAll('path.land')] }));
  const bb = e => { const b = e.getBBox(); return {x: b.x, y: b.y, r: b.x + b.width, b: b.y + b.height}; };
  const grow = (b, m) => ({x: b.x - m, y: b.y - m, r: b.r + m, b: b.b + m});
  const inter = (a, b) => a.x < b.r && b.x < a.r && a.y < b.b && b.y < a.b;
  const inFill = (p, x, y) => { pt.x = x; pt.y = y; return p.isPointInFill(pt); };
  const inStroke = (p, x, y) => { pt.x = x; pt.y = y; return p.isPointInStroke(pt); };
  const allLands = conts.flatMap(c => c.lands.map(l => ({id: c.id, el: l})));

  // 1. landmass gap, every pair, sampled on A's fill at 1px, B stroked 2*GAP
  const fillOverlaps = [], gapViolations = [], closest = [];
  for (let i = 0; i < allLands.length; i++) for (let j = 0; j < allLands.length; j++) {
    if (i === j) continue;
    const A = allLands[i], B = allLands[j]; if (A.id === B.id) continue;
    if (j < i && A.id !== B.id) { /* still test both directions: A-samples vs B-stroke is not symmetric */ }
    const a = bb(A.el);
    const savedW = B.el.style.strokeWidth, savedF = B.el.style.filter; B.el.style.strokeWidth = (2 * GAP) + 'px'; B.el.style.filter = 'none';
    let both = 0, near = 0, minD = Infinity;
    for (let x = Math.floor(a.x); x <= a.r; x += 1) for (let y = Math.floor(a.y); y <= a.b; y += 1) {
      if (!inFill(A.el, x, y)) continue;
      if (inFill(B.el, x, y)) { both++; minD = 0; continue; }
      if (inStroke(B.el, x, y)) near++;
    }
    B.el.style.strokeWidth = savedW; B.el.style.filter = savedF;
    if (both) fillOverlaps.push({a: A.id, b: B.id, px: both});
    if (near) gapViolations.push({a: A.id, b: B.id, px: near});
    if (i < j) {
      // closest approach (px), by widening B's stroke until any A-fill sample touches it (coarse 2px grid, 1px steps)
      let d = 0;
      const bB = bb(B.el);
      if (inter(grow(a, 60), bB)) {
        B.el.style.filter = 'none';
        for (d = 1; d <= 60; d++) {
          B.el.style.strokeWidth = (2 * d) + 'px'; let hit = false;
          const x0 = Math.max(a.x, bB.x - d), x1 = Math.min(a.r, bB.r + d), y0 = Math.max(a.y, bB.y - d), y1 = Math.min(a.b, bB.b + d);
          for (let x = Math.floor(x0); x <= x1 && !hit; x += 1) for (let y = Math.floor(y0); y <= y1; y += 1) if (inFill(A.el, x, y) && (inStroke(B.el, x, y) || inFill(B.el, x, y))) { hit = true; break; }
          if (hit) break;
        }
        B.el.style.strokeWidth = savedW; B.el.style.filter = savedF;
        closest.push({a: A.id, b: B.id, px: both ? 0 : d > 60 ? '>60' : d});
      }
    }
  }
  // 2. labels vs labels
  const texts = [...document.querySelectorAll('#labels text')];
  const groups = {};
  texts.forEach(t => (groups[t.dataset.for] = groups[t.dataset.for] || []).push(t));
  const labelOverlaps = [];
  const ids = Object.keys(groups);
  for (let i = 0; i < ids.length; i++) for (let j = i + 1; j < ids.length; j++)
    for (const ta of groups[ids[i]]) for (const tb of groups[ids[j]]) if (inter(grow(bb(ta), LABEL_GAP), bb(tb))) labelOverlaps.push([ids[i], ids[j], ta.textContent, tb.textContent]);
  // 3. labels vs land
  const outside = [], foreign = [];
  const boxEdge = (b, step, fn) => { for (let x = b.x; x <= b.r; x += step) { if (fn(x, b.y) || fn(x, b.b)) return true; } for (let y = b.y; y <= b.b; y += step) { if (fn(b.x, y) || fn(b.r, y)) return true; } return false; };
  const boxAny = (b, step, fn) => { for (let x = b.x; x <= b.r; x += step) for (let y = b.y; y <= b.b; y += step) if (fn(x, y)) return true; return fn(b.r, b.b); };
  const insideIds = new Set([...document.querySelectorAll('#labels text')].filter(t => !document.querySelector(`#leaders [data-for="${t.dataset.for}"]`)).map(t => t.dataset.for));
  for (const c of conts) {
    for (const t of groups[c.id] || []) {
      const b = bb(t);
      if (c.lands.length === 1 && insideIds.has(c.id)) {
        const g = grow(b, INSIDE_MARGIN);
        if (boxEdge(g, 2, (x, y) => !inFill(c.lands[0], x, y))) outside.push({id: c.id, text: t.textContent});
      }
      for (const L of allLands) if (L.id !== c.id && boxAny(grow(b, LABEL_GAP), 2, (x, y) => inFill(L.el, x, y))) foreign.push({label: c.id, text: t.textContent, land: L.id});
    }
  }
  // 4. leaders
  const leaderProblems = [];
  for (const p of document.querySelectorAll('#leaders path.leader')) {
    const id = p.dataset.for; const own = conts.find(c => c.id === id);
    const L = p.getTotalLength(); const s = p.getPointAtLength(0), e = p.getPointAtLength(L);
    // one end must be on the owning land (the dot), the other end in open sea (the text side)
    const sOwn = own.lands.some(l => inFill(l, s.x, s.y)), eOwn = own.lands.some(l => inFill(l, e.x, e.y));
    const sLand = allLands.some(l => inFill(l.el, s.x, s.y)), eLand = allLands.some(l => inFill(l.el, e.x, e.y));
    const startOnOwn = sOwn || eOwn; const endOnLand = sOwn ? eLand : sLand;
    // the leader may only cross its OWN land (near the dot); never a foreign fill
    let crossesForeign = false;
    for (let k = 0; k <= L; k += 2) { const q = p.getPointAtLength(k); if (allLands.some(l => l.id !== id && inFill(l.el, q.x, q.y))) { crossesForeign = true; break; } }
    if (!startOnOwn || endOnLand || crossesForeign || L < 14) leaderProblems.push({id, startOnOwn, endOnLand, crossesForeign, length: +L.toFixed(1)});
  }
  // 5. font floor
  const smallFonts = texts.filter(t => parseFloat(t.getAttribute('font-size')) < MIN_FONT - 1e-6 || t.dataset.unfit).map(t => ({id: t.dataset.for, text: t.textContent, size: t.getAttribute('font-size'), unfit: !!t.dataset.unfit}));
  // 6. ruler numerals
  const nums = [...document.querySelectorAll('#ruler-nums text')].map(t => ({y: t.textContent, b: bb(t)})).sort((a, b) => a.b.x - b.b.x);
  const rulerGaps = []; const rulerClashes = [];
  for (let i = 1; i < nums.length; i++) { const g = nums[i].b.x - nums[i - 1].b.r; rulerGaps.push([nums[i - 1].y, nums[i].y, +g.toFixed(1)]); if (g < RULER_GAP) rulerClashes.push([nums[i - 1].y, nums[i].y, +g.toFixed(1)]); }
  const vb = svg.viewBox.baseVal;
  return {continents: conts.length, labels: texts.length, lands: allLands.length, fillOverlaps, gapViolations, closest, labelOverlaps, outside, foreign, leaderProblems, smallFonts, rulerGaps, rulerClashes, viewBox: [vb.width, vb.height]};
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
    ap.add_argument("--width", type=int, default=1800)
    a = ap.parse_args()
    url = a.url
    httpd = None
    if not url:
        httpd = serve(Path(__file__).resolve().parent, a.port)
        url = f"http://127.0.0.1:{a.port}/"
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": a.width, "height": 900})
        pg.goto(url, wait_until="networkidle")
        pg.wait_for_selector("#shapes .continent")
        pg.evaluate("document.fonts.ready")
        pg.wait_for_timeout(800)
        res = pg.evaluate(JS, dict(GAP=GAP, LABEL_GAP=LABEL_GAP, INSIDE_MARGIN=INSIDE_MARGIN, MIN_FONT=MIN_FONT, RULER_GAP=RULER_GAP))
        pg.screenshot(path=a.shot, full_page=True)
        html = pg.content()
        b.close()
    if httpd:
        httpd.shutdown()
    for k in ("continents", "labels", "lands", "viewBox"):
        print(f"{k}: {res[k]}")
    print(f"closest approach per neighbouring pair (px; require >= {GAP}): {json.dumps(res['closest'])}")
    print(f"ruler numeral gaps (px; require >= {RULER_GAP}): {json.dumps(res['rulerGaps'])}")
    fails = ("fillOverlaps", "gapViolations", "labelOverlaps", "outside", "foreign", "leaderProblems", "smallFonts", "rulerClashes")
    for k in fails:
        print(f"{k} ({len(res[k])}): {json.dumps(res[k], ensure_ascii=False)}")
    ok = res["continents"] == 10 and res["lands"] == 13 and all(not res[k] for k in fails) and BUILD_MARKER in html
    print("screenshot:", a.shot)
    print("build marker present:", BUILD_MARKER in html)
    print("RESULT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
