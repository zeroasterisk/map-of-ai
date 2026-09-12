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
