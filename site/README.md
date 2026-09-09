# site/ — review prototype (P2-T1-RENDER v10)

Single static page rendering `data/continents/REGISTRY.md` as an antique-atlas plate
(X = time, piecewise-scaled per AXES.md §1; Y = the five AXES.md §3 bands as faint
latitudes; terrain texture = biome). Deployed to GitHub Pages by `.github/workflows/pages.yml`.
No build step, no API calls from the browser — everything is static.

**Artistic license (v7, per Alan 2026-09-07):** the registered band span and time range are a
rough directional *envelope*, not a box to fill edge to edge. A region may recede to open sea
in some of its sub-bands for part of its span (see the "v7 east" comment block in `index.html`
for the chosen story: the Transformer Plateau is language-first and never reaches S2; the
Generative Coast arrives from the south in 2021, and its N1 reach is a late, thin cape; the
present-day frontier is a three-step ragged coast). The map must stay roughly and directionally
right — it is more art and information than a chart from which facts could be derived. The
check_layout gate enforces only the *outer* bound of each envelope (plus a declared ≤ 0.9-yr
`LICENSE_YR` overshoot for the two eastern regions' shared staircase seam).

- `index.html` — all HTML/CSS/JS inline. Fonts: Cinzel (names/titles) + Lora (body) via Google
  Fonts, Georgia fallback. **All text is vector SVG text** (names, subtitles, years, ruler,
  band labels, legend, cartouche title) — nothing textual is baked into an image.
- `assets/textures/` — generated terrain art, committed as static assets (~1 MB total):
  `parchment.jpg` (page + plate ground), `sea.jpg`, one seamless tile per biome
  (`highland` `grassland` `forest` `jungle` `wetland` `harbour` `mixed`, 512 px), plus two
  alpha cut-outs: `compass.png` (16-point rose, no letters) and `cartouche.png` (blank frame).
- `gen_textures.py` — one-off generator: one call per asset to Vertex AI `gemini-3-pro-image`
  (Nano Banana Pro, GA; project `alanblount-sandbox`, **global endpoint only** —
  `aiplatform.googleapis.com/v1/.../locations/global/...`, regional endpoints 404 for this model;
  ADC via `gcloud auth print-access-token`), a single shared prompt template with only the terrain
  clause swapped, `imageConfig` pinned to 1:1 / 1K (default output is 1408×768), raw PNGs to
  `/tmp/tex/raw`. Model policy (Alan, 2026-09-07): no Gemini 2.x anywhere; latest tier per
  docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/3-pro-image.
  Every output was vision-checked; prompts were iterated until no fake text, no grids, no
  vignette framing. Not run in CI, not run at page load.
- `prep_textures.py` — deterministic post-processing of the raw PNGs into `assets/textures/`:
  flatten (divide by a coarse brightness estimate → no vignette), offset-and-heal seamless
  wrap (no mirroring → no butterfly symmetry), lift dense tiles toward paper so labels stay
  legible, JPEG q80; compass/cartouche → RGBA ink cut-outs (baked paper removed).
- `build_registry_json.py` — parses REGISTRY.md (via `scripts/check_registry.py`'s parser) into
  `registry.json`; run it after editing the registry. The Pages workflow runs it on every deploy.
- `check_layout.py` — headless-Chromium (Playwright) review gate on the *rendered* SVG:
  exactly one mainland coastline loop (+4 isles); every chronologically adjacent pair of
  continents shares a border (fills within 2 px); zero fill overlap; every continent inside
  the coast; each continent's rendered extent matches its REGISTRY band span and start/end
  year (± hand-drawn wobble budget, read from `registry.json`); every land fill is a texture
  pattern with real luminance variance (not flat colour); no label/label or text/text overlap;
  inside labels wholly inside their own fill; leaders land on the right continent; no text
  clipped by the viewBox; all assets HTTP 200 and nothing fetched off-site but fonts.
  Writes `--shot` screenshots. Run:
  `PLAYWRIGHT_BROWSERS_PATH=... python3 site/check_layout.py` (needs playwright + pillow).
- Local preview: `python3 -m http.server -d site 8765` → http://localhost:8765/

## Placement model (render-only; not registry data)

v5 draws **one contiguous mainland**, not floating shapes. The mainland is a partition of a
(year × half-band) cell grid — `COLS` are the registry start/end years, `ROWY` the band edges
(N2 and C split in half) — and every cell has exactly one owner, so neighbours share their
border by construction. Each grid edge becomes the *same* deterministic wobbly polyline for
both of its cells (noise keyed by the edge), then a 3-octave domain warp bends the whole
plate, so shared borders coincide exactly and nothing is axis-straight. Each continent's fill
is an SVG `<pattern>` of its biome texture plus a faint biome-tint wash and a hand-tinted
border band; the ink coastline, waterlines, and province borders are vector strokes on top.
The pre-1943 Antecedent Isles stay a separate offshore archipelago (B-spline islets, same
texture/ink treatment).

### v5 — from strip to landmass (geometry only; data mapping unchanged)

v4 was rejected as "a bar chart": a straight horizontal strip cut by plumb year lines. v5
keeps the two load-bearing encodings — **x is time** (AXES.md non-linear scale, unchanged
`X(year)`) and **perpendicular offset is the domain band** — but bends and roughens the
skeleton:

- **Spine.** The whole plate is sheared vertically along a gentle S-curve `spineY(x)`
  (±46px). Screen `y = plate y + spineY(x)`; bands are read as offset from the spine, and
  the faint latitude graticule follows it so a reader can still place a region in its band.
  x is untouched, so the ruler stays honest.
- **Wandering shared borders.** Every grid edge is one cached polyline shared by both
  cells: a diagonal sweep + 2-lobe meander + low-frequency noise + hand wobble, all bounded
  by 25% of the narrower neighbouring column/row so borders can never cross. Year borders
  additionally get a per-column diagonal **lean** (top pushed one way, bottom the other,
  alternating per column) and an alternating zig-zag on the vertices, so no year border is
  plumb. Coast edges get an extra seaward cape/bay bulge.
- **Feathered textures.** Each region's texture is painted once more as a geometrically
  dilated copy (+14px, `dilatePath`) under an alpha-only feather filter and clipped to the
  mainland, so glyphs crossfade into the neighbour instead of being sliced at the border.
  (Stroking the outline with the pattern paint does not work in Chromium — it renders
  transparent — hence the dilation.)
- **Texture scale.** `highland`, `grassland`, `mixed` regenerated with an explicit
  "glyphs ≈ 3–4% of image width" scale clause (`gen_textures.py`); per-biome tile factors
  `BIOME[k].k` equalise the on-map zoom of all seven fills. Forest/jungle/wetland/harbour
  reused unchanged.
- **Labels.** All labels carry a parchment halo filter; the band legend sits in its own
  parchment box east of the coast; the Antecedent Isles get a leader like the Shore/Plateau.

`check_layout.py` gained two v5 gates: `straightBorders` (every adjacent pair's shared
border must wander ≥ 4px RMS from its best-fit line *or* tilt ≥ 6° from vertical) and
`flatSpine` (the spine must actually bend); the band-fidelity check now works in plate
coordinates (`y − spineY(x)`) so the bend cannot hide a band violation.

The 1974–2011 cluster (REGISTRY.md D2/D4 overlaps) is realised as:

- winter-steppes — N1–N2 from 1974; from 1980 it keeps N1 while the plateau takes N2 beneath it;
- expert-systems-plateau — N2, 1980–1993, nested under the steppes ("warm valley", D2);
- the **Winter Gulf** — open sea in C–S2 for 1974–1982: the heartland ends on the 1974
  escarpment and nothing stands south of the steppes until the revival opens in 1982;
- connectionist-revival — C–S2 from 1982; from 1988 the isthmus takes upper C;
- statistical-isthmus — a neck in upper C between plateau and revival from 1988 (Pearl),
  widening to N2–S1 once the steppes/plateau (1993) and revival (1998) end; a southern bay
  (S2) opens 1998–2006 before the basin;
- deep-learning-basin — S1–S2 from 2006, the full C–S2 span once the isthmus ends (2011).

Registry `band span` values are unchanged; these are their pixel realisations, and
`check_layout.py` fails if any rendered continent leaves its registry span.
