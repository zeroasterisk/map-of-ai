#!/usr/bin/env python3
"""Dev aid (LOD pilot): the ON-SCREEN pixel height of rendered text per lod level. Each level z is screenshotted at
device_scale_factor 2**z by build_tiles.py, so screen px = getBoundingClientRect().height (CSS px = plate units in
tilesrc mode) * 2**z. Prints the median height per text class per level and a few named samples that are visible at
several levels (same event / country), so text growth across zoom can be checked numerically.
Run: /tmp/pwvenv/bin/python site/measure_lod_text.py [--zmax 4]"""
import argparse, json, statistics, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_tiles import serve, SITE, PLATE

JS = """() => [...document.querySelectorAll('svg#map text')].filter(t => t.getClientRects().length).filter(t => /^(kname|ktag|ksub|kyrs|khint|kev-name|kev-year|kev-line)$/.test(t.getAttribute('class') || ''))
  .map(t => ({c: t.getAttribute('class'), s: t.textContent, f: t.dataset.for, e: t.dataset.ev, h: t.getBoundingClientRect().height, fs: +t.getAttribute('font-size') / (t.parentNode.getAttribute && /scale\\(([\\d.]+)\\)/.test(t.parentNode.getAttribute('transform') || '') ? 1 / +RegExp.$1 : 1)}))"""
ap = argparse.ArgumentParser(); ap.add_argument("--zmax", type=int, default=4); ap.add_argument("--port", type=int, default=8796)
ap.add_argument("--json", default=None); a = ap.parse_args()
from playwright.sync_api import sync_playwright
httpd = serve(SITE, a.port); res = {}
try:
    with sync_playwright() as p:
        b = p.chromium.launch()
        for lod in range(1, a.zmax + 1):
            pg = b.new_page(viewport={"width": PLATE[0], "height": PLATE[1]}, device_scale_factor=2 ** lod)
            pg.goto(f"http://127.0.0.1:{a.port}/atlas.html?tilesrc=1&lod={lod}", wait_until="networkidle"); pg.wait_for_timeout(1500)
            rows = pg.evaluate(JS); s = 2 ** lod
            for r in rows: r["px"] = round(r["h"] * s, 1); r["fs_px"] = round(r["fs"] * s, 1)
            res[lod] = rows; pg.close()
            by = {}
            for r in rows: by.setdefault(r["c"], []).append(r["px"])
            print(f"lod{lod} (device scale {s}x): " + ", ".join(f"{c}: median {statistics.median(v):.1f}px screen bbox height (n={len(v)})" for c, v in sorted(by.items())))
        b.close()
finally:
    httpd.shutdown()
# named samples visible at >= 2 levels
print("\nsame text across levels (screen px bbox height / font-size in screen px):")
seen = {}
for lod, rows in res.items():
    for r in rows: seen.setdefault((r["c"], r["s"]), {})[lod] = (r["px"], r["fs_px"])
shown = 0
for (c, s), d in sorted(seen.items()):
    if len(d) < 2 or shown >= 14: continue
    shown += 1; print(f"  {c:9s} {s[:34]:34s} " + "  ".join(f"lod{l}: {v[0]}px (fs {v[1]})" for l, v in sorted(d.items())))
if a.json: Path(a.json).write_text(json.dumps({str(k): v for k, v in res.items()}, indent=0))
