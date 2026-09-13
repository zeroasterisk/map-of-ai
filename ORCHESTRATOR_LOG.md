# ORCHESTRATOR LOG — Map of AI (recovery/continuity notes)

> Written by the orchestrating Hermes session (not Fable) to preserve project
> state across a context compaction. If you're Fable picking up work, or a
> future orchestrator session, START HERE alongside STATUS.md.

## Current iteration status (as of this write)

- **Live:** https://zeroasterisk.github.io/map-of-ai/
- **HEAD at write time:** `47cf0d2` (v11 — biome fills visibly tinted, SHIPPED 2026-09-09)
- **In-flight job:** none.
- **Host note (2026-09-09):** the v10 session ran on a fresh host — no
  `/home/node/map-of-ai` clone, no `/tmp/pw*` Playwright setup, no `gh` in
  `~/.local/bin` (system `/usr/bin/gh` exists). Clone + the
  `headless-chromium-sandbox` skill recipe rebuilt everything in ~3 min;
  don't assume `/tmp` state survives between sessions.

## Rating history (visual review, "map-like vs bar-chart/rectangular", 1-10)

| Version | Score | What changed |
|---|---|---|
| v5 (initial curved coastline) | ~4/10 | Eastern regions still read as full-height vertical bars |
| v6 (in-region coastline wander) | 5.5/10 | Internal wobble added, still columnar |
| v7 (artistic-license asymmetry) | 6-7.2/10 | Transformer/Generative border wanders, heights differ |
| v8 (global funnel envelope) | 6.5/10 | Overall width now varies 4.7x (88px→415px) west-to-east — real structural fix. Alan's verdict after seeing v8: **"still too 90 degree rectangular... basic allocations still too rigidly along x and y grids"** |
| v9 (shipped `e2bf8c3`) | 8.5/10 (independent) | Diagonal isochrone frontiers: each region's arrival/departure year differs BY BAND. Alan: "looking pretty good" + two asks → v10. |
| v11 (shipped `47cf0d2`) | independent: "clearly more saturated, still antique" | Fix for the invisible v10 tint bump: tint solved from the wanted rendered colour (`tint = 2·target − texture mean`, wash .30→.50, band .48→.52). Lesson: the biome texture is ~80 % parchment, so any wash < .5 is mostly invisible; verify colour changes by SAMPLING RENDERED PIXELS (recipe: `/tmp/sample.py` pattern — isPointInFill sampling + PIL mean + HSV), not by reading the hex in the source. |
| v10 (shipped `c2fb8c0`) | east edge confirmed; tint bump NOT visible (independent review) | Alan's two v9 asks: (1) present-day coast now spans N1a–S2b in every column from 2024.3 (the v7 receding-N1a / ragged N2a–S2a GRID rows were the cause, not the registry or ENV); (2) BIOME tints ~2× saturation, wash .13→.30, border band .26→.48. |

## Key structural insight (v8 → v9 turning point)

The root cause of "rectangular" feel was diagnosed precisely by Alan: every
region boundary was `x = start_year`, a single x-value for the whole
boundary regardless of band (N1..S2). Wobble/noise on top of that is still
fundamentally a vertical line. The v9 fix: boundaries become
`x = f(band, year)` — genuine diagonal frontiers, e.g. a paradigm can reach
the language band years before it reaches the embodiment/control band.
Full brief is in `/tmp/fable_prompt12.txt` (not in this repo — recreate from
this log if needed, or read the git history/STATUS.md for what actually
shipped).

## Working pattern established (keep using this)

1. Single Fable job at a time against `/home/node/map-of-ai` — never run two
   concurrently, avoid git races.
2. Each dispatch: write full spec/brief to `/tmp/fable_promptN.txt`, wrapper
   script `/tmp/run_mapofaiN.sh` (git pull → export GITHUB_TOKEN/GH_TOKEN
   from `/home/node/agent/.env` → `hermes -z "$(cat prompt)" -m
   vertex-claude-fable-5-1 --yolo`, output tee'd to `/tmp/fable_runN.log`).
   Run via `terminal(background=true, notify_on_complete=true)`.
3. On completion: pull, check `git log`, read the tail of the run log for
   Fable's self-report, then **independently verify** — curl the live URL
   for `last-modified` freshness, screenshot with the Playwright script
   pattern (see any `/tmp/shot_v*.py` for the working recipe — needs
   `PLAYWRIGHT_BROWSERS_PATH=/tmp/pw-browsers`,
   `LD_LIBRARY_PATH=/tmp/localroot/usr/lib/x86_64-linux-gnu:/usr/lib/x86_64-linux-gnu`,
   `UV_CACHE_DIR=/tmp/uvcache`, run via `uv run --with playwright`), then
   `vision_analyze` on the screenshot with a non-leading prompt. Don't just
   trust Fable's self-reported rating — cross-check independently every time.
4. ADLC/spec-kit artifacts already exist in-repo: `SPEC.md`, `PLAN.md`,
   `STATUS.md` (source of truth for state), `scripts/validate.py` (V-01..V-60
   rules), decision records in `AXES.md`/`ALTITUDES.md`. Fable is instructed
   to keep `STATUS.md` current every pass — check there first for the fullest
   picture of registry/data state.
5. Alan granted "artistic license" for this creative/visual work — prioritize
   directional correctness over literal data precision.
6. Model in use for texture generation: `gemini-3-pro-image` (global endpoint
   only — regional 404s). No Gemini 2.x anywhere in the repo (verified).
7. Farm Table (`ft` CLI) is NOT installed in this sandbox. Alan flagged it as
   optional ("if you need more try farmtable"). Not needed yet — this is a
   single-track sequential pipeline, not parallel multi-agent work. Revisit
   if/when work fans out to genuinely parallel independent tracks (e.g.
   countries/cities layer built concurrently with geometry polish).

## v9 job anomaly (2026-09-08, pre-compaction) — ROOT CAUSE FOUND

Two consecutive job attempts (`proc_eedaa61d915b`, `proc_6c2011773086`) each
ran 20-25 min, exited 0, produced zero commits. Root cause found by reading
the session transcript directly (`session_search` on session id
`20260908_041306_77f71c`): Fable called `vision_analyze` on its own
screenshot and then tried to **transcribe the full analysis verbatim** in
its response, hit the output-length truncation limit, got a "continue where
you left off" system nudge, tried again, got truncated again — burning the
entire turn/time budget on narrating a screenshot description instead of
writing code. It never got past reading the geometry file before the
session ended (`agent_close`). Not a git/infra/hermes-CLI problem — a
prompting problem. **Fix for future prompts to Fable:** explicitly instruct
it to summarize `vision_analyze` output in 2-3 sentences (facts needed for
the decision only), never transcribe/quote it at length, and to prioritize
writing code over narrating analysis. HEAD is still `25c295e` (v8) as of
this checkpoint — v9 (diagonal isochrone frontiers) has NOT shipped yet.

## Next steps after v9 lands

1. Verify v9 independently (see pattern above).
2. If diagonal frontiers genuinely break the grid-aligned perception, ask
   Alan whether to proceed to the countries/cities data layer (Phase 3/4 per
   PROJECT_PLAN.md) or keep polishing continent-level geometry.
3. If v9 still reads rigid, the next lever (per Fable's v8 report) is
   possibly allowing the Deep Learning Basin to reach N2 (currently
   registry-capped at C-S2), which needs an ALTITUDES/REGISTRY decision from
   Alan, not just a render tweak.

## Session 4 (2026-09-11) — registry accepted; P3 spec gaps closed; pilot data layer

Alan accepted the continent registry (v11) as final for now and said
"continue". Work done in one pass, spec/plan first, data second:

**Phase A (spec/plan).**
- `SPEC.md` §9 P3-RENDER: visual grammar G1–G10 + binary criteria
  A-V1…A-V10 for countries inside continents. Decisions: A1/A2 zoom states
  (country labels only at A2; selected continent's name hidden, others dim to
  40 %); countries reuse the parent's texture unless `biome` differs;
  interior borders 1/3 continent stroke with the same lean/wobble discipline;
  `wall` = double stroke, `bridge` = dashed causeway; `draft` = frontier haze;
  data via `site/build_entities_json.py` → `entities.json`; continent
  geometry must not change (unit stops and files a conflict instead).
- `PLAN.md`: "registry-frozen" gate — P3-T<n> depends only on the accepted
  registry + that continent's own P2-T<n>; new P3-RENDER unit; wave table
  row 2b (P2-T8 → P3-T8 → P3-RENDER → Alan review); fixed stale P3-T6→P3-T8
  basin reference. `REGISTRY.md` header marked accepted/frozen.

**Phase B (data).**
- `data/continents/deep-learning-basin.yaml` (P2-T8): band `[C, S1, S2]`
  per the registry row (not the older SPEC §2.10 example's N2 reach);
  neighbours deferred as `pending-neighbour:` for P2-T12.
- `data/countries/` ×9 (P3-T8), one per `## Schools of thought` bullet, none
  merged/dropped: pretraining-foothills, gpu-convnet-school,
  neural-nlp-sequence-school, deep-rl-delta (S1, wetland),
  deep-generative-shoreline, speech-recognition-converts, tooling-guild
  (S1–S2, harbour), industrial-lab-founders (C–S1), chinese-state-response
  (C, grassland). Summaries 113–137 words; sibling `neighbours` filled;
  cross-continent borders as `pending-neighbour:` notes.
- `data/coverage/deep-learning-basin.md`: header (A-M1) + Table 1 (A-M2,
  9 rows = 9 bullets, awk check in file).
- Verification: `scripts/validate.py --summary` → files=10 rules=25 fails=0
  with V-20 live link checking; A-K2 script (refs ⊆ bullet [n]s) true for
  all 9; V-32 (cities) intentionally off.

**Pitfalls hit.** (1) `read_file` output is line-numbered — never splice it
back into a file (one bad write of SPEC.md, caught by `git diff --stat`,
fixed). (2) check_links.sh truncates URLs at `)` — percent-encode Wikipedia
titles with parentheses. (3) `python3` has no PyYAML; use
`uv run --with pyyaml`.

**Next.** Alan reviews SPEC §9 → build P3-RENDER against the pilot (do not
bulk-author the other nine continents' countries before the A2 view has been
seen once; the continent phase showed the render review changes the data).

## Session 5 — 2026-09-12 — P3-RENDER v2 (country layer, pre-solved partition)

**Input.** Alan handed a fully solved partition; instruction was implement +
verify, no redesign. Three commits on main: data/schema (`f7e598f`), render
(`1dfda27`), gates (`c89e7f3`).

**Data.** 7 spatial countries get `sub_band` (always a list — `["S2a"]`,
`["Cb","S1a"]` — one render path for 1- and 2-row spans); `tooling-guild`,
`pretraining-foothills` get `spatial: false` (data/sources untouched);
`related_facts` on gpu-convnet-school (foothills) and on the continent YAML
(tooling-guild); chinese-state-response 2014→2015 with a note. `validate.py`
learned the three keys (V-01 strict keys) — files=10 fails=0.
`build_entities_json.py` emits `entities.json` + `entities.js` (JS global; the
page is static, loaded via `<script src>` — no fetch/CORS/file:// issue).

**Render.** Countries are traced on a FINE grid (rows Ca Cb S1a S1b S2a S2b S2c
as fractions of ROWY rows; cols = COLS ∪ {2009,2013,2015,2016}) with the same
loop-walk as `trace()`; a fine cell belongs to a country iff its year slot,
sub-band, AND `ownerAt(parentCol, parentRow) === parent_id` — containment by
construction. Country edges lying on continent grid lines are `polySlice`s of
the continent's own `edgePts` polylines, so outer edges coincide with the coast
exactly; country-only seams get a ≤6 px wobble. ROWY/BANDS/GRID/ENV/COLS
untouched; continent `d` strings unchanged. A2: click continent → `#map.zoomed`,
`#klabels`/`#kleaders`, dashed province lines; Esc or sea click → A1. Hover
cards: country (name/sub/span/sub-band/biome/neighbours/summary + facts),
continent card gains the tooling-guild fact.

**Gates (real output).** `countryContainment (0)`, `countryOverlap (0)` —
8 bbox-intersecting pairs × 500 seeded interior samples; `zoomInconsistent (0)`;
`countryLabelOverlaps (0)`; all prior gates still 0; `RESULT: PASS`.
Mutation check: forcing deep-rl-delta onto S2a → `countryOverlap (1)
[deep-rl-delta × gpu-convnet-school, 108 samples]`, so the gate bites.

**Honest A2 assessment.** Partition is correct and provably tiled, but lanes
are thin (~40–60 px tall at the plate scale): 5/7 labels fall back to
name+years with a leader; only industrial-lab-founders and deep-rl-delta
carry inside labels. The uncovered 2006–2011 western lobe reads as
"unlabelled forest" — by design (foothills demoted), but a reviewer may want
a faint "precursors" annotation there. Province dashes are visible but subtle
against the tree texture.

## Session 6 — 2026-09-12 — Leaflet tile re-platform, milestone 1 (continents)

**Ask.** Alan: "replace this with a tiling system" — real Google-Maps-style
pinch/scroll/drag zoom, not the A1/A2 class toggle. Milestone 1 = continents
only; milestone 2 (next session) = port the P3-RENDER country layer.

**Architecture (shipped).**
- `site/atlas.html` = the old `index.html` (git mv; v11 art + P3-RENDER v2
  country layer untouched). Added: `?tilesrc=1` → CSS class `html.tilesrc`
  that strips page chrome, continent labels/leaders and the country layer and
  pins the SVG at 1800×700 CSS px (1 px per viewBox unit); and
  `window.exportLabels()` → placed label lines (x, y, size, class, text,
  bbox), leaders, dots and land `d` strings in plate units.
- `site/build_tiles.py` (Playwright + Pillow): screenshot atlas.html?tilesrc=1
  at device_scale_factor 8 (clip 1800×700 → 14400×5600 px; a locator
  screenshot timed out, page.screenshot with clip works), LANCZOS downsample
  per level, slice 256 px XYZ tiles z0–z3 → `site/tiles/` (+ `meta.json`),
  write `site/labels.json`. ~4.5 min. 1687 tiles / 62 MB committed.
- `site/index.html` (new, Leaflet 1.9.4 from unpkg, no build): `L.CRS.Simple`,
  latlng = [-y, x] plate units, `L.tileLayer('tiles/{z}/{x}/{y}.png')`
  minZoom −1 / maxZoom 3 (= maxNativeZoom; upscaling disabled on purpose),
  zoomSnap .25, fitBounds on load, maxBounds pad .25. Overlays: an
  `L.svgOverlay` with the land paths (hover cards), leaders, dots; one
  `L.marker` + divIcon per continent label block at its bbox centre, font
  sizes = atlas sizes × 2^min(zoom,1). A `z-country` class toggles on the map
  container at zoom ≥ 1.5 — the hook for milestone 2's country fade-in.
- `site/verify_leaflet.py`: initial → 6 wheel ticks → 20-step drag →
  maxZoom → z2 on the Basin; asserts zoom rose, centre moved, all tile
  responses 200, no JS errors; writes 5 screenshots.
- `site/check_layout.py` default URL → `/atlas.html` (its gates are about the
  SVG renderer and still pass there).

**Problems hit / fixed.** (1) Tiles did not render at all at first: with
`minZoom: -1` on the map but not on the tile layer, Leaflet's `_isValidZoom`
rejected the fitted zoom −0.5 → added minZoom/maxZoom to the layer options.
(2) At zoom 3.5 (tiles upscaled 1.4×) vision review found blur and 1 px
hairline gaps; also at native z2 a measured column-brightness spike of ~100/255
every 256 px. Root cause: Leaflet sets tile `width/height` via style and
Chromium's transformed tile container left sub-pixel gaps; `img { width:256px
!important; height:256px !important; outline:1px solid transparent }` +
`will-change: transform` on the container took the spike to ≤ 7 at integer
zooms and ≤ 6 at fractional zooms (measured, not eyeballed); a 256.5 px
overlap made it worse. maxZoom capped at 3 so nothing is upscaled.

**Verification (live).** Pages run 34703636937 green; live `Last-Modified:
Sat, 12 Sep 2026 15:54:52 GMT`; page contains `LEAFLET v1`; verify_leaflet.py
against the live URL: PASS (zoom −0.5 → 3.0, centre moved, 192/192 tiles 200,
0 JS errors). Vision review of the live-equivalent screenshots: labels on
their landmasses, offset labels (Isles / Shore / Plateau) keep their leaders,
strokes crisp at z2/z3, no seams.

**Honest quality note vs. the v11 SVG.** The SVG was resolution-independent;
the pyramid is crisp up to z3 (8× the old 1:1 view), which is already past
the resolution of the 512 px texture JPGs, so there is nothing to gain from
z4 except repo weight. Between integer levels the browser downsamples
(slightly softer than a native level; no seams). The label overlay is HTML
text so it is always crisp; it does not (yet) re-fit when zoomed, it just
scales up to 2× and then holds.

**Next session (milestone 2).** Port the country layer: export country `d`
strings (fineTrace) + A2 label placement from atlas.html into
`labels.json`/`countries.json`, draw them as an `L.svgOverlay` (or a second
tile set for the biome provinces, since G4 country textures are raster),
show/hide with the `z-country` threshold (continuous zoom = A1→A2), keep the
containment/overlap gates running against atlas.html (geometry is identical by
construction since the overlay reuses the same `d`). Then decide whether
atlas.html stays as the authoring/gate renderer or is folded away.

## Session 7 — 2026-09-12 — real level-of-detail (Alan: "I zoomed in and the tiles didn't change")

- **Diagnosis confirmed from code, not guessed:** `build_tiles.py` v1 = one 8× screenshot, z0–z2 LANCZOS-downsampled
  from it. Same content at every level ⇒ zoom only rescaled. (Above z3 Leaflet upscales, which reads as "no change" too.)
- **Fix shape:** per-level renders. `atlas.html` got `?tilesrc=1&lod=0..3` as CSS toggles only (`html.tilesrc.lodN`
  rules on `.texbleed/.land/.tint`, `#labels .csub`, `#countries`, `.kzoom`, `#klabels/.ksub`, `#kleaders`) — zero new
  drawing code. `build_tiles.py` now screenshots lod=z at scale 2^z and slices only level z. Verified the four lod
  screenshots by vision BEFORE touching the tile builder (commit e76915c), then rebuilt (115d688).
- **One design bug found and fixed on the way:** at lod2/3 the continent's own huge name ("...BASIN") collided with the
  country label "The AlphaGo Delta". Now a continent with spatial countries hides its own label + leader at lod2/3
  (`.haskids`, same rule A2 already used). First attempt marked the class inside `drawCountries` but `relayout()` re-creates
  inside labels after fonts load and dropped it; the mark is now a helper called after both — verified via computed
  `display:none` on the two Basin label lines at lod2, `block` at lod1.
- **Gates:** `check_lod.py` (new; ink growth per level, adjacent-level Δ vs resample floor, flat-vs-textured, bytes per
  plate area — all measured on the SHIPPED tiles, not the source screenshots) PASS; `check_layout.py` PASS;
  `verify_leaflet.py` updated (labels no longer DOM) and PASS, now proving the level directory Leaflet loads from
  changes with zoom ({0:24} → {3:50} → {2:28}).
- **index.html:** DOM label overlay removed (labels are in the raster per level), hover hit-paths kept, HUD shows the
  level whose tiles are on screen, banner links the audit page. `static-map.html` audit page added (query params; GH
  Pages has no routing). Live confirmed 22:22:43 GMT.
- **Process note:** kept to the brief — small patches, 5 commits, each verified before the next; no new continents'
  country data, no city layer, no style redesign. Remaining softness: fractional zooms between native levels are still
  browser-resampled from the nearest level (that is normal slippy-map behaviour, not the reported bug).

## Session 8 — 2026-09-12 — LOD PILOT: every zoom step adds information (Deep Learning Basin only)

**Trigger (Alan, two messages):** "the details are not detail-y enough … more and more and more detail at every
step, not just a different texture"; then the correction: don't add a deeper tier, "each of those steps needs to
have a significant increase in the amount of information presented for the same region … four levels, five,
maybe six." Scope confirmed: pilot on the Deep Learning Basin only.

**Diagnosis of v2 (session 7) with a real measurement** (`check_lod_labels.py --site <HEAD~2 archive>`): text items
/ chars visible inside the Basin per level were 5/39 → 4/64 → 15/184 → 22/247 — z0→z1 lost an item, z2→z3 added
seven subtitle lines. The session-7 gate (ink fraction after downsampling everything to z0 size) could not see
this: small type averages away, so it read +0.0016 for z2→z3 and still passed.

**Design (5 levels).** z0 unchanged · z1 + 4 landmark hints per sub-region · z2 + one-line "what happened here"
tag + years per country (subtitle moves to z3) · z3 + 17 headline events as labelled dots at X(year) inside the
country's lane · z4 (basin bbox only) + all 32 placeable events + a sourced one-line fact under each headline
event. Five not four because 40+ events at z3 sizes collide; not six because the sourcing (research/06) does not
support another tier without padding.

**Data.** `data/events/deep-learning-basin.yaml`: hints, tags, 50 events (id, name, year, lod, one_line ≤15
words, sources[url]) for the 7 spatial countries; `build_entities_json.py` merges them into entities.json.
Mechanical check: all 50 events' URLs appear verbatim in research/06 or a country YAML `sources:` — 0 unsourced.

**Render (`atlas.html`).** New layers `#khints` / `#kevents3` / `#kevents4`, CSS-toggled per `?lod=`; positions
derived (x = X(year), y = lane centre off the country label's rows); placement = the country-label idiom (offset
search → reject boxes hitting placed boxes → leader when displaced → curate out if nothing fits, strict pass
"inside own country" then "centre inside own country + inside the continent"). Bugs on the way: `union()` returns
{x,y,r,b} not a bbox (NaN boxes → everything curated); event dots landing outside a concave lane (fixed: walk to
the nearest interior y, gate checks isPointInFill); Chromium hints sub-3 px glyph advances even at DPR 16 → bunched
letters in z4 tiles — fixed with `text-rendering: geometricPrecision` in tilesrc mode (the scale-group trick did NOT
fix it), verified on a 16× crop.

**Tiles (`build_tiles.py`).** z4 = 16 px/unit, rendered ONLY for the pilot bbox (768,304)–(1216,624) in tile-row
strips (28800×11200 for the whole plate would be ~5000 more tiles and a memory problem); `meta.full_zmax` /
`meta.pilot_bbox`; `index.html` mounts z4 as a second bounded tile layer, base layer upsamples z3 elsewhere.

**Gates.** `check_lod_labels.py` (new): per level, 0 text-on-text overlaps, event dots inside own country, event
text on the plate, and basin items+chars strictly growing per step — PASS (5/39 → 8/152 → 33/429 → 67/662 →
144/1880; 17 and 32 event marks). `check_lod.py` reworked to ink MASS at native resolution (dark px ÷ 2^z ÷ area),
min gain per step — PASS (20 → 49 → 195 → 439 → 919; before 20 → 47 → 162 → 355). `check_layout.py`,
`check_url.py` PASS. Curated out (hover-card only): 6 at z3, 18 at z4 — mostly the 2014 cluster and the narrow
Eastern Coast Forts lane; listed in `docs/screens/check_lod_labels_after.txt`.

**Not done / next (separate task, not started):** rollout to the other ~9 continents needs their own sourced event
files; hover cards for events in index.html (data is in entities.json); the 2014 cluster could use a wider lane
or a z5 if Alan wants those 18 on the raster.

## Session 9 — 2026-09-13 — LOD pilot fixes (Alan: "text is crazy big … should have resized"; "I don't understand the red lines")

Two mechanical fixes to site/atlas.html, done directly (no dispatch — both were pre-diagnosed).

**Fix 1 — text growing with zoom.** Root cause: build_tiles.py renders lod z at device scale 2**z and every
font-size was a plate-unit constant, so screen px = plate × 2**z grew per level (kname 48 → 96 → 192 px at
lod2/3/4; kev-name 42.7 → 48 px lod3 → lod4). Fix: `TILESRC`, `LOD`, `ZSCALE = 2**LOD`, `PX(px, plate)` at the top
of the script; `plate_fs = target_px / ZSCALE` in tilesrc mode, legacy plate constants otherwise (interactive
page untouched). Targets: kname 34, ktag/ksub/kyrs 28 (lod2–4; the fit-tier ladder scaled by CK = (34/ZSCALE)/10.2,
line gap 4 px); khint 16 (lod1 — swept 28/24/22/20/18/16/14: 28–22 placed 0 hints, 20/18 placed 1, 16 places both,
so 16); kev-name 30/26, kev-year 22/19 (lod3/lod4), kev-line 19. Pitfall hit: `const TILE` already exists (texture
repeat) — renamed to TILESRC after "Identifier already declared" broke the page (check_lod_labels timed out).
Measured after (site/measure_lod_text.py, new): kname 40/40/48, ktag 36/36/48, kev-name 40.0 → 34.3 (AlexNet, same
text at lod3/lod4: −14 %, was +12 % and ×2 per level for country text), kev-year 26.7 → 22.9, kev-line 22.9.
Side effect: smaller z4 text fits 47 of the 50 events (was 32); z3 places 20 headline events (was 17).

**Fix 2 — red leaders.** `.kev-leader` #7a2414 (dot red) → country-leader brown #3d2e1a, .45 hairline, opacity .7,
solid. The task's suggested dashed variant (1.2 1) was tried first and rejected on the z4 crop: at lod4 the .kzoom
province line and .cborder.road are already dashed brown, and the reviewer could not tell the GLOVE leader from the
route lines ("same dashed stroke … near-identical width"). Solid hairline reviewed as "clearly a different class of
line … thin, unbroken, lighter". Evidence: docs/screens/lod4-leaders-after.png.

Gates: check_lod.py PASS (ink mass z0→z4 20.0 → 49.7 → 171.6 → 322.4 → 569.1, all steps gain); check_lod_labels.py
PASS (0 overlaps, 0 dots outside, 0 off-plate at every level; lod1 hints 2/2 placed). Tiles rebuilt twice (fix 1,
fix 2), ~8.5 min each. Screens: docs/screens/lod2-{0..4}.png, lod-tiles-same-region.png.
