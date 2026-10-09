# Gemini 4 Argon took a stalled 34-session repo from 0% to 100% in two passes

*Gemini 4 field notes*

**Title options (85 characters or fewer)**

1. Gemini 4 Argon took a stalled 34-session repo from 0% to 100% in two passes (75, recommended)
2. How Gemini 4 Argon rescued a 360-year interactive map of AI in two passes (73)
3. When your agent stalls at 0%: rescuing a broken UI build with Gemini 4 Argon (76)
4. From 34 stalled sessions to 60fps: building the Map of AI with Gemini 4 Argon (77)

**TL;DR**

I wanted to build an interactive map of AI history from 1666 to 2026 (inspired by [mapofmetal.com](https://mapofmetal.com) and old Swiss relief maps) where you can zoom smoothly from whole eras down to individual papers, labs, and models. I spent five days and 34 sessions with another frontier model trying to get it working. It generated plenty of markdown specs and code, but when we ran a 100-frame mobile viewport test (`tests/sample_frames.py`), **`0 out of 100` frames passed**. Text overlapped everywhere, labels drifted out of sync when zooming, and four of the ten continents had zero landmarks on them.

I handed the stalled repo to **Gemini 4 Argon** with a one-paragraph prompt: rethink it from first principles, pack it with everything that belongs in a 2036 AI textbook, and make it feel great. In two passes (`b6f2011a..8ad7f929`), Argon took the exact same 100-frame mobile test from **`0.0%` (`0/100`) to `100.0%` (`100/100`)**. From there, we ran a few rounds of post-review polish (the commits after `8ad7f929`): expanding the catalog to **517 primary-sourced landmarks** (including **10 outlying islands**), organizing the entire historical graph as a **601-file Open Knowledge Format (OKF v0.2) LLM Wiki** (`wiki/`), compiling **79 causal Lineage Post Roads** (`492` directed edges), and refining the **`7,599` multi-scale copperplate tiles (`z=0..4`)**.

**Byline**

Alan Blount

**Live links**

- Public site: [mapofai.dev](https://mapofai.dev) ([github.com/zeroasterisk/map-of-ai](https://github.com/zeroasterisk/map-of-ai))

[![Map of AI: The 2036 Textbook Atlas (mapofai.dev)](https://mapofai.dev/assets/screenshots/map-of-ai-hero.png)](https://mapofai.dev)

---

## The scorecard: 34 sessions vs. Gemini 4 Argon

Every build was graded by the same headless Playwright test (`tests/sample_frames.py`), which checks 100 mobile viewports across four zoom altitudes (`z0` through `z3`). Every frame has to hit a minimum label and landmark floor with zero overlapping text boxes and zero clipped labels.

| What we measured | Act I: Other frontier model (34 sessions, `24411faa`) | Act II: Gemini 4 Argon two-pass rescue (`8ad7f929`) | Post-review polish (`HEAD`) |
| :--- | :--- | :--- | :--- |
| Mobile viewport test (`tests/sample_frames.py`) | `0.0%` (`0 / 100` frames passed) | `100.0%` (`100 / 100` frames passed) | `100.0%` (`100 / 100` frames passed) |
| Why frames failed | `81/100` had overlapping text, `19/100` were empty | `0` overlaps, `0` clipped labels, `0` empty frames | `0` overlaps, `0` clipped labels, `0` empty frames |
| Historical dataset | `6` populated continents (4 western continents had `0` events) | `10` continents, `49` provinces, `365` milestones | `576` entries (`10` continents, `49` provinces, `10` outlying islands, `517` landmarks) + `601`-file OKF v0.2 LLM Wiki (`wiki/`) |
| Map terrain | Static SVG + 2.5D cartoon mountain stamps (`5,755` tiles, `156 MB`) | `2,549` pure-terrain 2D DEM relief tiles (`z=0..3`) with Imhof hillshading & Lehmann hachures | `7,599` multi-scale 2D relief & copperplate micro-cartography tiles (`z=0..4`) with clean interiors |
| Historical interconnections | Short dashed lines that stopped at province borders | Intra-province chronology chains | `79` OKF-compiled West-to-East Lineage Post Roads (`10` trunks, `14` branches, `55` spurs = `492` causal edges) with interactive highlighting |
| Zoom and label behavior | Jerky discrete zoom jumps; labels lagged behind tiles | 60fps continuous cursor-locked zoom; vector labels locked to world coordinates | Hardened post-zoom bounds clamping & parent/child tile retention across `z=-1.0..5.0` |

---

## Act I: Why 34 sessions with another model stalled at 0%

Building an interactive map from scratch is a great stress test for a coding agent because data, cartography, and viewport math all share the same screen space. If you tweak one without understanding the other two, the whole thing falls apart (the classic trap where fixing a layout bug on desktop breaks 80 mobile frames).

Over 34 sessions, the previous model got stuck in four ruts:

First, when asked to move from a single SVG to map tiles, it baked all the text labels and pins directly into 5,755 PNG images (`156 MB`). Zooming in turned the text into blurry pixels, and zooming out crushed dozens of tiny labels on top of each other (`81 out of 100` test frames failed on text overlap).

Second, it drew highland regions by stamping 2.5D side-view cartoon mountain wedges (`/\`) onto a flat top-down map. Besides looking like a pirate treasure map, the side-view peaks didn't line up with top-down coordinates when zooming.

Third, even though the markdown research files covered 1666 to 2026, the model only wired up province polygons and events for six of the ten continents. Four entire western continents (Antecedent Isles, Cybernetic Shore, Winter Steppes, and Expert Systems Plateau) rendered as blank land with zero milestones (`19 out of 100` mobile frames failed with empty viewports).

Fourth, panning and zooming stepped in discrete jumps and re-calculated DOM label positions after the zoom finished, so the labels visibly floated and snapped after every scroll tick.

---

## Act II: Handing the broken repo to Gemini 4 Argon (0% to 100% in two passes)

Instead of spoon-feeding CSS fixes or pointing to specific files, I gave Gemini 4 Argon the stalled repository and a short brief:

```text
I want you to consider it from first principles and make an implementation which is
informed by the github repo, solve exactly the same needs, but use Gemini 4 (you) and
make it actually work a lot better, be more attractive, more fluent when zooming, and
contain a lot more data. Anything which belongs in a textbook in 2036 should be
represented, showing off "altitudes" which do a great job of presenting the right level
of data at the right time, and making it beautiful and fun. This is now yours. Show off.
```

Argon's first pass rebuilt the terrain generator, filled in the missing centuries of data, and wired the altitude tiers. I tested it in the browser and sent a follow-up note on how the zoom felt:

```text
I like the mountains, I like the density of information. I dislike the labels which are
out of sync with zooming in. I would like it to zoom more smoothly and more quickly,
like Google Maps. Right now it feels jerky, like I zoom in a little and it jumps up or
down... Google Maps lets me zoom in fast and it goes fast, or slow and it zooms in
slowly, and whenever I stop zooming it immediately stops. There are clearly overlays
but they always line up correctly and are never out of sync.
```

Across those two passes (`b6f2011a..8ad7f929`), Argon solved the core architectural failures and brought `tests/sample_frames.py` from `0.0%` to `100.0%`:

### 1. Stripped text out of the PNG tiles and locked vector labels to world coordinates
Argon threw out the `156 MB` of blurry text-baked tiles and split the renderer cleanly in two. The raster tile pyramid holds only paper texture, ocean waterlines, terrain detail, roads, and 2D relief. All continent banners, province headers, and milestone pins live as crisp vector elements anchored in world coordinates inside `.leaflet-labels-pane`. When you zoom, the GPU scales the vector pane and the tile pane with the exact same matrix transform, so labels never drift or lag behind the terrain.

### 2. Replaced cartoon mountain stamps with real 2D topographic relief
Instead of pasting triangular mountain icons, Argon wrote a Python elevation model (`scripts/build_dem.py`) that synthesizes a continuous `1800x1050` heightfield along the Silicon Range, rendering five nested marching-squares elevation contour bands, 315-degree northwest hillshading, and Lehmann slope hachure strokes aligned to the terrain gradient.

### 3. Patched Leaflet's integer rounding for Google Maps physics
Argon traced the zoom judder to four Leaflet 1.9.4 methods (`_getNewPixelOrigin`, `latLngToLayerPoint`, `_setZoomTransform`, and `_reset`) that call `.round()` on pixel coordinates, causing 1-pixel staircase judder during slow zooms. Patching those four methods to preserve floating-point coordinates and adding a velocity-proportional wheel controller made scroll speed map directly to zoom speed and stop on the exact frame your fingers stop moving (`0 ms` coasting).

---

## Post-review polish: What we added after the `100%` baseline (commits after `8ad7f929`)

Once the core rescue hit `100/100` at `8ad7f929`, we kept iterating on the repository the way you do on any real engineering project: reviewing the live map at high zoom, spotting edge cases, and adding three layers of polish:

### 1. More data + an Open Knowledge Format (OKF v0.2) LLM Wiki (`wiki/`)
First, we expanded the catalog from `365` to **517 landmarks** (`475` milestone events, `15` Silicon Range hardware summits, and `27` milestones across **10 newly populated Outlying Islands** for alternative paradigms like Cyc, Reservoir Computing, BDI Agents, and Neuromorphic Engineering) and asked Argon to connect related milestones with West-to-East roads:

```text
openai founded and tensorflow opensourced right next to each other.... fine
but I would kindof expect a road going east from each of those, connecting OpenAI to all
of their models and other news stories, and a road going east (or perhaps sharing some of
the same roads) connecting tensorflow to pytorch and TPUs.
since we now have these tiles (good job) let's use them to tell the story better with
interconnections. warning - don't make a mess... it still needs to be aesthetically
pleasing and we can omit or miss details as reasonable sacrifices to keep the aesthetics...
this is an art piece as well as information.
```

In our first road pass, a procedural nearest-neighbor loop wired unlinked pins to whichever milestone was closest in the same province, which accidentally connected OpenAI's `GPT-4o (2024)` to the `2024 AI Nobel Prizes` awarded to Demis Hassabis, John Jumper, John Hopfield, and Geoffrey Hinton just because their pins sat 19 pixels apart.

To fix that class of bug permanently, we had Argon organize all `475` milestones, `47` spatial provinces, and `79` lineage roads into a **`601`-file Open Knowledge Format (OKF v0.2) LLM Wiki** (`wiki/`) and audit every edge against three explicit questions:
- *Would a lawyer complain about this implied relationship?*
- *Would someone on Reddit (`r/MachineLearning`) complain about this implied relationship?*
- *Would the researchers or laureates involved complain about this relationship?*

### 2. 79 causal Lineage Post Roads compiled from the OKF Wiki
Argon deleted the procedural nearest-neighbor spur generator and wrote a deterministic compiler (`scripts/compile_okf_roads.py`) that compiles the OKF v0.2 wiki directly into **79 named Lineage Post Roads** (`10` primary trunks, `14` cross-province branches, and `55` thematic/lab spurs = `492` directed causal edges) with `100%` milestone coverage (`475/475`) and `0` chronological reversals:
- `AI Nobel Prizes (2024)` is now fed exclusively by its two actual prize lineages: `AlphaFold 2 -> ... -> AlphaFold 3 -> AI Nobel Prizes` (*The DeepMind, AlphaGo, AlphaFold & Science Causeway*) and `Hopfield network -> Boltzmann machine -> Deep Belief Nets -> DNNresearch -> Vector Institute -> Hinton leaves Google -> AI Nobel Prizes` (*The Hopfield-Hinton Physics Nobel Lineage Road*).
- `GPT-4o (2024)` connects strictly along *The OpenAI Post Road* (`GPT-4 Turbo -> GPT-4o -> GPT-4o mini`) and *The OpenAI o1, o3 & Test-Time Reasoning Branch* (`GPT-4o -> o1-preview -> o1 -> o3 -> GPT-5`).
- Hovering or clicking any milestone highlights its connected West/East roads on the map and lets you walk step-by-step along the lineage in the Citation Inspector.

[![Deep Learning Gateway (z=4.8): Interactive Lineage Post Road highlighting and Citation Inspector](https://mapofai.dev/assets/screenshots/map-of-ai-lineage-roads.png)](https://mapofai.dev/?z=4.8&x=1066.9&y=612.5)

### 3. Multi-scale copperplate tiles (`z=0..4`) and visual decluttering
Finally, we extended the tile pyramid to `z=0..4` (`7,599` tiles) so zooming into `Alt 3` Syllabus (`z=3.6`) and `Alt 4` Archive (`z=4.8`) replaces low-zoom raster textures with crisp vector copperplate micro-cartography: woodcut trees, marsh reeds, alpine crags, engraved town rosettes, and Vauban star-citadel fortifications. When we noticed that inward polygon offset lines (`dilatePath`) were folding inside-out into sharp zig-zag triangles at concave province corners (and that Leaflet's `maxBounds` was clamping against the pre-zoom scale during scroll-wheel zoom-out), Argon stripped out the noisy inward offset loops, replaced `maxBounds` with a post-zoom bounds helper, and verified the final plate across 3 automated Playwright UX rounds and all 100 mobile frames.

[![Syllabus Altitude (z=3.6): Multi-scale copperplate micro-cartography, town rosettes, and lineage post roads](https://mapofai.dev/assets/screenshots/map-of-ai-alt3.png)](https://mapofai.dev/?z=3.6&x=1470&y=495)

---

## What stood out working with Argon

First, give Argon an automated verification harness and let it iterate. Having `python3 tests/sample_frames.py` check 100 mobile viewports, `python3 site/check_layout.py` verify 30+ geometric invariants, and `python3 scripts/compile_okf_roads.py` enforce OKF v0.2 schema and causal ordering meant every polish pass stayed at `100/100` without regressing mobile layout.

Second, use an explicit knowledge graph (`wiki/` in Open Knowledge Format) instead of spatial heuristics for semantic relationships. Proximity on a map is great for label collision detection, but terrible for historical lineage. Compiling roads from an audited OKF v0.2 wiki gave every road a verifiable rationale and eliminated cross-lab hallucinations.

Third, drive baked tile art and interactive DOM overlays from a single source of truth. By exporting event coordinates and road segments directly from the SVG plate generator during tile builds, every interactive pin sits dead-center inside its baked town rosette and road junction.
