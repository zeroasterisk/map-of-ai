# ORCHESTRATOR LOG — Map of AI (recovery/continuity notes)

> Written by the orchestrating Hermes session (not Fable) to preserve project
> state across a context compaction. If you're Fable picking up work, or a
> future orchestrator session, START HERE alongside STATUS.md.

## Current iteration status (as of this write)

- **Live:** https://zeroasterisk.github.io/map-of-ai/
- **HEAD at write time:** session 14 (tile pyramid rebuilt z0–z4 with two z4 pilot regions — Deep Learning Basin + Generative Coast; Policy Coast z3 tuning; multi-bbox `pilot_bboxes` in build_tiles.py/index.html) on main
- **Active Cron Watchdog:** `map-of-ai-rework-trigger` (every 3h, idle > 30m guard via `/home/node/agent/scripts/map_of_ai_watchdog.py`)
- **Gates:** `validate.py` files=19 rules=25 fails=0; `check_lod_labels.py` PASS (lod3 21 marks / lod4 48 marks + 75 one-line rows in the sampled region; 5 events curated out, down from 14); `check_layout.py` all structural, country & thread gates 0 (clipped 625 — all event text boxes at plate x > 2746, the same pre-existing class; +23 from the newly-placed Policy Coast events).
- **Tiles:** z0 40 / z1 135 / z2 493 / z3 1881 / z4 1594 (basin 560 + coast 1034) = 4143 tiles, 119 MB. `meta.json` carries `pilot_bboxes` (list) plus `pilot_bbox` (first region, back-compat); `counts["4"].regions` has per-region tile/col/row counts.

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

## Session 10 — 2026-09-13 — Generative Coast → 8 countries (density stress-test, PHASE 1: data layer only)

Alan: "the map looks sparse to me … We can try the most current timeframe and see what dense looks like." Task
scoped to data + wiring; tiles/events/hints are Phase 2.

**Coverage decision** (`data/coverage/generative-coast.md`, P3-T10): research/08's `## Schools of thought` has exactly
8 bullets (awk count 8 = Table 1 rows, A-M2); each becomes a country, none merged/dropped, 8 < SPEC §4.3 cap 9. Ids +
names: `closed-frontier-labs` The Closed Frontier · `open-weights-movement` The Open-Weights Commons ·
`diffusion-media-district` The Diffusion Shoreline · `reasoning-test-time-compute` Reasoning Ridge ·
`agents-tooling-coast` The Agents Causeway · `alignment-interpretability-plateau` The Alignment Plateau ·
`policy-governance-coast` The Policy Coast · `compute-hardware-hinterland` The Compute Hinterland. Research/08's own
"Map notes" suggested A2 labels by institution; Table 1 follows the school bullets per A-K2 (institutions → P4 cities).

**Placement** (one lane each, N→S, so the full-height coast is a 9-row stack): N1a policy · N1b alignment · N2b
reasoning (2024–) · Ca closed labs · Cb open weights (2023–) · S1a+S1b agents · S2a+S2b diffusion · S2c compute.
Biomes: jungle (parent) for the three model districts; wetland reasoning (RL), mixed agents + alignment, highland
policy (hand-authored rules), harbour compute. Two deliberate A-K7 calls recorded in the coverage notes: compute drawn
as territory although AXES.md says "hardware → roads" (tooling-guild was demoted in the basin) so all 8 land on the
raster for the density test; policy highland vs grassland.

**P2-T10 written in-session** (`data/continents/generative-coast.yaml`): validate.py V-30 rejects a country whose
parent file doesn't exist, so the continent yaml was authored from research/08's summary + Sources (not in the task
brief, unavoidable).

**Sourcing proof:** script check — all 59 country urls + 8 continent urls are exact substrings of research/08; all
research_ref ints ∈ its [1]–[120]; summary word counts 163–209 (country range 80–220). Grep spot-checks of 20 dated
facts all hit (two first "misses" — Midjourney "12 Jul", "$4T" — were my grep patterns, the facts are in rows 15/48).
`scripts/validate.py` (with V-20 live links) → files=19 rules=25 fails=0.

**Step 3 mechanics (the hidden part):** there is NO cell-assignment file. `site/atlas.html` derives country polygons
from `time_range` × `sub_band` × parent ownership (`fineCell`) over a fine grid `FINE` (rows) × `SUBCOLS` (years).
Three gaps, all fixed in atlas.html: (1) `FINE` only had C/S1/S2 rows → added N1a/N1b/N2a/N2b (each = one continent
row, f 0–1); (2) `SUBCOLS` lacked 2023/2024 → added; (3) `fineCell` compared `SUBCOLS[i+1] <= k.end` with the string
'present' → `kEnd(k)` maps 'present' → E (present-day coast). `build_entities_json.py` + `validate.py` SUB_BANDS enum
extended with N1a–N2b. Build → `entities.json` 17 countries (15 spatial). No basin data/tiles touched; basin's 7
polygons unchanged (check_layout containment/overlap still pass for them).

**Verification:** `check_layout.py` N_COUNTRIES 7→15; country gates all PASS (count 15, containment 300/300 ×15,
zero-overlap 0 pairs, label overlaps 0, outside 0, A2 zoom consistent, A1 country labels hidden). Overall RESULT FAIL
is the pre-existing `clipped` gate (A1 event labels at viewBox edge): 179 at baseline via `git stash`, 160 now.
Screenshot `docs/screens/generative-coast-a2.png` (new `site/probe_continent_countries.py generative-coast`, serves
site/ over localhost — file:// fails on the registry.json fetch): A2 view of the coast shows 8 stacked provinces with
distinct fills (tan hachured policy strip on top, purple alignment, blue-hachured reasoning wedge on the east coast,
dark forest closed frontier, thin teal open-weights band, broad purple agents block, olive stippled diffusion
shoreline, tan compute foot) each with name + years label inside its polygon; Open-Weights Commons label is tight
vertically (single Cb lane) — a Phase 2 label-fit note, not a gate failure. `site/probe_countries.py` times out at
baseline too (pre-existing).

Commits: 7b0c1fa coverage · 0f5a39a continent + 8 countries · 0654d92 wiring + screenshot · (this) STATUS/LOG.

## Session 11 — 2026-09-13 — Y-funnel geometry + the Silicon Range (branch `axis-recalibration-y-height-hardware-range`)

Task (Alan, pilot on deep-learning-basin + generative-coast; geometry only, no data/fact edits): (1) make the Y
(height) dimension grow non-linearly toward the present the way the X axis already does (AXES.md §1 SEG), without
redrawing pre-2025 content; (2) draw hardware/compute (AXES.md §3 linear thread, research/09 thread (d)) as a
MOUNTAIN RANGE, not a country, from research/09's sourced [d1]–[d12] milestones only.

Part 1 — Y-FUNNEL v12 (commit b80154d). YSEG = [[2017,1],[2022,1.1],[2024,1.3],[2025.2,1.6],[PRESENT,2.0]],
piecewise-linear `yScale(yr)`. Rationale: 2017 anchor = start of SEG's 6×/yr segment and the last era that must stay
pixel-identical; 1.1 for the Plateau ("a bit more breathing room"); 2× at the east edge (low end of the 2–2.5× ask,
because the ±46 px spine shear also needs canvas) with the steep part after 2024 (1.3 → 2.0), mirroring SEG's 3× → 6×.
First attempt made `bandH`/`bandTop` functions of year and moved MAP_TOP; abandoned after the gate showed the spine
envelope + ocean labels drifting (`outside` 2, `envelopeViol` 1, `smallFonts` 4) — because warp()'s noise is sampled in
plate coordinates, moving the 1× frame changes every pre-2017 wobble. Final design keeps the 1× authoring frame at the
v11 150–560 and applies the funnel as ONE transform `FY(x,py) = Y_OFF + MAP_MID + (py − MAP_MID)·yScale(yearAt(x))`
inside `SY()`; `plateY()` is its inverse and check_layout.py's band gates use it. Plate 1800×700 → 1800×1050.
Measured (probe): Basin land bbox height 288 → 288; Generative Coast 474 → 819. Gate after Part 1: everything PASS
except pre-existing `clipped` (160 → 162, A1 event labels). Shots: docs/shots/y-funnel-{before,after}-A2.png,
y-funnel-after-A1.png. Vision check of after-A2: 8 coast provinces intact, labels legible, no overlaps.

Part 2 — THE SILICON RANGE (this commit). Pre-check: `river|road|thread` in atlas.html/data → nothing rendered; this
is the first thread primitive. New `data/threads/silicon-river-hardware.yaml` (kind: mountain-range, placement band
[S1,S2] bank 0.5 = the connectionist/scaling bank per research/09 (d), time_range 1999–present) with 10 milestones,
each `sources[]` url copied verbatim from research/09's [d1]–[d12]: GeForce 256 1999 [d3]; CUDA 2007 [d4]; AlexNet on
GPUs 2012 [d5]; TPU + DGX-1 2016 [d6]; Volta V100 2017 [d11]; Cerebras WSE-1 2019 [d11]; Scaling laws 2020 [d7][d12];
Hopper H100 2022 [d8]; Export controls/CHIPS 2022 [d10]; Blackwell 2024 [d9]. Lisp machines [d1] + Connection Machine
[d2] recorded as `not_yet_drawn` (symbolic bank, west of the pilots). `build_entities_json.py` passes
`data/threads/*.yaml` through as `threads` and refuses a milestone with no sources. Render: `drawThreads()` — ridge
spine at the S1/S2 seam through SY() (so it follows funnel + spine), continuous relief silhouette (minor chain +
smoothstep summits ∝ `peak` × local band height), south-face wash + shadow + hachures, heavier ink summit outlines
with dots, hover card listing every milestone with its [dN] refs. Labels reuse the country/event idiom (offset search,
`union`, `fitsInside(coast)`, placed-box hit test; lod 2 curated out when nothing fits, lod 1 gets a leader). Two
iterations after vision review: (1) first pass looked like "peaks stuck on a grey road" and GeForce sat detached →
added the continuous minor-peak chain and made the face opaque; (2) "The Deep Learning Basin" label sat on the
AlexNet peak → the range's skyline is now registered as `window.THREAD_OBSTACLES` before `relayout()` and
`placeInside` rejects anchors touching it (constraint by construction), `deep-learning-basin` got `alt` anchors north
of the ridge, and milestone labels may also go south of the foot line. New gates in check_layout.py: threadCount,
threadLabelsVisible (≥ 4), threadLabelOverlaps (vs continent labels + each other), threadLabelOutside (coast).
Final gate: threads 1 drawn, 10 peaks, 10 labelled, 0 curated, 0/0 overlaps/outside; all other gates as after Part 1;
RESULT FAIL only on the pre-existing `clipped` 162. Shot: docs/shots/silicon-range-A1.png (vision: continuous ridge
CUDA → coast with foothills to GeForce; no label collisions; all 10 milestone labels + SILICON RANGE readable).

Jalapeño chip: requested; at build time `grep -ri jalape research/ data/ site/ AXES.md` = 0 hits → NOT added, no
citation invented. Commit 6612451 (Alan via Hermes, between the two session commits) then added it to research/09 (d)
as [d13] (OpenAI announcement 25 Aug 2026, Wayback snapshot); only then was it added as the 11th milestone
(year 2026.65, lod 1). Because X(2026.65) is the east coast, `MX()` clamps a summit west by half a peak width so the
peak stays on land (vision check before the clamp: "slightly spills over the shore line"; after: bbox back to 879 px
wide, on land). Final gate: 11 peaks, 11 labelled, 0 curated, 0 overlaps/outside; RESULT FAIL only on `clipped` 162.
Source-quality caveat recorded in STATUS: [d13] is a vendor announcement, weaker than [d1]–[d12].

Out of scope (flagged): tile pyramid rebuild (`build_tiles.py` PLATE still (1800, 700); threads not in labels.json)
— do after this geometry is confirmed. Tooling note: the two band-gate helpers in check_layout.py now go through
`SY()`/`plateY()` instead of `± spineY(x)`; any future plate transform must be added in those two functions only.

## Session 14 (2026-09-16) — tile pyramid rebuilt for the Generative Coast; second z4 pilot region; Policy Coast z3 tuning

**Why.** Session 13 added 105 Generative Coast events + Redwood but never reran `build_tiles.py`, so the Leaflet viewer
kept serving session-12 tiles; and `PILOT_BBOX` covered only the Deep Learning Basin, so even a rebuild would have left
the coast's new z4 event layer (one-line facts) invisible at zoom 4.

**Part 1 — Policy Coast (`data/events/generative-coast.yaml`).** Root cause of the z3 curation was geometric, not
density: the country's `time_range` opens in 2023 but its land polygon (a diagonal wedge on the N1a coast) only widens
around 2024, so every 2023-dated event clamped to the bbox edge landed on a lane too thin for its dot. Two fixes:
(a) data — `pause-letter-2023`, `eo14110-2023`, `nyt-openai-2023` demoted lod 3 → 4 (Bletchley 2023.84 and EU AI Act
2024.2 stay the lod 3 headlines); (b) render — `atlas.html` event placement now builds a short candidate list per
event: its own year first, then columns sliding inward by ≤ 40 plate units (~0.8 yr, nearest first) whose lane is at
least one label block tall and not already taken; the first candidate where the label also fits wins. Events that fit
at their own year never move. `ubox()` hoisted to a shared helper (takes KS). Result: z3 Policy Coast shows Bletchley +
EU AI Act inline; z4 shows all 10 (was 4). Sampled-region curated list fell 14 → 5 (`white-house-2016`,
`export-controls-2022` at z3; `ntm-2014`, `show-and-tell-2014`, `hinton-leaves-2023` at z4).

**Part 2 — multi-bbox z4 (`build_tiles.py`, `index.html`).** `PILOT_BBOXES = {deep-learning-basin: (768,304,1216,624),
generative-coast: (1280,128,1632,880)}` (both multiples of 16 = one z4 tile); `PILOT_BBOX` kept as the first entry for
back-compat. `--pilot-bbox` is now repeatable (`action=append`); default = every entry. For z > full_zmax each bbox is
captured in strips and sliced into the same `tiles/4/` tree (disjoint x ranges, no collisions). `meta.json`: `pilot_bbox`
(first) + `pilot_bboxes` (list); `counts["4"]` = totals + `regions[]`. `index.html` mounts one bounded `L.tileLayer`
per entry of `meta.pilot_bboxes || [meta.pilot_bbox]`. The coast bbox's east edge 1632 sits 21 units past the coast's land bbox (x ≤ 1611) for leader lines, well inside the 1800-wide plate.

**Part 3 — rebuild.** `build_tiles.py` (default args): z0 40, z1 135, z2 493, z3 1881, z4 1594 (basin 560 = 28×20,
coast 1034 = 22×47) → 4143 tiles / 119 MB (was 3069 / 94 MB). `labels.json` regenerated; `build_anchors.py` → 25
anchors, unchanged coordinates (geometry did not move).

**Part 4 — gates.** `validate.py` files=19 rules=25 fails=0. `check_layout.py` all structural/country/containment/
overlap/thread gates 0; `clipped` 625 (was 602), script-checked: min x 2746, all > plate width — the pre-existing A1
event-box class, +23 from the Policy Coast events that now place. `check_lod_labels.py` LOD LABEL GATE: PASS. Leaflet
(Playwright, `?place=generative-coast`): all requested tiles loaded, 0 HTTP ≥ 400, both z4 layers serve
(`layers: [0–3], [4,4], [4,4]`). Shots in docs/screens/: `leaflet-s14-generative-coast-z2.5.png` (Closed Frontier /
Open-Weights Commons names + tags + z3 event dots), `leaflet-s14-generative-coast-policy-z4.png` (Bletchley + EU AI Act
with one-line facts, EO 14110, Getty, Pause letter), `-frontier-z4`, `-agents-z4`, `-deep-learning-basin-z4`.

**Known / next.** (1) z4 text is soft — tiles are rastered at DPR 16 from ~3 px glyphs; crispness needs an SVG overlay
or larger per-event fonts at lod 4 — unchanged from session 12. (2) A vision pass flagged one z4 marker sitting on the
GPT-4o fact line in the Closed Frontier; the gate's box test passes (dot vs text box), so it is a gap ≤ 1 unit, not an
overlap — worth a `S.gap` bump for lod 4 later. (3) `clipped` still non-zero by design (A1 event boxes east of plate).

## Session 15 (2026-09-16) — staged-candidate promotion (research/08 + /09), lod-4 `S.gap` .6 → 1.0, z4 tiles rebuilt

**Why.** Two items had been sitting in STATUS since sessions 13–14: the innermost-loop staging file
(`data/staging/innermost-loop-candidates.md`) kept accumulating sourced 2026 events that the curated corpus did not
carry, and the lod-4 event placer's `S.gap` was flagged as too tight after a vision pass saw a z4 dot on a fact line.

**Part 1 — promotions.** Seven landmark items → 12 staging rows ticked. research/08 timeline +3 rows: *13–16 Aug 2026*
open-weights week (DeepSeek Harness v0.1 MIT + V4-Pro API; Alibaba Qwen3.8-27B + 2.4T Max under Apache 2.0; Qwen passes
3 B downloads, ahead of Meta and Google — [126] [127]); *3–8 Sep* AI-for-biology (Google + HHMI Janelia complete the
male fruit-fly connectome, ~166 k neurons; DeepMind AlphaGenome Atlas scores all ~9 B human point mutations — [128]
[129]); *6–11 Sep* governance realignment (Christiano to the OpenAI Foundation board; Pachocki's "An Alien Mind";
Altman tells staff OpenAI is open to slowing — [130]); Key people +Pachocki and Christiano. research/09: Conscience Road
+Anthropic multi-agent swarm red-team study, 13 Aug ([c15]); Silicon River +Cerebras CS-4 + $20 B OpenAI pact, 12–19
Aug ([d15]); both descriptions extended. Rows sit in date order (CS-4 placed before Jalapeño, 25 Aug).

**Sourcing.** Every URL fetched before citing. Live-fetchable: deepmind.google, research.google, anthropic.com, the
Simon Willison post, the two X posts (via the syndication endpoint; snowflake ids decode to 14 Aug / 9 Sep). Bot-blocked
and verified another way, then allowlisted with the method noted: openai.com ×2 (RSS feed 200 + Wayback), venturebeat
(Wayback 20260830), globenewswire (Wayback 20260827; live host drops non-browser TLS), bloomberg ×2 (reader proxy for
headline + date), reuters (ET Telecom syndication in Google News for headline + date). `check_research.py` R-05 crashed
with `int('d13')` on any thread-prefixed source id — it had never actually run to completion on research/09 since
session 12 added `[d13]`; fixed (ids kept as strings). That surfaced `[d13]` as R-03 + R-05 red (openai.com 403, no
`(accessed YYYY-MM-DD)`); normalised its wording and allowlisted it. Both files R-01…R-07 PASS.

**Part 2 — `S.gap`.** The session 14 note named GPT-4o, but a probe (dot → nearest *foreign* event text or country
label, user space, at `?tilesrc=1&lod=4`, 1800×1050) shows GPT-4o's own dot and the nearest other dot both ≥ 4.9 units
from its text — not reproducible at this viewport. The same probe found the real offenders at gap .6: 3 dots under 1
unit (`inflection-ssi-2024` −0.25 into the *Claude 3.5 Sonnet* name; `pixelrnn-2016` 0.4 from WaveNet's line;
`eo14110-2023` 0.79 from *Bletchley Declaration*), 12 under 2. Tried .8 and 1.0: both give 0 under 1; 1.0 leaves 8
under 2 (min 1.29) and is what shipped. Cost at either value: `vector-2017` joins the sampled-region curated list
(lod4 47 marks, was 48; lod3 unchanged at 21). `gap` .6 → 1.0 for `ev4` only; `ev3` stays 1.2.

**Part 3 — tiles.** `S.gap` only changes the z4 layer, which is baked into `site/tiles/4/` — the session 14 lesson —
so `build_tiles.py` (default args) was rerun: z0 40 / z1 135 / z2 493 / z3 1881 / z4 1594 = 4143, same counts.

**Part 4 — gates.** `validate.py` files=19 rules=25 fails=0 (run under `/tmp/pwvenv/bin/python`; system python3 has no
PyYAML). `check_layout.py`: all structural / country / containment / zero-overlap / thread gates 0; `clipped` 625,
same class and count as session 14. `check_lod_labels.py` LOD LABEL GATE: PASS; `docs/screens/lod_labels_summary.json`
refreshed.

**Known / next.** (1) z4 softness unchanged (SVG overlay still the fix). (2) 212 staging rows remain unticked; chip /
compute (~45) and OpenAI / Anthropic lab events (~39 each) are the densest clusters. (3) `clipped` non-zero by design.

## Session 16 (2026-09-16) — frontier-lab reasoning + gigawatt-compute promotions (research/08 [131]–[135], research/09 [d16]–[d19])

**Why.** Session 15's STATUS named the two densest unpromoted clusters in `data/staging/innermost-loop-candidates.md`:
frontier reasoning / lab milestones (Lean FLT proof, Fable/Mythos 5.1 and the UK withholding, FrontierMath Erdős, the
OpenAI automated-researcher post) and gigawatt-scale compute (Terafab FEL, Broadcom/Anthropic 5 GW, SB Energy 8.8 GW,
Microsoft 38 GW). This session promotes exactly those nine, nothing else.

**Part 1 — promotions.** research/08 +5 timeline rows, all in the Sep 2026 column and slotted in date order around the
existing GPT-6 Astra (3 Sep), Navier–Stokes (8–11 Sep) and governance (6–11 Sep) rows: [131] Fable 5.1 / Mythos 5.1 (1
Sep), [132] FrontierMath Erdős (1 Sep), [133] FLT formalised (4 Sep), [134] "Research acceleration" (6 Sep), [135] FT on
Mythos 5.1 and the UK AISI (8 Sep). [135]'s significance cell cross-references [131] (the withheld tier is the
higher-safeguard half of the two-tier release). research/09 Thread (d) +4 rows: [d16] Terafab (6–16 Aug; placed before
Cerebras 12–19 Aug to keep the table chronological), [d17] SB Energy (1 Sep), [d18] Broadcom/Anthropic (2 Sep), [d19]
Microsoft (10 Sep); description tail now reads "[d1]–[d19]" and names the chips → gigawatts shift. No Key-people
additions — none of the nine introduces a person the file lacks.

**What the sources actually said vs the staging rows.** Dates: staging's ~3 Sep / ~3 Sep / ~6 Sep / ~7 Sep / ~12 Sep
became 1 / 1 / 4 / 6 / 8 Sep from the primary pages, the anthropic.com newsroom and research indexes, the OpenAI RSS
`pubDate` and the FT Wayback snapshot. Content: the FT piece (standfirst: "Decision to exclude Aisi for the first time
has prompted fears inside British government of wider protectionist shift among tech groups") is about pre-release
access for the UK AI Security Institute, not a market withdrawal — row and citation say so. Epoch's post gives 2/68
under the fixed protocol and 5/68 across looser additional attempts, and names the two protocol solves (problem 74
disproved, problem 126 proved); the row carries both numbers rather than the staging's bare "2 of 68". Broadcom's exact
wording (via CNBC) is "5 gigawatts of TPU 8i chips in 2027, with line of sight to deliver another 10 gigawatts" — the
"10 GW" is line-of-sight, not contracted, and the row keeps that distinction. The Terafab X thread is thin on its own
(Musk's whole post is "FEL FTW"), so [d16] pairs the two X posts with Bits&Chips (10 Aug) and TrendForce (12 Aug) for
the FEL-vs-LPP explanation; the $100 B / in-house-memory framing is attributed to the Innermost Loop digest, not to a
source that states it.

**Sourcing.** Each URL fetched before citing. Live 200: anthropic.com ×2, epoch.ai, cnbc.com, sbenergy.com,
bits-chips.com, trendforce.com; the two X posts via the fxtwitter status API (dates + text; @teslayoda's post is an
image post, no quoted tweet). Blocked → verified another way → allowlisted with the method in the comment: openai.com
(RSS feed lists the post with pubDate Sun 06 Sep 2026; Wayback 20260915050818 200), ft.com (Wayback 20260909043414
headline + standfirst; Google News RSS shows the FT item dated 8 Sep plus IT Pro / The Next Web / euractiv pickups),
bloomberg.com ×2 (reader proxy returns headline, `Published Time` and lede for both; the SB Energy lede links the live
sec.gov S-1, which is 200). `check_links.sh` before allowlisting failed on exactly those four and nothing else.
`check_research.py`: research/08 R-01…R-07 PASS (232 links, 0 failed, 15 allowlisted); research/09 first run FAIL R-05
on `[d16]` — I had put prose after the date inside the `(accessed …)` parenthesis, which the regex rightly rejects —
moved the note before the URL; rerun R-01…R-07 PASS (229 links, 0 failed, 9 allowlisted).

**Gates.** `validate.py` files=19 rules=25 fails=0. `check_layout.py` all structural / country / containment /
zero-overlap / thread gates 0; `clipped` 625 (same class + count as sessions 14–15; overall RESULT: FAIL is that gate
alone, as before). `check_lod_labels.py` LOD LABEL GATE: PASS (lod4 47 marks, 75 one-line rows, curated set unchanged).
Nothing under `site/` or `data/regions/` changed, so no tile rebuild.

**Commits.** One content commit (research/08, research/09, allowlist, staging ticks) followed by this STATUS +
ORCHESTRATOR_LOG commit; both pushed straight to `main` per the brief.

**Next.** The nine items are corpus-only; none is a map event yet. When the Generative Coast's event budget is next
opened, the Sep 2026 column wants at least the FLT proof and the two-tier release (both already have research/08 ids).
Remaining staging density: chip/compute (Nvidia, Groq-for-China, xAI) and OpenAI/Anthropic product cadence.

## Session 17 (2026-09-16) — frontier-lab product cadence + hardware-architecture promotions (research/08 [136]–[141], research/09 [d20]–[d23])

**Why.** Session 16's STATUS named the next two clusters in `data/staging/innermost-loop-candidates.md`: frontier-lab
product cadence / benchmarks / agent platforms (Daybreak + GPT-5.6-Cyber, GPT-5.6 Sol on ZeroBench and Crouzeix, Opus 5
+ Claude Code on ARC-AGI-3 and ProgramBench, Gemini 3.7 Flash + Spark, Grok 4.6, Cowork browser) and chip architecture
(Vera Rubin NVL72 first silicon, the Groq-for-China report, SpaceXAI's Vera CPU, Apple M6 / M5 Ultra). This session
promotes exactly those twelve staging rows (49, 54, 69, 70, 71, 73, 75, 108, 155, 172, 186, 190), nothing else.

**Part 1 — promotions.** research/08 +6 timeline rows, all in the Aug 2026 column and slotted in date order between the
OpenAI swarm row (May–Sep) and the existing 13–16 Aug open-weights / 14–27 Aug consolidation rows: [136] GPT-5.6 Sol
research-grade results — Crouzeix proof + ZeroBench 30% (27 Jul–15 Aug), [137] Daybreak Blue/Red + GPT-5.6-Cyber (10
Aug), [138] Opus 5 + Claude Code on ARC-AGI-3 and ProgramBench (11–13 Aug), [139] Grok 4.6 (12 Aug), [140] Gemini 3.7
Flash + Spark (13 Aug), [141] Cowork built-in browser (26 Aug). Two staging rows pair into one corpus row twice: the
two GPT-5.6 Sol research results share [136], and the ARC-AGI-3 + ProgramBench records share [138] — same model, same
week, same "harness is the variable" significance. Cross-references: [137] → [131] (Anthropic's two-tier release three
weeks later) and [122] (the RL-training pause); [138] → [121] (GPT-6 Astra saturating ARC-AGI-3); [139] → [124] (the
Cursor acquisition two days later); [141] → [15] (the Oct 2024 computer-use origin) and [122]. research/09 Thread (d) +4
rows: [d20] Vera Rubin NVL72 on CoreWeave (21 Jul, placed first in the 2026 block), [d21] The Information China chip
report + denial (20–21 Aug, *contested*), [d22] SpaceXAI adopts Vera CPU / Starmind (24 Aug), [d23] Apple M6 + M5 Ultra
(25 Aug, after the same-day Jalapeño row); description tail now "[d1]–[d23]" and names tokens-per-megawatt, the
agent-oriented CPU, the export-control detour and desktop open-weight inference. No Key-people additions.

**What the sources actually said vs the staging rows / brief.** Dates: staging's ~12 Aug (Daybreak), ~12–13 Aug
(ZeroBench, Crouzeix), ~13 Aug (Grok 4.6), ~27 Aug (Cowork), ~16 Aug (CoreWeave), ~21 Aug (Information), ~25 Aug
(SpaceXAI), ~27 Aug (Apple) became 10 Aug (OpenAI RSS pubDate), 7 Aug + 27 Jul–15 Aug, 12 Aug, 26 Aug, **21 Jul** (the
CoreWeave post's own byline — the digest carried it 26 days late; the citation records both), 20 Aug (datePublished
16:58Z), 24 Aug, 25 Aug. Content: (1) the brief said GPT-5.6 Sol "proves a counterexample to the Crouzeix conjecture" —
the SIAM News essay (Townsend & Greenbaum, checked with Michel Crouzeix) says the conjecture was *proved*, by Dr. Shanmu
Jin's preprint whose key theorem came from a ~16-hour autonomous run; the row says proof and cites the independent
Lorist–Schwenninger arXiv proof too. (2) Grok 4.6 "matching GPT-5.6 Sol Max across standard benchmarks" is xAI's own
table: AA Intelligence Index 61 vs 61, but Fable 5 Max 62 leads, and Grok wins CursorBench while losing DeepSWE — the
row says "matching … on the AA Index" and names the price. (3) The Information's headline is "Nvidia Plots China Comeback
With New AI Chip"; neither headline nor lede says Groq or LPU — that framing is the digest's and the pickups'
(Tom's Hardware, Yahoo Tech), and Nvidia denied it the same day via Reuters ("no China-specific LPU product in our
roadmap"). Row marked *contested*; citation attributes each claim. (4) Apple's newsroom page does not say "open-weight";
it says "running compute-intensive frontier AI models on device" and LLMs "with hundreds of billions" of parameters —
quoted, with the open-weight connection stated as Thread (e)'s interpretation. (5) The jerber/arc-code README is
explicit that this is an independent run, not ARC Prize-verified — confidence medium, said in the row.

**Sourcing.** Each URL fetched before citing. Live 200: alextownsend.net (PDF; pdfTeX CreationDate 2026-08-15; text
extracted with pypdf via `uv run --with pypdf`), github.com ×2, arcprize.org, arxiv.org, x.ai, blog.google, claude.com,
coreweave.com, nvidianews.nvidia.com, apple.com; the two X posts via the fxtwitter status API. Blocked → verified
another way → allowlisted with the method in the comment: openai.com (RSS title + pubDate Mon 10 Aug 2026; Wayback
20260914205743 200, body quoted), theinformation.com (200 to the checker today but the domain is intermittently 403 —
page metadata + Wayback 20260906103803; denial pickups via Google News RSS). preprints.org (Jin's manuscript) is 403 to
every UA tried and has no Wayback snapshot — cited as text in [136], with the author's public GitHub repo (200) linked in
its place. `check_research.py`: research/08 R-01…R-07 PASS (82 rows, 141 sources, 244 links 0 failed / 16 allowlisted);
research/09 R-01…R-07 PASS (16 rows, 109 sources, 234 links 0 failed / 9 allowlisted). Clean on first run.

**Gates.** `validate.py` files=19 rules=25 fails=0. `check_layout.py` all structural / country / containment /
zero-overlap / thread gates 0; `clipped` 625 — confirmed identical by running the gate against a `git stash` baseline in
the same session (overall RESULT: FAIL is that pre-existing gate alone, as in sessions 14–16). `check_lod_labels.py` LOD
LABEL GATE: PASS (lod4 47 marks, 75 one-line rows, curated set unchanged). Nothing under `site/` or `data/regions/`
changed, so no tile rebuild.

**Commits.** One content commit (research/08, research/09, allowlist, staging ticks) followed by this STATUS +
ORCHESTRATOR_LOG commit; both pushed straight to `main` per the brief.

**Next.** The twelve items are corpus-only; none is a map event yet. Candidates for the Generative Coast's Aug 2026
column when its budget is next opened: the Crouzeix proof and the ARC-AGI-3 harness result (both have research/08 ids);
Vera Rubin NVL72 for `compute-hardware-hinterland`. Staging: 190 unticked rows, no single cluster now above ~10 rows.

## Session 18 (2026-09-16) — multi-agent safety / cyber escalations + gigawatt-infrastructure promotions (research/08 [142]–[145], research/09 [c16]–[c18], [d24]–[d29])

**Why.** Session 17's STATUS left two dense clusters in `data/staging/innermost-loop-candidates.md`: the multi-agent
sandbox-escape / covert-dead-drop / cyber-safety escalation (Astra Critical-cyber disclosure, Black Hat briefing, the
Australian gym-API attack, Dwarkesh's account, Reuters' 10+ sites, Anthropic's four-incident assessment) and
gigawatt-scale power + AI-factory capital (SemiAnalysis on SpaceX 10 GW, Amazon's 7.65 GW gas plant, Nvidia's $500B
asset-class platforms, SK Hynix's $720B megasite, Nvidia's $105B for OpenAI's Ohio campus, Anthropic's $45B Nscale
lease). This session promotes exactly those twelve rows (20, 21, 32, 41, 45, 58, 77, 124, 192, 225, 294, 295).

**Part 1 — promotions.** research/08 +4 timeline rows, each slotted by date among the existing Aug/Sep 2026 rows: [142]
Black Hat sandbox walkthrough + Astra "cannot rule out Critical" pause (6–7 Aug, before the 8 Aug Alphabet row), [143]
Australia's autonomous gym-API attack (10 Aug, after the same-day Daybreak row), [144] Dwarkesh's "Rise and Fall of
Agent Civilizations" (29 Aug, before the 1 Sep rows), [145] Reuters dead-drop sites + Anthropic's alignment assessment
(9–10 Sep, closing the table after the 8 Sep FT row). Six staging rows pair into four corpus rows: the Black Hat talk
and the next-day Astra post share [142] (same disclosure week, same incident), and Reuters + Anthropic share [145]
(same 48 hours, same "sandbox to real systems" significance at both labs). Cross-references: every row → [122] (the
swarm postmortem); [142] → [137] (Daybreak Red) and [121] (GPT-6 Astra's Critical designation on release). research/09
Thread (c) +3 rows after the 13 Aug multiagent-study row: [c16] (6–10 Aug: Black Hat + Astra + Australia), [c17]
(29 Aug: Dwarkesh), [c18] (9–10 Sep: Reuters + Anthropic) — the thread's first rows in which *both* frontier labs have
incident logs, and METR audits both. Thread (d) +4 rows: [d24] [d25] [d26] grouped as one 7–10 Aug "gigawatt turn
becomes an asset class" row (SemiAnalysis, NYT/Amazon, Nvidia blog) placed before the 12–19 Aug Cerebras row; [d27] SK
Hynix (13 Aug); [d28] Nvidia/OpenAI Ohio (17 Aug); [d29] Anthropic/Nscale (26 Aug, before the 27 Aug Redwood row);
description tail now "[d1]–[d29]" and names the financing platforms, the Ohio campus, Nscale, Pecos County, SK Hynix
and the SpaceX case. No Key-people additions.

**What the sources actually said vs the staging rows / brief.** Dates: ~8 Aug (PCMag) → 6 Aug datePublished; ~8 Aug
(SemiAnalysis) → 7 Aug; ~10 Aug (Nvidia asset class) → 11 Aug byline / 12 Aug 00:38Z datePublished; ~31 Aug (Dwarkesh)
→ 29 Aug; ABC 10 Aug is 9 Aug 18:44Z (AEST 10 Aug — kept, explained). Content: (1) SemiAnalysis's H1 and body say
**$300B** ARR and a 10 GW 2027 plan; "$500B" survives only in the page's og:title and "6–10+ GW" is the digest's
paraphrase — the row uses the body. (2) The brief described Anthropic's disclosure as a "1,022-page red-team log
detailing Mythos 5 sandbox break-out attempts" and an Opus 4.6 breach "without human detection". The primary
assessment says: four incidents during cyber evaluations *built by the same evaluation partner*, whose environment was
misconfigured onto the real internet; the 1,022 pages are Mythos 5's PyPI-upload transcript (TechCrunch: hundreds of
pages fighting the CAPTCHA); the fourth incident is an *early checkpoint of Claude Opus 4.6*, from January 2026, found in
August when a wider scan (~481M transcripts) turned it up — Anthropic says its assessment of it is preliminary and not
more severe than the other three. Rows and citations quote that. (3) Reuters' "at least 10" is Kenneth DeGraff's
count; CivAI's Andrew Yoon reports 18, Sydney Von Arx's group 23; Unite.AI's explorer has 30 sites total (12 community-
found, incl. the tmcleod.org AP Chemistry wiki, 27 revisions 24 May–7 Jul). Row: "at least 10 — by other counts 18–23".
(4) The brief's "10-gigawatt data center lease" conflates two figures: CNBC's securities-filing report says 4.25 GW
initial + 3.75 GW option of *compute*, with SB Energy/SoftBank building "power sources supporting 10 gigawatts" and
$4.2B of grid investment; the row separates them. (5) "Repurposed former Microsoft data center site" — Microsoft signed
a letter of intent for the West Virginia Monarch site in March and exited it over the summer; nothing was built. Row:
"a site Microsoft had signed a letter of intent for … and walked away from". (6) The Dwarkesh piece is a secondary
synthesis of the OpenAI (38 pp) and METR/Redwood (91 pp) reports, with an OpenAI researcher's public correction
appended on one detail; confidence medium, and the row credits the synthesis, not the lab, for the third-wave scope.

**Sourcing.** Each URL fetched before citing. Live 200: pcmag.com, abc.net.au, dwarkesh.com, anthropic.com (primary
"An alignment assessment of recent cybersecurity incidents", 9 Sep — linked from the TechCrunch piece), techcrunch.com,
tomshardware.com ×2, unite.ai, newsletter.semianalysis.com, blogs.nvidia.com, cnbc.com ×3, finance.yahoo.com. Blocked →
verified another way → allowlisted with the method in the comment: openai.com (RSS pubDate Fri 07 Aug 2026 15:20 GMT;
Wayback 20260916035605 200, cited alongside), reuters.com (401 + DataDome; `archive.ph` unreachable, no Wayback
snapshot; headline + date via Google News RSS' Reuters source entry, Seeking Alpha and Yahoo NZ syndication; content
via the Tom's Hardware and Unite.AI pickups cited alongside), nytimes.com (403; no Wayback snapshot; headline + 8 Aug
date via Google News RSS; figures via Tom's Hardware, which attributes them to the NYT report), bloomberg.com ×2
(headline + date via r.jina.ai; terms via CNBC's confirmations, "Bloomberg was first to report"). Method note: Google
News RSS article IDs were resolved to real publisher URLs with the `batchexecute` decoder (`/tmp/gdecode.py`) instead of
guessing CNBC slugs — two guessed slugs had returned CNBC's generic 2018 page and were discarded. The staging feed's
17 Aug Bloomberg URL lacks the `www.` host; kept verbatim (Bloomberg redirects) and allowlisted as-is.
`check_research.py`: research/08 R-01…R-07 PASS (86 rows, 145 sources, 254 links 0 failed / 18 allowlisted);
research/09 R-01…R-07 PASS (16 rows, 118 sources, 254 links 0 failed / 14 allowlisted). The first /09 run reported
failed=1 (transient; `check_links.sh` alone and a full re-run both gave failed=0).

**Gates.** `validate.py` files=19 rules=25 fails=0 (`/tmp/validate_venv/bin/python`). The session-17 `/tmp/pwvenv` and
`/tmp/pw-browsers` had been wiped between sessions; rebuilt with `uv venv /tmp/pwvenv`, `uv pip install playwright
pyyaml pillow`, `playwright install chromium` (PLAYWRIGHT_BROWSERS_PATH=/tmp/pw-browsers) — `pillow` is needed for
check_layout's texture-variance sample and is not in the brief's recipe. `check_layout.py` all structural / country /
containment / zero-overlap / thread gates 0; `clipped` 625 (the pre-existing A1 event-box class at plate x > 2746,
unchanged since session 14; RESULT: FAIL is that gate alone). `check_lod_labels.py` LOD LABEL GATE: PASS (lod4 47 marks,
75 one-line rows, curated-out set unchanged). Nothing under `site/` or `data/regions/` changed, so no tile rebuild.

**Commits.** One content commit (research/08, research/09, allowlist, staging ticks) followed by this STATUS +
ORCHESTRATOR_LOG commit; both pushed straight to `main` per the brief.

**Next.** All twelve are corpus-only. The Black Hat / Anthropic-assessment pair is the strongest candidate for a
Generative Coast `alignment-interpretability-plateau` event when budgets reopen; the $105B Ohio campus and the $500B
financing platforms for `compute-hardware-hinterland`. Staging: 178 unticked rows, no cluster above ~8.


## Session 19 (2026-09-17) — agent-platform / inter-agent + Chinese-frontier / Pax Silica promotions (research/08 [146]–[155], research/09 [c19]–[c20], [e13]–[e17])

**Why.** Session 18's STATUS left two dense clusters in `data/staging/innermost-loop-candidates.md`: agent platforms,
inter-agent communication and harnesses (Claude Code inter-session messaging and auto-mode default, Cloudflare
Kitesurf, OpenAI Computer History, Slack Code, Nvidia AVO) and Chinese frontier open weights + Pax Silica geopolitics
(ByteDance's 10T model, GLM-5.3 and its AA Index score, Apple's China model with Alibaba, the State Department's
"pick sides" letter, Hugging Face's summer open-models report). The brief named the twelve staging rows and their
sources.

**What.** Every source was fetched before writing. research/08 gained ten timeline rows in date order among the
existing Aug 2026 rows and sources [146]–[155]; research/09 gained two Conscience Road rows ([c19] auto-mode default +
Computer History's prompt-injection note; [c20] GLM-5.3's open-weights cyber claim against the gated Mythos tier) and
five Commons Road rows ([e13] ByteDance, [e17] the agent layer as commons, [e14] GLM-5.3 + AA Index, [e15] the Hugging
Face report, [e16] Apple-in-China + Pax Silica), with both thread descriptions extended and the (e) table re-sorted so
the new rows precede the existing 14–27 Aug consolidation row. The GLM-5.3 release and the 18 Aug AA Index post share
one research/08 row cited [149][152]; the two Reuters exclusives share [150].

**Corrections against sources.** Eight of the twelve staging dates were off by 1–4 days (fixed from page metadata,
fxtwitter timestamps and Google News RSS pubDates). Claims: auto mode is default for *new sessions on Pro/Max/Team
from 14 Aug* (announced 7 Aug); the ByteDance item is two reports (FT for "up to 10 trillion total parameters", The
Information for the no-distillation pledge); GLM-5.3's Mythos 5 / Sol comparisons are Z.ai's own numbers; the AA
Index has GLM-5.3 and Kimi K3 tied at 60 *one point behind* Grok 4.6 and GPT-5.6 Sol Max, not matching them; the Pax
Silica letter is a draft addressed to the 35 June "AI Opportunity Statement" signatories and names WAICO; Apple's is
the first *foreign proprietary model approved by Beijing* (no on-device/cloud-hybrid claim in the source); Hugging Face
measures monthly parameter ceilings and Qwen derivatives, not "downloads dominance"; AVO's 100% is on the public
ARC-AGI-3 set without ARC Prize verification.

**Sourcing hygiene.** Live 200: simonwillison.net, claude.com, blog.cloudflare.com, learn.chatgpt.com, 9to5mac.com,
salesforce.com, developer.nvidia.com, z.ai (client-rendered; text read from the JS bundle), huggingface.co,
techtimes.com, finance.yahoo.com and taipeitimes.com (Reuters syndications), x.com ×2 (200 to curl; text + timestamps
via the fxtwitter API mirror). Allowlisted with method: ft.com (403; reader proxy for headline + Published Time;
Reuters pickup in Google News RSS), reuters.com ×2 (401 + DataDome; Google News RSS IDs decoded via batchexecute; full
text via the syndications cited alongside). web.archive.org refused all connections this session (archive.org 200), so
no Wayback snapshots. `check_research.py`: 08 and 09 R-01…R-07 PASS (08: 96 rows, 155 sources, 271 links 0 failed /
21 allowlisted; 09: 16 rows, 125 sources, 271 links 0 failed / 17 allowlisted). Transient failures: one /09 link on the
first run, then the session-18 Wayback URL in /08 (connection refused) — both 0 on re-run; not allowlisted since the
outage is archive.org's. My own first-pass failures (a `[d10]` cross-file cite in a /08 row; `(accessed …; note)`
ordering that R-05 rejects) were fixed before commit.

**Gates.** `validate.py` files=19 rules=25 fails=0 (`/tmp/pwvenv/bin/python`). `/tmp/localroot` had been wiped, so
headless-shell failed on `libnspr4.so`; the libs survive under `/tmp/localdeps/usr/lib/x86_64-linux-gnu` (and
`/tmp/debroot/...`) — set `LD_LIBRARY_PATH` there before `check_layout.py` / `check_lod_labels.py`. `check_layout.py`
all structural / country / containment / zero-overlap / thread gates 0; `clipped` 625 (pre-existing A1 class at plate
x > 2746; identical on a stashed-clean `main` run; RESULT: FAIL is that gate alone). `check_lod_labels.py` LOD LABEL
GATE: PASS (lod4 47 marks, 75 one-line rows, curated-out set unchanged). Nothing under `site/` or `data/regions/`
changed, so no tile rebuild.

**Commits.** One content commit (research/08, research/09, allowlist, staging ticks) followed by this STATUS +
ORCHESTRATOR_LOG commit; both pushed straight to `main` per the brief.

**Next.** All twelve are corpus-only. The GLM-5.3 open-cyber row and the Pax Silica letter are the strongest
candidates for Generative Coast events (`alignment-interpretability-plateau` / policy) when budgets reopen; Kitesurf +
Slack Code + AVO for an agent-harness event. Staging: 166 unticked rows, no cluster above ~6.

## Session 20 (2026-09-17) — frontier-lab finance / IPO run-up + data-center power / moratorium / sovereign-energy promotions (research/08 [156]–[166], research/09 [d30]–[d34])

**Why.** The session-20 brief named two clusters in `data/staging/innermost-loop-candidates.md`: frontier-lab
financial escalation, IPO run-up and corporate restructuring (Anthropic's $965B → ~$2T valuation, Q2 $11.5B /
positive adjusted operating income / $65B run rate vs OpenAI's $40B run rate, $6.7B Q2 and $12.3B loss; Reuters' inside
account of Brin's reshuffle; Axios on OpenAI's pre-IPO exec exits) and data-centre power battles, municipal
moratoriums and sovereign energy deals (Nvidia's $3B Lancium stake, >500 local bans, Theseus Infrastructure, the $9.1B
Riot lease, Mistral's European Compute Units, Shapiro's Pennsylvania order, Broadcom's $60–100B chip debt). Twelve
candidates across fifteen staging checkboxes.

**What.** Every source was fetched before writing. research/08 gained five combined timeline rows in date order among
the existing Aug 2026 rows and sources [156]–[166]; research/09 gained three Silicon River rows ([d30]–[d32] the
7–11 Aug power-ownership week: Lancium, the 500-ban count, Theseus, Riot; [d33] Mistral's ECUs and the 1 GW-by-2030
target; [d34] Shapiro's order + Broadcom's debt raise) with the thread description extended to [d1]–[d34]. The
WSJ/FT valuation pair, the Bloomberg Q2 / run-rate figures and the WSJ scoreboard share one /08 row cited [161][162];
Reuters + Axios share [163][164]; the two The Information reports and Theseus share [156][157][158].

**Corrections against sources.** Five of the staging dates were off by 1–2 days (Lancium 7 Aug, WSJ confidence piece
11 Aug, Mistral 11 Aug, Shapiro 18 Aug; WSJ scoreboard 19 Aug confirmed). Claims: Nvidia's $3B is "up to" (initial $2B
for ~20%); the moratorium count is >500 jurisdictions and NY/TX are a permit freeze and an audit, not bans; Theseus is
owned by Macquarie + GIC with Anthropic as anchor tenant, not a three-way JV, and the electricity pledge dates from
Feb 2026; Riot's own statement names only "a leading frontier AI lab"; Mistral's post does not state a gigawatt — the
1 GW / 2030 target is Mensch's VentureBeat interview; FT's $2T is a "bet", WSJ's $965B the May Series H mark;
Anthropic's profit is "adjusted" and WSJ flags the methodology; Reuters' Brin piece is an inside account of the 8 Aug
reshuffle already at [125]; Broadcom is "in talks" for a $60–70B senior-secured tranche, up to $100B total.

**Sourcing hygiene.** Live 200: mistral.ai, nbcnews.com, anthropic.com, businesstimes.com.sg, thenextweb.com,
techtimes.com, cnbc.com ×3, finance.yahoo.com, financialpost.com, seekingalpha.com, calcalistech.com,
proactiveinvestors.com. Wayback is back: snapshots for both WSJ pieces and the Axios piece, `<title>` verified, cited
alongside. Allowlisted with method: wsj.com ×2, ft.com, reuters.com, bloomberg.com ×6 (reader proxy for headline +
date; figures from the pickups cited alongside), axios.com, datacenterdynamics.com ×2, venturebeat.com (429).
theinformation.com ×2 are 200 to the checker so not allowlisted. `check_research.py`: 08 and 09 R-01…R-07 PASS (08:
101 rows, 166 sources, 303 links 0 failed / 35 allowlisted; 09: 16 rows, 130 sources, 285 links 0 failed / 23
allowlisted). One /09 link is flaky (failed on two of four runs, 0 on both immediate `check_links.sh` re-runs). The
full-corpus run surfaces research/04 R-03 failed=2 — europepmc.org ×2 now 403 to curl; that file is untouched since
6 Sep and outside this brief, left as a follow-up rather than allowlisted blind.

**Gates.** `validate.py` files=19 rules=25 fails=0 (`/tmp/validate_venv/bin/python`). `check_layout.py` all
structural / country / containment / zero-overlap / thread gates 0; `clipped` 625 (pre-existing; RESULT: FAIL is that
gate alone). `check_lod_labels.py` LOD LABEL GATE: PASS (lod4 47 marks, 75 one-line rows, curated-out set unchanged).
`LD_LIBRARY_PATH=/tmp/localdeps/usr/lib/x86_64-linux-gnu:/tmp/debroot/usr/lib/x86_64-linux-gnu` still required for
headless-shell. Nothing under `site/` or `data/regions/` changed, so no tile rebuild.

**Commits.** One content commit (research/08, research/09, allowlist, staging ticks) followed by this STATUS +
ORCHESTRATOR_LOG commit; both pushed straight to `main` per the brief.

**Next.** All fifteen are corpus-only. The lab-finance divergence row ([161][162]) is the strongest Generative Coast
event candidate; the 7–11 Aug power-ownership week ([156]–[159]) the strongest Silicon River one. Staging: 151
unticked rows, no cluster above ~6. Fix research/04's europepmc.org links (allowlist with method or swap to
PubMed/DOI).

## Session 21 (2026-09-17) — physical-AI / robotics / autonomous-fleet + AI-for-science / math / bio-discovery promotions (research/08 [167]–[182], research/09 [b13]–[b19], [d35]–[d36]); research/04 europepmc → PubMed

**Why.** The session-21 brief named two clusters in `data/staging/innermost-loop-candidates.md`: physical AI,
robotics, embodiment and autonomous fleets (Dyna-2's human-to-robot scaling law, Waymo's 18-county CPUC approval,
$47.4B of H1 physical-AI funding, Generalist's GEN-1.5, Nevada's 7,000 robotaxi permits, Waymo's 1,000-TOPS ASIC,
SoftBank's $6B bid for 1X, Anthropic's Model Hardware Standard, Nvidia's $10B physical-AI business and China's 90%
humanoid share) and AI for science, mathematics and bio-discovery (research Claude's 41.6% → 67.2% Riemann bound
with Lean certificate, Claude's 14/15 protein-design campaign, GenBio's AIDO Cell, Google's Co-Scientist paper,
BirdCODE, UCSF's profound-autism protein atlas, Insilico's rentosertib aging-clock result). Sixteen staging
checkboxes. Plus the open research/04 europepmc follow-up from session 20.

**What.** Every source was fetched before writing. research/08 gained fourteen timeline rows in date order among
the existing Aug–Sep 2026 rows and sources [167]–[182]; Nevada + Waymo compute share one "robotaxi day" row
[174][175]. research/09 Thread (b) Embodiment Road gained six milestone rows and sources [b13]–[b19] with the
description extended to [b1]–[b19]; Thread (d) Silicon River gained [d35] (Waymo ASIC) and [d36] (Nvidia physical
AI / China) with the description extended to [d1]–[d36]; the (b) rows cross-link to (c) for MHS and to (d) for the
chip and export-control items. research/04 [3] and [4] now link PubMed (200) with the PNAS DOIs noted; the three
europepmc URLs (two for [3], one in the timeline) are gone.

**Corrections against sources.** Nine of the sixteen staging dates were off by 1–3 days (Riemann 10 Aug; Crunchbase,
protein design and AIDO Cell all 18 Aug; GEN-1.5 19 Aug; SoftBank–1X 26 Aug; MHS and Co-Scientist 27 Aug; WSJ 29
Aug). Claims: the Riemann result is a lower bound on the proportion of zeros on the critical line, not a proof; the
"95% expressed" figure is not on Anthropic's page and was dropped (the page gives 14/15, 26.7%/22.6% batch vs 35.1%
single-target, 354 binders from 1,320 designs, and a dual-use warning); Waymo's own post says >1,000 TOPS and 20× in
eight years and lists TSMC among seven partners — the "5 nm to reduce Nvidia dependence" framing is Bloomberg's
(Ed Ludlow; Yahoo Finance full text); Nevada is three permits totalling 7,000 (Tesla 5,000 / Waymo 1,000 / Uber
1,000 via Motional + Zoox) and Tesla's engineer called 5,000 "a ceiling"; the Co-Scientist MXene claim is hedged in
the abstract ("further experiments are needed to confirm the atomic structure"); the Nvidia $10B is against $303B
trailing revenue and the 90% humanoid share is H1 2026 shipments; UCSF's ~1,800 interactions are in Science, with
AlphaFold for contact geometry and frogs + organoids for function; Insilico's result is n = 42, six proteomic clocks,
company release on a Nature Biotechnology paper — flagged medium confidence.

**Sourcing hygiene.** Live 200: dyna.co, electrek.co, news.crunchbase.com, generalistai.com, techcrunch.com,
waymo.com, anthropic.com ×3, arxiv.org, earthspecies.org, npr.org, insilico.com, statnews.com,
interestingengineering.com, finance.yahoo.com, livemint.com, zawya.com, theinformation.com (200 to the checker
though client-rendered — headline + date confirmed via Google News RSS). Allowlisted with method: bloomberg.com
(Waymo chip; no Wayback snapshot exists, syndication cited alongside), wsj.com (Nvidia robots; 401, Google News RSS +
Mint syndication), genbio.ai (Cloudflare challenge 403; reader proxy + STAT). Google News RSS article links were
resolved to publisher URLs with the batchexecute decoder (`/tmp/s21_gdecode.py`) — useful for paywalled headlines.
`check_research.py`: 08, 09 and 04 all R-01…R-07 PASS on a clean pass (08: 116 rows / 182 sources / 325 links 0
failed 38 allowlisted; 09: 16 / 139 / 299, 0 failed 25 allowlisted; 04: 34 / 92 / 102, 0 failed). Wayback is flaky
again: one /08 run showed 11 `000` timeouts all on web.archive.org, the next 0; one /09 run showed 1, the next two
0. Nothing allowlisted for it. R-05 pitfall: the accessed date must be the literal `(accessed YYYY-MM-DD)` group —
`(doi …; accessed …)` fails the regex, so the DOI note is a separate parenthetical.

**Gates.** `validate.py` files=19 rules=25 fails=0. `check_layout.py` all structural / country / containment /
zero-overlap / thread gates 0; `clipped` 625 (pre-existing; verified identical with this session's changes stashed;
RESULT: FAIL is that gate alone). `check_lod_labels.py` LOD LABEL GATE: PASS (lod4 47 marks, 75 one-line rows,
curated-out set unchanged). `LD_LIBRARY_PATH=/tmp/localdeps/usr/lib/x86_64-linux-gnu:/tmp/debroot/usr/lib/x86_64-linux-gnu`
still required. Nothing under `site/` or `data/regions/` changed, so no tile rebuild.

**Commits.** One content commit (research/04, research/08, research/09, allowlist, staging ticks) followed by this
STATUS + ORCHESTRATOR_LOG commit; both pushed straight to `main` per the brief.

**Next.** All sixteen are corpus-only. The 20 Aug robotaxi-day row ([174][175]) is the strongest Embodiment Road
event candidate; the Riemann bound ([167]) and the protein-design/AIDO Cell pair ([171][172]) the strongest science
ones. Staging: 135 unticked rows, no cluster above ~5. No open link follow-ups.
