# AXES — coordinate system for the Map of AI

> Status: proposal for Alan's decision. Recommendation at the bottom.
> Everything in `research/` carries a "Map placement" line written in terms of
> the *symbolic ↔ connectionist* poles. Section 3 explains why those placements
> stay valid under the recommended axis.

## 0. Design rules

1. **X is time, full stop.** West = oldest, east = present. Nothing else may
   leak into X.
2. **Y must be time-invariant.** Because X already encodes chronology, any Y
   candidate that is itself strongly correlated with time collapses the map
   into a diagonal band with empty corners. Every era must be able to populate
   the whole height of the map.
3. **Locality is the product.** Alan's goal is that "similar schools of thought"
   sit near each other. A Y axis is good to the degree that intellectual
   neighbours become geographic neighbours *in every era*, not only in the one
   that inspired the axis.
4. **Two dimensions are not enough; use cartographic channels.** Real maps
   carry more than lat/long: terrain colour (biome), roads, rivers, borders,
   elevation. Dimensions that fail as Y can still be first-class on the map
   as biome colour or overlays. This is how mapofmetal.com gets away with only
   two axes: genre-family position plus visual texture.

## 1. X axis — where does AI history start?

Candidates for the western edge, with what each implies:

| Candidate | Why | Problem |
|---|---|---|
| Dartmouth 1956 | The field is named; canonical "founding event" (Wikipedia, AAAI) | Erases the 1943–55 work that Dartmouth attendees were already building on: McCulloch–Pitts, Wiener, Shannon, Turing 1950, Minsky's SNARC (1951), Samuel's checkers (1952–), Georgetown–IBM MT (1954) |
| Turing 1950 (*Computing Machinery and Intelligence*) | First explicit philosophical framing of machine intelligence; the Turing test | Post-dates McCulloch–Pitts and cybernetics; picks the philosophy strand over the engineering strand |
| McCulloch & Pitts 1943 | First mathematical model of neural computation; cited by von Neumann, Wiener, Minsky; both poles of the field descend from it; Wiener's cybernetics circle and the Macy conferences start within 3 years | "AI" as a *research programme* isn't quite there yet; it is neuro-logic |
| Turing 1936 (*On Computable Numbers*) | Defines the universal machine that everything runs on; Church, Post, Kleene in the same 12 months | It is theory of computation, not of intelligence; putting it on the mainland drags in all of CS |
| Boole 1854 / Leibniz / Lovelace 1843 / Hobbes 1651 / Aristotle | Genuine intellectual ancestry ("reasoning is reckoning") | Millennia of near-empty ocean if X is linear; nobody would call this AI research |

**Recommendation for X:**

- **Mainland west coast = 1943** (McCulloch–Pitts). This is the first artifact
  that every subsequent school claims as an ancestor: the logic camp (it is a
  paper about propositional logic), the neural camp (it is a neuron model), and
  cybernetics (Pitts joined Wiener's circle immediately). Starting here also
  makes 1943–1956 a visible, populated coastal strip (cybernetics, Hebb 1949,
  Shannon 1948/50, Turing 1950, SNARC, perceptron pre-history) rather than an
  invisible prologue.
- **Western sea with an archipelago = pre-1943.** Turing 1936, Church, Gödel
  1931, Hilbert, Frege, Boole, Babbage/Lovelace, Leibniz, Llull, Hobbes,
  Aristotle rendered as *islands* off the coast, on a compressed non-linear
  scale, labelled as "Antecedents". They are navigable and cited but visually
  off-continent. This honours "maybe before Turing" without pretending the
  ocean is land.
- **East coast = the last completed calendar month.** The monthly update adds
  a new strip of coastline. The final ~12 months render with a "frontier"
  treatment (see `SOURCING.md`): lower confidence, fewer permanent labels.

**X scale is non-linear.** Content density is roughly exponential in time.
Linear years would make 2012–2026 a sliver holding half the content.
Proposed: a piecewise scale where map-width per year grows with era, with a
visible year graticule so the distortion is honest, like a Mercator grid:

| Span | Relative width per year | Rationale |
|---|---|---|
| pre-1943 archipelago | ~0 (log-compressed) | islands, not mainland |
| 1943–1974 | 1× | founding era |
| 1974–2006 | 1.5× | winters, expert systems, connectionist revival, statistical ML |
| 2006–2017 | 3× | deep learning revolution |
| 2017–present | 6× | transformer/LLM/agent era; monthly updates |

Exact ratios are a rendering decision (Phase 4); the principle is decided now.
Alternative: a continuous density-weighted scale computed from the number of
A3 entities per year. Either works; the piecewise one is easier to read.

## 2. Y axis — candidates

Each candidate is judged on: what it captures, what it fails to capture,
time-invariance (rule 2), and clustering quality per era (rule 3).

### Candidate A — Symbolic/logic (north) ↔ Connectionist/statistical (south)

The classic schism: GOFAI, neats, knowledge engineering, logic programming vs.
perceptrons, PDP, deep learning, "the bitter lesson". It is the axis every
history of AI is written along (Nilsson, Russell & Norvig, Boden), and it is
the one the `research/` files were drafted against.

- Captures: the defining intellectual conflict 1943–2012; Perceptrons (1969)
  as a wall; the 1986 revival; the 2012 flood. Neighbours cluster beautifully
  pre-2010: expert systems next to Prolog next to Cyc; PDP next to Hopfield
  next to LeNet.
- Fails: **it is strongly time-correlated.** 1969–1982 has almost nothing in
  the south; 2012–present has almost nothing in the north. The east half of
  the map, where most of the content and all the monthly updates live, becomes
  a single latitude band: vision, NLP, RL, robotics, diffusion, agents all pile
  on top of each other with no way to separate them. Also has no natural place
  for probabilistic/Bayesian AI or classical statistical ML (the compendium
  had to invent a "statistical isthmus" mid-latitude).
- Clustering by era: 1943–74 excellent; 1974–2010 good; 2012–present poor.

### Candidate B — Theory/cognition (north) ↔ Applied/industry (south)

Academic, theory-driven, "understand intelligence" work vs. engineering,
product, and industrial-lab work.

- Captures: the migration of the field from universities to Bell Labs, IBM,
  Google Brain, DeepMind, OpenAI; the AI-winter funding story; Breiman's
  "two cultures".
- Fails: nearly every school has both a theory wing and an applied wing, so it
  splits schools instead of clustering them. It also puts strangers together:
  Cyc and Bell Labs cheque-reading are both "applied". Loosely time-correlated
  (industry share rises monotonically after 2011).
- Clustering: weak in every era.

### Candidate C — Narrow/specialised (north) ↔ General-purpose (south)

Task-specific systems vs. general intelligence ambitions.

- Captures: the AGI thread (GPS 1959 → Cyc → AGI conferences → foundation
  models); the specialise-then-generalise rhythm of each paradigm.
- Fails: "general" is relative to its era (GPS was general in 1959) so it is
  not stably scoreable; most work would sit at "narrow" and cluster nothing.
- Clustering: mediocre.

### Candidate D — Open/commons (north) ↔ Closed/proprietary (south)

Open science and open weights vs. closed labs and products.

- Captures: a real and important tension of 2015–present (TensorFlow/PyTorch,
  LLaMA leak, Llama 2/3, Mistral, DeepSeek vs. GPT-4/Claude/Gemini).
- Fails: meaningless before ~2010, when almost everything was published
  academic work. Maximally time-correlated. Cannot be the Y axis of a map that
  starts in 1943. It is an excellent **overlay** for the east.
- Clustering: n/a west of 2010.

### Candidate E — The abstraction gradient: Reasoning & knowledge (north) ↔ Perception & action / embodiment (south)

Position work by *what aspect of intelligence it is about*, from the most
abstract to the most embodied. Five latitude bands, north to south:

| Band | Content | Examples across eras |
|---|---|---|
| N1 Philosophy & foundations | theory of mind, computability, critiques, safety/ethics | Turing 1950, Dreyfus, Searle, Bostrom, Stochastic Parrots, alignment |
| N2 Logic, knowledge & reasoning | theorem proving, knowledge representation, expert systems, probabilistic reasoning, formal methods, reasoning models | Logic Theorist, Prolog, MYCIN, Cyc, Bayesian networks, knowledge graphs, o1/R1-style reasoning |
| C  Language & communication | MT, dialogue, NLP, LLMs, code generation | Georgetown–IBM, ELIZA, SHRDLU, IBM statistical MT, word2vec, BERT, GPT, ChatGPT |
| S1 Planning, search, decision & games | search, planning, game playing, RL, agents | Samuel, GPS, STRIPS, Deep Blue, TD-Gammon, DQN, AlphaGo, LLM agents, MCP |
| S2 Perception, control & embodiment | vision, speech, robotics, cybernetics, control | Cybernetics, Shakey, Neocognitron, LeNet, AlexNet, diffusion, Boston Dynamics, VLA models |

- Captures: **time-invariance.** Every era has work in every band, so every
  vertical slice of the map is populated (1960s: GPS / ELIZA / Samuel / Shakey;
  2020s: reasoning models / LLMs / agents / diffusion+robotics). Long
  west-east "lineages" appear as continuous features: a *language river* from
  Georgetown–IBM to GPT, a *vision coast* from Neocognitron to diffusion, an
  *RL delta* from Samuel to RLHF. Moravec's paradox becomes geography: the
  north (reasoning) was conquered early, the south (perception, dexterity)
  late. The east edge spreads across the full height so monthly additions
  have room.
- Fails: (1) general-purpose *methods* have no modality: PAC theory, SVMs,
  boosting, optimisers, frameworks. Convention: place them where they had
  their dominant impact (SVM/boosting → perception/pattern recognition next to
  LeNet; graphical models → N2 next to the expert systems they displaced; PAC/VC
  → N1/N2 theory; frameworks/hardware → roads, not places). (2) Tightly-knit
  *methodological* communities get spread vertically: the 1987–98 NIPS
  community (Elman in C, LeCun in S2, Tesauro in S1, Cybenko in N2). This is
  the real cost and it is mitigated by biome colour (section 3). (3)
  Multimodal work (CLIP, GPT-4o, Gemini) spans bands; render as larger
  territories straddling C/S2.
- Clustering by era: good in every era; excellent for 2012–present, which is
  exactly where Candidate A fails.

### Comparison

| | A symbolic↔connectionist | B theory↔applied | C narrow↔general | D open↔closed | E reasoning↔embodiment |
|---|---|---|---|---|---|
| Time-invariant (rule 2) | no | weak | weak | no | **yes** |
| Clusters schools 1943–1990 | **excellent** | weak | weak | n/a | good |
| Clusters schools 1990–2012 | good | weak | weak | weak | good |
| Clusters schools 2012–now | poor | weak | weak | good | **excellent** |
| Room at the east edge | poor | ok | ok | ok | **good** |
| Recognisable to AI researchers | **very** | yes | yes | yes | yes |
| Objectively scoreable | mostly | no | no | yes | mostly |

## 3. Recommendation

**Y position = Candidate E (reasoning ↔ embodiment), rendered as five named
latitude bands.**
**Methodology (Candidate A, symbolic ↔ learned) = terrain biome, not position.**
**Open ↔ closed (Candidate D) = toggleable overlay for the eastern third.**

Why this combination:

1. E is the only candidate that satisfies rule 2. With X fixed to time, this is
   close to decisive: a Y axis that empties out for whole eras produces a map
   with a diagonal continent and dead corners, and it starves the east edge of
   space precisely where monthly growth happens.
2. **A and E agree on the west half of the map.** Symbolic AI *was* about
   reasoning and knowledge; connectionism and cybernetics *were* about
   perception and control. So under E, 1943–2010 still reads north =
   symbolic, south = neural. Every "Map placement" line already written in
   `research/` (symbolic pole / connectionist pole / mixed) translates
   directly: symbolic pole → N2, connectionist pole → S2 (or C for PDP
   language work), mixed → C/S1. Nothing needs to be redone.
3. Where A and E disagree is 2012–present, and there E is strictly better: the
   connectionist "flood" that takes over every band is *the* visual story of
   the modern map. With biome = methodology, the viewer literally watches
   neural terrain (say, green forest) spread northward across the map from the
   south-west, submerging the symbolic highlands (say, ochre/rock) band by
   band, until by the 2020s only a few symbolic outcrops remain (knowledge
   graphs, formal verification, neurosymbolic, program synthesis) and the
   reasoning band is re-colonised by RL-trained language models. That is a
   better rendering of the symbolic-vs-connectionist story than putting it on
   an axis, and it costs the map nothing in locality.
4. The known cost, vertically scattered methodological communities in the
   1980s–90s, is exactly what a shared biome colour plus a labelled A2 region
   ("PDP / NIPS connectionism", drawn as an irregular territory spanning
   several bands) is for. Countries on real maps are not rectangles.

Biome palette (proposal, refine in Phase 4):

| Biome | Meaning |
|---|---|
| Rock / highland | hand-authored logic and knowledge (symbolic) |
| Grassland | probabilistic / statistical models with explicit structure |
| Forest | learned neural representations |
| Dense jungle | scaled self-supervised / foundation models |
| Wetland / delta | reinforcement learning and control |
| Coast / harbour | benchmarks, datasets, competitions, tooling (ports of entry) |

Cross-cutting threads from `research/09-cross-cutting-threads.md` render as
linear features: hardware/compute as a **road** (Lisp machines → GPUs → TPUs →
H100), RL as a **river** running through S1, safety/ethics as a **ridge** along
the northern edge, open-vs-closed as a **border** drawn only east of ~2015.

## 4. If Alan prefers Candidate A

It is the conservative, most-recognisable choice and the compendium already
uses its vocabulary. If chosen, adopt these mitigations:

- Give the south pole internal structure for the modern era by sub-banding
  it with E's bands (reasoning models at the top of the south, robotics at the
  bottom), which is E in disguise.
- Accept an empty NE (few symbolic events after 2012) and render it as sea or
  as a "neurosymbolic frontier" territory.
- Compress the east edge less aggressively in X to compensate for the lost
  vertical room.

## 5. Open decisions for Alan

1. Confirm Y = E with A as biome (recommended) vs. Y = A.
2. Confirm mainland start 1943 with a pre-1943 archipelago vs. starting at
   1936 or 1950.
3. Piecewise X scale vs. density-weighted X scale (rendering-time decision,
   but it affects how much content A3 needs per era).
4. Whether N1 (philosophy/safety) is a full band or a thin northern ridge.
5. Band boundaries: hard borders (like mapofmetal's genre regions) or soft
   gradients with entities free to sit between bands.
