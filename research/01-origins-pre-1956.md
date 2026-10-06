# Origins: Logic, Computability and Cybernetics (pre-1956)

> **Status:** reviewed
> **Date range:** 1666–1955 (dense core 1936–1955; thin antecedent strip back to Leibniz/Boole/Babbage)
> **Map placement (proposed):** X = far west edge, up to 1955; Y = mixed — a northern *symbolic/logic pole* strand (Leibniz → Boole → Frege → Hilbert → Gödel → Church → Turing) and a southern *connectionist/cybernetic pole* strand (McCulloch–Pitts → Wiener → Ashby → Hebb → SNARC → early perceptron work), converging on the 1956 Dartmouth border
> **Altitude:** **two** A1 continents from this file, split at 1943 per `AXES.md` §1 — (i) *The Antecedent Isles* (pre-1943, `offshore: true`; Leibniz → Boole → Frege → Hilbert → Gödel → Church → Turing 1936) and (ii) *Cybernetic Shore* (1943–1955 mainland coast; McCulloch–Pitts → Wiener/Macy → Hebb → Turing 1950 → SNARC → Samuel → Dartmouth proposal). A2 countries ("Mathematical Logic & Computability" on the isles; "Cybernetics", "Neural Modelling & Learning Machines", "Information Theory & Game Search", "Machine Translation" on the shore); A3 cities (Turing 1936, Turing 1950, McCulloch–Pitts 1943, Macy Conferences, Ratio Club); see "Archipelago / shore split" table in Map notes

## One-paragraph summary
Before anyone called it "artificial intelligence", two intellectual rivers were already flowing toward it. The first is the **logic/computability** river: Leibniz's dream of a *calculus ratiocinator*, Boole's algebra of thought (1854), Frege's *Begriffsschrift* (1879), Hilbert's programme to formalise all mathematics, Gödel's incompleteness theorems (1931), and then in 1936 Church's lambda calculus and Turing's universal machine, which together answered Hilbert's *Entscheidungsproblem* in the negative and, as a by-product, defined what a computer *is*. Turing then asked in 1950 whether such a machine could think, proposing the imitation game. The second is the **cybernetic/neural** river: McCulloch and Pitts (1943) showed networks of idealised neurons could compute any logical function; Wiener's *Cybernetics* (1948) and the Macy Conferences (1946–1953) built an interdisciplinary science of feedback and control; Ashby's Homeostat and Grey Walter's tortoises embodied adaptive behaviour in hardware; Hebb (1949) proposed the synaptic learning rule that still bears his name; Shannon's maze-running mouse Theseus (1950) and Oettinger's EDSAC programs (1951–52) were the first learning devices and learning programs; and Minsky's SNARC (1951) was the first neural-network learning machine. By 1955 the ingredients — stored-program computers, formal logic, neuron models, learning rules, game-playing heuristics (Shannon 1950, Samuel's checkers from 1952) — were on the table, and McCarthy's Dartmouth proposal named the field. On the map this era is the west coast: the place every later road ultimately leads back to, with the symbolic and connectionist poles already visibly distinct.

## Timeline of key events
| Year | Event | Why it matters | Source |
|------|-------|----------------|--------|
| 1666–1679 | Leibniz proposes a *characteristica universalis* and *calculus ratiocinator* — a universal formal language and mechanical rules of reasoning | The founding fantasy of mechanised reasoning; the symbolic pole's mythic origin | [1] |
| 1837–1843 | Babbage designs the Analytical Engine; Lovelace's 1843 notes describe programming it and argue it "has no pretensions to originate anything" | First general-purpose programmable machine design; "Lady Lovelace's objection" is answered by Turing in 1950 | [2], [3], [7] |
| 1854 | George Boole, *An Investigation of the Laws of Thought* | Algebra of logic: reasoning as symbol manipulation | [4] |
| 1879 | Gottlob Frege, *Begriffsschrift* | Modern predicate logic with quantifiers — the notation of symbolic AI | [5] |
| 1910–1913 | Whitehead & Russell, *Principia Mathematica* | Formal derivation of mathematics from logic; its theorems are what Logic Theorist proves in 1956 | [6] |
| 1920s | Hilbert's programme: finitary proof of consistency/completeness/decidability of mathematics | Sets up the *Entscheidungsproblem* that Church and Turing answer | [8] |
| 1931 | Gödel, "Über formal unentscheidbare Sätze…" | Incompleteness: limits of formal systems; later cited both for and against machine intelligence | [9] |
| 1936 | Church, "An Unsolvable Problem of Elementary Number Theory" (lambda calculus) | Independent negative answer to the *Entscheidungsproblem*; lambda calculus later underpins Lisp | [10] |
| 1936–37 | Turing, "On Computable Numbers, with an Application to the Entscheidungsproblem"; Post independently publishes an equivalent worker-and-boxes model in 1936 | Defines the Turing machine and the universal machine — the theoretical computer; the equivalence of Church's, Turing's, Post's and Kleene's formulations becomes the Church–Turing thesis | [11], [44] |
| 1943 | McCulloch & Pitts, "A Logical Calculus of the Ideas Immanent in Nervous Activity" | First mathematical neuron; shows neural nets can compute any logical function — birth of the connectionist pole | [12] |
| 1943 | Rosenblueth, Wiener & Bigelow, "Behavior, Purpose and Teleology" | Feedback as the basis of purposive behaviour; the cybernetics manifesto | [13] |
| 1945 | von Neumann, *First Draft of a Report on the EDVAC* | Stored-program architecture; makes general-purpose programmable computers real — first realised in the Manchester Baby (21 June 1948), prototype of the Ferranti Mark 1 | [14], [50] |
| 1946–1953 | Macy Conferences on Cybernetics (New York) | Interdisciplinary forum where Wiener, McCulloch, Pitts, von Neumann, Shannon, Bateson, Mead etc. shaped cybernetics | [15] |
| 1947 | Pitts & McCulloch, "How We Know Universals: The Perception of Auditory and Visual Forms" | First neural-net account of invariant pattern recognition (recognising a shape despite size/orientation) — the problem the perceptron and Pandemonium inherit | [33] |
| 1948 | Wiener, *Cybernetics: Or Control and Communication in the Animal and the Machine* | Names the field; feedback, control, information — the frame McCarthy will deliberately avoid in 1955 | [16] |
| 1948 | Shannon, "A Mathematical Theory of Communication" | Information theory; quantifies information, underlies later probabilistic AI | [17] |
| 1948 | Turing writes the unpublished NPL report "Intelligent Machinery" | Describes "unorganised machines" (random neural nets), learning, and search; not published until 1968 | [18] |
| 1948 | von Neumann, "The General and Logical Theory of Automata" (Hixon Symposium lecture) | Automata theory and self-reproducing automata, compared explicitly with McCulloch–Pitts nets; adjacent-field item (theory of computation) kept because it fed cellular automata / artificial life and von Neumann's later brain–computer comparisons | [34] |
| 1948 | Turing & Champernowne devise "Turochamp", a paper chess program (hand-simulated against Alick Glennie in 1952; never ran on a computer). Zuse had drafted chess routines in Plankalkül, 1942–45, likewise unrun | Earliest known chess program; direct inspiration for Prinz's 1951 Ferranti Mark 1 program | [41], [45] |
| 1948–1949 | W. Grey Walter builds the tortoises Elmer and Elsie | First autonomous electronic robots showing goal-seeking behaviour from simple circuits | [19] |
| 1949 | Hebb, *The Organization of Behavior* | Hebbian learning rule ("cells that fire together wire together") | [20] |
| 1949 | Warren Weaver's "Translation" memorandum (July 1949, Rockefeller Foundation) | Proposes computer translation via cryptanalysis, McCulloch–Pitts-style logic and language universals; launches funded MT research in the US | [35] |
| 1949 | Ross Ashby builds the Homeostat; Ratio Club founded in Britain (members include Turing, Ashby, Walter and Albert Uttley; Kenneth Craik's *The Nature of Explanation*, 1943, is its acknowledged precursor) | Ultrastability/adaptation in hardware; the UK cybernetics circle — Uttley's conditional-probability nets and Craik's mental-model theory are both cited in the 1955 Dartmouth proposal | [21], [22], [48], [49] |
| 1950 | Turing, "Computing Machinery and Intelligence", *Mind* | The imitation game (Turing test); rebuts nine objections including Lovelace's | [7] |
| 1950 | Shannon, "Programming a Computer for Playing Chess" | Minimax search with evaluation function — the template for game-playing AI | [23] |
| 1950 | Shannon builds "Theseus", a relay-driven maze-solving mechanical mouse | First electromechanical device to learn by trial and error (it remembers the maze and takes the direct path on re-entry) | [36] |
| 1950–1955 | Soviet press denounces cybernetics as a "reactionary pseudoscience" (1950–54); rehabilitation begins with articles in *Voprosy Filosofii* in 1955 | First state-level controversy over the field; delays Soviet cybernetics/AI until the Khrushchev thaw | [42] |
| 1951 | CNRS colloque *Les machines à calculer et la pensée humaine*, Paris (8–13 Jan 1951), organised by Louis Couffignal, with Wiener, Ashby and McCulloch attending | First international conference on calculating machines and thought; continental Europe's entry point to cybernetics | [37] |
| 1951 | Kleene's RAND memorandum on "regular events" in McCulloch–Pitts nerve nets (published 1956 as "Representation of Events in Nerve Nets and Finite Automata" in *Automata Studies*) | Regular expressions and finite automata born from analysing neural nets; adjacent-field item (theory of computation) kept because it fed the formal-language/grammar lineage (Chomsky hierarchy, era 02) | [38] |
| 1951 | Minsky & Edmonds build SNARC at Princeton | First neural-network learning machine (40 Hebb-style synapses, reinforcement) | [24] |
| 1951 | Strachey's draughts and Prinz's chess run on the Ferranti Mark 1 (Manchester); Strachey's love-letter generator follows on the same machine in 1952 | First game-playing programs on a stored-program computer; the love-letter generator is the first computer-generated text | [25], [46] |
| 1951–1952 | Anthony Oettinger's "response learning" and "Shopper" programs on Cambridge's EDSAC ("Programming a Digital Computer to Learn", *Phil. Mag.* 1952) | First programs written explicitly to learn (rote memory of which shop stocks what); written under Turing's influence — the earliest UK machine-learning software | [39] |
| 1952 | Ashby, *Design for a Brain* | Adaptive behaviour as a dynamical-systems property | [26] |
| 1952–1955 | Arthur Samuel writes a checkers program at IBM that learns, on the IBM 701 (IBM's first commercial scientific computer, announced May 1952; publicly demonstrated 1956; paper 1959) | Coins "machine learning"; rote learning and self-play | [27], [43] |
| 1954 | Georgetown–IBM experiment (7 Jan 1954), following the first MT conference (MIT, June 1952, organised by Yehoshua Bar-Hillel, the first full-time MT researcher) | Public demo of Russian→English machine translation; triggers a decade of MT funding, later reversed by ALPAC | [28], [40] |
| 1955 | McCarthy, Minsky, Rochester & Shannon submit the Dartmouth proposal (31 Aug 1955) | Coins the term "artificial intelligence"; the eastern border of this region | [29] |

## Key people
- **Gottfried Wilhelm Leibniz** (Hanover / Paris, 17th c.) — *calculus ratiocinator*: reasoning reduced to calculation; built a stepped-reckoner calculator. [1]
- **Charles Babbage & Ada Lovelace** (London, 1830s–40s) — Analytical Engine design; Lovelace's notes are the first published program and first argument about machine creativity. [2], [3]
- **George Boole** (Queen's College Cork) — Boolean algebra, *Laws of Thought* (1854). [4]
- **Gottlob Frege** (Jena) — predicate logic and quantifiers, *Begriffsschrift* (1879). [5]
- **David Hilbert** (Göttingen) — Hilbert's programme and the *Entscheidungsproblem*. [8]
- **Kurt Gödel** (Vienna) — incompleteness theorems (1931). [9]
- **Alonzo Church** (Princeton) — lambda calculus; Church's thesis (1936); Turing's doctoral supervisor. [10]
- **Alan Turing** (Cambridge / NPL / Manchester) — universal machine (1936), "Intelligent Machinery" (1948), the imitation game (1950). [7], [11], [18]
- **Warren McCulloch & Walter Pitts** (University of Illinois → MIT) — logical neuron model (1943) and invariant pattern recognition (1947); both central to the Macy Conferences; from 1952 McCulloch's group at MIT's Research Laboratory of Electronics (with Pitts and Lettvin, near Wiener) is the neural-modelling hub. [12], [15], [33], [51]
- **Norbert Wiener** (MIT) — *Cybernetics* (1948); feedback and control as a unifying science; *The Human Use of Human Beings* (1950) takes it to the public and to the automation debate. [13], [16], [47]
- **John von Neumann** (IAS Princeton) — EDVAC stored-program architecture (1945); automata theory and self-reproducing automata (Hixon lecture 1948); Macy participant. [14], [34]
- **Claude Shannon** (Bell Labs) — information theory (1948), chess program design (1950), the learning mouse Theseus (1950), Dartmouth co-proposer (1955). [17], [23], [29], [36]
- **Donald Hebb** (McGill) — Hebbian synaptic learning rule (1949). [20]
- **W. Ross Ashby** (Barnwood House, Gloucester) — Homeostat, *Design for a Brain* (1952); Ratio Club member. [21], [26]
- **W. Grey Walter** (Burden Neurological Institute, Bristol) — tortoise robots (1948–49). [19]
- **Marvin Minsky** (Princeton, then Harvard) — SNARC neural-net learning machine (1951); Dartmouth co-proposer. [24], [29]
- **Arthur Samuel** (IBM Poughkeepsie) — self-learning checkers program (1952–59). [27]
- **Stephen Kleene** (Wisconsin / RAND) — recursion theory alongside Church and Turing; regular events in nerve nets (1951, published 1956). [38], [44]
- **Warren Weaver** (Rockefeller Foundation) — the 1949 "Translation" memorandum that founded machine translation; also Shannon's populariser. [35]
- **Anthony Oettinger** (Cambridge, EDSAC) — first learning programs (1951–52). [39]
- **John McCarthy** (Dartmouth College) — coins "artificial intelligence" in the 1955 proposal. [29]

## Key papers / artifacts
- Turing, A. M. *On Computable Numbers, with an Application to the Entscheidungsproblem*. Proc. London Math. Soc. s2-42, 1936–37. https://www.cs.virginia.edu/~robins/Turing_Paper_1936.pdf (DOI 10.1112/plms/s2-42.1.230). [11]
- Turing, A. M. *Computing Machinery and Intelligence*. Mind LIX(236):433–460, 1950. doi:10.1093/mind/LIX.236.433 — open copy: https://redirect.cs.umbc.edu/courses/471/papers/turing.pdf [7]
- Turing, A. M. *Intelligent Machinery* (NPL report, 1948; published 1968). https://weightagnostic.github.io/papers/turing1948.pdf [18]
- McCulloch, W. S. & Pitts, W. *A Logical Calculus of the Ideas Immanent in Nervous Activity*. Bulletin of Mathematical Biophysics 5:115–133, 1943. https://doi.org/10.1007/BF02478259 [12]
- Pitts, W. & McCulloch, W. S. *How We Know Universals: The Perception of Auditory and Visual Forms*. Bulletin of Mathematical Biophysics 9:127–147, 1947. https://doi.org/10.1007/BF02478291 [33]
- Rosenblueth, A., Wiener, N. & Bigelow, J. *Behavior, Purpose and Teleology*. Philosophy of Science 10(1):18–24, 1943. https://doi.org/10.1086/286788 [13]
- Wiener, N. *Cybernetics: Or Control and Communication in the Animal and the Machine*. MIT Press / Wiley, 1948. https://archive.org/details/cyberneticsorcon00wien [16]
- Shannon, C. E. *A Mathematical Theory of Communication*. Bell System Technical Journal 27, 1948. https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf [17]
- Shannon, C. E. *Programming a Computer for Playing Chess*. Philosophical Magazine 41(314), 1950. https://vision.unipv.it/IA1/ProgrammingaComputerforPlayingChess.pdf [23]
- Hebb, D. O. *The Organization of Behavior: A Neuropsychological Theory*. Wiley, 1949. https://en.wikipedia.org/wiki/Organization_of_Behavior [20]
- Ashby, W. R. *Design for a Brain*. Chapman & Hall, 1952. https://archive.org/details/designforbrain00ashb [26]
- Gödel, K. *Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I*. Monatshefte für Mathematik und Physik 38:173–198, 1931. https://doi.org/10.1007/BF01700692 [9]
- Church, A. *An Unsolvable Problem of Elementary Number Theory*. American Journal of Mathematics 58(2):345–363, 1936. https://doi.org/10.2307/2371045 [10]
- Boole, G. *An Investigation of the Laws of Thought*. 1854. https://www.gutenberg.org/ebooks/15114 [4]
- Menabrea, L. F., trans. with notes by Ada Lovelace. *Sketch of the Analytical Engine Invented by Charles Babbage*. 1843. https://www.fourmilab.ch/babbage/sketch.html [3]
- Oettinger, A. G. *Programming a Digital Computer to Learn*. Philosophical Magazine 43(347):1243–1263, 1952. doi:10.1080/14786441208520256 (publisher page blocks automated fetch; context https://en.wikipedia.org/wiki/Anthony_Oettinger) [39]
- Kleene, S. C. *Representation of Events in Nerve Nets and Finite Automata*. In Shannon & McCarthy (eds.), *Automata Studies*, Princeton, 1956 (RAND memorandum 1951). Context: https://en.wikipedia.org/wiki/Stephen_Cole_Kleene [38]
- Samuel, A. L. *Some Studies in Machine Learning Using the Game of Checkers*. IBM Journal of Research and Development 3(3):210–229, 1959. https://doi.org/10.1147/rd.33.0210 [27]
- McCarthy, J., Minsky, M., Rochester, N. & Shannon, C. *A Proposal for the Dartmouth Summer Research Project on Artificial Intelligence*, 31 Aug 1955. http://jmc.stanford.edu/articles/dartmouth/dartmouth.pdf [29]

## Schools of thought / sub-clusters
- **Formal logic & foundations of mathematics** (Leibniz, Boole, Frege, Russell/Whitehead, Hilbert, Gödel) — reasoning as symbol manipulation under explicit rules; borders: *Computability* (east), and via *Principia* directly to Logic Theorist/GPS in era 02. [1], [4], [5], [6], [8], [9]
- **Computability / theory of computation** (Church, Turing, Post, Kleene; von Neumann architecture and automata theory 1948; Kleene's regular events 1951/56) — what can be mechanically computed at all; borders: *Formal logic* (west), *Turing test & philosophy of mind* (south-east), *Neural modelling* (Kleene's and von Neumann's automata are analyses of McCulloch–Pitts nets), Lisp/lambda-calculus and the Chomsky hierarchy in era 02, and the whole of theoretical CS (off-map). [10], [11], [14], [34], [38], [44]
- **Turing test & philosophy of machine intelligence** (Turing 1950, Lovelace objection) — behavioural criterion for intelligence; borders: ELIZA (era 02), Dreyfus/Searle critiques (era 03), Loebner/LLM-era debates (far east). [3], [7]
- **Cybernetics** (Wiener, Rosenblueth, Bigelow, Ashby, Grey Walter, Macy Conferences, Ratio Club; UK precursor Craik 1943; Couffignal's Paris colloque 1951; Soviet rejection 1950–55) — feedback, control, homeostasis, embodied adaptive machines; borders: *Neural modelling* (shared members), control theory (off-map south), and — after a long gap — behaviour-based robotics / Brooks in era 03 and reinforcement learning. [13], [15], [16], [19], [21], [22], [26], [37], [42], [48]
- **Neural modelling & learning machines** (McCulloch–Pitts 1943/1947, Hebb, Uttley's conditional-probability nets, Shannon's Theseus 1950, Minsky's SNARC, Oettinger's EDSAC programs 1951–52, Farley & Clark 1954, early Rosenblatt) — brain-inspired computation, synaptic learning and the first learning devices/programs; borders: *Cybernetics* (west/south), Rosenblatt's perceptron 1957–58 and the *Perceptrons* controversy (era 02), PDP/backprop revival (era 03). [12], [20], [24], [30], [33], [36], [39], [49]
- **Information theory & game search** (Shannon 1948/1950, Turing–Champernowne's Turochamp 1948, Samuel, Strachey, Prinz) — quantifying information; minimax + evaluation heuristics; borders: heuristic search in Newell–Simon (era 02), computer chess lineage (Deep Blue, far east), probabilistic AI (era 03+). [17], [23], [25], [27], [41]
- **Machine translation (proto-NLP)** (Weaver memo 1949, Bar-Hillel's MIT conference 1952, Georgetown–IBM 1954) — first funded "language AI"; borders: ALPAC report 1966 (era 02 winter episode), statistical NLP (east). [28], [35], [40]

## Map notes
- **A1 label:** "The Foundations" (or "Pre-AI Coast"). **A2 labels:** "Logic & Computability Highlands" (north), "Cybernetic Lowlands" (south). **A3 labels:** "Turing 1936", "Turing 1950 / Imitation Game", "McCulloch–Pitts 1943", "Macy Conferences", "Ratio Club", "Hebb 1949", "SNARC 1951", "Georgetown–IBM 1954"; candidates added in review: "Theseus 1950", "Paris colloque 1951".
- **West edge decision:** the map's coastline should start at Turing 1936 / McCulloch–Pitts 1943 as the first *land*; Leibniz→Boole→Frege→Gödel→Church should be drawn as offshore islands / an archipelago labelled "Antecedents" rather than continuous continent — they are indispensable context but not AI research.
- **Rivers/borders:** the "Hilbert–Gödel–Turing river" flows from the logic highlands south-east into Dartmouth; the "Wiener–McCulloch river" flows from the cybernetic lowlands. They meet at the 1955–56 delta (Dartmouth proposal). A range of hills ("the Symbolic Divide") should begin here and run east, separating symbolic from connectionist territory for the next three regions.
- **Bridges east:** *Principia Mathematica* → Logic Theorist (1956); lambda calculus → Lisp (1958); Hebb/SNARC → perceptron (1957–58); Shannon/Samuel game search → Newell–Simon heuristics and computer chess; Georgetown MT → ALPAC 1966.
- **Open questions for curation:** (a) how far to extend the antecedent archipelago (Llull? Hobbes' "reasoning is reckoning"? Jaquet-Droz automata?) — recommend a single "Myths & Automata" islet only; (b) whether Macy Conferences deserve A3 city status or an A4 street inside "Cybernetics"; (c) placing Turing 1948 "Intelligent Machinery" — it is chronologically connectionist (unorganised machines) yet authored by the symbolic pole's founder; suggest a mid-latitude placement.

### Archipelago / shore split (P1-T11; input to `data/continents/REGISTRY.md`)

`AXES.md` §1 (decided): the mainland west coast is 1943 (McCulloch–Pitts); everything earlier is an offshore archipelago on a log-compressed scale. This file therefore yields **two** continents. Every timeline row, school bullet and key person of this file is assigned exactly once below. Rule: an item goes to *shore* if its date is ≥ 1943; a person goes with the item that carries their AI significance (Turing: 1950, not 1936). Cross-checked against the overview histories [31], [32].

**Timeline rows (36)**

| # | Timeline row | Continent | Note |
|---|---|---|---|
| 1 | 1666–1679 Leibniz, *characteristica universalis* | archipelago (pre-1943, offshore) | outermost isle |
| 2 | 1837–1843 Babbage / Lovelace | archipelago (pre-1943, offshore) |  |
| 3 | 1854 Boole, *Laws of Thought* | archipelago (pre-1943, offshore) |  |
| 4 | 1879 Frege, *Begriffsschrift* | archipelago (pre-1943, offshore) |  |
| 5 | 1910–1913 *Principia Mathematica* | archipelago (pre-1943, offshore) | bridge to Logic Theorist (era 02) starts here |
| 6 | 1920s Hilbert's programme | archipelago (pre-1943, offshore) |  |
| 7 | 1931 Gödel, incompleteness | archipelago (pre-1943, offshore) |  |
| 8 | 1936 Church, lambda calculus | archipelago (pre-1943, offshore) |  |
| 9 | 1936–37 Turing, *On Computable Numbers* (with Post 1936) | archipelago (pre-1943, offshore) | largest, nearest isle; the shore is in sight |
| 10 | 1943 McCulloch & Pitts | shore (1943–1955) | **the west coast itself** (`AXES.md` §1) |
| 11 | 1943 Rosenblueth, Wiener & Bigelow | shore (1943–1955) |  |
| 12 | 1945 von Neumann, EDVAC report (→ Manchester Baby 1948) | shore (1943–1955) |  |
| 13 | 1946–1953 Macy Conferences | shore (1943–1955) |  |
| 14 | 1947 Pitts & McCulloch, *How We Know Universals* | shore (1943–1955) |  |
| 15 | 1948 Wiener, *Cybernetics* | shore (1943–1955) |  |
| 16 | 1948 Shannon, information theory | shore (1943–1955) |  |
| 17 | 1948 Turing, *Intelligent Machinery* | shore (1943–1955) |  |
| 18 | 1948 von Neumann, Hixon lecture on automata | shore (1943–1955) | adjacent-field item (§2.9): fed cellular automata / artificial life |
| 19 | 1948 Turing & Champernowne, Turochamp (Zuse's Plankalkül chess) | shore (1943–1955) |  |
| 20 | 1948–1949 Grey Walter's tortoises | shore (1943–1955) |  |
| 21 | 1949 Hebb, *Organization of Behavior* | shore (1943–1955) |  |
| 22 | 1949 Weaver, "Translation" memorandum | shore (1943–1955) |  |
| 23 | 1949 Ashby's Homeostat; Ratio Club (Uttley, Craik precursor) | shore (1943–1955) |  |
| 24 | 1950 Turing, *Computing Machinery and Intelligence* | shore (1943–1955) |  |
| 25 | 1950 Shannon, chess programming | shore (1943–1955) |  |
| 26 | 1950 Shannon, Theseus maze mouse | shore (1943–1955) |  |
| 27 | 1950–1955 Soviet denunciation / rehabilitation of cybernetics | shore (1943–1955) | controversy; non-US strand |
| 28 | 1951 CNRS colloque, Paris (Couffignal) | shore (1943–1955) | non-US (France) strand |
| 29 | 1951 Kleene, regular events in nerve nets | shore (1943–1955) | adjacent-field item (§2.9): fed formal-language theory |
| 30 | 1951 Minsky & Edmonds, SNARC | shore (1943–1955) |  |
| 31 | 1951 Strachey / Prinz on the Ferranti Mark 1 (love letters 1952) | shore (1943–1955) |  |
| 32 | 1951–1952 Oettinger's EDSAC learning programs | shore (1943–1955) |  |
| 33 | 1952 Ashby, *Design for a Brain* | shore (1943–1955) |  |
| 34 | 1952–1955 Samuel's checkers (IBM 701) | shore (1943–1955) |  |
| 35 | 1954 Georgetown–IBM experiment (MIT MT conference 1952) | shore (1943–1955) |  |
| 36 | 1955 Dartmouth proposal | shore (1943–1955) | eastern border; the 1956 workshop itself belongs to era 02 |

**School bullets (7)**

| School bullet | Continent | Note |
|---|---|---|
| Formal logic & foundations of mathematics | archipelago | entirely pre-1943 |
| Computability / theory of computation | archipelago | Church/Turing 1936 are isles; the von Neumann architecture (1945) item is folded into the shore's cybernetics/computing coast, not a separate school |
| Turing test & philosophy of machine intelligence | shore | anchored on 1950; the Lovelace objection (1843) is its offshore antecedent |
| Cybernetics | shore | |
| Neural modelling & learning machines | shore | |
| Information theory & game search | shore | |
| Machine translation (proto-NLP) | shore | Weaver memo 1949, Georgetown 1954 |

**Key people (21 entries)**

| Person | Continent | Anchoring item |
|---|---|---|
| Leibniz | archipelago | 1666–1679 |
| Babbage & Lovelace | archipelago | 1843 |
| Boole | archipelago | 1854 |
| Frege | archipelago | 1879 |
| Hilbert | archipelago | 1920s |
| Gödel | archipelago | 1931 |
| Church | archipelago | 1936 |
| Turing | shore | 1950 (*Computing Machinery and Intelligence*); his 1936 paper stays an isle, drawn with a causeway to the shore |
| McCulloch & Pitts | shore | 1943 (and 1947) |
| Wiener | shore | 1943 / 1948 |
| von Neumann | shore | 1945 |
| Shannon | shore | 1948 / 1950 |
| Hebb | shore | 1949 |
| Ashby | shore | 1949 / 1952 |
| Grey Walter | shore | 1948–49 |
| Minsky | shore | 1951 (SNARC) |
| Samuel | shore | 1952– |
| Kleene | shore | 1951 (regular events; his 1930s recursion theory is an isle) |
| Weaver | shore | 1949 memorandum |
| Oettinger | shore | 1951–52 |
| McCarthy | shore | 1955 proposal |

Consequences for `REGISTRY.md`: the archipelago continent has `offshore: true`, ends 1942 at the latest (V-14), sits in the reasoning bands (N1–N2) and is drawn as islands; the shore runs 1943–1955 (Dartmouth proposal), spans N1 (Turing 1950, Shannon) to S2 (Walter, Ashby, SNARC) and is the first mainland. Its eastern neighbour is the Dartmouth/symbolic continent of era 02.

## Sources
[1] Leibniz's Influence on 19th Century Logic — Stanford Encyclopedia of Philosophy — https://plato.stanford.edu/entries/leibniz-logic-influence/ (accessed 2026-09-06)
[2] Analytical Engine — Wikipedia — https://en.wikipedia.org/wiki/Analytical_Engine (accessed 2026-09-06)
[3] Menabrea/Lovelace, Sketch of the Analytical Engine (1843) — https://www.fourmilab.ch/babbage/sketch.html (accessed 2026-09-06)
[4] Boole, An Investigation of the Laws of Thought (1854) — Project Gutenberg — https://www.gutenberg.org/ebooks/15114 (accessed 2026-09-06)
[5] Begriffsschrift — Wikipedia — https://en.wikipedia.org/wiki/Begriffsschrift (accessed 2026-09-06)
[6] Principia Mathematica — Wikipedia — https://en.wikipedia.org/wiki/Principia_Mathematica (accessed 2026-09-06)
[7] Turing, Computing Machinery and Intelligence, Mind 1950 — doi:10.1093/mind/LIX.236.433; open copy https://redirect.cs.umbc.edu/courses/471/papers/turing.pdf ; context https://en.wikipedia.org/wiki/Computing_Machinery_and_Intelligence (accessed 2026-09-06)
[8] Hilbert's Program — Stanford Encyclopedia of Philosophy — https://plato.stanford.edu/entries/hilbert-program/ (accessed 2026-09-06)
[9] Gödel, Über formal unentscheidbare Sätze… (1931) — https://doi.org/10.1007/BF01700692 (accessed 2026-09-06)
[10] Church, An Unsolvable Problem of Elementary Number Theory (1936) — https://doi.org/10.2307/2371045 (accessed 2026-09-06)
[11] Turing, On Computable Numbers (1936) — https://www.cs.virginia.edu/~robins/Turing_Paper_1936.pdf ; context https://en.wikipedia.org/wiki/Turing_machine (accessed 2026-09-06)
[12] McCulloch & Pitts, A Logical Calculus… (1943) — https://doi.org/10.1007/BF02478259 ; context https://en.wikipedia.org/wiki/Warren_Sturgis_McCulloch (accessed 2026-09-06)
[13] Rosenblueth, Wiener & Bigelow, Behavior, Purpose and Teleology (1943) — https://doi.org/10.1086/286788 (accessed 2026-09-06)
[14] First Draft of a Report on the EDVAC — Wikipedia — https://en.wikipedia.org/wiki/First_Draft_of_a_Report_on_the_EDVAC (accessed 2026-09-06)
[15] Macy conferences — Wikipedia — https://en.wikipedia.org/wiki/Macy_conferences (accessed 2026-09-06)
[16] Wiener, Cybernetics (1948) — https://archive.org/details/cyberneticsorcon00wien ; context https://en.wikipedia.org/wiki/Cybernetics (accessed 2026-09-06)
[17] Shannon, A Mathematical Theory of Communication (1948) — https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf (accessed 2026-09-06)
[18] Turing, Intelligent Machinery (1948) — https://weightagnostic.github.io/papers/turing1948.pdf ; context https://en.wikipedia.org/wiki/Alan_Turing (accessed 2026-09-06)
[19] William Grey Walter / tortoise robots — https://en.wikipedia.org/wiki/William_Grey_Walter and https://en.wikipedia.org/wiki/Turtle_%28robot%29 (accessed 2026-09-06)
[20] Hebb, The Organization of Behavior (1949) — https://en.wikipedia.org/wiki/Organization_of_Behavior ; Hebbian theory https://en.wikipedia.org/wiki/Hebbian_theory (accessed 2026-09-06)
[21] Homeostat — Wikipedia — https://en.wikipedia.org/wiki/Homeostat ; W. Ross Ashby https://en.wikipedia.org/wiki/W._Ross_Ashby (accessed 2026-09-06)
[22] Ratio Club — Wikipedia — https://en.wikipedia.org/wiki/Ratio_Club (accessed 2026-09-06)
[23] Shannon, Programming a Computer for Playing Chess (1950) — https://vision.unipv.it/IA1/ProgrammingaComputerforPlayingChess.pdf (accessed 2026-09-06)
[24] SNARC (Stochastic Neural Analog Reinforcement Calculator) — Wikipedia — https://en.wikipedia.org/wiki/Stochastic_neural_analog_reinforcement_calculator (accessed 2026-09-06)
[25] Ferranti Mark 1 — Wikipedia — https://en.wikipedia.org/wiki/Ferranti_Mark_1 ; Christopher Strachey https://en.wikipedia.org/wiki/Christopher_Strachey ; Dietrich Prinz https://en.wikipedia.org/wiki/Dietrich_Prinz (accessed 2026-09-06)
[26] Ashby, Design for a Brain (1952) — https://archive.org/details/designforbrain00ashb (accessed 2026-09-06)
[27] Samuel, Some Studies in Machine Learning Using the Game of Checkers (1959) — https://doi.org/10.1147/rd.33.0210 ; context https://en.wikipedia.org/wiki/Arthur_Samuel_%28computer_scientist%29 (accessed 2026-09-06)
[28] Georgetown–IBM experiment — Wikipedia — https://en.wikipedia.org/wiki/Georgetown%E2%80%93IBM_experiment (accessed 2026-09-06)
[29] McCarthy et al., A Proposal for the Dartmouth Summer Research Project on Artificial Intelligence (1955) — http://jmc.stanford.edu/articles/dartmouth/dartmouth.pdf ; context https://en.wikipedia.org/wiki/Dartmouth_workshop (accessed 2026-09-06)
[30] Farley & Clark, Simulation of Self-Organizing Systems by Digital Computer (1954) — https://doi.org/10.1109/TIT.1954.1057468 (accessed 2026-09-06)
[31] History of artificial intelligence — Wikipedia (overview used for cross-checking) — https://en.wikipedia.org/wiki/History_of_artificial_intelligence (accessed 2026-09-06)
[32] AAAI, A Brief History of AI — https://aitopics.org/misc/brief-history (accessed 2026-09-06)
[33] Pitts & McCulloch, How We Know Universals: The Perception of Auditory and Visual Forms (1947) — https://doi.org/10.1007/BF02478291 ; context https://en.wikipedia.org/wiki/Warren_Sturgis_McCulloch (accessed 2026-09-06)
[34] von Neumann, The General and Logical Theory of Automata (Hixon Symposium, 1948; publ. 1951) — https://www.vordenker.de/ggphilosophy/jvn_the-general-and-logical-theory-of-automata.pdf ; context https://en.wikipedia.org/wiki/Cellular_automaton and https://en.wikipedia.org/wiki/Von_Neumann_universal_constructor (accessed 2026-09-06)
[35] Warren Weaver — Wikipedia (the 1949 "Translation" memorandum) — https://en.wikipedia.org/wiki/Warren_Weaver ; context https://en.wikipedia.org/wiki/History_of_machine_translation (accessed 2026-09-06)
[36] Claude Shannon — Wikipedia (Theseus, 1950) — https://en.wikipedia.org/wiki/Claude_Shannon (accessed 2026-09-06)
[37] Louis Couffignal — Wikipédia (fr; colloque CNRS "Les machines à calculer et la pensée humaine", 8–13 Jan 1951) — https://fr.wikipedia.org/wiki/Louis_Couffignal ; English context https://en.wikipedia.org/wiki/Louis_Couffignal (accessed 2026-09-06)
[38] Stephen Cole Kleene — Wikipedia (regular events, RAND 1951; Automata Studies 1956) — https://en.wikipedia.org/wiki/Stephen_Cole_Kleene ; https://en.wikipedia.org/wiki/Regular_expression ; https://en.wikipedia.org/wiki/Automata_theory (accessed 2026-09-06)
[39] Oettinger, Programming a Digital Computer to Learn, Phil. Mag. 43:1243–1263 (1952) — Crossref record https://api.crossref.org/works/10.1080/14786441208520256 ; context https://en.wikipedia.org/wiki/Anthony_Oettinger (accessed 2026-09-06)
[40] Yehoshua Bar-Hillel — Wikipedia (first full-time MT researcher, MIT 1951; first MT conference 1952) — https://en.wikipedia.org/wiki/Yehoshua_Bar-Hillel (accessed 2026-09-06)
[41] Turochamp — Wikipedia — https://en.wikipedia.org/wiki/Turochamp (accessed 2026-09-06)
[42] Cybernetics in the Soviet Union — Wikipedia — https://en.wikipedia.org/wiki/Cybernetics_in_the_Soviet_Union (accessed 2026-09-06)
[43] IBM 701 — Wikipedia — https://en.wikipedia.org/wiki/IBM_701 (accessed 2026-09-06)
[44] Emil Leon Post — Wikipedia (1936 Post machine) — https://en.wikipedia.org/wiki/Emil_Leon_Post ; Church–Turing thesis https://en.wikipedia.org/wiki/Church%E2%80%93Turing_thesis (accessed 2026-09-06)
[45] Plankalkül — Wikipedia (Zuse's chess program, 1942–45) — https://en.wikipedia.org/wiki/Plankalk%C3%BCl (accessed 2026-09-06)
[46] Strachey love letter algorithm — Wikipedia — https://en.wikipedia.org/wiki/Strachey_love_letter_algorithm (accessed 2026-09-06)
[47] Wiener, The Human Use of Human Beings (1950) — https://en.wikipedia.org/wiki/The_Human_Use_of_Human_Beings (accessed 2026-09-06)
[48] Kenneth Craik — Wikipedia (The Nature of Explanation, 1943; Ratio Club precursor) — https://en.wikipedia.org/wiki/Kenneth_Craik (accessed 2026-09-06)
[49] Albert Uttley — Wikipedia (conditional-probability nets; named the Ratio Club) — https://en.wikipedia.org/wiki/Albert_Uttley (accessed 2026-09-06)
[50] Manchester Baby — Wikipedia (first stored-program computer, 21 June 1948) — https://en.wikipedia.org/wiki/Manchester_Baby (accessed 2026-09-06)
[51] Walter Pitts — Wikipedia (MIT / RLE group with McCulloch, Lettvin, Wiener) — https://en.wikipedia.org/wiki/Walter_Pitts (accessed 2026-09-06)
