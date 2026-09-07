# site/ — review prototype (P2-T1-RENDER v4)

Single static page rendering `data/continents/REGISTRY.md` as an antique-atlas plate
(X = time, piecewise-scaled per AXES.md §1; Y = the five AXES.md §3 bands as faint
latitudes; terrain texture = biome). Deployed to GitHub Pages by `.github/workflows/pages.yml`.
No build step, no API calls from the browser — everything is static.

- `index.html` — all HTML/CSS/JS inline. Fonts: Cinzel (names/titles) + Lora (body) via Google
  Fonts, Georgia fallback. **All text is vector SVG text** (names, subtitles, years, ruler,
  band labels, legend, cartouche title) — nothing textual is baked into an image.
- `assets/textures/` — generated terrain art, committed as static assets (~1 MB total):
  `parchment.jpg` (page + plate ground), `sea.jpg`, one seamless tile per biome
  (`highland` `grassland` `forest` `jungle` `wetland` `harbour` `mixed`, 512 px), plus two
  alpha cut-outs: `compass.png` (16-point rose, no letters) and `cartouche.png` (blank frame).
- `gen_textures.py` — one-off generator: one call per asset to Vertex AI `gemini-2.5-flash-image`
  (project `alanblount-sandbox`, `us-central1`, ADC via `gcloud auth print-access-token`), a single
  shared prompt template with only the terrain clause swapped, raw 1024² PNGs to `/tmp/tex/raw`.
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

v4 draws **one contiguous mainland**, not floating shapes. The mainland is a partition of a
(year × half-band) cell grid — `COLS` are the registry start/end years, `ROWY` the band edges
(N2 and C split in half) — and every cell has exactly one owner, so neighbours share their
border by construction. Each grid edge becomes the *same* deterministic wobbly polyline for
both of its cells (noise keyed by the edge), then a 3-octave domain warp bends the whole
plate, so shared borders coincide exactly and nothing is axis-straight. Each continent's fill
is an SVG `<pattern>` of its biome texture plus a faint biome-tint wash and a hand-tinted
border band; the ink coastline, waterlines, and province borders are vector strokes on top.
The pre-1943 Antecedent Isles stay a separate offshore archipelago (B-spline islets, same
texture/ink treatment).

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
