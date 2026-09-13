# STATUS — as of 2026-09-13 (session 10: Generative Coast decomposed into 8 countries — density stress-test, data layer only)

## One-line status

**Session 10 — P2-T10 + P3-T10 (Generative Coast, 2022–present) data layer shipped 2026-09-13.** Alan: "the map
looks sparse to me … We can try the most current timeframe and see what dense looks like." Coverage matrix
`data/coverage/generative-coast.md` maps research/08's 8 `## Schools of thought` bullets 1:1 to 8 countries (8 < SPEC
§4.3 cap of 9; 0 merged, 0 dropped): `closed-frontier-labs` The Closed Frontier (Ca) · `open-weights-movement` The
Open-Weights Commons (Cb, 2023–) · `diffusion-media-district` The Diffusion Shoreline (S2a+S2b) ·
`reasoning-test-time-compute` Reasoning Ridge (N2b, 2024–, wetland) · `agents-tooling-coast` The Agents Causeway
(S1a+S1b, mixed) · `alignment-interpretability-plateau` The Alignment Plateau (N1b, mixed) · `policy-governance-coast`
The Policy Coast (N1a, 2023–, highland) · `compute-hardware-hinterland` The Compute Hinterland (S2c, harbour).
`data/continents/generative-coast.yaml` (P2-T10) written in the same session because validate.py V-30 needs the
parent. Sourcing: all 59 country `sources[].url` + 8 continent urls are byte-identical substrings of research/08's
`## Sources`; every `research_ref.sources` int exists there (V-22); every dated fact in the 9 summaries was
spot-checked by grep against research/08's timeline (Midjourney 12 Jul 2022, GroqCloud 19 Feb 2024, Nvidia $4T, 28
countries at Bletchley, Qwen3.8, Muse Spark, Sora 2, Cowork, $5.6M, Mostaque, Sydney, SSI, AlphaProof, Kimi K2, Gemma 4,
Turing Award, 100 million — all present). `scripts/validate.py` → files=19 rules=25 fails=0 **including V-20 live
links**. Render wiring: `site/atlas.html` country grid gained N1a/N1b/N2a/N2b fine rows (the coast is the only
full-height continent), 2023/2024 sub-columns and `end: 'present'` → E; `build_entities_json.py` / `validate.py`
SUB_BANDS now list N1a–N2b; `entities.json` = 17 countries, 15 spatial. `check_layout.py` (N_COUNTRIES 7 → 15): all
country gates PASS — countryCount 15/15, containment 300/300 inside parent for all 15, zero-overlap 0 pairs, 0 label
overlaps, 0 labels outside, A2 zoom consistent. Its overall RESULT is FAIL only on `clipped` (A1 event labels near
the viewBox edge), which is pre-existing: 179 before this change, 160 after (verified by `git stash`). Evidence:
`docs/screens/generative-coast-a2.png` (A2 country view: 8 stacked provinces N→S, each with name + years; new
`site/probe_continent_countries.py <continent-id>` prints per-country bbox + visible labels). NOT done (Phase 2,
separate task): z0–z5 tiles, `data/events/generative-coast.yaml`, hints, headline events; deep-learning-basin data
and tiles untouched. Known: `site/probe_countries.py` times out on `#shapes .continent` visibility at baseline too
(pre-existing, not investigated).

**LEAFLET v3.1 (LOD pilot fixes) shipped 2026-09-13** — https://zeroasterisk.github.io/map-of-ai/
**Alan on v3:** "text is crazy big, when you zoom in it should have resized" and "I don't understand the red lines".

**Fix 1 — text sized in SCREEN px, not plate units.** build_tiles.py screenshots
lod level z at device scale 2**z, and every label font-size was a plate-unit
constant, so on-screen text GREW with zoom (kev-name 4.0 plate × 8 = 32 px at
z3 → 2.3 × 16 = 36.8 px at z4; country kname 10.2 plate × 16 = 163 px at z4).
atlas.html now derives the plate font-size from a per-role screen-px target:
`plate_fs = target_px / 2**lod` (`TILESRC`/`LOD`/`ZSCALE`/`PX()` at the top of
the script; only in `?tilesrc=1` mode — the plain interactive atlas.html is
byte-for-byte the same layout). Targets: kname 34 px, ktag/ksub/kyrs 28 px
(lod2–4, the auto-fit tier ladder scales by the same factor, line gap 4 px);
khint 16 px (lod1 — 28 px fits in no lane, 16 px is the largest size that
places both hints); kev-name 30 → 26 px, kev-year 22 → 19 px (lod3 → lod4),
kev-line 19 px. Measured (site/measure_lod_text.py, getBoundingClientRect ×
2**lod, median bbox height in screen px):

| role | before lod2 / lod3 / lod4 | after lod2 / lod3 / lod4 |
|---|---|---|
| kname (country) | 48 / 96 / 192 | 40 / 40 / 48 |
| ktag / kyrs | 40 / 80 / 160 | 36 / 36–40 / 48 |
| kev-name (same event, e.g. AlexNet) | – / 42.7 / 48.0 (+12 %) | – / 40.0 / 34.3 (−14 %) |
| kev-year | – / 29.3 / 35.2 | – / 26.7 / 22.9 |
| kev-line | – / – / 32 | – / – / 22.9 |

(kname at lod4 is 48 vs 40 at lod3 because the widest tier now fits inside
every lane at z4 — +20 %, the "a bit bigger at deeper lod" allowance; before it
was ×2 per level.)

**Fix 2 — event leaders.** `.kev-leader` was the dot's rust red (#7a2414) and
read as a road. Now the country leader's language: solid #3d2e1a hairline
(.45, opacity .7). Deliberately NOT dashed — the province line (.kzoom) and
road border (.cborder.road) at lod2–4 are already dashed brown, and a dashed
trial rendered indistinguishable from them (docs/screens review). Evidence:
docs/screens/lod4-leaders-after.png (Attention Headwaters, z4, 4 leaders).
`.kev-dot` stays red.

Gates after both fixes: check_lod.py PASS, check_lod_labels.py PASS (0
overlaps, 0 dots outside, 0 off-plate; curated: ev3 white-house-2016, ev4
ntm-2014 / show-and-tell-2014 / sensetime-ilsvrc-2016). Basin text items /
chars / marks per level are now 5/39/0 → 7/122/0 → 32/446/0 → 72/928/20 →
201/2950/47 (smaller text = more of the 47 events fit at z4; was 32).

## One-line status (session 8, superseded)

**LEAFLET v3 (LOD pilot) shipped 2026-09-12** — https://zeroasterisk.github.io/map-of-ai/
**Alan's feedback on v2:** "the details are not detail-y enough … I really want
the zoom-in to provide more and more and more detail at every step, not just
a different texture" and, correcting the plan to bolt a deeper tier on: "the
levels you have right now maybe don't need to exist without additional
detail … each of those steps needs to have a significant increase in the
amount of information presented for the same region." Diagnosis of v2 by its
own numbers: z0→z1 was texture + one year line, z2→z3 was a subtitle line.

**What changed — 5 levels (z0–z4), each step carries new FACTS, not a new
texture.** Content redistributed and expanded across the existing steps; z4
added because 40+ sourced events at z3 would have collided (curate, don't
overlap). PILOT SCOPE: only the Deep Learning Basin has hint/tag/event data;
every other continent renders exactly as before (its z3 art also serves
zoom 4 — no new tiles elsewhere). Wider rollout is a separate task, not
started.

| level | px/unit | tiles | NEW at this step (Basin) | basin text items / chars / event marks |
|---|---|---|---|---|
| z0 | 1 | 24 | continents, names | 5 / 39 / 0 |
| z1 | 2 | 90 | textures, continent years, faint borders, **+4 landmark hints** ("ImageNet · AlexNet 2012", "DQN → AlphaGo", "word2vec → attention", "Google Brain · DeepMind · OpenAI") | 8 / 152 / 0 |
| z2 | 4 | 319 | solid borders, country names, **+ per-country one-line tag + years** (7 tags, e.g. "ImageNet → AlexNet → ResNet", "SenseTime; first national AI plans") | 33 / 429 / 0 |
| z3 | 8 | 1254 | country subtitles, **+17 headline events as dots at their year** (ImageNet 2009, Google Brain 2011, AlexNet 2012, DQN 2013, word2vec 2013, VAE 2013, GAN 2014, ResNet 2015, AlphaGo v. Lee Sedol 2016, WaveNet 2016, Switchboard parity 2016 …) | 67 / 662 / 17 |
| z4 | 16 (bbox only, 560 tiles) | 560 | **+15 more events (32 on the map) and a sourced one-line fact under each headline event** (e.g. AlexNet "15.3 % top-5 error vs 26.2 %"; Four-groups paper "error rates fall ~30 %") | 144 / 1880 / 32 |

Before (v2, same region, same measurement): 5/39 → 4/64 → 15/184 → 22/247;
z0→z1 LOST items; z2→z3 added only 7 subtitle lines. After: every step at
least doubles the text items (5→8→33→67→144) and chars grow 39→152→429→
662→1880. `site/check_lod_labels.py` (new gate) asserts this growth per
step and ZERO text-on-text overlaps, every event dot inside its own country,
at every level: PASS (`docs/screens/check_lod_labels_after.txt`; before
numbers in `docs/screens/lod_labels_before.json` — v2 also had one kname
overlap at lod2 the old gate never saw).

`site/check_lod.py` reworked: the old "ink fraction after downsampling all
levels to z0 size" metric erased small type (z2→z3 read +0.0016) and could
not see the difference; it now measures ink MASS at each level's own
resolution, scale-normalised (dark px ÷ 2^z ÷ area ×1000), with a minimum
gain per step. Basin, plate (804,320,386×288):

| step | before (v2) | after (v3) |
|---|---|---|
| z0→z1 | 20.1 → 47.1 (+27.1) | 20.0 → 49.0 (+29.0) |
| z1→z2 | 47.1 → 161.9 (+114.8) | 49.0 → 195.4 (+146.5) |
| z2→z3 | 161.9 → 354.7 (+192.8) | 195.4 → 438.7 (+243.2) |
| z3→z4 | — | 438.7 → 919.4 (+480.7) |

(ink mass also counts textures/borders, so v2's steps were not zero — the
text-item / char counts above are the information measure; both improved
on every step.) Gate PASS, see `docs/screens/check_lod_before.txt` /
`check_lod_after.txt`.

**Sourcing — zero invented facts.** Every hint, tag and event lives in
`data/events/deep-learning-basin.yaml` with `sources:` and traces to
`research/06-deep-learning-revolution-2006-2017.md` (its numbered refs) or a
country YAML `sources:` entry — checked mechanically: all 50 events' URLs
appear verbatim in one of those files (0 unsourced). Examples: AlexNet 2012
→ proceedings.neurips.cc …c399862d… (Krizhevsky, Sutskever & Hinton) +
en.wikipedia.org/wiki/AlexNet; ResNet 2015 → arxiv.org/abs/1512.03385;
"Four groups" 2012 → ieeexplore.ieee.org/document/6296526 (Hinton et al.,
IEEE SPM); AlphaGo v. Lee Sedol → en.wikipedia.org/wiki/AlphaGo_versus_Lee_Sedol.
Detail is
uneven on purpose: Eastern Coast Forts (SenseTime / national plans, 2015–17)
is a narrow lane with only 4 sourced events, 2 of which fit; Speech has 7.
Events that did not fit are curated off the raster (listed by the gate) and
remain in entities.json for hover cards — not overlapped.

**Rendering notes:** events are positioned by derivation (x = X(year), y in
the country's lane), placed with the country-label idiom (offset search →
collision against placed boxes → leader line → curate out). Chromium hints
sub-3 px glyph advances even at DPR 16, which bunched letters in the z4
tiles; `text-rendering: geometricPrecision` in tilesrc mode fixed it (verified
on a 16× crop). z4 is rendered in tile-row strips of the Basin bbox
(768,304)–(1216,624) to bound memory; `index.html` mounts it as a second,
bounded tile layer (`meta.full_zmax`, `meta.pilot_bbox`) so no 404 storm off
the basin. `check_layout.py`, `check_url.py` still PASS.

**Evidence:** `docs/screens/lod2-0.png .. lod2-4.png` (atlas render of the
Basin, 780,300→1220,620, per lod, 4× — compare v2's `lod-0..3.png`),
`docs/screens/lod2-index-z0..z4.png` (the Leaflet viewer on the shipped
tiles at each integer zoom), `docs/screens/lod-tiles-same-region.png`
(z0..z4 reassembled from tiles).
Previous status follows.

## One-line status (session 7, superseded)

**LEAFLET v2 (LOD) shipped 2026-09-12** — https://zeroasterisk.github.io/map-of-ai/
**Alan's bug: "I zoomed in and the tiles didn't change."** Root cause: v1
took ONE 8× screenshot of `atlas.html?tilesrc=1` and made z0–z2 by LANCZOS
downsampling it, so every level was the same picture at a different
resolution — zooming sharpened strokes but never revealed anything. Fix:
**each zoom level is now its own render.** `atlas.html?tilesrc=1&lod=N`
(N=0..3) is a set of CSS-only toggles on already-placed elements (no drawing
math duplicated), and `build_tiles.py` screenshots lod=z at device-scale 2^z
and slices it ONLY into level z (no resampling between levels). What is
visible per level:

| level | px/plate unit | tiles | shows |
|---|---|---|---|
| z0 | 1 (1800×700) | 24 | flat tinted continents (no terrain texture), coast, ONE label per continent (name only), leaders; no country layer |
| z1 | 2 (3600×1400) | 90 | + terrain textures, + continent subtitle/year lines, + faint country borders (A1 style), no country labels |
| z2 | 4 (7200×2800) | 319 | + solid country borders (A2 province line), + country NAME labels; a continent whose countries are labelled hides its own huge name (else "BASIN" sat on "The AlphaGo Delta") |
| z3 | 8 (14400×5600) | 1254 | full detail: country name + subtitle + years, country leaders/dots, per-country biome tints |

Only the Deep Learning Basin has country data (unchanged scope); other
continents just gain textures and year lines from z1 on. Labels/leaders/
countries are therefore IN the raster now; `index.html` dropped the DOM
label overlay (the invisible continent hit-paths for hover cards remain),
and its HUD says which level's tiles are on screen. 1687 tiles, 58 MB.

**Evidence that content changes, not just resolution:**
- `docs/screens/lod-0.png .. lod-3.png` — the same plate region (Basin,
  780,300 → 1220,620) screenshotted at each lod, same scale, side by side.
- `docs/screens/lod-tiles-same-region.png` — the same region REASSEMBLED
  FROM THE SHIPPED TILES of z0..z3, downsampled to one size.
- `site/check_lod.py` (new gate, PASS): after downsampling every level to
  z0 size, dark-ink fraction in the Basin interior is z0 .0103 < z1 .0123 <
  z2 .0371 < z3 .0375 (the z1→z2 jump is the country borders + names);
  adjacent levels differ by mean |Δluma| 23.0 / 10.0 / 6.1 vs a pure-resample
  noise floor of 1.8 / 1.7 / 1.0; a texture-only land patch has luma stddev
  2.9 at z0 vs 18.9 at z1 (flat vs textured); bytes per plate unit² z0 1.1 →
  z3 30.9.
- `site/verify_leaflet.py` (PASS): at fit zoom Leaflet holds 24 tiles all
  from `tiles/0/`; after wheel-zoom to 3.0 it holds 50 tiles all from
  `tiles/3/`; at zoom 2 on the Basin 28 tiles all from `tiles/2/`; 167
  requests, 0 non-200, 0 JS errors. Live: `Last-Modified: Sat, 12 Sep 2026
  22:22:43 GMT` on `/`, `/static-map.html`, `/tiles/meta.json`, sample z0
  and z3 tiles; live `meta.json` carries the per-level `lod` descriptions.

**Audit URL (no pan/zoom UI, raw 256 px tiles at 1:1):**
`https://zeroasterisk.github.io/map-of-ai/static-map.html?level=2&x=15&y=7`
— one tile; add `&r=1` for the 3×3 ring around it; `?level=0` alone shows a
whole level; **`?level=3&px=1000&py=450`** shows the tile containing plate
point (1000,450) — change only `level` to compare the same place across
levels (the page links z0/z1/z2/z3 for the focused tile's centre, and prints
the tile's plate-unit extent). Query params rather than a path like
`/static-map/2/15,7` because GitHub Pages serves static files only — no
server routing, no `_redirects`. `check_layout.py` (atlas.html) still PASS.
Previous status follows.

## One-line status (session 6, superseded)

**LEAFLET v1 shipped 2026-09-12** — https://zeroasterisk.github.io/map-of-ai/
is now a real Leaflet 1.9.4 map (`L.CRS.Simple`, Google-Maps-style
scroll-wheel / pinch / drag / +− zoom) over a raster XYZ tile pyramid of the
**unchanged v11 continent art**. Nothing was redrawn: the old renderer is
`site/atlas.html` (was `index.html`, art byte-identical; gained a
`?tilesrc=1` bare-plate mode and `window.exportLabels()`), and
`site/build_tiles.py` screenshots it at device-scale 8 (14400×5600 px) and
slices `site/tiles/{z}/{x}/{y}.png`, z0–z3, 256 px, **1687 tiles, 62 MB**,
committed as static files (z3 1254 · z2 319 · z1 90 · z0 24). Coordinate
system: 1 plate unit (atlas viewBox px, 1800×700) = 2^z screen px, so every
overlay position is the same `X(year)` / `bandTop(band)` number atlas.html
draws — continent name labels (divIcon markers, sizes from atlas.html's own
placement, ×2^min(zoom,1)), leaders, leader dots and land hit-paths (hover
cards) come from `site/labels.json` exported by that placement code.
Verification (`site/verify_leaflet.py`, run against the LIVE URL): wheel
zoom −0.5 → 3.0, drag moved centre (1131,349) → (1176,334), 192 tile
requests all 200, 0 JS errors — screens `docs/screens/leaflet-v1-initial.png`,
`leaflet-v1-after-wheel-drag.png`, `leaflet-v1-z2-basin.png`.
**Not in this view yet (milestone 2, next session): the P3-RENDER country
layer** (7 Basin countries, A2 labels, containment gates) — still fully
working at `atlas.html`, which `check_layout.py` now targets. Honest image
quality: at fit zoom (−0.5) and z2–z3 native the raster is crisp (ink strokes
clean, no visible seams after the integer-tile-size fix); z3 = 8 px per plate
unit, i.e. 8× the old SVG's 1:1, and `maxZoom` is capped at 3 so tiles are
never upscaled (a z3.5 test showed visible blur + 1 px hairline gaps — both
fixed by the cap and by `width:256px !important` + `will-change`). Fractional
zooms (zoomSnap .25) between native levels are browser-downsampled, slightly
softer than integer levels but no seams. Tile decisions: 256 px (Leaflet
default; 512 would quarter request count but the whole pyramid is ~60 MB
either way), z3 max because z4 would be ~4× the tiles (~250 MB in the repo,
untested 16× = 28800 px screenshot) while z3 already out-resolves the source
textures (512 px JPGs at 230 plate px → 1.8 px per texture px at z3). Previous status
follows.

## One-line status (session 5, superseded)

**P3-RENDER v2 shipped 2026-09-12** — the Deep Learning Basin pilot now renders
7 spatial countries (partition pre-solved by Alan, implemented as given):
`gpu-convnet-school` S2a 2009–2015 · `speech-recognition-converts` S2b
2009–2016 · `deep-generative-shoreline` S2c 2013–2017 ·
`neural-nlp-sequence-school` Ca 2011–2016 · `industrial-lab-founders`
Cb+S1a 2011–2015 · `deep-rl-delta` S1b 2013–2017 · `chinese-state-response`
Cb 2015–2017. Two countries demoted to hover facts (`spatial: false`, data
kept): `tooling-guild` → continent-card "also happening" fact;
`pretraining-foothills` → "preceded by" fact on gpu-convnet-school. One
nudge: chinese-state-response start 2014→2015 (clean Cb handoff from
industrial-lab-founders; noted in its YAML). Sub-bands are a country-layer-only
split of the existing ROWY rows (C→Ca/Cb, S1→S1a/S1b, S2→S2a/S2b/S2c);
continent geometry is byte-identical A1↔A2 (gate). `check_layout.py` →
RESULT: PASS incl. new gates: containment 300/300 in parent for all 7,
zero-overlap 0 hits over 8 pairs × 500 samples, coast/border `d` identical
zoomed vs not, A2 labels non-colliding. Live: https://zeroasterisk.github.io/map-of-ai/
(click the Basin → A2; Esc/sea → A1). Screens: `docs/screens/p3-v2-A1.png`,
`p3-v2-A2.png`, `p3-v2-A2-crop.png`. Honest A2 note: 5 of 7 lanes are too
thin for an inside label and fall back to name+years with a leader; the
2006–2011 western lobe of the Basin is intentionally uncovered (foothills
demoted). Previous status follows.

## One-line status (session 4, superseded)

**Registry accepted by Alan 2026-09-11 (v11) — "registry-frozen".** P0, P1,
P2-T1, P2-T1-RENDER done. Session 4 closed the two P3 spec/plan gaps
(`SPEC.md` §9 P3-RENDER; `PLAN.md` §5 dependency note + P3-RENDER unit) and
landed the pilot data layer: `data/continents/deep-learning-basin.yaml`
(P2-T8) + 9 country YAMLs (P3-T8) + `data/coverage/deep-learning-basin.md`
Table 1; `scripts/validate.py --summary` → files=10 fails=0 (V-20 links live).
**Next gate: Alan reviews `SPEC.md` §9, then P3-RENDER is built** so the pilot
decomposition can be reviewed visually. Monthly frontier intake (P5) remains
**deferred by Alan, not scheduled.**

## What Alan is being asked to review

**Session 4 (2026-09-11) items — review first:**

1. `SPEC.md` §9 (P3-RENDER): the visual grammar G1–G10 and acceptance
   criteria A-V1…A-V10 for drawing countries inside a continent. Key calls:
   two zoom states (A1 = today's map, A2 = click a continent → its countries
   with labels, other continents dimmed); countries reuse the parent texture
   unless their `biome` differs (wetland RL delta, harbour tooling guild);
   thin wobbly interior borders, no new continent geometry.
2. `PLAN.md` §5 dependency note: a continent's countries proceed on
   *registry-frozen* + its own continent YAML, not on all ten continents'
   P2-T2…T13.
3. The pilot decomposition itself (`data/countries/*.yaml`, 9 files) — the
   A-K7 judgement calls are listed at the bottom of
   `data/coverage/deep-learning-basin.md`. Read them as YAML for now; visual
   review comes after P3-RENDER.

**Earlier (registry, v11 — accepted 2026-09-11):**

Open <https://zeroasterisk.github.io/map-of-ai/> (GitHub Pages, deployed from
`site/` by `.github/workflows/pages.yml`; source of truth is
`data/continents/REGISTRY.md`). Questions on the page banner:

1. Does the west-to-east ordering and the left-right sense of scale feel right?
   (X is piecewise-scaled per `AXES.md` §1: 1943–74 1×, 1974–2006 1.5×,
   2006–17 3×, 2017–present 6×; pre-1943 is a log-compressed archipelago.)
2. Do the biome colours read clearly (highland / grassland / forest / jungle /
   mixed)?
3. The two judgement calls in `REGISTRY.md` §2: **D1** research/01 → Antecedent
   Isles (offshore) + Cybernetic Shore; **D2** research/03 → Winter Steppes
   (1974–1993) + Expert Systems Plateau (1980–1993, nested "warm valley").
4. Names/subtitles (`REGISTRY.md` §1). Ids freeze once accepted.

| # | id | name | span | biome |
|---|---|---|---|---|
| 1 | `antecedent-isles` | The Antecedent Isles | 1666–1942 (offshore) | highland |
| 2 | `cybernetic-shore` | The Cybernetic Shore | 1943–1956 | mixed |
| 3 | `symbolic-heartland` | The Symbolic Heartland | 1956–1974 | highland |
| 4 | `winter-steppes` | The Winter Steppes | 1974–1993 | highland |
| 5 | `expert-systems-plateau` | The Expert Systems Plateau | 1980–1993 | highland |
| 6 | `connectionist-revival` | The Connectionist Revival | 1982–1998 | forest |
| 7 | `statistical-isthmus` | The Statistical Isthmus | 1988–2011 | grassland |
| 8 | `deep-learning-basin` | The Deep Learning Basin | 2006–2017 | forest |
| 9 | `transformer-plateau` | The Transformer Plateau | 2017–2022 | jungle |
| 10 | `generative-coast` | The Generative Coast | 2022–present | jungle |

## Phase status

| Phase | Units | State | Evidence |
|---|---|---|---|
| G0 | go-ahead | done (Alan: "get the history and current correct") | this session |
| P0 tooling | P0-T1…T4 | **done** | commits `9d25447` `1db3e92` `bf7c56d` `76d9de6`; `scripts/fixtures/run.sh` passes (25 V-rules, one FAIL per invalid fixture) |
| P1 research coverage | P1-T1…T9, T10, T11 | **done** | commits `7bc7c72` (T11), `89793c3` `c096929` `937d2bf` `28bb209` `40ae90b` `32d271b` `4296598` `58b035d` `8bbfbbe`; all nine files `Status: reviewed`; `scripts/check_research.py research/0*.md` → R-01…R-07 PASS for every file; review reports in `data/reviews/2026-09-06-research-0N.md` |
| P2-T1 registry | P2-T1 | **done, proposed** | commit `95e9323`; `scripts/check_registry.py` → 13/13 PASS |
| P2-T1-RENDER | render + Pages | **done, live (v11)** | commits `1247b0b` … `47cf0d2`; Pages workflow green; live URL HTTP 200 with title text; headless Chromium draws 10 continents, 0 JS errors; `site/check_layout.py` PASS |
| P2-T2…T13 | continents | **P2-T8, P2-T10 done** (`data/continents/deep-learning-basin.yaml`, `generative-coast.yaml`, status sourced); T2–T7, T9, T11–T13 not started, unblocked (registry-frozen) | validate.py 0 FAIL incl. V-20 |
| P3 countries | P3-T1…T12 | **P3-T8 done** (9 countries, coverage Table 1 = 9/9 bullets); **P3-T10 done** (8 countries, Table 1 = 8/8 bullets, all spatial, rendered at A2); A-K2 refs⊆bullet checked; T1–T7, T9, T11–T12 not started | `scripts/validate.py` → files=19 fails=0; `check_layout.py` country gates 15/15 |
| P4 city pilot | P4-T1…T8 | not started | — |
| P5 frontier intake | P5-T0, P5-R1…R6 | **deferred by Alan, not scheduled** (`PLAN.md` §7 header) | — |
| P6 quality | P6-T1…T5 | not started | — |

## P1 in numbers (history accuracy work)

| File | Timeline rows | Sources | Candidates reviewed (added/folded/rejected) |
|---|---|---|---|
| 01 origins | 36 | 51 | 25 (10/9/6) |
| 02 Dartmouth & symbolic | 40 | 57 | 25 (15/7/3) |
| 03 winters & expert systems | 35 | 55 | 24 (12/8/4) |
| 04 connectionism | 34 | 92 | 24 (11/8/5) |
| 05 statistical ML | 30 | 92 | 28 (22/1/5) |
| 06 deep learning | 41 | 120 | 33 (15/13/5) |
| 07 transformers | 43 | 94 | 38 (20/12/6) |
| 08 generative & agents | 63 | 120 | 47 (33/4/10) + triangulation of 6 provisional items (5 moved to sourced rows with confidence, 1 rejected) |
| 09 cross-cutting threads | 16 junctions (+ 8 thread tables) | 95 | 30 (20/5/5) |

Every added item carries a source fetched (HTTP 200) during the review;
reviewer ≠ author per git log (SPEC.md R-07). `research/08`'s "Needs
verification" section is empty; the east edge is Sept 2026 with
`(confidence: …)` annotations on the last rows (`data/reviews/2026-09-06-research-08-triangulation.md`).

## Where to look

| Question | File |
|---|---|
| What is this project? | `BRIEF.md`, `README.md` |
| Coordinates / zoom levels | `AXES.md`, `ALTITUDES.md` — decided |
| What "correct" looks like | `SPEC.md` |
| Work breakdown, DAG, gates | `PLAN.md` (§4 has P2-T1-RENDER; §7 marks P5 DEFERRED) |
| The continent registry | `data/continents/REGISTRY.md` |
| The rendered prototype | `site/` → <https://zeroasterisk.github.io/map-of-ai/> |
| Deep links to a view (`?place=deep-rl-delta`, `?z=2&x=1000&y=400`, copy-link button) | `docs/URL_SCHEME.md`; gate `site/check_url.py` |
| Review reports | `data/reviews/` |
| Tooling | `scripts/README.md` |

## Decisions (recorded; do not re-open)

| # | Decision | Status | Where |
|---|---|---|---|
| 1 | Y = Candidate E, five soft bands; symbolic ↔ learned as biome | Confirmed | `AXES.md` §3 |
| 2 | X mainland starts 1943; pre-1943 offshore archipelago | Confirmed | `AXES.md` §1 |
| 3 | Three altitudes; people are `type: person` cities | Confirmed | `ALTITUDES.md` |
| 4 | Evocative name + neutral subtitle | Confirmed | `SPEC.md` §2.3 |
| 5 | Adjacent fields case-by-case | Soft default | `SPEC.md` §2.9 |
| 6 | X scale piecewise (prototype uses AXES.md §1 ratios) | Rendering decision; prototype implements the piecewise table | `AXES.md` §1 |
| 7 | Monthly frontier intake | **Deferred by Alan, not scheduled** | `PLAN.md` §7 |
| 8 | research/01 → two continents; research/03 → two continents | Proposed (P2-T1), awaiting Alan | `REGISTRY.md` §2 |

## What exists in the repo

| Path | State |
|---|---|
| `research/01`–`09` | `Status: reviewed`; R-01…R-07 PASS; links `failed=0` |
| `data/continents/REGISTRY.md` | proposed (10 rows) |
| `data/reviews/` | 11 reports (9 coverage, 1 triangulation, 1 review brief) |
| `scripts/validate.py` | SPEC.md §3 rules V-01…V-60 (25 rules); `--offline`, `--file`, `--require-children` |
| `scripts/fixtures/` | valid set + one invalid case per rule + `EXPECTED.txt` + `run.sh` |
| `scripts/check_links.sh` | Markdown + YAML `url:` values; allowlist with reasons |
| `scripts/check_research.py` | R-01…R-07 for research files (numeric and lettered source keys) |
| `scripts/check_registry.py` | P2-T1 Check |
| `scripts/wiki.sh` | back-off + retry + on-disk cache |
| `site/` + `.github/workflows/pages.yml` | review prototype, deployed |
| `data/countries/`, `data/cities/`, `data/coverage/` | do not exist yet (P3/P4) |

## Known issues / tooling notes

- `check_links.sh`: `dspace.mit.edu` returns 405 to non-browser requests and
  `doi.org/10.1086/286788` is intermittently slow — both allowlisted with
  reasons in `scripts/link_allowlist.txt`.
- `ai.meta.com/blog/*` → 400 and `openai.com/index/*` → 403 to curl; use
  `about.fb.com`, `openai.com/news/rss.xml`, or Wayback snapshots (recorded in
  the research/08 triangulation report).
- Render prototype: the 1980–2011 cluster (Steppes / Plateau / Revival /
  Isthmus) overlaps by design (ALTITUDES.md §2 "continents overlap in X on
  purpose"); translucency is used so all four read. Real Phase-4 polygons will
  replace this.
- Render pass v10 (2026-09-09): Alan on v9 — "looking pretty good … the
  easternmost edge should be full top to bottom, and if there's some kind of a
  color coding, it should be on theme but a bit more intense." (1) East edge:
  the registry already had the coast at N1–S2; the v7 "ragged frontier" GRID
  rows receded the last two columns to N1b–S2b and N2a–S2a, so the present-day
  coast was only 284 plate px of a 410 px band area. GRID columns 2024.3 →
  present are now all `ggggggggg`; measured land at 2025.9 is plate y 142–564
  (band area 150–560). (2) Tints: BIOME hues kept, saturation ~1.5–3× (highland
  #b48a5c→#c4763a, grassland #c8a85a→#d6a52c, forest #7d8f60→#5e9238, jungle
  #5f8378→#2a8c6c, wetland #7f8f96→#4c8ca4, harbour #a59a84→#b89a5e, mixed
  #7c6f8c→#7a58a4) and the wash/border-band opacities .13/.26 → `TINT_WASH`
  .30 / `TINT_BAND` .48. All gates PASS. **Independent review found the tint
  bump NOT visible** ("colors are on the muted/parchment side") — see v11.
- Render pass v11 (2026-09-09, "biome-only intensity"; Alan: "Intense = biome
  only and don't overdo it"). Root cause of the invisible v10 bump: the tint is
  a normal-blend wash over a texture that is itself ~80 % parchment (texture
  means: sat .20–.36, value .81–.97), so rendered = tex·(1−wash) + tint·wash;
  at wash .30 a fill was still 70 % parchment. Sampled live v10 fill saturation
  (HSV of the mean of 300 in-fill pixels per region) was only .13–.46 and
  chroma barely moved vs v9 — the swatches got vivid, the map did not. v11
  solves the tint FROM the wanted rendered colour (`tint = 2·target − texture
  mean` at `TINT_WASH` .50; `TINT_BAND` .52): highland #b66b30, grassland
  #c5a64c (pulled back from a first candidate #cd9e28 that the reviewer called
  "the one that tips toward garish"), forest #558828, jungle #0f7562, wetland
  #2d7eb7, harbour #af974c, mixed #7155b8. Measured live v10 → v11 saturation:
  symbolic-heartland .38→.45, expert-systems .40→.48, isthmus .46→.45 (chroma
  106→99, deliberately held), connectionist .30→.37, basin .31→.39, transformer
  .18→.24, generative-coast .18→.26, cybernetic .13→.15. Only biome fills
  changed — border ink, labels, sea, halo untouched. Independent vision review
  of the live v11: "clearly more saturated … still holds the antique-atlas
  register". All gates PASS (`check_layout.py` RESULT: PASS, marker v11).
- Render pass v9 (2026-09-08, "isochrone frontiers"): Alan on v8 — "still too 90
  degree rectangular … the basic allocations are still too rigidly along x and
  y grids". Root cause: every boundary was `x = start_year` (one x for the whole
  boundary; wobble/lean on a plumb line is still a plumb line). v9 adds `FRONT`
  in `site/index.html`: per column line, per half-band row, a YEAR OFFSET, so
  every boundary is `x = f(band, year)` — a frontier that arrives in some bands
  years before others (one-line story per line in the comment block). The same
  table ramps the outer envelope's fixed-year steps. Frontiers cannot cross: the
  page asserts ≥ 18 px between consecutive lines on every used row, bounds skew
  per region (≤ 3 yr and ≤ 30 % of span), and clamps jitter + wander to the
  actual local gap. `check_layout.py` now holds each region's drawn x-extent to
  the published `FRONTIER` (± YEAR_SLACK) and has a `frontiersNotDiagonal` gate
  (≥ 6 regions with ≥ 30 px arrival spread across band rows). Measured: 8 of 9
  mainland regions diagonal (the one-row plateau cannot be); formerly plumb
  seams now tilt 16–24°. All gates PASS. Next lever if still too rigid: let the
  Deep Learning Basin reach N2 (needs an ALTITUDES/REGISTRY decision).
- Render pass v8 (2026-09-07, "the funnel"): the mainland now has a GLOBAL
  outer envelope (`ENV` in `site/index.html`, documented in the comment block
  above it) — 2 half-band rows of land at the 1943 tip, 9 rows by 2022, with
  bays (the Winter Gulf 1974–82, the isthmus' southern bay 1998–2006) and a
  tilted north bank so the widening is irregular, not a cone. Regions are
  clipped to the envelope; the v5–v7 internal-border work lives inside it.
  `site/check_layout.py` gained `envelopeViol` (rendered land beyond ENV) and
  `notFunnel` (tip ≤150 px, max ≥3× tip, east-quarter mean ≥2× west-quarter).
  Rendered profile: 88 px at 1943 → 415 px at 2024 (4.7×).
- GitHub Actions warns that `actions/checkout@v4`, `configure-pages@v5`,
  `upload-pages-artifact@v3`, `deploy-pages@v4` target Node 20 (forced to
  Node 24); bump to the next majors when convenient — deploy is green as is.

## Ideas noted, NOT scope

- Street level via citation-graph projection (Phase 5+).
- Voice/copy-edit pass across research files (`SPEC.md` §6 item 8).
- Full render/frontend (Phase 4 of `PROJECT_PLAN.md`) — the `site/` prototype
  is a review aid, not the start of that work.
