# ALTITUDES — zoom levels for the Map of AI

> Status: design proposal. Depends on `AXES.md` (Y = reasoning ↔ embodiment
> bands; biome = symbolic ↔ learned).

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
- **Labels carry a date.** Every entity at A2–A4 shows a year or year range on
  hover/click, so the X axis is always legible even where the scale is
  non-linear.
- **Four altitudes, the fourth optional per region.** Continents, countries,
  cities, streets. A4 is only authored where the content justifies it (dense
  modern regions) and is the natural home for monthly updates.

## 1. Altitude table

| | A1 Continent | A2 Country | A3 City | A4 Street |
|---|---|---|---|---|
| Entity | era-paradigm | school of thought / subfield | lab, group, landmark system, landmark paper, event | person, paper, model, dataset, tool |
| Count (target) | 8–10 | 40–70 | 300–600 | 2,000+ (open-ended) |
| Source in repo | `research/0N-*.md` file headers | `## Schools of thought` sections | timeline + key papers + key people sections | future `data/` entries; monthly `SOURCING.md` intake |
| Label style | large serif, letter-spaced, follows terrain | medium, with date range | small, with year, icon by type | tiny, on demand |
| Terrain visible | biome colour, rivers, roads | + borders, mountains, coast detail | + city markers, routes | + street grid, building footprints |
| What clicking does | fly to A2 | fly to A3, show 1-paragraph summary | open card: summary, dates, sources | open card: full citation, link out |
| Analogy | mapofmetal top level (Heavy Metal / Thrash / Death …) | mapofmetal sub-genre regions | mapofmetal band markers | (mapofmetal has no equivalent; albums would be) |

## 2. A1 — Continents (era-paradigms)

One per research file, roughly. Each continent spans a time range on X and a
characteristic set of bands on Y. Names are working titles; the final names
should have the same evocative quality as mapofmetal's region names.

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
inside its parent continent, positioned in the band where it belongs. Borders
between countries are drawn where the research notes say "borders:".

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

## 4. A3 — Cities (labs, landmark systems, landmark papers, events)

The densest authored level. Everything in the timeline tables, key papers,
and key people sections of the research files is an A3 candidate, filtered
by "would a well-read practitioner recognise this name?". City *types* get
different icons:

| Type | Icon (proposal) | Examples |
|---|---|---|
| Lab / group | star / capital | MIT AI Lab, SAIL, Bell Labs Holmdel, PDP group UCSD, Google Brain, DeepMind, FAIR, OpenAI, Anthropic |
| Landmark system / model | filled circle | Logic Theorist, ELIZA, SHRDLU, MYCIN, XCON, TD-Gammon, LeNet-5, Deep Blue, Watson, AlexNet, AlphaGo, GPT-3, ChatGPT, AlphaFold 2 |
| Landmark paper | open circle / book | McCulloch–Pitts 1943, Turing 1950, *Perceptrons* 1969, Rumelhart–Hinton–Williams 1986, Pearl 1988, Cortes–Vapnik 1995, LSTM 1997, *Attention Is All You Need* 2017, scaling laws 2020 |
| Event | flag | Dartmouth 1956, Lighthill 1973, NIPS 1987, ILSVRC 2012, Lee Sedol 2016, ChatGPT launch 2022, Bletchley 2023, Nobel 2024 |
| Dataset / benchmark | anchor (harbour) | MNIST, ImageNet, Netflix Prize, GLUE, HumanEval |
| Institution / conference | town hall | AAAI, NeurIPS, ICML, ICLR, ICOT, MCC |

Example — cities of the Connectionist Revival, arranged by band:

- C: Elman nets (1990), NETtalk (1987), PDP volumes (1986)
- S2: Neocognitron (1980), LeNet (1989), LeNet-5 / MNIST (1998), TDNN
- S1: TD-Gammon (1992)
- N2: Universal approximation (Cybenko 1989), Hopfield (1982), Boltzmann (1985)
- harbour: NIPS 1987

## 5. A4 — Streets (people, individual papers, models, tools)

Optional per region; authored where density justifies it and as the intake
level for monthly updates. Modern east-edge regions will be street-dense (every
notable model release, every major paper); 1950s regions may have none, with
the A3 card carrying the people instead.

- People appear at A4 as residents of their lab-city, with tenure dates. A
  person who moved (Hinton: Carnegie → Toronto → Google) appears in each with
  the respective date range; the card links them.
- Model families render as street grids: GPT-1/2/3/3.5/4/4o/o1 as consecutive
  streets in the OpenAI city.
- Monthly update rule: new items enter at A4 with `status: provisional`. After
  the retention window in `SOURCING.md` they are promoted to A3 or pruned.

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

Not built yet; recorded so content authoring converges on it.

```yaml
id: alexnet-2012
type: system            # lab | system | paper | event | dataset | institution | person | model | tool
altitude: 3
parent: gpu-convnet-school   # A2 id
continent: deep-learning-basin
x: 2012-09              # ISO date or year; X derived by scale function
band: S2                # N1 | N2 | C | S1 | S2
biome: forest
label: AlexNet
years: 2012
summary: "..."
sources:
  - https://en.wikipedia.org/wiki/AlexNet
  - https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks
threads: [vision, compute]
status: verified        # provisional | draft | verified
```

## 8. Open decisions

1. Three altitudes shipped first (A1–A3), A4 later? Recommended: yes; A4 only
   for 2017+ initially.
2. Whether people are A3 (own city) or A4 (residents). Recommended: A4, with
   the "founders" (Turing, McCarthy, Minsky, Hinton, …) also promoted to A3
   monuments.
3. Label language: neutral ("Symbolic AI 1956–1974") or evocative ("The
   Symbolic Heartland")? mapofmetal uses genre names straight; our regions have
   no canonical names, so evocative labels with a neutral subtitle is the
   proposal.
