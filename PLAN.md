# PLAN — Map of AI, decomposed work plan

> **Status: ready to execute, awaiting Alan's go-ahead.** Supersedes the
> task breakdown in `PROJECT_PLAN.md` §3–§4 (that file's goal statement,
> risks, and Phase 4/5 sketch remain useful background). Every unit below is
> written so that a subagent, a future session, or a human can take it with
> **only** `SPEC.md`, the unit's listed inputs, and this entry — no
> conversation history.
>
> Conventions:
> - Unit IDs are `P<phase>-T<n>` (one-shot) or `P5-R<n>` (recurring, per
>   month). IDs are stable; never renumber.
> - **Check** always names `SPEC.md` rule/criterion IDs. "Reviewer" = a
>   different agent/model/person than the author (`SPEC.md` §0).
> - **Size**: S ≈ one subagent dispatch (< 1 h), M ≈ one focused session
>   (1–3 h), L ≈ split before assigning.
> - Units in the same **wave** can run in parallel. A unit may start when all
>   its **Deps** are merged to `main`.
> - Commit subject starts with the unit id (`SPEC.md` §7 step 6).

## 0. Gate

**G0 — Alan's go-ahead.** No unit starts before Alan confirms this plan and
`SPEC.md`. Anything he changes is applied to `SPEC.md` first (with a `SPEC:`
commit), then the affected units are re-read.

## 1. Phase map and DAG

```
G0
 ├─► P0 tooling ──────────────────────────────────────────────────┐
 │    P0-T1 wiki.sh backoff      (S)                               │
 │    P0-T2 validate.py           (M)  ◄─ SPEC §3                  │
 │    P0-T3 validator fixtures    (S)  ◄─ P0-T2                    │
 │    P0-T4 check_links for YAML  (S)  ◄─ P0-T2                    │
 │                                                                 │
 ├─► P1 research coverage gaps  (needs P0-T1 only)                 │
 │    P1-T1..T9  coverage review per research file (S each, ×9, parallel)
 │    P1-T10     triangulate research/08 provisional items (M)     │
 │    P1-T11     research/01 archipelago vs shore split note (S)   │
 │                                                                 │
 ├─► P2 continents  (needs P0-T2, P1-T11; benefits from P1 done)   │
 │    P2-T1  continent registry: ids, names, subtitles, spans (M)  │
 │    P2-T1-RENDER static review prototype on GitHub Pages (S) ◄─ P2-T1
 │        ▲ REVIEW GATE: Alan reviews the rendered registry before P2-T2+ │
 │    P2-T2..T11 author one continent each (S each, parallel) ◄─ P2-T1 + Alan's review
 │    P2-T12 X-axis tiling + west/east neighbour pass (S) ◄─ all P2-T2..T11
 │    P2-T13 continent review → verified (M, reviewer) ◄─ P2-T12   │
 │                                                                 │
 ├─► P3 countries  (needs P2-T1; per-continent units need that continent's P2-Tn merged)
 │    P3-T1..T10 coverage matrix table 1 + author countries, per continent (M each, parallel)
 │    P3-T11 cross-continent pending-neighbour resolution (S) ◄─ all P3-T1..T10
 │    P3-T12 country review → verified (L: split per continent, reviewer) ◄─ P3-T11
 │                                                                 │
 ├─► P4 city pilot: Deep Learning Basin  (needs P3-T<basin>, P1-T6)│
 │    P4-T1 coverage matrix table 2 for research/06 (M)            │
 │    P4-T2..T5 author cities per country group (S each, parallel) ◄─ P4-T1
 │    P4-T6 person cities for the basin (S) ◄─ P4-T1               │
 │    P4-T7 pilot city review → verified (M, reviewer) ◄─ P4-T2..T6
 │    P4-T8 pilot retrospective + SPEC change proposals (S) ◄─ P4-T7
 │                                                                 │
 ├─► P5 frontier intake (recurring monthly; first run needs P0-T2, P2-T1, P3-T<generative-frontier>)
 │    P5-T0 one-time setup: API keys, manual checklist for feedless labs (S)
 │    P5-R1 collect → P5-R2 filter+triangulate → P5-R3 write frontier file + draft cities
 │        → P5-R4 review → P5-R5 aging → P5-R6 commit   (S/S/M/S/S/S, strictly sequential within a month)
 │                                                                 │
 └─► P6 quality & coverage review (needs the phase it reviews)     │
      P6-T1 id/duplicate/consistency audit across data/ (S)         │
      P6-T2 sibling-set placement review per continent → placed (M each, reviewer)
      P6-T3 source audit: link rot, kind mix, Wikipedia-only entities (S)
      P6-T4 summary claim sampling audit (M, reviewer)              │
      P6-T5 STATUS.md refresh (S)  ◄─ P6-T1..T4
```

**Critical path:** G0 → P0-T2 → P2-T1 → P2-T(basin) → P3-T(basin) →
P4-T1 → P4-T2..T6 → P4-T7 → P4-T8. Everything else hangs off it in parallel.

**Waves (maximum parallelism):**

| Wave | Units that can run simultaneously | Blocks on |
|---|---|---|
| 0 | P0-T1, P0-T2, P1-T11 | G0 |
| 1 | P0-T3, P0-T4, P1-T1…P1-T9, P1-T10, P2-T1 | wave 0 (P1-Tn only needs P0-T1; P2-T1 needs P0-T2 + P1-T11) |
| 1b | P2-T1-RENDER | P2-T1 — then **stop**: Alan reviews the rendered registry (review gate) |
| 2 | P2-T2…P2-T11 (10 units) | P2-T1 + Alan's review of P2-T1-RENDER. (P5-T0 removed from this wave — see §7, DEFERRED) |
| 3 | P3-T1…P3-T10 (each as soon as *its* continent from wave 2 merges), P2-T12 | per-continent |
| 4 | P2-T13, P3-T11, P4-T1 (as soon as P3-T6 basin merges), P6-T1 | wave 3 |
| 5 | P4-T2…P4-T6, P3-T12 (split by continent) | wave 4 (P5-R1 removed — §7 DEFERRED) |
| 6 | P4-T7, P6-T2 (per continent), P6-T3 | wave 5 |
| 7 | P4-T8, P6-T4, P6-T5 | wave 6 |

## 2. Phase 0 — Tooling (small, unblocks everything mechanical)

### P0-T1 — Add back-off to `scripts/wiki.sh`
- **Objective:** Make Wikipedia fetches survive parallel agents (429s after ~25 rapid calls, per `STATUS.md`).
- **Inputs:** `scripts/wiki.sh`; `STATUS.md` "Known issues".
- **Outputs:** modified `scripts/wiki.sh` (sleep + retry on 429/5xx, optional on-disk cache under `.cache/wiki/`).
- **Check:** PASS if a loop of 40 sequential calls for distinct articles completes with 0 non-200 results (command and output pasted in commit body); existing invocation syntax unchanged.
- **Deps:** G0. **Size:** S.

### P0-T2 — Write `scripts/validate.py`
- **Objective:** Implement every rule in `SPEC.md` §3 so entities can be checked mechanically.
- **Inputs:** `SPEC.md` §1–§3, §5.1 (V-50 status requirements); `scripts/check_links.sh` (to shell out for V-20).
- **Outputs:** `scripts/validate.py` (Python 3.11 stdlib + PyYAML via `uv`); `scripts/README.md` usage section; flags `--offline`, `--require-children`, `--file <path>`.
- **Check:** PASS if (a) every V-rule in §3 appears in the code as a function named `check_V_nn` (grep count = 25, one per row of the §3 table), (b) running against P0-T3's fixtures yields exactly the expected FAIL lines, (c) `--offline` skips only V-20, (d) exit code 1 on any FAIL and 0 otherwise.
- **Deps:** G0. **Size:** M.

### P0-T3 — Validator fixtures
- **Objective:** Prove the validator catches what it claims to catch.
- **Inputs:** `SPEC.md` §2.10 worked examples, §3 rule table; `scripts/validate.py`.
- **Outputs:** `scripts/fixtures/valid/` (the three §2.10 examples, made mutually consistent), `scripts/fixtures/invalid/<rule>.yaml` — one file per V-rule that violates exactly that rule — and `scripts/fixtures/EXPECTED.txt` listing expected FAIL lines.
- **Check:** PASS if `validate.py --offline scripts/fixtures/valid` exits 0 and `validate.py --offline scripts/fixtures/invalid` output equals `EXPECTED.txt` byte-for-byte (one FAIL per fixture, correct rule id).
- **Deps:** P0-T2. **Size:** S.

### P0-T4 — Extend link checking to YAML
- **Objective:** `check_links.sh` and V-20 cover `data/**/*.yaml` URLs.
- **Inputs:** `scripts/check_links.sh`, `SPEC.md` V-20.
- **Outputs:** modified `scripts/check_links.sh` (accepts `.yaml`; extracts `url:` values), allowlist unchanged unless a new bot-blocked host appears (with reason comment).
- **Check:** PASS if running it on `scripts/fixtures/valid/*.yaml` prints `checked=N failed=0` with N equal to the number of distinct URLs in those files.
- **Deps:** P0-T2. **Size:** S.

## 3. Phase 1 — Research coverage gaps (fixes what `STATUS.md` flagged)

`STATUS.md` states that link-verification is done but **coverage** is not:
nobody has asked "what important thing is missing?", and `research/08` has a
single-sourced provisional section. These units fix that. They author *review
reports and research-file edits only* — no entities.

### P1-T1 … P1-T9 — Coverage review of one research file (template unit, 9 instances)

| Instance | File |
|---|---|
| P1-T1 | `research/01-origins-pre-1956.md` |
| P1-T2 | `research/02-dartmouth-and-early-symbolic-ai-1956-1974.md` |
| P1-T3 | `research/03-ai-winters-and-expert-systems-1974-1993.md` |
| P1-T4 | `research/04-connectionism-and-backprop-revival-1982-1998.md` |
| P1-T5 | `research/05-statistical-ml-and-probabilistic-ai-1988-2011.md` |
| P1-T6 | `research/06-deep-learning-revolution-2006-2017.md` |
| P1-T7 | `research/07-transformers-and-llms-2017-2022.md` |
| P1-T8 | `research/08-generative-ai-and-agents-2022-present.md` (coverage only; provisional section is P1-T10) |
| P1-T9 | `research/09-cross-cutting-threads.md` |

- **Objective:** Find and fix omissions in one era file, by a reviewer who did not write it.
- **Inputs:** the file; `research/TEMPLATE.md`; `SPEC.md` §4.1 (R-01…R-07), §4.5; `scripts/wiki.sh` (after P0-T1); `SPEC.md` §2.9 scope rule for adjacent-field candidates.
- **Outputs:** `data/reviews/YYYY-MM-DD-research-0N.md` (review report); edits to the research file adding every `added` item with a numbered source; file `Status:` set to `reviewed`; `scripts/link_allowlist.txt` only if a new bot-blocked host is cited.
- **Check:** PASS if R-01…R-07 all PASS for the file (R-07: ≥ 10 candidate omissions each dispositioned `added|folded|rejected` with reason), `scripts/check_links.sh <file>` reports `failed=0`, and A-R1…A-R5 PASS for the report. Prompt to use for candidate generation: "List at least ten things a historian of AI would expect in <era> that are absent from this file; for each, cite one authoritative source."
- **Deps:** P0-T1. **Size:** S each. **Parallel:** all nine, different models/agents preferred.

### P1-T10 — Triangulate `research/08` "Needs verification" section
- **Objective:** Move every item in the mid-2025→2026-09 provisional list to either a sourced timeline row or a documented rejection.
- **Inputs:** `research/08-…md` §"Needs verification"; `SOURCING.md` §1 (source tiers), §4 (triangulation table), §3 (exclusions); `scripts/check_links.sh`.
- **Outputs:** edited `research/08-…md` (provisional section emptied; items moved to timeline rows with Primary + Independent sources, or listed under a new `### Rejected at triangulation` with reason); review report `data/reviews/YYYY-MM-DD-research-08-triangulation.md`.
- **Check:** PASS if the "Needs verification" section contains zero items; every moved row cites ≥ 2 sources of which ≥ 1 is kind primary/official; R-03…R-05 PASS; the rejection list gives a `SOURCING.md` §3 exclusion reason per item.
- **Deps:** P0-T1. **Size:** M.

### P1-T11 — Archipelago / Cybernetic Shore split note for `research/01`
- **Objective:** Make the pre-1943 vs 1943–1955 boundary explicit in the research file so P2 can derive two continents from it.
- **Inputs:** `research/01-origins-pre-1956.md`; `AXES.md` §1 (1943 mainland decision); `ALTITUDES.md` §2 table.
- **Outputs:** edited `research/01` "Map notes" section: a table assigning every timeline row, school bullet and key person to `archipelago (pre-1943, offshore)` or `shore (1943–1955)`; frontmatter "Altitude" line updated to name both continents.
- **Check:** PASS if every timeline row of the file appears exactly once in the new table; R-01…R-05 still PASS.
- **Deps:** G0. **Size:** S.

## 4. Phase 2 — Continents (10–15 entities)

### P2-T1 — Continent registry
- **Objective:** Fix the set of continents, their ids, evocative names, subtitles, X spans, band spans, biomes and source research files, so every later unit can reference stable parent ids.
- **Inputs:** `ALTITUDES.md` §2 table (working titles); every `research/0N` frontmatter + "Map notes" A1 label suggestions; `research/01` split table (P1-T11); `SPEC.md` §2.1, §2.3, §5.2 (min 9, target 10–15, max 15; must tile ≤1943 → current month).
- **Outputs:** `data/continents/REGISTRY.md` — table: `id | name | subtitle | start | end | band span | biome | research file | offshore? | split-of`; plus the decision record for any split/merge of era files.
- **Check:** PASS if 9 ≤ rows ≤ 15; every `research/0[1-8]` file is the source of ≥ 1 row; ids match the V-03 regex and are unique; subtitles match V-12 regex; sorted `start`s tile from ≤ 1943 (archipelago row has `offshore: true`) to `present` with no uncovered year; a reviewer answers "understand from subtitle alone" yes for every row (A-C2 pre-check, recorded at the bottom of the file).
- **Deps:** P0-T2, P1-T11. **Size:** M. **Note:** this is the single most load-bearing unit; do it once, carefully. `AXES.md` rule 2 applies: choose spans that feel right, not spans that satisfy a formula.

### P2-T1-RENDER — Static review prototype of the continent registry (added 2026-09-06)
- **Objective:** Give Alan a rendered map strip to review the registry against ("do these feel like the right regions and neighbours?") instead of raw Markdown. This is the reviewer-optimised bundle that gates P2-T2 onward.
- **Inputs:** `data/continents/REGISTRY.md` (source of truth); `AXES.md` §1 (piecewise X scale, offshore archipelago), §3 (bands, biome palette); `SPEC.md` §2.6.
- **Outputs:** `site/index.html` (single self-contained page: SVG map strip, time graticule, biome-coloured continents with evocative name + neutral subtitle, offshore archipelago, hover/click card, reviewer banner, legend, registry table); `site/build_registry_json.py` (REGISTRY.md → `registry.json`, reusing `scripts/check_registry.py`'s parser); `.github/workflows/pages.yml` (Pages deploy on push to `main`); `site/README.md`.
- **Check:** PASS if the Pages workflow run is green (`gh run watch`), `curl` of the live `html_url` from `gh api /repos/zeroasterisk/map-of-ai/pages` returns 200 and contains the title text "Map of AI — Continent Registry (review prototype)", a headless browser draws exactly as many `g.continent` elements as registry rows with zero JS errors, and no two continents' label bounding boxes overlap.
- **Deps:** P2-T1. **Size:** S. **Gate:** after this unit, wait for Alan's review before dispatching P2-T2…P2-T13. Live URL recorded in `STATUS.md`.

### P2-T2 … P2-T11 — Author one continent entity (template unit, one instance per registry row)
Instances are created from `REGISTRY.md` rows once P2-T1 merges; name them `P2-T<2+row index>` and list them in `REGISTRY.md`'s last column so ids are stable. Expected instances (subject to P2-T1): antecedent-isles, cybernetic-shore, symbolic-heartland, winter-steppes / expert-systems-plateau, connectionist-revival, statistical-isthmus, deep-learning-basin, transformer-plateau, generative-frontier.
- **Objective:** Write the YAML entity for one continent to `status: sourced`.
- **Inputs:** its `REGISTRY.md` row; its research file (summary paragraph, map notes, sources list); `SPEC.md` §2.1 (continent column), §2.3, §2.10 continent example, §4.2; `scripts/validate.py`.
- **Outputs:** `data/continents/<id>.yaml`; header block of `data/coverage/<id>.md` (A-M1 only — tables come in P3/P4).
- **Check:** PASS if `validate.py --file data/continents/<id>.yaml` exits 0 (A-C1); `summary` 120–300 words (V-11); ≥ 3 sources incl. ≥ 1 non-Wikipedia; `research_ref.sources` ≥ 3 and each resolves (V-22); `band` derived per A-C5 with the translation written in `notes`; `neighbours` left as `pending-neighbour:` notes (P2-T12 fills them); `status: sourced`.
- **Deps:** P2-T1 (+ the file's P1 review merged is preferred but not required — if not merged, `notes` says `authored-before-coverage-review`). **Size:** S each. **Parallel:** all instances.

### P2-T12 — X-axis tiling and west/east neighbour pass
- **Objective:** Connect the continents into one coastline: fill `neighbours` west/east for every continent and confirm the X axis is tiled.
- **Inputs:** all `data/continents/*.yaml`; `REGISTRY.md`; each research file's map notes (border descriptions: "ILSVRC 2012 fault line", "First AI Winter cliff", "12 June 2017").
- **Outputs:** edited `data/continents/*.yaml` (`neighbours` filled, `pending-neighbour` notes removed); `data/continents/REGISTRY.md` gains a "tiling verified: <date>" line with the sorted span list.
- **Check:** PASS if every continent has ≥ 1 neighbour (ends: the archipelago has only east; the eastern coast only west) with `relation` and a `note` quoting the research file (A-C6); V-31 zero FAIL; the sorted `time_range` list has no gap (§5.2).
- **Deps:** all P2-T2…T11. **Size:** S.

### P2-T13 — Continent review → `verified`
- **Objective:** Independent verification of all continents.
- **Inputs:** all `data/continents/*.yaml`; `SPEC.md` §4.2, §4.5, §5.1.
- **Outputs:** `data/reviews/YYYY-MM-DD-continents.md`; `status: verified` + `verified_by` on every passing continent; fixes or `STATUS.md` known-issue entries for any FAIL.
- **Check:** PASS if the report lists A-C1…A-C7 per continent with evidence (A-R3), reviewer ≠ author per git log (A-R2), 5-claim spot-check recorded per continent (A-C3), and `validate.py` exits 0 over `data/continents/`.
- **Deps:** P2-T12. **Size:** M. **Reviewer unit.**

## 5. Phase 3 — Countries (~60 entities, 5–9 per continent)

### P3-T1 … P3-T10 — Coverage matrix table 1 + author countries for one continent (template unit, one per continent)
Instances map 1:1 to continents in `REGISTRY.md` (P3-T1 = first row, etc.; record the mapping in `REGISTRY.md`).
- **Objective:** Turn one research file's `## Schools of thought` bullets into country entities under one continent, with every bullet accounted for.
- **Inputs:** the continent's `data/continents/<id>.yaml`; its research file `## Schools of thought` section (each bullet has a `borders:` clause), "Map notes" A2 label suggestions, sources; `ALTITUDES.md` §3 worked examples; `SPEC.md` §2.1 (country column), §2.3, §2.5, §2.9, §2.10 country example, §4.3, §4.4 A-M1/A-M2; `scripts/validate.py`.
- **Outputs:** `data/coverage/<continent-id>.md` Table 1 (one row per school bullet → `country | merged-into:<id> | dropped` + entity id + reason); `data/countries/<id>.yaml` for every `country` decision (5–9 files), each at `status: sourced`, `neighbours` filled for siblings that exist and `pending-neighbour: <name>` notes for schools in other continents.
- **Check:** PASS if Table 1 row count equals the bullet count in the research file (A-M2, checkable with the awk one-liner in `data/coverage/README.md` — created by the first instance to merge); 5 ≤ countries ≤ 9; `validate.py --file` exits 0 for each (A-K1); every country's `research_ref.sources` ⊆ the bullet's cited `[n]`s (A-K2); every sibling named in a `borders:` clause is in `neighbours` (A-K4); word counts in range (V-11); subtitles pass V-12; band recorded as the neighbourhood that "feels right" with `band_override_note` where it departs from a literal reading (A-K7).
- **Deps:** P2-T1 and the continent's own P2-T<n> merged. Not blocked by P2-T13. **Size:** M each. **Parallel:** all ten.

### P3-T11 — Cross-continent pending-neighbour resolution
- **Objective:** Replace every `pending-neighbour:` note with a real `neighbours` entry now that all countries exist.
- **Inputs:** all `data/countries/*.yaml`; `grep -rn pending-neighbour data/`.
- **Outputs:** edited country files; a short table in `data/coverage/README.md` of unresolved names (schools that were `dropped` or merged) with the id they now point to.
- **Check:** PASS if `grep -rn 'pending-neighbour' data/countries` returns 0 lines; V-31 zero FAIL; every country has ≥ 1 neighbour.
- **Deps:** all P3-T1…T10. **Size:** S.

### P3-T12 — Country review → `verified` (split per continent when assigning)
- **Objective:** Independent verification of countries, one continent's set at a time.
- **Inputs:** `data/countries/*.yaml` with `parent_id == <continent>`; that continent's coverage matrix; `SPEC.md` §4.3, §4.5, §5.1.
- **Outputs:** `data/reviews/YYYY-MM-DD-countries-<continent-id>.md`; `status: verified` + `verified_by` on passing countries; fixes or `STATUS.md` known issues.
- **Check:** PASS if A-K1…A-K7 listed per country with evidence; A-R1…A-R4 PASS; 5-claim spot-check per country recorded; `validate.py` exits 0 for the set; ≥ 3 sources per verified country (V-50).
- **Deps:** P3-T11 (or, per continent, that continent's P3-Tn + P2-T13 if you accept later neighbour edits). **Size:** L → assign one continent per dispatch. **Reviewer unit.**

## 6. Phase 4 — City pilot: Deep Learning Basin (`research/06`)

Chosen because it is the densest and best-sourced file (82 numbered sources,
8 schools, ~30 timeline rows). The pilot's purpose is to learn what the
schema and process get wrong before 300–600 cities are written.

### P4-T1 — Coverage matrix Table 2 for `research/06`
- **Objective:** Decide, for every timeline row, key paper and key person in the file, whether it becomes a city, is folded into another city's card, or is dropped.
- **Inputs:** `research/06-…md`; `data/coverage/deep-learning-basin.md` (Table 1 from P3); `data/countries/*.yaml` with `parent_id: deep-learning-basin`; `SPEC.md` §2.2 (types), §2.8 (people rule), §4.4 A-M3, §5.4 (30–50 cities, 3–8 people), §6 item 6 (recognisability test).
- **Outputs:** Table 2 in `data/coverage/deep-learning-basin.md`: `source item | kind (timeline/paper/person) | decision (city | folded-into:<id> | dropped) | proposed city id | type | parent country id | reason`; a "batches" list assigning proposed city ids to P4-T2…T5 by parent country.
- **Check:** PASS if row count equals (timeline rows + key-paper bullets + key-person bullets) in the file (A-M3); 30 ≤ `city` decisions ≤ 50; 3 ≤ `type: person` ≤ 8; every `parent country id` exists; every `dropped` has a reason; proposed ids pass the V-03 regex and are unique.
- **Deps:** P3-T<basin> merged; P1-T6 merged (so the coverage review's additions are included). **Size:** M.

### P4-T2 … P4-T5 — Author cities for one country group (template unit, 4 batches)
Batches are defined in P4-T1's output. Suggested grouping by parent country: (T2) pre-training + speech converts; (T3) GPU ConvNet school; (T4) neural NLP + deep generative; (T5) deep RL + tooling guild + industrial-lab founders.
- **Objective:** Write every non-person city in the batch to `status: sourced`.
- **Inputs:** the batch's rows from Table 2; `research/06` timeline rows / paper bullets and their `[n]` sources; `SPEC.md` §2.1 (city column), §2.2, §2.10 city example, §4.4 A-T1…A-T4; `scripts/validate.py`.
- **Outputs:** `data/cities/deep-learning-basin/<id>.yaml` per row.
- **Check:** PASS if every row with decision `city` in the batch has a file; `validate.py --file` exits 0 for each (A-T1, V-30 directory rule); `time_range.start` precision matches the primary source (A-T3 — e.g. AlexNet `2012-09-30`, word2vec `2013-01-16`); ≥ 2 sources with ≥ 1 non-Wikipedia (pre-empting V-50 at verify); summary 30–150 words with no unsourced benchmark numbers (A-T4).
- **Deps:** P4-T1. **Size:** S each. **Parallel:** all four.

### P4-T6 — Person cities for the basin
- **Objective:** Write the 3–8 `type: person` cities decided in Table 2.
- **Inputs:** Table 2 person rows; `research/06` "Key people" section; `SPEC.md` §2.8, A-T5; Wikipedia articles via `scripts/wiki.sh`.
- **Outputs:** `data/cities/deep-learning-basin/<person-id>.yaml` per row.
- **Check:** PASS if each person has a Wikipedia article URL in `sources` and is named in `research/06` Key people (A-T5); placed under the country of their defining work with other affiliations in `summary`; `validate.py` clean; no person duplicated from another continent (grep `data/cities/*/` for the id stem).
- **Deps:** P4-T1. **Size:** S.

### P4-T7 — Pilot city review → `verified`
- **Objective:** Independent verification of all pilot cities and the coverage matrix.
- **Inputs:** `data/cities/deep-learning-basin/*.yaml`; `data/coverage/deep-learning-basin.md`; `SPEC.md` §4.4 (A-T1…A-T6, A-M1…A-M5), §4.5, §5.1, §5.4.
- **Outputs:** `data/reviews/YYYY-MM-DD-cities-deep-learning-basin.md`; `status: verified` + `verified_by` on passing cities; fixes.
- **Check:** PASS if A-T1…A-T6 per city and A-M1…A-M5 for the matrix are listed with evidence; A-R1…A-R4 PASS; `validate.py --require-children` exits 0 scoped to the basin (every basin country has ≥ 2 cities, §5.4); V-60 zero FAIL.
- **Deps:** P4-T2…T6. **Size:** M. **Reviewer unit.**

### P4-T8 — Pilot retrospective and SPEC change proposals
- **Objective:** Capture what the pilot taught before scaling to the other continents.
- **Inputs:** all P4 review reports and commit messages; `SPEC.md`.
- **Outputs:** `data/reviews/YYYY-MM-DD-pilot-retrospective.md` with sections: schema fields that were missing/unused; rules that were too strict/loose (by V-/A- id); time per city; recommended batch size; a list of proposed `SPEC:` commits (each a one-line change + rule ids affected); and a proposed instance list for the remaining nine continents' city phases (future `P4b-*` units, not yet scheduled).
- **Check:** PASS if every proposal names a rule id or §; every "unused field" claim is backed by a `grep -c` over `data/cities/`; the report is linked from `STATUS.md`.
- **Deps:** P4-T7. **Size:** S.

## 7. Phase 5 — Frontier intake (recurring, monthly)

> **DEFERRED — Alan has explicitly deprioritized monthly frontier intake indefinitely ("Let's not worry about monthly updates for now. Let's get the history and current correct."). Do not schedule or dispatch P5 units (P5-T0, P5-R1…R6) without new instruction.** The east edge of the map stays at the last row triangulated by P1-T10 (Sept 2026) until further notice.

One-time setup, then six sequential units per month. Each month's run is a
fresh instance: `P5-R1[2026-09]`, etc. Runs are independent across months
except for P5-R5 (aging) which reads the files from month−6 and month−12.

### P5-T0 — One-time setup
- **Objective:** Remove the known blockers to running the cadence.
- **Inputs:** `SOURCING.md` §1 probe notes (Semantic Scholar 429 without key; Anthropic/Meta/xAI/Microsoft have no bot-readable feed; smol.ai 402), §8 known gaps.
- **Outputs:** `SOURCING.md` §1 updated with a working Semantic Scholar key procedure (key itself in env, never committed) and a "manual checklist" subsection listing the exact URLs a human/agent opens for feedless labs; re-probe of every Tier-1/2 URL with today's status codes; `cs.RO` + CoRL added to Tier 1 per §8.
- **Check:** PASS if every Tier-1/2 row has a probe date within 30 days and a status code; the feedless-labs checklist has ≥ 4 entries with URLs that return < 400 in a browser-UA curl or are marked `manual-only`.
- **Deps:** G0. **Size:** S.

### P5-R1 — Collect (month M)
- **Objective:** Pull raw candidates for calendar month M from Tier-1 and Tier-2 sources.
- **Inputs:** `SOURCING.md` §1 (URLs), §2 step 1; month M.
- **Outputs:** `intake/M/raw.jsonl` (one JSON object per item: `source, url, title, date, snippet`) — **git-ignored**; `intake/M/collect.log` (committed: per-source item counts and HTTP status).
- **Check:** PASS if `collect.log` lists every Tier-1 and Tier-2 source with a count or an explicit `skipped: <reason>`; ≥ 1 item from ≥ 6 distinct sources; all `date`s fall in month M.
- **Deps:** P5-T0. **Size:** S (automatable).

### P5-R2 — Filter and triangulate
- **Objective:** Reduce raw items to 30–80 candidates and triangulate each.
- **Inputs:** `intake/M/raw.jsonl`; `SOURCING.md` §3 (filters), §4 (triangulation fields), §3 exclusions.
- **Outputs:** `intake/M/candidates.md` — table with every §4 column (Date, Who, Claim, Independent confirmation, Wikipedia status, Confidence) and a `filter_hit` column naming which §3 rule admitted it.
- **Check:** PASS if 30 ≤ rows ≤ 80 (or fewer with a note explaining a quiet month); every row has a `filter_hit`; every row with Confidence ≥ medium has ≥ 2 URLs; no row matches a §3 exclusion (funding round, pricing, minor version bump, etc.).
- **Deps:** P5-R1[M]. **Size:** S.

### P5-R3 — Write frontier file and draft cities
- **Objective:** Produce the month's research file and `draft` city entities for survivors.
- **Inputs:** `intake/M/candidates.md`; `SOURCING.md` §6 template; `SPEC.md` §4.1 R-08, §4.4 A-T6, §5.4 (frontier draft rule), §2.1; existing `data/countries/*.yaml` under the eastern continent(s) for `parent_id`; `scripts/validate.py`.
- **Outputs:** `research/frontier/M.md`; `data/cities/<eastern-continent>/<id>.yaml` at `status: draft` for each "New provisional" row (expect 0–8 per month); if a survivor has no suitable parent country, a `pending-country: <proposed name>` note in `research/frontier/M.md` "Notes" — **never** a new country in this unit.
- **Check:** PASS if R-01…R-05 and R-08 PASS for the frontier file; every new city passes A-T6 (≥ 1 primary/official + ≥ 1 independent) and `validate.py`; entity count ≤ 8 unless justified in the file; `time_range.start` inside month M.
- **Deps:** P5-R2[M]. **Size:** M.

### P5-R4 — Review
- **Objective:** 15-minute veto/add pass by Alan or a second model.
- **Inputs:** `research/frontier/M.md`; the new city files; `SPEC.md` §4.5.
- **Outputs:** `data/reviews/YYYY-MM-DD-frontier-M.md` (can be short); edits/removals.
- **Check:** PASS if A-R1…A-R4 PASS; reviewer ≠ author of P5-R3; every removed item is moved to `research/frontier/pruned.md` with a reason.
- **Deps:** P5-R3[M]. **Size:** S. **Reviewer unit.**

### P5-R5 — Aging (M−6 and M−12)
- **Objective:** Promote, keep or prune frontier cities from six and twelve months ago.
- **Inputs:** `research/frontier/<M−6>.md`, `<M−12>.md` (if they exist); the `draft` cities they created; `SOURCING.md` §5 (two-of-four promotion criteria); `SPEC.md` §5.1.
- **Outputs:** status changes (`draft → sourced`/`verified` with `verified_by`) or deletions with an appended row in `research/frontier/pruned.md`; the "Aging review" section of `research/frontier/M.md` filled.
- **Check:** PASS if every `draft` city whose `time_range.start` is in M−6 or M−12 has a row in the aging table with `Decision ∈ {promote, keep, prune}` and the two §5 criteria it met (for promote); pruned ids no longer exist under `data/` and appear in `pruned.md`; `validate.py` clean.
- **Deps:** P5-R4[M]. **Size:** S.

### P5-R6 — Commit and move the east edge
- **Objective:** Land the month atomically.
- **Inputs:** everything from P5-R1…R5[M].
- **Outputs:** one commit `frontier: M` on `main`; `STATUS.md` "east edge" line updated to M.
- **Check:** PASS if `git log --oneline -1` subject is exactly `frontier: M`; `validate.py` exits 0 on the whole `data/` tree; `scripts/check_links.sh research/frontier/M.md` `failed=0`.
- **Deps:** P5-R5[M]. **Size:** S.

## 8. Phase 6 — Quality and coverage review (distinct from authoring)

These units never author content. They audit what authoring produced and
either fix mechanically or file issues. Run after each phase's authoring
completes, and again before any render work begins.

### P6-T1 — Id, duplicate and consistency audit
- **Objective:** Catch the cross-file problems a per-file validator can't see.
- **Inputs:** whole `data/` tree; `scripts/validate.py`.
- **Outputs:** `data/reviews/YYYY-MM-DD-consistency.md` listing: near-duplicate names across levels/continents (normalised-string similarity > 0.85), the same person/system appearing under two continents, `research_ref` files that no entity points at, countries with `time_range` outside their parent without `time-overlap-ok:`, `mixed` biomes lacking a `notes` justification; mechanical fixes committed; judgement calls listed for a human.
- **Check:** PASS if `validate.py --require-children` exits 0 for the phases complete so far; the report's "judgement calls" section is empty or each item is linked to a `STATUS.md` known issue.
- **Deps:** P3-T11 (first run); repeat after P4-T7. **Size:** S.

### P6-T2 — Sibling-set placement review → `placed` (per continent)
- **Objective:** The curatorial pass `AXES.md` rule 2 asks for: look at all countries (and pilot cities) of one continent *together* and decide whether the neighbourhoods feel right.
- **Inputs:** one continent's countries (+ cities if authored); their `band`, `neighbours`, `biome`; the research file's map notes; `AXES.md` §0 rule 2, §3 "in practice"; `SPEC.md` §5.1 `placed`.
- **Outputs:** `data/reviews/YYYY-MM-DD-placement-<continent-id>.md` containing a text sketch (ASCII or list) of the continent by band with each country placed, the changes made (band spans, `band_override_note`s, neighbour relations), and `status: placed` on entities the reviewer accepts.
- **Check:** PASS if every country in the continent is in the sketch; every band change has a `band_override_note` ≥ 20 chars (V-09); V-50 `placed` requirements hold; the reviewer answers two recorded questions per continent: "Does a 1965/1990/2015/2025 vertical slice through this continent read as intellectual neighbours?" and "Would a mapofmetal visitor find this region's internal layout obvious?".
- **Deps:** that continent's P3-T12 (and P4-T7 for the basin). **Size:** M each. **Reviewer unit.**

### P6-T3 — Source audit
- **Objective:** Guard against factual drift and Wikipedia-only sourcing.
- **Inputs:** whole `data/` tree; `scripts/check_links.sh`; `scripts/link_allowlist.txt`.
- **Outputs:** `data/reviews/YYYY-MM-DD-sources.md`: link-rot list (URLs now ≥ 400 that were < 400), entities whose sources are 100 % `kind: wikipedia` at `status ≥ verified` (V-50 violation), allowlist entries older than 6 months to re-probe; status downgrades applied per `SPEC.md` §5.1.
- **Check:** PASS if `check_links.sh` over `data/ research/` reports `failed=0` after fixes; zero `verified` entities with Wikipedia-only sources; every allowlist line has a reason comment.
- **Deps:** any authoring phase complete. **Size:** S. Repeatable.

### P6-T4 — Summary claim sampling audit
- **Objective:** Statistically check that `summary` text is actually supported by `sources`, beyond the 5-claim spot-checks done at verification.
- **Inputs:** random sample of 10 % of entities at `status ≥ verified` (seeded RNG, seed recorded); their sources; `scripts/wiki.sh`.
- **Outputs:** `data/reviews/YYYY-MM-DD-claims-audit.md`: per sampled entity, every date/name/number in `summary` with `supported by source #n` or `UNSUPPORTED`; fixes committed; failure rate.
- **Check:** PASS if unsupported-claim rate ≤ 2 % of checked claims; every UNSUPPORTED has a fix commit or a status downgrade; sample list and seed recorded so it can be re-run.
- **Deps:** P2-T13 (first run); repeat after P3-T12 and P4-T7. **Size:** M. **Reviewer unit.**

### P6-T5 — STATUS.md refresh
- **Objective:** Keep the project's single status page honest.
- **Inputs:** all review reports since the last refresh; `validate.py` summary counts; `git log`.
- **Outputs:** `STATUS.md` updated: entity counts by level and status (from `validate.py --summary`), phases complete, open known issues (each linked to a review report), east-edge month, next units ready to dispatch.
- **Check:** PASS if every count in `STATUS.md` equals the validator's output on the same commit (paste both); every known issue links to a report or unit id; no "decisions Alan needs to make" entry that is already recorded as decided in `AXES.md`/`ALTITUDES.md`/`SPEC.md`.
- **Deps:** P6-T1…T4 of the current cycle. **Size:** S.

## 9. What is deliberately NOT in this plan

- Render/frontend/style work (Phase 4 of `PROJECT_PLAN.md`) — blocked on the
  content phases above and on a separate visual spec that does not exist yet.
- City authoring for the nine non-pilot continents — scheduled only after
  P4-T8 produces the instance list, because the pilot may change the schema.
- Voice/copy-edit pass across research files (`SPEC.md` §6 item 8).
- Street level / citation-graph projection (Phase 5+ idea in `STATUS.md`).

## 10. Dispatch checklist (copy into any subagent prompt)

```
Unit: <id>  (from PLAN.md)
Read first: SPEC.md (all), PLAN.md §<phase> entry for this unit, then the Inputs listed.
Produce only the Outputs listed. Do not create or edit other files.
Before finishing: run the Check exactly as written; paste the command(s) and
output into the commit body; list each SPEC rule/criterion id as PASS/FAIL.
Author may set status ≤ sourced. Do not set verified/placed unless you are the
designated reviewer and are not the git author of the file.
Commit subject: "<id>: <one line>". Push to main.
If SPEC.md cannot represent something you found, stop and write the gap in
the commit body under "SPEC gap:" rather than inventing a field.
```
