# AI Winters, Expert Systems and the Connectionist Revival (1974–1993)

> **Status:** verified
> **Date range:** 1974–1993
> **Map placement (proposed):** X = 1974–1993; Y = *mixed*, strongly polarised — the commercial/knowledge-based mainstream (MYCIN, XCON, Fifth Generation, Lisp machines, Cyc) sits at the *symbolic/logic pole*; the 1980s revival (Hopfield 1982, backprop 1986, PDP, neocognitron, TD/Q-learning) re-opens the *connectionist/cybernetic pole*; Brooks' behaviour-based robotics and Pearl's Bayesian networks sit between them as new "third routes"
> **Altitude:** A1 continent ("Knowledge Era & Winters"); A2 countries ("Expert Systems Country", "Fifth Generation / Logic Programming", "Lisp Machine Industry", "Connectionist Revival", "Nouvelle AI & Probabilistic AI"); A3 cities (MYCIN, XCON/R1, Fifth Generation 1982, Cyc 1984, Hopfield 1982, Backprop 1986, PDP 1986, Subsumption 1986, Bayesian networks 1988, Lisp-machine collapse 1987); A4 streets

## One-paragraph summary
After the 1974 funding cliff, AI regrouped around a new thesis — Feigenbaum's "knowledge is power": intelligence in a domain comes less from clever general search than from large bodies of hand-coded expert knowledge. Dendral's successors MYCIN (Stanford, 1972–76) and PROSPECTOR showed rule-based expert systems could match specialists, and John McDermott's R1/XCON, configuring VAX orders at Digital Equipment from 1980, proved they could pay: by 1986 it was saving DEC an estimated $25M a year and corporations worldwide were building in-house AI groups. Japan's Fifth Generation Computer Systems project (1982) — massively parallel logic-programming machines — provoked matching national programmes (DARPA's Strategic Computing Initiative 1983, the UK's Alvey Programme 1984–90, the MCC consortium in Texas) and a knowledge-engineering industry of Lisp-machine makers (Symbolics, LMI, TI, Xerox) and shell vendors (Teknowledge, IntelliCorp). Underneath the boom, alternatives were maturing: Hopfield networks (1982), Fukushima's neocognitron (1979–80), and the 1986 backpropagation paper and *Parallel Distributed Processing* volumes revived neural networks; Pearl's Bayesian networks (1985–88) made probability respectable; Brooks' subsumption architecture (1986) rejected representation altogether; Sutton's TD learning (1988) and Watkins' Q-learning (1989) formalised reinforcement learning; and Quinlan's ID3 (1986) and the new journal *Machine Learning* (1986) marked ML as a discipline. Searle's Chinese Room (1980) reopened the philosophical front. Then the second winter: the Lisp-machine market collapsed in 1987 when general-purpose workstations overtook it, the SCI cut new AI spending in 1988, expert systems proved brittle and expensive to maintain, the Fifth Generation project closed in 1992 short of its goals, and by 1993 "AI" was a label researchers avoided even as machine learning, probabilistic reasoning and statistical NLP quietly gathered strength. Expert systems nonetheless left a lasting footprint: by the late 1980s two-thirds of Fortune 500 companies were using the technology.

## Timeline of key events
| Year | Event | Why it matters | Source |
|------|-------|----------------|--------|
| 1974 | First AI winter begins: DARPA cutbacks in the US following the 1973 Lighthill Report in the UK | Basic AI funding collapses on both sides of the Atlantic; UK AI survives only at Edinburgh, Essex, Sussex | [1], [2] |
| 1972–1976 | MYCIN developed at Stanford (Shortliffe's PhD, with Buchanan & Cohen) | Backward-chaining rule-based consultant with ~600 rules and certainty factors; template for expert systems; Newell: "the granddaddy of them all" | [3], [4] |
| 1975 | Newell & Simon, Turing Award lecture "Computer Science as Empirical Inquiry" (published 1976) | States the physical symbol system hypothesis — the creed of symbolic AI | [5] |
| 1976 | Weizenbaum, *Computer Power and Human Reason* | Insider critique of AI's social claims | [6] |
| 1977 | Feigenbaum, "The Art of Artificial Intelligence" (IJCAI-77): knowledge engineering and "knowledge is power" | Programmatic statement of the knowledge-based turn; EMYCIN shell separates inference engine from knowledge base | [7] |
| 1979 | Fukushima's neocognitron (paper 1980) | Hierarchical, shift-invariant multilayer network — direct ancestor of convolutional nets | [8] |
| 1979 | AAAI founded (as the American Association for Artificial Intelligence); *AI Magazine* launched 1980 | Field institutionalises in the US | [9] |
| 1980 | XCON/R1 (McDermott, CMU, written in OPS5) goes into production at DEC's Salem, NH plant | First big commercial expert-system success; ~2,500 rules, 80,000 orders by 1986, ~$25M/yr savings | [10], [11] |
| 1980 | Searle, "Minds, Brains, and Programs" (Chinese Room) | Landmark argument that symbol manipulation is not understanding; defines "strong AI" | [12] |
| 1981 | Symbolics ships the LM-2; Lisp-machine industry begins (Symbolics, LMI; later TI, Xerox) | Dedicated AI hardware market worth hundreds of millions by mid-decade | [13], [14] |
| 1982 | Japan's MITI launches the Fifth Generation Computer Systems project (ICOT) | Ten-year national programme for parallel logic-programming machines; triggers global competitive response | [15] |
| 1982 | Hopfield, "Neural networks and physical systems with emergent collective computational abilities" | Energy-based associative memory; brings physicists into neural nets | [16] |
| 1982 | Kohonen's self-organising maps; MCC consortium formed in Austin (Inman) as US response to Japan | Unsupervised neural learning; industrial AI consortium that will host Cyc | [17], [18] |
| 1983–84 | DARPA Strategic Computing Initiative (1983–1993, ~$1B); UK Alvey Programme (1984–1990, £350M) | Governments re-fund AI at scale in response to the Fifth Generation | [19], [20] |
| 1984 | Lenat begins Cyc at MCC (July 1984) | Decades-long attempt to hand-code commonsense knowledge; the symbolic pole's most ambitious bet | [18] |
| 1984 | "AI winter" term coined at the AAAI annual meeting (Schank & Minsky panel) | Insiders warn the business bubble will burst | [1] |
| 1985 | Pearl introduces the term "Bayesian networks"; book *Probabilistic Reasoning in Intelligent Systems* (1988) | Rigorous uncertainty handling replaces ad-hoc certainty factors; foundation of probabilistic AI | [21] |
| 1986 | Rumelhart, Hinton & Williams, "Learning representations by back-propagating errors" (*Nature*); Rumelhart & McClelland's two-volume *Parallel Distributed Processing* | Backpropagation for multilayer nets popularised; the connectionist revival goes mainstream | [22], [23] |
| 1986 | Brooks, "A Robust Layered Control System for a Mobile Robot" (subsumption architecture) | Behaviour-based robotics; explicit rejection of central symbolic representation | [24] |
| 1986 | Quinlan, "Induction of Decision Trees" (ID3), in vol. 1 of the new journal *Machine Learning* | Symbolic machine learning matures; ML acquires its own venue | [25], [26] |
| 1987 | Lisp-machine market collapses as Sun/Apple workstations and PCs run Lisp cheaper; first NIPS conference (Denver) | Second AI winter begins for industry; neural-net community gets its own conference | [1], [14], [27] |
| 1988 | Strategic Computing Initiative cancels new AI spending; Sutton, "Learning to Predict by the Methods of Temporal Differences" | Government retreat; TD learning formalises reinforcement learning | [1], [28] |
| 1989 | Watkins' PhD thesis introduces Q-learning (convergence proof with Dayan 1992); LeCun et al. apply backprop to handwritten ZIP-code recognition at Bell Labs | Model-free RL; first practical convolutional net | [29], [30] |
| 1990 | Brown et al. (IBM), "A Statistical Approach to Machine Translation"; Brooks, "Elephants Don't Play Chess" | Statistical NLP and Nouvelle AI stake out the post-symbolic future | [31], [32] |
| 1991 | Brooks, "Intelligence Without Representation" (*Artificial Intelligence* 47) | The definitive anti-representationalist manifesto | [32] |
| 1992 | Fifth Generation project's ten-year plan concludes without meeting its original goals (a wind-down phase runs to 1994); Tesauro's TD-Gammon reaches expert backgammon play | Symbolic megaproject closes in commercial failure; RL + neural nets deliver a striking result | [1], [15], [33] |
| 1993 | Symbolics and most Lisp companies fail or exit; SCI concludes; "AI" becomes a label to avoid — eastern border of this region | Bottom of the second winter; research continues under names like machine learning, informatics, knowledge-based systems | [1], [2], [14] |

## Key people
- **Edward Feigenbaum** (Stanford Heuristic Programming Project) — "father of expert systems"; Dendral, knowledge engineering, "knowledge is power"; co-author of *The Fifth Generation* (1983); Turing Award 1994. [7], [34]
- **Bruce Buchanan & Edward Shortliffe** (Stanford) — MYCIN and *Rule-Based Expert Systems* (1984); certainty factors; EMYCIN. [3], [4]
- **John P. McDermott** (Carnegie Mellon) — R1/XCON for DEC (1978–80); AAAI Classic Paper award for the 1980 R1 paper. [10], [11]
- **Charles Forgy** (CMU) — OPS5 and the Rete algorithm (1979–82), the production-system engine behind XCON. [10]
- **Douglas Lenat** (Stanford → MCC → Cycorp) — AM, EURISKO, and Cyc (from 1984). [18]
- **Ehud Shapiro** (Weizmann Institute; visiting ICOT 1982) — Concurrent Prolog; captured the rationale of the Fifth Generation programme. [15]
- **Russell Noftsker & Richard Greenblatt** (MIT AI Lab → Symbolics / LMI) — founders of the two Lisp-machine companies. [13], [14]
- **John Hopfield** (Caltech) — Hopfield networks (1982); later Nobel Prize in Physics 2024. [16]
- **David Rumelhart, Geoffrey Hinton & Ronald Williams** (UCSD / CMU) — backpropagation paper (1986); PDP Research Group with James McClelland. [22], [23]
- **Kunihiko Fukushima** (NHK Laboratories) — neocognitron (1979–80). [8]
- **Teuvo Kohonen** (Helsinki University of Technology) — self-organising maps (1982). [17]
- **Judea Pearl** (UCLA) — Bayesian networks (1985–88); Turing Award 2011. [21]
- **Rodney Brooks** (MIT) — subsumption architecture (1986), "Intelligence Without Representation" (1991). [24], [32]
- **Richard Sutton & Christopher Watkins** (UMass Amherst / Cambridge) — TD learning (1988), Q-learning (1989). [28], [29]
- **J. Ross Quinlan** (Sydney / RAND) — ID3 decision-tree induction (1986). [25]
- **Yann LeCun** (Bell Labs) — backprop applied to handwritten digit recognition (1989). [30]
- **John Searle** (Berkeley, philosopher) — the Chinese Room (1980). [12]
- **Roger Schank & Marvin Minsky** — warned of the coming "AI winter" at AAAI 1984. [1]

## Key papers / artifacts
- Shortliffe, E. H. et al. *Computer-Based Consultations in Clinical Therapeutics: Explanation and Rule Acquisition Capabilities of the MYCIN System*. Computers and Biomedical Research 8(4):303–320, 1975. https://doi.org/10.1016/0010-4809%2875%2990009-9 [3]
- Buchanan, B. G. & Shortliffe, E. H. (eds.). *Rule-Based Expert Systems: The MYCIN Experiments of the Stanford Heuristic Programming Project*. Addison-Wesley, 1984. https://www.shortliffe.net/Buchanan-Shortliffe-1984/MYCIN%20Book.htm [4]
- Newell, A. & Simon, H. A. *Computer Science as Empirical Inquiry: Symbols and Search*. CACM 19(3):113–126, 1976. doi:10.1145/360018.360022 — context: https://en.wikipedia.org/wiki/Physical_symbol_system [5]
- Feigenbaum, E. A. *The Art of Artificial Intelligence: Themes and Case Studies of Knowledge Engineering*. IJCAI-77, 1977. https://www.ijcai.org/Proceedings/77-2/Papers/092.pdf [7]
- Fukushima, K. *Neocognitron: A Self-Organizing Neural Network Model for a Mechanism of Pattern Recognition Unaffected by Shift in Position*. Biological Cybernetics 36:193–202, 1980. https://doi.org/10.1007/BF00344251 [8]
- Searle, J. R. *Minds, Brains, and Programs*. Behavioral and Brain Sciences 3(3):417–424, 1980. https://doi.org/10.1017/S0140525X00005756 [12]
- McDermott, J. *R1: A Rule-Based Configurer of Computer Systems*. Artificial Intelligence 19(1):39–88, 1982. https://doi.org/10.1016/0004-3702%2882%2990021-2 [11]
- Hopfield, J. J. *Neural Networks and Physical Systems with Emergent Collective Computational Abilities*. PNAS 79(8):2554–2558, 1982. doi:10.1073/pnas.79.8.2554 — open copy: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC346238/ [16]
- Kohonen, T. *Self-Organized Formation of Topologically Correct Feature Maps*. Biological Cybernetics 43:59–69, 1982. https://doi.org/10.1007/BF00337288 [17]
- Rumelhart, D. E., Hinton, G. E. & Williams, R. J. *Learning Representations by Back-Propagating Errors*. Nature 323:533–536, 1986. https://doi.org/10.1038/323533a0 [22]
- Rumelhart, D. E., McClelland, J. L. & the PDP Research Group. *Parallel Distributed Processing*, 2 vols. MIT Press, 1986. https://en.wikipedia.org/wiki/Connectionism [23]
- Brooks, R. A. *A Robust Layered Control System for a Mobile Robot*. IEEE Journal of Robotics and Automation 2(1):14–23, 1986. https://doi.org/10.1109/JRA.1986.1087032 [24]
- Quinlan, J. R. *Induction of Decision Trees*. Machine Learning 1:81–106, 1986. https://doi.org/10.1007/BF00116251 [25]
- Sutton, R. S. *Learning to Predict by the Methods of Temporal Differences*. Machine Learning 3:9–44, 1988. https://doi.org/10.1007/BF00115009 [28]
- LeCun, Y. et al. *Backpropagation Applied to Handwritten Zip Code Recognition*. Neural Computation 1(4):541–551, 1989. doi:10.1162/neco.1989.1.4.541 — open copy: http://yann.lecun.com/exdb/publis/pdf/lecun-89e.pdf [30]
- Brown, P. F. et al. *A Statistical Approach to Machine Translation*. Computational Linguistics 16(2):79–85, 1990. https://aclanthology.org/J90-2002/ [31]
- Brooks, R. A. *Intelligence Without Representation*. Artificial Intelligence 47(1–3):139–159, 1991. https://doi.org/10.1016/0004-3702%2891%2990053-M [32]
- Watkins, C. J. C. H. & Dayan, P. *Q-learning*. Machine Learning 8:279–292, 1992. https://doi.org/10.1007/BF00992698 [29]
- Lindsay, R. K., Buchanan, B. G., Feigenbaum, E. A. & Lederberg, J. *DENDRAL: A Case Study of the First Expert System for Scientific Hypothesis Formation*. Artificial Intelligence 61(2):209–261, 1993. https://doi.org/10.1016/0004-3702%2893%2990068-M [34]

## Schools of thought / sub-clusters
- **Knowledge-based / expert systems** (Stanford HPP, CMU; MYCIN, PROSPECTOR, XCON, EMYCIN shells; Teknowledge, IntelliCorp) — domain knowledge as production rules with an inference engine; certainty factors for uncertainty; borders: Dendral and frames/semantic nets (west, era 02), Cyc and ontologies (east within this era), Bayesian networks (rival across the uncertainty border), 1990s knowledge management and Semantic Web (far east). [3], [4], [7], [10], [11], [35]
- **Logic programming & the Fifth Generation** (ICOT Tokyo; Prolog, concurrent logic languages; Alvey and SCI as responses) — parallel inference machines running logic programs; borders: resolution/Prolog (west, era 02), constraint programming and theorem proving (east), national-programme politics (SCI, Alvey, MCC). [15], [19], [20]
- **Lisp-machine industry & AI commerce** (Symbolics, LMI, TI Explorer, Xerox Interlisp-D) — specialised hardware and software environments for symbolic AI; borders: MIT AI Lab hacker culture (west), workstation/PC economics that killed it (1987), Common Lisp standardisation. [13], [14]
- **Commonsense knowledge / Cyc** (Lenat at MCC) — encyclopaedic hand-built ontology; borders: McCarthy's Advice Taker (west), knowledge graphs and LLM-era commonsense debates (far east). [18]
- **Connectionist revival / PDP** (Hopfield, Rumelhart, Hinton, McClelland, Sejnowski, Fukushima, Kohonen, LeCun; NIPS from 1987) — distributed representations learned by gradient descent; borders: perceptron strip and the *Perceptrons* gap (west, era 02), 1990s neural-net plateau and the 2012 deep-learning revolution (far east), computational neuroscience (south). [8], [16], [17], [22], [23], [27], [30]
- **Probabilistic AI** (Pearl; Bayesian networks, belief propagation) — graphical models as principled uncertainty handling; borders: certainty factors and Dempster–Shafer in expert systems (west/north), 1990s Bayesian ML and causal inference (east). [21]
- **Reinforcement learning** (Sutton, Barto, Watkins, Tesauro) — learning from delayed reward; borders: Samuel's checkers and Minsky's SNARC (west, eras 01–02), TD-Gammon (1992) and deep RL (far east); shares a cybernetic ancestry with control theory. [28], [29], [33]
- **Symbolic machine learning** (Quinlan, Michalski, Mitchell; ID3, version spaces; *Machine Learning* journal 1986) — induction of explicit rules/trees from data; borders: expert-system knowledge acquisition bottleneck (which motivated it), statistical ML and data mining (east). [25], [26]
- **Nouvelle AI / behaviour-based robotics** (Brooks at MIT; subsumption, Allen, Genghis) — intelligence without central representation, situated in the world; borders: cybernetic tortoises and Ashby (west, era 01), Shakey's sense-plan-act (which it opposes), embodied cognition and later robotics (east). [24], [32]
- **Philosophical critics** (Searle, Dreyfus & Dreyfus *Mind over Machine* 1986, Weizenbaum) — borders: Turing test lineage (west), consciousness/AGI debates (far east). [6], [12]
- **Statistical NLP** (IBM Candide group, Brown et al. 1990) — MT from parallel corpora; borders: Georgetown–IBM and ALPAC (west), 1990s corpus linguistics and, eventually, neural MT (east). [31]

## Map notes
- **A1 label:** "The Knowledge Era" (or "Boom, Bust and Revival"). **A2 labels:** "Expert Systems Country" (Stanford–CMU–DEC axis), "Fifth Generation Shogunate" (Tokyo/ICOT with Alvey and SCI as satellite provinces), "Lisp Machine Industrial Belt" (Cambridge MA), "Cyc Territory" (Austin), "Connectionist Revival" (San Diego / CMU / Toronto / Bell Labs), "Bayesian Highlands" (UCLA), "Nouvelle AI Coast" (MIT), "RL Valley" (Amherst / Cambridge UK).
- **A3 labels:** "MYCIN", "XCON/R1 1980", "Fifth Generation 1982", "Hopfield 1982", "Cyc 1984", "Backprop 1986", "PDP 1986", "Subsumption 1986", "ID3 1986", "NIPS 1987", "Lisp Machine Crash 1987", "Bayesian Networks 1988", "TD 1988 / Q-learning 1989", "Chinese Room 1980".
- **Rivers/borders:** the western border is the *First Winter escarpment* (1974). Two bands of "frozen ground" should be shaded: 1974–1980 in the west and 1987–1993 in the east; the expert-systems boom lies between them as a warm valley. The *Symbolic Divide* from earlier eras is finally breached: the "Backprop Pass" (1986) reconnects the connectionist south to the mainstream, and a new *Probability River* (Pearl) begins to flow east. The eastern border (~1993) is a fog bank rather than a cliff — the field does not end, it renames itself.
- **Bridges east (to 1993–2012 region):** backprop → LeNet, LSTM, deep learning; Bayesian networks → graphical models, Bayesian ML; TD/Q-learning → TD-Gammon → deep RL; ID3 → C4.5, random forests, data mining; statistical MT → statistical NLP → neural MT; Cyc → knowledge graphs; subsumption → Roomba/iRobot and embodied AI; expert systems → business rules engines.
- **Bridges west:** MYCIN ← Dendral; XCON ← OPS/production systems ← Newell–Simon; Fifth Generation ← Prolog ← resolution; Hopfield/PDP ← perceptron ← McCulloch–Pitts/Hebb; Brooks ← Grey Walter/Ashby; TD learning ← Samuel/SNARC.
- **Open questions for curation:** (a) whether the two winters should be one continuous shaded feature ("the Winter Steppe") or two separate ones — recommend two, since the boom between them is the era's defining feature; (b) how much prominence to give national programmes (SCI, Alvey, MCC) — they are funding geography, not ideas; suggest A3 "forts"; (c) whether the connectionist revival (1982–1989) should be split off as its own A1 region beginning a new continent — recommend keeping it here but drawing it as a large peninsula that becomes the mainland of the next era; (d) the Nobel/Turing honours awarded much later (Hopfield & Hinton 2024, Pearl 2011, Feigenbaum 1994) — mark as A4 monuments, not events.

## Sources
[1] AI winter — Wikipedia — https://en.wikipedia.org/wiki/AI_winter (accessed 2026-09-06)
[2] History of artificial intelligence — Wikipedia — https://en.wikipedia.org/wiki/History_of_artificial_intelligence (accessed 2026-09-06)
[3] Mycin — Wikipedia — https://en.wikipedia.org/wiki/Mycin ; Shortliffe et al. 1975 https://doi.org/10.1016/0010-4809%2875%2990009-9 (accessed 2026-09-06)
[4] Buchanan & Shortliffe, Rule-Based Expert Systems (1984), full text — https://www.shortliffe.net/Buchanan-Shortliffe-1984/MYCIN%20Book.htm ; Edward Shortliffe https://en.wikipedia.org/wiki/Edward_Shortliffe (accessed 2026-09-06)
[5] Physical symbol system — Wikipedia — https://en.wikipedia.org/wiki/Physical_symbol_system (Newell & Simon 1976, doi:10.1145/360018.360022) (accessed 2026-09-06)
[6] Computer Power and Human Reason — Wikipedia — https://en.wikipedia.org/wiki/Computer_Power_and_Human_Reason ; Joseph Weizenbaum https://en.wikipedia.org/wiki/Joseph_Weizenbaum (accessed 2026-09-06)
[7] Feigenbaum, The Art of Artificial Intelligence (IJCAI 1977) — https://www.ijcai.org/Proceedings/77-2/Papers/092.pdf ; Knowledge engineering https://en.wikipedia.org/wiki/Knowledge_engineering (accessed 2026-09-06)
[8] Fukushima, Neocognitron (1980) — https://doi.org/10.1007/BF00344251 ; Neocognitron — Wikipedia https://en.wikipedia.org/wiki/Neocognitron (accessed 2026-09-06)
[9] Association for the Advancement of Artificial Intelligence — Wikipedia — https://en.wikipedia.org/wiki/Association_for_the_Advancement_of_Artificial_Intelligence (accessed 2026-09-06)
[10] Xcon — Wikipedia — https://en.wikipedia.org/wiki/Xcon ; OPS5 https://en.wikipedia.org/wiki/OPS5 ; Rete algorithm https://en.wikipedia.org/wiki/Rete_algorithm (accessed 2026-09-06)
[11] McDermott, R1: A Rule-Based Configurer of Computer Systems (1982) — https://doi.org/10.1016/0004-3702%2882%2990021-2 (accessed 2026-09-06)
[12] Searle, Minds, Brains, and Programs (1980) — https://doi.org/10.1017/S0140525X00005756 ; Chinese room — Wikipedia https://en.wikipedia.org/wiki/Chinese_room (accessed 2026-09-06)
[13] Symbolics — Wikipedia — https://en.wikipedia.org/wiki/Symbolics (accessed 2026-09-06)
[14] Lisp machine — Wikipedia — https://en.wikipedia.org/wiki/Lisp_machine (accessed 2026-09-06)
[15] Fifth Generation Computer Systems — Wikipedia — https://en.wikipedia.org/wiki/Fifth_Generation_Computer_Systems ; ICOT https://en.wikipedia.org/wiki/Institute_for_New_Generation_Computer_Technology (accessed 2026-09-06)
[16] Hopfield, Neural networks and physical systems… (PNAS 1982) — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC346238/ ; Hopfield network — Wikipedia https://en.wikipedia.org/wiki/Hopfield_network (accessed 2026-09-06)
[17] Kohonen, Self-organized formation of topologically correct feature maps (1982) — https://doi.org/10.1007/BF00337288 ; Self-organizing map https://en.wikipedia.org/wiki/Self-organizing_map (accessed 2026-09-06)
[18] Cyc — Wikipedia — https://en.wikipedia.org/wiki/Cyc ; Microelectronics and Computer Technology Corporation https://en.wikipedia.org/wiki/Microelectronics_and_Computer_Technology_Corporation ; Douglas Lenat https://en.wikipedia.org/wiki/Douglas_Lenat (accessed 2026-09-06)
[19] Strategic Computing Initiative — Wikipedia — https://en.wikipedia.org/wiki/Strategic_Computing_Initiative (accessed 2026-09-06)
[20] Alvey — Wikipedia — https://en.wikipedia.org/wiki/Alvey (accessed 2026-09-06)
[21] Bayesian network — Wikipedia — https://en.wikipedia.org/wiki/Bayesian_network ; Judea Pearl https://en.wikipedia.org/wiki/Judea_Pearl (accessed 2026-09-06)
[22] Rumelhart, Hinton & Williams, Learning representations by back-propagating errors (Nature 1986) — https://doi.org/10.1038/323533a0 ; Backpropagation https://en.wikipedia.org/wiki/Backpropagation (accessed 2026-09-06)
[23] Connectionism / Parallel Distributed Processing — Wikipedia — https://en.wikipedia.org/wiki/Connectionism ; https://en.wikipedia.org/wiki/Parallel_Distributed_Processing (accessed 2026-09-06)
[24] Brooks, A Robust Layered Control System for a Mobile Robot (1986) — https://doi.org/10.1109/JRA.1986.1087032 ; Subsumption architecture https://en.wikipedia.org/wiki/Subsumption_architecture (accessed 2026-09-06)
[25] Quinlan, Induction of Decision Trees (1986) — https://doi.org/10.1007/BF00116251 ; ID3 algorithm https://en.wikipedia.org/wiki/ID3_algorithm (accessed 2026-09-06)
[26] Machine Learning (journal) — Wikipedia — https://en.wikipedia.org/wiki/Machine_Learning_%28journal%29 (accessed 2026-09-06)
[27] Conference on Neural Information Processing Systems — Wikipedia — https://en.wikipedia.org/wiki/Conference_on_Neural_Information_Processing_Systems (accessed 2026-09-06)
[28] Sutton, Learning to Predict by the Methods of Temporal Differences (1988) — https://doi.org/10.1007/BF00115009 ; Temporal difference learning https://en.wikipedia.org/wiki/Temporal_difference_learning (accessed 2026-09-06)
[29] Watkins & Dayan, Q-learning (1992) — https://doi.org/10.1007/BF00992698 ; Q-learning — Wikipedia https://en.wikipedia.org/wiki/Q-learning (accessed 2026-09-06)
[30] LeCun et al., Backpropagation Applied to Handwritten Zip Code Recognition (1989) — http://yann.lecun.com/exdb/publis/pdf/lecun-89e.pdf ; LeNet https://en.wikipedia.org/wiki/LeNet (accessed 2026-09-06)
[31] Brown et al., A Statistical Approach to Machine Translation (1990) — https://aclanthology.org/J90-2002/ (accessed 2026-09-06)
[32] Brooks, Intelligence Without Representation (1991) — https://doi.org/10.1016/0004-3702%2891%2990053-M ; Rodney Brooks https://en.wikipedia.org/wiki/Rodney_Brooks (accessed 2026-09-06)
[33] TD-Gammon — Wikipedia — https://en.wikipedia.org/wiki/TD-Gammon (accessed 2026-09-06)
[34] Edward Feigenbaum — Wikipedia — https://en.wikipedia.org/wiki/Edward_Feigenbaum ; Lindsay et al., DENDRAL: A Case Study… (1993) https://doi.org/10.1016/0004-3702%2893%2990068-M ; Dendral https://en.wikipedia.org/wiki/Dendral (accessed 2026-09-06)
[35] Expert system — Wikipedia — https://en.wikipedia.org/wiki/Expert_system (accessed 2026-09-06)
[36] AAAI, A Brief History of AI — https://aitopics.org/misc/brief-history (accessed 2026-09-06)
[37] Nilsson, N. J. *The Quest for Artificial Intelligence* (2010), free PDF — https://ai.stanford.edu/~nilsson/QAI/qai.pdf (accessed 2026-09-06)
