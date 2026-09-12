#!/usr/bin/env python3
"""Build the Leaflet raster tile pyramid for the Map of AI (continent layer) + the label/leader overlay JSON.

Source of truth for the ART is still site/atlas.html (the P2-T1-RENDER v11 generative SVG). This script does not
re-draw anything. LEVEL OF DETAIL: every zoom level is its OWN screenshot of atlas.html?tilesrc=1&lod=z (the lod CSS
in atlas.html shows more layers per level: z0 flat continents + names, z1 textures + years + faint country borders,
z2 solid borders + country names, z3 full country labels), taken at device-scale 2**z and sliced ONLY into that
level's tiles. Nothing is resampled between levels, so zooming in swaps in genuinely new content (Google-Maps
style), not an enlarged copy of the same picture. Leaflet's L.CRS.Simple reads plate units == zoom-0 pixels:

    plate      1800 x 700 viewBox units (W, H in atlas.html)
    zoom z     1 plate unit = 2**z px   -> the plate is 1800*2**z x 700*2**z px, tiled at TILE px
    z          sliced from its own 2**z-scale screenshot of lod=z (z3: 8x -> 14400 x 5600 px; z0: 1800 x 700 px)

Outputs (all under site/):
    tiles/{z}/{x}/{y}.png     the pyramid (RGB PNG, plate-coloured padding outside the plate)
    tiles/meta.json           {plate, tile, zmin, zmax, lod, counts, bytes}
    labels.json               continent label blocks, leaders, leader dots and land outlines in plate units
                              (window.exportLabels() in atlas.html) for the Leaflet hover/hit-target overlay

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


LOD_DESC = {
    0: "world view: flat tinted continents, coast, continent name only, leaders; no textures, no country layer",
    1: "+ terrain textures, + continent subtitle/years, + faint country borders (no country labels)",
    2: "+ solid country borders, + country name labels (no country subtitle/years)",
    3: "full detail: country name + subtitle + years, country leaders, per-country biome tints",
}


def screenshot(browser, url: str, scale: int, want_labels: bool = False) -> tuple[Image.Image, dict | None]:
    pg = browser.new_page(viewport={"width": PLATE[0], "height": PLATE[1]}, device_scale_factor=scale)
    errors = []
    pg.on("pageerror", lambda e: errors.append(str(e)))
    pg.goto(url, wait_until="networkidle")
    pg.wait_for_selector("#shapes .continent")
    pg.evaluate("document.fonts.ready")
    pg.wait_for_timeout(1500)
    if errors:
        sys.exit("JS errors in tile source: " + "; ".join(errors))
    labels = pg.evaluate("window.exportLabels()") if want_labels else None
    png = pg.screenshot(type="png", clip={"x": 0, "y": 0, "width": PLATE[0], "height": PLATE[1]}, timeout=600_000)
    pg.close()
    img = Image.open(io.BytesIO(png)).convert("RGB")
    assert img.size == (PLATE[0] * scale, PLATE[1] * scale), img.size
    return img, labels


def slice_level(img: Image.Image, out: Path, tile: int, z: int) -> dict:
    """Slice ONE zoom level's own screenshot (already at 2**z px per plate unit) into tiles/{z}/{x}/{y}.png."""
    w, h = img.size
    nx, ny = -(-w // tile), -(-h // tile)
    n, nbytes = 0, 0
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
    print(f"z{z}: {nx}x{ny} = {n} tiles ({w}x{h}px, lod {z})", flush=True)
    return {"tiles": n, "cols": nx, "rows": ny, "px": [w, h], "bytes": nbytes, "lod": z}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--zmax", type=int, default=3, help="max native zoom (= max lod); level z is screenshotted at 2**z")
    ap.add_argument("--tile", type=int, default=256)
    ap.add_argument("--port", type=int, default=8793)
    ap.add_argument("--keep-full", default=None, help="also save each level's full screenshot as <dir>/lod-{z}.png")
    a = ap.parse_args()
    out = SITE / "tiles"
    if out.exists():
        shutil.rmtree(out)
    httpd = serve(SITE, a.port)
    counts, labels = {}, None
    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            b = p.chromium.launch()
            for z in range(a.zmax + 1):
                img, lb = screenshot(b, f"http://127.0.0.1:{a.port}/atlas.html?tilesrc=1&lod={min(z, 3)}", 2 ** z, want_labels=(z == 0))
                labels = lb or labels
                if a.keep_full:
                    Path(a.keep_full).mkdir(parents=True, exist_ok=True)
                    img.save(Path(a.keep_full) / f"lod-{z}.png")
                counts[z] = slice_level(img, out, a.tile, z)
                del img
            b.close()
    finally:
        httpd.shutdown()
    (SITE / "labels.json").write_text(json.dumps(labels, separators=(",", ":")) + "\n")
    meta = {"plate": list(PLATE), "tile": a.tile, "zmin": 0, "zmax": a.zmax, "source_px": counts[a.zmax]["px"],
            "lod": {str(z): LOD_DESC[min(z, 3)] for z in counts}, "counts": counts, "bytes": sum(c["bytes"] for c in counts.values())}
    (out / "meta.json").write_text(json.dumps(meta, indent=1) + "\n")
    print(json.dumps(meta, indent=1))


if __name__ == "__main__":
    main()
