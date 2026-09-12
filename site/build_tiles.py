#!/usr/bin/env python3
"""Build the Leaflet raster tile pyramid for the Map of AI (continent layer) + the label/leader overlay JSON.

Source of truth for the ART is still site/atlas.html (the P2-T1-RENDER v11 generative SVG). This script does not
re-draw anything: it opens atlas.html?tilesrc=1 (bare 1800x700 plate, labels/leaders/countries hidden — CSS in
atlas.html), screenshots it at device-scale SCALE, and slices the result into an XYZ pyramid that Leaflet's
L.CRS.Simple reads with plate units == zoom-0 pixels:

    plate      1800 x 700 viewBox units (W, H in atlas.html)
    zoom z     1 plate unit = 2**z px   -> the plate is 1800*2**z x 700*2**z px, tiled at TILE px
    z = ZMAX   sliced from the SCALE-x screenshot (SCALE == 2**ZMAX, 8x -> 14400 x 5600 px)
    z < ZMAX   sliced from LANCZOS downsamples of that screenshot

Outputs (all under site/):
    tiles/{z}/{x}/{y}.png     the pyramid (RGB PNG, plate-coloured padding outside the plate)
    tiles/meta.json           {plate, tile, zmin, zmax, counts, bytes}
    labels.json               continent label blocks, leaders, leader dots and land outlines in plate units
                              (window.exportLabels() in atlas.html) for the Leaflet vector overlay

Run (sandbox toolchain from earlier sessions):
    PLAYWRIGHT_BROWSERS_PATH=/tmp/pw-browsers \
    LD_LIBRARY_PATH=/tmp/localdeps/usr/lib/x86_64-linux-gnu:/tmp/localdeps/lib/x86_64-linux-gnu \
    /tmp/pwvenv/bin/python site/build_tiles.py
"""
import argparse
import io
import json
import shutil
import sys
import threading
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from PIL import Image

Image.MAX_IMAGE_PIXELS = None
SITE = Path(__file__).resolve().parent
PLATE = (1800, 700)   # must match W, H in atlas.html
SEA = (0xDC, 0xCF, 0xAE)  # atlas.html sea base colour: padding outside the plate


def serve(root: Path, port: int):
    h = partial(SimpleHTTPRequestHandler, directory=str(root))
    httpd = ThreadingHTTPServer(("127.0.0.1", port), h)
    httpd.daemon_threads = True
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd


def screenshot(url: str, scale: int) -> tuple[Image.Image, dict]:
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": PLATE[0], "height": PLATE[1]}, device_scale_factor=scale)
        errors = []
        pg.on("pageerror", lambda e: errors.append(str(e)))
        pg.goto(url, wait_until="networkidle")
        pg.wait_for_selector("#shapes .continent")
        pg.evaluate("document.fonts.ready")
        pg.wait_for_timeout(1500)
        if errors:
            sys.exit("JS errors in tile source: " + "; ".join(errors))
        labels = pg.evaluate("window.exportLabels()")
        png = pg.screenshot(type="png", clip={"x": 0, "y": 0, "width": PLATE[0], "height": PLATE[1]}, timeout=600_000)
        b.close()
    img = Image.open(io.BytesIO(png)).convert("RGB")
    return img, labels


def slice_pyramid(full: Image.Image, out: Path, tile: int, zmax: int) -> dict:
    if out.exists():
        shutil.rmtree(out)
    counts, nbytes = {}, 0
    for z in range(zmax, -1, -1):
        w, h = PLATE[0] * 2 ** z, PLATE[1] * 2 ** z
        img = full if z == zmax else full.resize((w, h), Image.LANCZOS)
        nx, ny = -(-w // tile), -(-h // tile)
        n = 0
        for x in range(nx):
            (out / str(z) / str(x)).mkdir(parents=True, exist_ok=True)
            for y in range(ny):
                box = (x * tile, y * tile, min((x + 1) * tile, w), min((y + 1) * tile, h))
                t = Image.new("RGB", (tile, tile), SEA)
                t.paste(img.crop(box), (0, 0))
                path = out / str(z) / str(x) / f"{y}.png"
                t.save(path, "PNG", optimize=True)
                nbytes += path.stat().st_size
                n += 1
        counts[z] = {"tiles": n, "cols": nx, "rows": ny, "px": [w, h]}
        print(f"z{z}: {nx}x{ny} = {n} tiles ({w}x{h}px)", flush=True)
    return {"counts": counts, "bytes": nbytes}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--zmax", type=int, default=3, help="max native zoom; screenshot scale = 2**zmax")
    ap.add_argument("--tile", type=int, default=256)
    ap.add_argument("--port", type=int, default=8793)
    ap.add_argument("--keep-full", default=None, help="also save the full screenshot here (png)")
    a = ap.parse_args()
    scale = 2 ** a.zmax
    httpd = serve(SITE, a.port)
    try:
        full, labels = screenshot(f"http://127.0.0.1:{a.port}/atlas.html?tilesrc=1", scale)
    finally:
        httpd.shutdown()
    assert full.size == (PLATE[0] * scale, PLATE[1] * scale), full.size
    print("source", full.size, flush=True)
    if a.keep_full:
        full.save(a.keep_full)
    (SITE / "labels.json").write_text(json.dumps(labels, separators=(",", ":")) + "\n")
    stats = slice_pyramid(full, SITE / "tiles", a.tile, a.zmax)
    meta = {"plate": list(PLATE), "tile": a.tile, "zmin": 0, "zmax": a.zmax, "source_px": list(full.size), **stats}
    (SITE / "tiles" / "meta.json").write_text(json.dumps(meta, indent=1) + "\n")
    print(json.dumps(meta, indent=1))


if __name__ == "__main__":
    main()
