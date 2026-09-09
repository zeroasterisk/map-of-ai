# STATUS — as of 2026-09-09 (session 3 + render passes v5–v11; v11 visibly-tinted biome fills live)

## One-line status

**Gate: awaiting Alan's review of the continent registry via the rendered
prototype at <https://zeroasterisk.github.io/map-of-ai/> before P2-T2
(individual continent authoring) proceeds.** P0 (tooling) and P1 (research
coverage + triangulation) are complete and pushed; `data/continents/REGISTRY.md`
(10 continents) is proposed. Monthly frontier intake (P5) is **deferred by
Alan, not scheduled.**

## What Alan is being asked to review

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
| P2-T2…T13 | continents | **not started — gated on Alan's review** | — |
| P3 countries | P3-T1…T12 | not started (instance mapping recorded in `REGISTRY.md` §6) | — |
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
