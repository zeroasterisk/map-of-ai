#!/usr/bin/env python3
"""Turn the raw 1024x1024 gemini-3-pro-image outputs (from gen_textures.py) into the small static
assets committed under site/assets/textures/. Run once after (re)generating; the site never calls an API.

- tiles (parchment, sea, biomes):
    1. flatten: divide by a 10x10 box-downsampled brightness estimate (kills the vignette / uneven
       density the image model tends to add; measured residual < 1 grey level corner-to-centre);
    2. seamless: offset by half a tile (wrap seams move to the centre cross) and heal that cross by
       cross-fading back to the un-offset image over a feathered band — no mirroring, so no
       "butterfly" symmetry when the tile repeats;
    3. lift: blend dense tiles toward paper so vector labels stay legible on top of them;
    4. downscale to 512 and save as progressive JPEG.
- compass / cartouche: convert the sepia ink drawing to an RGBA cut-out (alpha = darkness), so the
  baked-in parchment background and its vignette disappear and the element sits on the page paper. PNG.

Usage: python3 site/prep_textures.py [--raw /tmp/tex/raw] [--out site/assets/textures]
"""
import argparse
from pathlib import Path

from PIL import Image, ImageChops, ImageEnhance, ImageFilter, ImageMath, ImageOps, ImageStat

PAPER = (233, 220, 192)
# name -> (output px, lift toward paper 0..1 [negative = boost contrast], flatten grid n)
TILES = {"parchment": (768, 0.0, 6), "sea": (512, 0.0, 10), "highland": (512, 0.12, 10),
         "grassland": (512, -0.6, 10), "forest": (512, 0.18, 10), "jungle": (512, 0.32, 10),
         "wetland": (512, 0.22, 10), "harbour": (512, -0.4, 10), "mixed": (512, 0.12, 10)}
# name -> (max px, pre-crop box in raw px to drop torn-paper edge artefacts outside the element, or None)
# gemini-3-pro-image (3:2 request -> 1264x848 raw) puts the whole frame inside the image with clean margins
# (0 ink px on every edge), so no pre-crop; the old 2.5 box (100,215,925,810) would clip its top and right.
CUTOUTS = {"compass": (600, None), "cartouche": (1024, None)}


def flatten(im: Image.Image, n: int = 10) -> Image.Image:
    im = im.convert("RGB")
    low = im.resize((n, n), Image.Resampling.BOX).resize(im.size, Image.Resampling.BICUBIC)
    out = []
    for ch, bl in zip(im.split(), low.split()):
        m = ImageStat.Stat(bl).mean[0]
        res = ImageMath.lambda_eval(lambda a: a["a"] * a["m"] / (a["b"] + 1), a=ch.convert("F"), b=bl.convert("F"), m=m)
        out.append(res.convert("L"))
    return Image.merge("RGB", out)


def seamless(im: Image.Image, feather: int = 56) -> Image.Image:
    """Offset-and-heal. Output wraps seamlessly on all four edges."""
    w, h = im.size
    rolled = ImageChops.offset(im, w // 2, h // 2)
    # mask = 1 on the centre cross (where the old edges now meet), fading to 0 over `feather` px
    mask = Image.new("L", (w, h), 0)
    px = mask.load()
    cx, cy = w // 2, h // 2
    for y in range(h):
        dy = abs(y - cy)
        for x in range(w):
            d = min(abs(x - cx), dy)
            px[x, y] = 255 if d >= feather else int(255 * d / feather)
    # where mask==255 keep rolled; where 0 use the original (continuous across the centre)
    return Image.composite(rolled, im, mask)


def lift(im: Image.Image, k: float) -> Image.Image:
    if k == 0:
        return im
    if k < 0:
        return ImageEnhance.Contrast(im).enhance(1 - k)
    return Image.blend(im, Image.new("RGB", im.size, PAPER), k)


def cutout(im: Image.Image, ink=(58, 42, 24), paper_lo: int = 175, ink_hi: int = 90) -> Image.Image:
    """alpha = 0 for anything paper-toned (>= paper_lo), 255 for real ink (<= ink_hi), linear between.
    Paper on these renders sits at ~200–245 grey with stains down to ~190, ink below ~150."""
    g = ImageOps.autocontrast(im.convert("L"), cutoff=1).filter(ImageFilter.GaussianBlur(0.6))
    span = paper_lo - ink_hi
    alpha = g.point(lambda v: 0 if v >= paper_lo else 255 if v <= ink_hi else int((paper_lo - v) * 255 / span))
    rgba = Image.new("RGBA", im.size, ink + (0,))
    rgba.putalpha(alpha)
    return rgba


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", default="/tmp/tex/raw")
    ap.add_argument("--out", default=str(Path(__file__).resolve().parent / "assets" / "textures"))
    a = ap.parse_args()
    raw, out = Path(a.raw), Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    for name, (size, k, n) in TILES.items():
        im = Image.open(raw / f"{name}.png").convert("RGB")
        im = flatten(im, n)
        im = seamless(im)
        im = lift(im, k)
        im = im.resize((size, size), Image.Resampling.LANCZOS)
        dst = out / f"{name}.jpg"
        im.save(dst, "JPEG", quality=80, optimize=True, progressive=True)
        L = im.convert("L")
        print(f"{dst.name}: {size}px {dst.stat().st_size // 1024} KB  mean-lum {ImageStat.Stat(L).mean[0]:.0f}")
    for name, (size, box) in CUTOUTS.items():
        im = Image.open(raw / f"{name}.png").convert("RGB")
        if box:
            im = im.crop(box)
        c = cutout(im)
        c = c.crop(c.getbbox())
        c.thumbnail((size, size), Image.Resampling.LANCZOS)
        dst = out / f"{name}.png"
        c.save(dst, "PNG", optimize=True)
        print(f"{dst.name}: {c.size[0]}x{c.size[1]} {dst.stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
