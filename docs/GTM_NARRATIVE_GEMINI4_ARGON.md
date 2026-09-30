# From 0% to 100%: How Gemini 4 Argon rescued the Map of AI

## Summary

**Map of AI** ([mapofai.dev](https://mapofai.dev) | [github.com/zeroasterisk/map-of-ai](https://github.com/zeroasterisk/map-of-ai)) started with a simple idea: build an interactive, antique-cartographic map of the entire history of artificial intelligence (1666 to 2026) that zooms like Google Maps across semantic altitudes, from whole eras down to individual papers, labs, and citations.

Before handing the project to **Gemini 4 (Argon)**, I spent five days and 34 sessions trying to build it with another frontier model in a multi-agent harness. Despite generating 18,000+ lines of markdown specs, orchestrator logs, and 5,755 raster tiles, the build stalled out. When the previous model finally wrote a headless Playwright verification script (`tests/sample_frames.py`) to test 100 mobile viewports across four zoom levels, its own commit (`record 0.0% baseline`) told the whole story: **`0 out of 100` frames passed (`0.0%`)**.

I handed the stalled repository to **Gemini 4 (Argon)** with a one-paragraph first-principles brief and one follow-up UX note:
1. Make it zoom like Google Maps: fast when you scroll fast, slow when you scroll slow, stopping the instant your fingers stop, with labels that never drift out of sync.
2. Replace the cartoon 2.5D mountain icons with real 2D topographic relief (elevation contours, northwest hillshading, and slope hachures).
3. Populate every era and school of thought that belongs in a 2036 AI textbook, with clean visual density at every altitude.

In two passes, Gemini 4 Argon diagnosed why the layout was failing, threw out the blurry text-baked PNG tiles, compiled a 424-entry dataset across all 10 continents, wrote a Python 2D elevation model, and built a subpixel floating-point zoom engine inside Leaflet. On the exact same 100-frame mobile verification suite, the pass rate went from **`0.0%` (`0/100`) to `100.0%` (`100/100`)**.

---

## Act I: Where the first 34 sessions got stuck (0.0% pass rate)

Building an interactive historical map is a tough test for an agent because historical taxonomy, cartography, and 60fps viewport math all share the same pixels. Fixing one in isolation breaks the other two.

Over 34 sessions (`commits 1..4` in this repository), the initial build fell into four traps:

### 1. Baking text into 5,755 PNG tiles (`156 MB`)
When asked to move from a static SVG to a tiled pyramid, the previous model baked text labels, pins, and mountain icons directly into a raster image and sliced it into 5,755 PNG files. Zooming in turned typography into blurry pixels. Zooming out crushed dozens of tiny labels on top of each other (`81 out of 100` mobile test frames failed on bounding-box text overlaps).

### 2. Four unpopulated western continents (1666 to 1993 missing country & event data)
Even though the markdown research notes in `research/` covered 1666 through 2026, the previous model only wired country polygons and milestone pins for six continents. Four western continents (Antecedent Isles, Cybernetic Shore, Winter Steppes, and Expert Systems Plateau) had zero province polygons or milestone pins (`19 out of 100` mobile frames failed with empty viewports).

### 3. Cartoon mountain stamps on a 2D map
To draw highland terrain along the Silicon Range, the previous model stamped side-view 2.5D triangular wedges (`/\`) onto a top-down map. Besides looking like a cartoon treasure map, side-view peaks didn't line up with top-down coordinates when zooming.

### 4. Jerky integer zoom steps and lagging DOM labels
Panning and zooming stepped through discrete zoom increments and re-projected HTML/SVG labels after the zoom transition ended, so labels visibly floated and snapped out of sync with the underlying tiles.

---

## Act II: How Gemini 4 Argon solved it (`commits 5..8`)

When I pointed **Gemini 4 Argon** at the repo, I didn't write a 20-page spec. I gave it the product intent in one paragraph and let it work from first principles.

### 1. Stripped text out of the PNG tiles and locked vector labels to world coordinates
Instead of baking text into PNG files or re-projecting DOM elements on every scroll tick, Argon split the rendering pipeline in two (`site/build_tiles.py` and `site/index.html`). The raster pyramid (`z=0..3`, `2,549` tiles, `90 MB`, down from `5,755` tiles and `156 MB`, with zero baked text) carries only rag-paper grain, ocean waterlines, biome textures, and 2D terrain relief. All 10 continent banners, 49 province headers, and 365 milestone pins live in plate coordinates inside `.leaflet-labels-pane`. During a zoom gesture, the browser's GPU compositor scales the vector layer and the tile layer with the exact same matrix transform, so labels never lag behind the terrain.

### 2. Built a real 2D elevation model (`scripts/build_dem.py` and `site/atlas.html`)
Argon replaced the 2.5D cartoon wedges with a continuous `1800x1050` float32 Digital Elevation Model along the Silicon Range. It generates 315-degree northwest Lambertian hillshading (`site/assets/textures/hillshade.png`), 5-band marching-squares hypsometric elevation contours (`site/data/contours.geojson`), and gradient-aligned Lehmann slope hachures (`site/data/hachures.geojson`).

### 3. Completed the 2036 textbook dataset (`site/atlas_data.js`)
Argon populated the four missing western continents and structured 424 sourced entries across 360 years of computing and AI:
- 10 continents: Antecedent Isles (1666-1942), Cybernetic Shore (1943-1956), Symbolic Heartland (1956-1973), Winter Steppes (1974-1993), Expert Systems Plateau (1980-1993), Connectionist Revival (1982-1998), Statistical Isthmus (1988-2011), Deep Learning Basin (2006-2017), Transformer Plateau (2017-2022), and Generative Coast (2022-present).
- 49 provinces and 365 milestones (plus 15 Silicon Range hardware summits) with years, one-line summaries, primary citations, and 5 semantic zoom altitudes (`Alt 0` World through `Alt 4` Archive).

### 4. Fixed Leaflet's integer rounding for subpixel Google Maps zoom (`site/index.html`)
After pass one, I gave one piece of UX feedback: *"I dislike the labels which are out of sync with zooming in. I would like it to zoom more smoothly and more quickly, like Google Maps."*

Argon inspected Leaflet 1.9.4 and fixed three low-level bottlenecks:
1. Standard Leaflet rounds pixel origins and layer points with `.round()` inside `L.Map.prototype._getNewPixelOrigin`, `L.Map.prototype.latLngToLayerPoint`, `L.GridLayer.prototype._setZoomTransform`, and `L.SVGOverlay.prototype._reset`, causing 1-pixel staircase judder during slow zooms. Argon patched all four methods to preserve floating-point subpixel precision.
2. Standard Leaflet buffers wheel events and jumps in discrete zoom steps. Argon disabled the built-in wheel handler and wrote a direct cursor-anchored wheel controller where scroll delta maps proportionally to zoom velocity and stops on the exact frame you stop scrolling (`0 ms` coasting).
3. On every wheel or animation step, the camera updates via `map._move(P(newCx, newCy), newZ, {pinch: true})` using the exact closed-form identity keeping the map coordinate under your cursor locked to within `< 1e-12 px`:
   $$\text{center}_{\text{new}} = \text{anchor}_{\text{world}} - \frac{\text{cursor}_{\text{px}} - \tfrac{1}{2}\text{viewport}_{\text{px}}}{2^{z_{\text{new}}}}$$

---

## Side-by-side comparison

| What we measured | Act I: Stalled prototype (34 sessions) | Act II: Gemini 4 Argon (2 passes) |
|---|---|---|
| Mobile viewport test (`tests/sample_frames.py`) | `0.0%` (`0 / 100` frames passed) | `100.0%` (`100 / 100` frames passed) |
| Label overlaps (100 frames) | `81/100` frames failed with overlapping text | `0` overlaps across all 100 frames |
| Empty frames (100 frames) | `19/100` frames failed with zero landmarks | `0` empty frames across all 100 frames |
| Western continents (1666-1993) | `0` provinces or milestones across 4 western continents | `18` provinces and `105` sourced milestones across 4 western continents |
| Total dataset | `6` populated continents (`252` events) | `10` continents, `49` provinces, `365` milestones (`424` entities + `15` hardware peaks) |
| Terrain rendering | Cartoon 2.5D triangular wedges (`/\`) | 2D Digital Elevation Model, 5 contour bands, NW hillshading, and Lehmann slope hachures |
| Tile pyramid & typography | `5,755` PNG tiles (`156 MB`) with baked blurry text | `2,549` pure-terrain tiles (`z=0..3`, `90 MB`) + world-locked vector typography |
| Zoom mechanics | Jerky discrete step transitions; labels lag | 60fps continuous subpixel zoom (`< 1e-12 px` cursor drift, `0 ms` stop coasting) |
| Interactive features | Static pan/zoom only | Guided textbook tours, live search (`/`), 5 altitude buttons (`Alt 0..4`), and citation drawer |

---

## Takeaways for builders

First, give Argon an executable verification harness and step back. Having `python3 tests/sample_frames.py` in the repository meant Argon didn't guess whether labels overlapped on mobile screens. It ran the 100-frame headless Chromium suite, saw the exact collision failures, and tuned its spatial layout until `100/100` frames passed.

Second, let Argon write deterministic Python generators instead of hand-editing coordinates. Front-end agents struggle when asked to hand-pick `(x, y)` coordinates for hundreds of labels. Argon solved this by writing Python spatial relaxers and terrain rasterizers, turning a visual layout problem into repeatable math.

Third, describe physical behavior rather than line-by-line patches. Simply describing how Google Maps feels ("zoom fast when I scroll fast, stop immediately when I stop, and keep overlays locked in sync") was enough for Argon to track down Leaflet's integer rounding and rewrite the camera transform in one shot.
