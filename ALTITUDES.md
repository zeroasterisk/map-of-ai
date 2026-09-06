# ALTITUDES — zoom levels for the Map of AI

> **Status: DECIDED (Alan, 2026-09-06). Three altitudes: continent / country /
> city.** There is no "street" level in scope. Major individual figures live
> at city level. Naming is evocative name + neutral subtitle. Depends on
> `AXES.md` (Y = reasoning ↔ embodiment soft bands; biome = symbolic ↔
> learned). The normative, checkable form is `SPEC.md`.

## 0. Principles

- **Each altitude is a different map, not a filtered version of the same one.**
  mapofmetal.com works because each zoom reveals new labels, not smaller
  versions of the same labels. Same here: continent names disappear when
  country names appear.
- **Fixed entity types per altitude.** An entity has exactly one home
  altitude. Its label renders there; at higher altitudes it is a fill; at lower
  altitudes it is an anchor for its children.
- **Every entity has a parent** (except continents) and a position inherited
  from, but adjustable within, its parent. This is what makes the content model
  a tree and the map navigable.
- **Labels carry a date.** Every entity at A2–A3 shows a year or year range on
  hover/click, so the X axis is always legible even where the scale is
  non-linear.
- **Three altitudes: continent, country, city.** The formerly proposed fourth
  "street" level (individual papers, model versions, tools) is out of scope.
  Rationale (Alan): existing citation-graph tools (Connected Papers, Semantic
  Scholar graphs, Papers with Code lineage) could later be *projected* onto a
  street layer instead of hand-curating thousands of entities. That is
  recorded as a Phase 5+ idea in `STATUS.md`, not committed scope. Monthly
  frontier intake therefore lands at **city** level with `status: draft`
  (see `SPEC.md` §5 and `SOURCING.md`), not at a street level.
- **Names are evocative + a neutral subtitle** at continent and country level
  (mapofmetal style): "The Statistical Isthmus" / "Bayesian & probabilistic
  ML, 1988–2011". Cities use their plain, recognisable name ("AlexNet",
  "Dartmouth 1956") with the date in the subtitle.

## 1. Altitude table

| | A1 Continent | A2 Country | A3 City |
|---|---|---|---|
| Entity | era-paradigm | school of thought / subfield / lab-cluster | lab, group, landmark system or model, landmark paper, event, dataset/benchmark, institution, **major person** |
| Count (target) | 10–15 (incl. archipelago) | ~60 (5–9 per continent) | 300–600 overall; pilot = one continent first |
| Source in repo | `research/0N-*.md` file headers + map notes | `## Schools of thought` sections | timeline + key papers + key people sections |
| Label style | large serif, letter-spaced, follows terrain | medium, with date range | small, with year, icon by type |
| Terrain visible | biome colour, rivers, roads | + borders, mountains, coast detail | + city markers, routes |
| What clicking does | fly to A2 | fly to A3, show 1-paragraph summary | open card: summary, dates, sources |
| Analogy | mapofmetal top level (Heavy Metal / Thrash / Death …) | mapofmetal sub-genre regions | mapofmetal band markers |

## 2. A1 — Continents (era-paradigms)

One per research file, roughly. Each continent spans a time range on X and a
characteristic set of bands on Y. Names below are working titles; final names
must follow the evocative-name + neutral-subtitle rule (`SPEC.md` §2.3).

| Continent | X span | Dominant Y bands | Source file |
|---|---|---|---|
| The Antecedent Isles | pre-1943 (archipelago) | N1–N2 | 01 |
| Cybernetic Shore | 1943–1956 | S2, N1 | 01 |
| The Symbolic Heartland | 1956–1974 | N2, C, S1 | 02 |
| Winter Steppes & Expert Systems Plateau | 1974–1993 | N2 | 03 |
| Connectionist Revival | 1982–1998 | S2, C | 04 |
| The Statistical Isthmus | 1988–2011 | N2–S1 (mid-latitudes) | 05 |
| Deep Learning Basin | 2006–2017 | S2 → C → S1 | 06 |
| Transformer Plateau | 2017–2022 | C, spreading to all bands | 07 |
| Generative Frontier | 2022–present | all bands | 08 |

Notes:
- Continents overlap in X on purpose (Connectionist Revival 1982–98 coexists
  with the Expert Systems Plateau 1974–93). They are distinguished by Y band
  and biome, not by non-overlapping time. This is where the map does something
  a timeline can't.
- The AI winters are rendered as *terrain* (steppe/tundra with sparse cities),
  not as blank space. There was work; it was underfunded.
- Cross-cutting threads (file 09) are not continents; they are linear features
  visible at A1 and A2.

## 3. A2 — Countries (schools of thought)

Roughly 5–9 per continent, drawn straight from each file's
`## Schools of thought / sub-clusters` section. Each is an irregular territory
inside its parent continent, positioned in the band(s) where it belongs —
bands are soft, so a country that genuinely spans N2→S2 records the span.
Borders between countries are drawn where the research notes say "borders:".

Example — countries of the Symbolic Heartland (from `research/02`):

| Country | Band | Border notes |
|---|---|---|
| Heuristic Search & Cognitive Simulation (Newell–Simon) | N2 | borders Logic-based AI; north bank of the Search river |
| Logic-based AI / the Neats (McCarthy) | N2 | borders Heuristic Search; bridge east to Prolog/Fifth Generation |
| Micro-worlds & the Scruffies (Minsky, Winograd, Schank) | C | straddles N2/C; borders ELIZA |
| Perceptron Strip (Rosenblatt, Widrow) | S2 | cut off by the "Perceptrons wall" (1969) on its eastern border |
| Robotics, Vision & Planning (Shakey, Freddy) | S1–S2 | bridge west to cybernetics |
| Game Playing (Samuel, Greenblatt) | S1 | source of the RL river |
| Early Knowledge Systems (DENDRAL) | N2 | headwaters of the Expert Systems Plateau |
| Critics & Philosophers (Dreyfus, ALPAC, Lighthill) | N1 | ridge along the northern edge |

Example — countries of the Generative Frontier (from `research/08`):

| Country | Band |
|---|---|
| Closed Frontier Labs (scaling + RLHF) | C, spreading N2 |
| Open-Weights Movement | C |
| Reasoning & Test-Time-Compute School | N2 |
| Diffusion / Generative Media | S2 |
| Agents, Tool Use & Protocols | S1 |
| Alignment, Safety & Governance | N1 |
| Embodied / VLA Robotics | S2 |

## 4. A3 — Cities (labs, landmark systems, landmark papers, events, major people)

The densest authored level. Everything in the timeline tables, key papers,
and key people sections of the research files is an A3 candidate, filtered
by "would a well-read practitioner recognise this name?". **People are
cities**: the founders and major figures (Turing, McCarthy, Minsky, Hinton,
Hassabis, Ng, Fei-Fei Li, …) get their own city, typed `person`, placed
inside the country where they did their defining work; a person who moved
between schools is placed once, at the defining work, with the moves noted in
the card. City *types* get different icons:

| Type | Icon (proposal) | Examples |
|---|---|---|
| Lab / group | star / capital | MIT AI Lab, SAIL, Bell Labs Holmdel, PDP group UCSD, Google Brain, DeepMind, FAIR, OpenAI, Anthropic |
| Landmark system / model | filled circle | Logic Theorist, ELIZA, SHRDLU, MYCIN, XCON, TD-Gammon, LeNet-5, Deep Blue, Watson, AlexNet, AlphaGo, GPT-3, ChatGPT, AlphaFold 2 |
| Landmark paper | open circle / book | McCulloch–Pitts 1943, Turing 1950, *Perceptrons* 1969, Rumelhart–Hinton–Williams 1986, Pearl 1988, Cortes–Vapnik 1995, LSTM 1997, *Attention Is All You Need* 2017, scaling laws 2020 |
| Event | flag | Dartmouth 1956, Lighthill 1973, NIPS 1987, ILSVRC 2012, Lee Sedol 2016, ChatGPT launch 2022, Bletchley 2023, Nobel 2024 |
| Dataset / benchmark | anchor (harbour) | MNIST, ImageNet, Netflix Prize, GLUE, HumanEval |
| Institution / conference | town hall | AAAI, NeurIPS, ICML, ICLR, ICOT, MCC |
| Person | monument / bust | Turing, McCarthy, Minsky, Newell & Simon, Rosenblatt, Pearl, Hinton, LeCun, Bengio, Schmidhuber, Fei-Fei Li, Ng, Hassabis, Sutskever, Amodei |

Example — cities of the Connectionist Revival, arranged by band:

- C: Elman nets (1990), NETtalk (1987), PDP volumes (1986)
- S2: Neocognitron (1980), LeNet (1989), LeNet-5 / MNIST (1998), TDNN
- S1: TD-Gammon (1992)
- N2: Universal approximation (Cybenko 1989), Hopfield (1982), Boltzmann (1985)
- harbour: NIPS 1987
- people: Hinton (Toronto), Rumelhart & McClelland (UCSD), LeCun (Bell Labs),
  Hochreiter & Schmidhuber (TU Munich / IDSIA)

## 5. Below city level — not in scope

Individual papers that are not landmarks, individual model versions
(GPT-1/2/3/3.5/4/4o as separate entries), tools, tricks (ReLU, dropout,
Adam) and minor people are **not authored as entities**. Where the research
files mention them, they live in the parent city's card text (e.g. the
"OpenAI GPT series" city card lists the versions) and nowhere else.

Future idea, explicitly *not* committed (Phase 5+, see `STATUS.md`): project
an external citation graph (Semantic Scholar / OpenAlex / Connected Papers)
onto a fourth zoom level, anchored to our A3 cities, instead of hand-curating
it. That would give paper-level detail for free once cities have stable IDs
and at least one DOI/arXiv identifier each — which is why `SPEC.md` requires
`sources` on every city.

Monthly update rule under three levels: new items enter at **A3 with
`status: draft`** (frontier haze) and are promoted, kept or pruned on the
`SOURCING.md` aging schedule. Most months add zero to a handful of cities.

## 6. Non-positional layers (every altitude)

| Layer | What | Where defined |
|---|---|---|
| Biome | symbolic ↔ statistical ↔ neural ↔ foundation, RL wetlands, harbours | AXES.md §3 |
| Rivers | RL (Samuel → RLHF), Language (Georgetown–IBM → GPT), Vision coast | research/09 threads a, f, g |
| Roads | Compute/hardware (Lisp machines → CUDA → TPU → H100) | research/09 thread d |
| Ridge | Safety/ethics/philosophy along the northern edge | research/09 thread c |
| Borders | Open ↔ closed, east of ~2015 (toggle) | research/09 thread e |
| Graticule | year lines, denser toward the east | AXES.md §1 |
| Frontier haze | last 12 months: lower-confidence styling | SOURCING.md |

## 7. Data model sketch (for Phase 3/4)

Superseded. The authoritative schema, field types, enums and validation rules
are in `SPEC.md` §2–§3. Do not author entities against the sketch that used
to be here.

## 8. Decision record

| # | Question | Decision | Status |
|---|---|---|---|
| 1 | How many altitudes | Three: continent / country / city. No street level. | **Confirmed** (Alan, 2026-09-06) |
| 2 | Where do people live | City level (`type: person`), major figures only | **Confirmed** (Alan, 2026-09-06) |
| 3 | Label language | Evocative name + neutral subtitle for continents and countries; plain name + date for cities | **Confirmed** (Alan, 2026-09-06) |
| 4 | Street level via citation-graph projection | Noted as a Phase 5+ idea; not scope | Idea only |
