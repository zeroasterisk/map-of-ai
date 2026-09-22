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
N_THREADS = 1          # THREADS v1: data/threads/*.yaml drawn as linear features (the Silicon Range)
MIN_THREAD_LABELS = 4  # milestone labels that must survive curation on the A1 plate
TEX_STD = 6.0     # min luminance stddev sampled inside a continent (flat colour ≈ 0; generated texture ≫ 6)
BUILD_MARKER = "P2-T1-RENDER v11"
COUNTRY_MARKER = "P3-RENDER v2"
N_COUNTRIES = 31         # spatial countries in entities.json: basin 8 + generative coast 8 + transformer plateau 8 + statistical isthmus 4 + connectionist revival 3 (tooling-guild & national-champion-scalers are spatial: false)
CONTAIN_N = 300          # interior samples per country for the containment gate (A-V2)
OVERLAP_N = 500          # interior samples per country for the pairwise zero-overlap gate (A-V3)
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
  //     spine and (v12) stretched by the Y-funnel, so band membership is judged in 1x PLATE coordinates: y_plate = plateY(x, y_screen) (the renderer's exact inverse), sampled over the
  //     fill (a bbox would mix the spine's rise into the band extent).
  const {BANDS_Y, SPANS, BAND_SLACK, YEAR_SLACK} = cfg;
  const bandViol = [];
  const plateExtent = {}, yearExtent = {};
  for (const c of mainland) {
    const s = SPANS[c.id]; if (!s) continue; const a = bb(c.lands[0]);
    const yTop = BANDS_Y[s.bands[0]][0] - BAND_SLACK, yBot = BANDS_Y[s.bands[1]][1] + BAND_SLACK;
    let pyMin = 1e9, pyMax = -1e9;
    for (let x = Math.floor(a.x); x <= a.r; x += 2) for (let y = Math.floor(a.y); y <= a.b; y += 2) if (inFill(c.lands[0], x, y)) { const py = plateY(x, y); if (py < pyMin) pyMin = py; if (py > pyMax) pyMax = py; }
    plateExtent[c.id] = [+pyMin.toFixed(0), +pyMax.toFixed(0)];
    yearExtent[c.id] = [+(a.x - s.x0).toFixed(0), +(a.r - s.x1).toFixed(0)];   // px offset of the drawn x-extent from the registry years (−: earlier, +: later)
    // v7: a region may legitimately NOT fill its envelope (recede-to-sea is artistic license), so only the OUTER
    // bound is enforced on the band axis; on the year axis the drawn extent must still sit within YEAR_SLACK of the
    // registry years, plus the declared LICENSE overshoot (px) for the two eastern regions' shared L-seam.
    const lic = cfg.LICENSE[c.id] || {};
    // v9: the renderer publishes its ISOCHRONE FRONTIER per region (declared start/end years per band, window.FRONTIER);
    // the drawn x-extent is held to the DECLARED frontier ± YEAR_SLACK (+ the v7 license), not to a single year.
    const fr = (typeof FRONTIER !== 'undefined' && FRONTIER[c.id]) || null;
    const fx0 = fr ? [X(fr.startMin) - s.x0, X(fr.startMax) - s.x0] : [0, 0], fx1 = fr ? [X(fr.endMin) - s.x1, X(fr.endMax) - s.x1] : [0, 0];
    const dx0 = a.x - s.x0, dx1 = a.r - s.x1;
    const okStart = dx0 >= fx0[0] - (YEAR_SLACK + (lic.start || 0)) && dx0 <= fx0[1] + YEAR_SLACK + (lic.startLate || 0);
    const okEnd = dx1 <= fx1[1] + YEAR_SLACK + (lic.end || 0) && dx1 >= fx1[0] - (YEAR_SLACK + (lic.endEarly || 0));
    if (pyMin < yTop || pyMax > yBot || !okStart || !okEnd) bandViol.push({id: c.id, plateY: [+pyMin.toFixed(0), +pyMax.toFixed(0)], allowedY: [+yTop.toFixed(0), +yBot.toFixed(0)], dxStart: +dx0.toFixed(1), dxEnd: +dx1.toFixed(1)});
  }
  // 1f. v8 ENVELOPE CONFORMANCE + FUNNEL PROFILE. The renderer publishes its global outer envelope (ENV: per time
  //     column the outermost half-band rows land may occupy, ROWY: the row edges in plate px, COLS: the column
  //     years). Sample the rendered MAINLAND coast fill (not the authoring grid) at every column's mid-year over the
  //     full band height: no land pixel may lie beyond the envelope's plate-y bounds (+ BAND_SLACK of wobble), and
  //     the measured land thickness per column must realise the funnel — the west tip (first column) must be at
  //     most FUNNEL_TIP_MAX px thick and the thickest column at least FUNNEL_RATIO × the tip.
  const envViol = [], profile = [];
  if (typeof ENV !== 'undefined') {
    for (let i = 0; i < ENV.length; i++) {
      const x = X((COLS[i] + COLS[i + 1]) / 2), yN = ROWY[ENV[i][0]] - BAND_SLACK, yS = ROWY[ENV[i][1] + 1] + BAND_SLACK;
      let top = null, bot = null, beyond = 0;
      for (let y = ROWY[0] - 40; y <= ROWY[ROWY.length - 1] + 40; y += 1) { const sy = SY(x, y); if (inFill(coastMain, x, sy)) { if (top === null) top = y; bot = y; if (y < yN || y > yS) beyond++; } }
      profile.push({yr: +COLS[i].toFixed(1), env: [+ROWY[ENV[i][0]].toFixed(0), +ROWY[ENV[i][1] + 1].toFixed(0)], land: top === null ? null : [top, bot], thick: top === null ? 0 : bot - top});
      if (beyond) envViol.push({yr: COLS[i], beyond, land: [top, bot], env: [yN, yS]});
    }
  }
  const thick = profile.map(p => p.thick), funnel = {tip: thick[0] || 0, max: Math.max(...thick, 0), westMean: 0, eastMean: 0};
  if (thick.length) { const q = Math.floor(thick.length / 4); funnel.westMean = Math.round(thick.slice(0, q).reduce((a, b) => a + b, 0) / q); funnel.eastMean = Math.round(thick.slice(-q).reduce((a, b) => a + b, 0) / q); }
  const funnelOK = typeof ENV !== 'undefined' && funnel.tip <= cfg.FUNNEL_TIP_MAX && funnel.max >= cfg.FUNNEL_RATIO * funnel.tip && funnel.eastMean >= 2 * funnel.westMean;
  // 1g. v9 ISOCHRONE FRONTIERS. For every mainland region, sample its rendered fill along the centre of each
  //     half-band row (plate coords, spine removed) and record the westmost / eastmost land x per row, converted
  //     back to years. A boundary is DIAGONAL when the arrival year differs across the rows it spans by at least
  //     MIN_FRONT_SPREAD_PX (measured at the region's west edge = its arrival frontier). The gate needs at least
  //     MIN_DIAG_FRONTS regions with a diagonal arrival frontier, and no per-row arrival may be outside the
  //     declared FRONTIER window ± YEAR_SLACK (the per-band form of the registry-year check above).
  const fronts = {};
  if (typeof ROWY !== 'undefined') {
    for (const c of mainland) {
      const a = bb(c.lands[0]); const rows = [];
      for (let j = 0; j < ROWY.length - 1; j++) {
        const py = (ROWY[j] + ROWY[j + 1]) / 2; let w = null, e = null;
        for (let x = Math.floor(a.x); x <= a.r; x += 1) if (inFill(c.lands[0], x, SY(x, py))) { if (w === null) w = x; e = x; }
        if (w !== null) rows.push({row: j, west: w, east: e});
      }
      const ws = rows.map(r => r.west), es = rows.map(r => r.east);
      fronts[c.id] = {rows, westSpreadPx: rows.length ? +(Math.max(...ws) - Math.min(...ws)).toFixed(0) : 0, eastSpreadPx: rows.length ? +(Math.max(...es) - Math.min(...es)).toFixed(0) : 0};
    }
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
  const allT = [...svg.querySelectorAll('text')].filter(t => t.textContent.trim() && t.getClientRects().length > 0);   // rendered text only (A2 country labels sit under a display:none group at A1)
  const textClash = [];
  // stacked lines of one block touch by a couple of px (ascender/descender slack) — a real clash overlaps by
  // >= 40% of the shorter line's height AND >= 4px horizontally
  const realClash = (a, b) => { const oy = Math.min(a.b, b.b) - Math.max(a.y, b.y), ox = Math.min(a.r, b.r) - Math.max(a.x, b.x); return oy > .4 * Math.min(a.b - a.y, b.b - b.y) && ox > 4; };
  for (let i = 0; i < allT.length; i++) for (let j = i + 1; j < allT.length; j++) if (realClash(bb(allT[i]), bb(allT[j]))) textClash.push([allT[i].textContent, allT[j].textContent]);
  // every text on the map (labels, margins, ruler, titles) must be inside the viewBox
  for (const t of allT) { const b = bb(t); if (b.x < EDGE || b.y < EDGE || b.r > vb.width - EDGE || b.b > vb.height - EDGE) clipped.push({text: t.textContent, x: +b.x.toFixed(1), r: +b.r.toFixed(1), y: +b.y.toFixed(1), b: +b.b.toFixed(1)}); }
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
  // 9. v6 coastline sanity: no vertex of the mainland coast may turn back on itself (a needle spike / hairpin —
  //    the wide waterline strokes render an ink blob at such a tip). Report every turn > HAIRPIN_DEG.
  const cpts = cm.getAttribute('d').slice(1, -1).split('L').map(s => s.split(',').map(Number));
  const hairpins = [];
  for (let i = 0; i < cpts.length; i++) { const a = cpts[(i - 1 + cpts.length) % cpts.length], p = cpts[i], c = cpts[(i + 1) % cpts.length]; const v1 = [p[0] - a[0], p[1] - a[1]], v2 = [c[0] - p[0], c[1] - p[1]]; const t = Math.abs(Math.atan2(v1[0] * v2[1] - v1[1] * v2[0], v1[0] * v2[0] + v1[1] * v2[1]) * 180 / Math.PI); if (t > cfg.HAIRPIN_DEG) hairpins.push({at: p.map(v => +v.toFixed(0)), turnDeg: +t.toFixed(0)}); }
  // 10. v6 in-region shape variation: per mainland region, sample the fill's top and bottom (plate coords) per x
  //     column across the region's own span and report the peak-to-peak wander of its north and south coast,
  //     plus its height range. A constant-height slab gives ≈ 0; a landmass with capes and bays gives tens of px.
  const shape = {};
  for (const c of mainland) {
    const p = c.lands[0]; const a = bb(p); const tops = [], bots = [], hs = [];
    for (let x = Math.floor(a.x) + 14; x <= a.r - 14; x += 4) { let t = null, bt = null; for (let y = Math.floor(a.y); y <= a.b; y += 1) if (inFill(p, x, y)) { if (t === null) t = y; bt = y; } if (t !== null) { tops.push(plateY(x, t)); bots.push(plateY(x, bt)); hs.push(plateY(x, bt) - plateY(x, t)); } }
    if (tops.length) shape[c.id] = {northP2P: +(Math.max(...tops) - Math.min(...tops)).toFixed(0), southP2P: +(Math.max(...bots) - Math.min(...bots)).toFixed(0), height: [+Math.min(...hs).toFixed(0), +Math.max(...hs).toFixed(0)], width: +(a.r - a.x).toFixed(0)};
  }
  return {fronts, continents: conts.length, lands: allLands.length, coastLoops: coastPaths.length, overlaps, notAdjacent, outsideCoast, bandViol, envViol, profile, funnel, funnelOK, plateExtent, yearExtent, borders, spineRise, hairpins, shape, flatFills, fillSamples, labelOverlaps, textClash, outside, foreign, clipped, leaderProblems, smallFonts, rulerClashes, images, viewBox: [vb.width, vb.height]};
}
"""
# P3-RENDER v2 country gates (SPEC §9.2 A-V2 / A-V3 / A-V6 / A-V7 + the zoom-consistency check). Evaluated in-page.
JS_COUNTRY = r"""
(cfg) => {
  const {N_IN, N_OV, LABEL_GAP, SEED} = cfg;
  const svg = document.getElementById('map'); const pt = svg.createSVGPoint();
  const inFill = (p, x, y) => { pt.x = x; pt.y = y; return p.isPointInFill(pt); };
  const bb = e => { const b = e.getBBox(); return {x: b.x, y: b.y, r: b.x + b.width, b: b.y + b.height}; };
  const grow = (b, m) => ({x: b.x - m, y: b.y - m, r: b.r + m, b: b.b + m});
  const inter = (a, b) => a.x < b.r && b.x < a.r && a.y < b.b && b.y < a.b;
  let s = SEED >>> 0; const rnd = () => { s = (Math.imul(s, 1664525) + 1013904223) >>> 0; return s / 4294967296; };   // seeded LCG: repeatable samples
  const ks = [...document.querySelectorAll('#countries .country')].map(g => ({id: g.dataset.id, parent: g.dataset.parent, land: g.querySelector('path.cland')}));
  const parents = {}; for (const k of ks) parents[k.parent] = parents[k.parent] || document.querySelector(`#shapes .continent[data-id="${k.parent}"] path.land`);
  const others = pid => [...document.querySelectorAll('#shapes .continent path.land')].filter(p => p.closest('.continent').dataset.id !== pid);
  // random interior points of a country: rejection-sample its bbox until N points fall in its own fill
  const interior = (k, N) => { const b = bb(k.land); const out = []; for (let g = 0; g < N * 400 && out.length < N; g++) { const x = b.x + rnd() * (b.r - b.x), y = b.y + rnd() * (b.b - b.y); if (inFill(k.land, x, y)) out.push([x, y]); } return out; };
  // 11. containment (A-V2): >= N_IN interior points per country, 100 % inside the parent's rendered polygon, 0 % in any other continent
  const containment = {}; const contFail = [];
  for (const k of ks) { const pts = interior(k, N_IN); const oth = others(k.parent); let inP = 0, inO = 0; for (const [x, y] of pts) { if (inFill(parents[k.parent], x, y)) inP++; if (oth.some(p => inFill(p, x, y))) inO++; }
    containment[k.id] = {sampled: pts.length, inParent: inP, inOther: inO}; if (pts.length < N_IN || inP !== pts.length || inO) contFail.push({id: k.id, ...containment[k.id]}); }
  // 12. zero overlap (A-V3): N_OV interior points per country; none may lie inside a sibling's fill (points within
  // 1 px of the sibling's outline are on the shared polyline — edge-inclusive hit test, not area — and are excluded)
  const overlapFail = []; let ovPairs = 0, ovPts = 0;
  for (const A of ks) { const pts = interior(A, N_OV); for (const B of ks) { if (A.id >= B.id) continue; if (!inter(bb(A.land), bb(B.land))) continue; ovPairs++;
    const sw = B.land.style.strokeWidth; B.land.style.strokeWidth = '2px'; B.land.style.stroke = '#000'; let n = 0;
    for (const [x, y] of pts) { ovPts++; pt.x = x; pt.y = y; if (B.land.isPointInFill(pt) && !B.land.isPointInStroke(pt)) n++; }
    B.land.style.strokeWidth = sw; B.land.style.stroke = ''; if (n) overlapFail.push({a: A.id, b: B.id, samples: n}); } }
  // 13. consistency: the parent's coastline/border path d must not change between A1 and A2
  const map = document.getElementById('map'); const coastD = () => [...document.querySelectorAll('#coast path')].map(p => p.getAttribute('d')).join('|');
  const borderD = pid => document.querySelector(`#shapes .continent[data-id="${pid}"] path.border`).getAttribute('d');
  const pids = Object.keys(parents); const before = {coast: coastD(), borders: pids.map(borderD)};
  const a1Labels = document.querySelectorAll('#klabels text').length, a1Vis = [...document.querySelectorAll('#klabels text')].filter(t => getComputedStyle(t).display !== 'none' && getComputedStyle(t.parentNode).display !== 'none').length;
  // enter A2 by a real click on the first parent's land (the same handler the user hits)
  const parentG = document.querySelector(`#shapes .continent[data-id="${pids[0]}"]`); parentG.dispatchEvent(new MouseEvent('click', {bubbles: true}));
  const zoomed = map.classList.contains('zoomed');
  const after = {coast: coastD(), borders: pids.map(borderD)};
  const consistent = zoomed && before.coast === after.coast && before.borders.every((d, i) => d === after.borders[i]);
  // A-V6 / A-V7 at A2: >= 2 text nodes per country (name + years; subtitle when it fits), selected continent's name hidden,
  // no two country label boxes intersect after LABEL_GAP growth, and each label is inside its own polygon or has a leader
  const kt = [...document.querySelectorAll('#klabels text')]; const byK = {}; kt.forEach(t => (byK[t.dataset.for] = byK[t.dataset.for] || []).push(t));
  const fewTexts = ks.filter(k => (byK[k.id] || []).length < 2).map(k => k.id);
  const selHidden = [...document.querySelectorAll(`#labels text[data-for="${pids[0]}"]`)].every(t => getComputedStyle(t).display === 'none');
  const kOverlaps = []; const kids = Object.keys(byK);
  for (let i = 0; i < kids.length; i++) for (let j = i + 1; j < kids.length; j++) for (const ta of byK[kids[i]]) for (const tb of byK[kids[j]]) if (inter(grow(bb(ta), LABEL_GAP), bb(tb))) kOverlaps.push([kids[i], kids[j], ta.textContent, tb.textContent]);
  const kOutside = [];
  for (const k of ks) { const ts = byK[k.id] || []; if (!ts.length) continue; const hasLeader = !!document.querySelector(`#kleaders path[data-for="${k.id}"]`);
    if (hasLeader) { const c = document.querySelector(`#kleaders circle[data-for="${k.id}"]`); if (!inFill(k.land, +c.getAttribute('cx'), +c.getAttribute('cy'))) kOutside.push({id: k.id, leaderEndOutside: true}); }
    else for (const t of ts) { const b = bb(t); let bad = false; for (let x = b.x; x <= b.r && !bad; x += 2) if (!inFill(k.land, x, b.y) || !inFill(k.land, x, b.b)) bad = true; if (bad) kOutside.push({id: k.id, text: t.textContent}); } }
  const zoomBorders = [...document.querySelectorAll('#countries .kzoom')].filter(e => getComputedStyle(e).display !== 'none').length;
  document.dispatchEvent(new KeyboardEvent('keydown', {key: 'Escape'})); const unzoomed = !map.classList.contains('zoomed');
  return {countries: ks.length, containment, contFail, overlapPairs: ovPairs, overlapPoints: ovPts, overlapFail, zoomed, unzoomed, consistent, a1Labels, a1Vis, fewTexts, selHidden, kOverlaps, kOutside, zoomBorders};
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
# v7 artistic license (site/index.html "v7 east"): the Transformer Plateau's language belt runs to 2022.8 and the
# Generative Coast's diffusion toe starts at 2021.3, so those two edges may overshoot the registered 2022 border by
# up to LICENSE_YR years (converted to px in-page) on top of YEAR_SLACK. Every other edge keeps the plain slack.
LICENSE_YR = {"transformer-plateau": {"end": 0.9}, "generative-coast": {"start": 0.9}}
# v8 funnel: the rendered mainland's north-south thickness at the 1943 tip column may be at most FUNNEL_TIP_MAX px
# (2 half-bands = 82 plate px + coast wobble) and the thickest column must be >= FUNNEL_RATIO x the tip; the mean
# thickness of the eastern quarter of columns must be >= 2x the western quarter. envViol lists any land pixel
# beyond the renderer's published ENV bounds (+ BAND_SLACK).
FUNNEL_TIP_MAX = 150
FUNNEL_RATIO = 3.0
# v5 border audit thresholds: a border counts as a straight vertical cut only if it deviates < MIN_WANDER px RMS
# from its best-fit line AND that line is within MIN_TILT° of vertical. Any real border must clear at least one.
MIN_WANDER = 4.0
MIN_TILT = 6.0
MIN_SPINE_RISE = 40   # px: the mainland centreline must rise/fall at least this much across the page
HAIRPIN_DEG = 150     # v6: max turning angle at any mainland coast vertex (a spike folds back ≥ 150°)
# v6: the wide regions must not be constant-height slabs across their own span: north or south coast must wander
# at least MIN_COAST_P2P px peak-to-peak (measured in plate coords over the region's own x-range, corners excluded)
MIN_COAST_P2P = 40
WIDE = ["deep-learning-basin", "transformer-plateau", "generative-coast"]
# v9 isochrone frontiers: a region's ARRIVAL frontier (its west edge) is diagonal when the westmost land x differs
# across its half-band rows by >= MIN_FRONT_SPREAD_PX; at least MIN_DIAG_FRONTS of the mainland regions must have
# one (v8 measured 0 — every boundary was x = start_year + wobble).
MIN_FRONT_SPREAD_PX = 30
MIN_DIAG_FRONTS = 6


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
        url = f"http://127.0.0.1:{a.port}/atlas.html"
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
        yr_px = pg.evaluate("() => X(2023) - X(2022)")   # px per year in the 6× era
        license_px = {cid: {k: round(v * yr_px, 1) for k, v in d.items()} for cid, d in LICENSE_YR.items()}
        res = pg.evaluate(JS, dict(ADJ=ADJ, LABEL_GAP=LABEL_GAP, INSIDE_MARGIN=INSIDE_MARGIN, MIN_FONT=MIN_FONT, RULER_GAP=RULER_GAP, EDGE=EDGE, ADJACENT=ADJACENT, BANDS_Y=geom["BANDS_Y"], SPANS=spans, BAND_SLACK=BAND_SLACK, YEAR_SLACK=YEAR_SLACK, LICENSE=license_px, MIN_WANDER=MIN_WANDER, MIN_TILT=MIN_TILT, HAIRPIN_DEG=HAIRPIN_DEG, FUNNEL_TIP_MAX=FUNNEL_TIP_MAX, FUNNEL_RATIO=FUNNEL_RATIO))
        pg.screenshot(path=a.shot, full_page=True)
        pg.query_selector("#map").screenshot(path=a.shot.replace(".png", "-map.png"))
        # P3-RENDER v2 country gates: run AFTER the continent screenshot (they toggle A2 and back)
        ent = json.loads((Path(__file__).resolve().parent / "entities.json").read_text())
        spatial_ids = sorted(c["id"] for c in ent["countries"] if c.get("spatial", True))
        kres = pg.evaluate(JS_COUNTRY, dict(N_IN=CONTAIN_N, N_OV=OVERLAP_N, LABEL_GAP=LABEL_GAP, SEED=20260912))
        # THREADS v1 gate (A1, unzoomed): every thread milestone label must (a) not intersect any continent label
        # or any other thread label (grown by LABEL_GAP) and (b) sit inside the mainland coast; and the range must
        # actually be on the page with >= MIN_THREAD_LABELS visible milestone labels.
        tres = pg.evaluate(r"""(G) => {
          const svg = document.getElementById('map'); const coast = document.querySelector('#coast path');
          const bb = t => { const b = t.getBBox(); return {x: b.x, y: b.y, r: b.x + b.width, b: b.y + b.height, text: t.textContent}; };
          const inter = (u, v) => u.x < v.r + G && v.x < u.r + G && u.y < v.b + G && v.y < u.b + G;
          const cont = [...document.querySelectorAll('#labels text')].filter(t => t.getClientRects().length).map(bb);
          const thr = [...document.querySelectorAll('#thread-labels text.thr-name, #thread-labels text.thr-year, #thread-labels text.thr-title')].map(t => Object.assign(bb(t), {ms: t.getAttribute('data-ms') || t.textContent}));
          const names = [...document.querySelectorAll('#thread-labels text.thr-name')].map(t => t.getAttribute('data-ms'));
          const over = []; for (const u of thr) { for (const v of cont) if (inter(u, v)) over.push([u.text, v.text]); }
          for (let i = 0; i < thr.length; i++) for (let j = i + 1; j < thr.length; j++) { const u = thr[i], v = thr[j]; if (u.ms === v.ms) continue; /* a milestone's own name+year stack */ if (inter(u, v)) over.push([u.text, v.text]); }
          const pt = svg.createSVGPoint(); const inside = u => { for (const [x, y] of [[u.x, u.y], [u.r, u.y], [u.x, u.b], [u.r, u.b], [(u.x + u.r) / 2, (u.y + u.b) / 2]]) { pt.x = x; pt.y = y; if (!coast.isPointInFill(pt)) return false; } return true; };
          const outside = thr.filter(u => !inside(u)).map(u => u.text);
          const peaks = document.querySelectorAll('#threads .thr-peak').length;
          return {threads: document.querySelectorAll('#threads .thread').length, peaks, labels: names, overlaps: over, outside, curated: window.THREAD_CURATED || {}};
        }""", LABEL_GAP)
        pg.evaluate("document.querySelector('#shapes .continent[data-id=\"deep-learning-basin\"]').dispatchEvent(new MouseEvent('click', {bubbles: true}))")
        pg.wait_for_timeout(200)
        pg.query_selector("#map").screenshot(path=a.shot.replace(".png", "-A2.png"))
        pg.keyboard.press("Escape")
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
    # same-origin test: compare against the page URL without its query string, so a cache-buster (?cb=...) on
    # --url does not make the site's own registry.json / textures look like third-party requests
    base = url.split("?", 1)[0].rsplit("/", 1)[0] + "/"
    offsite = [u for u, _ in responses if not u.startswith(base) and "fonts.g" not in u]
    print(f"license slack px (v7, on top of YEAR_SLACK={YEAR_SLACK}): {json.dumps(license_px)}")
    for k in ("continents", "lands", "coastLoops", "viewBox", "images", "spineRise", "plateExtent", "yearExtent"):
        print(f"{k}: {res[k]}")
    print("in-region shape (v6; plate px over each region's own span): north/south coast peak-to-peak, height range:")
    for cid, s in res["shape"].items():
        print("  ", cid, json.dumps(s))
    print(f"v8 funnel profile (mainland thickness in plate px per time column; envelope rows -> land rows): {json.dumps(res['funnel'])}")
    for pr in res["profile"]:
        print("  ", json.dumps(pr))
    print(f"v9 frontier spread px per region (west edge / east edge, across half-band rows; diagonal >= {MIN_FRONT_SPREAD_PX}):")
    for cid, f in res["fronts"].items():
        print(f"   {cid}: west {f['westSpreadPx']} east {f['eastSpreadPx']}  rows " + " ".join(f"{r['row']}:[{r['west']},{r['east']}]" for r in f["rows"]))
    print("border audit (per adjacent pair: rmsDev px from best-fit line, tilt° from vertical, straightVertical?):")
    for bd in res["borders"]:
        print("  ", json.dumps(bd))
    print(f"texture luminance stddev per continent (require >= {TEX_STD}): {json.dumps(texStd)}")
    fails = {k: res[k] for k in ("overlaps", "notAdjacent", "outsideCoast", "bandViol", "flatFills", "labelOverlaps", "textClash", "outside", "foreign", "clipped", "leaderProblems", "smallFonts", "rulerClashes")}
    fails["lowTexture"] = lowTex
    fails["straightBorders"] = [bd["pair"] for bd in res["borders"] if bd.get("n", 0) < 10 or bd.get("straightVertical")]
    fails["flatSpine"] = [] if res["spineRise"] >= MIN_SPINE_RISE else [res["spineRise"]]
    fails["hairpins"] = res["hairpins"]
    fails["envelopeViol"] = res["envViol"]
    fails["notFunnel"] = [] if res["funnelOK"] else [res["funnel"]]
    fails["slabRegions"] = [cid for cid in WIDE if max(res["shape"][cid]["northP2P"], res["shape"][cid]["southP2P"]) < MIN_COAST_P2P]
    fails["badAssets"] = badAssets
    diag = [cid for cid, f in res["fronts"].items() if f["westSpreadPx"] >= MIN_FRONT_SPREAD_PX]
    fails["frontiersNotDiagonal"] = [] if len(diag) >= MIN_DIAG_FRONTS else [{"diagonal": diag, "need": MIN_DIAG_FRONTS}]
    fails["offsiteRequests"] = offsite
    # P3-RENDER v2 country gates (all sampled in-page; see JS_COUNTRY)
    rendered_ids = sorted(kres["containment"].keys())
    print(f"country layer: {kres['countries']} rendered {rendered_ids}; entities.json spatial: {spatial_ids}")
    print(f"containment ({CONTAIN_N} interior samples per country, must be 100 % inside parent, 0 % in other continents): {json.dumps(kres['containment'])}")
    print(f"zero-overlap: {kres['overlapPairs']} bbox-intersecting pairs, {kres['overlapPoints']} point tests ({OVERLAP_N} interior samples per country)")
    print(f"A1 country labels present/visible: {kres['a1Labels']}/{kres['a1Vis']}; A2 zoomed={kres['zoomed']} selNameHidden={kres['selHidden']} zoomBorders={kres['zoomBorders']} unzoomedByEsc={kres['unzoomed']}; parent coast/border d identical A1 vs A2: {kres['consistent']}")
    fails["countryCount"] = [] if rendered_ids == spatial_ids and len(rendered_ids) == N_COUNTRIES else [rendered_ids]
    fails["countryContainment"] = kres["contFail"]
    fails["countryOverlap"] = kres["overlapFail"]
    fails["zoomInconsistent"] = [] if kres["consistent"] and kres["zoomed"] and kres["unzoomed"] else [{"zoomed": kres["zoomed"], "unzoomed": kres["unzoomed"], "consistent": kres["consistent"]}]
    fails["a1CountryLabelsVisible"] = [] if kres["a1Vis"] == 0 else [kres["a1Vis"]]
    fails["a2FewTexts"] = kres["fewTexts"]
    fails["a2SelNameShown"] = [] if kres["selHidden"] else ["deep-learning-basin"]
    fails["countryLabelOverlaps"] = kres["kOverlaps"]
    fails["countryLabelOutside"] = kres["kOutside"]
    fails["countryMarker"] = [] if COUNTRY_MARKER in html else [COUNTRY_MARKER]
    print(f"threads (v1): {tres['threads']} drawn, {tres['peaks']} milestone peaks, labelled: {tres['labels']}, curated out: {json.dumps(tres['curated'])}")
    fails["threadCount"] = [] if tres["threads"] == N_THREADS else [tres["threads"]]
    fails["threadLabelsVisible"] = [] if len(tres["labels"]) >= MIN_THREAD_LABELS else [tres["labels"]]
    fails["threadLabelOverlaps"] = tres["overlaps"]
    fails["threadLabelOutside"] = tres["outside"]
    for k, v in fails.items():
        print(f"{k} ({len(v)}): {json.dumps(v, ensure_ascii=False)}")
    ok = res["continents"] == 10 and res["lands"] == 13 and res["coastLoops"] == 5 and all(not v for v in fails.values()) and BUILD_MARKER in html
    print("screenshot:", a.shot)
    print("build marker present:", BUILD_MARKER in html)
    print("RESULT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
