#!/usr/bin/env python3
"""
tests/sample_frames.py — Deterministic Mobile Density & Validation Sampler for Map of AI.
Evaluates the map against mobile viewports (412x892 @ DPR 2) across semantic zoom levels.
Enforces density floors, detects dead zones, text clipping, and text overlaps.
"""

import os
import sys
import json
import time
import random
import argparse
import threading
from pathlib import Path
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

REPO = Path(__file__).resolve().parent.parent
SITE = REPO / "site"
FIXTURES_DIR = REPO / "tests" / "fixtures" / "frames"
DENSITY_DIR = REPO / "docs" / "density"
SHOTS_DIR = DENSITY_DIR / "shots"

SEED = 20260919
VIEWPORT = {"width": 412, "height": 892}
DPR = 2

# Semantic Level -> Leaflet / Map URL zoom
# z0=World (0.0), z1=Regions (1.5), z2=Countries (2.5), z3=Papers/Deep (4.0)
ZOOM_LEVELS = {
    0: {"zoom": 0.0, "min_labels": 8, "min_landmarks": 1},
    1: {"zoom": 1.5, "min_labels": 6, "min_landmarks": 2},
    2: {"zoom": 2.5, "min_labels": 10, "min_landmarks": 4},
    3: {"zoom": 4.0, "min_labels": 14, "min_landmarks": 8},
}

PINNED_PROBES = [
    {"id": "pinned-stat-isthmus", "x": 829.9, "y": 668.2, "level": 2, "zoom": 2.5, "name": "Statistical Isthmus (Alan link 1)"},
    {"id": "pinned-gen-coast", "x": 1476.3, "y": 676.4, "level": 1, "zoom": 1.8, "name": "Generative Coast (Alan link 2)"},
]

# ---- v2 target (site/v2/index.html, MapLibre). REFACTOR_PLAN §2.2/§2.4: semantic level → MapLibre zoom. The fixture
# files keep their legacy Leaflet `zoom`; for --target v2 the frame's `level` selects the zoom below (x, y are plate
# units in both renderers, so the fixtures are shared unchanged). Thresholds are the §2.4 rows the v2 renderer can
# currently be measured against (labels / landmarks / facts floors, max labels, hard clipped==0 / overlaps==0, font caps).
V2_LEVELS = {
    0: {"zoom": 3.0, "min_labels": 9,  "min_landmarks": 1,  "min_facts": 0, "max_labels": 24, "min_continents": 8},
    1: {"zoom": 4.5, "min_labels": 8,  "min_landmarks": 4,  "min_facts": 0, "max_labels": 30, "min_countries": 3},
    2: {"zoom": 6.0, "min_labels": 14, "min_landmarks": 10, "min_facts": 2, "max_labels": 45, "min_countries": 2},
    3: {"zoom": 7.5, "min_labels": 24, "min_landmarks": 18, "min_facts": 6, "max_labels": 60, "min_countries": 1},
}
V2_FONT_CAPS = {"continent": 42, "country": 28, "landmark": 16, "fact": 13}
V2_FONT_MIN = 11
V2_CLASS_OF_LAYER = {   # symbol layer id → §2.3 label class
    "symbol-continent": "continent", "symbol-ocean": "continent", "symbol-range": "landmark",   # §2.4 z0: min landmarks 1 = the Silicon Range title
    "symbol-country": "country", "symbol-country-hint": "fact", "symbol-country-tag": "fact",
    "symbol-event": "landmark", "symbol-event-z1": "landmark", "symbol-summit": "landmark", "symbol-pass": "landmark", "symbol-fact": "fact",
}
# Phase 4b (task D): at z1 "Regions" the landmarks a reader sees are the lod 1–2 events (symbol-event-z1), the lod ≤ 1
# summits and the country names themselves (§2.4 z1 row: "≥ 3 country names, ≥ 2 summits/passes" ≈ the 4-landmark floor),
# so at level 1 `landmarks` = landmark-class symbols + country labels. `labels.country` stays separate for the country floor.
Z1_COUNTRIES_ARE_LANDMARKS = True

# One page.evaluate per frame (§2.3). Placed symbols = map.queryRenderedFeatures over the symbol layers (only
# uncollided symbols are returned). Text boxes = MapLibre's OWN committed collision boxes (style.placement.collisionIndex
# .grid, viewport px offset by the engine's 100 px viewportPadding) — the authoritative placed extents, so `overlaps`
# is exact and `clipped` (box crosses the viewport by > 2 CSS px after removing the layer's text-padding) is exact.
# Each box resolves to its exact feature through retainedQueryData → featureIndex (layer ids + GeoJSON tile). Font
# sizes: text-size expressions evaluated at the frame zoom by a small evaluator (get/zoom/literal/+/concat/interpolate/
# format — the operators style.json uses). Fallback when the internals are unavailable: canvas measureText boxes.
# NOTE (measured, Phase 4a): MapLibre deliberately places labels inside a 100 px band outside the viewport, so on a
# continuous-pan map some labels always straddle the edge; the §2.3 premise "labels MapLibre already hid don't count"
# does not hold for MapLibre. clipped is reported as measured.
V2_EVAL_JS = r"""(ARGS) => {
  const {classOf} = ARGS;
  // viewport = the MAP CANVAS (Phase 4c task D: the UI chrome is a bottom bar outside the canvas, so the canvas is
  // shorter than the window; collision boxes and projections are in canvas px)
  const cr = map.getCanvas().getBoundingClientRect();
  const vw = cr.width, vh = cr.height, zoom = map.getZoom();
  const style = map.getStyle();
  const symLayers = style.layers.filter(l => l.type === 'symbol');
  const ids = symLayers.map(l => l.id);
  const feats = map.queryRenderedFeatures({layers: ids});
  const canvas = document.createElement('canvas'); const ctx = canvas.getContext('2d');
  const evalAt = (expr, props) => {
    if (expr === undefined || expr === null) return undefined;
    if (typeof expr !== 'object') return expr;
    const ev = e => {
      if (!Array.isArray(e)) return e;
      const op = e[0];
      if (op === 'get') return props[e[1]];
      if (op === 'zoom') return zoom;
      if (op === 'literal') return e[1];
      if (op === '+') return e.slice(1).map(ev).reduce((a, b) => a + b, 0);
      if (op === 'concat') return e.slice(1).map(ev).join('');
      if (op === 'interpolate') {
        const input = ev(e[2]); const stops = [];
        for (let i = 3; i < e.length; i += 2) stops.push([e[i], ev(e[i + 1])]);
        if (input <= stops[0][0]) return stops[0][1];
        for (let i = 1; i < stops.length; i++) if (input <= stops[i][0]) { const [a, va] = stops[i - 1], [b, vb] = stops[i]; return va + (vb - va) * (input - a) / (b - a); }
        return stops[stops.length - 1][1];
      }
      if (op === 'format') { let s = ''; for (let i = 1; i < e.length; i += 2) s += String(ev(e[i])); return s; }
      return e;
    };
    return ev(expr);
  };
  // ---- engine collision boxes (viewport px), keyed by layer id + feature id: MapLibre's committed placement
  // (style.placement.collisionIndex.grid → boxKeys/bboxes; retainedQueryData[bucketInstanceId] → featureIndex →
  // bucketLayerIDs + the GeoJSON tile layer, so every box resolves to its exact feature; 100 px viewportPadding removed)
  const engine = new Map(); let engineBoxes = 0, engineErr = null;
  try {
    const pl = map.style.placement, ci = pl.collisionIndex, g = ci.grid, pad = (g.width - ci.transform.width) / 2;
    for (let i = 0; i < g.boxKeys.length; i++) {
      const k = g.boxKeys[i], rq = pl.retainedQueryData[k.bucketInstanceId]; if (!rq) continue;
      const fi = rq.featureIndex, layersOf = fi.bucketLayerIDs[rq.bucketIndex] || [];
      const vt = fi.loadVTLayers(), lyr = vt['_geojsonTileLayer']; if (!lyr) continue;
      const f = lyr.feature(k.featureIndex);
      const box = {x1: g.bboxes[4 * i] - pad, y1: g.bboxes[4 * i + 1] - pad, x2: g.bboxes[4 * i + 2] - pad, y2: g.bboxes[4 * i + 3] - pad};
      for (const lid of layersOf) { const key = lid + ':' + f.properties.id; /* properties.id (promoteId): tile-local numeric ids differ from query ids */ if (!engine.has(key)) engine.set(key, []); engine.get(key).push(box); }
      engineBoxes++;
    }
  } catch (e) { engineErr = e.message; }
  const seen = new Set(); const boxes = [];
  const counts = {continent: 0, country: 0, landmark: 0, fact: 0}; const kinds = {};
  let clipped = 0, clippedMajor = 0, clippedMajorAnchored = 0, clipMax = 0, minFont = Infinity, maxFont = 0, unmatched = 0; const capViol = []; const majorByLayer = {};
  for (const f of feats) {
    const key = f.layer.id + ':' + f.properties.id;
    if (seen.has(key)) continue; seen.add(key);
    const layer = symLayers.find(l => l.id === f.layer.id); const lay = layer.layout || {};
    const cls = classOf[f.layer.id] || 'landmark';
    counts[cls]++; kinds[f.properties.kind] = (kinds[f.properties.kind] || 0) + 1;
    const size = +evalAt(lay['text-size'], f.properties) || 12;
    const text = String(evalAt(lay['text-field'], f.properties) || '');
    const p = map.project(f.geometry.coordinates);
    const tpad = lay['text-padding'] !== undefined ? lay['text-padding'] : 2;
    let box = null;
    const eb = engine.get(key);
    if (eb && eb.length) {   // a feature can have one box per tile it was placed from; take the one nearest its anchor
      let best = null, bd = Infinity;
      for (const b of eb) { const d = Math.hypot(Math.max(b.x1 - p.x, 0, p.x - b.x2), Math.max(b.y1 - p.y, 0, p.y - b.y2)); if (d < bd) { bd = d; best = b; } }
      box = {x1: best.x1 + tpad, y1: best.y1 + tpad, x2: best.x2 - tpad, y2: best.y2 - tpad, src: 'engine'};
    } else unmatched++;
    if (!box) {   // fallback: canvas measurement of the wrapped text, centred on the anchor
      const fontStack = (lay['text-font'] || ['Lora Regular'])[0];
      ctx.font = `${fontStack.includes('Italic') ? 'italic ' : ''}${size}px "${fontStack.startsWith('Cinzel') ? 'Cinzel' : 'Lora'}", Georgia, serif`;
      const maxW = (lay['text-max-width'] !== undefined ? lay['text-max-width'] : 10) * size, ls = (lay['text-letter-spacing'] || 0) * size;
      const lines = []; for (const para of text.split('\n')) { let line = ''; for (const w of para.split(' ')) { const t = line ? line + ' ' + w : w; if (ctx.measureText(t).width + ls * t.length > maxW && line) { lines.push(line); line = w; } else line = t; } lines.push(line); }
      const w = Math.max(...lines.map(l => ctx.measureText(l).width + ls * l.length)), h = lines.length * (lay['text-line-height'] || 1.2) * size;
      box = {x1: p.x - w / 2, y1: p.y - h / 2, x2: p.x + w / 2, y2: p.y + h / 2, src: 'canvas'};
    }
    Object.assign(box, {text: text.slice(0, 40), cls, layer: f.layer.id, size});
    boxes.push(box);
    if (box.x1 < -2 || box.x2 > vw + 2 || box.y1 < -2 || box.y2 > vh + 2) {
      clipped++;
      const over = Math.max(-box.x1, box.x2 - vw, -box.y1, box.y2 - vh); clipMax = Math.max(clipMax, over);
      const visW = Math.max(0, Math.min(box.x2, vw) - Math.max(box.x1, 0)), visH = Math.max(0, Math.min(box.y2, vh) - Math.max(box.y1, 0));
      if (visW * visH < 0.5 * (box.x2 - box.x1) * (box.y2 - box.y1)) {
        clippedMajor++; majorByLayer[f.layer.id] = (majorByLayer[f.layer.id] || 0) + 1;
        // anchor (the feature's own point) inside the viewport → the label is chopped although its subject is on screen;
        // anchor outside → MapLibre placed a label for an off-screen feature inside its 100 px padding band (pan-in behaviour)
        if (p.x >= 0 && p.x <= vw && p.y >= 0 && p.y <= vh) clippedMajorAnchored++;
      }
    }
    minFont = Math.min(minFont, size); maxFont = Math.max(maxFont, size);
    if (size > ARGS.caps[cls] + 0.01 || size < ARGS.fontMin - 0.01) capViol.push({layer: f.layer.id, size, cls});
  }
  let overlaps = 0; const overlapPairs = [];
  for (let i = 0; i < boxes.length; i++) for (let j = i + 1; j < boxes.length; j++) {
    const a = boxes[i], b = boxes[j];
    if (a.x1 < b.x2 - 0.5 && a.x2 > b.x1 + 0.5 && a.y1 < b.y2 - 0.5 && a.y2 > b.y1 + 0.5) { overlaps++; if (overlapPairs.length < 5) overlapPairs.push([a.text, b.text]); }
  }
  let ink = 0; for (const b of boxes) ink += Math.max(0, Math.min(b.x2, vw) - Math.max(b.x1, 0)) * Math.max(0, Math.min(b.y2, vh) - Math.max(b.y1, 0));
  let land = 0, tot = 0; for (let gx = 0.5; gx < 12; gx++) for (let gy = 0.5; gy < 26; gy++) { tot++; if (map.queryRenderedFeatures([gx * vw / 12, gy * vh / 26], {layers: ['continent-fill']}).length) land++; }
  const total = counts.continent + counts.country + counts.landmark + counts.fact;
  const html = document.querySelectorAll('.maplibregl-marker, .leaflet-marker-icon').length;
  return {visibleLabels: total, labels: counts, kinds, landmarks: counts.landmark, facts: counts.fact, clipped, clipped_major: clippedMajor, clipped_major_anchored: clippedMajorAnchored,
          clipped_major_by_layer: majorByLayer, clip_max_px: Math.round(clipMax), overlaps, overlapPairs,
          box_source: engineBoxes ? 'engine' : 'canvas', unmatched_boxes: unmatched, engine_boxes: engineBoxes, engine_error: engineErr,
          min_font_px: isFinite(minFont) ? minFont : null, max_font_px: maxFont || null, font_cap_violations: capViol.slice(0, 5),
          ink_ratio: ink / (vw * vh), sea_ratio: 1 - land / tot, html_markers: html, zoom, sampleTexts: boxes.slice(0, 10).map(b => b.text)};
}"""

# Approximate Plate Bounds & Land Mass Bounding Boxes (in plate coordinates)
# Used to seed deterministic land sampling points across the continents
LAND_REGIONS = [
    {"name": "cybernetic-shore", "bbox": [160, 450, 320, 670]},
    {"name": "symbolic-heartland", "bbox": [250, 410, 470, 680]},
    {"name": "winter-steppes", "bbox": [440, 370, 690, 520]},
    {"name": "connectionist-revival", "bbox": [510, 510, 760, 730]},
    {"name": "statistical-isthmus", "bbox": [590, 420, 990, 690]},
    {"name": "deep-learning-basin", "bbox": [800, 480, 1200, 780]},
    {"name": "transformer-plateau", "bbox": [1090, 330, 1440, 700]},
    {"name": "generative-coast", "bbox": [1300, 70, 1620, 890]},
]

class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *a, **k): pass

def generate_frame_fixtures(n_per_level=25):
    FIXTURES_DIR.mkdir(parents=True, exist_ok=True)
    rng = random.Random(SEED)
    fixtures = {}
    
    for level, cfg in ZOOM_LEVELS.items():
        frames = []
        # Prepend pinned probes matching this level
        for p in PINNED_PROBES:
            if p["level"] == level or (level == 2 and p["id"] == "pinned-stat-isthmus") or (level == 1 and p["id"] == "pinned-gen-coast"):
                frames.append({
                    "id": p["id"],
                    "x": p["x"],
                    "y": p["y"],
                    "zoom": p["zoom"],
                    "level": level,
                    "pinned": True,
                    "name": p["name"],
                })
        
        # Sample across land regions
        count = len(frames)
        while count < n_per_level:
            region = rng.choice(LAND_REGIONS)
            bx0, by0, bx1, by1 = region["bbox"]
            px = round(rng.uniform(bx0, bx1), 1)
            py = round(rng.uniform(by0, by1), 1)
            frames.append({
                "id": f"z{level}-{count:03d}",
                "x": px,
                "y": py,
                "zoom": cfg["zoom"],
                "level": level,
                "pinned": False,
                "name": region["name"],
            })
            count += 1
            
        fixture_path = FIXTURES_DIR / f"z{level}.json"
        fixture_path.write_text(json.dumps(frames, indent=2) + "\n")
        fixtures[level] = frames
        print(f"Generated fixture for z{level}: {len(frames)} frames -> {fixture_path}")
        
    return fixtures

def load_frame_fixtures():
    fixtures = {}
    for level in ZOOM_LEVELS:
        p = FIXTURES_DIR / f"z{level}.json"
        if not p.exists():
            return None
        fixtures[level] = json.loads(p.read_text())
    return fixtures

EVAL_JS = """() => {
    const vw = window.innerWidth;
    const vh = window.innerHeight;
    
    // Find all visible text elements inside Leaflet or SVG
    const texts = Array.from(document.querySelectorAll('text, .leaflet-marker-icon, .country-label, .cname, .kname, .kev-name, .thr-name, .thr-title'));
    
    let visibleLabels = 0;
    let landmarks = 0;
    let clipped = 0;
    let labelTexts = [];
    
    const boxes = [];
    
    for (const el of texts) {
        const rect = el.getBoundingClientRect();
        if (rect.width === 0 || rect.height === 0) continue;
        
        // Check if inside or intersecting viewport
        const inViewport = (
            rect.right > 0 && rect.left < vw &&
            rect.bottom > 0 && rect.top < vh
        );
        if (!inViewport) continue;
        
        visibleLabels++;
        const str = el.textContent ? el.textContent.trim() : '';
        if (str) labelTexts.push(str.slice(0, 30));
        
        if (el.classList.contains('kev-name') || el.classList.contains('thr-name') || el.classList.contains('thr-dot') || el.classList.contains('kev-dot')) {
            landmarks++;
        }
        
        // Clipped check: crosses edge by > 4px
        if (rect.left < -4 || rect.right > vw + 4 || rect.top < -4 || rect.bottom > vh + 4) {
            clipped++;
        }
        
        boxes.push({x1: rect.left, y1: rect.top, x2: rect.right, y2: rect.bottom, text: str});
    }
    
    // Also count SVG landmark dots
    const dots = Array.from(document.querySelectorAll('.kev-dot, .thr-dot'));
    for (const d of dots) {
        const rect = d.getBoundingClientRect();
        if (rect.right > 0 && rect.left < vw && rect.bottom > 0 && rect.top < vh) {
            landmarks++;
        }
    }
    
    // Overlap detection
    let overlaps = 0;
    for (let i = 0; i < boxes.length; i++) {
        for (let j = i + 1; j < boxes.length; j++) {
            const a = boxes[i], b = boxes[j];
            if (a.x1 < b.x2 - 1 && a.x2 > b.x1 + 1 && a.y1 < b.y2 - 1 && a.y2 > b.y1 + 1) {
                overlaps++;
            }
        }
    }
    
    return {
        visibleLabels,
        landmarks,
        clipped,
        overlaps,
        sampleTexts: labelTexts.slice(0, 10)
    };
}"""

def run_sampler(port=8992, save_shots=True):
    from playwright.sync_api import sync_playwright
    
    fixtures = load_frame_fixtures()
    if not fixtures:
        print("Fixtures not found, generating...")
        fixtures = generate_frame_fixtures(25)
        
    DENSITY_DIR.mkdir(parents=True, exist_ok=True)
    if save_shots:
        SHOTS_DIR.mkdir(parents=True, exist_ok=True)
        
    httpd = ThreadingHTTPServer(("127.0.0.1", port), partial(QuietHandler, directory=str(SITE)))
    httpd.daemon_threads = True
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    
    results = {}
    total_frames = 0
    failing_frames = 0
    worst_frames = []
    
    try:
        with sync_playwright() as p:
            b = p.chromium.launch()
            for level, frames in fixtures.items():
                cfg = ZOOM_LEVELS[level]
                level_results = []
                print(f"\n--- Testing Semantic Level z{level} (Target Zoom {cfg['zoom']}) ---")
                
                for f in frames:
                    total_frames += 1
                    pg = b.new_page(viewport=VIEWPORT, device_scale_factor=DPR)
                    url = f"http://127.0.0.1:{port}/index.html?z={f['zoom']}&x={f['x']}&y={f['y']}"
                    
                    try:
                        pg.goto(url, wait_until="networkidle", timeout=15000)
                        pg.wait_for_timeout(1000)
                        metrics = pg.evaluate(EVAL_JS)
                    except Exception as e:
                        metrics = {"visibleLabels": 0, "landmarks": 0, "clipped": 0, "overlaps": 0, "sampleTexts": [], "error": str(e)}
                        
                    # Evaluate density floors
                    failed_reasons = []
                    if metrics["visibleLabels"] < cfg["min_labels"]:
                        failed_reasons.append(f"labels={metrics['visibleLabels']} < min={cfg['min_labels']}")
                    if metrics["landmarks"] < cfg["min_landmarks"]:
                        failed_reasons.append(f"landmarks={metrics['landmarks']} < min={cfg['min_landmarks']}")
                    if metrics["clipped"] > 3:
                        failed_reasons.append(f"clipped_labels={metrics['clipped']} > 3")
                    if metrics["overlaps"] > 2:
                        failed_reasons.append(f"overlaps={metrics['overlaps']} > 2")
                        
                    is_pass = len(failed_reasons) == 0
                    if not is_pass:
                        failing_frames += 1
                        worst_frames.append({
                            "id": f["id"],
                            "name": f["name"],
                            "x": f["x"],
                            "y": f["y"],
                            "level": level,
                            "zoom": f["zoom"],
                            "metrics": metrics,
                            "reasons": failed_reasons
                        })
                        if save_shots:
                            shot_path = SHOTS_DIR / f"fail_{f['id']}.png"
                            pg.screenshot(path=str(shot_path))
                            
                    status_str = "PASS" if is_pass else f"FAIL ({', '.join(failed_reasons)})"
                    print(f"  Frame {f['id']:20s} [{f['name']:25s}] (x={f['x']}, y={f['y']}): {status_str} | texts: {metrics['sampleTexts'][:3]}")
                    
                    level_results.append({
                        "frame": f,
                        "metrics": metrics,
                        "passed": is_pass,
                        "reasons": failed_reasons
                    })
                    pg.close()
                    
                results[f"z{level}"] = level_results
            b.close()
    finally:
        httpd.shutdown()
        
    pass_rate = (total_frames - failing_frames) / total_frames if total_frames else 0
    report = {
        "timestamp": time.time(),
        "total_frames": total_frames,
        "failing_frames": failing_frames,
        "pass_rate": pass_rate,
        "worst_frames": worst_frames[:15],
    }
    
    report_file = DENSITY_DIR / "baseline.json"
    report_file.write_text(json.dumps(report, indent=2) + "\n")
    print(f"\n=====================================================================")
    print(f"SAMPLER FINISHED: {total_frames} frames tested | Pass Rate: {pass_rate*100:.1f}%")
    print(f"Baseline report written to: {report_file}")
    print(f"=====================================================================\n")
    
    return pass_rate >= 0.95


def _v2_judge(level, m):
    """§2.4 row for the level → (hard_failures, soft_failures). Hard: clipped_major==0 (planner decision, Phase 4b: a
    placed label with < 50 % of its box inside the viewport — the "giant half-cut banner"; raw `clipped` = any box over
    the edge by > 2 px stays reported, not gated, because MapLibre places symbols in a 100 px band outside the viewport),
    overlaps==0, font caps, no HTML markers, page error. Soft: density floors/ceilings (reported, not blocking here)."""
    cfg = V2_LEVELS[level]
    hard, soft = [], []
    if m.get("error"):
        hard.append(f"page error: {m['error'][:80]}")
        return hard, soft
    # Phase 4c planner decision: hard gate = clipped_major_anchored == 0 (label whose ANCHOR is inside the viewport but
    # < 50 % of its box is visible). Major clips of off-screen anchors are MapLibre's 100 px padding band: reported only.
    if m.get("clipped_major_anchored", 0) > 0:
        hard.append(f"clipped_major_anchored={m['clipped_major_anchored']}")
    if m["overlaps"] > 0:
        hard.append(f"overlaps={m['overlaps']}")
    if m.get("font_cap_violations"):
        hard.append(f"font caps: {m['font_cap_violations'][:2]}")
    if m.get("html_markers"):
        hard.append(f"html_markers={m['html_markers']}")
    # land frame = sea_ratio ≤ 0.6 (§2.4). Measured: on a 412×892 portrait phone the z0 frame (whole plate) and the z1
    # frame (≈640×1385 units vs a ≈560-unit-tall land band) can never reach 40 % land, so z0/z1 floors apply to every
    # frame (the §2.4 z0 row already says "whole plate fits"); z2/z3 floors apply to land frames only.
    land = m["sea_ratio"] <= 0.6 or level <= 1
    if land:
        if m["visibleLabels"] < cfg["min_labels"]:
            soft.append(f"labels={m['visibleLabels']} < {cfg['min_labels']}")
        if m["visibleLabels"] > cfg["max_labels"]:
            soft.append(f"labels={m['visibleLabels']} > {cfg['max_labels']}")
        if m["landmarks"] < cfg["min_landmarks"]:
            soft.append(f"landmarks={m['landmarks']} < {cfg['min_landmarks']}")
        if m["facts"] < cfg["min_facts"]:
            soft.append(f"facts={m['facts']} < {cfg['min_facts']}")
        if "min_continents" in cfg and m["labels"]["continent"] < cfg["min_continents"]:
            soft.append(f"continents={m['labels']['continent']} < {cfg['min_continents']}")
        if "min_countries" in cfg and m["labels"]["country"] < cfg["min_countries"]:
            soft.append(f"countries={m['labels']['country']} < {cfg['min_countries']}")
    return hard, soft


def run_sampler_v2(port=8992, save_shots=True, levels=None, report_name="v2-phase4a.json"):
    """--target v2: drive site/v2/index.html (MapLibre) over the same fixtures; §2.3 metrics from queryRenderedFeatures.
    Writes docs/density/<report_name> (per frame) and docs/density/summary.md (per level). Returns True iff every frame
    passes the hard gates (soft pass rate is reported, not enforced, until Phase 2 content lands)."""
    from playwright.sync_api import sync_playwright
    fixtures = load_frame_fixtures()
    if not fixtures:
        print("Fixtures not found; run --generate first")
        return False
    if levels is not None:
        fixtures = {l: fr for l, fr in fixtures.items() if l in levels}
    DENSITY_DIR.mkdir(parents=True, exist_ok=True)
    if save_shots:
        SHOTS_DIR.mkdir(parents=True, exist_ok=True)
    httpd = ThreadingHTTPServer(("127.0.0.1", port), partial(QuietHandler, directory=str(SITE)))
    httpd.daemon_threads = True
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    per_level, records = {}, []
    ext_requests, console_errors = set(), []
    t0 = time.time()
    try:
        with sync_playwright() as p:
            b = p.chromium.launch()
            ctx = b.new_context(viewport=VIEWPORT, device_scale_factor=DPR)
            ctx.on("request", lambda r: ext_requests.add(r.url) if not (r.url.startswith(f"http://127.0.0.1:{port}") or r.url.startswith("blob:http://127.0.0.1")) else None)
            for level, frames in fixtures.items():
                cfg = V2_LEVELS[level]
                stats = {"n": 0, "land": 0, "hard_fail": 0, "soft_fail": 0, "pass": 0, "reasons": {}}
                print(f"\n--- v2 level z{level} (MapLibre zoom {cfg['zoom']}) ---")
                for f in frames:
                    zoom = cfg["zoom"]
                    url = f"http://127.0.0.1:{port}/v2/index.html?test=1&z={zoom}&x={f['x']}&y={f['y']}"
                    pg = ctx.new_page()
                    errs = []
                    pg.on("console", lambda msg, errs=errs: errs.append(msg.text) if msg.type == "error" and "GL Driver" not in msg.text else None)
                    pg.on("pageerror", lambda e, errs=errs: errs.append(str(e)))
                    try:
                        pg.goto(url, wait_until="load", timeout=20000)
                        pg.wait_for_function("window.__idle === true", timeout=30000)
                        m = pg.evaluate(V2_EVAL_JS, {"classOf": V2_CLASS_OF_LAYER, "caps": V2_FONT_CAPS, "fontMin": V2_FONT_MIN})
                    except Exception as e:
                        m = {"visibleLabels": 0, "labels": {"continent": 0, "country": 0, "landmark": 0, "fact": 0}, "landmarks": 0, "facts": 0,
                             "clipped": 0, "clipped_major": 0, "clipped_major_anchored": 0, "overlaps": 0, "sea_ratio": 1, "sampleTexts": [], "error": str(e)}
                    if errs:
                        m["console_errors"] = errs[:3]
                        console_errors.extend(errs[:3])
                    if level == 1 and Z1_COUNTRIES_ARE_LANDMARKS and not m.get("error"):
                        m["landmarks_symbols"] = m["landmarks"]
                        m["landmarks"] = m["labels"]["landmark"] + m["labels"]["country"]
                    hard, soft = _v2_judge(level, m)
                    land = m["sea_ratio"] <= 0.6 or level <= 1
                    stats["n"] += 1
                    stats["land"] += land
                    if hard:
                        stats["hard_fail"] += 1
                    elif soft:
                        stats["soft_fail"] += 1
                    elif land:
                        stats["pass"] += 1
                    for r in hard + soft:
                        k = r.split("=")[0].split(":")[0].strip()
                        stats["reasons"][k] = stats["reasons"].get(k, 0) + 1
                    rec = {"id": f["id"], "name": f.get("name"), "level": level, "zoom": zoom, "x": f["x"], "y": f["y"], "pinned": f.get("pinned", False),
                           "link": f"v2/index.html?z={zoom}&x={f['x']}&y={f['y']}", "land_frame": land, "metrics": m, "hard": hard, "soft": soft,
                           "passed": not hard and not soft}
                    records.append(rec)
                    tag = "HARD-FAIL" if hard else ("soft-fail" if soft else ("PASS" if land else "sea (skipped floors)"))
                    print(f"  {f['id']:20s} z{zoom} x={f['x']:<7} y={f['y']:<6} labels={m['visibleLabels']:>2} lm={m['landmarks']:>2} facts={m['facts']:>2} "
                          f"clip={m['clipped']}/{m.get('clipped_major', 0)}/{m.get('clipped_major_anchored', 0)} ovl={m['overlaps']} sea={m['sea_ratio']:.2f} {tag} {'; '.join((hard + soft)[:3])}")
                    if save_shots and (hard or f.get("pinned")):
                        pg.screenshot(path=str(SHOTS_DIR / f"v2-{'hardfail' if hard else 'pinned'}_{f['id']}.png"))
                    pg.close()
                per_level[f"z{level}"] = stats
            b.close()
    finally:
        httpd.shutdown()
    total = len(records)
    hard_fails = sum(1 for r in records if r["hard"])
    land_recs = [r for r in records if r["land_frame"]]
    report = {
        "timestamp": time.time(), "target": "v2", "renderer": "site/v2/index.html (MapLibre GL JS)", "viewport": VIEWPORT, "dpr": DPR,
        "levels": {f"z{l}": V2_LEVELS[l] for l in fixtures}, "total_frames": total, "land_frames": len(land_recs),
        "hard_gate_failures": hard_fails, "soft_pass_rate_land": (sum(1 for r in land_recs if r["passed"]) / len(land_recs)) if land_recs else None,
        "external_requests": sorted(ext_requests), "console_errors": console_errors[:20], "seconds": round(time.time() - t0, 1),
        "per_level": {}, "frames": records,
    }
    for lk, s in per_level.items():
        report["per_level"][lk] = dict(s, pass_rate_land=(s["pass"] / s["land"]) if s["land"] else None)
    (DENSITY_DIR / report_name).write_text(json.dumps(report, indent=1) + "\n")
    # ---- summary.md
    lines = [f"# Density sampler — v2 (MapLibre) — {time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime())}", "",
             f"Renderer `site/v2/index.html`, {VIEWPORT['width']}×{VIEWPORT['height']} CSS px @ DPR {DPR}, {total} fixture frames "
             f"({len(land_recs)} land frames with sea_ratio ≤ 0.6), {report['seconds']} s.", "",
             f"Hard gates (clipped_major_anchored==0, overlaps==0, font caps, no HTML markers): **{total - hard_fails}/{total} frames pass**.",
             f"External (non-localhost) requests: {len(ext_requests)}. Console errors: {len(console_errors)}.", "",
             "| level | MapLibre z | frames | land | pass | soft-fail | HARD-fail | pass rate (land) | p50 labels / landmarks / facts / clipped / clipped_major / major_anchored | p50 sea | top failure reasons |", "|---|---|---|---|---|---|---|---|---|---|---|"]
    def p50(lv, key):
        vals = sorted(r["metrics"].get(key, 0) for r in records if r["level"] == lv)
        return vals[len(vals) // 2] if vals else 0
    for lk, s in report["per_level"].items():
        lv = int(lk[1])
        pr = "–" if s["pass_rate_land"] is None else f"{100 * s['pass_rate_land']:.0f}%"
        top = ", ".join(f"{k}×{v}" for k, v in sorted(s["reasons"].items(), key=lambda kv: -kv[1])[:4])
        lines.append(f"| {lk} | {V2_LEVELS[lv]['zoom']} | {s['n']} | {s['land']} | {s['pass']} | {s['soft_fail']} | {s['hard_fail']} | {pr} | "
                     f"{p50(lv, 'visibleLabels')} / {p50(lv, 'landmarks')} / {p50(lv, 'facts')} / {p50(lv, 'clipped')} / {p50(lv, 'clipped_major')} / {p50(lv, 'clipped_major_anchored')} | {p50(lv, 'sea_ratio'):.2f} | {top} |")
    lines += ["", "## Worst 10 frames", "", "| frame | level | labels | landmarks | facts | clip/major/anchored | ovl | sea | reasons | link |", "|---|---|---|---|---|---|---|---|---|---|"]
    def badness(r):
        return (len(r["hard"]) * 100 + len(r["soft"]) * 10 - r["metrics"]["visibleLabels"] * 0.1) if r["land_frame"] else -1
    for r in sorted(records, key=badness, reverse=True)[:10]:
        m = r["metrics"]
        lines.append(f"| {r['id']} | z{r['level']} | {m['visibleLabels']} | {m['landmarks']} | {m['facts']} | {m['clipped']}/{m.get('clipped_major', 0)}/{m.get('clipped_major_anchored', 0)} | {m['overlaps']} | {m['sea_ratio']:.2f} | "
                     f"{'; '.join(r['hard'] + r['soft'])[:90]} | [`?z={r['zoom']}&x={r['x']}&y={r['y']}`]({r['link']}) |")
    lines += ["", "## Measurement notes", "",
              "- `labels`/`landmarks`/`facts` = symbols MapLibre actually placed (`queryRenderedFeatures` over the symbol layers, deduped by layer+feature id).",
              "- `overlaps`/`clipped` use MapLibre's own committed collision boxes (exact placed extents, text-padding removed).",
              "- `clipped` counts every placed label whose box crosses the viewport edge by > 2 CSS px. MapLibre places symbols inside a fixed 100 px band",
              "  outside the viewport and has no option to suppress edge-straddling labels, so on a continuous-pan map this count is structurally > 0 whenever",
              "  labels exist near the frame edge. Planner decision (Phase 4c, supersedes 4b): the HARD gate is `clipped_major_anchored == 0` — a placed",
              "  label whose anchor point is inside the viewport but < 50 % of its box is visible (the half-cut banner of an on-screen subject). Raw",
              "  `clipped` and `clipped_major` (which includes labels of off-screen anchors in MapLibre's padding band) are reported, not gated.",
              "- z0/z1 frames on a portrait phone can never reach sea_ratio ≤ 0.6 (the land band is ≈560 units tall vs a 1385–3920-unit frame), so their",
              "  density floors are applied to every frame; z2/z3 floors apply to land frames only.",
              "- z1 `landmarks` = landmark-class symbols (lod 1–2 events, lod ≤ 1 summits) + country names (Phase 4b task D); `landmarks_symbols` in the JSON",
              "  is the symbol-only count."]
    (DENSITY_DIR / "summary.md").write_text("\n".join(lines) + "\n")
    print(f"\nv2 sampler: {total} frames, hard-gate failures {hard_fails}, soft pass rate (land) "
          f"{(100 * report['soft_pass_rate_land']) if report['soft_pass_rate_land'] is not None else 0:.1f}% → {DENSITY_DIR / report_name}, {DENSITY_DIR / 'summary.md'}")
    return hard_fails == 0 and not ext_requests

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--generate", action="store_true", help="Regenerate frame fixtures")
    ap.add_argument("--port", type=int, default=8992)
    ap.add_argument("--target", choices=["legacy", "v2"], default="legacy", help="legacy = site/index.html (Leaflet tiles); v2 = site/v2/index.html (MapLibre)")
    ap.add_argument("--levels", default=None, help="comma-separated semantic levels to run (v2 only), e.g. 1,2")
    ap.add_argument("--no-shots", action="store_true")
    ap.add_argument("--report", default="v2-phase4a.json", help="v2 only: report file name under docs/density/")
    args = ap.parse_args()
    
    if args.generate:
        generate_frame_fixtures(25)
        sys.exit(0)
        
    if args.target == "v2":
        levels = [int(l) for l in args.levels.split(",")] if args.levels else None
        success = run_sampler_v2(port=args.port, save_shots=not args.no_shots, levels=levels, report_name=args.report)
        sys.exit(0 if success else 1)
    success = run_sampler(port=args.port)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
