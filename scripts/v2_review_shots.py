"""Phase 4a review shots: 4 mobile frames (412×892 DPR 2) of site/v2 → docs/density/shots/v2-*.png"""
import threading, sys
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from playwright.sync_api import sync_playwright
REPO = Path(__file__).resolve().parent.parent
class Q(SimpleHTTPRequestHandler):
    def log_message(self, *a, **k): pass
httpd = ThreadingHTTPServer(("127.0.0.1", 8999), partial(Q, directory=str(REPO / "site")))
threading.Thread(target=httpd.serve_forever, daemon=True).start()
SHOTS = [("v2-z0-world", "z=3&x=900&y=525"), ("v2-z1-gen-coast", "z=4.5&x=1476.3&y=676.4"),
         ("v2-z2-stat-isthmus", "z=6&x=829.9&y=668.2"), ("v2-z3-imagenet", "z=7.5&x=1000&y=650")]
out = REPO / "docs" / "density" / "shots"; out.mkdir(parents=True, exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch()
    for name, q in SHOTS:
        pg = b.new_page(viewport={"width": 412, "height": 892}, device_scale_factor=2)
        pg.goto(f"http://127.0.0.1:8999/v2/index.html?test=1&{q}", wait_until="load")
        pg.wait_for_function("window.__idle === true", timeout=30000)
        pg.screenshot(path=str(out / f"{name}.png"))
        print(out / f"{name}.png")
        pg.close()
    b.close()
