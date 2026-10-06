"""Quick render probe for the country layer (dev aid; the real gates live in check_layout.py)."""
import json, sys, threading, http.server
from pathlib import Path
from playwright.sync_api import sync_playwright

root = Path(__file__).resolve().parent
class Q(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k): super().__init__(*a, directory=str(root), **k)
    def log_message(self, *a, **k): pass
httpd = http.server.ThreadingHTTPServer(("127.0.0.1", 8793), Q); threading.Thread(target=httpd.serve_forever, daemon=True).start()
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1800, "height": 900})
    errs = []; pg.on("pageerror", lambda e: errs.append(str(e))); pg.on("console", lambda m: errs.append(m.text) if m.type in ("error", "warning") else None)
    pg.goto("http://127.0.0.1:8793/", wait_until="networkidle"); pg.wait_for_selector("#shapes .continent"); pg.wait_for_timeout(1200)
    print("errors:", errs)
    print(pg.evaluate("""() => [...document.querySelectorAll('#countries .country')].map(g => { const b = g.querySelector('.cland').getBBox(); return [g.dataset.id, Math.round(b.x), Math.round(b.y), Math.round(b.width), Math.round(b.height), g.querySelector('.cland').getAttribute('d').length]; })"""))
    pg.screenshot(path="/tmp/A1.png", clip={"x": 0, "y": 0, "width": 1800, "height": 720})
    pg.click('#shapes .continent[data-id="deep-learning-basin"] path.land', force=True)
    pg.wait_for_timeout(300)
    print("zoomed:", pg.evaluate("document.getElementById('map').classList.contains('zoomed')"), "klabels:", pg.evaluate("document.querySelectorAll('#klabels text').length"), "leaders:", pg.evaluate("document.querySelectorAll('#kleaders path').length"))
    pg.screenshot(path="/tmp/A2.png", clip={"x": 0, "y": 0, "width": 1800, "height": 720})
    x0, x1 = pg.evaluate("() => [X(2004), X(2019)]")
    pg.screenshot(path="/tmp/A2-crop.png", clip={"x": x0, "y": 250, "width": x1 - x0, "height": 380})
    pg.keyboard.press("Escape"); print("after Esc zoomed:", pg.evaluate("document.getElementById('map').classList.contains('zoomed')"))
    b.close()
