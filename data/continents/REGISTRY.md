# Continent registry (A1) — `data/continents/REGISTRY.md`

> **Unit:** PLAN.md P2-T1. **Status:** proposed — awaiting Alan's review via the rendered prototype (P2-T1-RENDER) before any continent YAML (P2-T2…) is authored.
> **Authoritative for:** continent `id`s, `name`, `subtitle`, `time_range`, `band` span, `biome`, `research_ref`, `offshore`, `split-of`. Every later unit references these ids; **ids never change** after this file is accepted (SPEC.md §2.1: "stable forever; never reuse").
> **Not yet decided here:** `neighbours` (P2-T12), polygons, exact X pixel placement, country membership (P3).
> **Inputs used:** ALTITUDES.md §2 table; every `research/0[1-8]` frontmatter ("Date range", "Map placement", "Altitude") and "Map notes" A1 label lines; `research/01` archipelago/shore split table (P1-T11); SPEC.md §2.1, §2.3, §2.6, §5.2; AXES.md §1 (1943 west coast, offshore archipelago), §3 (bands, biome palette, rule 2).

## 1. The registry

Ten continents. Sorted by `start`. `band span` is a home neighbourhood hint (AXES.md §3), not a coordinate; a range like `N2–S1` means the contiguous list `[N2, C, S1]`.

| # | id | name | subtitle | start | end | band span | biome | research file | offshore? | split-of |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `antecedent-isles` | The Antecedent Isles | Logic, computability and the mathematical prehistory of AI, 1666–1942 | 1666 | 1942 | N1–N2 | highland | 01 | **true** | 01 → isles (P1-T11 split, archipelago half) |
| 2 | `cybernetic-shore` | The Cybernetic Shore | Cybernetics, neural modelling and the first thinking-machine programmes, 1943–1956 | 1943 | 1956 | N1–S2 (home S2, N1) | mixed | 01 | false | 01 → shore (P1-T11 split, mainland half) |
| 3 | `symbolic-heartland` | The Symbolic Heartland | Dartmouth and the golden age of symbolic AI, 1956–1974 | 1956 | 1974 | N2–S1 | highland | 02 | false | — |
| 4 | `winter-steppes` | The Winter Steppes | The two AI winters — funding collapse and retrenchment, 1974–1993 | 1974 | 1993 | N1–N2 | highland | 03 | false | 03 → steppes (this file, §2 decision D2) |
| 5 | `expert-systems-plateau` | The Expert Systems Plateau | Knowledge engineering, expert systems and the Fifth Generation boom, 1980–1993 | 1980 | 1993 | N2 | highland | 03 | false | 03 → plateau (this file, §2 decision D2) |
| 6 | `connectionist-revival` | The Connectionist Revival | Hopfield nets, backpropagation and the PDP era of neural networks, 1982–1998 | 1982 | 1998 | C–S2 (home S2) | forest | 04 | false | — |
| 7 | `statistical-isthmus` | The Statistical Isthmus | Probabilistic, Bayesian and statistical machine learning, 1988–2011 | 1988 | 2011 | N2–S1 (mid-latitude) | grassland | 05 | false | — |
| 8 | `deep-learning-basin` | The Deep Learning Basin | GPU-trained deep neural networks from DBNs to AlphaGo, 2006–2017 | 2006 | 2017 | C–S2 (home S2 → C → S1) | forest | 06 | false | — |
| 9 | `transformer-plateau` | The Transformer Plateau | Attention, pre-trained language models and scaling laws, 2017–2022 | 2017 | 2022 | N2–S2 (home C, spreading) | jungle | 07 | false | — |
| 10 | `generative-coast` | The Generative Coast | Chat assistants, open-weight models, reasoning models and agents, 2022–present | 2022 | present | N1–S2 (all bands) | jungle | 08 | false | — |

Border landmarks quoted from the research files (input to P2-T12, not yet `neighbours`):

| id | west border (from research file) | east border (from research file) |
|---|---|---|
| `antecedent-isles` | open ocean; Leibniz 1666 is the westernmost isle (research/01 "Open questions": a single "Myths & Automata" islet at most further west) | 1943 coastline; Turing 1936 isle "drawn with a causeway to the shore" (research/01 split table) |
| `cybernetic-shore` | 1943 McCulloch–Pitts / Rosenblueth–Wiener–Bigelow (AXES.md §1 west coast) | "the 1955–56 delta (Dartmouth proposal)" where the Hilbert–Gödel–Turing and Wiener–McCulloch rivers meet (research/01 map notes) |
| `symbolic-heartland` | Dartmouth 1956 delta | "a cliff/escarpment labelled 'First AI Winter (1974)' with three marked passes: Lighthill (UK), Mansfield/DARPA (US), and ALPAC" (research/02 map notes) |
| `winter-steppes` | First Winter escarpment 1974 (research/03 map notes: "1974–1980 in the west … frozen ground") | "The eastern border (~1993) is a fog bank rather than a cliff — the field does not end, it renames itself" (research/03); second frozen band "1987–1993 in the east" |
| `expert-systems-plateau` | XCON/R1 1980 — "the expert-systems boom lies between [the two winters] as a warm valley" (research/03 map notes) | "Lisp Machine Crash 1987" / second winter; fades into the 1993 fog bank |
| `connectionist-revival` | Hopfield 1982; "the 'Backprop Pass' (1986) reconnects the connectionist south to the mainstream" (research/03); "the Fodor–Pylyshyn river (1988) separates this continent from the symbolic/expert-systems landmass" (research/04) | "LSTM (1997) and LeNet-5 (1998) are the last high ground before the deep-learning continent"; "a wide statistical-learning strait … partially submerges connectionism in the mid-1990s" (research/04) |
| `statistical-isthmus` | Pearl 1988 — "a new Probability River (Pearl) begins to flow east" (research/03); "a broad isthmus connecting era 03 (north-west) and era 04 (south-west) to era 06 (east)" (research/05) | ILSVRC 2012 fault line (shared with the basin; research/06) |
| `deep-learning-basin` | "the ILSVRC 2012 fault line — SVM-plus-hand-crafted-features on one side, learned features on the other — with the 2006 DBN papers as the foothills that precede it" (research/06) | "the Attention River … leaves the map eastward at Vaswani 2017" (research/06); 12 June 2017 |
| `transformer-plateau` | Vaswani 2017 ("becomes navigable at Vaswani 2017"; research/07) | "the RLHF canal (2017 preferences paper → InstructGPT 2022) is the crossing into the chatbot era" (research/07); ChatGPT 30 Nov 2022 |
| `generative-coast` | "Draw the western border at 30 Nov 2022 (ChatGPT)" (research/08 map notes) | "an open coastline dated Sept 2026 with a 'here be dragons' strip east of the last triangulated rows" (research/08); east edge = last completed month (AXES.md §1) |

## 2. Decision record

**D1 — research/01 is two continents (isles + shore).** Decided in AXES.md §1 and executed by P1-T11: the mainland west coast is 1943; Leibniz → Boole → Frege → Hilbert → Gödel → Church → Turing 1936 are offshore islands on a log-compressed scale. `antecedent-isles` is the only `offshore: true` row; its `end` is 1942 so V-14 (`end ≤ 1943`) holds and the two rows do not overlap. The split table in research/01 assigns every timeline row, school bullet and person to exactly one of the two.

**D2 — research/03 is two continents (steppes + plateau), overlapping in X.** SPEC.md §5.2 names this exact split as the allowed example ("03 → Winter Steppes + Expert Systems Plateau"). The research file's own map notes argue for it: "Two bands of 'frozen ground' should be shaded: 1974–1980 in the west and 1987–1993 in the east; the expert-systems boom lies between them as a warm valley", and the curation answer to open question (a) is "two [winters], since the boom between them is the era's defining feature". Drawing one 1974–1993 continent would flatten the boom–bust shape that is the era's whole story. So:
- `winter-steppes` spans the full 1974–1993 (both frozen bands and the thin ground between them: Dreyfus/Searle critiques, Lighthill aftermath, the 1987 Lisp-machine crash, the AI-Winter naming at AAAI 1984). It is the northern (N1–N2) terrain; ALTITUDES.md: "The AI winters are rendered as terrain (steppe/tundra with sparse cities), not as blank space."
- `expert-systems-plateau` is the 1980–1993 warm valley (MYCIN's commercialisation → XCON 1980 → Fifth Generation 1982 → Cyc 1984 → the 1987 crash and the long tail to 1993). Start = 1980 (XCON at DEC; the first industrial deployment), not MYCIN 1972/76, which stays a border town in the steppes' western frozen band (research/02 open question (a) also calls Dendral a "border town").
- The 1980s connectionist revival (Hopfield, PDP, backprop, TD/Q-learning) is *not* a third split of 03: research/03 open question (c) recommends "keeping it here but drawing it as a large peninsula that becomes the mainland of the next era", and research/04 owns that content from 1982. Country-level rows for those 03 items will point to `connectionist-revival` at P3 (`time-overlap-ok` note) rather than to a duplicated continent.
- P3 coverage-matrix header for research/03 must record this split (SPEC.md §5.2).

**D3 — no other era file is split or merged.** 02, 04, 05, 06, 07, 08 each map to one continent; their proposed date ranges are used unchanged. Checked candidates and rejected: splitting 08 into "chatbot era" + "agents/reasoning era" (rejected — research/08 open question (3) says reasoning models *may* merit an A2 country by 2026, not a continent; the coast is the map's monthly-growing edge and should stay one region until it is actually too big); merging 04 into 03 (rejected — the two are distinguished by Y band and biome, "this is where the map does something a timeline can't", ALTITUDES.md §2 notes).

**D4 — overlaps are intentional; gaps are not.** Sorted starts: 1666, 1943, 1956, 1974, 1980, 1982, 1988, 2006, 2017, 2022 → present. Every year from 1666 to the current month is covered by ≥ 1 row (SPEC.md §5.2). Overlapping spans (1980–93 ×3 with 1982–98; 1988–98; 2006–11) are distinguished by band and biome, as ALTITUDES.md §2 requires.

**D5 — names and subtitles.** Names are cartographic (SPEC.md §2.3) and follow the working titles in ALTITUDES.md §2 wherever those already read well; "Generative Frontier" became **The Generative Coast** because research/08 consistently calls it "the map's eastern seaboard; the ocean beyond is the unknown future", and "frontier" is reserved for the SOURCING.md/monthly-intake vocabulary. "Knowledge Era" (research/03's own A1 suggestion) is not used as a name because the split makes "Expert Systems Plateau" more specific. Subtitles are neutral, name the *content*, and end in the V-12 form `, YYYY–YYYY` or `, YYYY–present`; each reads as a plain-English answer to "what is this region?" without the evocative name (A-C2 pre-check in §3).

**D6 — band spans** translate each file's "Map placement" line per AXES.md §3 point 2 (symbolic pole → N2; connectionist pole → S2 or C; mixed → span), then widen where the file explicitly says the era spreads:
- isles N1–N2 (logic + foundations; "N1–N2" in ALTITUDES.md);
- shore N1–S2 (research/01: "Y = mixed — a northern symbolic/logic pole strand … and a southern connectionist/cybernetic pole strand"; home bands S2 and N1 per ALTITUDES.md, with the Turing-test strand N1 and Georgetown MT in C);
- heartland N2–S1 (research/02: "predominantly symbolic/logic pole … ELIZA and MT sit mixed/central", Shakey/GPS in S1; the shrinking perceptron strip is a country-level S2 exclave, not enough to widen the continent);
- steppes N1–N2 (critiques, funding politics, and knowledge-engineering retrenchment);
- plateau N2 (research/03: "commercial/knowledge-based mainstream … sits at the symbolic/logic pole");
- revival C–S2, home S2 (research/04 "Map placement" and AXES.md "connectionist pole → S2 (or C for PDP language work)");
- isthmus N2–S1 (research/05: "this era sits at mid-latitude"; ALTITUDES.md "N2–S1 (mid-latitudes)");
- basin C–S2, home S2 → C → S1 (ALTITUDES.md; vision first, then NLP (word2vec/seq2seq), then RL (DQN/AlphaGo));
- transformer plateau N2–S2, home C (ALTITUDES.md "C, spreading to all bands"; AlphaFold/N2-ish reasoning and CLIP/S2 are in the file; N1 safety discourse stays a country-level exclave);
- coast N1–S2 (ALTITUDES.md "all bands"; policy/alignment N1 through robotics/VLA S2).

**D7 — biomes** per SPEC.md §2.6: the three symbolic-era rows are `highland` (steppes are *sparse* highland — "steppe/tundra", not a separate enum; noted for the renderer); revival and basin `forest`; isthmus `grassland`; transformer plateau and coast `jungle` (scaled self-supervised / foundation models). `cybernetic-shore` is the one `mixed` biome: it is genuinely half logic (McCulloch–Pitts is a paper about propositional logic) and half control/neural (Wiener, Ashby, Hebb, SNARC), and SPEC.md §2.6 asks that `mixed` be justified — this is the justification to copy into its `notes`. No row is `wetland` or `harbour` at continent scale; those appear as countries/cities (RL Valley, ImageNet, NeurIPS).

## 3. A-C2 pre-check — "would a visitor understand what this region is from the subtitle alone?"

Answered by the P2-T1 author (Hermes, 2026-09-06) reading each subtitle with the evocative name hidden. A reviewer ≠ author must re-answer at P2-T13.

| id | subtitle alone → understood? | note |
|---|---|---|
| `antecedent-isles` | yes | "prehistory of AI" + the dates make the offshore status obvious |
| `cybernetic-shore` | yes | names the three strands (cybernetics, neural modelling, thinking-machine programmes) |
| `symbolic-heartland` | yes | "Dartmouth" + "golden age of symbolic AI" is the textbook framing |
| `winter-steppes` | yes | "two AI winters — funding collapse and retrenchment" is self-explanatory |
| `expert-systems-plateau` | yes | expert systems + Fifth Generation + boom |
| `connectionist-revival` | yes | Hopfield / backprop / PDP are the three recognisable anchors |
| `statistical-isthmus` | yes | "probabilistic, Bayesian and statistical machine learning" |
| `deep-learning-basin` | yes | "GPU-trained deep neural networks from DBNs to AlphaGo" gives both ends |
| `transformer-plateau` | yes | attention + pre-trained LMs + scaling laws |
| `generative-coast` | yes | four nouns a 2026 reader recognises (chat assistants, open weights, reasoning models, agents) |

## 4. Mechanical check (PLAN.md P2-T1)

Run `scripts/check_registry.py` (added with this file). It parses §1 and asserts: 9 ≤ rows ≤ 15; every `research/0[1-8]` is the source of ≥ 1 row; ids match `^[a-z0-9]+(-[a-z0-9]+)*$`, ≤ 48 chars, unique; subtitles match `^.+, \d{4}(–(\d{4}|present))?$` and their years equal `start`/`end`; exactly the rows with `offshore? = true` have `end ≤ 1943`; sorted starts tile ≤ 1943 → present with no uncovered year; §3 has a "yes" for every id.

## 5. What P2-T12 (tiling / neighbours) will need from here

Sorted span list (year granularity): 1666–1942 (offshore) · 1943–1956 · 1956–1974 · 1974–1993 · 1980–1993 · 1982–1998 · 1988–2011 · 2006–2017 · 2017–2022 · 2022–present. West/east border landmarks are in the second table of §1. The intended coastline order for the render, west → east: isles (offshore) → shore → heartland → {steppes (N) over plateau (N2) over revival (S)} → isthmus → basin → transformer plateau → coast.

## 6. P3 instance mapping (recorded here per PLAN.md P3 header; not started)

P3-T1 `antecedent-isles` · P3-T2 `cybernetic-shore` · P3-T3 `symbolic-heartland` · P3-T4 `winter-steppes` · P3-T5 `expert-systems-plateau` · P3-T6 `connectionist-revival` · P3-T7 `statistical-isthmus` · P3-T8 `deep-learning-basin` · P3-T9 `transformer-plateau` · P3-T10 `generative-coast`. (Ten continents ⇒ ten P3 instances, matching PLAN.md's "P3-T1 … P3-T10".)
