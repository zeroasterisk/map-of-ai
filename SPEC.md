# SPEC — Map of AI, content and data specification

> **Status: normative.** This document defines what "correct" means for every
> content artifact in this repository. A reader with no conversation history
> should be able to pick any task in `PLAN.md`, read this file, do the work,
> and know — by running the checks in §7 — whether it is done.
>
> Decisions it encodes (all confirmed by Alan on 2026-09-06 unless marked):
> X mainland starts 1943 with a pre-1943 archipelago (`AXES.md` §1); Y is the
> reasoning ↔ embodiment gradient in five *soft* bands (`AXES.md` §0 rule 2,
> §3); three altitudes — continent / country / city — with people at city
> level (`ALTITUDES.md`); evocative names with neutral subtitles; adjacent
> fields included case-by-case only (§2.9 — *default, revisit if wrong*).
>
> Every rule that a checker can enforce has an ID (`V-nn` for data
> validation, `R-nn` for research files, `A-nn` for acceptance criteria).
> `PLAN.md` references these IDs; do not renumber them.

## 0. Vocabulary

| Term | Meaning |
|---|---|
| **Entity** | One YAML file under `data/` describing a continent, country or city. The unit of content. |
| **Level** | `continent`, `country`, or `city`. Formerly A1/A2/A3. An entity has exactly one level. |
| **Band** | One of five soft north–south neighbourhoods: `N1` philosophy & foundations, `N2` logic/knowledge/reasoning, `C` language & communication, `S1` planning/search/decision/games, `S2` perception/control/embodiment. A *hint*, not a coordinate. |
| **Biome** | Terrain colour encoding methodology (symbolic ↔ learned). See §2.6. |
| **Research file** | `research/0N-*.md` or `research/09-*.md`: the human-readable, sourced compendium. Entities are *derived from* research files and cite back into them. |
| **Frontier** | Content dated within the last ~12 months, sourced via `SOURCING.md`; renders with "haze". |
| **Coverage matrix** | A markdown table proving that every candidate item in a research file was either turned into an entity, folded into another entity's card, or dropped with a reason. See §4.4. |
| **Reviewer** | A different agent, model, or human than the author of the artifact under review. Author ≠ reviewer is a hard rule for the `verified` status. |

## 1. Repository layout (normative for `data/`; other dirs already exist)

```
BRIEF.md  AXES.md  ALTITUDES.md  SOURCING.md  SPEC.md  PLAN.md  STATUS.md
research/
  01-…09-*.md            era files + cross-cutting threads (exist)
  TEMPLATE.md            research-file template (exists)
  frontier/YYYY-MM.md    monthly intake files (per SOURCING.md §6)
  frontier/pruned.md     items rejected during aging, with reasons
data/
  continents/<id>.yaml   one file per continent
  countries/<id>.yaml    one file per country
  cities/<continent-id>/<id>.yaml   one file per city, grouped by continent
  coverage/<continent-id>.md        coverage matrix per continent (§4.4)
  reviews/YYYY-MM-DD-<scope>.md     review reports (§4.5)
scripts/
  check_links.sh  link_allowlist.txt  wiki.sh   (exist)
  validate.py     entity validator implementing §3 (does not exist yet; PLAN P0-T2)
```

One entity per file. File name equals the entity `id` plus `.yaml`. No entity
may be defined in two files.

## 2. Data model

### 2.1 Entity schema

All fields, all levels. "Req" column: **R** required at every status; **P**
required once status ≥ `placed`; **V** required once status ≥ `verified`;
**O** optional; **–** not allowed at this level.

| Field | Type | continent | country | city | Notes |
|---|---|---|---|---|---|
| `id` | string, `^[a-z0-9]+(-[a-z0-9]+)*$`, ≤ 48 chars | R | R | R | Globally unique across all levels. Stable forever; never reuse. Cities disambiguate with a year suffix when the name alone is ambiguous (`perceptron-1958`, `alphago-2016`). |
| `level` | enum `continent\|country\|city` | R | R | R | Must match the directory the file lives in. |
| `type` | enum, see §2.2 | – | – | R | City kind; selects icon. |
| `name` | string, 2–60 chars | R | R | R | Evocative for continent/country (§2.3). Plain recognisable name for city. |
| `subtitle` | string, 10–90 chars | R | R | R | Neutral description. Continent/country: `"<what it is>, <start>–<end>"`. City: `"<one-line what>, <year>"`. |
| `summary` | string (markdown allowed) | R | R | R | The click-through write-up. Word limits: continent 120–300, country 80–220, city 30–150. Every date, name, and number in it must be supported by an entry in `sources`. |
| `time_range.start` | int year, or `YYYY-MM`, or `YYYY-MM-DD` | R | R | R | X anchor. Continents/countries: year granularity is fine. Cities: as precise as the primary source allows. |
| `time_range.end` | int year / `YYYY-MM` / `YYYY-MM-DD` / literal `present` | R | R | R | Point-in-time cities set `end` equal to `start`. `present` only for things still operating (labs, institutions, living people's tenure). |
| `offshore` | bool | O | – | – | `true` only for the pre-1943 archipelago continent(s). Default false. |
| `band` | enum `N1\|N2\|C\|S1\|S2`, **or** list of 2–5 of those | R | R | R | A list is an explicit multi-band span and must be contiguous in the order N1, N2, C, S1, S2 (e.g. `[N2, C]` ok; `[N1, S2]` not ok). Home neighbourhood, not a coordinate (`AXES.md` rule 2). |
| `band_override_note` | string | O | O | O | Required **iff** the entity is deliberately placed off its "pure" band to keep it next to its intellectual neighbours. Says why. |
| `biome` | enum, see §2.6 | R | R | O | Cities inherit the parent's biome when omitted. |
| `parent_id` | string (an existing `id`) | – | R | R | Country → a continent id. City → a country id. Exactly one parent. |
| `research_ref.file` | path under `research/` | R | R | O | The research file this entity is derived from. Frontier cities use `research/frontier/YYYY-MM.md`. |
| `research_ref.sources` | list of ints | R | R | O | Numbered `[n]` sources in that file that support this entity. ≥ 1 if `research_ref` present. |
| `sources` | list of source objects (§2.4) | R (≥ 3) | R (≥ 2) | R (≥ 1) | Verified status raises the minimum (§5). |
| `threads` | list of enum, see §2.7 | O | O | O | Which cross-cutting river/road passes through. |
| `neighbours` | list of neighbour objects (§2.5) | O | P (≥ 1) | O | Curatorial locality: who borders whom. |
| `adjacent_field` | object `{field: string, fed: id}` | – | O | O | Required iff the entity is from outside AI proper (§2.9). `fed` must be an existing entity id. |
| `status` | enum `draft\|sourced\|verified\|placed` | R | R | R | See §5 for what each means and requires. |
| `verified_by` | object `{who: string, date: YYYY-MM-DD, method: string}` | V | V | V | `who` must differ from the author recorded in git for the file's first commit. |
| `notes` | string | O | O | O | Curatorial notes, open questions, disputed priority claims. Free text; not rendered. |

Unknown fields are a validation error (`V-01`); extend this table first.

### 2.2 City `type` enum

| `type` | What | Icon intent |
|---|---|---|
| `lab` | Lab, group, company research org | star / capital |
| `system` | Landmark system or model (Logic Theorist, AlexNet, GPT-3, AlphaFold 2). Model *families* are one `system` city whose card lists versions. | filled circle |
| `paper` | Landmark paper or book | open circle / book |
| `event` | Conference occurrence, match, report, launch, prize | flag |
| `dataset` | Dataset, benchmark, competition | anchor / harbour |
| `institution` | Recurring venue or standing body (NeurIPS, AAAI, ICOT) | town hall |
| `person` | Major individual figure (§2.8) | monument |

### 2.3 Naming rules (continent and country)

- `name` is evocative and cartographic: "The Statistical Isthmus", "Winter
  Steppes", "The Perceptron Strip". Not a textbook heading.
- `subtitle` is neutral and dated: "Bayesian & probabilistic machine
  learning, 1988–2011". A reader who dislikes whimsy gets the plain fact from
  the subtitle alone.
- Checkable form: `subtitle` matches `^.+, \d{4}(–(\d{4}|present))?$` and
  the years in it equal `time_range.start`/`time_range.end` at year
  granularity (`V-12`).
- Names must be unique within a level (`V-13`).
- Cities: `name` is the recognisable name ("AlexNet", "Dartmouth 1956",
  "Geoffrey Hinton"); `subtitle` is `"<what>, <year>"`.

### 2.4 Source object

```yaml
- url: https://en.wikipedia.org/wiki/AlexNet
  title: "Wikipedia: AlexNet"
  kind: wikipedia          # wikipedia | primary | secondary | official
  accessed: 2026-09-06
```

- `kind`: `primary` = the paper/report/code itself; `official` = the
  authoring org's own page (lab blog, press release); `secondary` = a
  history, survey, newsletter, encyclopaedia other than Wikipedia.
- Every URL must return HTTP < 400 via `scripts/check_links.sh` or be listed
  in `scripts/link_allowlist.txt` with a reason (`V-20`).
- No invented URLs. If a DOI landing page blocks bots, cite the DOI in
  `title` and link an open mirror or Wikipedia (this is what the research
  files already do).

### 2.5 Neighbour object

```yaml
- id: logic-based-ai-neats
  relation: borders       # borders | bridge | wall | river | road
  note: "north bank of the Search river; Newell–Simon vs McCarthy"
```

`id` must exist (`V-30`). Relations are directional from this entity;
reciprocity is encouraged, not required. `wall` = a documented cut-off
(*Perceptrons* 1969, the 1974 winter cliff). `bridge` = a lineage handoff to
a later school. These come straight from the research files' `borders:`
clauses and map notes.

### 2.6 Biome enum

| `biome` | Meaning (from `AXES.md` §3) |
|---|---|
| `highland` | hand-authored logic and knowledge (symbolic) |
| `grassland` | probabilistic / statistical models with explicit structure |
| `forest` | learned neural representations |
| `jungle` | scaled self-supervised / foundation models |
| `wetland` | reinforcement learning and control |
| `harbour` | benchmarks, datasets, competitions, tooling, venues |
| `mixed` | genuinely hybrid (neurosymbolic, AlphaGo's MCTS + nets); use sparingly and say why in `notes` |

### 2.7 Thread enum

From `research/09-cross-cutting-threads.md`: `rl`, `robotics`, `safety`,
`compute`, `open-closed`, `language`, `vision`, `games`.

### 2.8 People

People are **city-level entities of `type: person`**, major figures only.
Test: the person has a Wikipedia article and is named in at least one
research file's "Key people" section. Place the person inside the country of
their *defining* work; record moves and other affiliations in `summary`, not
as duplicate entities. Target density: 3–8 people per continent, not per
country. Minor contributors stay as names inside other cities' `summary`.

### 2.9 Scope edge — adjacent fields (DEFAULT, revisit if wrong)

Control theory, cybernetics-as-engineering, operations research, cognitive
science, neuroscience, HCI, statistics, and pure theory of computation are
**not** given their own territories. A specific person, paper or event from
such a field is included **only** when it directly fed an AI milestone, and
the entity must carry `adjacent_field: {field: …, fed: <entity id>}` naming
what it fed (`V-40`). Examples: Wiener's *Cybernetics* (1948) → in, feeds
the cybernetic shore and Shakey; "control theory" as a field → out. This
default was relayed on Alan's behalf without an explicit answer and is
flagged as such in `STATUS.md`; if Alan overrides it, only §2.9 and `V-40`
change.

### 2.10 Worked examples

Continent (`data/continents/deep-learning-basin.yaml`):

```yaml
id: deep-learning-basin
level: continent
name: The Deep Learning Basin
subtitle: "GPU-trained neural networks take over perception, language and control, 2006–2017"
summary: >
  Between 2006 and 2017 multi-layer neural networks went from an unfashionable
  niche to the default method for perception, language and control … (120–300 words)
time_range: {start: 2006, end: 2017}
band: [N2, C, S1, S2]
biome: forest
research_ref: {file: research/06-deep-learning-revolution-2006-2017.md, sources: [1, 17, 18, 38]}
sources:
  - {url: https://en.wikipedia.org/wiki/Deep_learning, title: "Wikipedia: Deep learning", kind: wikipedia, accessed: 2026-09-06}
  - {url: https://www.nature.com/articles/nature14539, title: "LeCun, Bengio & Hinton, Deep learning, Nature 2015", kind: primary, accessed: 2026-09-06}
  - {url: https://en.wikipedia.org/wiki/AlexNet, title: "Wikipedia: AlexNet", kind: wikipedia, accessed: 2026-09-06}
threads: [vision, language, rl, compute]
neighbours:
  - {id: statistical-isthmus, relation: wall, note: "ILSVRC 2012 fault line: hand-crafted features west, learned features east"}
  - {id: transformer-plateau, relation: bridge, note: "Attention Is All You Need, 12 Jun 2017"}
status: sourced
notes: "Schmidhuber/IDSIA priority claims vs AlexNet are a live dispute; see research/06 open question 2."
```

Country (`data/countries/gpu-convnet-school.yaml`):

```yaml
id: gpu-convnet-school
level: country
name: The ImageNet Escarpment
subtitle: "GPU-trained convolutional networks for vision, 2009–2015"
summary: >
  Stanford (Raina/Ng), IDSIA (Cireşan/Schmidhuber), Toronto (AlexNet), Oxford (VGG), Google (Inception) and MSRA (ResNet) … (80–220 words)
time_range: {start: 2009, end: 2015}
band: S2
biome: forest
parent_id: deep-learning-basin
research_ref: {file: research/06-deep-learning-revolution-2006-2017.md, sources: [6, 12, 13, 17, 33, 34, 42]}
sources:
  - {url: https://en.wikipedia.org/wiki/ImageNet_Large_Scale_Visual_Recognition_Challenge, title: "Wikipedia: ILSVRC", kind: wikipedia, accessed: 2026-09-06}
  - {url: https://arxiv.org/abs/1512.03385, title: "He et al., Deep Residual Learning, 2015", kind: primary, accessed: 2026-09-06}
threads: [vision, compute]
neighbours:
  - {id: convnets-bell-labs, relation: bridge, note: "LeNet/Neocognitron lineage from the Connectionist Revival"}
  - {id: neural-nlp-sequence-school, relation: borders, note: "shares the Silicon River"}
status: sourced
```

City (`data/cities/deep-learning-basin/alexnet-2012.yaml`):

```yaml
id: alexnet-2012
level: city
type: system
name: AlexNet
subtitle: "Wins ILSVRC 2012 with 15.3% top-5 error, 2012"
summary: >
  Krizhevsky, Sutskever and Hinton's eight-layer convolutional network … (30–150 words)
time_range: {start: 2012-09-30, end: 2012-09-30}
band: S2
parent_id: gpu-convnet-school
research_ref: {file: research/06-deep-learning-revolution-2006-2017.md, sources: [17, 18]}
sources:
  - {url: https://proceedings.neurips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html, title: "Krizhevsky, Sutskever & Hinton, NIPS 2012", kind: primary, accessed: 2026-09-06}
  - {url: https://en.wikipedia.org/wiki/AlexNet, title: "Wikipedia: AlexNet", kind: wikipedia, accessed: 2026-09-06}
threads: [vision, compute]
status: verified
verified_by: {who: "reviewer-model-B", date: 2026-09-20, method: "checked date, error rate and authors against both sources"}
```

## 3. Validation rules (mechanical; `scripts/validate.py` must implement all)

The validator reads every `data/**/*.yaml`, applies every rule, prints one
line per violation as `FAIL <rule> <file> <message>`, prints a summary, and
exits 1 on any FAIL. Rules marked (net) need network and are skippable with
`--offline`; everything else is pure.

| ID | Rule |
|---|---|
| V-01 | File parses as YAML into a mapping; no keys outside §2.1; every field present has the declared type. |
| V-02 | Every field marked **R** for the entity's level is present and non-empty. |
| V-03 | `id` matches the regex, equals the file basename, and is unique across all of `data/`. |
| V-04 | `level` matches the directory (`continents/`, `countries/`, `cities/`). |
| V-05 | `type` present iff `level == city`, and is in the §2.2 enum. |
| V-06 | `time_range.start` ≤ `time_range.end` (treat `present` as +∞); formats valid. |
| V-07 | For countries and cities: `time_range` lies within the parent's `time_range` **or** `notes` contains the token `time-overlap-ok:` followed by a reason (continents deliberately overlap; children spilling over a border are allowed but must be deliberate). |
| V-08 | `band` is a single enum value or a contiguous list of 2–5 in N1→N2→C→S1→S2 order. |
| V-09 | `band_override_note`, if present, is ≥ 20 chars. |
| V-10 | `biome` in §2.6 enum; present for continent and country. |
| V-11 | `summary` word count within the level's range (§2.1). |
| V-12 | Continent/country `subtitle` matches `^.+, \d{4}(–(\d{4}\|present))?$` and its years equal `time_range` at year granularity. |
| V-13 | `name` unique within the level. |
| V-14 | `offshore` present only on continents; if `offshore: true` then `time_range.end` ≤ 1943. |
| V-20 | (net) Every `sources[].url` returns HTTP < 400 via `scripts/check_links.sh`, or is in `scripts/link_allowlist.txt`. |
| V-21 | `sources` length ≥ level minimum (continent 3, country 2, city 1); each source has `url`, `title`, `kind` (enum), `accessed` (date). |
| V-22 | `research_ref.file` exists on disk; each int in `research_ref.sources` matches a `[n]` entry in that file's `## Sources` section. |
| V-30 | `parent_id` exists, is one level up (city→country, country→continent), and cities live in `data/cities/<grandparent continent id>/`. |
| V-31 | Every `neighbours[].id` exists; `relation` in enum; no self-reference. |
| V-32 | Every continent has ≥ 1 country and every country has ≥ 1 city **once the relevant PLAN phase is complete** (validator flag `--require-children` turns this on; off by default so partial progress validates). |
| V-33 | No cycles; the parent graph is a forest rooted at continents. |
| V-40 | If `adjacent_field` present: `field` non-empty and `fed` is an existing entity id ≠ self. |
| V-50 | `status` in enum; the fields required at that status (§5) are present: `placed` ⇒ country has ≥ 1 neighbour; `verified` ⇒ `verified_by` present with valid date and `who` ≠ git author of the file's first commit; `verified` city ⇒ ≥ 2 sources with ≥ 1 of kind ≠ `wikipedia`; `verified` country/continent ⇒ ≥ 3 sources. |
| V-51 | `threads[]` values in §2.7 enum, no duplicates. |
| V-60 | Every city id in a coverage matrix (§4.4) exists, and every city under `data/cities/<c>/` appears in `data/coverage/<c>.md`. |

Until `validate.py` exists, a unit of work is checked by hand against this
table and the checker records "manual V-check, rules V-01…V-60, date, who" in
the PR/commit message. The plan front-loads building the validator (P0-T2)
so that period is short.

## 4. Acceptance criteria per artifact type (binary pass/fail)

Each criterion is either PASS or FAIL. An artifact is accepted only when
every criterion for its type passes. "Reviewer" means author ≠ reviewer.

### 4.1 Research file `research/0N-*.md` (existing) and `research/frontier/YYYY-MM.md`

| ID | PASS when |
|---|---|
| R-01 | File follows `research/TEMPLATE.md` section order; every `##` heading in the template is present. |
| R-02 | Frontmatter `Status:` is one of `draft`, `verified`, `reviewed` and matches reality: `verified` ⇒ R-03…R-06 pass; `reviewed` ⇒ additionally R-07 passes. |
| R-03 | `scripts/check_links.sh <file>` reports `failed=0`. |
| R-04 | Every timeline row has a non-empty Source cell; every `[n]` used anywhere in the file resolves to an entry in `## Sources`; no `## Sources` entry is unreferenced. |
| R-05 | Every `## Sources` entry has ≥ 1 URL and an `(accessed YYYY-MM-DD)` date. |
| R-06 | `## Schools of thought` has ≥ 3 bullets and every bullet contains a `borders:` clause. |
| R-07 | A review report (§4.5) exists for this file with ≥ 10 candidate omissions considered, each marked `added` / `folded` / `rejected` with a one-line reason, and every `added` item is now present in the file with a source. |
| R-08 | (frontier files only) Follows `SOURCING.md` §6 template; every new-entry row has both a Primary and an Independent source column filled, and a Confidence value; the "Aging review" section names the files for month−6 and month−12 or states they don't exist yet. |

### 4.2 Continent entity

| ID | PASS when |
|---|---|
| A-C1 | `validate.py` reports zero FAIL for the file (or manual V-check recorded). |
| A-C2 | `name` and `subtitle` satisfy §2.3 (V-12, V-13) **and** a reviewer has answered "yes" to "would a visitor understand what this region is from the subtitle alone?" (recorded in the review report). |
| A-C3 | `summary` is 120–300 words and every year and proper noun in it can be found in at least one listed source (reviewer spot-checks 5; all 5 must pass). |
| A-C4 | `research_ref` points at exactly one era file and lists ≥ 3 source numbers from it. |
| A-C5 | `band` reflects the era file's "Map placement" line translated per `AXES.md` §3 point 2 (symbolic pole → N2; connectionist pole → S2 or C; mixed → span). Reviewer confirms. |
| A-C6 | `neighbours` names the west and east neighbours (or `offshore: true` / eastern coast for the ends) with the relation and note taken from the era file's map notes. |
| A-C7 | Appears in `data/coverage/<id>.md` header with its research file and school count. |

### 4.3 Country entity

| ID | PASS when |
|---|---|
| A-K1 | `validate.py` zero FAIL (or manual V-check). |
| A-K2 | Derived from exactly one bullet (or an explicitly documented merge of bullets) in a research file's `## Schools of thought` section; the coverage matrix row says so. |
| A-K3 | `parent_id` is the continent derived from the same research file (or the coverage matrix documents why it moved). |
| A-K4 | `neighbours` contains every school named in the source bullet's `borders:` clause that exists as an entity, with a relation. Schools that don't exist yet are listed in `notes` as `pending-neighbour: <name>`. |
| A-K5 | `summary` is 80–220 words, mentions the 2–5 defining people/systems, and passes the 5-claim reviewer spot-check. |
| A-K6 | `name`/`subtitle` satisfy §2.3 and the reviewer "understand from subtitle alone" test. |
| A-K7 | `band` is the single band or contiguous span a reviewer agrees "feels like the right neighbourhood" (`AXES.md` rule 2). Disagreement is resolved by the reviewer writing `band_override_note`, not by blocking. |

### 4.4 City entity and coverage matrix

| ID | PASS when |
|---|---|
| A-T1 | `validate.py` zero FAIL (or manual V-check). |
| A-T2 | The city corresponds to a row in the parent continent's coverage matrix `data/coverage/<continent-id>.md` with decision `city`. |
| A-T3 | `time_range.start` matches the date in the primary source to the precision given there; reviewer checks. |
| A-T4 | `summary` 30–150 words; says what it is, who did it, why it matters; no benchmark number without a source of kind `primary` or `secondary`. |
| A-T5 | `type: person` entities meet §2.8 (Wikipedia article exists; named in a research file's Key people). |
| A-T6 | For frontier cities (start within 12 months of authoring): `status` is `draft`, ≥ 1 source of kind `primary` or `official` **and** ≥ 1 independent source per `SOURCING.md` §4. |

**Coverage matrix** `data/coverage/<continent-id>.md` — PASS when:

| ID | PASS when |
|---|---|
| A-M1 | Header lists the continent id, the research file, and the date. |
| A-M2 | Table 1 has one row per bullet in the research file's `## Schools of thought` with columns `school bullet → decision (country \| merged-into:<id> \| dropped) → entity id → reason`. Row count equals bullet count. |
| A-M3 | Table 2 has one row per timeline row, key-paper bullet, and key-person bullet in the research file, with decision `city \| folded-into:<id> \| dropped` and a reason for `dropped`. Row count equals source item count. |
| A-M4 | Every `city` / `country` decision names an entity id that exists (V-60). |
| A-M5 | Every `folded-into` target's `summary` actually mentions the folded item (reviewer spot-checks 5). |

### 4.5 Review report `data/reviews/YYYY-MM-DD-<scope>.md`

| ID | PASS when |
|---|---|
| A-R1 | Header names scope (file or entity ids), reviewer identity (model/person), date, and the exact commit SHA reviewed. |
| A-R2 | Reviewer ≠ author (per git log of the reviewed files). |
| A-R3 | Every criterion from §4.1–§4.4 applicable to the scope is listed with PASS/FAIL and a one-line evidence note. |
| A-R4 | Every FAIL has a follow-up: a commit SHA that fixes it, or an entry in `STATUS.md` "Known issues". |
| A-R5 | For coverage reviews (R-07): ≥ 10 candidate omissions listed with disposition. |

## 5. Status lifecycle and Definition of Done per level

### 5.1 Status values (all levels)

| `status` | Means | Requires (checked by V-50) |
|---|---|---|
| `draft` | Schema-valid; content may be single-sourced or frontier. Renders with haze. | All **R** fields; ≥ 1 source. |
| `sourced` | Author asserts every claim in `summary` traces to a listed source and all URLs resolve. | `draft` + V-20 passes + level source minimum (§2.1). |
| `verified` | A reviewer (≠ author) has confirmed the claims against the sources. | `sourced` + `verified_by` + the higher source minimums in V-50 + a review report line. |
| `placed` | A curator has decided its neighbourhood: band, neighbours, biome reviewed *in context of its siblings* (not alone). | `verified` + (countries) ≥ 1 neighbour + reviewed in a sibling-set review report. |

Status is monotonic except that a `verified`/`placed` entity whose source
later 404s drops back to `sourced` until fixed (V-20 in CI will catch it).

### 5.2 Definition of Done — continents

- Count: **minimum 9** (one per era file 01–08 plus the pre-1943
  archipelago), **target 10–15**, hard max 15. Splitting an era file into two
  continents (e.g. 03 → "Winter Steppes" + "Expert Systems Plateau") is
  allowed and must be recorded in that file's coverage matrix header.
- Mandatory fields: all **R** for continents (§2.1) — notably `band` span,
  `biome`, `research_ref`, ≥ 3 sources, `neighbours` west/east.
- **Done** = every continent at `status ≥ verified`, A-C1…A-C7 all PASS, and
  the set of continents tiles the X axis from ≤ 1943 to the current month with
  no year uncovered (overlaps are fine; gaps are not) — checkable by sorting
  `time_range`s.

### 5.3 Definition of Done — countries

- Count: **5–9 per continent**, total **minimum 45, target ~60**, max 80.
- Mandatory: all **R** for countries; `parent_id`; `research_ref` to a
  school bullet; ≥ 2 sources; at `placed`, ≥ 1 neighbour.
- **Done** = every research file's school bullets are 100 % accounted for in
  coverage matrices (A-M2), every country at `status ≥ verified`,
  A-K1…A-K7 PASS, and every continent has ≥ 5 countries (V-32 with
  `--require-children`).

### 5.4 Definition of Done — cities

- Count: **pilot** = one continent (Deep Learning Basin, `research/06`,
  best-sourced) with **30–50** cities including 3–8 `person` cities.
  **Full map** (later phase) = 300–600 total, 20–60 per continent, scaled to
  the era's density; the archipelago may have as few as 5.
- Mandatory: all **R** for cities; `type`; `parent_id`; ≥ 1 source
  (≥ 2 with one non-Wikipedia for `verified`).
- **Pilot done** = coverage matrix for the pilot continent passes A-M1…A-M5
  (every timeline row / key paper / key person accounted for), every pilot
  city at `status ≥ verified`, A-T1…A-T6 PASS, and every pilot country has
  ≥ 2 cities.
- **Draft vs verified at city level**: `draft` cities are allowed to exist
  indefinitely only if they are frontier (start within 12 months). A
  non-frontier city that stays `draft` for more than one review cycle is a
  FAIL in the next review report (A-R3).

### 5.5 Frontier intake (recurring)

One intake is **done** when `research/frontier/YYYY-MM.md` passes R-01…R-05
and R-08, every item it promotes exists as a `draft` city passing A-T6, the
aging section has been applied (promotions bump `status`, prunes are
appended to `research/frontier/pruned.md`), `validate.py` is clean, and the
commit is titled `frontier: YYYY-MM`.

## 6. Non-goals and explicit exclusions for the content phase

The following are **out of scope** until `STATUS.md` says otherwise. A unit
of work that touches them is out of spec regardless of quality.

1. **No rendering, no frontend, no map engine, no style tiles.** No
   MapLibre/Leaflet, no tiles, no SVG polygons, no terrain rasters.
2. **No x/y coordinates in the data.** `time_range` and `band` are the only
   positional fields. Polygons and pixel positions are Phase 4 artifacts that
   will be authored *from* this data, not stored in it.
3. **No street level.** No entity below city. Model versions, individual
   tricks, tools and minor people live in city `summary` text. The
   citation-graph-projection idea is a Phase 5+ note in `STATUS.md`.
4. **No automated verification pipeline / CI** beyond `check_links.sh` and
   the single `validate.py` this spec defines. No GitHub Actions in this
   phase.
5. **No new source *types***: no scraping of sites that block bots, no
   social-media sourcing. `SOURCING.md` tiers are the whitelist.
6. **No exhaustive bibliography.** A city must pass "would a well-read
   practitioner recognise this name?". Coverage matrices exist precisely so
   that *dropping* something is a recorded decision, not an omission.
7. **No adjacent-field territories** (§2.9) — case-by-case entities only.
8. **No copy-editing for a single voice** across research files in this
   phase; voice unification is a later pass and must not be mixed into
   content-correctness commits.
9. **No renaming of entity ids once merged to `main`.** Rename = new id +
   `notes: superseded-by`.

## 7. How to check a unit of work (the whole procedure)

1. `git pull`; identify the unit in `PLAN.md`; read its **Inputs**.
2. Do the work. Author only the **Outputs** listed. Touch nothing else.
3. Run `scripts/check_links.sh` on every markdown/YAML file you changed (or
   `validate.py` once it exists, which calls it).
4. Walk the acceptance table for the artifact type (§4) and write a
   PASS/FAIL line per criterion into the commit message or a review report.
5. If you are the author, you may set `status` up to `sourced`. Only a
   reviewer (different agent/model/person) may set `verified` or `placed`.
6. Commit with the unit id in the subject: `P2-T3: author countries for
   symbolic-heartland`. Push.
7. Record any deviation from this spec as a proposed spec change in the
   commit body — do not silently invent fields or statuses.

## 8. Change control

This spec changes by commit to `main` with subject `SPEC: …`. Rule IDs are
never renumbered; retired rules are struck through with a reason. `PLAN.md`
units reference rule IDs, so a rule change may require re-checking the units
that cite it — list them in the commit body.


## 9. Review-render spec — countries inside continents (P3-RENDER)

> Added 2026-09-11 (`SPEC:` commit). Governs the **review prototype** in
> `site/` only (the P2-T1-RENDER lineage), not the eventual Phase-4 map
> engine. §6 item 2 still holds: no coordinates are stored in `data/`; every
> position below is *derived* at render time from `time_range`, `band`,
> `parent_id`, `neighbours` and the parent's drawn polygon.

### 9.1 Visual grammar (normative)

| # | Rule |
|---|---|
| G1 | **Containment.** A country is drawn as one irregular polygon strictly inside its parent continent's drawn polygon (the v9+ isochrone-frontier shape), never crossing the parent's outer coast or a sibling continent's border. |
| G2 | **Tiling.** The set of countries of one continent tiles the parent polygon: no interior gaps larger than the border stroke, no overlaps. Area is a hint, not data: a country's X extent comes from its `time_range` (piecewise scale, `AXES.md` §1) and its Y extent from its `band` (single band or contiguous span); the remaining slack is absorbed by the curator's tiling, not by stretching `time_range`. |
| G3 | **Band containment.** A country's `band` (or span) is a subset of the parent continent's registry span. A country that genuinely lies outside it is recorded as `band_override_note` + a `notes: exclave:` token and is drawn as an exclave *touching* the parent, not a free-floating island. |
| G4 | **Terrain.** A country reuses the parent's biome texture when its `biome` equals the parent's; a differing `biome` (e.g. `wetland` RL delta, `harbour` tooling guild inside a `forest` continent) is drawn with that biome's texture and tint, same wash constants as the continent layer (`TINT_WASH`/`TINT_BAND`), so the mixed-terrain continent reads as one landmass with provinces. |
| G5 | **Borders.** Country–country borders are a thin hand-drawn stroke (1/3 the continent border width, same ink), following the same `x = f(band, year)` wobble discipline as continent frontiers (no plumb lines). `relation: wall` neighbours get a double stroke; `bridge` a dashed causeway across the border; `river`/`road` are drawn as the thread's linear feature, not as a border. |
| G6 | **Labels by zoom.** Two zoom states exist in the prototype: **A1** (continent view, default) and **A2** (country view, entered by clicking a continent). At A1 no country labels render; countries appear only as faint interior border strokes and biome provinces. At A2 the clicked continent's name label is hidden and every country renders name (Cinzel, ≤ 60 % of the continent-name size) + subtitle + year range, and the other continents' labels dim to 40 % opacity. |
| G7 | **Label density.** At A2 no two country label bounding boxes overlap (same `LABEL_GAP` gate as continents) and every label lies inside its own polygon or, if the polygon is too small, is attached by a leader line to it. Minimum font size is the existing `MIN_FONT`. |
| G8 | **Hover/click.** Hovering a country at A2 shows the existing card with name, subtitle, `time_range`, `band`, `biome`, the first 60 words of `summary`, and its `neighbours` list; clicking a country is a no-op until the city phase (P4) exists. |
| G9 | **Status treatment.** `status: draft` countries render with the frontier haze (reduced fill opacity + dashed border); `sourced`/`verified`/`placed` render solid. No other status is visually distinguished in the prototype. |
| G10 | **Source of truth.** The prototype reads `data/continents/*.yaml` + `data/countries/*.yaml` via a build step (`site/build_entities_json.py`, sibling of `build_registry_json.py`) into a single `entities.json`; `REGISTRY.md` remains authoritative for continent *ids/spans* until P2-T13 marks the YAMLs verified, at which point the YAMLs take over (recorded in `STATUS.md`). |

### 9.2 Acceptance criteria (binary; checked by `site/check_layout.py` unless stated)

| ID | PASS when |
|---|---|
| A-V1 | For every continent that has ≥ 1 country YAML on `main`, the A2 view draws exactly as many `g.country` elements as `data/countries/*.yaml` files with that `parent_id`; zero JS errors. |
| A-V2 | Every rendered country path is inside its parent's path: point-in-fill sampling of ≥ 300 interior points per country yields 100 % inside the parent polygon and 0 % inside any other continent (G1). |
| A-V3 | Union of a continent's country paths covers ≥ 97 % of the parent's fill area and pairwise country overlap is 0 px² after stroke subtraction (G2). |
| A-V4 | Every country's `band` ⊆ its parent's registry span, **or** the file carries `band_override_note` and `notes` contains `exclave:` (G3). Mechanical: `scripts/check_country_bands.py`, exit 0. |
| A-V5 | Rendered country fill colour matches its `biome`: sampled mean HSV of each country fill lies within the same tolerance band `scripts/sample_fill_colours.py` already applies to continents (G4). |
| A-V6 | At A1, `g.country text` count is 0; at A2 for the selected continent, every country has ≥ 3 `text` nodes (name, subtitle, years) and the selected continent's `.cname` is hidden (G6). |
| A-V7 | At A2, no two country label bounding boxes intersect after `LABEL_GAP` growth; every label bbox is inside its own path or has a leader whose far end is (G7). |
| A-V8 | Every country border stroke has a measured lean spread ≥ 6 px between its northernmost and southernmost band rows (the continent `frontiersNotDiagonal` gate scaled to country size) — no plumb-line borders (G5). |
| A-V9 | The Pages deploy is green and the live page contains the marker text `P3-RENDER v1`; `entities.json` on the live site lists every country file on `main` at that commit (G10). |
| A-V10 | Independent vision review (reviewer ≠ author) of a screenshot of the A2 view answers "yes" to: "Do the countries read as provinces of one landmass rather than a second layer of rectangles?" — recorded in `data/reviews/YYYY-MM-DD-p3-render.md`. |

### 9.3 Out of scope for P3-RENDER

City markers, rivers/roads as geometry (only the `river`/`road` neighbour
stroke of G5), fly-to animation, per-country textures, and any change to
continent geometry. If a country cannot be tiled without moving a continent
frontier, the unit stops and files the conflict in `STATUS.md` rather than
editing `FRONT`/`ENV`.


