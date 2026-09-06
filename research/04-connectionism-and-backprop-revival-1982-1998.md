# Connectionism and the Backpropagation Revival (1982–1998)

> **Status:** reviewed
> **Date range:** 1982–1998
> **Map placement (proposed):** X = 1982–1998; Y = connectionist pole (with a cognitive-science / neuroscience shoreline to the north and a small statistical-learning inlet to the south)
> **Altitude:** A1 continent ("Connectionist Revival"), A2 countries (PDP / Hopfield–Boltzmann energy models / ConvNets at Bell Labs / Recurrent nets & LSTM / RL-with-nets), A3 cities (individual labs: UCSD PDP group, CMU, Toronto, Bell Labs Holmdel, TU Munich–IDSIA, Caltech), A4 streets (papers, people)

## One-paragraph summary
After the first AI winter for neural nets (Minsky & Papert's *Perceptrons*, 1969, is usually blamed) the "second wave" of connectionism began in the early 1980s: John Hopfield's 1982 energy-based associative memory made neural networks respectable to physicists, Hinton and Sejnowski's Boltzmann machine (1985) gave them a learning rule grounded in statistical mechanics, and the 1986 Rumelhart–Hinton–Williams *Nature* paper (plus the two-volume *Parallel Distributed Processing* books) popularised backpropagation for training multi-layer networks — even though the algorithm itself had been published as reverse-mode automatic differentiation by Linnainmaa in 1970 and applied to neural nets by Werbos in 1982. [1][7][8][14] The decade that followed produced most of the architectural vocabulary of modern deep learning: Fukushima's Neocognitron (1980) inspired LeCun's convolutional networks at Bell Labs (1989 zip codes → LeNet-5 and MNIST, 1998); Jordan and Elman networks re-opened recurrent nets; Hochreiter diagnosed the vanishing-gradient problem (1991) and, with Schmidhuber, answered it with LSTM (1997); Cybenko and Hornik proved universal approximation (1989); Barto and Sutton's actor–critic (1983) and TD(λ) (1988) re-founded reinforcement learning with neuron-like elements and Tesauro's TD-Gammon (1992) fused it with backprop nets; Grossberg's ART and INNS (1987), NIPS (1987) and the journals *Neural Networks* (1988) and *Neural Computation* (1989) gave the community institutions; and by the mid-1990s Bayesian neural nets (MacKay, Neal), mixtures of experts and the Helmholtz machine were already pointing toward the statistical era. [5][18][22][24][26][29][31][60][70][73][81] On the map this era is the connectionist pole's first true "continent": small, fiercely argued with symbolic AI (Fodor & Pylyshyn, Pinker & Prince, 1988), and destined to be partly submerged by the statistical-learning tide of the 1990s before re-emerging as deep learning after 2006. [38][39][49]

## Timeline of key events
| Year | Event | Why it matters | Source |
|------|-------|----------------|--------|
| 1970 | Seppo Linnainmaa's master's thesis publishes reverse-mode automatic differentiation (the modern form of backpropagation); journal version in *BIT*, 1976 | The mathematical core of backprop predates its neural-net fame by 16 years | [7][9][10] |
| 1980 | Kunihiko Fukushima publishes the Neocognitron (*Biological Cybernetics*, April 1980), a hierarchical shift-invariant network for handwritten-character recognition | Direct ancestor of convolutional neural networks | [5][6][45] |
| 1982 | John Hopfield, "Neural networks and physical systems with emergent collective computational abilities" (*PNAS*) | Content-addressable memory as energy minimisation; imports statistical mechanics into neural nets and re-legitimises the field (the same Hebbian–Ising associative memory had been published by Nakano 1971, Amari 1972 and Little 1974 — hence "Amari–Hopfield network") | [2][3][91] |
| 1982 | Paul Werbos applies backpropagation to multilayer perceptrons "in the way that has become standard" | Backprop meets neural nets (Werbos's 1974 thesis is the often-cited precursor; David Parker 1985 and LeCun's 1987 Paris thesis are further independent derivations) | [7][11][42] |
| 1982 | Teuvo Kohonen, "Self-organized formation of topologically correct feature maps"; Erkki Oja's 1982 rule shows a normalised Hebbian neuron extracts principal components | Self-organising maps and Hebbian PCA: the era's main unsupervised competitive-learning models, both from Helsinki | [36][37][53][90] |
| 1983 | Barto, Sutton & Anderson, "Neuronlike adaptive elements that can solve difficult learning control problems" (*IEEE Trans. SMC* 13): the actor–critic architecture balances a cart-pole; Sutton's TD(λ) paper follows in *Machine Learning* 3 (1988) | Reinforcement learning is re-founded with neuron-like elements at UMass Amherst — the RL thread that TD-Gammon and later DQN run on | [60][61][62][63][64] |
| 1984 | Hopfield extends his model to neurons with graded (continuous) response (*PNAS*) | Continuous Hopfield nets; the standard model for statistical-mechanics studies of neural networks | [2][4] |
| 1985 | Ackley, Hinton & Sejnowski, "A Learning Algorithm for Boltzmann Machines" (*Cognitive Science* 9); Smolensky's "Harmonium" (PDP vol. 1, 1986) is the first restricted Boltzmann machine | Stochastic energy-based networks with hidden units; the restricted variant (RBM) later seeds deep belief nets | [12][13][79] |
| 1986 | Rumelhart, Hinton & Williams, "Learning representations by back-propagating errors" (*Nature* 323) | The paper that made backprop the standard training method for multi-layer nets | [7][8] |
| 1986 | *Parallel Distributed Processing*, vols. 1–2 (Rumelhart, McClelland & the PDP Research Group, MIT Press) | The manifesto of connectionism; hidden layers, distributed representations, cognitive modelling | [14][15] |
| 1986 | Michael I. Jordan proposes the Jordan recurrent network; Jeffrey Elman's simple recurrent network follows in 1990 ("Finding Structure in Time") | Recurrent nets for sequence/language modelling re-enter the field | [32][33][58] |
| 1986 | *Machine Learning* journal begins publication | Institutional home for the (largely symbolic) ML community that connectionists would later share | [51] |
| 1987 | First NIPS conference held in Denver (president Ed Posner; program chair Yaser Abu-Mostafa); MIT Press launches *Neural Computation* (1989, editor Terry Sejnowski) | The connectionist community gets its own annual meeting (Denver 1987–2000) and its flagship journal | [31][84] |
| 1987–89 | Institutional boom: Stephen Grossberg founds the International Neural Network Society (1987) and its journal *Neural Networks* (1988); first IEEE ICNN (1987) merges with the INNS meeting into IJCNN (1989); the DARPA Neural Network Study (1987–88) revives US government funding; HNC Software (Hecht-Nielsen, 1986) leads a wave of neural-net start-ups | Neural nets acquire societies, journals, federal money and an industry — the infrastructure of a field, not a fad | [81][83][92] |
| 1987 | Carpenter & Grossberg publish ART 1 (Adaptive Resonance Theory), a self-organising network that addresses the stability–plasticity dilemma | The Boston University school's alternative to backprop; the main non-PDP unsupervised architecture besides SOMs | [81][82] |
| 1987 | Sejnowski & Rosenberg's NETtalk learns to pronounce English text with backprop; appears on the *Today* show | First widely publicised backprop demo | [16][17] |
| 1987–89 | Alex Waibel et al. introduce Time-Delay Neural Networks for phoneme recognition | 1-D convolution with weight sharing along time — an early ConvNet | [34][35][57] |
| 1988 | Fodor & Pylyshyn, "Connectionism and cognitive architecture"; Pinker & Prince, "On language and connectionism" (*Cognition* 28); Minsky & Papert reissue *Perceptrons* with a new prologue and epilogue answering the revival | The great symbolic-vs-connectionist debate; the river between this continent and classical AI | [38][39][85] |
| 1988–90 | Connectionist replies on compositionality: Smolensky, "On the proper treatment of connectionism" (*BBS* 11, 1988) and tensor-product variable binding (*Artificial Intelligence* 46, 1990); Pollack's RAAM, "Recursive distributed representations" (same issue) | Shows structured symbols can be encoded in vector spaces — the ancestor of today's "neuro-symbolic" question | [77][78][79][80] |
| 1988 | Broomhead & Lowe (RSRE, Malvern), "Multivariable functional interpolation and adaptive networks" (*Complex Systems* 2): radial-basis-function networks | Learning as interpolation; RBF nets become the 1990s bridge from neural nets to kernel methods | [89] |
| 1989 | LeCun et al., "Backpropagation Applied to Handwritten Zip Code Recognition" (*Neural Computation* 1) at AT&T Bell Labs | First practical backprop-trained ConvNet on real US Postal Service data — prototype of LeNet | [18][19][42] |
| 1989 | Cybenko proves universal approximation for sigmoidal networks; Hornik, Stinchcombe & White generalise it | Theoretical guarantee that one hidden layer suffices (in principle) | [26][27][28] |
| 1989–92 | Carver Mead (Caltech), *Analog VLSI and Neural Systems* (1989) and "Neuromorphic electronic systems" (*Proc. IEEE* 78, 1990); Misha Mahowald's silicon retina (PhD 1992) | Neuromorphic engineering is born: neural nets as analog hardware, the compute strand of this era | [86][87][88] |
| 1991 | Jacobs, Jordan, Nowlan & Hinton, "Adaptive Mixtures of Local Experts" (*Neural Computation* 3) | Gated expert networks — the mixture-of-experts idea that returns in 2017–2024 sparse LLMs | [67][68] |
| 1991 | Sepp Hochreiter's diploma thesis (TU Munich, advisor Schmidhuber) identifies the vanishing-gradient problem | Explains why deep/recurrent nets trained by backprop failed; motivates LSTM | [24][46] |
| 1992 | Gerald Tesauro's TD-Gammon (IBM) reaches near-expert backgammon with a neural net trained by TD(λ) self-play | Neural nets + reinforcement learning; ancestor of AlphaGo-style self-play | [29][30][52] |
| 1992 | Ronald Williams, "Simple statistical gradient-following algorithms for connectionist reinforcement learning" (*Machine Learning* 8): REINFORCE | The first policy-gradient method; the estimator behind modern policy optimisation | [65][66] |
| 1992–96 | Bayesian neural networks: MacKay's evidence framework, "A Practical Bayesian Framework for Backpropagation Networks" (*Neural Computation* 4, 1992; Caltech PhD under Hopfield); Neal, *Bayesian Learning for Neural Networks* (1996, Toronto PhD under Hinton; priors for infinite-width networks); Bishop's textbook *Neural Networks for Pattern Recognition* (1995) | Puts neural nets on a statistical footing and builds the bridge to the era-05 Bayesian/kernel mainland | [73][74][75][76] |
| 1994 | Bengio, Simard & Frasconi, "Learning long-term dependencies with gradient descent is difficult" | Formalises the vanishing/exploding-gradient obstacle for RNNs | [24][25] |
| 1995 | Hinton, Dayan, Frey & Neal, "The wake-sleep algorithm for unsupervised neural networks" (*Science* 268); Dayan, Hinton, Neal & Zemel, "The Helmholtz machine" (*Neural Computation* 7) | Recognition + generative networks trained together — the direct ancestor of variational autoencoders | [70][71][72] |
| 1997 | Hochreiter & Schmidhuber, "Long Short-Term Memory" (*Neural Computation* 9(8)); Schuster & Paliwal introduce bidirectional RNNs the same year | The recurrent architecture that would dominate speech and NLP until the Transformer | [22][23][40] |
| 1998 | LeCun, Bottou, Bengio & Haffner, "Gradient-based learning applied to document recognition" (*Proc. IEEE*): LeNet-5 and the MNIST benchmark | Canonical ConvNet; MNIST becomes the field's drosophila; cheque-reading systems deployed commercially | [18][20][21] |
| 1999 | Gers, Schmidhuber & Cummins add the forget gate to LSTM | The LSTM variant actually used in the 2010s (border event into the next era) | [22] |
| 2024 | Hopfield and Hinton awarded the Nobel Prize in Physics "for foundational discoveries and inventions that enable machine learning with artificial neural networks" | Retrospective recognition of this era's founding work | [41][48] |

## Key people
- **John Hopfield** (Caltech) — 1982/1984 energy-based associative memory networks; 2024 Nobel laureate in Physics. [2][3][48]
- **Geoffrey Hinton** (UCSD → CMU → Toronto from 1987) — Boltzmann machine (1985), backprop popularisation (1986), later deep belief nets; 2018 Turing Award, 2024 Nobel Prize. [8][13][41][59]
- **David Rumelhart** (UCSD → Stanford) — co-leader of the PDP Research Group; first author of the 1986 *Nature* backprop paper. [8][14][44]
- **James L. McClelland** (CMU) — co-editor of the PDP volumes; connectionist models of cognition. [14][54]
- **Ronald J. Williams** (UCSD → Northeastern) — third author of the 1986 backprop paper; REINFORCE policy-gradient algorithm (1992) and real-time recurrent learning. [8][55][65][66]
- **Terry Sejnowski** (Johns Hopkins → Salk Institute) — Boltzmann machine co-inventor; NETtalk (1987); long-time president of the NIPS Foundation. [13][17][43]
- **Yann LeCun** (AT&T Bell Labs, Holmdel) — backprop ConvNets for handwritten digits (1989), LeNet-5 and MNIST (1998); 2018 Turing Award. [18][19][20][42]
- **Kunihiko Fukushima** (NHK Labs, Tokyo) — Neocognitron (1980), the first deep convolutional architecture. [5][6][45]
- **Sepp Hochreiter** (TU Munich) — vanishing-gradient analysis (1991) and LSTM (1997). [23][24][46]
- **Jürgen Schmidhuber** (TU Munich / IDSIA) — LSTM co-author; 1991 neural history compressor (pre-training stacked RNNs). [23][47][49]
- **Jeffrey Elman** (UCSD) — simple recurrent ("Elman") network, "Finding Structure in Time" (1990). [32][33][58]
- **Teuvo Kohonen** (Helsinki University of Technology) — self-organising maps (1982). [36][37][53]
- **Gerald Tesauro** (IBM T.J. Watson) — TD-Gammon (1992–95). [29][30][52]
- **Andrew Barto & Richard Sutton** (UMass Amherst; Sutton at GTE Labs 1985–94) — actor–critic cart-pole (1983), TD(λ) (1988), *Reinforcement Learning: An Introduction* (1998); 2024 Turing Award. [60][61][62][63][64]
- **Michael I. Jordan** (UCSD PhD 1985 → MIT 1988–98) — Jordan recurrent nets; mixtures of experts with Jacobs, Nowlan & Hinton (1991); later the bridge to graphical models (era 05). [32][67][68][69]
- **Paul Smolensky** (Colorado → Johns Hopkins) — Harmony theory / Harmonium (the first RBM, 1986); "On the proper treatment of connectionism" (1988); tensor-product representations (1990). [77][78][79]
- **Stephen Grossberg & Gail Carpenter** (Boston University) — Adaptive Resonance Theory (ART 1, 1987); Grossberg founded INNS (1987) and *Neural Networks* (1988) and triggered the DARPA Neural Network Study. [81][82][83]
- **Peter Dayan** (Edinburgh PhD → Toronto postdoc → MIT) — Helmholtz machine and wake-sleep with Hinton, Neal, Frey & Zemel (1995); Q-learning convergence proof with Watkins (1992). [70][71][72]
- **David J. C. MacKay** (Caltech PhD 1992 under Hopfield → Cambridge) & **Radford Neal** (Toronto PhD 1995 under Hinton) — Bayesian neural networks: the evidence framework (1992) and *Bayesian Learning for Neural Networks* (1996). [73][74][75]
- **Carver Mead** (Caltech) — analog-VLSI neural systems and the term "neuromorphic" (1989–90); with Hopfield and Feynman taught the Caltech "Physics of Computation" course; advised Misha Mahowald's silicon retina. [86][87][88]
- **Shun'ichi Amari** (Univ. of Tokyo → RIKEN) — Amari–Hopfield associative memory (1972) and SGD-trained multilayer nets (1967): the Japanese precursor line running from era 02 into this one. [91]
- **George Cybenko** (Univ. of Illinois → Dartmouth) — 1989 universal approximation theorem for sigmoidal nets. [26][27][56]
- **Paul Werbos** (Harvard PhD 1974) & **Seppo Linnainmaa** (Univ. of Helsinki) — the two independent pre-1986 sources of backpropagation. [9][10][11]

## Key papers / artifacts
- Linnainmaa, S. *Taylor expansion of the accumulated rounding error*. BIT Numerical Mathematics 16, 1976 (journal form of the 1970 thesis). https://doi.org/10.1007/BF01931367 [9]
- Fukushima, K. *Neocognitron: A self-organizing neural network model for a mechanism of pattern recognition unaffected by shift in position*. Biological Cybernetics 36, 1980. https://doi.org/10.1007/BF00344251 [6]
- Hopfield, J. J. *Neural networks and physical systems with emergent collective computational abilities*. PNAS 79(8), 1982. https://europepmc.org/article/MED/6953413 [3]
- Kohonen, T. *Self-organized formation of topologically correct feature maps*. Biological Cybernetics 43, 1982. https://doi.org/10.1007/BF00337288 [37]
- Barto, A. G., Sutton, R. S. & Anderson, C. W. *Neuronlike adaptive elements that can solve difficult learning control problems*. IEEE Trans. Systems, Man, and Cybernetics SMC-13, 1983. https://doi.org/10.1109/TSMC.1983.6313077 [60]
- Ackley, D. H., Hinton, G. E. & Sejnowski, T. J. *A Learning Algorithm for Boltzmann Machines*. Cognitive Science 9, 1985. https://www.cs.toronto.edu/~hinton/absps/cogscibm.pdf [13]
- Rumelhart, D. E., Hinton, G. E. & Williams, R. J. *Learning representations by back-propagating errors*. Nature 323, 1986. https://doi.org/10.1038/323533a0 [8]
- Rumelhart, D. E., McClelland, J. L. & the PDP Research Group. *Parallel Distributed Processing: Explorations in the Microstructure of Cognition*, vols. 1–2. MIT Press, 1986. https://stanford.edu/~jlmcc/papers/PDP/ [14][15]
- Sejnowski, T. J. & Rosenberg, C. R. *Parallel Networks that Learn to Pronounce English Text*. Complex Systems 1, 1987. https://www.complex-systems.com/abstracts/v01_i01_a10/ [17]
- Carpenter, G. A. & Grossberg, S. *A massively parallel architecture for a self-organizing neural pattern recognition machine*. Computer Vision, Graphics, and Image Processing 37, 1987. https://doi.org/10.1016/S0734-189X%2887%2980014-2 [82]
- Fodor, J. A. & Pylyshyn, Z. W. *Connectionism and cognitive architecture: A critical analysis*. Cognition 28, 1988. https://doi.org/10.1016/0010-0277%2888%2990031-5 [38]
- Smolensky, P. *On the proper treatment of connectionism*. Behavioral and Brain Sciences 11, 1988. https://doi.org/10.1017/S0140525X00052432 [78]
- Sutton, R. S. *Learning to predict by the methods of temporal differences*. Machine Learning 3, 1988. https://doi.org/10.1007/BF00115009 [62]
- Broomhead, D. S. & Lowe, D. *Multivariable functional interpolation and adaptive networks*. Complex Systems 2, 1988. https://www.complex-systems.com/abstracts/v02_i03_a05/ [89]
- LeCun, Y. et al. *Backpropagation Applied to Handwritten Zip Code Recognition*. Neural Computation 1(4), 1989. http://yann.lecun.com/exdb/publis/pdf/lecun-89e.pdf [19]
- Cybenko, G. *Approximation by superpositions of a sigmoidal function*. Mathematics of Control, Signals and Systems 2, 1989. https://doi.org/10.1007/BF02551274 [27]
- Hornik, K., Stinchcombe, M. & White, H. *Multilayer feedforward networks are universal approximators*. Neural Networks 2, 1989. https://doi.org/10.1016/0893-6080%2889%2990020-8 [28]
- Waibel, A. et al. *Phoneme recognition using time-delay neural networks*. IEEE Trans. ASSP 37, 1989. https://doi.org/10.1109/29.21701 [35]
- Elman, J. L. *Finding Structure in Time*. Cognitive Science 14, 1990. https://www.semanticscholar.org/paper/668087f0ae7ce1de6e0bd0965dbb480c08103260 [33]
- Mead, C. *Neuromorphic electronic systems*. Proceedings of the IEEE 78(10), 1990. https://doi.org/10.1109/5.58356 [87]
- Smolensky, P. *Tensor product variable binding and the representation of symbolic structures in connectionist systems*. Artificial Intelligence 46, 1990. https://doi.org/10.1016/0004-3702%2890%2990007-M [77]
- Pollack, J. B. *Recursive distributed representations*. Artificial Intelligence 46, 1990. https://doi.org/10.1016/0004-3702%2890%2990005-K [80]
- Jacobs, R. A., Jordan, M. I., Nowlan, S. J. & Hinton, G. E. *Adaptive Mixtures of Local Experts*. Neural Computation 3(1), 1991. https://www.cs.toronto.edu/~hinton/absps/jjnh91.pdf [67]
- Williams, R. J. *Simple statistical gradient-following algorithms for connectionist reinforcement learning*. Machine Learning 8, 1992. https://doi.org/10.1007/BF00992696 [65]
- MacKay, D. J. C. *A Practical Bayesian Framework for Backpropagation Networks*. Neural Computation 4(3), 1992. https://api.crossref.org/works/10.1162/neco.1992.4.3.448 [73]
- Bengio, Y., Simard, P. & Frasconi, P. *Learning long-term dependencies with gradient descent is difficult*. IEEE Trans. Neural Networks 5, 1994. https://doi.org/10.1109/72.279181 [25]
- Tesauro, G. *Temporal Difference Learning and TD-Gammon*. Communications of the ACM 38(3), 1995. https://www.bkgm.com/articles/tesauro/tdl.html [30]
- Hinton, G. E., Dayan, P., Frey, B. J. & Neal, R. M. *The wake-sleep algorithm for unsupervised neural networks*. Science 268, 1995. https://www.cs.toronto.edu/~hinton/absps/ws.pdf [70]
- Neal, R. M. *Bayesian Learning for Neural Networks*. Lecture Notes in Statistics 118, Springer, 1996. https://doi.org/10.1007/978-1-4612-0745-0 [74]
- Hochreiter, S. & Schmidhuber, J. *Long Short-Term Memory*. Neural Computation 9(8), 1997. https://www.bioinf.jku.at/publications/older/2604.pdf [23]
- Schuster, M. & Paliwal, K. K. *Bidirectional recurrent neural networks*. IEEE Trans. Signal Processing 45, 1997. https://doi.org/10.1109/78.650093 [40]
- LeCun, Y., Bottou, L., Bengio, Y. & Haffner, P. *Gradient-based learning applied to document recognition*. Proceedings of the IEEE 86(11), 1998. https://doi.org/10.1109/5.726791 [20]
- Sutton, R. S. & Barto, A. G. *Reinforcement Learning: An Introduction*. MIT Press, 1998 (authors' page for the first edition). http://incompleteideas.net/book/first/the-book.html [63]

## Schools of thought / sub-clusters
- **PDP / cognitive connectionism** (UCSD, CMU; Rumelhart, McClelland, Hinton, Elman; Smolensky and Pollack on the compositionality front) — neural nets as models of human cognition (past-tense learning, reading, memory), tensor-product and recursive distributed representations as the reply to Fodor–Pylyshyn; borders: cognitive science and psycholinguistics to the north; the symbolic-AI continent across the Fodor–Pylyshyn river to the west/south; deep learning (era 06) downstream to the east. [14][38][39][77][80]
- **Energy-based / statistical-mechanics models** (Caltech, CMU, Johns Hopkins, Toronto; Hopfield, Hinton, Sejnowski, Smolensky, Dayan, Neal) — Hopfield nets, Boltzmann machines and Harmonium/RBM, simulated annealing, Helmholtz machines and wake-sleep (1995); borders: physics/spin-glass theory to the north (Amari's 1972 model is the Japanese headwater); probabilistic graphical models (era 05) to the south-east, since RBMs are undirected graphical models; deep belief nets (2006) and VAEs (era 06) to the east. [2][12][13][70][79][91]
- **Adaptive Resonance / Boston University school** (Grossberg, Carpenter) — ART networks, the stability–plasticity dilemma, INNS and *Neural Networks*; the era's largest non-backprop community and its main institution-builder; borders: neuroscience and mathematical psychology to the north; Kohonen SOMs and Oja's rule (Helsinki) as the sibling unsupervised/competitive-learning province; PDP to the south, with which it competed for the label "neural networks". [81][82][83][90]
- **ConvNets and applied pattern recognition** (Bell Labs Holmdel, NHK; Fukushima, LeCun, Bottou, Denker, Jackel) — Neocognitron, TDNN, LeNet, MNIST, cheque reading; borders: computer vision and OCR to the north; SVMs/kernel methods (era 05) as the same-lab rival at Bell Labs (Vapnik joined the same department in 1990); AlexNet (era 06) directly east. [5][18][34]
- **Recurrent networks and sequence learning** (UCSD, TU Munich/IDSIA; Jordan, Elman, Hochreiter, Schmidhuber) — Jordan/Elman nets, vanishing gradients, LSTM, bidirectional RNNs; borders: HMM-based speech recognition (era 05) to the south, which it would displace only in the 2010s; seq2seq/NMT (era 06) to the east. [22][24][32]
- **Neural nets meet reinforcement learning** (UMass Amherst, GTE Labs, IBM Watson, Northeastern; Barto, Sutton, Tesauro, Williams) — actor–critic (1983), TD(λ) (1988), TD-Gammon, REINFORCE (1992), the Sutton–Barto textbook (1998); borders: control theory and Klopf's hedonistic-neuron ideas to the south-west (adjacent field, in only as what fed actor–critic); Watkins's Q-learning (era 05) to the south; DQN, AlphaGo and policy-gradient RLHF (eras 06–08) to the east. [29][30][60][62][63][65]
- **Theory of approximation and learning** (Cybenko, Hornik, White, Baum; MacKay, Neal and Bishop on the Bayesian side; Broomhead & Lowe's RBF nets) — universal approximation, capacity, generalisation, Bayesian model comparison, priors for infinite-width networks; borders: computational learning theory / PAC / VC theory and kernel methods (era 05) directly south; Bayesian ML (era 05) south-east. [26][73][74][76][89]
- **Neuromorphic / analog-VLSI hardware** (Caltech; Mead, Mahowald, with Hopfield as physics neighbour) — silicon retina and cochlea, subthreshold-CMOS neurons; borders: the Hopfield energy models to the north (same Caltech campus); Lisp machines and Connection Machine of era 03 to the west as the previous AI-hardware wave; GPUs and TPUs (eras 06–07) far to the east. [86][87][88]

## Map notes
- Suggested A1 label: **"Connectionist Revival"** (or "The PDP Era"). A2 labels: *PDP Cognitive Modelling*, *Energy Models (Hopfield–Boltzmann)*, *Bell Labs ConvNets*, *Recurrent Nets & LSTM*, *RL Province (UMass–IBM)*, *Approximation & Bayesian Theory*, *ART / Boston University*, *Neuromorphic Caltech*. A3: UCSD PDP group, CMU, Toronto (Hinton from 1987, also a CIFAR fellow from 1987), Bell Labs Holmdel, TU Munich/IDSIA, Caltech (Hopfield, Mead, MacKay), IBM Watson, UMass Amherst, Boston University, Helsinki (Kohonen, Oja), RSRE Malvern. [41]
- Rivers/borders: the **Fodor–Pylyshyn river (1988)** separates this continent from the symbolic/expert-systems landmass of era 03; it is bridged only by cognitive science. The **1987 Lisp-machine collapse / second AI winter** is a coastline event to the west. To the south-east, a wide **statistical-learning strait** (SVMs, graphical models, HMMs — era 05) partially submerges connectionism in the mid-1990s; LSTM (1997) and LeNet-5 (1998) are the last high ground before the deep-learning continent rises again after 2006/2012 (era 06). [24][49][50]
- Bridges east: LeNet → AlexNet; RBM → deep belief nets; Helmholtz machine / wake-sleep → variational autoencoders; mixtures of experts (1991) → sparse MoE LLMs; TD-Gammon, actor–critic and REINFORCE → DQN/AlphaGo/RLHF; MacKay–Neal Bayesian nets → Gaussian processes and Bayesian deep learning; LSTM → seq2seq/GNMT; NIPS 1987 → NeurIPS as the field's main venue. [31][49]
- Open questions for curation: (1) Where to put the Werbos/Linnainmaa priority thread (and the Amari 1967/1972 Japanese line) — as an off-map "source spring" west of 1982? (2) Should Kohonen SOMs, Oja's rule and ART (Grossberg) form one "unsupervised/competitive learning" A2 country, or stay as two A3 cities (Helsinki, Boston)? (3) The 1988–1998 "neural nets in speech" work (TDNN, hybrid HMM/ANN) straddles the border with era 05 — assign to one side or draw it as a shared delta. (4) The RL province (Barto–Sutton 1983–1998) is claimed by eras 03, 04 and 05 — the reviewer suggests drawing it once, as a river with its source here (1983 actor–critic) and its mouth in era 06 (DQN).

## Sources
[1] Connectionism — Wikipedia — https://en.wikipedia.org/wiki/Connectionism (accessed 2026-09-06)
[2] Hopfield network — Wikipedia — https://en.wikipedia.org/wiki/Hopfield_network (accessed 2026-09-06)
[3] Hopfield, J. J. (1982). Neural networks and physical systems with emergent collective computational abilities. PNAS 79(8):2554–2558 — https://europepmc.org/article/MED/6953413 (accessed 2026-09-06)
[4] Hopfield, J. J. (1984). Neurons with graded response have collective computational properties like those of two-state neurons. PNAS 81(10):3088–3092 — https://europepmc.org/article/MED/6587342 (accessed 2026-09-06)
[5] Neocognitron — Wikipedia — https://en.wikipedia.org/wiki/Neocognitron (accessed 2026-09-06)
[6] Fukushima (1980), Biological Cybernetics 36(4):193–202 — https://doi.org/10.1007/BF00344251 (accessed 2026-09-06)
[7] Backpropagation — Wikipedia (history section: Linnainmaa 1970, Werbos 1982, Rumelhart 1985/1986) — https://en.wikipedia.org/wiki/Backpropagation (accessed 2026-09-06)
[8] Rumelhart, Hinton & Williams (1986), Nature 323:533–536 — https://doi.org/10.1038/323533a0 (accessed 2026-09-06)
[9] Linnainmaa (1976), BIT 16:146–160 — https://doi.org/10.1007/BF01931367 (accessed 2026-09-06)
[10] Seppo Linnainmaa — Wikipedia — https://en.wikipedia.org/wiki/Seppo_Linnainmaa (accessed 2026-09-06)
[11] Paul Werbos — Wikipedia — https://en.wikipedia.org/wiki/Paul_Werbos (accessed 2026-09-06)
[12] Boltzmann machine — Wikipedia — https://en.wikipedia.org/wiki/Boltzmann_machine (accessed 2026-09-06)
[13] Ackley, Hinton & Sejnowski (1985), Cognitive Science 9:147–169 (author PDF) — https://www.cs.toronto.edu/~hinton/absps/cogscibm.pdf (accessed 2026-09-06)
[14] Parallel Distributed Processing (Connectionism article, PDP section and references) — Wikipedia — https://en.wikipedia.org/wiki/Parallel_Distributed_Processing (accessed 2026-09-06)
[15] PDP volume chapters hosted by J. L. McClelland (Stanford) — https://stanford.edu/~jlmcc/papers/PDP/ (accessed 2026-09-06)
[16] NETtalk (artificial neural network) — Wikipedia — https://en.wikipedia.org/wiki/NETtalk_%28artificial_neural_network%29 (accessed 2026-09-06)
[17] Sejnowski & Rosenberg (1987), Complex Systems 1:145–168 — https://www.complex-systems.com/abstracts/v01_i01_a10/ (accessed 2026-09-06)
[18] LeNet — Wikipedia — https://en.wikipedia.org/wiki/LeNet (accessed 2026-09-06)
[19] LeCun et al. (1989), Neural Computation 1(4):541–551 (author PDF) — http://yann.lecun.com/exdb/publis/pdf/lecun-89e.pdf (accessed 2026-09-06)
[20] LeCun, Bottou, Bengio & Haffner (1998), Proc. IEEE 86(11):2278–2324 — https://doi.org/10.1109/5.726791 (accessed 2026-09-06)
[21] MNIST database — Wikipedia — https://en.wikipedia.org/wiki/MNIST_database (accessed 2026-09-06)
[22] Long short-term memory — Wikipedia — https://en.wikipedia.org/wiki/Long_short-term_memory (accessed 2026-09-06)
[23] Hochreiter & Schmidhuber (1997), Neural Computation 9(8):1735–1780 (author PDF) — https://www.bioinf.jku.at/publications/older/2604.pdf (accessed 2026-09-06)
[24] Vanishing gradient problem — Wikipedia — https://en.wikipedia.org/wiki/Vanishing_gradient_problem (accessed 2026-09-06)
[25] Bengio, Simard & Frasconi (1994), IEEE Trans. Neural Networks 5(2):157–166 — https://doi.org/10.1109/72.279181 (accessed 2026-09-06)
[26] Universal approximation theorem — Wikipedia — https://en.wikipedia.org/wiki/Universal_approximation_theorem (accessed 2026-09-06)
[27] Cybenko (1989), Math. Control Signals Systems 2:303–314 — https://doi.org/10.1007/BF02551274 (accessed 2026-09-06)
[28] Hornik, Stinchcombe & White (1989), Neural Networks 2(5):359–366 — https://doi.org/10.1016/0893-6080%2889%2990020-8 (accessed 2026-09-06)
[29] TD-Gammon — Wikipedia — https://en.wikipedia.org/wiki/TD-Gammon (accessed 2026-09-06)
[30] Tesauro (1995), Communications of the ACM 38(3):58–68 (author-authorised HTML) — https://www.bkgm.com/articles/tesauro/tdl.html (accessed 2026-09-06)
[31] Conference on Neural Information Processing Systems — Wikipedia — https://en.wikipedia.org/wiki/Conference_on_Neural_Information_Processing_Systems (accessed 2026-09-06)
[32] Recurrent neural network — Wikipedia — https://en.wikipedia.org/wiki/Recurrent_neural_network (accessed 2026-09-06)
[33] Elman (1990), Cognitive Science 14(2):179–211 — https://www.semanticscholar.org/paper/668087f0ae7ce1de6e0bd0965dbb480c08103260 (accessed 2026-09-06)
[34] Convolutional neural network — Wikipedia — https://en.wikipedia.org/wiki/Convolutional_neural_network (accessed 2026-09-06)
[35] Waibel et al. (1989), IEEE Trans. ASSP 37(3):328–339 — https://doi.org/10.1109/29.21701 (accessed 2026-09-06)
[36] Self-organizing map — Wikipedia — https://en.wikipedia.org/wiki/Self-organizing_map (accessed 2026-09-06)
[37] Kohonen (1982), Biological Cybernetics 43:59–69 — https://doi.org/10.1007/BF00337288 (accessed 2026-09-06)
[38] Fodor & Pylyshyn (1988), Cognition 28:3–71 — https://doi.org/10.1016/0010-0277%2888%2990031-5 (accessed 2026-09-06)
[39] Pinker & Prince (1988), Cognition 28:73–193 — https://doi.org/10.1016/0010-0277%2888%2990032-7 (accessed 2026-09-06)
[40] Schuster & Paliwal (1997), IEEE Trans. Signal Processing 45(11):2673–2681 — https://doi.org/10.1109/78.650093 (accessed 2026-09-06)
[41] Geoffrey Hinton — Wikipedia — https://en.wikipedia.org/wiki/Geoffrey_Hinton (accessed 2026-09-06)
[42] Yann LeCun — Wikipedia — https://en.wikipedia.org/wiki/Yann_LeCun (accessed 2026-09-06)
[43] Terry Sejnowski — Wikipedia — https://en.wikipedia.org/wiki/Terry_Sejnowski (accessed 2026-09-06)
[44] David Rumelhart — Wikipedia — https://en.wikipedia.org/wiki/David_Rumelhart (accessed 2026-09-06)
[45] Kunihiko Fukushima — Wikipedia — https://en.wikipedia.org/wiki/Kunihiko_Fukushima (accessed 2026-09-06)
[46] Sepp Hochreiter — Wikipedia — https://en.wikipedia.org/wiki/Sepp_Hochreiter (accessed 2026-09-06)
[47] Jürgen Schmidhuber — Wikipedia — https://en.wikipedia.org/wiki/J%C3%BCrgen_Schmidhuber (accessed 2026-09-06)
[48] The Nobel Prize in Physics 2024 — NobelPrize.org — https://www.nobelprize.org/prizes/physics/2024/summary/ (accessed 2026-09-06)
[49] Deep learning — Wikipedia (history section) — https://en.wikipedia.org/wiki/Deep_learning (accessed 2026-09-06)
[50] History of artificial intelligence — Wikipedia (1987 Lisp-machine collapse, second AI winter) — https://en.wikipedia.org/wiki/History_of_artificial_intelligence (accessed 2026-09-06)
[51] Machine Learning (journal) — Wikipedia — https://en.wikipedia.org/wiki/Machine_Learning_%28journal%29 (accessed 2026-09-06)
[52] Gerald Tesauro — Wikipedia — https://en.wikipedia.org/wiki/Gerald_Tesauro (accessed 2026-09-06)
[53] Teuvo Kohonen — Wikipedia — https://en.wikipedia.org/wiki/Teuvo_Kohonen (accessed 2026-09-06)
[54] James McClelland (psychologist) — Wikipedia — https://en.wikipedia.org/wiki/James_McClelland_%28psychologist%29 (accessed 2026-09-06)
[55] Ronald J. Williams — Wikipedia — https://en.wikipedia.org/wiki/Ronald_J._Williams (accessed 2026-09-06)
[56] George Cybenko — Wikipedia — https://en.wikipedia.org/wiki/George_Cybenko (accessed 2026-09-06)
[57] Alex Waibel — Wikipedia — https://en.wikipedia.org/wiki/Alex_Waibel (accessed 2026-09-06)
[58] Jeffrey Elman — Wikipedia — https://en.wikipedia.org/wiki/Jeffrey_Elman (accessed 2026-09-06)
[59] Turing Award — Wikipedia (2018 award to Bengio, Hinton, LeCun) — https://en.wikipedia.org/wiki/Turing_Award (accessed 2026-09-06)
[60] Barto, Sutton & Anderson (1983), Neuronlike adaptive elements that can solve difficult learning control problems, IEEE Trans. SMC-13(5):834–846 — https://doi.org/10.1109/TSMC.1983.6313077 (accessed 2026-09-06)
[61] Andrew Barto — Wikipedia — https://en.wikipedia.org/wiki/Andrew_Barto (accessed 2026-09-06)
[62] Sutton (1988), Learning to predict by the methods of temporal differences, Machine Learning 3:9–44 — https://doi.org/10.1007/BF00115009 (accessed 2026-09-06)
[63] Sutton & Barto (1998), Reinforcement Learning: An Introduction, MIT Press — authors' first-edition page (incl. ch. 1.6 history: actor–critic 1983, Klopf, Witten) — http://incompleteideas.net/book/first/the-book.html (accessed 2026-09-06)
[64] Richard S. Sutton — Wikipedia (GTE Labs 1985–94; 2024 Turing Award) — https://en.wikipedia.org/wiki/Richard_S._Sutton (accessed 2026-09-06)
[65] Williams (1992), Simple statistical gradient-following algorithms for connectionist reinforcement learning, Machine Learning 8:229–256 — https://doi.org/10.1007/BF00992696 (accessed 2026-09-06)
[66] Policy gradient method — Wikipedia (REINFORCE, Williams 1992) — https://en.wikipedia.org/wiki/Policy_gradient_method (accessed 2026-09-06)
[67] Jacobs, Jordan, Nowlan & Hinton (1991), Adaptive Mixtures of Local Experts, Neural Computation 3(1):79–87 (author PDF; publication list at https://www.cs.toronto.edu/~hinton/papers.html) — https://www.cs.toronto.edu/~hinton/absps/jjnh91.pdf (accessed 2026-09-06)
[68] Mixture of experts — Wikipedia — https://en.wikipedia.org/wiki/Mixture_of_experts (accessed 2026-09-06)
[69] Michael I. Jordan — Wikipedia (UCSD PhD 1985 under Rumelhart; MIT 1988–98) — https://en.wikipedia.org/wiki/Michael_I._Jordan (accessed 2026-09-06)
[70] Hinton, Dayan, Frey & Neal (1995), The wake-sleep algorithm for unsupervised neural networks, Science 268:1158–1161 (author PDF) — https://www.cs.toronto.edu/~hinton/absps/ws.pdf (accessed 2026-09-06)
[71] Helmholtz machine — Wikipedia; Wake-sleep algorithm — Wikipedia — https://en.wikipedia.org/wiki/Helmholtz_machine ; https://en.wikipedia.org/wiki/Wake-sleep_algorithm (accessed 2026-09-06)
[72] Peter Dayan — Wikipedia (Edinburgh PhD, Salk/Toronto postdocs, MIT; Q-learning convergence with Watkins) — https://en.wikipedia.org/wiki/Peter_Dayan (accessed 2026-09-06)
[73] MacKay (1992), A Practical Bayesian Framework for Backpropagation Networks, Neural Computation 4(3):448–472 — Crossref record (direct.mit.edu returns 403 to non-browser requests) https://api.crossref.org/works/10.1162/neco.1992.4.3.448 ; MacKay's thesis page http://www.inference.org.uk/mackay/PhD.html (accessed 2026-09-06)
[74] Neal (1996), Bayesian Learning for Neural Networks, Lecture Notes in Statistics 118, Springer (ch. 2 "Priors for Infinite Networks") — https://doi.org/10.1007/978-1-4612-0745-0 (accessed 2026-09-06)
[75] David J. C. MacKay — Wikipedia (Caltech PhD 1992 under Hopfield); Radford M. Neal — Wikipedia (Toronto PhD 1995 under Hinton) — https://en.wikipedia.org/wiki/David_J._C._MacKay ; https://en.wikipedia.org/wiki/Radford_M._Neal (accessed 2026-09-06)
[76] Bishop (1995), Neural Networks for Pattern Recognition, Oxford University Press — Crossref record https://api.crossref.org/works/10.1093/oso/9780198538493.001.0001 ; Christopher Bishop — Wikipedia https://en.wikipedia.org/wiki/Christopher_Bishop (accessed 2026-09-06)
[77] Smolensky (1990), Tensor product variable binding and the representation of symbolic structures in connectionist systems, Artificial Intelligence 46:159–216 — https://doi.org/10.1016/0004-3702%2890%2990007-M (accessed 2026-09-06)
[78] Smolensky (1988), On the proper treatment of connectionism, Behavioral and Brain Sciences 11:1–23 — https://doi.org/10.1017/S0140525X00052432 (accessed 2026-09-06)
[79] Paul Smolensky — Wikipedia; Restricted Boltzmann machine — Wikipedia (Harmonium, 1986) — https://en.wikipedia.org/wiki/Paul_Smolensky ; https://en.wikipedia.org/wiki/Restricted_Boltzmann_machine (accessed 2026-09-06)
[80] Pollack (1990), Recursive distributed representations, Artificial Intelligence 46:77–105 — https://doi.org/10.1016/0004-3702%2890%2990005-K (accessed 2026-09-06)
[81] Stephen Grossberg — Wikipedia (INNS 1987, Neural Networks journal, DARPA Neural Network Study 1987–88, ICNN 1987 → IJCNN 1989) — https://en.wikipedia.org/wiki/Stephen_Grossberg (accessed 2026-09-06)
[82] Carpenter & Grossberg (1987), A massively parallel architecture for a self-organizing neural pattern recognition machine, Computer Vision, Graphics, and Image Processing 37:54–115 — https://doi.org/10.1016/S0734-189X%2887%2980014-2 ; Adaptive resonance theory — Wikipedia https://en.wikipedia.org/wiki/Adaptive_resonance_theory (accessed 2026-09-06)
[83] Neural Networks (journal) — Wikipedia (established 1988; founding editor Grossberg) — https://en.wikipedia.org/wiki/Neural_Networks_%28journal%29 (accessed 2026-09-06)
[84] Neural Computation (journal) — Wikipedia (established 1989, MIT Press, editor Sejnowski) — https://en.wikipedia.org/wiki/Neural_Computation_%28journal%29 (accessed 2026-09-06)
[85] Perceptrons (book) — Wikipedia (1988 expanded edition with new prologue and epilogue) — https://en.wikipedia.org/wiki/Perceptrons_%28book%29 (accessed 2026-09-06)
[86] Carver Mead — Wikipedia; Open Library record for Analog VLSI and Neural Systems (1989) — https://en.wikipedia.org/wiki/Carver_Mead ; https://openlibrary.org/search.json?title=Analog+VLSI+and+Neural+Systems&author=Mead (accessed 2026-09-06)
[87] Mead (1990), Neuromorphic electronic systems, Proceedings of the IEEE 78(10):1629–1636 — https://doi.org/10.1109/5.58356 ; Neuromorphic computing — Wikipedia https://en.wikipedia.org/wiki/Neuromorphic_computing (accessed 2026-09-06)
[88] Misha Mahowald — Wikipedia (silicon retina; PhD 1992) — https://en.wikipedia.org/wiki/Misha_Mahowald (accessed 2026-09-06)
[89] Broomhead & Lowe (1988), Multivariable functional interpolation and adaptive networks, Complex Systems 2(3) — https://www.complex-systems.com/abstracts/v02_i03_a05/ ; Radial basis function network — Wikipedia https://en.wikipedia.org/wiki/Radial_basis_function_network (accessed 2026-09-06)
[90] Oja's rule — Wikipedia (1982 paper; PCA) — https://en.wikipedia.org/wiki/Oja%27s_rule (accessed 2026-09-06)
[91] Shun'ichi Amari — Wikipedia (1967 SGD-trained MLP; 1972 Amari–Hopfield network); Hopfield network — Wikipedia, history section (Nakano 1971, Amari 1972, Little 1974) — https://en.wikipedia.org/wiki/Shun%27ichi_Amari ; https://en.wikipedia.org/wiki/Hopfield_network (accessed 2026-09-06)
[92] Robert Hecht-Nielsen — Wikipedia (HNC Software founded 1986; Neurocomputing textbook 1989) — https://en.wikipedia.org/wiki/Robert_Hecht-Nielsen (accessed 2026-09-06)
