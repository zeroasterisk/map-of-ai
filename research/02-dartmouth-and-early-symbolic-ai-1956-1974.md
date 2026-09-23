# Dartmouth and the Golden Age of Symbolic AI (1956–1974)

> **Status:** reviewed
> **Date range:** 1956–1974
> **Map placement (proposed):** X = 1956–1974; Y = predominantly *symbolic/logic pole* (Logic Theorist, GPS, Lisp, theorem proving, SHRDLU, Shakey, semantic nets), with a shrinking *connectionist/cybernetic* strip in the south (perceptron, ADALINE) that is nearly cut off after *Perceptrons* (1969); ELIZA and machine translation sit mixed/central
> **Altitude:** A1 continent ("Symbolic AI / The Golden Age"); A2 countries ("Heuristic Search & Problem Solving", "Lisp & Logic", "Micro-worlds & Language", "Robotics & Planning", "Perceptron Country"); A3 cities (Dartmouth 1956, Logic Theorist, Lisp 1958, Perceptron 1958, ELIZA, Shakey, SHRDLU, *Perceptrons* 1969, Lighthill 1973); A4 streets (individual papers/programs)

## One-paragraph summary
The Dartmouth Summer Research Project of 1956 gave the field its name and its first cohort — McCarthy, Minsky, Newell, Simon, Shannon, Rochester, Selfridge, Solomonoff and others — and Newell, Shaw and Simon's Logic Theorist, which proved theorems from *Principia Mathematica*, gave it a founding artefact. What followed was two decades of exuberant, mostly symbolic work: heuristic search formalised as the General Problem Solver (1959) and the physical-symbol-system hypothesis; McCarthy's Lisp (1958) and "Programs with Common Sense" (1959) proposing logic-based commonsense reasoning; Minsky's "Steps Toward Artificial Intelligence" (1961) surveying the agenda; Robinson's resolution principle (1965) launching automated theorem proving and, eventually, Prolog (1972); ELIZA (1966) exposing how easily people attribute understanding; Shakey the robot (1966–72) integrating perception, A* search and STRIPS planning; and Winograd's SHRDLU (1968–70) apparently "understanding" English in a blocks world. New labs (MIT AI Lab, Stanford SAIL, CMU, SRI, Edinburgh) were lavishly funded by DARPA/ARPA, and leaders predicted human-level machines within a generation. Meanwhile Rosenblatt's perceptron (1957–58) and Widrow–Hoff's ADALINE (1960) carried the connectionist banner until Minsky and Papert's *Perceptrons* (1969) and the funding climate marginalised neural nets for a decade. The ALPAC report (1966) killed machine-translation funding, the Mansfield Amendment (1969) redirected DARPA to mission-oriented work, Dreyfus published *What Computers Can't Do* (1972), and the Lighthill Report (1973) and DARPA cutbacks of 1973–74 closed the era in the first AI winter. On the map this is the great symbolic plateau: broad, confident, and ending abruptly at a cliff.

## Timeline of key events
| Year | Event | Why it matters | Source |
|------|-------|----------------|--------|
| 1956 | Dartmouth Summer Research Project on Artificial Intelligence (Hanover, NH; ~6–8 weeks) | Founding event; term "artificial intelligence" adopted; organisers McCarthy, Minsky, Rochester, Shannon | [1] |
| 1956 | Newell, Shaw & Simon complete Logic Theorist; presented at Dartmouth | First program deliberately engineered for automated reasoning; proved 38 of the first 52 theorems of *Principia* ch. 2 | [2], [3] |
| 1956–1959 | Samuel's IBM checkers program matures; 1959 paper coins "machine learning" | First widely known self-learning program; rote learning, self-play and a learned evaluation function | [4] |
| 1957 | Rosenblatt begins perceptron work at Cornell Aeronautical Laboratory; 1958 *Psychological Review* paper | The connectionist flagship; Mark I Perceptron hardware demonstrated 1960 | [5], [6] |
| 1957 | Chomsky, *Syntactic Structures* | Generative grammar and the formal-language hierarchy; frames language as rule-governed symbol manipulation for NLP | [58] |
| 1958 | McCarthy designs Lisp at MIT (paper 1960) | Language of AI for 30+ years; list processing, recursion, garbage collection | [7] |
| 1958–59 | Gelernter (with Rochester, IBM) builds the Geometry Theorem Prover; FLPL list-processing extension of Fortran written for it | Third AI program after LT and checkers; first to prune proof search with a diagram ("semantic model") of the problem | [35], [37] |
| 1958–59 | Selfridge, "Pandemonium: A Paradigm for Learning" (Teddington symposium Nov 1958; proceedings 1959) | Parallel feature-demon architecture; ancestor of blackboard systems and layered recognition | [8] |
| 1959 | McCarthy, "Programs with Common Sense" (Advice Taker) | Manifesto for logic-based knowledge representation and commonsense reasoning | [9] |
| 1959 | Newell, Shaw & Simon, General Problem Solver (GPS) | Means–ends analysis; separates problem-solving strategy from domain knowledge | [10] |
| 1959 | Hao Wang's IBM 704 program proves several hundred *Principia* propositional/predicate theorems in about nine minutes | Algorithmic (non-heuristic) theorem proving outperforms LT; opens the logician's route to resolution | [39] |
| 1959 | MIT AI project founded by McCarthy & Minsky (becomes MIT AI Lab 1970) | One of the three main US AI centres (with Stanford, CMU) | [11] |
| 1959 | Lettvin, Maturana, McCulloch & Pitts, "What the Frog's Eye Tells the Frog's Brain" | Retinal cells as feature detectors; adjacent-field item (neuroscience) kept because it fed feature-based vision | [59], [60] |
| 1959 | Hubel & Wiesel record receptive fields of single neurons in cat visual cortex (Nobel 1981) | Orientation-selective, hierarchical cells; adjacent-field item (neuroscience) kept because it fed the Neocognitron and CNNs | [61], [62] |
| 1959 | Bledsoe (with Browning) introduces the n-tuple method | Early learned pattern-recognition method | [63] |
| 1960 | Widrow & Hoff, ADALINE and the LMS (delta) rule; MADALINE (1962); SRI's MINOS I–III perceptron machines under Rosen and Brain (1960–68, funding ends 1966) | Gradient-based learning for linear units; direct ancestor of backprop-era training; MINOS shows the hardware strand also ran at SRI | [12], [28] |
| 1960 | Licklider, "Man-Computer Symbiosis" (IRE Transactions; the Wikipedia article's 1962 is the journal's end date) | Human–computer partnership agenda; Licklider then directs IPTO | [64], [65] |
| 1961 | Minsky, "Steps Toward Artificial Intelligence" | Survey/agenda of search, pattern recognition, learning, planning, induction | [13] |
| 1961 | Slagle's SAINT (MIT PhD under Minsky, written in Lisp) solves freshman-calculus symbolic integration | Heuristic problem solving in a formal domain; lineage runs to Moses's SIN and Project MAC's Macsyma (1968–) | [35], [36], [38], [54] |
| 1961 | Michie holds a tournament against MENACE, his 304-matchbox noughts-and-crosses learner | Reinforcement learning demonstrated with no computer at all | [66] |
| 1961 | Unimate industrial robot starts work on a General Motors assembly line (Devol patent 1954, granted 1961) | First industrial robot in production; industrial branch of robotics | [67] |
| 1962–63 | ARPA's Information Processing Techniques Office created (Licklider first director, Oct 1962); Project MAC launched at MIT 1 July 1963 on a $2M ARPA grant, housing the Minsky–McCarthy AI Group | The funding engine of the golden age: ARPA money flows to MIT, CMU and Stanford with few strings until the Mansfield Amendment | [11], [43] |
| 1962 | Rosenblatt, *Principles of Neurodynamics: Perceptrons and the Theory of Brain Mechanisms* | Book-length statement of the perceptron programme, the target of Minsky & Papert (1969) | [53] |
| 1962 | Glushkov founds the Institute of Cybernetics in Kiev and becomes its first director | Soviet cybernetics centre; the institute where Ivakhnenko's GMDH (1968) is later developed | [68] |
| 1963 | McCarthy (at Stanford from 1962) starts the Stanford AI Laboratory (SAIL) | Second major US centre; home of later robotics, vision and hand–eye work | [14] |
| 1963 | Feigenbaum & Feldman (eds.), *Computers and Thought*; Roberts's MIT thesis "Machine Perception of Three-Dimensional Solids" | First AI anthology (its royalties fund the IJCAI Computers and Thought Award from 1971); Roberts's blocks-world edge detection starts computer vision, followed by the over-optimistic MIT Summer Vision Project (1966) | [35], [42], [50] |
| 1963–64 | MIT AI Group PhDs: Evans's ANALOGY (1963, IQ-test geometric analogies), Bobrow's STUDENT (1964, algebra word problems, Project MAC TR-1), Raphael's SIR (1964, logical question answering) | The "semantic information processing" programs (collected in Minsky's 1968 volume) that made micro-domain "understanding" the MIT style | [35], [40], [41] |
| 1963 | Ivan Sutherland's Sketchpad (MIT PhD thesis) | Interactive graphical man–machine communication; object-based drawing | [69] |
| 1964 | Solomonoff, "A Formal Theory of Inductive Inference", Parts I–II | Algorithmic probability: the probabilistic-learning minority report of the Dartmouth cohort; root of Kolmogorov complexity and universal induction | [49] |
| 1965 | Edinburgh's Department of Machine Intelligence and Perception established under Donald Michie (from the earlier Experimental Programming Unit) | UK centre of AI; later target of the Lighthill Report | [15] |
| 1965 | J. A. Robinson, resolution principle | Complete inference rule for first-order logic; foundation of theorem proving and Prolog | [16] |
| 1965 | Dendral begins at Stanford (Feigenbaum, Lederberg, Buchanan) | First expert system: knowledge-intensive rather than general search — the seed of era 03 | [17] |
| 1965 | Simon predicts "machines will be capable, within twenty years, of doing any work a man can do" (he had already predicted in 1957 that a computer would be chess champion within ten years) | Emblematic over-prediction that fed the later backlash | [18] |
| 1965 | Zadeh, "Fuzzy sets" | Graded membership; root of fuzzy logic and fuzzy control | [70], [71] |
| 1965 | Gordon Moore observes that components per integrated circuit double on a regular schedule (Moore's law) | Adjacent-field item (hardware) kept because it fed the compute-scaling expectation behind later AI | [72] |
| 1966 | ALPAC report ends US machine-translation funding (the case had been made by Bar-Hillel in 1960: fully automatic high-quality MT is infeasible) | First funded-AI collapse; "winter" episode within the golden age | [19], [55] |
| 1966 | Weizenbaum's ELIZA / DOCTOR script (paper in CACM) | Pattern-matching chatbot; the "ELIZA effect" | [20] |
| 1966–1972 | Shakey the Robot at SRI (Rosen, Nilsson, Hart) | First mobile robot reasoning about its actions; yields A* (1968) and STRIPS (1971) | [21], [22], [23] |
| 1966–67 | Kotok–McCarthy chess program (MIT 1959–62, run at Stanford) loses a nine-month telegraph match 3–1 to the ITEP program (Adelson-Velsky, Arlazarov, Bitman, Uskov; Moscow) | First computer-vs-computer chess match and the most visible Soviet AI result of the era; ITEP lineage becomes Kaissa | [36], [46] |
| 1966–67 | Greenblatt's Mac Hack VI plays in human chess tournaments at MIT | First chess program to play under tournament conditions, receive a USCF rating, and beat a person in tournament play | [24] |
| 1966 | Alan Perlis receives the first ACM Turing Award | Computing's top prize begins; AI researchers are among its early laureates | [73] |
| 1967 | Cover & Hart, "Nearest neighbor pattern classification" | Error bound for the nearest-neighbour rule (Fix & Hodges 1951) — early statistical learning theory | [74] |
| 1967 | Amari, "A Theory of Adaptive Pattern Classifiers": a multilayer network trained by stochastic gradient descent | Japanese headwater of deep learning, outside the US perceptron debate | [75], [76] |
| 1968 | Quillian's semantic networks (PhD 1966; *Semantic Information Processing*, ed. Minsky, 1968) | Graph-based knowledge representation; ancestor of frames, ontologies, knowledge graphs | [25] |
| 1968 | Ivakhnenko's Group Method of Data Handling (Institute of Cybernetics, Kyiv) | Inductive training of layered polynomial networks — eight layers deep by 1971 — outside the US perceptron debate; a Soviet ancestor of deep learning | [48] |
| 1968 | HAL 9000 in Kubrick's *2001: A Space Odyssey* | Adjacent-field item (fiction) kept because it fed the public image of general machine intelligence gone wrong | [77] |
| 1968 | Engelbart's "Mother of All Demos" of the NLS system (9 December 1968, San Francisco) | Mouse, hypertext and collaboration shown in one system — the augmentation counterpoint to AI | [78] |
| 1969 | McCarthy & Hayes, "Some Philosophical Problems from the Standpoint of AI" (situation calculus, frame problem); Hewitt's PLANNER (Micro-Planner is SHRDLU's implementation language) | Names the frame problem that dogs logic-based AI; PLANNER's procedural knowledge is the scruffy counter-proposal to resolution | [44], [45] |
| 1969 | Minsky & Papert, *Perceptrons* | Proves single-layer perceptrons can't compute XOR/connectedness; widely credited with chilling neural-net funding | [26] |
| 1969 | First IJCAI held in Washington, D.C.; Mansfield Amendment requires DARPA to fund mission-oriented research; Elsevier's journal *Artificial Intelligence* founded 1970 | Field gets its conference and journal; funding regime starts to tighten | [27], [28], [56] |
| 1969 | First ARPANET host-to-host connection, SRI–UCLA (29 October 1969) | Links the ARPA-funded AI labs; adjacent-field item (networking) kept because it fed shared AI tooling | [79] |
| 1969 | Minsky receives the ACM Turing Award | AI's founding generation gains computing's top honour three years after the prize begins | [30] |
| 1970 | Winograd's SHRDLU (MIT PhD, 1968–70) | Natural-language understanding in a blocks micro-world; peak of the micro-worlds programme | [29] |
| 1970 | Minsky (in *Life*) predicts a machine with average human intelligence "in from three to eight years" | The most quoted over-promise of the era | [30] |
| 1970 | Woods, "Transition Network Grammars for Natural Language Analysis" (augmented transition networks) | Recursive parsing formalism used in NL question answering and speech understanding | [80], [81] |
| 1971 | Vapnik & Chervonenkis, "On the Uniform Convergence of Relative Frequencies of Events to Their Probabilities" | VC theory of capacity; Soviet foundation of statistical learning theory and later SVMs | [82], [83] |
| 1971 | Intel 4004 released (15 November 1971) | First in Intel's line of CPUs; adjacent-field item (hardware) kept because microprocessors fed cheap AI computing | [84] |
| 1972 | Colmerauer & Roussel create Prolog (Marseille); Kowalski's procedural interpretation of Horn clauses | Logic programming; later the basis of Japan's Fifth Generation project | [31] |
| 1972 | Dreyfus, *What Computers Can't Do* (following his 1965 RAND memo "Alchemy and AI") | Phenomenological critique of symbolic AI's assumptions | [32] |
| 1972 | Kenneth Colby's PARRY (Stanford) simulates a person with paranoid schizophrenia | Chatbot with an internal belief model — ELIZA's clinical counterpart | [85] |
| 1973 | Lighthill Report ("Artificial Intelligence: A General Survey") for the UK Science Research Council; BBC debate 9 May 1973 | UK government ends most AI funding; combinatorial explosion named as the core failure | [33] |
| 1973 | Hewitt, Bishop & Steiger introduce the actor model | Mathematical model of concurrent computation with actors as building blocks; basis of practical concurrent systems | [86] |
| 1974 | Kaissa (Institute of Control Sciences, Moscow) wins the first World Computer Chess Championship in Stockholm | A Soviet program tops the field as Western funding falls; game playing keeps running through the winter | [47] |
| 1974 | DARPA cutbacks to academic AI (following disappointments incl. the Speech Understanding Research programme, 1971–75) | Start of the first AI winter (~1974–1980); eastern border of this region | [28] |

## Key people
- **John McCarthy** (Dartmouth → MIT → Stanford) — coined "AI"; Lisp (1958); Advice Taker / logic-based commonsense (1959); started SAIL (1963); Turing Award 1971. [1], [7], [9], [14]
- **Marvin Minsky** (Harvard → MIT) — Dartmouth co-organiser; "Steps Toward AI" (1961); MIT AI Lab co-founder; *Perceptrons* (1969); frames (1974); Turing Award 1969. [1], [11], [13], [26]
- **Allen Newell & Herbert A. Simon** (RAND / Carnegie Tech, later CMU) — Logic Theorist (1956), GPS (1959), *Human Problem Solving* (1972), physical symbol system hypothesis (1976); joint Turing Award 1975; Simon Nobel in Economics 1978. [2], [3], [10], [18]
- **J. C. (Cliff) Shaw** (RAND) — co-author of Logic Theorist and GPS; implemented IPL, the first list-processing language. [2], [10]
- **Claude Shannon** (Bell Labs / MIT) — Dartmouth co-organiser; information theory and chess-program design carried in from era 01. [1]
- **Nathaniel Rochester** (IBM) — Dartmouth co-organiser; designer of the IBM 701; early neural-net simulations at IBM. [1]
- **Oliver Selfridge** (MIT Lincoln Lab) — Pandemonium (1958–59); Dartmouth attendee. [1], [8]
- **Arthur Samuel** (IBM) — checkers program with rote and generalisation learning (1952–59). [4]
- **Frank Rosenblatt** (Cornell Aeronautical Laboratory) — perceptron (1957–58) and Mark I hardware (1960); the connectionist standard-bearer of the era; died in a boating accident in 1971, two years after *Perceptrons*. [5], [6], [53]
- **Bernard Widrow & Ted Hoff** (Stanford) — ADALINE and LMS rule (1960). [12]
- **Joseph Weizenbaum** (MIT) — ELIZA (1964–67); later critic in *Computer Power and Human Reason* (1976). [20]
- **Nils Nilsson, Peter Hart, Charles Rosen, Richard Fikes** (SRI) — Shakey project; A* (Hart, Nilsson, Raphael 1968); STRIPS (Fikes & Nilsson 1971). [21], [22], [23]
- **Terry Winograd** (MIT) — SHRDLU (1968–70). [29]
- **J. Alan Robinson** (Rice / Argonne) — resolution principle (1965). [16]
- **Seymour Papert** (MIT) — co-author of *Perceptrons*; Logo; micro-worlds pedagogy. [26]
- **Donald Michie** (Edinburgh) — founded UK AI at Edinburgh; MENACE matchbox learner; *Machine Intelligence* workshop series (from 1965–66); Freddy robots (1969–76); debated Lighthill in 1973. [15], [33], [52]
- **Edward Feigenbaum, Joshua Lederberg & Bruce Buchanan** (Stanford) — Dendral (from 1965): the bridge to expert systems; Feigenbaum earlier wrote EPAM (Carnegie PhD under Simon, 1959–60), the first computer model of human verbal learning, and co-edited *Computers and Thought* (1963). [17], [42], [57]
- **Herbert Gelernter** (IBM) — Geometry Theorem Prover (1958–59) with Rochester; FLPL. [37]
- **James Slagle** (MIT → NIH) — SAINT symbolic integrator (1961), the first of Minsky's problem-solving theses. [38]
- **Thomas Evans, Daniel Bobrow & Bertram Raphael** (MIT AI Group, Minsky students) — ANALOGY (1963), STUDENT (1964), SIR (1964); Raphael then led Shakey work at SRI. [35], [40], [41]
- **Ray Solomonoff** (Dartmouth attendee; independent) — inductive inference machine memo (1956), algorithmic probability (1960–64). [49]
- **Patrick Winston** (MIT) — ARCH concept-learning thesis (1970); Computers and Thought Award 1973; directed the MIT AI Lab 1972–97. [35], [51]
- **Carl Hewitt & Pat Hayes** (MIT / Edinburgh–Stanford) — PLANNER (1969); Hayes co-authored the frame-problem paper with McCarthy (1969). [44], [45]
- **J. C. R. Licklider** (ARPA IPTO, 1962–64; later Project MAC director) — the programme manager whose office bankrolled MIT, Stanford and CMU AI. [43]
- **Alexey Ivakhnenko** (Institute of Cybernetics, Kyiv) — GMDH (1968), deep polynomial networks trained inductively. [48]
- **Sir James Lighthill** (Cambridge, applied mathematician) — author of the 1973 report that ended most UK AI funding. [33]
- **Hubert Dreyfus** (MIT → Berkeley, philosopher) — "Alchemy and AI" (1965), *What Computers Can't Do* (1972). [32]

## Key papers / artifacts
- McCarthy, J., Minsky, M., Rochester, N. & Shannon, C. *A Proposal for the Dartmouth Summer Research Project on Artificial Intelligence*, 1955. http://jmc.stanford.edu/articles/dartmouth/dartmouth.pdf [1]
- Newell, A. & Simon, H. A. *The Logic Theory Machine — A Complex Information Processing System*. IRE Transactions on Information Theory 2(3):61–79, 1956. https://doi.org/10.1109/TIT.1956.1056797 [3]
- Rosenblatt, F. *The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain*. Psychological Review 65(6):386–408, 1958. doi:10.1037/h0042519 — open copy: https://homepages.math.uic.edu/~lreyzin/papers/rosenblatt58.pdf [5]
- McCarthy, J. *Programs with Common Sense*. Proc. Teddington Conference on the Mechanization of Thought Processes, 1959. http://jmc.stanford.edu/articles/mcc59/mcc59.pdf [9]
- Newell, A., Shaw, J. C. & Simon, H. A. *Report on a General Problem-Solving Program*. RAND P-1584, 1959. http://bitsavers.trailing-edge.com/pdf/rand/ipl/P-1584_Report_On_A_General_Problem-Solving_Program_Feb59.pdf [10]
- Samuel, A. L. *Some Studies in Machine Learning Using the Game of Checkers*. IBM J. Res. Dev. 3(3), 1959. https://doi.org/10.1147/rd.33.0210 [4]
- McCarthy, J. *Recursive Functions of Symbolic Expressions and Their Computation by Machine, Part I*. CACM 3(4):184–195, 1960. doi:10.1145/367177.367199 — open copy: http://jmc.stanford.edu/articles/recursive/recursive.pdf [7]
- Widrow, B. & Hoff, M. E. *Adaptive Switching Circuits*. IRE WESCON Convention Record, 1960. https://isl.stanford.edu/~widrow/papers/c1960adaptiveswitching.pdf [12]
- Minsky, M. *Steps Toward Artificial Intelligence*. Proceedings of the IRE 49(1):8–30, 1961. https://doi.org/10.1109/JRPROC.1961.287775 [13]
- Robinson, J. A. *A Machine-Oriented Logic Based on the Resolution Principle*. JACM 12(1):23–41, 1965. doi:10.1145/321250.321253 — context: https://en.wikipedia.org/wiki/Resolution_%28logic%29 [16]
- Weizenbaum, J. *ELIZA — A Computer Program for the Study of Natural Language Communication Between Man and Machine*. CACM 9(1):36–45, 1966. doi:10.1145/365153.365168 — open copy: https://web.stanford.edu/class/cs124/p36-weizenabaum.pdf [20]
- Pierce, J. R. et al. *Language and Machines: Computers in Translation and Linguistics* (ALPAC report). National Academy of Sciences, 1966. https://nap.nationalacademies.org/catalog/9547/language-and-machines-computers-in-translation-and-linguistics [19]
- Hart, P. E., Nilsson, N. J. & Raphael, B. *A Formal Basis for the Heuristic Determination of Minimum Cost Paths* (A*). IEEE Trans. Systems Science and Cybernetics 4(2):100–107, 1968. https://doi.org/10.1109/TSSC.1968.300136 [22]
- Minsky, M. & Papert, S. *Perceptrons: An Introduction to Computational Geometry*. MIT Press, 1969. https://archive.org/details/perceptronsintro00mins [26]
- Winograd, T. *Procedures as a Representation for Data in a Computer Program for Understanding Natural Language* (SHRDLU). MIT AI-TR-235 / PhD thesis, 1971. https://dspace.mit.edu/handle/1721.1/7095 [29]
- Fikes, R. E. & Nilsson, N. J. *STRIPS: A New Approach to the Application of Theorem Proving to Problem Solving*. Artificial Intelligence 2(3–4):189–208, 1971. https://doi.org/10.1016/0004-3702%2871%2990010-5 [23]
- Newell, A. & Simon, H. A. *Human Problem Solving*. Prentice-Hall, 1972. https://archive.org/details/humanproblemsolv0000newe [18]
- Lighthill, J. *Artificial Intelligence: A General Survey*. Science Research Council, 1973. http://www.chilton-computing.org.uk/inf/literature/reports/lighthill_report/p001.htm [33]
- McCarthy, J. & Hayes, P. J. *Some Philosophical Problems from the Standpoint of Artificial Intelligence*. Machine Intelligence 4:463–502, 1969. http://jmc.stanford.edu/articles/mcchay69/mcchay69.pdf [44]
- Minsky, M. *A Framework for Representing Knowledge* (frames). MIT AI Memo 306, 1974. https://dspace.mit.edu/handle/1721.1/6089 [34]

## Schools of thought / sub-clusters
- **Heuristic search & cognitive simulation** (Newell, Shaw, Simon at RAND/Carnegie; Logic Theorist, GPS, *Human Problem Solving*; Gelernter's geometry prover and Slagle's SAINT as heuristic-search offshoots) — intelligence as symbol manipulation guided by heuristics; explicitly models human protocols; borders: *Principia*/logic (west, era 01), cognitive science and the physical-symbol-system hypothesis (east, era 03), SOAR/ACT-R (further east). [2], [3], [10], [18], [37], [38]
- **Logic-based AI / "neats"** (McCarthy, Robinson, Green, Hayes, Kowalski; Advice Taker, situation calculus, Wang's 1959 prover, resolution, the McCarthy–Hayes frame problem, Prolog) — knowledge as first-order logic sentences, reasoning as deduction; borders: computability & lambda calculus (west, era 01), theorem proving and logic programming → Fifth Generation project (east, era 03), knowledge representation & the frame problem. [7], [9], [16], [31], [39], [44]
- **Micro-worlds & language / "scruffies"** (Minsky, Papert, Evans, Bobrow, Raphael, Winston, Hewitt, Winograd, Weizenbaum, Quillian, Schank; MIT AI Lab blocks world, ANALOGY, STUDENT, SIR, PLANNER, SHRDLU, ELIZA, semantic nets, conceptual dependency) — build working systems in simplified domains and scale up later; borders: frames → expert-system knowledge engineering (east, era 03), NLP lineage (east), Lighthill's combinatorial-explosion critique (border wall). [11], [20], [25], [29], [34], [40], [45], [51]
- **Robotics, vision & planning** (SRI Shakey group; Roberts's 1963 blocks-world vision and the 1966 MIT Summer Vision Project; Stanford Cart; Edinburgh Freddy 1969–76) — integrating perception, representation and action; borders: cybernetic robots (west, era 01), A*/STRIPS → planning subfield, behaviour-based robotics as a reaction (east, era 03). [21], [22], [23], [50], [52]
- **Perceptron / connectionist strip** (Rosenblatt, Widrow–Hoff, Block; Cornell, Stanford; SRI's MINOS machines; Ivakhnenko's GMDH in Kyiv as a separate deep-network tributary) — learning linear classifiers from data; borders: McCulloch–Pitts, Hebb, SNARC (west, era 01); cut off by *Perceptrons* 1969 and re-emerging as PDP/backprop in era 03. [5], [6], [12], [26], [28], [48]
- **Game playing** (Samuel, Greenblatt, Kotok–McCarthy, Newell–Shaw–Simon chess, Michie's MENACE; ITEP and Kaissa in Moscow) — search + evaluation + learning on well-defined tasks; borders: Shannon 1950 (west), Deep Blue and TD-Gammon (east). [4], [15], [24], [46], [47]
- **Early knowledge-intensive systems** (Dendral at Stanford from 1965; Macsyma at Project MAC from 1968 as the mathematical counterpart) — the deviation from general methods toward domain knowledge; borders: SAINT and heuristic search (west), MYCIN and the expert-systems continent (east, era 03) — *this is the head-waters of era 03's expert-systems continent.* [17], [54]
- **Critics & philosophers** (Dreyfus, Weizenbaum, Lighthill, ALPAC) — external assessments that shaped funding; borders: Turing test debates (west), Searle's Chinese Room 1980 (east). [19], [32], [33]

## Map notes
- **A1 label:** "The Symbolic Plateau" / "Golden Age of AI". **A2 labels:** "Heuristic Search Country" (Carnegie/RAND), "Logic Country" (McCarthy/Stanford/Edinburgh), "Micro-world Coast" (MIT), "SRI Robotics Peninsula", "Perceptron Country" (a shrinking southern strip). **A3 labels:** "Dartmouth 1956", "Logic Theorist", "Lisp 1958", "Perceptron 1958", "GPS", "ELIZA", "Shakey", "SHRDLU", "*Perceptrons* 1969", "Resolution 1965", "Prolog 1972", "Lighthill 1973".
- **Rivers/borders:** the *Symbolic Divide* (from era 01) becomes a true mountain range here — north of it, symbolic AI; south, the perceptron strip. After 1969 the southern strip narrows to a footpath ("the Perceptrons Gap") that only reopens in the 1980s. The eastern border is a cliff/escarpment labelled "First AI Winter (1974)" with three marked passes: Lighthill (UK), Mansfield/DARPA (US), and ALPAC (MT, earlier).
- **Bridges east:** Dendral → MYCIN and expert systems; frames/semantic nets → knowledge engineering and Cyc; resolution/Prolog → Fifth Generation; ADALINE/LMS → backprop; Shakey/STRIPS → planning; Newell–Simon → cognitive science and SOAR; ELIZA → chatbots and the Turing-test lineage.
- **Bridges west:** Logic Theorist ← *Principia* (era 01); Lisp ← lambda calculus; perceptron ← McCulloch–Pitts/Hebb; Shannon and Samuel arrive from era 01 in person.
- **Open questions for curation:** (a) whether Dendral (1965) should be drawn inside this era or as an exclave of era 03 — recommend a border town; (b) the Prolog/logic-programming cluster is geographically European (Marseille, Edinburgh) — consider a distinct A2 label; (c) Minsky's frames (1974) straddle the border — placed here as the last major artefact before the winter; (d) how prominently to draw the over-predictions (Simon 1957/1965, Minsky 1970) — suggest A4 "monuments" rather than cities; (e) the Soviet work (ITEP/Kaissa chess, Ivakhnenko's GMDH) has no natural A2 home — suggest an "Eastern Bloc" exclave on the far side of the game-playing and perceptron strips; (f) Solomonoff's inductive inference (1964) is a probabilistic seed with no era-02 country — draw as a spring feeding era 05's statistical basin.

## Sources
[1] Dartmouth workshop — Wikipedia — https://en.wikipedia.org/wiki/Dartmouth_workshop ; proposal text http://jmc.stanford.edu/articles/dartmouth/dartmouth.pdf (accessed 2026-09-06)
[2] Logic Theorist — Wikipedia — https://en.wikipedia.org/wiki/Logic_Theorist (accessed 2026-09-06)
[3] Newell & Simon, The Logic Theory Machine (1956) — https://doi.org/10.1109/TIT.1956.1056797 (accessed 2026-09-06)
[4] Arthur Samuel — Wikipedia — https://en.wikipedia.org/wiki/Arthur_Samuel_%28computer_scientist%29 ; Samuel 1959 https://doi.org/10.1147/rd.33.0210 (accessed 2026-09-06)
[5] Rosenblatt, The Perceptron (1958) — https://homepages.math.uic.edu/~lreyzin/papers/rosenblatt58.pdf ; Perceptron — Wikipedia https://en.wikipedia.org/wiki/Perceptron (accessed 2026-09-06)
[6] Cornell Chronicle, "Professor's perceptron paved the way for AI – 60 years too soon" (2019) — https://news.cornell.edu/stories/2019/09/professors-perceptron-paved-way-ai-60-years-too-soon ; Mark I Perceptron https://en.wikipedia.org/wiki/Mark_I_Perceptron (accessed 2026-09-06)
[7] McCarthy, Recursive Functions of Symbolic Expressions (1960) — http://jmc.stanford.edu/articles/recursive/recursive.pdf ; Lisp — Wikipedia https://en.wikipedia.org/wiki/Lisp_%28programming_language%29 (accessed 2026-09-06)
[8] Pandemonium architecture — Wikipedia — https://en.wikipedia.org/wiki/Pandemonium_architecture ; Oliver Selfridge https://en.wikipedia.org/wiki/Oliver_Selfridge (accessed 2026-09-06)
[9] McCarthy, Programs with Common Sense (1959) — http://jmc.stanford.edu/articles/mcc59/mcc59.pdf ; Advice taker https://en.wikipedia.org/wiki/Advice_taker (accessed 2026-09-06)
[10] Newell, Shaw & Simon, Report on a General Problem-Solving Program (RAND P-1584, 1959) — http://bitsavers.trailing-edge.com/pdf/rand/ipl/P-1584_Report_On_A_General_Problem-Solving_Program_Feb59.pdf ; GPS — Wikipedia https://en.wikipedia.org/wiki/General_Problem_Solver (accessed 2026-09-06)
[11] MIT CSAIL (history of the MIT AI Lab) — Wikipedia — https://en.wikipedia.org/wiki/MIT_Computer_Science_and_Artificial_Intelligence_Laboratory (accessed 2026-09-06)
[12] Widrow & Hoff, Adaptive Switching Circuits (1960) — https://isl.stanford.edu/~widrow/papers/c1960adaptiveswitching.pdf ; ADALINE https://en.wikipedia.org/wiki/ADALINE (accessed 2026-09-06)
[13] Minsky, Steps Toward Artificial Intelligence (1961) — https://doi.org/10.1109/JRPROC.1961.287775 (accessed 2026-09-06)
[14] Stanford Artificial Intelligence Laboratory — Wikipedia — https://en.wikipedia.org/wiki/Stanford_Artificial_Intelligence_Laboratory ; John McCarthy https://en.wikipedia.org/wiki/John_McCarthy_%28computer_scientist%29 (accessed 2026-09-06)
[15] Donald Michie — Wikipedia — https://en.wikipedia.org/wiki/Donald_Michie (accessed 2026-09-06)
[16] Robinson, A Machine-Oriented Logic Based on the Resolution Principle (1965) — doi:10.1145/321250.321253 ; Resolution (logic) — Wikipedia https://en.wikipedia.org/wiki/Resolution_%28logic%29 ; John Alan Robinson https://en.wikipedia.org/wiki/John_Alan_Robinson (accessed 2026-09-06)
[17] Dendral — Wikipedia — https://en.wikipedia.org/wiki/Dendral ; Lindsay, Buchanan, Feigenbaum & Lederberg, "DENDRAL: a case study…", Artificial Intelligence 61 (1993) https://doi.org/10.1016/0004-3702%2893%2990068-M (accessed 2026-09-06)
[18] Herbert A. Simon — Wikipedia — https://en.wikipedia.org/wiki/Herbert_A._Simon ; Newell & Simon, Human Problem Solving (1972) https://archive.org/details/humanproblemsolv0000newe (accessed 2026-09-06)
[19] ALPAC — Wikipedia — https://en.wikipedia.org/wiki/ALPAC ; report https://nap.nationalacademies.org/catalog/9547/language-and-machines-computers-in-translation-and-linguistics (accessed 2026-09-06)
[20] ELIZA — Wikipedia — https://en.wikipedia.org/wiki/ELIZA ; Weizenbaum 1966 https://web.stanford.edu/class/cs124/p36-weizenabaum.pdf (accessed 2026-09-06)
[21] Shakey the robot — Wikipedia — https://en.wikipedia.org/wiki/Shakey_the_robot ; SRI page https://www.sri.com/hoi/shakey-the-robot/ (accessed 2026-09-06)
[22] Hart, Nilsson & Raphael, A Formal Basis for the Heuristic Determination of Minimum Cost Paths (1968) — https://doi.org/10.1109/TSSC.1968.300136 (accessed 2026-09-06)
[23] Fikes & Nilsson, STRIPS (1971) — https://doi.org/10.1016/0004-3702%2871%2990010-5 (accessed 2026-09-06)
[24] Mac Hack (Greenblatt, 1967) — Wikipedia — https://en.wikipedia.org/wiki/Mac_Hack (accessed 2026-09-06)
[25] Semantic network — Wikipedia — https://en.wikipedia.org/wiki/Semantic_network (accessed 2026-09-06)
[26] Perceptrons (book) — Wikipedia — https://en.wikipedia.org/wiki/Perceptrons_%28book%29 ; scan https://archive.org/details/perceptronsintro00mins (accessed 2026-09-06)
[27] International Joint Conference on Artificial Intelligence — Wikipedia — https://en.wikipedia.org/wiki/International_Joint_Conference_on_Artificial_Intelligence (accessed 2026-09-06)
[28] AI winter — Wikipedia (Mansfield Amendment, DARPA 1973–74 cuts, SUR programme) — https://en.wikipedia.org/wiki/AI_winter ; History of artificial intelligence https://en.wikipedia.org/wiki/History_of_artificial_intelligence (accessed 2026-09-06)
[29] SHRDLU — Wikipedia — https://en.wikipedia.org/wiki/SHRDLU ; Winograd thesis https://dspace.mit.edu/handle/1721.1/7095 (accessed 2026-09-06)
[30] Marvin Minsky — Wikipedia — https://en.wikipedia.org/wiki/Marvin_Minsky (1970 *Life* quotation via History of AI article [28]) (accessed 2026-09-06)
[31] Prolog — Wikipedia — https://en.wikipedia.org/wiki/Prolog ; Alain Colmerauer https://en.wikipedia.org/wiki/Alain_Colmerauer ; Robert Kowalski https://en.wikipedia.org/wiki/Robert_Kowalski (accessed 2026-09-06)
[32] Hubert Dreyfus's views on artificial intelligence — Wikipedia — https://en.wikipedia.org/wiki/Hubert_Dreyfus%27s_views_on_artificial_intelligence ; What Computers Can't Do https://en.wikipedia.org/wiki/What_Computers_Can%27t_Do (accessed 2026-09-06)
[33] Lighthill report — Wikipedia — https://en.wikipedia.org/wiki/Lighthill_report ; full text at Chilton Computing http://www.chilton-computing.org.uk/inf/literature/reports/lighthill_report/p001.htm (accessed 2026-09-06)
[34] Minsky, A Framework for Representing Knowledge (1974) — https://dspace.mit.edu/handle/1721.1/6089 ; Frame (AI) https://en.wikipedia.org/wiki/Frame_%28artificial_intelligence%29 (accessed 2026-09-06)
[35] AAAI, A Brief History of AI — https://aitopics.org/misc/brief-history (accessed 2026-09-06)
[36] Nilsson, N. J. *The Quest for Artificial Intelligence* (2010), free PDF — https://ai.stanford.edu/~nilsson/QAI/qai.pdf (accessed 2026-09-06)
[37] Herbert Gelernter — Wikipedia — https://en.wikipedia.org/wiki/Herbert_Gelernter (accessed 2026-09-06)
[38] James Robert Slagle — Wikipedia — https://en.wikipedia.org/wiki/James_Robert_Slagle (accessed 2026-09-06)
[39] Hao Wang (academic) — Wikipedia — https://en.wikipedia.org/wiki/Hao_Wang_%28academic%29 (accessed 2026-09-06)
[40] STUDENT (computer program) — Wikipedia — https://en.wikipedia.org/wiki/STUDENT_%28computer_program%29 ; Daniel G. Bobrow https://en.wikipedia.org/wiki/Daniel_G._Bobrow (accessed 2026-09-06)
[41] Bertram Raphael — Wikipedia — https://en.wikipedia.org/wiki/Bertram_Raphael (accessed 2026-09-06)
[42] Edward Feigenbaum — Wikipedia (Computers and Thought 1963; EPAM) — https://en.wikipedia.org/wiki/Edward_Feigenbaum ; IJCAI Computers and Thought Award https://en.wikipedia.org/wiki/IJCAI_Computers_and_Thought_Award (accessed 2026-09-06)
[43] Information Processing Techniques Office — Wikipedia — https://en.wikipedia.org/wiki/Information_Processing_Techniques_Office (accessed 2026-09-06)
[44] McCarthy & Hayes, Some Philosophical Problems from the Standpoint of Artificial Intelligence (1969) — http://jmc.stanford.edu/articles/mcchay69/mcchay69.pdf ; Frame problem — Wikipedia https://en.wikipedia.org/wiki/Frame_problem ; Situation calculus https://en.wikipedia.org/wiki/Situation_calculus (accessed 2026-09-06)
[45] Planner (programming language) — Wikipedia — https://en.wikipedia.org/wiki/Planner_%28programming_language%29 (accessed 2026-09-06)
[46] Kotok-McCarthy — Wikipedia — https://en.wikipedia.org/wiki/Kotok-McCarthy (accessed 2026-09-06)
[47] Kaissa — Wikipedia — https://en.wikipedia.org/wiki/Kaissa (accessed 2026-09-06)
[48] Group method of data handling — Wikipedia — https://en.wikipedia.org/wiki/Group_method_of_data_handling ; Alexey Ivakhnenko https://en.wikipedia.org/wiki/Alexey_Ivakhnenko (accessed 2026-09-06)
[49] Ray Solomonoff — Wikipedia — https://en.wikipedia.org/wiki/Ray_Solomonoff (accessed 2026-09-06)
[50] Lawrence Roberts (scientist) — Wikipedia — https://en.wikipedia.org/wiki/Lawrence_Roberts_%28scientist%29 ; Computer vision (history: 1966 summer project) https://en.wikipedia.org/wiki/Computer_vision (accessed 2026-09-06)
[51] Patrick Winston — Wikipedia — https://en.wikipedia.org/wiki/Patrick_Winston (accessed 2026-09-06)
[52] Freddy II (Edinburgh robots, 1969–76) — Wikipedia — https://en.wikipedia.org/wiki/Freddy_II (accessed 2026-09-06)
[53] Frank Rosenblatt — Wikipedia — https://en.wikipedia.org/wiki/Frank_Rosenblatt (accessed 2026-09-06)
[54] Macsyma — Wikipedia — https://en.wikipedia.org/wiki/Macsyma (accessed 2026-09-06)
[55] Yehoshua Bar-Hillel — Wikipedia — https://en.wikipedia.org/wiki/Yehoshua_Bar-Hillel (accessed 2026-09-06)
[56] Artificial Intelligence (journal) — Wikipedia — https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29 (accessed 2026-09-06)
[57] EPAM (Elementary Perceiver and Memorizer) — Wikipedia — https://en.wikipedia.org/wiki/Elementary_Perceiver_and_Memorizer (accessed 2026-09-06)
[58] Syntactic Structures — Wikipedia (Chomsky, 1957) — https://en.wikipedia.org/wiki/Syntactic_Structures (accessed 2026-09-23)
[59] Jerome Lettvin — Wikipedia ("What the Frog's Eye Tells the Frog's Brain", 1959) — https://en.wikipedia.org/wiki/Jerome_Lettvin (accessed 2026-09-23)
[60] Lettvin, Maturana, McCulloch & Pitts, "What the Frog's Eye Tells the Frog's Brain", Proc. IRE 47 (1959), doi:10.1109/JRPROC.1959.287207 — https://doi.org/10.1109/JRPROC.1959.287207 (accessed 2026-09-23)
[61] David H. Hubel — Wikipedia (1959 cat visual-cortex experiment; 1981 Nobel with Wiesel) — https://en.wikipedia.org/wiki/David_H._Hubel (accessed 2026-09-23)
[62] Crossref record — Hubel & Wiesel, "Receptive fields of single neurones in the cat's striate cortex", J. Physiol. (1959), doi:10.1113/jphysiol.1959.sp006308 (DOI 403 to bots) — https://api.crossref.org/works/10.1113/jphysiol.1959.sp006308 (accessed 2026-09-23)
[63] Woody Bledsoe — Wikipedia (n-tuple method, 1959) — https://en.wikipedia.org/wiki/Woody_Bledsoe (accessed 2026-09-23)
[64] Licklider, "Man-Computer Symbiosis", IRE Trans. Human Factors in Electronics (1960), doi:10.1109/THFE2.1960.4503259 — https://doi.org/10.1109/THFE2.1960.4503259 (accessed 2026-09-23)
[65] Man-Computer Symbiosis — Wikipedia — https://en.wikipedia.org/wiki/Man-Computer_Symbiosis (accessed 2026-09-23)
[66] Matchbox Educable Noughts and Crosses Engine — Wikipedia (Michie's 1961 tournament) — https://en.wikipedia.org/wiki/Matchbox_Educable_Noughts_and_Crosses_Engine (accessed 2026-09-23)
[67] Unimate — Wikipedia (GM assembly line, 1961) — https://en.wikipedia.org/wiki/Unimate (accessed 2026-09-23)
[68] Victor Glushkov — Wikipedia (founds Kiev Institute of Cybernetics, 1962) — https://en.wikipedia.org/wiki/Victor_Glushkov (accessed 2026-09-23)
[69] Sketchpad — Wikipedia (Sutherland, 1963) — https://en.wikipedia.org/wiki/Sketchpad (accessed 2026-09-23)
[70] Fuzzy set — Wikipedia (Zadeh, 1965) — https://en.wikipedia.org/wiki/Fuzzy_set (accessed 2026-09-23)
[71] Zadeh, "Fuzzy sets", Information and Control 8 (1965), doi:10.1016/S0019-9958(65)90241-X — https://doi.org/10.1016/S0019-9958%2865%2990241-X (accessed 2026-09-23)
[72] Moore's law — Wikipedia (Gordon Moore, 1965) — https://en.wikipedia.org/wiki/Moore%27s_law (accessed 2026-09-23)
[73] Turing Award — Wikipedia (first recipient Alan Perlis, 1966) — https://en.wikipedia.org/wiki/Turing_Award (accessed 2026-09-23)
[74] Cover & Hart, "Nearest neighbor pattern classification", IEEE Trans. Inf. Theory 13 (1967), doi:10.1109/TIT.1967.1053964 — https://doi.org/10.1109/TIT.1967.1053964 (accessed 2026-09-23)
[75] Shun'ichi Amari — Wikipedia (1967 SGD-trained deep network) — https://en.wikipedia.org/wiki/Shun%27ichi_Amari (accessed 2026-09-23)
[76] Amari, "A Theory of Adaptive Pattern Classifiers", IEEE Trans. Electronic Computers (1967), doi:10.1109/PGEC.1967.264666 — https://doi.org/10.1109/PGEC.1967.264666 (accessed 2026-09-23)
[77] HAL 9000 — Wikipedia (2001: A Space Odyssey, 1968) — https://en.wikipedia.org/wiki/HAL_9000 (accessed 2026-09-23)
[78] The Mother of All Demos — Wikipedia (Engelbart, 9 December 1968) — https://en.wikipedia.org/wiki/The_Mother_of_All_Demos (accessed 2026-09-23)
[79] ARPANET — Wikipedia (first host-to-host connection 29 October 1969) — https://en.wikipedia.org/wiki/ARPANET (accessed 2026-09-23)
[80] Augmented transition network — Wikipedia (Woods 1970) — https://en.wikipedia.org/wiki/Augmented_transition_network (accessed 2026-09-23)
[81] Crossref record — Woods, "Transition network grammars for natural language analysis", CACM 13 (1970), doi:10.1145/355598.362773 — https://api.crossref.org/works/10.1145/355598.362773 (accessed 2026-09-23)
[82] Vapnik–Chervonenkis dimension — Wikipedia — https://en.wikipedia.org/wiki/Vapnik%E2%80%93Chervonenkis_dimension (accessed 2026-09-23)
[83] Crossref record — Vapnik & Chervonenkis, "On the Uniform Convergence of Relative Frequencies of Events to Their Probabilities", Theory Probab. Appl. 16 (1971), doi:10.1137/1116025 (DOI 403 to bots) — https://api.crossref.org/works/10.1137/1116025 (accessed 2026-09-23)
[84] Intel 4004 — Wikipedia (released 15 November 1971) — https://en.wikipedia.org/wiki/Intel_4004 (accessed 2026-09-23)
[85] PARRY — Wikipedia (Colby, 1972) — https://en.wikipedia.org/wiki/PARRY (accessed 2026-09-23)
[86] Actor model — Wikipedia (originated 1973) — https://en.wikipedia.org/wiki/Actor_model (accessed 2026-09-23)
