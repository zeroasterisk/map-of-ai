#!/usr/bin/env python3
"""Gate for the deep-link URL scheme (docs/URL_SCHEME.md) on site/index.html.
(a) ?place=deep-learning-basin centers on the anchor, (b) ?z=2&x=1000&y=400 gives that exact view, (c) pan/zoom
rewrites the URL to the precise form, (d) the copy-link button puts location.href on the clipboard. Exit 1 on failure.
Usage: PLAYWRIGHT_BROWSERS_PATH=... LD_LIBRARY_PATH=... /tmp/pwvenv/bin/python site/check_url.py [--url BASE] [--out DIR]"""
import argparse, json, sys, threading
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from playwright.sync_api import sync_playwright

SITE = Path(__file__).resolve().parent
ap = argparse.ArgumentParser(); ap.add_argument("--url"); ap.add_argument("--out", default="/tmp/url-check"); ap.add_argument("--port", type=int, default=8798)
a = ap.parse_args(); out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
base = a.url
if not base:
    class Quiet(SimpleHTTPRequestHandler):
        def log_message(self, *a, **k): pass
    httpd = ThreadingHTTPServer(("127.0.0.1", a.port), partial(Quiet, directory=str(SITE))); httpd.daemon_threads = True
    threading.Thread(target=httpd.serve_forever, daemon=True).start(); base = f"http://127.0.0.1:{a.port}/"
AN = json.loads((SITE / "anchors.json").read_text())["anchors"]
STATE = "() => { const c = MAP.getCenter(); return {z: MAP.getZoom(), x: c.lng, y: -c.lat, search: location.search}; }"
fails = []
def check(name, ok, detail):
    print(("PASS" if ok else "FAIL"), name, detail); ok or fails.append(name)

with sync_playwright() as p:
    b = p.chromium.launch(); ctx = b.new_context(viewport={"width": 1500, "height": 800}, permissions=["clipboard-read", "clipboard-write"])
    def load(q, shot):
        pg = ctx.new_page(); errs = []; pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.goto(base + q, wait_until="networkidle"); pg.wait_for_function("window.MAP && document.querySelectorAll('img.leaflet-tile-loaded').length > 0"); pg.wait_for_timeout(1200)
        pg.screenshot(path=str(out / shot)); check(f"no JS errors {q}", not errs, errs); return pg
    # (a) named anchor: continent
    an = AN["deep-learning-basin"]; pg = load("?place=deep-learning-basin", "a_place_continent.png"); s = pg.evaluate(STATE)
    check("(a) ?place=deep-learning-basin center", abs(s["x"] - an["x"]) < 1 and abs(s["y"] - an["y"]) < 1 and s["z"] == .5, f"got z={s['z']} x={s['x']:.1f} y={s['y']:.1f}, anchor {an['x']},{an['y']}")
    pg.close()
    an = AN["deep-rl-delta"]; pg = load("?place=deep-rl-delta", "a_place_country.png"); s = pg.evaluate(STATE)
    check("(a) ?place=deep-rl-delta center", abs(s["x"] - an["x"]) < 1 and abs(s["y"] - an["y"]) < 1 and s["z"] == 2.5, f"got z={s['z']} x={s['x']:.1f} y={s['y']:.1f}, anchor {an['x']},{an['y']}")
    pg.close()
    pg = load("?place=deep-rl-delta&z=1", "a_place_zoom_override.png"); s = pg.evaluate(STATE)
    check("(a) ?place=&z= override", abs(s["x"] - an["x"]) < 1 and s["z"] == 1, f"got z={s['z']} x={s['x']:.1f}"); pg.close()
    pg = load("?place=no-such-place", "a_place_unknown.png"); s = pg.evaluate(STATE)
    check("(a) unknown place → default view", s["z"] < .5 and abs(s["x"] - 900) < 5, f"got z={s['z']} x={s['x']:.1f} y={s['y']:.1f}"); pg.close()
    # (b) precise
    pg = load("?z=2&x=1000&y=400", "b_precise.png"); s = pg.evaluate(STATE)
    check("(b) ?z=2&x=1000&y=400 exact view", s["z"] == 2 and abs(s["x"] - 1000) < .01 and abs(s["y"] - 400) < .01, f"got z={s['z']} x={s['x']:.3f} y={s['y']:.3f}")
    # (c) URL follows pan/zoom
    if "URLWRITE" in sys.argv[0] or True:
        s0 = pg.evaluate(STATE)
        pg.evaluate("MAP.panBy([300, 120], {animate: false})"); pg.wait_for_timeout(500); s1 = pg.evaluate(STATE)
        pg.evaluate("MAP.setZoom(3, {animate: false})"); pg.wait_for_timeout(500); s2 = pg.evaluate(STATE)
        exp = lambda s: f"?z={s['z']:g}&x={round(s['x'], 1):g}&y={round(s['y'], 1):g}"
        check("(c) URL after pan", s1["search"] == exp(s1) and s1["search"] != s0["search"], f"before {s0['search']} after pan {s1['search']} (view {exp(s1)})")
        check("(c) URL after zoom", s2["search"] == exp(s2) and s2["z"] == 3, f"after zoom {s2['search']} (view {exp(s2)})")
        check("(c) replaceState, no history growth", pg.evaluate("history.length") == 1, f"history.length={pg.evaluate('history.length')}")
        pg.screenshot(path=str(out / "c_after_pan_zoom.png"))
        # (d) copy link
        btn = pg.locator(".copylink")
        check("(d) copy-link button present", btn.count() == 1, f"count={btn.count()}")
        if btn.count():
            btn.click(); pg.wait_for_timeout(200); label = btn.inner_text(); clip = pg.evaluate("navigator.clipboard.readText()")
            check("(d) clipboard == location.href", clip == pg.evaluate("location.href"), f"clipboard {clip}")
            check("(d) 'Copied' feedback", "Copied" in label, f"label after click: {label!r}")
            pg.screenshot(path=str(out / "d_copied.png"))
    pg.close(); b.close()
print("URL scheme:", "PASS" if not fails else f"FAIL {fails}"); sys.exit(1 if fails else 0)
