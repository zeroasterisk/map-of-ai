#!/usr/bin/env python3
"""Headless layout gate for site/index.html (P2-T1-RENDER v4: atlas textures, one supercontinent).

Serves site/ locally (or takes --url), renders in headless Chromium (Playwright), then asserts on the
RENDERED geometry (isPointInFill / getBBox on the live SVG — never on the authoring grid):

  1. contiguity — exactly ONE mainland coastline loop (#coast has 1 + 4 isle paths); every mainland continent
     fill is inside it; every pair of chronologically adjacent continents TOUCHES (fills within ADJ px);
     no pair of continents OVERLAPS (no pixel inside two different fills).
  2. texture — each continent's land fill is a url(#tex-*) pattern (not a flat colour) and the sampled
     luminance inside every continent has stddev >= TEX_STD (i.e. visible glyph texture, not a flat fill).
  3. labels — no two continents' text bboxes come within LABEL_GAP px; no two text elements anywhere overlap; inside labels sit wholly inside their
     own fill; no label touches a foreign fill; every text is inside the viewBox with EDGE px margin.
  4. leaders — outside labels have a leader whose land end is on the owning fill and text end is on no land.
  5. font floor — no label text < MIN_FONT; no data-unfit.
  6. ruler numerals — adjacent tick labels have >= RULER_GAP px of clear space.
  7. assets — every texture image the page references returned HTTP 200 and nothing was fetched from a
     non-local origin except Google Fonts.

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

ADJ = 2           # px: chronologically adjacent continents must come at least this close (shared border)
LABEL_GAP = 6
INSIDE_MARGIN = 5
MIN_FONT = 12
RULER_GAP = 6
EDGE = 2
TEX_STD = 6.0     # min luminance stddev sampled inside a continent (flat colour ≈ 0; generated texture ≫ 6)
BUILD_MARKER = "P2-T1-RENDER v5"
ORDER = ["cybernetic-shore", "symbolic-heartland", "winter-steppes", "expert-systems-plateau", "connectionist-revival",
         "statistical-isthmus", "deep-learning-basin", "transformer-plateau", "generative-coast"]
# pairs that must share a border on the rendered map (chronological neighbours + the D2/D4 cluster)
ADJACENT = [("cybernetic-shore", "symbolic-heartland"), ("symbolic-heartland", "winter-steppes"),
            ("winter-steppes", "expert-systems-plateau"), ("expert-systems-plateau", "connectionist-revival"),
            ("expert-systems-plateau", "statistical-isthmus"), ("connectionist-revival", "statistical-isthmus"),
            ("statistical-isthmus", "deep-learning-basin"), ("deep-learning-basin", "transformer-plateau"),
            ("transformer-plateau", "generative-coast"), ("symbolic-heartland", "cybernetic-shore")]

JS = r"""
(cfg) => {
  const {ADJ, LABEL_GAP, INSIDE_MARGIN, MIN_FONT, RULER_GAP, EDGE, ADJACENT} = cfg;
  const svg = document.getElementById('map');
  const pt = svg.createSVGPoint();
  const vb = svg.viewBox.baseVal;
  const conts = [...document.querySelectorAll('#shapes .continent')].map(g => ({ id: g.dataset.id, lands: [...g.querySelectorAll('path.land')] }));
  const bb = e => { const b = e.getBBox(); return {x: b.x, y: b.y, r: b.x + b.width, b: b.y + b.height}; };
  const grow = (b, m) => ({x: b.x - m, y: b.y - m, r: b.r + m, b: b.b + m});
  const inter = (a, b) => a.x < b.r && b.x < a.r && a.y < b.b && b.y < a.b;
  const inFill = (p, x, y) => { pt.x = x; pt.y = y; return p.isPointInFill(pt); };
  const inStroke = (p, x, y) => { pt.x = x; pt.y = y; return p.isPointInStroke(pt); };
  const byId = Object.fromEntries(conts.map(c => [c.id, c]));
  const mainland = conts.filter(c => c.id !== 'antecedent-isles');
  const coastPaths = [...document.querySelectorAll('#coast path')];
  // 1a. overlaps: sample every mainland fill at 2px, test every other fill. A sample lying exactly ON the shared
  // border polyline satisfies isPointInFill for both sides (edge inclusive) — those are not overlaps, so points
  // within 1px of B's outline are excluded; anything else inside both fills is a real overlap.
  const overlaps = [];
  for (const A of mainland) for (const B of mainland) {
    if (A.id >= B.id) continue; const a = bb(A.lands[0]), b = bb(B.lands[0]); if (!inter(a, b)) continue;
    const Bp = B.lands[0]; const sw = Bp.style.strokeWidth; Bp.style.strokeWidth = '2px'; Bp.style.stroke = '#000';
    let n = 0, edge = 0;
    for (let x = Math.floor(Math.max(a.x, b.x)); x <= Math.min(a.r, b.r); x += 2) for (let y = Math.floor(Math.max(a.y, b.y)); y <= Math.min(a.b, b.b); y += 2) if (inFill(A.lands[0], x, y) && inFill(Bp, x, y)) { if (inStroke(Bp, x, y)) edge++; else n++; }
    Bp.style.strokeWidth = sw; Bp.style.stroke = '';
    if (n) overlaps.push({a: A.id, b: B.id, samples: n, onEdge: edge});
  }
  // 1b. adjacency: A's fill samples within ADJ px of B (B stroked 2*ADJ)
  const notAdjacent = [];
  for (const [ai, bi] of ADJACENT) {
    const A = byId[ai].lands[0], B = byId[bi].lands[0]; const a = bb(A);
    const sw = B.style.strokeWidth; B.style.strokeWidth = (2 * ADJ) + 'px'; B.style.stroke = '#000';
    let hit = 0;
    for (let x = Math.floor(a.x); x <= a.r && hit < 3; x += 1) for (let y = Math.floor(a.y); y <= a.b; y += 1) if (inFill(A, x, y) && inStroke(B, x, y)) { hit++; if (hit >= 3) break; }
    B.style.strokeWidth = sw; B.style.stroke = '';
    if (hit < 3) notAdjacent.push([ai, bi]);
  }
  // 1c. every mainland fill inside the single mainland coast loop; isles inside isle coasts
  const coastMain = coastPaths[0];
  const outsideCoast = [];
  for (const c of mainland) { const a = bb(c.lands[0]); let bad = 0, tot = 0; for (let x = a.x; x <= a.r; x += 4) for (let y = a.y; y <= a.b; y += 4) if (inFill(c.lands[0], x, y)) { tot++; if (!inFill(coastMain, x, y)) bad++; } if (bad) outsideCoast.push({id: c.id, bad, tot}); }
  // 1d. registry fidelity: each mainland fill stays inside its REGISTRY band span (± BAND_SLACK px of hand-drawn
  //     wobble) and its X extent matches its start/end years (± YEAR_SLACK px). v5: the plate is bent along the
  //     spine, so band membership is judged in PLATE coordinates: y_plate = y_screen - spineY(x), sampled over the
  //     fill (a bbox would mix the spine's rise into the band extent).
  const {BANDS_Y, SPANS, BAND_SLACK, YEAR_SLACK} = cfg;
  const bandViol = [];
  const plateExtent = {};
  for (const c of mainland) {
    const s = SPANS[c.id]; if (!s) continue; const a = bb(c.lands[0]);
    const yTop = BANDS_Y[s.bands[0]][0] - BAND_SLACK, yBot = BANDS_Y[s.bands[1]][1] + BAND_SLACK;
    let pyMin = 1e9, pyMax = -1e9;
    for (let x = Math.floor(a.x); x <= a.r; x += 2) for (let y = Math.floor(a.y); y <= a.b; y += 2) if (inFill(c.lands[0], x, y)) { const py = y - spineY(x); if (py < pyMin) pyMin = py; if (py > pyMax) pyMax = py; }
    plateExtent[c.id] = [+pyMin.toFixed(0), +pyMax.toFixed(0)];
    const dx0 = a.x - s.x0, dx1 = a.r - s.x1;
    if (pyMin < yTop || pyMax > yBot || Math.abs(dx0) > YEAR_SLACK || Math.abs(dx1) > YEAR_SLACK) bandViol.push({id: c.id, plateY: [+pyMin.toFixed(0), +pyMax.toFixed(0)], allowedY: [+yTop.toFixed(0), +yBot.toFixed(0)], dxStart: +dx0.toFixed(1), dxEnd: +dx1.toFixed(1)});
  }
  // 1e. v5 border audit: no internal border may be a straight vertical (or straight horizontal) line. For each
  //     adjacent pair, collect the shared-border pixels (A's fill ∩ B's 2px stroke), fit the best straight line
  //     through them and measure (i) the RMS lateral deviation from that line and (ii) the line's angle from
  //     vertical. A Gantt cut would give deviation ≈ 0 and angle ≈ 0; we require dev ≥ MIN_WANDER px OR
  //     |angle| ≥ MIN_TILT deg, and we report both so the audit is explicit per border.
  const borders = [];
  const seen = new Set();
  for (const [ai, bi] of ADJACENT) {
    const pk = [ai, bi].sort().join('|'); if (seen.has(pk)) continue; seen.add(pk);
    const A = byId[ai].lands[0], B = byId[bi].lands[0]; const a = bb(A), b = bb(B); if (!inter(a, b)) { borders.push({pair: [ai, bi], n: 0}); continue; }
    const sw = B.style.strokeWidth; B.style.strokeWidth = '2px'; B.style.stroke = '#000';
    const P = [];
    for (let x = Math.floor(Math.max(a.x, b.x)); x <= Math.min(a.r, b.r); x += 1) for (let y = Math.floor(Math.max(a.y, b.y)); y <= Math.min(a.b, b.b); y += 1) if (inFill(A, x, y) && inStroke(B, x, y)) P.push([x, y]);
    B.style.strokeWidth = sw; B.style.stroke = '';
    const n = P.length; if (n < 10) { borders.push({pair: [ai, bi], n}); continue; }
    const mx = P.reduce((s, p) => s + p[0], 0) / n, my = P.reduce((s, p) => s + p[1], 0) / n;
    let sxx = 0, syy = 0, sxy = 0; for (const [x, y] of P) { sxx += (x - mx) ** 2; syy += (y - my) ** 2; sxy += (x - mx) * (y - my); }
    const th = 0.5 * Math.atan2(2 * sxy, sxx - syy);            // principal axis angle from +x
    const ux = Math.cos(th), uy = Math.sin(th);
    let dev = 0; for (const [x, y] of P) { const d = -(x - mx) * uy + (y - my) * ux; dev += d * d; } dev = Math.sqrt(dev / n);
    const len = Math.sqrt(Math.max(sxx, syy) / n) * 3.46;        // ≈ extent along the axis (uniform spread)
    const tiltFromVertical = Math.abs(90 - Math.abs(th * 180 / Math.PI));
    const xr = Math.max(...P.map(p => p[0])) - Math.min(...P.map(p => p[0]));
    borders.push({pair: [ai, bi], n, rmsDev: +dev.toFixed(1), tiltDeg: +tiltFromVertical.toFixed(1), xRange: xr, len: +len.toFixed(0), straightVertical: dev < cfg.MIN_WANDER && tiltFromVertical < cfg.MIN_TILT});
  }
  // 2. texture fills
  const flatFills = conts.filter(c => !c.lands.every(l => (l.getAttribute('fill') || '').startsWith('url(#tex-')) || (c.id !== 'antecedent-isles' && !document.querySelector(`#shapes .continent[data-id="${c.id}"] path.texbleed`))).map(c => c.id);
  const fillSamples = {}; // centre points for pixel sampling in python (client px)
  const ctm = svg.getScreenCTM();
  for (const c of conts) { const a = bb(c.lands[0]); const pts = []; for (let x = a.x; x <= a.r; x += 3) for (let y = a.y; y <= a.b; y += 3) if (inFill(c.lands[0], x, y)) { const p = pt; p.x = x; p.y = y; const q = p.matrixTransform(ctm); pts.push([q.x, q.y]); } fillSamples[c.id] = pts.filter((_, i) => i % 4 === 0).slice(0, 1500); }
  // 3. labels
  const texts = [...document.querySelectorAll('#labels text')];
  const groups = {}; texts.forEach(t => (groups[t.dataset.for] = groups[t.dataset.for] || []).push(t));
  const labelOverlaps = []; const ids = Object.keys(groups);
  for (let i = 0; i < ids.length; i++) for (let j = i + 1; j < ids.length; j++) for (const ta of groups[ids[i]]) for (const tb of groups[ids[j]]) if (inter(grow(bb(ta), LABEL_GAP), bb(tb))) labelOverlaps.push([ids[i], ids[j], ta.textContent, tb.textContent]);
  const boxEdge = (b, step, fn) => { for (let x = b.x; x <= b.r; x += step) { if (fn(x, b.y) || fn(x, b.b)) return true; } for (let y = b.y; y <= b.b; y += step) { if (fn(b.x, y) || fn(b.r, y)) return true; } return false; };
  const boxAny = (b, step, fn) => { for (let x = b.x; x <= b.r; x += step) for (let y = b.y; y <= b.b; y += step) if (fn(x, y)) return true; return fn(b.r, b.b); };
  const insideIds = new Set(texts.filter(t => !document.querySelector(`#leaders [data-for="${t.dataset.for}"]`)).map(t => t.dataset.for));
  const outside = [], foreign = [], clipped = [];
  for (const c of conts) for (const t of groups[c.id] || []) {
    const b = bb(t);
    if (c.lands.length === 1 && insideIds.has(c.id) && boxEdge(grow(b, INSIDE_MARGIN), 2, (x, y) => !inFill(c.lands[0], x, y))) outside.push({id: c.id, text: t.textContent});
    for (const L of conts) if (L.id !== c.id && L.lands.some(l => boxAny(grow(b, LABEL_GAP), 2, (x, y) => inFill(l, x, y)))) foreign.push({label: c.id, text: t.textContent, land: L.id});
  }
  // no two text elements anywhere on the plate may overlap (labels, margins, ocean names, titles, ruler)
  const allT = [...svg.querySelectorAll('text')].filter(t => t.textContent.trim());
  const textClash = [];
  // stacked lines of one block touch by a couple of px (ascender/descender slack) — a real clash overlaps by
  // >= 40% of the shorter line's height AND >= 4px horizontally
  const realClash = (a, b) => { const oy = Math.min(a.b, b.b) - Math.max(a.y, b.y), ox = Math.min(a.r, b.r) - Math.max(a.x, b.x); return oy > .4 * Math.min(a.b - a.y, b.b - b.y) && ox > 4; };
  for (let i = 0; i < allT.length; i++) for (let j = i + 1; j < allT.length; j++) if (realClash(bb(allT[i]), bb(allT[j]))) textClash.push([allT[i].textContent, allT[j].textContent]);
  // every text on the map (labels, margins, ruler, titles) must be inside the viewBox
  for (const t of svg.querySelectorAll('text')) { const b = bb(t); if (b.x < EDGE || b.y < EDGE || b.r > vb.width - EDGE || b.b > vb.height - EDGE) clipped.push({text: t.textContent, x: +b.x.toFixed(1), r: +b.r.toFixed(1), y: +b.y.toFixed(1), b: +b.b.toFixed(1)}); }
  // 4. leaders
  const allLands = conts.flatMap(c => c.lands.map(l => ({id: c.id, el: l})));
  const leaderProblems = [];
  for (const p of document.querySelectorAll('#leaders path.leader')) {
    const id = p.dataset.for; const own = byId[id]; const L = p.getTotalLength(); const s = p.getPointAtLength(0), e = p.getPointAtLength(L);
    const sOwn = own.lands.some(l => inFill(l, s.x, s.y)), eOwn = own.lands.some(l => inFill(l, e.x, e.y));
    const sLand = allLands.some(l => inFill(l.el, s.x, s.y)), eLand = allLands.some(l => inFill(l.el, e.x, e.y));
    const startOnOwn = sOwn || eOwn; const endOnLand = sOwn ? eLand : sLand;
    let crossesForeign = false; for (let k = 0; k <= L; k += 2) { const q = p.getPointAtLength(k); if (allLands.some(l => l.id !== id && inFill(l.el, q.x, q.y))) { crossesForeign = true; break; } }
    if (!startOnOwn || endOnLand || crossesForeign || L < 14) leaderProblems.push({id, startOnOwn, endOnLand, crossesForeign, length: +L.toFixed(1)});
  }
  // 5. font floor
  const smallFonts = texts.filter(t => parseFloat(t.getAttribute('font-size')) < MIN_FONT - 1e-6 || t.dataset.unfit).map(t => ({id: t.dataset.for, text: t.textContent, size: t.getAttribute('font-size'), unfit: !!t.dataset.unfit}));
  // 6. ruler numerals
  const nums = [...document.querySelectorAll('#ruler-nums text')].map(t => ({y: t.textContent, b: bb(t)})).sort((a, b) => a.b.x - b.b.x);
  const rulerClashes = []; for (let i = 1; i < nums.length; i++) { const g = nums[i].b.x - nums[i - 1].b.r; if (g < RULER_GAP) rulerClashes.push([nums[i - 1].y, nums[i].y, +g.toFixed(1)]); }
  const images = [...svg.querySelectorAll('image')].map(i => i.getAttribute('href'));
  // 8. v5 spine: the coast's centreline must actually bend (not a strip). Sample the mainland coast's vertical
  //    midpoint per x column and report the peak-to-peak rise of that centreline.
  const cm = coastPaths[0]; const cb = bb(cm); const mids = [];
  for (let x = Math.floor(cb.x) + 10; x < cb.r - 10; x += 20) { let t = null, bt = null; for (let y = Math.floor(cb.y); y <= cb.b; y += 2) if (inFill(cm, x, y)) { if (t === null) t = y; bt = y; } if (t !== null) mids.push((t + bt) / 2); }
  const spineRise = mids.length ? +(Math.max(...mids) - Math.min(...mids)).toFixed(0) : 0;
  return {continents: conts.length, lands: allLands.length, coastLoops: coastPaths.length, overlaps, notAdjacent, outsideCoast, bandViol, plateExtent, borders, spineRise, flatFills, fillSamples, labelOverlaps, textClash, outside, foreign, clipped, leaderProblems, smallFonts, rulerClashes, images, viewBox: [vb.width, vb.height]};
}
"""
# geometry the page exposes for the registry-fidelity check (evaluated in-page: same X() / band maths as the render)
JS_GEOM = r"""
() => { const out = {BANDS_Y: {}, X: {}}; BANDS.forEach(b => out.BANDS_Y[b] = [bandTop(b), bandTop(b) + bandH]);
  return out; }
"""
# hand-drawn wobble budget (v5) = vertex jitter (≤0.6·lat) + border wander (≤lat, lat ≤ 30px) + coast cape (≤26px)
# + 3-octave warp (≤6+4.5+1.2px). The budget is what keeps the bend/wander from becoming "draw anything": a fill
# may stray at most this far from its registry band / year edges, measured in plate coordinates (spine removed).
BAND_SLACK = 44
YEAR_SLACK = 44
# v5 border audit thresholds: a border counts as a straight vertical cut only if it deviates < MIN_WANDER px RMS
# from its best-fit line AND that line is within MIN_TILT° of vertical. Any real border must clear at least one.
MIN_WANDER = 4.0
MIN_TILT = 6.0
MIN_SPINE_RISE = 40   # px: the mainland centreline must rise/fall at least this much across the page


def serve(root: Path, port: int):
    class Quiet(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *a, **k):
            super().__init__(*a, directory=str(root), **k)

        def log_message(self, *a, **k):  # noqa: D102
            pass
    httpd = http.server.ThreadingHTTPServer(("127.0.0.1", port), Quiet)
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
    from PIL import Image  # noqa: WPS433 (only needed for the texture-variance sample)
    import io, statistics  # noqa: E401
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": a.width, "height": 900}, device_scale_factor=1)
        responses = []
        pg.on("response", lambda r: responses.append((r.url, r.status)))
        pg.goto(url, wait_until="networkidle")
        pg.wait_for_selector("#shapes .continent")
        pg.evaluate("document.fonts.ready")
        pg.wait_for_timeout(1000)
        reg = json.loads((Path(__file__).resolve().parent / "registry.json").read_text())
        geom = pg.evaluate(JS_GEOM)
        spans = {}
        for c in reg["continents"]:
            if c.get("offshore"):
                continue
            bands = c["band_span_text"].split(" ")[0].split("–")
            bands = bands if len(bands) == 2 else [bands[0], bands[0]]
            end_expr = "PRESENT - 0.06" if c["end"] == "present" else str(c["end"])
            x0, x1 = pg.evaluate(f"() => [X({c['start']}), X({end_expr})]")
            spans[c["id"]] = {"bands": bands, "x0": x0, "x1": x1}
        res = pg.evaluate(JS, dict(ADJ=ADJ, LABEL_GAP=LABEL_GAP, INSIDE_MARGIN=INSIDE_MARGIN, MIN_FONT=MIN_FONT, RULER_GAP=RULER_GAP, EDGE=EDGE, ADJACENT=ADJACENT, BANDS_Y=geom["BANDS_Y"], SPANS=spans, BAND_SLACK=BAND_SLACK, YEAR_SLACK=YEAR_SLACK, MIN_WANDER=MIN_WANDER, MIN_TILT=MIN_TILT))
        pg.screenshot(path=a.shot, full_page=True)
        pg.query_selector("#map").screenshot(path=a.shot.replace(".png", "-map.png"))
        png = pg.screenshot(full_page=False, clip={"x": 0, "y": 0, "width": a.width, "height": 900})
        html = pg.content()
        b.close()
    if httpd:
        httpd.shutdown()
    # 2b. texture variance from real pixels
    im = Image.open(io.BytesIO(png)).convert("L")
    texStd = {}
    for cid, pts in res["fillSamples"].items():
        vals = [int(im.getpixel((int(x), int(y))) or 0) for x, y in pts if 0 <= x < im.width and 0 <= y < im.height]  # type: ignore[arg-type]
        texStd[cid] = round(statistics.pstdev(vals), 1) if len(vals) > 10 else 0.0
    lowTex = {k: v for k, v in texStd.items() if v < TEX_STD}
    # 7. assets
    badAssets = [(u, s) for u, s in responses if s >= 400]
    offsite = [u for u, _ in responses if not u.startswith(url) and "fonts.g" not in u]
    for k in ("continents", "lands", "coastLoops", "viewBox", "images", "spineRise", "plateExtent"):
        print(f"{k}: {res[k]}")
    print("border audit (per adjacent pair: rmsDev px from best-fit line, tilt° from vertical, straightVertical?):")
    for bd in res["borders"]:
        print("  ", json.dumps(bd))
    print(f"texture luminance stddev per continent (require >= {TEX_STD}): {json.dumps(texStd)}")
    fails = {k: res[k] for k in ("overlaps", "notAdjacent", "outsideCoast", "bandViol", "flatFills", "labelOverlaps", "textClash", "outside", "foreign", "clipped", "leaderProblems", "smallFonts", "rulerClashes")}
    fails["lowTexture"] = lowTex
    fails["straightBorders"] = [bd["pair"] for bd in res["borders"] if bd.get("n", 0) < 10 or bd.get("straightVertical")]
    fails["flatSpine"] = [] if res["spineRise"] >= MIN_SPINE_RISE else [res["spineRise"]]
    fails["badAssets"] = badAssets
    fails["offsiteRequests"] = offsite
    for k, v in fails.items():
        print(f"{k} ({len(v)}): {json.dumps(v, ensure_ascii=False)}")
    ok = res["continents"] == 10 and res["lands"] == 13 and res["coastLoops"] == 5 and all(not v for v in fails.values()) and BUILD_MARKER in html
    print("screenshot:", a.shot)
    print("build marker present:", BUILD_MARKER in html)
    print("RESULT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
