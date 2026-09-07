#!/usr/bin/env python3
"""One-off texture generator for the atlas render (P2-T1-RENDER v4).

Calls Vertex AI `gemini-3-pro-image` (Nano Banana Pro, GA) ONCE per asset and writes raw PNGs to
--out (default /tmp/tex/raw). The committed assets in site/assets/textures/ are made from
these by `prep_textures.py` (downscale + JPEG). Nothing in the deployed site calls any API.

Auth: gcloud ADC (`gcloud auth print-access-token`). Project is fixed below.

Model choice (Alan, 2026-09-07: "no Gemini 2.x; latest tier of each model, confirmed against Cloud docs"):
  - https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/3-pro-image
    Model ID `gemini-3-pro-image`, Launch stage GA, Model availability "Global: global" only.
  - `gcloud ai model-garden models list` on alanblount-sandbox lists google/gemini-3-pro-image@default CAN_PREDICT=Yes.
  - It is NOT served from regional endpoints (us-central1 etc. return 404) — must use the global hostname
    `aiplatform.googleapis.com` AND `locations/global`. Regional hostname + locations/global also 404s.

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
MODEL = "gemini-3-pro-image"
URL = (f"https://aiplatform.googleapis.com/v1/projects/{PROJECT}/locations/global"
       f"/publishers/google/models/{MODEL}:generateContent")

# gemini-3-pro-image specifics (observed 2026-09-07, first full batch):
#   - default output is 1408x768 unless imageConfig.aspectRatio is set -> every asset now requests 1:1 (cartouche 3:2)
#   - it likes to add ships / sea serpents / compass roses / castles and paper fold-creases unless told not to,
#     and lays symbols out on a rigid lattice unless told to jitter -> explicit NEGATIVE list + jitter clause in TILE
#   - still tends to a mild vignette; prep_textures.flatten() removes it, as before
ASPECT = {"cartouche": "3:2"}  # everything else 1:1

# One template; only the bracketed part changes, so the ink style stays consistent across fills.
# v5: an explicit, identical scale clause for every biome so glyph size reads as one zoom level across tiles
# (v4 review: mixed/highland glyphs were 2-4x the size of forest/jungle ones; grassland was near-blank).
TILE = ("Seamless tileable texture, top-down view, hand-drawn antique atlas cartography style, aged parchment "
        "paper background, warm sepia and muted earth-tone ink illustration, {what}, medium density: each individual "
        "symbol is small, roughly 3 to 4 percent of the image width, dozens of symbols per row, all symbols the same "
        "scale, symbols placed at randomly jittered irregular positions (never a regular grid, never aligned rows), "
        "no text, no labels, no border, "
        "consistent ink linework style throughout, illustration only, no photorealism, evenly distributed across "
        "the whole image with no vignette, no central focus and no framing so the image repeats without seams. "
        "Strictly exclude: ships, boats, sea monsters, animals, people, buildings, castles, towers, compass roses, "
        "coastlines, rivers, roads, paper folds, creases, wrinkles, torn edges, stains, frames, banners, cartouches.")

ASSETS = {
    # page/base
    # parchment does NOT use TILE: on gemini-3-pro-image the long "strictly exclude: ... compass roses ..." list
    # seeded exactly those glyphs onto what must be a blank sheet. Short positive-only prompt instead.
    "parchment": ("Seamless tileable texture of plain blank aged parchment paper, top-down flat scan, warm cream "
                  "sepia tone, subtle fibre grain and faint even mottling, uniform brightness from edge to edge, "
                  "completely empty paper surface with nothing drawn on it, no vignette, no framing."),
    "sea": TILE.format(what="calm open sea drawn as sparse fine horizontal ripple linework in pale sepia ink on "
                       "parchment, very light and airy, mostly empty paper with occasional short wave strokes, "
                       "ONLY wave strokes and empty paper, nothing else"),
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
    "jungle": TILE.format(what="dense tropical jungle: tightly packed TINY palm and broadleaf tree symbols (each tree "
                          "about 3 percent of the image width, at least 15 trees across each row) drawn "
                          "in dark sepia ink ON LIGHT PARCHMENT with light cross-hatch shading between them, "
                          "high density but the pale paper still shows through, tree symbols scattered at random "
                          "irregular positions and slightly varying sizes, shading only as short strokes inside each "
                          "tree crown (no continuous hatch lattice across the background), sepia ink only, no green, "
                          "no black background"),
    "wetland": TILE.format(what="marsh and wetland: TINY reed tufts and short grass strokes over small ripple-lines "
                           "of standing water (each tuft-and-ripple group about 3 percent of the image width, at "
                           "least 15 groups across each row), scattered evenly at random positions"),
    "harbour": TILE.format(what="sand and shingle foreshore: fine ink stipple dots of slightly varying size and "
                           "density with only very gentle, subtle density variation (never distinct stripes, streaks "
                           "or bands, never empty channels), like engraved sandbank shading on an old sea chart, "
                           "purely small dots and a few very short dashes, no rings, no circles, no symbols, no "
                           "objects, no coastlines, no landforms"),
    "mixed": TILE.format(what="transitional terrain: small low rolling hill symbols, small round tree symbols and "
                         "scattered stipple mixed together in alternating patches, every hill and tree the same "
                         "small size as the others (a hill symbol is no wider than a tree symbol), no large mountain "
                         "ranges, no big vignettes"),
    # one-off decorative elements (not tiles)
    "compass": ("A single complete ornate antique compass rose, the WHOLE rose fully visible and centred with generous "
                "empty parchment margin on all four sides (nothing cut off by the image edge), hand-drawn in dark "
                "sepia ink in the style of a 17th-century "
                "atlas, sixteen-point star with alternating shaded and unshaded points, a decorative fleur-de-lis "
                "ornament marking north, fine engraved hatching, centred on a plain flat warm aged parchment square "
                "background with uniform brightness, ABSOLUTELY NO LETTERS of any kind (no N, no E, no S, no W), "
                "no text, no labels, no border, no page edges, no creases, no stains, illustration only, "
                "no photorealism."),
    "cartouche": ("An empty ornate antique map cartouche frame, hand-drawn in dark sepia ink in the style of a "
                  "17th-century atlas, baroque scrollwork and ribbons around a completely BLANK plain parchment "
                  "interior panel suitable for a title, wide landscape aspect, centred on a plain warm aged "
                  "parchment background with generous empty margin on all sides, scrollwork and foliage only: "
                  "no cherubs, no putti, no people, no animals, no fish, no dolphins, no crests, no shields, "
                  "absolutely no text, no letters, no labels, no page edges, no creases, no stains, "
                  "illustration only."),
}


def token() -> str:
    return subprocess.check_output(["gcloud", "auth", "print-access-token"], text=True).strip()


def generate(prompt: str, tok: str) -> bytes:
    return generate_cfg(prompt, tok, "1:1")


def generate_cfg(prompt: str, tok: str, aspect: str) -> bytes:
    body = json.dumps({"contents": [{"role": "user", "parts": [{"text": prompt}]}],
                       "generationConfig": {"responseModalities": ["IMAGE"],
                                            "imageConfig": {"aspectRatio": aspect, "imageSize": "1K"}}}).encode()
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
        dst.write_bytes(generate_cfg(ASSETS[n], tok, ASPECT.get(n, "1:1")))
        print(f"{n}: {dst.stat().st_size // 1024} KB in {time.time() - t0:.1f}s")


if __name__ == "__main__":
    main()
