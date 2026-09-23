# REFACTOR_PLAN — Map of AI v2: real map mechanics, terrain, density, deterministic gates

> Status: APPROVED DIRECTION (Alan, 2026-09-19): "Option A and your random sampling plan …
> tests which can be largely deterministic … more validation tests … keep the worker moving …
> reduce the level of zoom if it's too much … much more density … tech stack change, more like
> Google Maps / Leaflet … Terrain, yes."
> Author: Claude Fable 5.1 (planner). Worker: gemini-flash cron runner (never self-certifies).
> This file is the backlog of record for the refactor. `STATUS.md` records per-session results;
> `PLAN.md` (content phases P0–P6) stays valid for research/authoring and is referenced, not replaced.

## 0. Decisions (the short version)

| # | Decision | Why |
|---|----------|-----|
| D1 | **Option A: rebuild the renderer as a data-driven map stack.** Geometry, labels, terrain and events become generated GeoJSON / raster-DEM layers rendered by **MapLibre GL JS**; `site/atlas.html` (hand-tuned 1800×1050 SVG) and the screenshot→tile-slice pyramid (`build_tiles.py`, 5,127 PNG tiles, 141 MB) are retired. | Text baked into raster tiles cannot be crisp at fractional zoom or DPR 2/3, and every density fix today is a re-render of the whole pyramid. MapLibre gives us what "feels like Google Maps": continuous zoom, GPU-placed SDF text that never blurs, built-in label collision with priorities, hillshade from a DEM source, and symbol layers that appear per zoom. Leaflet stays only as the fallback reference (it has no collision engine and no DEM support). |
| D2 | **Four semantic zoom levels, not five.** z0 World · z1 Regions · z2 Countries/Schools · z3 Papers/Milestones. Mapped onto MapLibre zoom 3.0 / 4.5 / 6.0 / 7.5 (§3.2); overzoom to 8.5 allowed for inspection, but nothing new appears and text stops growing. | Alan: "reduce the level of zoom if it's too much". Max linear magnification drops from ~70× (today's z4 on a 412 px phone) to ~23×. Density per frame goes up because the same content sits in fewer, fuller levels. |
| D3 | **Deterministic mobile frame sampler is the primary gate** (`tests/sample_frames.py`): seeded, data-derived, fixture-pinned sample of 150 land frames per level at 412×892 CSS px, DPR 2. Counts labels/landmarks/clipping/overlap/legibility; numeric thresholds in §2.3. Blocks merge. | "Random sampling plan" + "largely deterministic". Counts are robust to renderer pixel noise; the seed and land polygons pin the frame set. |
| D4 | **Terrain is a real 2-D heightfield** (float32 DEM, 2 samples per plate unit) → Terrarium RGB `raster-dem` tiles → MapLibre `hillshade` + generated vector **hachures** (Lehmann slope-thickness rule) + summit/pass symbol layers. Silicon Range summits are hardware milestones with elevation ∝ log(transistors · FLOPS). | "Terrain. Yes." The current relief is a decorative SVG stroke; a DEM makes relief consistent at all zooms, and hachures/hillshade derive from the same data as the labelled summits. |
| D5 | **Content target 1,500–2,500 sourced entities** via `scripts/extract_entities.py` over `research/01`–`09` (670 timeline rows + people + systems + thread rows today) with per-continent floors (§5.4), so the seven western continents get country layers and paper-level density equal to the three eastern pilots. | "Much more density" and "no dead zones" cannot be met by placement tricks; the west simply has no A2/A3 entities yet (3 of 10 continents have countries; 228 events, all eastern). |
| D6 | **Worker cadence: one claimed task per 3 h run, idle-gated, branch `refactor/v2`, gates decide merge, planner reviews every 12 h.** (§7) | Alan's standing workflow (3 h crons, idle > 30 min, agent merges when gates pass, worker never self-certifies). |

Non-goals: no change to `SPEC.md` entity rules or `AXES.md` axes; no change to `research/` content; no new
cloud services (GitHub Pages remains the host; MapLibre + PMTiles/GeoJSON are static files).

## 1. Current state (measured 2026-09-19, commit a4904d2)

- Renderer: `site/atlas.html` (1,449 lines, 134 KB) draws one SVG plate 1800×1050; `site/build_tiles.py` screenshots it once per LOD at 2^z scale and slices PNG tiles; `site/index.html` shows them with Leaflet `L.CRS.Simple`, `zoomSnap .25`, z0–z4 (z4 only inside three pilot bboxes). Tiles: 5,127 files, 141 MB in git.
- Text is raster inside tiles; legible only at the integer zoom it was rendered for. Between levels it is bitmap-scaled (the "vector scaling isn't working" symptom). Label collision is solved offline in JS per LOD (`relayout`/`layoutCountries`/`placeLod`) and re-solved on every rebuild.
- Data: 10 continents in `data/continents/REGISTRY.md`; countries for 3 (26, 24 spatial); `data/events/*.yaml` 228 events, all in Deep Learning Basin / Transformer Plateau / Generative Coast; 1 thread (`silicon-river-hardware.yaml`, 15 milestones).
- Research timeline rows per file: 01:72 · 02:40 · 03:35 · 04:34 · 05:30 · 06:41 · 07:43 · 08:188 · 09:187 (=670), plus "Key people", "Key systems/papers" sections and numbered reference blocks in each file.
- Gates: `scripts/validate.py` (V-01…V-60, fixtures), `scripts/check_research.py`, `scripts/check_links.sh`, `site/check_layout.py`, `site/check_lod_labels.py` (both Playwright over the SVG). Nothing samples mobile viewports; nothing measures density per frame; the only "dead zone" check is two hard-coded coordinates.
- Toolchain on this host: `/tmp/pwvenv/bin/python` (Playwright + Pillow + PyYAML), `PLAYWRIGHT_BROWSERS_PATH=/tmp/pw-browsers`, `LD_LIBRARY_PATH=/tmp/localdeps/usr/lib/x86_64-linux-gnu:/tmp/localdeps/lib/x86_64-linux-gnu`; `uv` available; no root. Cron: `map-of-ai-rework-trigger` (id bfa07477835a, every 180 m, currently paused) with idle watchdog `/home/node/agent/scripts/map_of_ai_watchdog.py` (exit 10 = ready).

## 2. Deterministic Mobile Validation Suite — `tests/sample_frames.py`

### 2.1 Purpose
Answer, for every zoom level, "what does a phone user see at a random land location?" with numbers, the
same numbers every run, and fail the build when they regress. It replaces the two hard-coded
coordinates in the old cron prompt with 600 pinned frames.

### 2.2 Frame sampling algorithm (seeded, data-derived, fixture-pinned)

```
SEED          = 20260919                 # constant; bump only with a fixture regeneration commit
VIEWPORT      = (412, 892)               # CSS px, Pixel-class phone (Alan's review device)
DPR           = 2                        # deviceScaleFactor → 824×1784 device px screenshots
LEVELS        = {0: 3.0, 1: 4.5, 2: 6.0, 3: 7.5}   # semantic level → MapLibre zoom (§3.2)
N_FRAMES      = 150 per level            # within Alan's 100–200; z0 uses 12 (whole plate fits)
PLATE         = (1800, 1050)             # plate units; geo mapping in §3.2
```

1. Land mask: union of continent polygons from `site/data/continents.geojson` (generated, §3.3), in
   plate units, via shapely.
2. Stratified grid: for level ℓ, the frame footprint is `Wℓ × Hℓ` plate units
   (`Wℓ = 412 / px_per_unit(zoomℓ)`, `Hℓ = 892 / px_per_unit(zoomℓ)`). Lay a grid of cells of size
   `(Wℓ/2, Hℓ/2)` over the plate bbox (half-frame cells so adjacent frames overlap ≤ 50 %, no gaps).
3. One candidate per cell: `rng = random.Random(f"{SEED}:{ℓ}:{col}:{row}")`, point =
   cell origin + `rng.random()` × cell size. Keep iff point is ≥ 0.15·min(Wℓ,Hℓ) inside land
   (`land.buffer(-margin).contains(point)`), so a "land frame" is mostly land.
4. Order candidates row-major, take the first `N_FRAMES`; if fewer than `N_FRAMES` (z0/z1), take
   all. Result is written to `tests/fixtures/frames/z{ℓ}.json` as
   `[{"id":"z1-017","x":829.9,"y":668.2,"zoom":4.5}, …]` and **committed**.
5. Determinism contract: the fixture only changes when (a) SEED changes or (b) land polygons change.
   `sample_frames.py --check-fixture` recomputes and diffs; a diff without `--update` fails the gate
   with the message "land geometry changed: regenerate frames with --update in the same commit".
   Reviewers therefore see frame-set changes as diffs, never as silent drift.
6. Pinned probes: the fixture is prepended with the named regression coordinates
   (`829.9,668.2 @z2`, `1476.3,676.4 @z1`, and any coordinate Alan reports) tagged `"pinned":true`;
   they never rotate out.

### 2.3 Per-frame measurements
The page under test is `site/index.html` (v2, MapLibre) loaded with
`?x=&y=&z=&test=1` (`test=1` sets `fadeDuration:0`, disables the attribution/compass controls,
pins bearing 0 / pitch 0, self-hosted glyphs → zero network). After `map.once('idle')` the harness
runs one `page.evaluate` that returns:

| Metric | How | 
|---|---|
| `labels` | `map.queryRenderedFeatures({layers: SYMBOL_LAYERS})` deduped by feature id; only *placed* (uncollided) symbols are returned by MapLibre, so this is "visible labels". Split by class: `continent`, `country`, `landmark` (event/city/summit/pass), `fact` (one-line). |
| `landmarks` | placed symbols with `kind ∈ {event, city, summit, pass}`. |
| `clipped` | for each placed label, the text box = anchor point ± measured extent (`ctx.measureText` with the layer's font/size on an offscreen canvas, same string, ± halo). Clipped iff box crosses the viewport edge by > 2 CSS px. Labels within 8 px of the edge that MapLibre already hid don't count (they aren't placed). |
| `overlaps` | pairwise intersection of the text boxes above (IoU > 0 with a 0.5 px tolerance). MapLibre's global collision index should make this 0; the check exists to catch mis-configured `text-allow-overlap`/`icon-ignore-placement` and layers outside the symbol pipeline (HTML markers are banned by this gate). |
| `min_font_px`, `max_font_px` | resolved `text-size` per placed label (`map.getLayer().getPaintProperty` evaluated with `feature-state` off; harness evaluates the zoom-stops expression at the frame zoom). |
| `contrast` | static: WCAG contrast ratio of `text-color` vs `text-halo-color` per layer (halo is the effective background); rendered: mean luminance of the 3 px ring around each text box in the screenshot vs text colour (catches labels over dark hachure/hillshade). |
| `blank_windows` | slide a 200×200 CSS px window in 100 px steps over the land part of the frame; count windows with 0 placed features and 0 line features (`queryRenderedFeatures` on border/hachure/river layers). |
| `ink_ratio` | placed-text box area ÷ frame area (clutter ceiling). |
| `sea_ratio` | fraction of the frame's pixels classified as sea (from the fill layer query, not colour). |

Everything is a count or a ratio derived from feature queries; only `contrast` (rendered) and
`sea_ratio` look at pixels, and both use tolerant thresholds, so SwiftShader vs GPU vs CI runner
differences cannot flip the result.

### 2.4 Thresholds (per land frame; land frame = `sea_ratio ≤ 0.6`)

| Level | MapLibre z | Visible plate units (W×H) | Min labels (total) | Min landmarks | Min facts | Class floors | Max labels | Max ink | Blank 200 px windows |
|---|---|---|---|---|---|---|---|---|---|
| z0 World | 3.0 | whole plate fits (1800×1050 in 412×240 px band) | 9 | 1 (Silicon Range title) | 0 | ≥ 8 of 10 continent names, ≥ 1 ocean name | 24 | 0.20 | n/a |
| z1 Regions | 4.5 | ≈ 636 × 1377 (≈ ⅓ of plate width) | 8 | 4 | 0 | ≥ 1 continent name or subtitle, ≥ 3 country names, ≥ 2 summits/passes where a range is in frame | 30 | 0.25 | ≤ 2 |
| z2 Countries / Schools | 6.0 | ≈ 225 × 487 | 14 | 10 | 2 | ≥ 2 country names, ≥ 1 country tag, ≥ 6 dated landmarks | 45 | 0.32 | 0 |
| z3 Papers / Milestones | 7.5 | ≈ 80 × 172 | 24 | 18 | 6 | ≥ 1 country name, ≥ 12 dated landmarks, ≥ 6 one-line facts | 60 | 0.38 | 0 |

Hard (100 % of frames): `clipped_major == 0`, `overlaps == 0`, `11 ≤ font_px ≤ 42` (continent ≤ 42,
country ≤ 28, landmark ≤ 16, fact ≤ 13 CSS px), static contrast ≥ 4.5:1, rendered contrast ≥ 3:1.
Soft (pass rate): ≥ 95 % of land frames per level meet the min/max density row; the failing 5 % are
listed in the report so the worker can target them. Pinned probes are hard.

Planner decision (2026-09-23, Phase 4b, supersedes the `clipped == 0` wording above and in §2.3): the hard
clipping gate is **`clipped_major == 0`** — a *placed* label with < 50 % of its collision box inside the
viewport (the "giant half-cut banner" Alan reported). Raw `clipped` (any box over the edge by > 2 CSS px)
stays **reported, not gated**: MapLibre places symbols inside a fixed 100 px band outside the viewport and
has no option to suppress edge-straddling labels (measured in Phase 4a), so `clipped == 0` is structurally
unreachable on a continuous-pan map.

Planner decision (2026-09-23, Phase 4c, supersedes the 4b wording): the hard clipping gate is
**`clipped_major_anchored == 0`** — a placed label whose *anchor point is inside the viewport* but < 50 %
of its box is visible. Labels anchored off-screen are MapLibre's 100 px padding band: `clipped` and
`clipped_major` are reported, not gated. Continent/country title labels use center anchors only (no
`text-variable-anchor`) so the big titles never render half-cut. Density floors in the table above stay as
written: they are content-bound and content is being expanded in parallel (`refactor/v2-content`).

Calibration note: min-label floors were derived from the entity target (§5.4): with ~2,000 entities
over ~1.1 M plate units² of land, a z3 frame (~13,800 units²) contains ~25 entities on average, a z2
frame ~200 (collision-culled to the 14–45 band by priority). If the content target is missed, the
floors are not lowered — the extraction backlog is raised.

### 2.5 Growth / monotonicity checks (cross-level)
For every z2 frame, the four z3 frames tiling it must together show ≥ 2× the z2 landmarks
(information grows on zoom-in). For every z1 frame, its z2 children ≥ 1.5×. Continent names must
appear at z0 and z1 and never at z3; one-line facts never below z2.5. These are computed from the
same per-frame records (no extra rendering).

### 2.6 Outputs and runner integration
- `tests/sample_frames.py [--levels 0,1,2,3] [--frames N] [--update] [--check-fixture] [--shots DIR] [--port]`
  serves `site/` with the existing `build_tiles.serve()` helper, drives Chromium via Playwright,
  writes `docs/density/report.json` (per frame) and `docs/density/summary.md` (per level: pass
  rate, p05/p50/p95 of each metric, worst 10 frames with `?x=&y=&z=` links), and saves the
  screenshots of failing frames plus 3 random passing frames per level to `docs/density/shots/`
  for Alan's mobile review. Exit 1 on any hard failure or a soft pass rate < 95 %.
- `scripts/gate.sh` (new, single entry point) runs in order: `validate.py --offline`,
  `check_research.py --fast`, `fixtures/run.sh` (FIXTURE_OFFLINE=1), `pytest tests/unit`
  (extractor, geometry parity, DEM, placement — pure Python, < 20 s), `site/check_geo.py`,
  `tests/sample_frames.py --check-fixture`, `tests/sample_frames.py`. Prints `GATE: PASS|FAIL`.
- CI: `.github/workflows/gate.yml` on PR and push to `main`/`refactor/*`, ubuntu-latest,
  `uv sync` + `playwright install chromium`, runs `scripts/gate.sh`, uploads `docs/density/` as an
  artifact. Pages deploy (`pages.yml`) gains `needs: gate`.
- Pre-commit: `.githooks/pre-commit` runs the fast subset (`validate.py --offline`, `pytest tests/unit`,
  `--check-fixture`); the worker sets `git config core.hooksPath .githooks` once.

### 2.7 Additional validation tests (the "invest in more" list)
| Test | Kind | Asserts |
|---|---|---|
| `tests/unit/test_geometry_parity.py` | pytest | Python `geometry.py` reproduces the SVG plate: same coast loop count, continent centroids within 2 units of `site/labels.json` (frozen copy in fixtures), shared borders identical (hash of edge polylines). |
| `tests/unit/test_placement.py` | pytest | `place_entities.py` is deterministic (same input → byte-identical GeoJSON), every entity inside its country polygon, min spacing ≥ 6 units, x = X(year) within 0.5 unit. |
| `tests/unit/test_extract.py` | pytest | extractor on `tests/fixtures/research_mini.md` yields exact expected YAML; year parsing table (`1958–59→1958.5`, `Nov 2016→2016.87`, `c. 1666→1666.0 flag=approx`); every `[n]` resolved or reported. |
| `tests/unit/test_dem.py` | pytest | DEM shape/dtype, sea = 0, land ≥ 1, summit heights monotone in spec value, every pass is a local minimum along the ridge, hachure segments only where slope > 8°. |
| `site/check_geo.py` | Playwright/shapely | ports every `check_layout.py` gate to GeoJSON: one mainland loop (+ isles), adjacent continents share borders, zero overlap, envelope bounds ± wobble, all countries inside their continent. |
| `tests/test_style.py` | pytest | `style.json` lint: every symbol layer has `text-allow-overlap:false`, `symbol-sort-key`, size stops within the §2.4 font caps, `minzoom/maxzoom` consistent with the level table, glyphs/sprites are relative URLs. |
| `tests/test_links_sample.py` | network, nightly only | 50 seeded sources per continent through `check_links.sh` (full run stays monthly). |

## 3. Map Architecture & Tech Stack Evolution

### 3.1 Why MapLibre GL JS
The monolithic SVG plate screenshotted into raster tiles failed Alan's review for structural reasons:
1. **Raster blur at fractional zooms:** A 412 px phone zooming from 1.0 to 1.8 scales up the lower raster level, producing blurry text.
2. **Offline label baking:** Labels are hardcoded into static tiles; zooming in cannot dynamically reveal smaller, denser text or suppress parent labels without re-rendering entire raster tile pyramids.
3. **Huge asset overhead:** 5,127 PNG tiles (141 MB) for only 3 populated continents; expanding to 10 continents with dense papers would exceed 500 MB.

**The Solution:** Transition to **MapLibre GL JS** with vector feature layers (GeoJSON / PMTiles) and a raster DEM hillshade.
- Vector text rendered via Signed Distance Field (SDF) glyphs: permanently crisp at all fractional zooms and high DPR (2×/3×).
- Native, GPU-accelerated collision detection: `symbol-sort-key` guarantees that important landmarks and capitals win placement, and text never overlaps.
- Static hosting: MapLibre runs entirely client-side on GitHub Pages without a dynamic tile server.

### 3.2 Coordinate System & Zoom Mapping
The map uses an unprojected planar coordinate system mapped to Web Mercator bounds:
- Plate width $W = 1800$, height $H = 1050$.
- Plate → lng/lat mapping (binding, supersedes the earlier bbox text `[[-1050, 0], [0, 1800]]`):
  `lng = (x − 900) / 50`, `lat = −(y − 525) · 1.8 / 50` (1 plate unit = 0.02° lng, 0.036° lat; `LAT_SCALE = 1.8` is the
  Phase 4c task E vertical exaggeration of the land band for portrait phones — measured p50 sea_ratio z1 0.82 → 0.67,
  z2 0.45 → 0.34; the renderer's `toPlate` inverts it so `?x=&y=` deep links round-trip unchanged; implemented in
  `scripts/export_geojson.py`, `scripts/layout_countries.py`, `site/v2/index.html`, `style.json` metadata). Semantic zoom = MapLibre zoom 1:1.
- **The Four Semantic Zoom Levels:**
  - **z0 World ($z = 3.0$):** Global continent shapes, ocean basins, major era dates, and the Silicon Range spine. Max font 42px.
  - **z1 Regions / Provinces ($z = 4.5$):** Continents split into labeled provinces; major landmark hints appear; mountain peaks labeled. Max font 28px.
  - **z2 Countries / Schools ($z = 6.0$):** Country boundaries solid; paradigm tags and regional hubs labeled; major historical papers appear. Max font 16px.
  - **z3 Papers & Artifacts ($z = 7.5$):** Dense paper-level detail; one-line facts; specific equations; hardware chip specs and mountain passes. Max font 13px.
  - *Overzoom ($z \le 8.5$):* Allows close inspection without revealing new layers or bloating font sizes.

### 3.3 Style Specification & Layer Order
The MapLibre style (`site/v2/style.json`) defines strict rendering layers:
1. `background`: Aged parchment fill (`#dccfae`).
2. `ocean-waves`: Subtle contour wave linework.
3. `terrain-hillshade`: 2D DEM shaded relief layer (opacity 0.45, azimuth 315°).
4. `continent-fill`: Semi-transparent biome textures (`forest`, `grassland`, `highland`, `wetland`, `jungle`).
5. `terrain-hachures`: Vector engraved hachure strokes along ridges and steep slopes.
6. `continent-borders` & `country-borders`: Hand-drawn style ink boundaries.
7. `terrain-passes` & `rivers`: Linear infrastructure and connectionist waterways.
8. `symbol-landmarks`: Summits, passes, and papers (dots + compact labels).
9. `symbol-countries`: Crisp country labels with halos.
10. `symbol-continents`: Grand macro titles (fades out at $z \ge 5.0$).

---

## 4. Topographic Terrain & The Silicon Range

### 4.1 2D Digital Elevation Model (DEM)
Terrain will no longer be drawn as a 1D SVG line stroke. A dedicated generator (`scripts/build_dem.py`) creates a continuous float32 heightfield array ($3600 \times 2100$, 2 samples per plate unit):
- **Basal Land Elevation:** Base elevation of 10–30m above sea level across all landmasses, smoothly dropping to 0 at the coastlines.
- **Mountain Ridge Backbone:** Procedural ridge paths following the hardware lineage seam (S1/S2 boundary), modulated by multi-octave Perlin/simplex noise for natural, organic cragginess.
- **Summit Heights:** Milestone peaks rise naturally from the ridge with elevations proportional to historical impact:
  $$\text{Elevation} = H_{\text{ridge}} + K \cdot \log_{10}(\text{Transistors} \cdot \text{FLOPS})$$
- **Passes & Saddles:** True mathematical saddles carved between peaks where software architectures crossed hardware (e.g. `CUDA Pass`, `AlexNet Gap`, `Tensor Core Saddle`).

### 4.2 Hillshade & Engraved Hachure Generation
1. **Terrarium RGB Raster-DEM:** The heightfield is encoded into Terrarium format:
   $$\text{elevation} = (R \cdot 256 + G + B / 256) - 32768$$
   Sliced into standard 256px tiles for MapLibre's native `hillshade` renderer.
2. **Vector Hachures (Lehmann's Rule):** A vector generator computes slope and aspect across the heightfield:
   - Stroke direction points along the gradient (direction of steepest descent).
   - Stroke thickness and spacing follow Johann Georg Lehmann's classic 1799 cartographic law: steeper slopes produce darker, denser strokes.
   - Outputs to `site/data/hachures.geojson` as crisp vector ink lines.

### 4.3 Embedded Hardware Milestones & Passes
Hardware milestones are embedded as topographical features:
- **Summits:** Distinct peak symbols with elevation spot-heights and technical specs:
  - *Mt. Blackwell (2024):* 208B transistors, 20 PFLOPS FP4.
  - *Hopper Peak (2022):* 80B transistors, Transformer Engine.
  - *AlexNet Crag (2012):* 2× GTX 580, 1.5GB VRAM.
  - *Jalapeño Butte (2026):* First custom inference ASIC, pareto frontier.
- **Passes:** Depicted with standard mountain pass symbols `)(`:
  - *CUDA Pass (2007):* Connecting graphics hardware to general-purpose computing.
  - *FlashAttention Gorge (2022):* Memory-hierarchy IO-aware optimization.

---

## 5. Content Ingestion & Population Pipeline

### 5.1 The 2,000-Entity Target
To eliminate dead zones permanently, the map requires **1,500 to 2,500 dated, sourced entities** across all 10 continents. 
Content will be parsed systematically from `research/01` through `research/09` using `scripts/extract_entities.py`.

### 5.2 Western Continents De-clustering (Zero Dead Zones)
The four western continents will be decomposed into full country and event layers:
1. **The Statistical Isthmus (1988–2011) — The $x=829.9$ Dead Zone:**
   - *Country 1: The Support Vector Escarpment (1992–1998)* — Vapnik, Cortes, soft-margin SVM, Mercer kernels.
   - *Country 2: The Ensemble Highlands (1995–2001)* — Breiman's Bagging & Random Forests, AdaBoost, Gradient Boosting.
   - *Country 3: The Bayesian Plateau (1988–2003)* — Judea Pearl's Belief Propagation, Variational Methods, LDA.
   - *Country 4: The Graphical Valley (1988–2009)* — Junction-tree algorithm, HMMs, Rabiner tutorial, CRFs.
   - *Country 5: Probabilistic Robotics Marsh (1999–2005)* — Thrun's Stanley, Particle Filters, SLAM.
   - *Country 6: The Web & Corpus Coast (1998–2009)* — PageRank, Penn Treebank, "Unreasonable Effectiveness of Data".
2. **The Connectionist Revival (1982–1998):**
   - Hopfield networks (1982), Backpropagation revival (Rumelhart, Hinton, Williams 1986), PDP Research Group, LeNet-1/5 (1989–1998), TD-Gammon.
3. **The Symbolic Heartland (1956–1974):**
   - Dartmouth Workshop (1956), Logic Theorist, Lisp (McCarthy 1958), Resolution refutation (Robinson 1965), SHRDLU, Shakey the Robot.
4. **The Cybernetic Shore (1943–1956):**
   - McCulloch–Pitts neurons (1943), Hebbian learning (1949), Turing's Imitation Game (1950), SNARC (1951), Samuel's Checkers (1952).

### 5.3 Event Data Schema
Events are stored in `data/events/<continent_id>.yaml` adhering to strict schema:
```yaml
- id: svm-soft-margin-1995
  name: "Soft-Margin SVM"
  country_id: support-vector-escarpment
  year: 1995.7
  band: C
  sub_band: Cb
  lod: 3                   # 1=Landmark, 2=Regional Hub, 3=Headline Paper, 4=Artifact
  one_line: "Cortes & Vapnik introduce the soft-margin support vector network."
  sources:
    - title: "Cortes & Vapnik (1995)"
      url: "https://doi.org/10.1007/BF00994018"
  specs: "Margin slack formulation · C parameter"
```

---

## 6. Implementation Roadmap & Milestones

| Phase | Milestone | Deliverables | Exit Gate |
|---|---|---|---|
| **Phase 1** | **Deterministic Mobile Test Suite** | `tests/sample_frames.py`, fixture generator, baseline report `docs/density/baseline.json`. | Hard gate running in CI; deterministic 150-frame sampling per level. |
| **Phase 2** | **Massive Content Population** | `scripts/extract_entities.py`, full YAMLs for all 10 continents (2,000+ entities). | `validate.py --offline` passes on all 10 continent event files; 0 entity errors. |
| **Phase 3** | **Topographic Terrain Engine** | `scripts/build_dem.py`, float32 DEM array, Terrarium hillshade tiles, vector hachures. | Continuous 2D shaded relief; test_dem.py passing; hachures aligned to slope. |
| **Phase 4** | **MapLibre GL JS Engine Integration** | `site/v2/index.html`, `site/v2/style.json`, SDF glyphs, GeoJSON feature pipelines. | Vector rendering active; zero clipping; text permanently sharp at DPR 2/3. |
| **Phase 5** | **Verification & Cutover** | Run `tests/sample_frames.py` against v2; compare against baseline; switch `site/index.html` to v2. | `sample_frames.py` PASS (density thresholds met in 95%+ land frames; 0 dead zones). |

---

## 7. Automated Cron Worker Schedule & Workflow

### 7.1 Cadence and Concurrency
- The cron worker runs every **3 hours** (`schedule: 'every 3h'`).
- The worker executes on a dedicated branch `refactor/v2`.
- **Idle Guard:** Script `/home/node/agent/scripts/map_of_ai_watchdog.py` checks active processes and thread turns. If a user turn occurred within the last 30 minutes, the cron worker exits silently (`STATUS: ACTIVE_CONVERSATION`).

### 7.2 The Outcome-Gated Execution Contract
Every automated cron session must execute this precise cycle:
1. `git checkout refactor/v2 && git pull origin refactor/v2`
2. Run `tests/sample_frames.py` to identify the **top 10 lowest-density or failing frames**.
3. Claim exactly ONE bounded task from the next unfinished Phase in `REFACTOR_PLAN.md`.
4. Implement the changes (add content YAMLs, adjust style layers, or tune terrain).
5. Re-run `tests/sample_frames.py`.
6. **Verification Gate:**
   - If the density score improved or a failing frame passed: commit with descriptive message, push to `refactor/v2`, and output progress.
   - If density regressed or hard gates failed: revert changes (`git reset --hard`), log failure reasons to `ORCHESTRATOR_LOG.md`, and exit without pushing.
7. When all Phase 5 gates pass on `refactor/v2`, merge `refactor/v2` to `main`.

