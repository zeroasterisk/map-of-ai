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
    {"id": "pinned-stat-isthmus", "x": 829.9, "y": 668.2, "level": 2, "zoom": 2.5, "name": "Statistical Isthmus (Pinned Probe 1)"},
    {"id": "pinned-gen-coast", "x": 1476.3, "y": 676.4, "level": 1, "zoom": 1.8, "name": "Generative Coast (Pinned Probe 2)"},
]

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
  fixtures = load_frame_fixtures()
  if not fixtures:
    print("Fixtures not found, generating...")
    fixtures = generate_frame_fixtures(25)

  DENSITY_DIR.mkdir(parents=True, exist_ok=True)

  httpd = ThreadingHTTPServer(
      ("127.0.0.1", port), partial(QuietHandler, directory=str(SITE))
  )
  httpd.daemon_threads = True
  threading.Thread(target=httpd.serve_forever, daemon=True).start()

  results = {}
  total_frames = 0
  failing_frames = 0
  worst_frames = []

  try:
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
      b = p.chromium.launch()
      pg = b.new_page(viewport=VIEWPORT, device_scale_factor=DPR)
      pg.goto(
          f"http://127.0.0.1:{port}/index.html",
          wait_until="networkidle",
          timeout=15000,
      )
      for level, frames in fixtures.items():
        cfg = ZOOM_LEVELS[level]
        level_results = []
        print(
            f"\n--- Testing Semantic Level z{level} (Target Zoom"
            f" {cfg['zoom']}) ---"
        )
        for f in frames:
          total_frames += 1
          try:
            pg.evaluate(
                "(f) => { window.__ATLAS.map.setView("
                "window.__ATLAS.P(f.x, f.y), f.zoom, {animate: false});"
                " window.__ATLAS.renderViewportLabels(); }",
                f,
            )
            metrics = pg.evaluate(EVAL_JS)
          except Exception as e:
            metrics = {
                "visibleLabels": 0,
                "landmarks": 0,
                "clipped": 0,
                "overlaps": 0,
                "sampleTexts": [],
                "error": str(e),
            }
          failed_reasons = []
          if metrics["visibleLabels"] < cfg["min_labels"]:
            failed_reasons.append(
                f"labels={metrics['visibleLabels']} < min={cfg['min_labels']}"
            )
          if metrics["landmarks"] < cfg["min_landmarks"]:
            failed_reasons.append(
                f"landmarks={metrics['landmarks']} <"
                f" min={cfg['min_landmarks']}"
            )
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
                "reasons": failed_reasons,
            })
            if save_shots:
              SHOTS_DIR.mkdir(parents=True, exist_ok=True)
              pg.screenshot(path=str(SHOTS_DIR / f"fail_{f['id']}.png"))
          status_str = (
              "PASS" if is_pass else f"FAIL ({', '.join(failed_reasons)})"
          )
          print(
              f"  Frame {f['id']:20s} [{f['name']:25s}] (x={f['x']},"
              f" y={f['y']}): {status_str} | texts:"
              f" {metrics['sampleTexts'][:3]}"
          )
          level_results.append({
              "frame": f,
              "metrics": metrics,
              "passed": is_pass,
              "reasons": failed_reasons,
          })
        results[f"z{level}"] = level_results
      pg.close()
      b.close()
  finally:
    httpd.shutdown()

  pass_rate = (
      (total_frames - failing_frames) / total_frames if total_frames else 0
  )
  report_file = DENSITY_DIR / "baseline.json"
  ts = time.time()
  if report_file.exists():
    try:
      prev = json.loads(report_file.read_text())
      if (
          prev.get("total_frames") == total_frames
          and prev.get("failing_frames") == failing_frames
          and prev.get("pass_rate") == pass_rate
          and prev.get("worst_frames") == worst_frames[:15]
      ):
        ts = prev.get("timestamp", ts)
    except Exception:
      pass
  report = {
      "timestamp": ts,
      "total_frames": total_frames,
      "failing_frames": failing_frames,
      "pass_rate": pass_rate,
      "worst_frames": worst_frames[:15],
  }

  report_file.write_text(json.dumps(report, indent=2) + "\n")
  print(f"\n=====================================================================")
  print(f"SAMPLER FINISHED: {total_frames} frames tested | Pass Rate: {pass_rate*100:.1f}%")
  print(f"Baseline report written to: {report_file}")
  print(f"=====================================================================\n")

  return pass_rate >= 0.95

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--generate", action="store_true", help="Regenerate frame fixtures")
    ap.add_argument("--port", type=int, default=8992)
    args = ap.parse_args()
    
    if args.generate:
        generate_frame_fixtures(25)
        sys.exit(0)
        
    success = run_sampler(port=args.port)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
