#!/usr/bin/env python3
"""Dev aid: screenshot atlas.html?tilesrc=1&lod=N for every level (0..ZMAX), cropped to one plate region, at one scale, so
the levels of detail can be compared side by side (docs/screens/<prefix>-{N}.png). Also prints window.LOD_CURATED (events
that did not fit and were curated out of the raster) and the per-level count of visible text nodes in the region.
Usage: lod_screens.py [--region x y w h] [--scale S] [--zmax Z] [--prefix lod]"""
import argparse, io, sys
from pathlib import Path
from PIL import Image
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_tiles import serve, SITE, PLATE

ap = argparse.ArgumentParser()
ap.add_argument("--region", type=float, nargs=4, default=[1080, 150, 560, 320], metavar=("X", "Y", "W", "H"), help="plate units")
ap.add_argument("--scale", type=int, default=3)
ap.add_argument("--zmax", type=int, default=4)
ap.add_argument("--prefix", default="lod")
ap.add_argument("--out", default=str(SITE.parent / "docs" / "screens"))
ap.add_argument("--port", type=int, default=8794)
a = ap.parse_args()
from playwright.sync_api import sync_playwright
httpd = serve(SITE, a.port)
COUNT_JS = """(r) => { const [x, y, w, h] = r; const out = {}; for (const t of document.querySelectorAll('svg#map text')) { if (!t.getClientRects().length) continue;
  const b = t.getBBox(); if (b.x + b.width < x || b.x > x + w || b.y + b.height < y || b.y > y + h) continue; const c = t.getAttribute('class') || '?'; out[c] = (out[c] || 0) + 1; } return out; }"""
try:
    with sync_playwright() as p:
        b = p.chromium.launch()
        for lod in range(a.zmax + 1):
            pg = b.new_page(viewport={"width": PLATE[0], "height": PLATE[1]}, device_scale_factor=a.scale)
            errs = []; pg.on("pageerror", lambda e: errs.append(str(e)))
            pg.goto(f"http://127.0.0.1:{a.port}/atlas.html?tilesrc=1&lod={lod}", wait_until="networkidle")
            pg.wait_for_selector("#shapes .continent"); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(1200)
            assert not errs, errs
            x, y, w, h = a.region
            print(f"lod{lod}: visible text in region by class:", pg.evaluate(COUNT_JS, a.region), "| curated:", pg.evaluate("window.LOD_CURATED"), flush=True)
            png = pg.screenshot(type="png", clip={"x": x, "y": y, "width": w, "height": h})
            out = Path(a.out) / f"{a.prefix}-{lod}.png"; out.parent.mkdir(parents=True, exist_ok=True)
            Image.open(io.BytesIO(png)).convert("RGB").save(out, optimize=True)
            print(out, flush=True); pg.close()
        b.close()
finally:
    httpd.shutdown()
