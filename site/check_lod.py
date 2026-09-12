#!/usr/bin/env python3
"""GATE: the tile pyramid has real level-of-detail — each zoom level carries MORE INFORMATION, not just a different
texture or a resample of its neighbour.

Measures, for a plate-space region (default: the Deep Learning Basin — the LOD pilot continent, the only one with
country / hint / event layers), what every zoom level's own tiles contain, and asserts that each z -> z+1 step adds
content. Two complementary measurements are made per transition, both on the region reassembled from the tiles:

  A. INK MASS at each level's OWN resolution: the count of dark (stroke / glyph) pixels divided by the level's linear
     scale, i.e. ink normalised to plate units of line length. Text that is legible at level z+1 but sub-pixel at
     level z's resolution is counted here — this is the number that captures "more labels / dots / borders appeared".
     Bar: each transition must add >= MIN_INK_GAIN units (set so the two weak transitions of the pre-pilot pyramid,
     see docs/screens/check_lod_before.txt, fail it).
  B. legacy: mean |Δ luma| between adjacent levels at the LOWER level's resolution must be above the resample noise
     floor (levels are not resamples of each other), and the whole pyramid must be monotone in A.

Plus: z0 is a flat fill (no textures), and z0 tiles are light relative to the deepest full-plate level.

Run: /tmp/pwvenv/bin/python site/check_lod.py    (exit 1 on failure; prints the numbers either way; writes
docs/screens/check_lod_after.json and the side-by-side evidence strip docs/screens/lod-tiles-same-region.png)
"""
import json
import sys
from pathlib import Path

from PIL import Image, ImageStat

SITE = Path(__file__).resolve().parent
TILES = SITE / "tiles"
META = json.loads((TILES / "meta.json").read_text())
T = META["tile"]
MIN_INK_GAIN = 0.25    # plate-unit-normalised ink units per transition (pre-pilot pyramid: z0→1 .12, z1→2 2.9, z2→3 .16)


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


def ink_pixels(im: Image.Image, thresh=95) -> int:
    hist = im.convert("L").histogram()
    return sum(hist[:thresh])


def ink_fraction(im: Image.Image, thresh=95) -> float:
    return ink_pixels(im, thresh) / (im.width * im.height)


def mean_abs_diff(a: Image.Image, b: Image.Image) -> float:
    b = b.resize(a.size, Image.LANCZOS) if b.size != a.size else b
    la, lb = list(a.convert("L").getdata()), list(b.convert("L").getdata())
    return sum(abs(pa - pb) for pa, pb in zip(la, lb)) / len(la)


def main():
    fails = []
    zs = list(range(META["zmin"], META["zmax"] + 1))
    # region A: the Deep Learning Basin (plate units; the continent's land spans x 804–1190, y 320–608)
    A = (804, 320, 386, 288)
    crops = {z: region(z, *A) for z in zs}
    base = crops[0].size
    # A. ink mass at each level's own resolution, normalised by the linear scale (dark px / 2**z / region area in plate units²) x 1000
    area = A[2] * A[3]
    mass = {z: ink_pixels(crops[z]) / (2 ** z) / area * 1000 for z in zs}
    down = {z: (crops[z] if z == 0 else crops[z].resize(base, Image.LANCZOS)) for z in zs}
    ink = {z: ink_fraction(down[z]) for z in zs}
    print("region A (Deep Learning Basin, plate", A, ")")
    for z in zs:
        c = META["counts"][str(z)]
        print(f"  z{z}: ink mass {mass[z]:6.2f} (own res, scale-normalised)   ink fraction at z0 size {ink[z]:.4f}   tiles {c['tiles']:5d}   level px {c['px']}" + ("  (pilot bbox only)" if c.get("bbox") else ""))
    if not all(mass[z] < mass[z + 1] for z in zs[:-1]):
        fails.append(f"ink mass must grow strictly with zoom, got { {z: round(v, 2) for z, v in mass.items()} }")
    print("  transitions:")
    trans = {}
    for z in zs[:-1]:
        lo, hi = crops[z], crops[z + 1]
        hi_a = hi.resize(lo.size, Image.LANCZOS)
        hi_b = hi.resize(lo.size, Image.BOX)
        floor = mean_abs_diff(hi_a, hi_b)
        d = mean_abs_diff(lo, hi_a)
        gain = mass[z + 1] - mass[z]
        trans[f"z{z}->z{z + 1}"] = {"ink_mass_gain": round(gain, 3), "ink_mass_ratio": round(mass[z + 1] / mass[z], 3), "delta_luma": round(d, 2), "floor": round(floor, 2)}
        print(f"    z{z} -> z{z + 1}: ink mass {mass[z]:.2f} -> {mass[z + 1]:.2f}  gain {gain:+.2f} (x{mass[z + 1] / mass[z]:.2f})   |Δ luma| at z{z} res {d:.2f} (resample floor {floor:.2f})" + ("" if gain >= MIN_INK_GAIN else f"   << below the {MIN_INK_GAIN} bar"))
        if not (d > floor * 1.5):
            fails.append(f"z{z}->z{z + 1} looks like a resample (|Δ| {d:.2f} vs floor {floor:.2f})")
        if not gain >= MIN_INK_GAIN:
            fails.append(f"z{z}->z{z + 1} does not add enough content (ink mass gain {gain:+.2f} < {MIN_INK_GAIN})")
    (SITE.parent / "docs" / "screens" / "check_lod_after.json").write_text(json.dumps({"region": A, "ink_mass": {str(z): round(v, 3) for z, v in mass.items()}, "transitions": trans}, indent=1) + "\n")
    # z0 is flat: local variance in a patch that is pure land at every level (no labels/borders) — Generative Coast
    B = (1400, 300, 60, 40)
    var = {z: sum(ImageStat.Stat(region(z, *B).resize(region(0, *B).size, Image.LANCZOS).convert("L")).stddev) for z in (0, 1)}
    print(f"region B (Generative Coast land patch {B}): luma stddev z0 {var[0]:.2f}  z1 {var[1]:.2f}  (z0 flat fill, z1 textured)")
    if not var[0] * 2 < var[1]:
        fails.append(f"z0 should be a flat fill with far less texture variance than z1, got {var}")
    # bytes per plate unit² (pilot levels cover only their bbox)
    def parea(z):
        c = META["counts"][str(z)]
        return (c["bbox"][2] - c["bbox"][0]) * (c["bbox"][3] - c["bbox"][1]) if c.get("bbox") else META["plate"][0] * META["plate"][1]
    bpu = {z: META["counts"][str(z)]["bytes"] / parea(z) for z in zs}
    print("bytes per plate unit²: " + ", ".join(f"z{z} {v:.2f}" for z, v in bpu.items()))
    if not bpu[0] * 4 < bpu[min(3, zs[-1])]:
        fails.append(f"z0 should be far lighter per plate area than z3, got {bpu}")
    # side-by-side evidence image for the report (every level at the same px size)
    out = SITE.parent / "docs" / "screens" / "lod-tiles-same-region.png"
    strip = Image.new("RGB", (base[0] * len(zs) + 10 * (len(zs) - 1), base[1]), (255, 255, 255))
    for i, z in enumerate(zs):
        strip.paste(down[z], (i * (base[0] + 10), 0))
    strip.save(out)
    print(f"evidence strip (z0..z{zs[-1]} tiles, same region, same px size):", out)
    print("LOD GATE:", "FAIL\n  " + "\n  ".join(fails) if fails else "PASS")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
