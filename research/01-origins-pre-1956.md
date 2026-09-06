# Origins: Logic, Computability and Cybernetics (pre-1956)

> **Status:** verified
> **Date range:** 1666–1955 (dense core 1936–1955; thin antecedent strip back to Leibniz/Boole/Babbage)
> **Map placement (proposed):** X = far west edge, up to 1955; Y = mixed — a northern *symbolic/logic pole* strand (Leibniz → Boole → Frege → Hilbert → Gödel → Church → Turing) and a southern *connectionist/cybernetic pole* strand (McCulloch–Pitts → Wiener → Ashby → Hebb → SNARC → early perceptron work), converging on the 1956 Dartmouth border
> **Altitude:** A1 continent ("Foundations / Pre-AI"); A2 countries ("Mathematical Logic & Computability", "Cybernetics & Neural Modelling"); A3 cities (Turing 1936, Turing 1950, McCulloch–Pitts 1943, Macy Conferences, Ratio Club); A4 streets (individual papers/machines)

## One-paragraph summary
Before anyone called it "artificial intelligence", two intellectual rivers were already flowing toward it. The first is the **logic/computability** river: Leibniz's dream of a *calculus ratiocinator*, Boole's algebra of thought (1854), Frege's *Begriffsschrift* (1879), Hilbert's programme to formalise all mathematics, Gödel's incompleteness theorems (1931), and then in 1936 Church's lambda calculus and Turing's universal machine, which together answered Hilbert's *Entscheidungsproblem* in the negative and, as a by-product, defined what a computer *is*. Turing then asked in 1950 whether such a machine could think, proposing the imitation game. The second is the **cybernetic/neural** river: McCulloch and Pitts (1943) showed networks of idealised neurons could compute any logical function; Wiener's *Cybernetics* (1948) and the Macy Conferences (1946–1953) built an interdisciplinary science of feedback and control; Ashby's Homeostat and Grey Walter's tortoises embodied adaptive behaviour in hardware; Hebb (1949) proposed the synaptic learning rule that still bears his name; and Minsky's SNARC (1951) was the first neural-network learning machine. By 1955 the ingredients — stored-program computers, formal logic, neuron models, learning rules, game-playing heuristics (Shannon 1950, Samuel's checkers from 1952) — were on the table, and McCarthy's Dartmouth proposal named the field. On the map this era is the west coast: the place every later road ultimately leads back to, with the symbolic and connectionist poles already visibly distinct.

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
| 1936–37 | Turing, "On Computable Numbers, with an Application to the Entscheidungsproblem" | Defines the Turing machine and the universal machine — the theoretical computer | [11] |
| 1943 | McCulloch & Pitts, "A Logical Calculus of the Ideas Immanent in Nervous Activity" | First mathematical neuron; shows neural nets can compute any logical function — birth of the connectionist pole | [12] |
| 1943 | Rosenblueth, Wiener & Bigelow, "Behavior, Purpose and Teleology" | Feedback as the basis of purposive behaviour; the cybernetics manifesto | [13] |
| 1945 | von Neumann, *First Draft of a Report on the EDVAC* | Stored-program architecture; makes general-purpose programmable computers real | [14] |
| 1946–1953 | Macy Conferences on Cybernetics (New York) | Interdisciplinary forum where Wiener, McCulloch, Pitts, von Neumann, Shannon, Bateson, Mead etc. shaped cybernetics | [15] |
| 1948 | Wiener, *Cybernetics: Or Control and Communication in the Animal and the Machine* | Names the field; feedback, control, information — the frame McCarthy will deliberately avoid in 1955 | [16] |
| 1948 | Shannon, "A Mathematical Theory of Communication" | Information theory; quantifies information, underlies later probabilistic AI | [17] |
| 1948 | Turing writes the unpublished NPL report "Intelligent Machinery" | Describes "unorganised machines" (random neural nets), learning, and search; not published until 1968 | [18] |
| 1948–1949 | W. Grey Walter builds the tortoises Elmer and Elsie | First autonomous electronic robots showing goal-seeking behaviour from simple circuits | [19] |
| 1949 | Hebb, *The Organization of Behavior* | Hebbian learning rule ("cells that fire together wire together") | [20] |
| 1949 | Ross Ashby builds the Homeostat; Ratio Club founded in Britain | Ultrastability/adaptation in hardware; UK cybernetics circle including Turing, Ashby, Walter | [21], [22] |
| 1950 | Turing, "Computing Machinery and Intelligence", *Mind* | The imitation game (Turing test); rebuts nine objections including Lovelace's | [7] |
| 1950 | Shannon, "Programming a Computer for Playing Chess" | Minimax search with evaluation function — the template for game-playing AI | [23] |
| 1951 | Minsky & Edmonds build SNARC at Princeton | First neural-network learning machine (40 Hebb-style synapses, reinforcement) | [24] |
| 1951 | Strachey's draughts and Prinz's chess run on the Ferranti Mark 1 (Manchester) | First game-playing programs on a stored-program computer | [25] |
| 1952 | Ashby, *Design for a Brain* | Adaptive behaviour as a dynamical-systems property | [26] |
| 1952–1955 | Arthur Samuel writes a checkers program at IBM that learns (publicly demonstrated 1956; paper 1959) | Coins "machine learning"; rote learning and self-play | [27] |
| 1954 | Georgetown–IBM experiment (7 Jan 1954) | Public demo of Russian→English machine translation; triggers a decade of MT funding, later reversed by ALPAC | [28] |
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
- **Warren McCulloch & Walter Pitts** (University of Illinois → MIT) — logical neuron model (1943); both central to the Macy Conferences. [12], [15]
- **Norbert Wiener** (MIT) — *Cybernetics* (1948); feedback and control as a unifying science. [13], [16]
- **John von Neumann** (IAS Princeton) — EDVAC stored-program architecture (1945); automata theory; Macy participant. [14]
- **Claude Shannon** (Bell Labs) — information theory (1948), chess program design (1950), Dartmouth co-proposer (1955). [17], [23], [29]
- **Donald Hebb** (McGill) — Hebbian synaptic learning rule (1949). [20]
- **W. Ross Ashby** (Barnwood House, Gloucester) — Homeostat, *Design for a Brain* (1952); Ratio Club member. [21], [26]
- **W. Grey Walter** (Burden Neurological Institute, Bristol) — tortoise robots (1948–49). [19]
- **Marvin Minsky** (Princeton, then Harvard) — SNARC neural-net learning machine (1951); Dartmouth co-proposer. [24], [29]
- **Arthur Samuel** (IBM Poughkeepsie) — self-learning checkers program (1952–59). [27]
- **John McCarthy** (Dartmouth College) — coins "artificial intelligence" in the 1955 proposal. [29]

## Key papers / artifacts
- Turing, A. M. *On Computable Numbers, with an Application to the Entscheidungsproblem*. Proc. London Math. Soc. s2-42, 1936–37. https://www.cs.virginia.edu/~robins/Turing_Paper_1936.pdf (DOI 10.1112/plms/s2-42.1.230). [11]
- Turing, A. M. *Computing Machinery and Intelligence*. Mind LIX(236):433–460, 1950. doi:10.1093/mind/LIX.236.433 — open copy: https://redirect.cs.umbc.edu/courses/471/papers/turing.pdf [7]
- Turing, A. M. *Intelligent Machinery* (NPL report, 1948; published 1968). https://weightagnostic.github.io/papers/turing1948.pdf [18]
- McCulloch, W. S. & Pitts, W. *A Logical Calculus of the Ideas Immanent in Nervous Activity*. Bulletin of Mathematical Biophysics 5:115–133, 1943. https://doi.org/10.1007/BF02478259 [12]
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
- Samuel, A. L. *Some Studies in Machine Learning Using the Game of Checkers*. IBM Journal of Research and Development 3(3):210–229, 1959. https://doi.org/10.1147/rd.33.0210 [27]
- McCarthy, J., Minsky, M., Rochester, N. & Shannon, C. *A Proposal for the Dartmouth Summer Research Project on Artificial Intelligence*, 31 Aug 1955. http://jmc.stanford.edu/articles/dartmouth/dartmouth.pdf [29]

## Schools of thought / sub-clusters
- **Formal logic & foundations of mathematics** (Leibniz, Boole, Frege, Russell/Whitehead, Hilbert, Gödel) — reasoning as symbol manipulation under explicit rules; borders: *Computability* (east), and via *Principia* directly to Logic Theorist/GPS in era 02. [1], [4], [5], [6], [8], [9]
- **Computability / theory of computation** (Church, Turing, Post, Kleene; von Neumann architecture) — what can be mechanically computed at all; borders: *Formal logic* (west), *Turing test & philosophy of mind* (south-east), Lisp/lambda-calculus in era 02, and the whole of theoretical CS (off-map). [10], [11], [14]
- **Turing test & philosophy of machine intelligence** (Turing 1950, Lovelace objection) — behavioural criterion for intelligence; borders: ELIZA (era 02), Dreyfus/Searle critiques (era 03), Loebner/LLM-era debates (far east). [3], [7]
- **Cybernetics** (Wiener, Rosenblueth, Bigelow, Ashby, Grey Walter, Macy Conferences, Ratio Club) — feedback, control, homeostasis, embodied adaptive machines; borders: *Neural modelling* (shared members), control theory (off-map south), and — after a long gap — behaviour-based robotics / Brooks in era 03 and reinforcement learning. [13], [15], [16], [19], [21], [22], [26]
- **Neural modelling & learning machines** (McCulloch–Pitts, Hebb, Minsky's SNARC, Farley & Clark 1954, early Rosenblatt) — brain-inspired computation and synaptic learning; borders: *Cybernetics* (west/south), Rosenblatt's perceptron 1957–58 and the *Perceptrons* controversy (era 02), PDP/backprop revival (era 03). [12], [20], [24], [30]
- **Information theory & game search** (Shannon 1948/1950, Samuel, Strachey, Prinz) — quantifying information; minimax + evaluation heuristics; borders: heuristic search in Newell–Simon (era 02), computer chess lineage (Deep Blue, far east), probabilistic AI (era 03+). [17], [23], [25], [27]
- **Machine translation (proto-NLP)** (Weaver memo 1949, Georgetown–IBM 1954) — first funded "language AI"; borders: ALPAC report 1966 (era 02 winter episode), statistical NLP (east). [28]

## Map notes
- **A1 label:** "The Foundations" (or "Pre-AI Coast"). **A2 labels:** "Logic & Computability Highlands" (north), "Cybernetic Lowlands" (south). **A3 labels:** "Turing 1936", "Turing 1950 / Imitation Game", "McCulloch–Pitts 1943", "Macy Conferences", "Ratio Club", "Hebb 1949", "SNARC 1951", "Georgetown–IBM 1954".
- **West edge decision:** the map's coastline should start at Turing 1936 / McCulloch–Pitts 1943 as the first *land*; Leibniz→Boole→Frege→Gödel→Church should be drawn as offshore islands / an archipelago labelled "Antecedents" rather than continuous continent — they are indispensable context but not AI research.
- **Rivers/borders:** the "Hilbert–Gödel–Turing river" flows from the logic highlands south-east into Dartmouth; the "Wiener–McCulloch river" flows from the cybernetic lowlands. They meet at the 1955–56 delta (Dartmouth proposal). A range of hills ("the Symbolic Divide") should begin here and run east, separating symbolic from connectionist territory for the next three regions.
- **Bridges east:** *Principia Mathematica* → Logic Theorist (1956); lambda calculus → Lisp (1958); Hebb/SNARC → perceptron (1957–58); Shannon/Samuel game search → Newell–Simon heuristics and computer chess; Georgetown MT → ALPAC 1966.
- **Open questions for curation:** (a) how far to extend the antecedent archipelago (Llull? Hobbes' "reasoning is reckoning"? Jaquet-Droz automata?) — recommend a single "Myths & Automata" islet only; (b) whether Macy Conferences deserve A3 city status or an A4 street inside "Cybernetics"; (c) placing Turing 1948 "Intelligent Machinery" — it is chronologically connectionist (unorganised machines) yet authored by the symbolic pole's founder; suggest a mid-latitude placement.

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
