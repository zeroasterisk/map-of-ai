"""P3-T10 verification: open site/atlas.html (interactive), zoom into a continent, report its countries, screenshot."""
import json, sys
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
cont = sys.argv[1] if len(sys.argv) > 1 else "generative-coast"
out = sys.argv[2] if len(sys.argv) > 2 else str(ROOT / "docs/screens" / f"{cont}-a2.png")
JS = r"""
(cid) => {
  const ks = [...document.querySelectorAll('#countries .country')].filter(g => g.dataset.parent === cid)
    .map(g => { const p = g.querySelector('path.cland'); const b = p.getBBox(); return {id: g.dataset.id, w: +b.width.toFixed(0), h: +b.height.toFixed(0), x: +b.x.toFixed(0), y: +b.y.toFixed(0), d: p.getAttribute('d').length}; });
  document.querySelector(`#shapes .continent[data-id="${cid}"]`).dispatchEvent(new MouseEvent('click', {bubbles: true}));
  const zoomed = document.getElementById('map').classList.contains('zoomed');
  const labels = [...document.querySelectorAll('#klabels text')].filter(t => getComputedStyle(t).display !== 'none' && ks.some(k => k.id === t.dataset.for)).map(t => [t.dataset.for, t.textContent]);
  return {ks, zoomed, labels};
}
"""
import functools, http.server, threading
class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
httpd = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(Quiet, directory=str(ROOT / "site")))
threading.Thread(target=httpd.serve_forever, daemon=True).start()
url = f"http://127.0.0.1:{httpd.server_address[1]}/atlas.html"
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1800, "height": 760}, device_scale_factor=2)
    errs = []
    pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.on("console", lambda m: errs.append(m.text) if m.type in ("error", "warning") else None)
    pg.goto(url, wait_until="networkidle")
    pg.wait_for_selector("#countries .country", state="attached")
    res = pg.evaluate(JS, cont)
    pg.wait_for_timeout(900)   # zoom transition
    pg.screenshot(path=out)
    b.close()
print(json.dumps(res, indent=1))
print("errors:", errs)
print("screenshot:", out)
