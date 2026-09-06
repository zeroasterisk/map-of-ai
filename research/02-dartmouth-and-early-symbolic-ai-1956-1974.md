# Dartmouth and the Golden Age of Symbolic AI (1956–1974)

> **Status:** verified
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
| 1958 | McCarthy designs Lisp at MIT (paper 1960) | Language of AI for 30+ years; list processing, recursion, garbage collection | [7] |
| 1958–59 | Selfridge, "Pandemonium: A Paradigm for Learning" (Teddington symposium Nov 1958; proceedings 1959) | Parallel feature-demon architecture; ancestor of blackboard systems and layered recognition | [8] |
| 1959 | McCarthy, "Programs with Common Sense" (Advice Taker) | Manifesto for logic-based knowledge representation and commonsense reasoning | [9] |
| 1959 | Newell, Shaw & Simon, General Problem Solver (GPS) | Means–ends analysis; separates problem-solving strategy from domain knowledge | [10] |
| 1959 | MIT AI project founded by McCarthy & Minsky (becomes MIT AI Lab 1970) | One of the three main US AI centres (with Stanford, CMU) | [11] |
| 1960 | Widrow & Hoff, ADALINE and the LMS (delta) rule | Gradient-based learning for linear units; direct ancestor of backprop-era training | [12] |
| 1961 | Minsky, "Steps Toward Artificial Intelligence" | Survey/agenda of search, pattern recognition, learning, planning, induction | [13] |
| 1963 | McCarthy (at Stanford from 1962) starts the Stanford AI Laboratory (SAIL) | Second major US centre; home of later robotics, vision and hand–eye work | [14] |
| 1965 | Edinburgh's Department of Machine Intelligence and Perception established under Donald Michie (from the earlier Experimental Programming Unit) | UK centre of AI; later target of the Lighthill Report | [15] |
| 1965 | J. A. Robinson, resolution principle | Complete inference rule for first-order logic; foundation of theorem proving and Prolog | [16] |
| 1965 | Dendral begins at Stanford (Feigenbaum, Lederberg, Buchanan) | First expert system: knowledge-intensive rather than general search — the seed of era 03 | [17] |
| 1965 | Simon predicts "machines will be capable, within twenty years, of doing any work a man can do" | Emblematic over-prediction that fed the later backlash | [18] |
| 1966 | ALPAC report ends US machine-translation funding | First funded-AI collapse; "winter" episode within the golden age | [19] |
| 1966 | Weizenbaum's ELIZA / DOCTOR script (paper in CACM) | Pattern-matching chatbot; the "ELIZA effect" | [20] |
| 1966–1972 | Shakey the Robot at SRI (Rosen, Nilsson, Hart) | First mobile robot reasoning about its actions; yields A* (1968) and STRIPS (1971) | [21], [22], [23] |
| 1966–67 | Greenblatt's Mac Hack VI plays in human chess tournaments at MIT | First chess program to play under tournament conditions, receive a USCF rating, and beat a person in tournament play | [24] |
| 1968 | Quillian's semantic networks (PhD 1966; *Semantic Information Processing*, ed. Minsky, 1968) | Graph-based knowledge representation; ancestor of frames, ontologies, knowledge graphs | [25] |
| 1969 | Minsky & Papert, *Perceptrons* | Proves single-layer perceptrons can't compute XOR/connectedness; widely credited with chilling neural-net funding | [26] |
| 1969 | First IJCAI held in Washington, D.C.; Mansfield Amendment requires DARPA to fund mission-oriented research | Field gets its conference; funding regime starts to tighten | [27], [28] |
| 1970 | Winograd's SHRDLU (MIT PhD, 1968–70) | Natural-language understanding in a blocks micro-world; peak of the micro-worlds programme | [29] |
| 1970 | Minsky (in *Life*) predicts a machine with average human intelligence "in from three to eight years" | The most quoted over-promise of the era | [30] |
| 1972 | Colmerauer & Roussel create Prolog (Marseille); Kowalski's procedural interpretation of Horn clauses | Logic programming; later the basis of Japan's Fifth Generation project | [31] |
| 1972 | Dreyfus, *What Computers Can't Do* (following his 1965 RAND memo "Alchemy and AI") | Phenomenological critique of symbolic AI's assumptions | [32] |
| 1973 | Lighthill Report ("Artificial Intelligence: A General Survey") for the UK Science Research Council; BBC debate 9 May 1973 | UK government ends most AI funding; combinatorial explosion named as the core failure | [33] |
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
- **Frank Rosenblatt** (Cornell Aeronautical Laboratory) — perceptron (1957–58) and Mark I hardware; the connectionist standard-bearer of the era. [5], [6]
- **Bernard Widrow & Ted Hoff** (Stanford) — ADALINE and LMS rule (1960). [12]
- **Joseph Weizenbaum** (MIT) — ELIZA (1964–67); later critic in *Computer Power and Human Reason* (1976). [20]
- **Nils Nilsson, Peter Hart, Charles Rosen, Richard Fikes** (SRI) — Shakey project; A* (Hart, Nilsson, Raphael 1968); STRIPS (Fikes & Nilsson 1971). [21], [22], [23]
- **Terry Winograd** (MIT) — SHRDLU (1968–70). [29]
- **J. Alan Robinson** (Rice / Argonne) — resolution principle (1965). [16]
- **Seymour Papert** (MIT) — co-author of *Perceptrons*; Logo; micro-worlds pedagogy. [26]
- **Donald Michie** (Edinburgh) — founded UK AI at Edinburgh; MENACE matchbox learner; debated Lighthill in 1973. [15], [33]
- **Edward Feigenbaum, Joshua Lederberg & Bruce Buchanan** (Stanford) — Dendral (from 1965): the bridge to expert systems. [17]
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
- Minsky, M. *A Framework for Representing Knowledge* (frames). MIT AI Memo 306, 1974. https://dspace.mit.edu/handle/1721.1/6089 [34]

## Schools of thought / sub-clusters
- **Heuristic search & cognitive simulation** (Newell, Shaw, Simon at RAND/Carnegie; Logic Theorist, GPS, *Human Problem Solving*) — intelligence as symbol manipulation guided by heuristics; explicitly models human protocols; borders: *Principia*/logic (west, era 01), cognitive science and the physical-symbol-system hypothesis (east, era 03), SOAR/ACT-R (further east). [2], [3], [10], [18]
- **Logic-based AI / "neats"** (McCarthy, Robinson, Green, Kowalski; Advice Taker, situation calculus, resolution, Prolog) — knowledge as first-order logic sentences, reasoning as deduction; borders: computability & lambda calculus (west, era 01), theorem proving and logic programming → Fifth Generation project (east, era 03), knowledge representation & the frame problem. [7], [9], [16], [31]
- **Micro-worlds & language / "scruffies"** (Minsky, Papert, Winograd, Weizenbaum, Quillian, Schank; MIT AI Lab blocks world, SHRDLU, ELIZA, semantic nets, conceptual dependency) — build working systems in simplified domains and scale up later; borders: frames → expert-system knowledge engineering (east, era 03), NLP lineage (east), Lighthill's combinatorial-explosion critique (border wall). [11], [20], [25], [29], [34]
- **Robotics, vision & planning** (SRI Shakey group; Stanford Cart; Edinburgh Freddy) — integrating perception, representation and action; borders: cybernetic robots (west, era 01), A*/STRIPS → planning subfield, behaviour-based robotics as a reaction (east, era 03). [21], [22], [23]
- **Perceptron / connectionist strip** (Rosenblatt, Widrow–Hoff, Block; Cornell, Stanford) — learning linear classifiers from data; borders: McCulloch–Pitts, Hebb, SNARC (west, era 01); cut off by *Perceptrons* 1969 and re-emerging as PDP/backprop in era 03. [5], [6], [12], [26]
- **Game playing** (Samuel, Greenblatt, Newell–Shaw–Simon chess, Michie's MENACE) — search + evaluation + learning on well-defined tasks; borders: Shannon 1950 (west), Deep Blue and TD-Gammon (east). [4], [15], [24]
- **Early knowledge-intensive systems** (Dendral at Stanford from 1965) — the deviation from general methods toward domain knowledge; border: *this is the head-waters of era 03's expert-systems continent.* [17]
- **Critics & philosophers** (Dreyfus, Weizenbaum, Lighthill, ALPAC) — external assessments that shaped funding; borders: Turing test debates (west), Searle's Chinese Room 1980 (east). [19], [32], [33]

## Map notes
- **A1 label:** "The Symbolic Plateau" / "Golden Age of AI". **A2 labels:** "Heuristic Search Country" (Carnegie/RAND), "Logic Country" (McCarthy/Stanford/Edinburgh), "Micro-world Coast" (MIT), "SRI Robotics Peninsula", "Perceptron Country" (a shrinking southern strip). **A3 labels:** "Dartmouth 1956", "Logic Theorist", "Lisp 1958", "Perceptron 1958", "GPS", "ELIZA", "Shakey", "SHRDLU", "*Perceptrons* 1969", "Resolution 1965", "Prolog 1972", "Lighthill 1973".
- **Rivers/borders:** the *Symbolic Divide* (from era 01) becomes a true mountain range here — north of it, symbolic AI; south, the perceptron strip. After 1969 the southern strip narrows to a footpath ("the Perceptrons Gap") that only reopens in the 1980s. The eastern border is a cliff/escarpment labelled "First AI Winter (1974)" with three marked passes: Lighthill (UK), Mansfield/DARPA (US), and ALPAC (MT, earlier).
- **Bridges east:** Dendral → MYCIN and expert systems; frames/semantic nets → knowledge engineering and Cyc; resolution/Prolog → Fifth Generation; ADALINE/LMS → backprop; Shakey/STRIPS → planning; Newell–Simon → cognitive science and SOAR; ELIZA → chatbots and the Turing-test lineage.
- **Bridges west:** Logic Theorist ← *Principia* (era 01); Lisp ← lambda calculus; perceptron ← McCulloch–Pitts/Hebb; Shannon and Samuel arrive from era 01 in person.
- **Open questions for curation:** (a) whether Dendral (1965) should be drawn inside this era or as an exclave of era 03 — recommend a border town; (b) the Prolog/logic-programming cluster is geographically European (Marseille, Edinburgh) — consider a distinct A2 label; (c) Minsky's frames (1974) straddle the border — placed here as the last major artefact before the winter; (d) how prominently to draw the over-predictions (Simon 1965, Minsky 1970) — suggest A4 "monuments" rather than cities.

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
