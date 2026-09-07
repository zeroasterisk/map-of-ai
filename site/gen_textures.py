#!/usr/bin/env python3
"""One-off texture generator for the atlas render (P2-T1-RENDER v4).

Calls Vertex AI `gemini-2.5-flash-image` ONCE per asset and writes raw 1024x1024 PNGs to
--out (default /tmp/tex/raw). The committed assets in site/assets/textures/ are made from
these by `prep_textures.py` (downscale + JPEG). Nothing in the deployed site calls any API.

Auth: gcloud ADC (`gcloud auth print-access-token`). Project/region are fixed below.

Usage:  python3 site/gen_textures.py [--only parchment,forest] [--out DIR] [--force]
"""
import argparse
import base64
import json
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

PROJECT = "alanblount-sandbox"
REGION = "us-central1"
MODEL = "gemini-2.5-flash-image"
URL = (f"https://{REGION}-aiplatform.googleapis.com/v1/projects/{PROJECT}/locations/{REGION}"
       f"/publishers/google/models/{MODEL}:generateContent")

# One template; only the bracketed part changes, so the ink style stays consistent across fills.
# v5: an explicit, identical scale clause for every biome so glyph size reads as one zoom level across tiles
# (v4 review: mixed/highland glyphs were 2-4x the size of forest/jungle ones; grassland was near-blank).
TILE = ("Seamless tileable texture, top-down view, hand-drawn antique atlas cartography style, aged parchment "
        "paper background, warm sepia and muted earth-tone ink illustration, {what}, medium density: each individual "
        "symbol is small, roughly 3 to 4 percent of the image width, dozens of symbols per row, all symbols the same "
        "scale, no text, no labels, no border, "
        "consistent ink linework style throughout, illustration only, no photorealism, evenly distributed across "
        "the whole image with no vignette, no central focus and no framing so the image repeats without seams.")

ASSETS = {
    # page/base
    "parchment": TILE.format(what="plain aged parchment paper only: subtle fibre grain and faint even mottling, "
                             "uniform brightness from edge to edge with NO darker corners, NO drawings, NO symbols, "
                             "NO lines, NO stains, just the empty flat paper surface"),
    "sea": TILE.format(what="calm open sea drawn as sparse fine horizontal ripple linework in pale sepia ink on "
                       "parchment, very light and airy, mostly empty paper with occasional short wave strokes"),
    # biome fills (colour legend order)
    "highland": TILE.format(what="dense hachure-shaded mountain range peaks drawn as small repeated hand-inked "
                            "mountain symbols with short slope shading strokes, a few rocky crags"),
    "grassland": TILE.format(what="open grassland and plains: small hand-inked grass-tuft symbols (three or four "
                             "short curved blades each) and a few tiny shrub dots scattered evenly at random, "
                             "clearly visible tufts at medium spacing with paper between them, light and airy, "
                             "absolutely no contour lines, no hills, no roads, no rivers, no ridges"),
    "forest": TILE.format(what="temperate forest: many small round-crowned deciduous tree symbols with short "
                          "trunks and light stippled canopy shading, placed at RANDOM irregular positions with "
                          "varying sizes (never a regular grid), moderate density, sepia ink only, no green"),
    "jungle": TILE.format(what="dense tropical jungle: tightly packed small palm and broadleaf tree symbols drawn "
                          "in dark sepia ink ON LIGHT PARCHMENT with light cross-hatch shading between them, "
                          "high density but the pale paper still shows through, sepia ink only, no green, no "
                          "black background"),
    "wetland": TILE.format(what="marsh and wetland: horizontal reed tufts and short grass strokes over small "
                           "ripple-lines of standing water, scattered evenly"),
    "harbour": TILE.format(what="sand and shingle foreshore: fine ink stipple dots of slightly varying size and "
                           "density drifting in loose irregular bands, like engraved sandbank shading on an old "
                           "sea chart, purely dots and a few short dashes, no symbols, no objects, no coastlines, "
                           "no landforms"),
    "mixed": TILE.format(what="transitional terrain: small low rolling hill symbols, small round tree symbols and "
                         "scattered stipple mixed together in alternating patches, every hill and tree the same "
                         "small size as the others, no large mountain ranges, no big vignettes"),
    # one-off decorative elements (not tiles)
    "compass": ("A single ornate antique compass rose, hand-drawn in dark sepia ink in the style of a 17th-century "
                "atlas, sixteen-point star with alternating shaded and unshaded points, a decorative fleur-de-lis "
                "ornament marking north, fine engraved hatching, centred on a plain flat warm aged parchment square "
                "background with uniform brightness, ABSOLUTELY NO LETTERS of any kind (no N, no E, no S, no W), "
                "no text, no labels, no border, illustration only, no photorealism."),
    "cartouche": ("An empty ornate antique map cartouche frame, hand-drawn in dark sepia ink in the style of a "
                  "17th-century atlas, baroque scrollwork and ribbons around a completely BLANK plain parchment "
                  "interior panel suitable for a title, wide landscape aspect, centred on a plain warm aged "
                  "parchment background, absolutely no text, no letters, no labels, illustration only."),
}


def token() -> str:
    return subprocess.check_output(["gcloud", "auth", "print-access-token"], text=True).strip()


def generate(prompt: str, tok: str) -> bytes:
    body = json.dumps({"contents": [{"role": "user", "parts": [{"text": prompt}]}],
                       "generationConfig": {"responseModalities": ["IMAGE"]}}).encode()
    req = urllib.request.Request(URL, data=body, headers={"Authorization": f"Bearer {tok}",
                                                          "Content-Type": "application/json"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                resp = json.load(r)
            for part in resp["candidates"][0]["content"]["parts"]:
                if "inlineData" in part:
                    return base64.b64decode(part["inlineData"]["data"])
            raise RuntimeError(f"no image part: {json.dumps(resp)[:400]}")
        except Exception as e:  # noqa: BLE001
            if attempt == 3:
                raise
            print(f"  retry {attempt + 1}: {e}", file=sys.stderr)
            time.sleep(3 * (attempt + 1))
    raise RuntimeError("unreachable")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="/tmp/tex/raw")
    ap.add_argument("--only", default="")
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    names = [n for n in a.only.split(",") if n] or list(ASSETS)
    tok = token()
    for n in names:
        dst = out / f"{n}.png"
        if dst.exists() and not a.force:
            print(f"{n}: exists, skip")
            continue
        t0 = time.time()
        dst.write_bytes(generate(ASSETS[n], tok))
        print(f"{n}: {dst.stat().st_size // 1024} KB in {time.time() - t0:.1f}s")


if __name__ == "__main__":
    main()
