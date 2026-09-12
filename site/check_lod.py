#!/usr/bin/env python3
"""GATE: the tile pyramid has real level-of-detail — each zoom level carries DIFFERENT content, not a resample.

For a plate-space region (default: the Deep Learning Basin interior, the only continent with a country layer) this
reassembles the region from each zoom level's tiles, brings every level to the same pixel size (downsample to z0's
resolution — the honest comparison: if the levels were the same picture at different resolutions, the downsampled
crops would be near-identical), and asserts:

  1. ink coverage (dark stroke/text pixels) grows with zoom: z3 > z2 > z1 > z0 inside the country-bearing continent
     (country borders + country labels appear; they must be ABSENT at z0/z1 and PRESENT at z2/z3)
  2. per-level structural difference vs z3 (mean |Δ| after downsampling) is well above the resample noise floor
  3. z0 is a flat fill: local colour variance in a texture-only patch is far lower at z0 than at z1 (no textures at z0)
  4. tile-file evidence: z0 tiles are each small relative to z3 tiles for the same plate area

Run: /tmp/pwvenv/bin/python site/check_lod.py    (exit 1 on failure; prints the numbers either way)
"""
import json
import sys
from pathlib import Path

from PIL import Image, ImageStat

SITE = Path(__file__).resolve().parent
TILES = SITE / "tiles"
META = json.loads((TILES / "meta.json").read_text())
T = META["tile"]


def region(z: int, x0: float, y0: float, w: float, h: float) -> Image.Image:
    """Crop plate-space region (units) out of level z by pasting the tiles that cover it."""
    s = 2 ** z
    px0, py0, pw, ph = round(x0 * s), round(y0 * s), round(w * s), round(h * s)
    out = Image.new("RGB", (pw, ph))
    for tx in range(px0 // T, (px0 + pw - 1) // T + 1):
        for ty in range(py0 // T, (py0 + ph - 1) // T + 1):
            p = TILES / str(z) / str(tx) / f"{ty}.png"
            if p.exists():
                out.paste(Image.open(p).convert("RGB"), (tx * T - px0, ty * T - py0))
    return out


def ink_fraction(im: Image.Image, thresh=95) -> float:
    g = im.convert("L")
    hist = g.histogram()
    return sum(hist[:thresh]) / (im.width * im.height)


def mean_abs_diff(a: Image.Image, b: Image.Image) -> float:
    b = b.resize(a.size, Image.LANCZOS) if b.size != a.size else b
    la, lb = list(a.convert("L").getdata()), list(b.convert("L").getdata())
    return sum(abs(pa - pb) for pa, pb in zip(la, lb)) / len(la)


def main():
    fails = []
    zs = list(range(META["zmin"], META["zmax"] + 1))
    # region A: Deep Learning Basin interior (plate units; the continent spans x 804–1190, y 320–608)
    A = (860, 380, 300, 180)
    crops = {z: region(z, *A) for z in zs}
    base = crops[0].size
    down = {z: (crops[z] if z == 0 else crops[z].resize(base, Image.LANCZOS)) for z in zs}
    ink = {z: ink_fraction(down[z]) for z in zs}
    print("region A (Deep Learning Basin interior, plate", A, ") after downsampling every level to z0 size", base)
    for z in zs:
        print(f"  z{z}: ink fraction {ink[z]:.4f}   tiles at this level {META['counts'][str(z)]['tiles']:5d}   level px {META['counts'][str(z)]['px']}")
    # 1. ink grows with zoom, and the country layer's jump (z1 -> z2) is the big one
    if not (ink[0] < ink[1] < ink[2] < ink[3]):
        fails.append(f"ink coverage must grow strictly with zoom, got {ink}")
    if not ink[2] > ink[0] * 1.5:
        fails.append(f"z2 must carry markedly more ink than z0 (country borders + names), got z0 {ink[0]:.4f} z2 {ink[2]:.4f}")
    # 2. adjacent levels differ structurally, compared at the LOWER level's own resolution (so small text added by the
    #    higher level is not averaged away). floor = the higher level downsampled two different ways (pure resample noise).
    print("  adjacent levels at the lower level's resolution:")
    for z in zs[:-1]:
        lo, hi = crops[z], crops[z + 1]
        hi_a = hi.resize(lo.size, Image.LANCZOS)
        hi_b = hi.resize(lo.size, Image.BOX)
        floor = mean_abs_diff(hi_a, hi_b)
        d = mean_abs_diff(lo, hi_a)
        dink = ink_fraction(hi_a) - ink_fraction(lo)
        print(f"    z{z} vs z{z + 1}: mean |Δ luma| {d:.2f} (resample floor {floor:.2f}), ink added by z{z + 1}: {dink:+.4f}")
        if not (d > floor * 1.5 and dink > 0.0005):
            fails.append(f"z{z}->z{z + 1} does not add content (|Δ| {d:.2f} vs floor {floor:.2f}, ink {dink:+.4f})")
    # 3. z0 is flat: local variance in a patch that is pure land at every level (no labels/borders) — Generative Coast
    B = (1400, 300, 60, 40)
    var = {z: sum(ImageStat.Stat(region(z, *B).resize(region(0, *B).size, Image.LANCZOS).convert("L")).stddev) for z in (0, 1)}
    print(f"region B (Generative Coast land patch {B}): luma stddev z0 {var[0]:.2f}  z1 {var[1]:.2f}  (z0 flat fill, z1 textured)")
    if not var[0] * 2 < var[1]:
        fails.append(f"z0 should be a flat fill with far less texture variance than z1, got {var}")
    # 4. bytes per plate area: z0 tiles cover 256x256 plate units each, z3 tiles 32x32; compare bytes per plate unit²
    bpu = {z: META["counts"][str(z)]["bytes"] / (META["plate"][0] * META["plate"][1]) for z in zs}
    print("bytes per plate unit²: " + ", ".join(f"z{z} {v:.2f}" for z, v in bpu.items()))
    if not bpu[0] * 4 < bpu[3]:
        fails.append(f"z0 should be far lighter per plate area than z3, got {bpu}")
    # side-by-side evidence image for the report
    out = SITE.parent / "docs" / "screens" / "lod-tiles-same-region.png"
    strip = Image.new("RGB", (base[0] * 4 + 30, base[1]), (255, 255, 255))
    for i, z in enumerate(zs):
        strip.paste(down[z], (i * (base[0] + 10), 0))
    strip.save(out)
    print("evidence strip (z0..z3 tiles, same region, same px size):", out)
    print("LOD GATE:", "FAIL\n  " + "\n  ".join(fails) if fails else "PASS")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
