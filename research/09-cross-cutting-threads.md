# Cross-Cutting Threads (rivers and roads spanning the whole map)

> **Status:** verified
> **Date range:** 1942–2026 (each thread spans several eras; see per-thread "Eras crossed")
> **Map placement (proposed):** X = full width of the map; Y = varies per thread — RL and hardware run along the connectionist/scaling bank, robotics and game-playing zig-zag between poles, safety/ethics and open-vs-closed run across both banks as roads rather than rivers
> **Altitude:** A1 (rivers/roads visible at continent scale), A2 (named reaches/junctions), A3 (individual milestone landmarks along each thread)

## One-paragraph summary
Eight themes recur in every era of AI history and therefore cannot be drawn as regions; they must be drawn as linear features — rivers (technical lineages that flow and merge: reinforcement learning, NLP, computer vision, hardware, game-playing) and roads (social/institutional debates that people travel along: safety & ethics, open vs closed, robotics as an applied frontier). This file catalogues each thread with 5–10 dated, sourced milestones and the eras it crosses, so the cartographer can route it across the era-based continents described in files 01–08. Reinforcement learning is the longest river (Bellman 1957 → RLHF 2022 → reasoning models 2025); hardware is the deepest (Lisp machines → CUDA → TPU → Blackwell), and every technical river ultimately empties into the Generative Coast of file 08. Safety/ethics and open-vs-closed are roads with forts and toll-gates (Asimov's laws, Wiener 1960, Bostrom 2014, the LLaMA leak 2023, Bletchley 2023, the EU AI Act 2024) where travellers from different eras argue about the same questions.

## Threads

### (a) Reinforcement learning — "the RL River"
**Description.** Learning from reward rather than labelled examples has its headwaters in Bellman's dynamic programming (1957) and Samuel's self-improving checkers player, is formalised in the 1980s–90s by Sutton and Barto (temporal-difference learning, 1988) and Watkins (Q-learning, 1989), and first startles the world with Tesauro's TD-Gammon (1992). It runs underground during the statistical-ML years, resurfaces as *deep* RL with DQN (2013/2015) and AlphaGo (2016), and then turns unexpectedly into the main channel of the LLM era: RLHF (2017 preferences paper → InstructGPT 2022 → ChatGPT) and RL-trained reasoning models (o1 2024, DeepSeek-R1 2025). The 2024 Turing Award to Barto and Sutton (announced March 2025) marks the river's canonisation. [a1]–[a10]

**Milestones.**
| Year | Milestone | Source |
|------|-----------|--------|
| 1957 | Richard Bellman publishes *Dynamic Programming*; the Bellman equation becomes the mathematical core of RL | [a1] |
| 1959 | Arthur Samuel's checkers program (IBM) learns from self-play; Samuel coins "machine learning" | [a2] |
| 1988 | Richard Sutton, "Learning to Predict by the Methods of Temporal Differences" (Machine Learning 3) — TD(λ) | [a3] |
| 1989 | Chris Watkins introduces Q-learning (PhD thesis *Learning from Delayed Rewards*); convergence proof with Dayan, 1992 | [a4] |
| 1992 | Gerald Tesauro's TD-Gammon (IBM) reaches world-class backgammon via TD learning and self-play | [a5] |
| 1998 | Sutton & Barto, *Reinforcement Learning: An Introduction* (MIT Press; 2nd ed. 2018) | [a6] |
| 2013/2015 | DeepMind DQN plays Atari from pixels (arXiv 1312.5602, Dec 2013; Nature, Feb 2015) | [a7] |
| 2016 (Mar) | AlphaGo defeats Lee Sedol 4–1 in Seoul (9–15 March 2016); AlphaGo Zero (Oct 2017) and AlphaZero (Dec 2017) learn from self-play alone | [a8] |
| 2017 (Jun) | Christiano et al., "Deep RL from Human Preferences" (arXiv 1706.03741); PPO (arXiv 1707.06347, Jul 2017) — the two ingredients of RLHF | [a9] |
| 2022–2025 | InstructGPT/RLHF (Mar 2022) → ChatGPT; RL-trained reasoning models o1 (Sep 2024) and DeepSeek-R1 (Jan 2025); Barto & Sutton receive the 2024 ACM Turing Award | [a10] |

**Eras crossed.** Cybernetics/foundations (1940s–50s) → symbolic era (dynamic programming, checkers) → connectionist revival (TD-Gammon) → statistical ML → deep learning (DQN, AlphaGo) → Transformer plateau (RLHF) → Generative Coast (reasoning models). Y-position: connectionist bank, but with a symbolic-side tributary (search/planning: MCTS in AlphaGo, MuZero's learned model).

### (b) Robotics / embodied AI — "the Embodiment Road"
**Description.** Robotics is where AI meets the physical world and where each era's dominant paradigm is tested hardest. Shakey (SRI, 1966–72) was the first mobile robot to reason about its actions with symbolic planning (STRIPS) and gave us A* search; Brooks's subsumption architecture (1986) rejected central world models in favour of layered reactive behaviours; the DARPA Grand and Urban Challenges (2004–2007) and Robotics Challenge (2012–2015) turned autonomy into a competitive engineering discipline and seeded the self-driving industry; Boston Dynamics (founded 1992) made dynamic legged locomotion iconic (BigDog 2005, Atlas 2013, Spot); and since 2022–23 the Transformer plateau has reached the road via vision-language-action (VLA) models — RT-1 (Dec 2022), RT-2 (Jul 2023), π0 (Oct 2024), Figure's Helix and Gemini Robotics (2025). [b1]–[b9]

**Milestones.**
| Year | Milestone | Source |
|------|-----------|--------|
| 1961 | Unimate, the first industrial robot, works a General Motors assembly line | [b1] |
| 1966–1972 | Shakey the Robot (SRI): first general-purpose mobile robot to reason about its actions; STRIPS planner, A* search, Hough transform emerge from the project | [b2] |
| 1979–1980 | Hans Moravec's Stanford Cart negotiates cluttered obstacle courses using stereo vision | [b3] |
| 1986 | Rodney Brooks, "A Robust Layered Control System for a Mobile Robot" — the subsumption architecture and behaviour-based robotics | [b4] |
| 1992 | Boston Dynamics founded as an MIT spin-off (Marc Raibert); BigDog 2005; Atlas unveiled 11 Jul 2013; acquired by Google 2013, SoftBank 2017, Hyundai 2020–21 | [b5] |
| 2004–2007 | DARPA Grand Challenge (2004, no finisher; 2005 won by Stanford's Stanley) and Urban Challenge (2007) | [b6] |
| 2012–2015 | DARPA Robotics Challenge for disaster-response humanoids | [b7] |
| 2022 (Dec) – 2023 (Jul) | Google's RT-1 Robotics Transformer (arXiv 2212.06817) and RT-2 vision-language-action model (arXiv 2307.15818) | [b8] |
| 2024–2025 | Physical Intelligence π0 (arXiv 2410.24164, Oct 2024); OpenVLA (arXiv 2406.09246); Gemini Robotics (12 Mar 2025); Figure Helix VLA | [b9] |

**Eras crossed.** Symbolic era (Shakey) → AI winter/behaviour-based reaction (Brooks) → probabilistic robotics & DARPA challenges (2000s) → deep learning (perception) → Generative Coast (VLA models). Y-position: starts at the symbolic pole, swings hard to the anti-representational pole with Brooks, and ends "mixed" as LLM planners drive learned controllers.

### (c) AI safety, alignment and ethics — "the Conscience Road"
**Description.** Worries about machines pursuing the wrong goals are as old as the field: Asimov's Three Laws (1942) in fiction, Wiener's 1960 *Science* essay "Some Moral and Technical Consequences of Automation" (the earliest statement of the alignment problem), and Weizenbaum's *Computer Power and Human Reason* (1976). The road splits in the 2010s into an *existential-risk* lane (MIRI, Bostrom's *Superintelligence* 2014, FLI open letter 2015, "Concrete Problems in AI Safety" 2016, Asilomar Principles 2017) and a *present-harms* lane (ProPublica's COMPAS investigation 2016, Gender Shades 2018, "Stochastic Parrots" 2021), before both lanes converge in the policy district of the Generative Coast: the 2023 pause letter and extinction statement, the Bletchley Declaration (Nov 2023), US EO 14110 (Oct 2023), and the EU AI Act (in force Aug 2024). [c1]–[c10]

**Milestones.**
| Year | Milestone | Source |
|------|-----------|--------|
| 1942 | Isaac Asimov's "Runaround" introduces the Three Laws of Robotics | [c1] |
| 1960 | Norbert Wiener, "Some Moral and Technical Consequences of Automation" (Science) — states the alignment problem in modern form | [c2] |
| 1976 | Joseph Weizenbaum, *Computer Power and Human Reason* — computers should never make decisions requiring compassion or wisdom | [c3] |
| 2014 | Nick Bostrom, *Superintelligence: Paths, Dangers, Strategies*; 2015 FLI open letter (Hawking, Musk, AI researchers) | [c4] |
| 2016 | Amodei et al., "Concrete Problems in AI Safety" (arXiv 1606.06565); ProPublica's "Machine Bias" COMPAS investigation; Partnership on AI founded | [c5] |
| 2017 | Asilomar AI Principles (FLI conference, 5–8 Jan 2017) | [c6] |
| 2018–2021 | Gender Shades (Buolamwini & Gebru, 2018); Model Cards (arXiv 1810.03993); "On the Dangers of Stochastic Parrots" (FAccT, Mar 2021) | [c7] |
| 2023 | "Pause Giant AI Experiments" letter (Mar); CAIS Statement on AI Risk (30 May); Hinton leaves Google (May); Bletchley Declaration (1–2 Nov); US EO 14110 (30 Oct) | [c8] |
| 2024 | EU AI Act passes Parliament 13 Mar, in force 1 Aug 2024 | [c9] |
| 2022–2024 | Technical alignment toolkit matures: Constitutional AI (Dec 2022), DPO (2023), mechanistic interpretability; safety institutes founded | [c10] |

**Eras crossed.** Every era from cybernetics onward; densest at the symbolic-era ELIZA controversy (Weizenbaum), the 2010s deep-learning ethics reckoning, and the 2023–24 policy district. Y-position: a road that runs across both banks — it is deliberately paradigm-agnostic.

### (d) Hardware and compute — "the Silicon River"
**Description.** Compute has repeatedly decided which paradigm wins. The symbolic era built specialised Lisp machines (MIT 1973 → Symbolics/LMI in the 1980s) and Thinking Machines' Connection Machine (CM-1, 1985); their collapse against commodity workstations in 1987 helped trigger the second AI winter. The connectionist revival was carried by commodity graphics chips: Nvidia's GeForce 256 (1999, marketed as the first "GPU"), CUDA (2007) turning GPUs into general-purpose parallel machines, and AlexNet's two GTX 580s (2012). Once scaling laws (2020) made compute a strategy, purpose-built accelerators and data-centre GPUs became geopolitical assets — Google's TPU (announced May 2016), Nvidia's DGX-1 (2016), A100, Hopper H100 (announced Mar 2022) and Blackwell (Mar 2024) — and Nvidia became the first company to exceed $4 trillion in market value (2025). [d1]–[d9]

**Milestones.**
| Year | Milestone | Source |
|------|-----------|--------|
| 1973–1980s | MIT Lisp machine project (Greenblatt & Knight, 1973); commercial Lisp machines from Symbolics, LMI and Texas Instruments in the 1980s; market collapses in 1987 | [d1] |
| 1985 | Thinking Machines' Connection Machine CM-1 (Danny Hillis), massively parallel hardware aimed at AI | [d2] |
| 1999 | Nvidia GeForce 256, marketed as "the world's first GPU" | [d3] |
| 2007 | Nvidia releases CUDA (created 2004), enabling general-purpose GPU computing | [d4] |
| 2012 | AlexNet trained on GPUs wins ILSVRC 2012, launching the deep-learning boom | [d5] |
| 2016 | Google announces the Tensor Processing Unit at I/O (May 2016), after >1 year of internal use; Nvidia announces DGX-1 (6 Apr 2016) | [d6] |
| 2020 | Kaplan et al. scaling laws; compute becomes the planning variable for frontier labs | [d7] |
| 2022 (Mar) | Nvidia Hopper architecture / H100 announced at GTC 2022, with a "transformer engine" | [d8] |
| 2024 (18 Mar) | Nvidia Blackwell announced at GTC 2024; Nvidia passes $1T (2023), $4T and $5T (2025) market capitalisation | [d9] |

**Eras crossed.** Symbolic era (Lisp machines) → AI winter (their collapse) → deep learning (GPUs/CUDA) → Transformer plateau (TPU, scaling laws) → Generative Coast (H100/Blackwell, export controls). Y-position: connectionist/scaling bank after 1999; symbolic bank before.

### (e) Open vs closed — "the Commons Road"
**Description.** Whether AI artefacts are shared or withheld has oscillated with each era. Academic openness (Weka 1993, Torch, Theano, Caffe 2014) gave way to corporate-but-open frameworks (TensorFlow 2015, PyTorch 2016–17, Hugging Face Transformers 2019) that made deep learning a commons. OpenAI's staged GPT-2 release (2019) was the first deliberate withholding on safety grounds; GPT-3 (2020) shipped as an API only, and GPT-4 (2023) without architectural details. The counter-movement — EleutherAI (2020), BLOOM (2022), Stable Diffusion (Aug 2022) — became mainstream when Meta's LLaMA weights leaked (3 Mar 2023) and Meta then embraced open weights with Llama 2 (Jul 2023) and Llama 3 (Apr 2024); Mistral (2023), Qwen and DeepSeek (V3 Dec 2024, R1 Jan 2025) extended the commons to Europe and China; even OpenAI returned with gpt-oss (Aug 2025). The Open Source Initiative's 2024 Open Source AI Definition formalised the "open weights ≠ open source" debate. [e1]–[e10]

**Milestones.**
| Year | Milestone | Source |
|------|-----------|--------|
| 1993–2014 | Open ML tooling era: Weka (GPL), Torch, Theano, Caffe (Berkeley, 2014) | [e1] |
| 2015–2017 | Google open-sources TensorFlow (Apache 2.0, 2015); Facebook releases PyTorch (2016–17) | [e2] |
| 2019 | OpenAI staggers GPT-2 release over misuse concerns (Feb → Nov 2019); Hugging Face Transformers becomes the open model hub | [e3] |
| 2020–2022 | EleutherAI (The Pile, GPT-J), BigScience BLOOM (Jul 2022), Stable Diffusion weights released (22 Aug 2022) | [e4] |
| 2023 (Feb–Mar) | LLaMA released to researchers (24 Feb), leaked on 4chan (3 Mar); Alpaca, Vicuna, llama.cpp follow within weeks | [e5] |
| 2023 (Jul) | Llama 2 released for commercial use with Microsoft | [e6] |
| 2023 (Sep–Dec) | Mistral 7B (Apache 2.0, 27 Sep) and Mixtral 8x7B (11 Dec) | [e7] |
| 2024 | Llama 3 (18 Apr) and Llama 3.1 405B (Jul); OSI publishes Open Source AI Definition 1.0 | [e8] |
| 2024–2025 | DeepSeek-V3 (26 Dec 2024) and R1 (20 Jan 2025, MIT licence); Qwen3 (Apache 2.0, 28 Apr 2025) | [e9] |
| 2025 (5 Aug) | OpenAI releases gpt-oss-120b/20b under Apache 2.0 — first open weights since GPT-2 | [e10] |

**Eras crossed.** Statistical ML (open toolkits) → deep learning (open frameworks) → Transformer plateau (GPT-2 withholding, EleutherAI) → Generative Coast (Llama, Mistral, DeepSeek). Y-position: a road that hugs the connectionist bank, with toll-gates (closed APIs) and free crossings (open weights).

### (f) Natural language processing lineage — "the Language River"
**Description.** NLP is the thread that most directly leads to today's LLMs. It begins with the Georgetown–IBM machine-translation demo (1954) and the optimism ALPAC crushed in 1966; runs through symbolic dialogue systems (ELIZA 1964–67, SHRDLU 1968–70); turns statistical with IBM's speech and translation work (Jelinek from 1972; IBM alignment models, early 1990s) and hidden Markov models; becomes neural with word2vec (2013), seq2seq and attention (2014), Google Neural Machine Translation (2016) and LSTMs; and then floods into the Transformer plateau — ELMo, GPT, BERT (2018), GPT-3 (2020) — and the Generative Coast (ChatGPT 2022). [f1]–[f9]

**Milestones.**
| Year | Milestone | Source |
|------|-----------|--------|
| 1954 (7 Jan) | Georgetown–IBM experiment translates 60+ Russian sentences; 1966 ALPAC report cuts MT funding | [f1] |
| 1964–1967 | Joseph Weizenbaum's ELIZA (MIT) — pattern-matching chatbot | [f2] |
| 1968–1970 | Terry Winograd's SHRDLU (MIT) — natural-language understanding in a blocks world | [f3] |
| 1972–1993 | Statistical turn: Jelinek's IBM speech group (from 1972); IBM alignment models for statistical MT (early 1990s) | [f4] |
| 1997 | Hochreiter & Schmidhuber, Long Short-Term Memory (Neural Computation) | [f5] |
| 2013 | Mikolov et al., word2vec (Google) — dense word embeddings at scale | [f6] |
| 2014 | Sutskever et al. seq2seq (arXiv 1409.3215) and Bahdanau et al. attention (arXiv 1409.0473); GNMT deployed Nov 2016 | [f7] |
| 2017–2018 | Transformer (Jun 2017); ELMo (Feb 2018), GPT-1 (Jun 2018), BERT (Oct 2018) | [f8] |
| 2020–2022 | GPT-3 (May 2020) → InstructGPT (Mar 2022) → ChatGPT (30 Nov 2022) | [f9] |

**Eras crossed.** Foundations/symbolic (Georgetown, ELIZA, SHRDLU) → AI winter (ALPAC) → statistical ML (HMMs, IBM models) → deep learning (word2vec, seq2seq) → Transformer plateau → Generative Coast. Y-position: begins at the symbolic pole (grammars, rules) and crosses fully to the connectionist pole by 2014.

### (g) Computer vision lineage — "the Vision River"
**Description.** Vision starts in neuroscience — Hubel and Wiesel's 1959 cat-cortex recordings of orientation-selective cells — and in Larry Roberts's 1963 MIT thesis "Machine Perception of Three-Dimensional Solids"; MIT's 1966 "Summer Vision Project" famously underestimated the problem. Fukushima's Neocognitron (1979) and LeCun's LeNet convolutional networks (1989–1998) laid the neural groundwork while hand-engineered features (SIFT 1999, Viola–Jones 2001) dominated the 2000s. ImageNet (2009) and AlexNet's 2012 ILSVRC win flipped the field to deep learning; ResNet (2015), Faster R-CNN and YOLO (2015) made detection real-time; GANs (2014) began the generative turn; and the Vision Transformer (2020), CLIP (2021), diffusion models (Stable Diffusion 2022, Sora 2024) and Segment Anything (2023) merged vision into the multimodal foundation-model mainstream. [g1]–[g10]

**Milestones.**
| Year | Milestone | Source |
|------|-----------|--------|
| 1959 | Hubel & Wiesel record orientation-selective neurons in cat visual cortex (Nobel 1981) | [g1] |
| 1963–1966 | Larry Roberts's "Machine Perception of Three-Dimensional Solids"; MIT Summer Vision Project (1966) | [g2] |
| 1979 | Kunihiko Fukushima's Neocognitron — hierarchical, shift-invariant network inspiring CNNs | [g3] |
| 1989–1998 | Yann LeCun's LeNet convolutional networks at Bell Labs read handwritten digits and cheques | [g4] |
| 1999–2001 | David Lowe's SIFT features (1999); Viola–Jones face detector (2001) | [g5] |
| 2009–2012 | ImageNet presented at CVPR 2009; ILSVRC from 2010; AlexNet wins ILSVRC 2012 on GPUs | [g6] |
| 2014–2015 | GANs (Goodfellow, Jun 2014); ResNet wins ILSVRC 2015; Faster R-CNN and YOLO (2015) | [g7] |
| 2020–2021 | Vision Transformer (Oct 2020); CLIP and DALL-E (Jan 2021) | [g8] |
| 2022–2024 | Latent diffusion / Stable Diffusion (Aug 2022), DALL-E 2, Midjourney; Segment Anything (Apr 2023); Sora (Feb 2024) | [g9] |
| 2023–2025 | Vision feeds robotics: RT-2, π0, Gemini Robotics (VLA models) | [g10] |

**Eras crossed.** Cybernetics/neuroscience → symbolic era (Roberts, blocks world) → connectionist revival (Neocognitron, LeNet) → statistical ML (SIFT, Viola–Jones) → deep learning (AlexNet, ResNet) → Transformer plateau (ViT, CLIP) → Generative Coast (diffusion, SAM). Y-position: connectionist bank throughout, with a hand-engineered-features meander in the 2000s.

### (h) Game-playing milestones — "the Tournament Road"
**Description.** Games have been AI's public proving ground since Samuel's checkers (1950s), because they offer clear rules and clear scores. The road passes IBM's landmark spectacles — Deep Blue beating Kasparov (May 1997) and Watson winning *Jeopardy!* (Feb 2011) — and Chinook, the first program to win a human world championship (checkers, 1994; game solved 2007). Deep RL then swept imperfect-information and real-time games: AlphaGo (2016), AlphaGo Zero/AlphaZero (2017), Libratus (2017) and Pluribus (2019) in poker, OpenAI Five in Dota 2 (2018–19), AlphaStar in StarCraft II (2019), and MuZero (2019/2020) learning rules from scratch. After 2020 the road merges into the RL river's LLM reach (reasoning models). [h1]–[h10]

**Milestones.**
| Year | Milestone | Source |
|------|-----------|--------|
| 1959 | Arthur Samuel's self-learning checkers program (IBM) | [h1] |
| 1994 & 2007 | Chinook (Jonathan Schaeffer, U. Alberta) becomes Man–Machine checkers champion (1994); checkers solved (2007) | [h2] |
| 1996–1997 | IBM Deep Blue loses to Kasparov 1996 (Feb), wins rematch 3½–2½ in May 1997 | [h3] |
| 2011 (14–16 Feb) | IBM Watson defeats Brad Rutter and Ken Jennings on *Jeopardy!* | [h4] |
| 2015–2016 | AlphaGo beats Fan Hui (Oct 2015; Nature Jan 2016) and Lee Sedol 4–1 (Mar 2016) | [h5] |
| 2017 | AlphaGo Zero (Nature, Oct 2017) and AlphaZero (arXiv, 5 Dec 2017) master Go, chess and shogi from self-play; Libratus beats poker pros (Jan 2017) | [h6] |
| 2018–2019 | OpenAI Five plays pros at The International 2018 and beats champions OG (Apr 2019) | [h7] |
| 2019 | AlphaStar reaches Grandmaster in StarCraft II (Nature, Oct/Nov 2019); Pluribus beats pros in six-player no-limit hold'em | [h8] |
| 2019–2020 | MuZero masters Go, chess, shogi and Atari without being told the rules (Nature, Dec 2020) | [h9] |
| 2024 | AlphaGeometry solves IMO-level geometry (Nature, Jan 2024) — games give way to olympiad mathematics | [h10] |

**Eras crossed.** Symbolic era (Samuel, minimax search) → expert-systems/IBM engineering (Deep Blue, Watson) → deep learning (AlphaGo) → Transformer plateau (MuZero era) → Generative Coast (reasoning models, olympiad maths). Y-position: starts at the symbolic pole (search), ends at the connectionist pole (learned evaluation + search hybrids — a true "mixed" road).

## Schools of thought / sub-clusters
- **Rivers (technical lineages)** — RL (a), hardware (d), NLP (f), vision (g): drawn as watercourses that widen as they approach the Generative Coast, where (a), (f) and (g) merge into one delta (LLMs + RLHF + multimodality). Borders: each rises in a specific western era (cybernetics, symbolic) and touches every continent en route.
- **Roads (social/institutional debates)** — safety/ethics (c) and open-vs-closed (e): drawn as roads with milestones and toll-gates crossing rivers via bridges (e.g. the GPT-2 staged release is a bridge where (c) and (e) cross). Borders: paradigm-agnostic; they connect symbolic-era critics (Weizenbaum) to connectionist-era critics (Gebru/Bender).
- **Applied frontiers** — robotics (b) and game-playing (h): drawn as roads that alternate between banks because each era used them as demonstrations of its paradigm (STRIPS vs subsumption; minimax vs self-play).

## Map notes
- Suggested A1 labels: **RL River**, **Language River**, **Vision River**, **Silicon River**, **Conscience Road**, **Commons Road**, **Embodiment Road**, **Tournament Road**.
- Rivers/borders/bridges: key confluences to mark — *Bellman → TD-Gammon → DQN → AlphaGo → RLHF* (RL joins Language at InstructGPT 2022); *CLIP bridge* (Vision joins Language, 2021); *AlexNet junction* (Silicon River carries Vision River across the deep-learning rapids, 2012); *LLaMA leak fork* (Commons Road splits the Generative Coast, Mar 2023); *Bletchley/EU AI Act toll-gates* (Conscience Road, 2023–24).
- Open questions for curation: (1) whether Game-playing should be a branch of the RL River rather than its own road; (2) whether to draw a ninth thread for "AI in science" (AlphaFold, Nobel 2024) or fold it into Vision/RL; (3) how to depict the 2024 Nobel/Turing awards (monuments at the RL and connectionist confluences?); (4) how far east to extend each thread given the "Needs verification" strip in file 08.

## Sources
**Thread (a) — Reinforcement learning**
[a1] Wikipedia: Richard E. Bellman (1957, *Dynamic Programming*) — https://en.wikipedia.org/wiki/Richard_E._Bellman (accessed 2026-09-06); Wikipedia: Bellman equation — https://en.wikipedia.org/wiki/Bellman_equation
[a2] Wikipedia: Arthur Samuel (computer scientist) — https://en.wikipedia.org/wiki/Arthur_Samuel_%28computer_scientist%29 (accessed 2026-09-06)
[a3] Sutton, R. S. "Learning to Predict by the Methods of Temporal Differences", Machine Learning 3, 1988 — https://link.springer.com/article/10.1007/BF00115009 (accessed 2026-09-06); Wikipedia: Temporal difference learning — https://en.wikipedia.org/wiki/Temporal_difference_learning
[a4] Wikipedia: Q-learning (Watkins 1989; Watkins & Dayan 1992) — https://en.wikipedia.org/wiki/Q-learning (accessed 2026-09-06); Watkins & Dayan, "Q-learning", Machine Learning 8, 1992 — https://link.springer.com/article/10.1007/BF00992698
[a5] Wikipedia: TD-Gammon — https://en.wikipedia.org/wiki/TD-Gammon (accessed 2026-09-06); Wikipedia: Gerald Tesauro — https://en.wikipedia.org/wiki/Gerald_Tesauro
[a6] Sutton & Barto, *Reinforcement Learning: An Introduction*, MIT Press 1998 / 2018 — http://incompleteideas.net/book/the-book-2nd.html (accessed 2026-09-06); Wikipedia: Andrew Barto — https://en.wikipedia.org/wiki/Andrew_Barto
[a7] Mnih et al., "Playing Atari with Deep Reinforcement Learning" — arXiv 1312.5602 — https://arxiv.org/abs/1312.5602; "Human-level control through deep reinforcement learning", Nature 2015 — https://www.nature.com/articles/nature14236 (accessed 2026-09-06)
[a8] Wikipedia: AlphaGo versus Lee Sedol — https://en.wikipedia.org/wiki/AlphaGo_versus_Lee_Sedol (accessed 2026-09-06); Silver et al., Nature 2016 — https://www.nature.com/articles/nature16961; AlphaZero — arXiv 1712.01815 — https://arxiv.org/abs/1712.01815
[a9] Christiano et al., "Deep Reinforcement Learning from Human Preferences" — arXiv 1706.03741 — https://arxiv.org/abs/1706.03741; Schulman et al., "Proximal Policy Optimization Algorithms" — arXiv 1707.06347 — https://arxiv.org/abs/1707.06347 (accessed 2026-09-06)
[a10] Ouyang et al., InstructGPT — arXiv 2203.02155 — https://arxiv.org/abs/2203.02155; Wikipedia: OpenAI o1 — https://en.wikipedia.org/wiki/OpenAI_o1; DeepSeek-R1 — arXiv 2501.12948 — https://arxiv.org/abs/2501.12948; Wikipedia: Richard S. Sutton (2024 Turing Award) — https://en.wikipedia.org/wiki/Richard_S._Sutton (accessed 2026-09-06)

**Thread (b) — Robotics / embodied AI**
[b1] Wikipedia: Unimate — https://en.wikipedia.org/wiki/Unimate (accessed 2026-09-06)
[b2] Wikipedia: Shakey the robot — https://en.wikipedia.org/wiki/Shakey_the_robot (accessed 2026-09-06); SRI: Shakey the Robot — https://www.sri.com/hoi/shakey-the-robot/
[b3] Wikipedia: Hans Moravec (Stanford Cart) — https://en.wikipedia.org/wiki/Hans_Moravec (accessed 2026-09-06)
[b4] Wikipedia: Subsumption architecture (Brooks, 1986) — https://en.wikipedia.org/wiki/Subsumption_architecture (accessed 2026-09-06); Brooks, "A Robust Layered Control System for a Mobile Robot", MIT AI Memo 864 — https://people.csail.mit.edu/brooks/papers/AIM-864.pdf
[b5] Wikipedia: Boston Dynamics — https://en.wikipedia.org/wiki/Boston_Dynamics (accessed 2026-09-06); Wikipedia: BigDog — https://en.wikipedia.org/wiki/BigDog; Wikipedia: Atlas (robot) — https://en.wikipedia.org/wiki/Atlas_%28robot%29
[b6] Wikipedia: DARPA Grand Challenge — https://en.wikipedia.org/wiki/DARPA_Grand_Challenge (accessed 2026-09-06); Wikipedia: Stanley (vehicle) — https://en.wikipedia.org/wiki/Stanley_%28vehicle%29
[b7] Wikipedia: DARPA Robotics Challenge — https://en.wikipedia.org/wiki/DARPA_Robotics_Challenge (accessed 2026-09-06)
[b8] RT-1: Robotics Transformer — arXiv 2212.06817 — https://arxiv.org/abs/2212.06817; RT-2 — arXiv 2307.15818 — https://arxiv.org/abs/2307.15818; Wikipedia: Vision–language–action model — https://en.wikipedia.org/wiki/Vision%E2%80%93language%E2%80%93action_model (accessed 2026-09-06)
[b9] π0: A Vision-Language-Action Flow Model — arXiv 2410.24164 — https://arxiv.org/abs/2410.24164; OpenVLA — arXiv 2406.09246 — https://arxiv.org/abs/2406.09246; Wikipedia: Gemini Robotics — https://en.wikipedia.org/wiki/Gemini_Robotics; Wikipedia: Figure AI — https://en.wikipedia.org/wiki/Figure_AI (accessed 2026-09-06)

**Thread (c) — AI safety, alignment and ethics**
[c1] Wikipedia: Three Laws of Robotics (Asimov, "Runaround", 1942) — https://en.wikipedia.org/wiki/Three_Laws_of_Robotics (accessed 2026-09-06)
[c2] Wikipedia: AI alignment (quotes Wiener 1960) — https://en.wikipedia.org/wiki/AI_alignment (accessed 2026-09-06); Wikipedia: Norbert Wiener — https://en.wikipedia.org/wiki/Norbert_Wiener
[c3] Wikipedia: Computer Power and Human Reason — https://en.wikipedia.org/wiki/Computer_Power_and_Human_Reason (accessed 2026-09-06)
[c4] Wikipedia: Superintelligence: Paths, Dangers, Strategies — https://en.wikipedia.org/wiki/Superintelligence:_Paths,_Dangers,_Strategies (accessed 2026-09-06); Wikipedia: Open letter on artificial intelligence (2015) — https://en.wikipedia.org/wiki/Open_letter_on_artificial_intelligence_%282015%29
[c5] Amodei et al., "Concrete Problems in AI Safety" — arXiv 1606.06565 — https://arxiv.org/abs/1606.06565; ProPublica, "Machine Bias" (2016) — https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing; Wikipedia: Partnership on AI — https://en.wikipedia.org/wiki/Partnership_on_AI (accessed 2026-09-06)
[c6] Wikipedia: Asilomar Conference on Beneficial AI — https://en.wikipedia.org/wiki/Asilomar_Conference_on_Beneficial_AI (accessed 2026-09-06); FLI, Asilomar AI Principles — https://futureoflife.org/open-letter/ai-principles/
[c7] Wikipedia: Joy Buolamwini (Gender Shades, 2018) — https://en.wikipedia.org/wiki/Joy_Buolamwini; Mitchell et al., "Model Cards for Model Reporting" — arXiv 1810.03993 — https://arxiv.org/abs/1810.03993; Wikipedia: Stochastic parrot — https://en.wikipedia.org/wiki/Stochastic_parrot (accessed 2026-09-06)
[c8] FLI, Pause Giant AI Experiments — https://futureoflife.org/open-letter/pause-giant-ai-experiments/; CAIS Statement on AI Risk — https://www.safe.ai/work/statement-on-ai-risk; Bletchley Declaration — https://www.gov.uk/government/publications/ai-safety-summit-2023-the-bletchley-declaration/the-bletchley-declaration-by-countries-attending-the-ai-safety-summit-1-2-november-2023; Wikipedia: Executive Order 14110 — https://en.wikipedia.org/wiki/Executive_Order_14110; Wikipedia: Geoffrey Hinton — https://en.wikipedia.org/wiki/Geoffrey_Hinton (accessed 2026-09-06)
[c9] Wikipedia: Artificial Intelligence Act — https://en.wikipedia.org/wiki/Artificial_Intelligence_Act (accessed 2026-09-06); Regulation (EU) 2024/1689 — https://eur-lex.europa.eu/eli/reg/2024/1689/oj
[c10] Constitutional AI — arXiv 2212.08073 — https://arxiv.org/abs/2212.08073; DPO — arXiv 2305.18290 — https://arxiv.org/abs/2305.18290; Wikipedia: Mechanistic interpretability — https://en.wikipedia.org/wiki/Mechanistic_interpretability (accessed 2026-09-06)

**Thread (d) — Hardware and compute**
[d1] Wikipedia: Lisp machine — https://en.wikipedia.org/wiki/Lisp_machine (accessed 2026-09-06); Wikipedia: History of artificial intelligence (1987 Lisp-machine collapse) — https://en.wikipedia.org/wiki/History_of_artificial_intelligence
[d2] Wikipedia: Connection Machine — https://en.wikipedia.org/wiki/Connection_Machine (accessed 2026-09-06)
[d3] Wikipedia: GeForce 256 — https://en.wikipedia.org/wiki/GeForce_256 (accessed 2026-09-06)
[d4] Wikipedia: CUDA — https://en.wikipedia.org/wiki/CUDA (accessed 2026-09-06); Nvidia, About CUDA — https://developer.nvidia.com/about-cuda
[d5] Wikipedia: AlexNet — https://en.wikipedia.org/wiki/AlexNet (accessed 2026-09-06)
[d6] Wikipedia: Tensor Processing Unit — https://en.wikipedia.org/wiki/Tensor_Processing_Unit (accessed 2026-09-06); Google Cloud blog, "Google supercharges machine learning tasks with TPU custom chip" (May 2016) — https://cloud.google.com/blog/products/ai-machine-learning/google-supercharges-machine-learning-tasks-with-custom-chip; Wikipedia: Nvidia DGX — https://en.wikipedia.org/wiki/Nvidia_DGX
[d7] Kaplan et al., Scaling Laws for Neural Language Models — arXiv 2001.08361 — https://arxiv.org/abs/2001.08361 (accessed 2026-09-06)
[d8] Wikipedia: Hopper (microarchitecture) — https://en.wikipedia.org/wiki/Hopper_%28microarchitecture%29 (accessed 2026-09-06); Nvidia Newsroom, Hopper announcement (GTC 2022) — https://nvidianews.nvidia.com/news/nvidia-announces-hopper-architecture-the-next-generation-of-accelerated-computing; Nvidia H100 product page — https://www.nvidia.com/en-us/data-center/h100/
[d9] Wikipedia: Blackwell (microarchitecture) — https://en.wikipedia.org/wiki/Blackwell_%28microarchitecture%29; Nvidia Newsroom, Blackwell (18 Mar 2024) — https://nvidianews.nvidia.com/news/nvidia-blackwell-platform-arrives-to-power-a-new-era-of-computing; Wikipedia: Nvidia (market capitalisation) — https://en.wikipedia.org/wiki/Nvidia (accessed 2026-09-06)

**Thread (e) — Open vs closed**
[e1] Wikipedia: Weka (software) — https://en.wikipedia.org/wiki/Weka_%28software%29; Wikipedia: Torch (machine learning) — https://en.wikipedia.org/wiki/Torch_%28machine_learning%29; Wikipedia: Theano (software) — https://en.wikipedia.org/wiki/Theano_%28software%29; Wikipedia: Caffe (software) — https://en.wikipedia.org/wiki/Caffe_%28software%29 (accessed 2026-09-06)
[e2] Wikipedia: TensorFlow — https://en.wikipedia.org/wiki/TensorFlow; Wikipedia: PyTorch — https://en.wikipedia.org/wiki/PyTorch (accessed 2026-09-06)
[e3] Wikipedia: GPT-2 (staged release 2019) — https://en.wikipedia.org/wiki/GPT-2; Hugging Face Transformers — https://github.com/huggingface/transformers (accessed 2026-09-06)
[e4] Wikipedia: EleutherAI — https://en.wikipedia.org/wiki/EleutherAI; Hugging Face, BLOOM — https://huggingface.co/blog/bloom; Stability AI, Stable Diffusion Public Release (22 Aug 2022) — https://stability.ai/news/stable-diffusion-public-release (accessed 2026-09-06)
[e5] Wikipedia: Llama (language model) (leak 3 Mar 2023) — https://en.wikipedia.org/wiki/Llama_%28language_model%29; Stanford Alpaca — https://crfm.stanford.edu/2023/03/13/alpaca.html; LMSYS Vicuna — https://lmsys.org/blog/2023-03-30-vicuna/; llama.cpp — https://github.com/ggml-org/llama.cpp (accessed 2026-09-06)
[e6] Llama 2 — arXiv 2307.09288 — https://arxiv.org/abs/2307.09288 (accessed 2026-09-06)
[e7] Mistral AI, Mistral 7B (27 Sep 2023) — https://mistral.ai/news/announcing-mistral-7b; Mixtral of experts (11 Dec 2023) — https://mistral.ai/news/mixtral-of-experts; Wikipedia: Mistral AI — https://en.wikipedia.org/wiki/Mistral_AI (accessed 2026-09-06)
[e8] The Llama 3 Herd of Models — arXiv 2407.21783 — https://arxiv.org/abs/2407.21783; OSI, The Open Source AI Definition — https://opensource.org/ai/open-source-ai-definition; Wikipedia: Open-source artificial intelligence — https://en.wikipedia.org/wiki/Open-source_artificial_intelligence (accessed 2026-09-06)
[e9] DeepSeek-V3 — arXiv 2412.19437 — https://arxiv.org/abs/2412.19437; DeepSeek-R1 — arXiv 2501.12948 — https://arxiv.org/abs/2501.12948; Wikipedia: DeepSeek — https://en.wikipedia.org/wiki/DeepSeek; Wikipedia: Qwen — https://en.wikipedia.org/wiki/Qwen (accessed 2026-09-06)
[e10] Wikipedia: Products and applications of OpenAI (GPT-OSS, 5 Aug 2025) — https://en.wikipedia.org/wiki/Products_and_applications_of_OpenAI (accessed 2026-09-06)

**Thread (f) — NLP lineage**
[f1] Wikipedia: Georgetown–IBM experiment — https://en.wikipedia.org/wiki/Georgetown%E2%80%93IBM_experiment; Wikipedia: ALPAC — https://en.wikipedia.org/wiki/ALPAC (accessed 2026-09-06)
[f2] Wikipedia: ELIZA — https://en.wikipedia.org/wiki/ELIZA (accessed 2026-09-06)
[f3] Wikipedia: SHRDLU — https://en.wikipedia.org/wiki/SHRDLU (accessed 2026-09-06)
[f4] Wikipedia: History of natural language processing — https://en.wikipedia.org/wiki/History_of_natural_language_processing; Wikipedia: IBM alignment models — https://en.wikipedia.org/wiki/IBM_alignment_models (accessed 2026-09-06)
[f5] Wikipedia: Long short-term memory — https://en.wikipedia.org/wiki/Long_short-term_memory (accessed 2026-09-06)
[f6] Wikipedia: Word2vec — https://en.wikipedia.org/wiki/Word2vec; Mikolov et al. — arXiv 1301.3781 — https://arxiv.org/abs/1301.3781 (accessed 2026-09-06)
[f7] Sutskever et al., seq2seq — arXiv 1409.3215 — https://arxiv.org/abs/1409.3215; Bahdanau et al. — arXiv 1409.0473 — https://arxiv.org/abs/1409.0473; Wikipedia: Google Neural Machine Translation — https://en.wikipedia.org/wiki/Google_Neural_Machine_Translation (accessed 2026-09-06)
[f8] Attention Is All You Need — arXiv 1706.03762 — https://arxiv.org/abs/1706.03762; ELMo — arXiv 1802.05365 — https://arxiv.org/abs/1802.05365; BERT — arXiv 1810.04805 — https://arxiv.org/abs/1810.04805; Wikipedia: GPT-1 — https://en.wikipedia.org/wiki/GPT-1 (accessed 2026-09-06)
[f9] GPT-3 — arXiv 2005.14165 — https://arxiv.org/abs/2005.14165; Wikipedia: ChatGPT — https://en.wikipedia.org/wiki/ChatGPT (accessed 2026-09-06)

**Thread (g) — Computer vision lineage**
[g1] Wikipedia: David H. Hubel — https://en.wikipedia.org/wiki/David_H._Hubel (accessed 2026-09-06)
[g2] Wikipedia: Larry Roberts (computer scientist) — https://en.wikipedia.org/wiki/Lawrence_Roberts_%28scientist%29; Wikipedia: Computer vision (1966 Summer Vision Project) — https://en.wikipedia.org/wiki/Computer_vision (accessed 2026-09-06)
[g3] Wikipedia: Neocognitron — https://en.wikipedia.org/wiki/Neocognitron (accessed 2026-09-06)
[g4] Wikipedia: LeNet — https://en.wikipedia.org/wiki/LeNet (accessed 2026-09-06)
[g5] Wikipedia: Scale-invariant feature transform — https://en.wikipedia.org/wiki/Scale-invariant_feature_transform; Wikipedia: Viola–Jones object detection framework — https://en.wikipedia.org/wiki/Viola%E2%80%93Jones_object_detection_framework (accessed 2026-09-06)
[g6] Wikipedia: ImageNet — https://en.wikipedia.org/wiki/ImageNet; Wikipedia: AlexNet — https://en.wikipedia.org/wiki/AlexNet (accessed 2026-09-06)
[g7] Goodfellow et al., GANs — arXiv 1406.2661 — https://arxiv.org/abs/1406.2661; He et al., ResNet — arXiv 1512.03385 — https://arxiv.org/abs/1512.03385; Ren et al., Faster R-CNN — arXiv 1506.01497 — https://arxiv.org/abs/1506.01497; Redmon et al., YOLO — arXiv 1506.02640 — https://arxiv.org/abs/1506.02640 (accessed 2026-09-06)
[g8] ViT — arXiv 2010.11929 — https://arxiv.org/abs/2010.11929; CLIP — arXiv 2103.00020 — https://arxiv.org/abs/2103.00020; Wikipedia: DALL-E — https://en.wikipedia.org/wiki/DALL-E (accessed 2026-09-06)
[g9] Latent diffusion — arXiv 2112.10752 — https://arxiv.org/abs/2112.10752; Segment Anything — arXiv 2304.02643 — https://arxiv.org/abs/2304.02643; Wikipedia: Midjourney — https://en.wikipedia.org/wiki/Midjourney; Wikipedia: Sora (text-to-video model) — https://en.wikipedia.org/wiki/Sora_%28text-to-video_model%29 (accessed 2026-09-06)
[g10] RT-2 — arXiv 2307.15818 — https://arxiv.org/abs/2307.15818; Wikipedia: Gemini Robotics — https://en.wikipedia.org/wiki/Gemini_Robotics (accessed 2026-09-06)

**Thread (h) — Game-playing milestones**
[h1] Wikipedia: Arthur Samuel (computer scientist) — https://en.wikipedia.org/wiki/Arthur_Samuel_%28computer_scientist%29 (accessed 2026-09-06)
[h2] Wikipedia: Chinook (computer program) — https://en.wikipedia.org/wiki/Chinook_%28computer_program%29 (accessed 2026-09-06)
[h3] Wikipedia: Deep Blue (chess computer) — https://en.wikipedia.org/wiki/Deep_Blue_%28chess_computer%29; IBM, Deep Blue — https://www.ibm.com/history/deep-blue (accessed 2026-09-06)
[h4] Wikipedia: IBM Watson — https://en.wikipedia.org/wiki/IBM_Watson; IBM, Watson on Jeopardy! — https://www.ibm.com/history/watson-jeopardy (accessed 2026-09-06)
[h5] Wikipedia: AlphaGo — https://en.wikipedia.org/wiki/AlphaGo; Silver et al., Nature 2016 — https://www.nature.com/articles/nature16961; Wikipedia: AlphaGo versus Lee Sedol — https://en.wikipedia.org/wiki/AlphaGo_versus_Lee_Sedol (accessed 2026-09-06)
[h6] Silver et al., "Mastering the game of Go without human knowledge", Nature 2017 — https://www.nature.com/articles/nature24270; AlphaZero — arXiv 1712.01815 — https://arxiv.org/abs/1712.01815; Wikipedia: Libratus — https://en.wikipedia.org/wiki/Libratus (accessed 2026-09-06)
[h7] Wikipedia: OpenAI Five — https://en.wikipedia.org/wiki/OpenAI_Five; Berner et al., "Dota 2 with Large Scale Deep RL" — arXiv 1912.06680 — https://arxiv.org/abs/1912.06680 (accessed 2026-09-06)
[h8] Vinyals et al., "Grandmaster level in StarCraft II", Nature 2019 — https://www.nature.com/articles/s41586-019-1724-z; Wikipedia: AlphaStar (software) — https://en.wikipedia.org/wiki/AlphaStar_%28software%29; Wikipedia: Pluribus (poker bot) — https://en.wikipedia.org/wiki/Pluribus_%28poker_bot%29; Brown & Sandholm, "Superhuman AI for multiplayer poker", Science 2019 (PDF) — https://www.cs.cmu.edu/~noamb/papers/19-Science-Superhuman.pdf (accessed 2026-09-06)
[h9] Schrittwieser et al., MuZero, Nature 2020 — https://www.nature.com/articles/s41586-020-03051-4; arXiv 1911.08265 — https://arxiv.org/abs/1911.08265; Wikipedia: MuZero — https://en.wikipedia.org/wiki/MuZero (accessed 2026-09-06)
[h10] Trinh et al., "Solving olympiad geometry without human demonstrations", Nature 2024 — https://www.nature.com/articles/s41586-023-06747-5; Wikipedia: AlphaGeometry — https://en.wikipedia.org/wiki/AlphaGeometry (accessed 2026-09-06)
