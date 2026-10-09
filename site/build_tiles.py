#!/usr/bin/env python3
"""Build the Leaflet raster tile pyramid for the Map of AI (continent layer) + the label/leader overlay JSON.

Source of truth for the ART is still site/atlas.html (the P2-T1-RENDER v11 generative SVG). This script does not
re-draw anything. LEVEL OF DETAIL: every zoom level is its OWN screenshot of atlas.html?tilesrc=1&lod=z (the lod CSS
in atlas.html shows more layers per level: z0 flat continents + names, z1 textures + years + faint country borders,
z2 solid borders + country names, z3 full country labels), taken at device-scale 2**z and sliced ONLY into that
level's tiles. Nothing is resampled between levels, so zooming in swaps in genuinely new content (Google-Maps
style), not an enlarged copy of the same picture. Leaflet's L.CRS.Simple reads plate units == zoom-0 pixels:

    plate      1800 x 1050 viewBox units (W, H in atlas.html; the v12 Y-funnel plate)
    zoom z     1 plate unit = 2**z px   -> the plate is 1800*2**z x 1050*2**z px, tiled at TILE px
    z          sliced from its own 2**z-scale screenshot of lod=z (z3: 8x -> 14400 x 8400 px; z0: 1800 x 1050 px)

Outputs (all under site/):
    tiles/{z}/{x}/{y}.png     the pyramid (RGB PNG, plate-coloured padding outside the plate)
    tiles/meta.json           {plate, tile, zmin, zmax, full_zmax, pilot_bbox, pilot_bboxes, lod, counts, bytes}
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
PLATE = (1800, 1050)   # must match W, H in atlas.html
SEA = (0xDC, 0xCF, 0xAE)  # atlas.html sea base colour: padding outside the plate


def serve(root: Path, port: int):
    h = partial(SimpleHTTPRequestHandler, directory=str(root))
    httpd = ThreadingHTTPServer(("127.0.0.1", port), h)
    httpd.daemon_threads = True
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd


LOD_DESC = {
    0: "world view: flat tinted continents, coast, continent name only, leaders; no textures, no country layer",
    1: "+ terrain textures, + continent subtitle/years, + faint country borders, + landmark hints",
    2: "+ solid country borders, + fine 0.50x textures, + sub-graticule, + terrace contours, + trade roads",
    3: "+ syllabus view (8x): 0.28x fine textures, + vellum wash, + 5-level terrace contours & hachures, + town rosettes, + submarine cables",
    4: "+ archive view (16x): 0.15x micro-textures, + vellum wash, + 7-level contours, + Vauban star-citadel planimetry & quarterly meridians",
}
LOD_MAX = max(LOD_DESC)
# Full inhabited atlas at z4 (16 plate units per tile), partitioned into 4 contiguous tile-aligned horizontal sectors
# so each Playwright capture stays <= 7,424 px wide while covering all 10 continents, 49 provinces, and 10 outlying islands.
PILOT_BBOXES = {
    "west-archipelago-heartland": (32, 128, 496, 928),
    "central-steppes-isthmus": (496, 128, 864, 928),
    "deep-learning-basin-shoals": (864, 128, 1248, 928),
    "transformer-generative-east": (1248, 128, 1648, 928),
}
PILOT_UNION_BBOX = [32, 128, 1648, 928]
PILOT_BBOX = PILOT_BBOXES["deep-learning-basin-shoals"]


def screenshot(browser, url: str, scale: int, want_labels: bool = False, clip: tuple | None = None) -> tuple[Image.Image, dict | None]:
  """One render of atlas.html at device-scale `scale`; `clip` = (x, y, w, h) in plate units (default: whole plate).
    Big levels (z4 = 16x = 28800x11200 px) are captured in horizontal strips by the caller to bound memory."""
  pg = browser.new_page(
      viewport={"width": PLATE[0], "height": PLATE[1]},
      device_scale_factor=scale,
  )
  errors = []
  pg.on("pageerror", lambda e: errors.append(str(e)))
  pg.goto(url, wait_until="networkidle")
  pg.wait_for_selector("#shapes .continent")
  pg.evaluate("document.fonts.ready")
  pg.wait_for_timeout(300)
  if errors:
    sys.exit("JS errors in tile source: " + "; ".join(errors))
  labels = pg.evaluate("window.exportLabels()") if want_labels else None
  x, y, w, h = clip or (0, 0, PLATE[0], PLATE[1])
  png = pg.screenshot(
      type="png",
      clip={"x": x, "y": y, "width": w, "height": h},
      timeout=600_000,
  )
  pg.close()
  img = Image.open(io.BytesIO(png)).convert("RGB")
  assert img.size == (w * scale, h * scale), img.size
  return img, labels


def slice_level(img: Image.Image, out: Path, tile: int, z: int, oy: int = 0, acc: dict | None = None, ox: int = 0) -> dict:
  """Slice ONE zoom level's own screenshot (already at 2**z px per plate unit) into tiles/{z}/{x}/{y}.png.
    `oy` = the strip's top edge in level px (a multiple of `tile`), so strips of one level tile independently."""
  from concurrent.futures import ThreadPoolExecutor

  w, h = img.size
  nx, ny = -(-w // tile), -(-h // tile)
  tasks = []
  for x in range(nx):
    col_dir = out / str(z) / str(x + ox // tile)
    col_dir.mkdir(parents=True, exist_ok=True)
    for y in range(ny):
      box = (x * tile, y * tile, min((x + 1) * tile, w), min((y + 1) * tile, h))
      crop = img.crop(box)
      path = col_dir / f"{y + oy // tile}.png"
      tasks.append((crop, path))

  def _save_tile(item):
    crop, path = item
    if crop.size == (tile, tile):
      crop.save(path, "PNG", compress_level=3)
    else:
      t = Image.new("RGB", (tile, tile), SEA)
      t.paste(crop, (0, 0))
      t.save(path, "PNG", compress_level=3)
    return path.stat().st_size

  with ThreadPoolExecutor(max_workers=16) as pool:
    sizes = list(pool.map(_save_tile, tasks))
  n = len(sizes)
  nbytes = sum(sizes)
  if acc is None:
    acc = {
        "tiles": 0,
        "cols": nx,
        "rows": 0,
        "px": [w, 0],
        "bytes": 0,
        "lod": z,
    }
  acc["tiles"] += n
  acc["rows"] += ny
  acc["px"][1] += h
  acc["bytes"] += nbytes
  print(
      f"z{z}: {nx}x{ny} = {n} tiles ({w}x{h}px strip at y={oy}, lod {z})",
      flush=True,
  )
  return acc


def main():
  ap = argparse.ArgumentParser()
  ap.add_argument(
      "--zmax",
      type=int,
      default=LOD_MAX,
      help="max native zoom (= max lod); level z is screenshotted at 2**z",
  )
  ap.add_argument("--tile", type=int, default=256)
  ap.add_argument("--port", type=int, default=8793)
  ap.add_argument(
      "--keep-full",
      default=None,
      help="also save each level's full screenshot as <dir>/lod-{z}.png",
  )
  ap.add_argument(
      "--strip-px",
      type=int,
      default=6000,
      help=(
          "capture levels taller than this in horizontal strips (memory bound)"
      ),
  )
  ap.add_argument(
      "--full-zmax",
      type=int,
      default=3,
      help=(
          "levels above this are rendered for the pilot bboxes only (the LOD"
          " pilot continents)"
      ),
  )
  ap.add_argument(
      "--pilot-bbox",
      type=int,
      nargs=4,
      action="append",
      default=None,
      metavar=("X0", "Y0", "X1", "Y1"),
      help=(
          "plate units, tile-aligned at zmax; repeatable. Default: every bbox"
          " in PILOT_BBOXES"
      ),
  )
  a = ap.parse_args()
  pilot_bboxes = (
      [tuple(b) for b in a.pilot_bbox]
      if a.pilot_bbox
      else list(PILOT_BBOXES.values())
  )
  final_out = SITE / "tiles"
  out = Path("/tmp/map_of_ai_tiles_stage")
  if out.exists():
    shutil.rmtree(out)
  out.mkdir(parents=True, exist_ok=True)
  httpd = serve(SITE, a.port)
  counts, labels = {}, None
  try:
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
      b = p.chromium.launch()
      for z in range(a.zmax + 1):
        s = 2**z
        url = (
            f"http://127.0.0.1:{a.port}/atlas.html?tilesrc=1&lod={min(z, LOD_MAX)}"
        )
        if (
            z > a.full_zmax
        ):  # pilot level: each pilot bbox in turn, in strips of whole tile rows
          tp = a.tile // s  # plate units per tile at this level
          step = tp * max(1, (a.strip_px // s) // tp)
          acc = {
              "tiles": 0,
              "cols": 0,
              "rows": 0,
              "px": [0, 0],
              "bytes": 0,
              "lod": z,
              "regions": [],
          }
          for bbox in pilot_bboxes:
            bx0, by0, bx1, by1 = bbox
            assert all(v % tp == 0 for v in bbox), (
                f"pilot bbox {bbox} must be tile-aligned at z{z} ({tp} plate"
                " units)"
            )
            n0 = acc["tiles"]
            for y0 in range(by0, by1, step):
              h = min(step, by1 - y0)
              img, _ = screenshot(b, url, s, clip=(bx0, y0, bx1 - bx0, h))
              acc = slice_level(
                  img, out, a.tile, z, oy=y0 * s, acc=acc, ox=bx0 * s
              )
              del img
            acc["regions"].append({
                "bbox": list(bbox),
                "tiles": acc["tiles"] - n0,
                "cols": (bx1 - bx0) // tp,
                "rows": (by1 - by0) // tp,
                "px": [(bx1 - bx0) * s, (by1 - by0) * s],
            })
          # per-level totals across regions: cols/px are sums over the regions (they are disjoint captures)
          acc["bbox"] = list(pilot_bboxes[0])
          acc["bboxes"] = [list(bb) for bb in pilot_bboxes]
          acc["cols"] = sum(r["cols"] for r in acc["regions"])
          acc["px"] = [
              sum(r["px"][0] for r in acc["regions"]),
              max(r["px"][1] for r in acc["regions"]),
          ]
          counts[z] = acc
        elif PLATE[1] * s <= a.strip_px:
          img, lb = screenshot(b, url, s, want_labels=(z == 0))
          labels = lb or labels
          if a.keep_full:
            Path(a.keep_full).mkdir(parents=True, exist_ok=True)
            img.save(Path(a.keep_full) / f"lod-{z}.png")
          counts[z] = slice_level(img, out, a.tile, z)
          del img
        else:  # strips of whole tile rows: strip height in plate units = tile * k / s
          step = max(a.tile // s, 1) * max(
              1, (a.strip_px // s) // max(a.tile // s, 1)
          )
          acc = None
          for y0 in range(0, PLATE[1], step):
            h = min(step, PLATE[1] - y0)
            img, _ = screenshot(b, url, s, clip=(0, y0, PLATE[0], h))
            acc = slice_level(img, out, a.tile, z, oy=y0 * s, acc=acc)
            del img
          counts[z] = acc
      b.close()
  finally:
    httpd.shutdown()
  (SITE / "labels.json").write_text(
      json.dumps(labels, separators=(",", ":")) + "\n"
  )
  pilot = a.zmax > a.full_zmax
  union_pbs = [list(bb) for bb in pilot_bboxes] if a.pilot_bbox else [PILOT_UNION_BBOX]
  meta = {
      "plate": list(PLATE),
      "tile": a.tile,
      "zmin": 0,
      "zmax": max(a.zmax, 4),
      "full_zmax": min(a.zmax, a.full_zmax),
      "pilot_bbox": (
          union_pbs[0] if pilot else None
      ),  # back-compat: the first pilot region
      "pilot_bboxes": union_pbs if pilot else [],
      "source_px": counts[a.zmax]["px"],
      "lod": {str(z): LOD_DESC[min(z, LOD_MAX)] for z in counts},
      "counts": counts,
      "bytes": sum(c["bytes"] for c in counts.values()),
  }
  (out / "meta.json").write_text(json.dumps(meta, indent=1) + "\n")
  if final_out.exists():
    shutil.rmtree(final_out)
  shutil.copytree(out, final_out)
  anchors_obj = (
      json.loads((SITE / "anchors.json").read_text())
      if (SITE / "anchors.json").exists()
      else {"anchors": {}}
  )
  entities_obj = (
      json.loads((SITE / "entities.json").read_text())
      if (SITE / "entities.json").exists()
      else {"countries": [], "threads": []}
  )
  (SITE / "atlas_data.js").write_text(
      "window.ATLAS_DATA = "
      + json.dumps(
          {
              "meta": meta,
              "labels": labels,
              "anchors": anchors_obj,
              "entities": entities_obj,
          },
          separators=(",", ":"),
      )
      + ";\n"
  )
  print(json.dumps(meta, indent=1))


if __name__ == "__main__":
    main()
