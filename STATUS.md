# STATUS — as of 2026-09-06 (session 2: spec + plan)

## One-line status

Framework decided, `SPEC.md` and `PLAN.md` written. **Ready to execute,
awaiting Alan's go-ahead (gate G0 in `PLAN.md`).** No execution work
(research edits, `data/` entities, scripts) happened this session, by
design.

## Where to look

| Question | File |
|---|---|
| What is this project? | `BRIEF.md` (Alan's intent), `README.md` |
| What are the coordinates? | `AXES.md` — **decided** |
| What are the zoom levels? | `ALTITUDES.md` — **decided** |
| What does "correct" look like for any artifact? | `SPEC.md` — normative; schema, validation rules `V-nn`, acceptance criteria `R-nn` / `A-xx`, status lifecycle, DoD per level, non-goals |
| What is the work, in what order, who can do it in parallel? | `PLAN.md` — 31 unit templates (~70 dispatchable instances), DAG + waves, dispatch checklist |
| Where do frontier sources come from? | `SOURCING.md` |
| Historical plan (goal, risks, render sketch) | `PROJECT_PLAN.md` — task breakdown superseded by `PLAN.md` |

## Decisions (recorded; do not re-open)

| # | Decision | Status | Where recorded |
|---|---|---|---|
| 1 | **Y axis = Candidate E** (reasoning ↔ embodiment), five bands N1/N2/C/S1/S2, symbolic ↔ learned as biome, open ↔ closed as eastern overlay. **Bands are soft**: a clustering guideline, not a scoring formula; neighbourhood and curatorial appeal beat band purity. | **Confirmed** by Alan | `AXES.md` §0 rule 2, §3, §5 |
| 2 | **X mainland starts 1943** (McCulloch–Pitts); pre-1943 (Turing 1936, Gödel, Boole, Leibniz…) is an offshore archipelago. | **Confirmed** by Alan | `AXES.md` §1, §5 |
| 3 | **Three altitudes: continent / country / city.** No street level. Major individual figures (Hassabis, Ng, Hinton…) are `type: person` cities. | **Confirmed** by Alan | `ALTITUDES.md` §0–§5, §8; `SPEC.md` §2.8 |
| 4 | **Naming: evocative region name + neutral subtitle** for continents and countries ("The Statistical Isthmus" / "Bayesian & probabilistic ML, 1988–2011"). Cities use plain names + date. | **Confirmed** by Alan | `ALTITUDES.md` §0; `SPEC.md` §2.3, V-12 |
| 5 | **Scope edge: adjacent fields case-by-case only.** Control theory, cognitive science, OR, HCI etc. get no territory; a specific person/paper/event is included only when it directly fed an AI milestone, tagged `adjacent_field: {field, fed}`. | **Soft default** — relayed on Alan's behalf without an explicit answer. Revisit if wrong; changing it touches only `SPEC.md` §2.9 and rule V-40. | `SPEC.md` §2.9, §6 item 7 |
| 6 | X scale (piecewise vs density-weighted) | Deferred to render phase; does not block content | `AXES.md` §5 |
| 7 | Frontier review sign-off | Open, low-stakes: `PLAN.md` P5-R4 accepts "Alan or a second model" | `PLAN.md` §7 |

## What exists in the repo

| File | State | Notes |
|---|---|---|
| `BRIEF.md` | Alan's verbatim intent | unchanged |
| `AXES.md` | decided | X origin + non-linear scale; Y = E soft bands; decision record table in §5 |
| `ALTITUDES.md` | decided | 3 levels; people at city; data-model sketch removed in favour of `SPEC.md` |
| `SPEC.md` | normative, v1 | see "Where to look" |
| `PLAN.md` | ready, gated on G0 | see "Where to look" |
| `PROJECT_PLAN.md` | partially superseded | §3–§4 task breakdown replaced by `PLAN.md`; goal/risks/render sketch still valid |
| `SOURCING.md` | draft; endpoints probed | 3 source tiers with live curl status, monthly cadence, filters, triangulation, aging |
| `research/01`–`08` | **verified** (links) / first-draft (coverage) | 8 era files, ~1,250 lines, 10–30 timeline rows each, numbered sources |
| `research/09-cross-cutting-threads.md` | verified (links) | 8 threads with dated milestones |
| `research/TEMPLATE.md` | stable | template every era file follows |
| `scripts/check_links.sh` | working | 737 URLs checked; 0 failures outside the documented allowlist |
| `scripts/wiki.sh` | working, no back-off | Wikipedia 429s after ~25 rapid calls — fixed by `PLAN.md` P0-T1 |
| `scripts/link_allowlist.txt` | | URLs known to block bots or template/API URLs |
| `data/` | **does not exist yet** | created by `PLAN.md` P2 onwards, per `SPEC.md` §1 |
| `scripts/validate.py` | **does not exist yet** | `PLAN.md` P0-T2 |

Commits are incremental on `main`; nothing is uncommitted.

## What "verified" means here, honestly

- **Verified (research files):** every URL resolves (HTTP < 400) and the
  writing agent cross-checked each date/name against the fetched Wikipedia
  extract or primary paper before writing it.
- **Not yet verified:** *coverage*. Nobody has asked "what important thing is
  missing from this era?" — that is `PLAN.md` P1-T1…T9, to be done by a
  different model than the authors (`SPEC.md` R-07).
- **Provisional:** `research/08` has a "Needs verification (mid-2025 →
  Sept 2026)" section, single-sourced. `PLAN.md` P1-T10 triangulates it.
- Going forward, "verified" for entities has the precise meaning in
  `SPEC.md` §5.1 (reviewer ≠ author, source minimums, V-50).

## What happens when Alan says go

`PLAN.md` wave 0 dispatches immediately and in parallel: P0-T1 (wiki.sh
back-off), P0-T2 (validate.py), P1-T11 (research/01 archipelago split note).
Wave 1 then fans out to nine parallel research coverage reviews plus the
continent registry (P2-T1). Critical path to the first drawable content is
G0 → P0-T2 → P2-T1 → continents → basin countries → basin city pilot →
retrospective (P4-T8), which is where the schema gets its first real
correction before scaling to the other nine continents.

Alan can also override anything in `SPEC.md` first; the plan says to apply
that as a `SPEC:` commit before re-reading affected units.

## Ideas noted, NOT scope

- **Street level via citation-graph projection (Phase 5+).** Instead of
  hand-curating thousands of paper/model/person entities, project an
  external graph (Semantic Scholar / OpenAlex / Connected Papers / Papers
  with Code lineage) onto a fourth zoom level anchored at our city ids. The
  only preparation being made now is that every city carries `sources`
  (ideally a DOI/arXiv id) so a future join key exists. Not committed.
- Voice/copy-edit pass to unify research files (later; `SPEC.md` §6 item 8).
- Render/frontend (Phase 4 in `PROJECT_PLAN.md`) — blocked on content and on
  a visual spec that does not exist yet. The engine sketch below still stands.

## How the visual map would eventually be built (plan only, not started)

- **Content → data.** Markdown research stays the human-readable source of
  truth; `data/` YAML entities (schema in `SPEC.md`) carry time range, band,
  biome, parent, sources, status. `validate.py` enforces `SPEC.md` §3.
- **Layout.** Continent/country polygons hand-drawn by the curator; city
  points placed inside their parent by the curator; an automated relaxation
  step only removes overlaps. Algorithms nudge; humans decide neighbourhood.
- **Terrain.** Biome polygons plus noise, hillshade and coastline rendered
  offline into a raster tile pyramid, one per altitude range.
- **Engine.** MapLibre GL JS with a custom style; fallback Leaflet + image
  pyramid.
- **Interaction.** Click region → side panel; click city → card with summary,
  dates, sources; search; year slider; thread and open/closed toggles;
  "frontier haze" for `draft` entities.
- **Delivery.** Static build to GitHub Pages; monthly `frontier:` commits
  trigger a rebuild.

## Known issues / tooling notes

- `scripts/wiki.sh` has no back-off (→ P0-T1).
- Publisher DOI landing pages (ACM, OUP, MIT Press, Science, AAAI) return 403
  to curl; files cite the DOI as text and link an open mirror or Wikipedia.
- OpenReview API is 403 to bots; Semantic Scholar 429s without a key;
  Anthropic / Meta / xAI / Microsoft have no bot-readable feed (→ P5-T0).
- One subagent run crashed after writing `research/04` in session 1 (file
  complete and passing checks) — no content lost.
