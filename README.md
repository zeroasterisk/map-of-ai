# Map of AI: The 2036 Textbook Atlas

**Live interactive atlas:** [mapofai.dev](https://mapofai.dev) (mirror: [zeroasterisk.github.io/map-of-ai](https://zeroasterisk.github.io/map-of-ai/))

An interactive, antique-cartographic map of the history of artificial intelligence research (1666 to 2026), inspired by [mapofmetal.com](https://mapofmetal.com) and 19th-century Swiss topographic relief plates (Eduard Imhof hillshading and Lehmann slope hachures).

- West is old, East is now (`AXES.md` §1), spanning the Antecedent Isles (1666-1942) through the Transformer Plateau (2017-2022) and the Generative Coast (2022-present).
- North to South encodes research approach (`AXES.md` §3), placing formal and symbolic work in the north (`N1`/`N2`), language and agentic synthesis along the central band (`C`), and statistical, connectionist, and embodied schools in the south (`S1`/`S2`).
- Five semantic zoom altitudes (`Alt 0` through `Alt 4`, `z0` through `z4`) reveal detail progressively from World (`Alt 0`) to Regions (`Alt 1`), Provinces (`Alt 2`), Syllabus Milestones (`Alt 3`), and Archival Citations (`Alt 4`).

---

## How it works

### 1. The 2036 textbook dataset (10 continents, 49 provinces, 10 outlying islands, 517 landmarks)
Every major era from Leibniz's *De Arte Combinatoria* (1666) to modern open agentic protocols (`MCP`, `A2A`, `A2UI`, `AP2`, `AAIF`, `SKILL.md`, `UCP`, `Agent Plugins`, `AX`, `ARD`) and frontier models (`DeepSeek-R1`, `Gemini 2.5`, `Gemini 3`, `Gemini 4 Argon`, `Claude 4`, `Claude Opus 5.5`, `o3`, `GPT-5`, `OpenAI 6`, `Gemma 1-4`) is mapped with verified dates, authors, institutional hubs, 15 hardware summits along the Silicon Range, 27 alternative-paradigm landmarks across 10 outlying islands, and primary citations (`site/atlas_data.js`, `data/continents/REGISTRY.md`, `research/`).

### 2. Open Knowledge Format (OKF v0.2) LLM Wiki & 79 Lineage Post Roads
All 475 historical milestone nodes, 47 spatial provinces, and 79 West-to-East lineage roads (`10` primary trunks, `14` cross-province branches, and `55` thematic/lab spurs = `492` directed causal edges) are maintained as a self-contained **601-file Open Knowledge Format (OKF) v0.2 knowledge graph** in [`wiki/`](wiki/index.md) and compiled into the plate via [`scripts/compile_okf_roads.py`](scripts/compile_okf_roads.py). Every road is audited for historical, institutional, and causal accuracy so competing labs are never conflated. Hovering or clicking any milestone highlights its connected West/East lineage paths and lets you walk step-by-step along the road in the Citation Inspector.

### 3. 2D topographic elevation model and multi-scale copperplate micro-cartography
Instead of 2.5D cartoon mountain stamps, a Python Digital Elevation Model (`scripts/build_dem.py` and `drawThreads` in `site/atlas.html`) synthesizes an `1800x1050` float32 heightfield along the Silicon Range, producing 315-degree northwest Lambertian hillshading (`site/assets/textures/hillshade.png`), 5-band marching-squares hypsometric elevation contours (`site/data/contours.geojson`), and gradient-aligned Lehmann slope hachures (`site/data/hachures.geojson`). At higher zoom levels (`z=3` and `z=4`), raster biome textures give way to fine vector copperplate detail: woodcut trees, marsh reeds, alpine crags, engraved town rosettes, and star-citadel fortifications.

### 4. Subpixel cursor-locked zoom and world-anchored vector labels
To make zooming feel like Google Maps, `site/index.html` patches Leaflet 1.9.4's integer pixel rounding (`_getNewPixelOrigin`, `latLngToLayerPoint`, `_setZoomTransform`, and `_reset`) to preserve floating-point subpixel precision and replaces discrete wheel snapping with a continuous velocity-proportional wheel controller + post-zoom bounds helper. Scroll speed maps directly to zoom speed, stops on the exact frame you stop scrolling (`0 ms` coasting), and keeps the plate coordinate under your cursor locked across `z=-1.0..5.0`. All continent banners, province headers, outlying islands, and milestone pins live in world coordinates inside `.leaflet-labels-pane` so the GPU scales labels and terrain tiles together without lag.

---

## Run locally and verify

### Serve the map locally
No build step or external API keys are required:

```bash
python3 -m http.server -d site 8765
# Open http://localhost:8765/
```

### Run verification checks

Run the 100-frame mobile viewport density and collision test (`412x892` @ DPR 2 across `z0` through `z3`):

```bash
python3 tests/sample_frames.py
```

Run the OKF v0.2 knowledge graph compiler, registry, YAML schema, and SVG plate layout checks:

```bash
python3 scripts/compile_okf_roads.py
python3 scripts/check_registry.py
python3 scripts/validate.py --offline --summary
python3 site/check_layout.py
```

---

## Repository structure

| Path | Purpose |
|---|---|
| `site/index.html` | Self-contained interactive atlas (`Leaflet` continuous subpixel zoom + world-locked vector label engine + interactive road highlighting) |
| `site/atlas.html` | Master planimetric SVG plate renderer (shorelines, copperplate micro-cartography, 3-tier lineage post roads, 2D topographic DEM) |
| `wiki/` | 601-file **Open Knowledge Format (OKF) v0.2 LLM Wiki** (`wiki/index.md`, `wiki/roads/`, `wiki/provinces/`, `wiki/milestones/`) |
| `scripts/compile_okf_roads.py` | Compiles and validates the 79 OKF v0.2 lineage roads (`492` causal edges across `475` milestones) into `wiki/` and `site/atlas.html` |
| `scripts/refresh.py` | Monthly milestone refresh CLI (`--status`, `--add`, `--build`) with deterministic `(year, province, y_Hint)` placement |
| `site/atlas_data.js` | Complete compiled 2036 Textbook dataset (10 continents, 49 provinces, 10 outlying islands, 517 landmarks, 79 lineage roads) |
| `site/tiles/{0..4}/{x}/{y}.png` | 7,599 multi-scale pure-terrain & copperplate raster tiles (`z=0..4`: `40 / 135 / 493 / 1,881 / 5,050`, zero baked text) |
| `scripts/build_dem.py` | Synthesizes the `1800x1050` float32 DEM, hillshade, marching-squares contours, and Lehmann hachures |
| `site/build_tiles.py` | Renders the multi-scale pure-terrain tile pyramid from `site/atlas.html` and bundles `site/atlas_data.js` |
| `site/CNAME` | Custom domain configuration (`mapofai.dev`) for GitHub Pages |
| `tests/sample_frames.py` | Mobile viewport (`412x892` @ DPR 2) density, clipping, and overlap gate (`100/100` pass) |
| `docs/density/baseline.json` | Latest verified 100-frame sampler report (`100.0%` pass rate) |
| `docs/GTM_NARRATIVE_GEMINI4_ARGON.md` | Engineering field notes: how Gemini 4 Argon rescued the repo (`0% -> 100%`) plus post-review polish (OKF LLM Wiki, causal roads, tile cleanup) |
| `research/` | 9-part historical research compendium (1666 to 2026) with verified primary citations |
| `SPEC.md` / `AXES.md` / `ALTITUDES.md` | Cartographic specification, coordinate axes, and semantic zoom taxonomy |
