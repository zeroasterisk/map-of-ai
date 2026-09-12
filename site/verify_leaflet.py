#!/usr/bin/env python3
"""Prove real pan/zoom on the Leaflet map (site/index.html): screenshot initial view, dispatch scroll-wheel zoom and a
mouse drag, screenshot again, and print the map's zoom/center before and after plus tile-request stats.
Usage: PLAYWRIGHT_BROWSERS_PATH=... LD_LIBRARY_PATH=... /tmp/pwvenv/bin/python site/verify_leaflet.py [--url URL] [--out /tmp/leaflet]"""
import argparse, json, threading
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from playwright.sync_api import sync_playwright

SITE = Path(__file__).resolve().parent
ap = argparse.ArgumentParser(); ap.add_argument("--url"); ap.add_argument("--out", default="/tmp/leaflet"); ap.add_argument("--port", type=int, default=8794)
a = ap.parse_args(); out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
url = a.url
if not url:
    httpd = ThreadingHTTPServer(("127.0.0.1", a.port), partial(SimpleHTTPRequestHandler, directory=str(SITE))); httpd.daemon_threads = True
    threading.Thread(target=httpd.serve_forever, daemon=True).start(); url = f"http://127.0.0.1:{a.port}/"
# labels are baked into the tiles per level of detail (LEAFLET v2); report which pyramid levels the loaded tiles come from
STATE = "() => { const m = window.MAP; const c = m.getCenter(); const lv = {}; document.querySelectorAll('img.leaflet-tile-loaded').forEach(i => { const k = (i.src.match(/tiles\\/(\\d)\\//) || [])[1]; lv[k] = (lv[k] || 0) + 1; }); return {zoom: m.getZoom(), center: [c.lng, -c.lat], tiles: document.querySelectorAll('img.leaflet-tile-loaded').length, levels: lv}; }"
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1500, "height": 800})
    errors, tiles = [], []
    pg.on("pageerror", lambda e: errors.append(str(e))); pg.on("response", lambda r: tiles.append((r.url, r.status)) if "/tiles/" in r.url else None)
    pg.goto(url, wait_until="networkidle"); pg.wait_for_function("window.MAP && document.querySelectorAll('img.leaflet-tile-loaded').length > 0"); pg.wait_for_timeout(1500)
    s0 = pg.evaluate(STATE); pg.screenshot(path=str(out / "1_initial.png")); print("initial", json.dumps(s0))
    box = pg.locator("#map").bounding_box(); cx, cy = box["x"] + box["width"] * .62, box["y"] + box["height"] * .5
    pg.mouse.move(cx, cy)
    for _ in range(6): pg.mouse.wheel(0, -120); pg.wait_for_timeout(120)
    pg.wait_for_timeout(1200); pg.wait_for_load_state("networkidle"); pg.wait_for_timeout(600)
    s1 = pg.evaluate(STATE); pg.screenshot(path=str(out / "2_after_wheel_zoom.png")); print("after wheel", json.dumps(s1))
    pg.mouse.move(cx, cy); pg.mouse.down()
    for i in range(1, 21): pg.mouse.move(cx - 18 * i, cy + 6 * i); pg.wait_for_timeout(15)
    pg.mouse.up(); pg.wait_for_timeout(900); pg.wait_for_load_state("networkidle"); pg.wait_for_timeout(400)
    s2 = pg.evaluate(STATE); pg.screenshot(path=str(out / "3_after_drag.png")); print("after drag", json.dumps(s2))
    pg.evaluate("() => window.MAP.setZoom(window.MAP.getMaxZoom())"); pg.wait_for_timeout(1500); pg.wait_for_load_state("networkidle")
    s3 = pg.evaluate(STATE); pg.screenshot(path=str(out / "4_max_zoom.png")); print("max zoom", json.dumps(s3))
    # the Deep Learning Basin (plate ~1000,450) at zoom 2: level-2 tiles carry country borders + names
    pg.evaluate("() => window.MAP.setView(L.latLng(-450, 1000), 2)")
    pg.wait_for_timeout(1500); pg.wait_for_load_state("networkidle"); pg.screenshot(path=str(out / "5_zoom2_basin.png")); print("zoom2 basin", json.dumps(pg.evaluate(STATE)))
    b.close()
bad = [t for t in tiles if t[1] != 200]
print(f"tile requests {len(tiles)}, non-200 {len(bad)} {bad[:5]}; js errors {errors}")
assert not errors and s1["zoom"] > s0["zoom"] and s2["center"] != s1["center"] and not bad, "pan/zoom did not change state or tiles failed"
print("PASS: wheel zoom raised zoom, drag moved center, all tiles 200")
