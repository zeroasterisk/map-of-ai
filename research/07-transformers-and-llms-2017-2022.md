# Transformers and Large Language Models (2017–2022)

> **Status:** reviewed
> **Date range:** 2017–2022
> **Map placement (proposed):** X = 2017–2022; Y = connectionist/scaling pole (with a thin "alignment" tributary emerging at the eastern edge)
> **Altitude:** A1 continent ("The Transformer Plateau"), A2 country (Google/Brain, OpenAI, DeepMind, Hugging Face, EleutherAI), A3 city (BERT, GPT-2, GPT-3, T5, ViT, CLIP, AlphaFold 2, Chinchilla, Gopher, OPT), A4 street (scaling-law papers, benchmarks — GLUE/MMLU/BIG-bench/HELM, tokenizers, Megatron/DeepSpeed systems papers, A100)

## One-paragraph summary
In June 2017 eight Google researchers published "Attention Is All You Need", replacing recurrence with self-attention and giving deep learning a highly parallelisable sequence architecture: the Transformer [1][2]. Within eighteen months two pre-train-then-fine-tune recipes built on it — OpenAI's decoder-only GPT (June 2018) and Google's encoder-only BERT (October 2018) — swept NLP benchmarks and made "pretrained language model" the default starting point for any text task [4][5][6][7]. The era's central discovery was empirical rather than architectural: model quality improves smoothly and predictably with parameters, data and compute (Kaplan et al., January 2020), which justified GPT-3's 175-billion-parameter bet (May 2020) and its surprising few-shot, in-context learning [9][10][11]. The same architecture then crossed modalities — Vision Transformer (2020), CLIP and DALL-E (January 2021), AlphaFold 2's protein-structure breakthrough (CASP14, November 2020; Nature, July 2021), Codex/Copilot for code (2021) — while DeepMind's Chinchilla (March 2022) corrected the scaling recipe toward more data per parameter [12][13][14][15][17][20]. The period ends with the ingredients of the chatbot age assembled but not yet released to the public: InstructGPT's reinforcement learning from human feedback (March 2022), PaLM's 540B parameters and chain-of-thought reasoning (April 2022), and open-weights counter-movements (EleutherAI, Meta's OPT-175B, BLOOM) that foreshadow the open-vs-closed rift of the next era [18][19][21][22][23][72]. Underneath ran a systems layer — Nvidia's Megatron-LM and A100, Microsoft's DeepSpeed, Google's TPU v4 — and a benchmark layer (GLUE 2018 → MMLU 2020 → BIG-bench/HELM 2022) that turned "capability" into a leaderboard number; outside the Bay Area, BAAI's Wu Dao, Huawei's PanGu and Baidu's ERNIE showed China entering the scaling race by mid-2021 [47][57][61][63][74].

## Timeline of key events
| Year | Event | Why it matters | Source |
|------|-------|----------------|--------|
| 2014 | Bahdanau, Cho & Bengio introduce attention for neural machine translation; Sutskever et al. publish seq2seq (Sept 2014) | Encoder–decoder + attention is the direct ancestor of the Transformer | [24][25] |
| 2016 (Nov) | Google Neural Machine Translation goes live in Google Translate | Shows neural sequence models at production scale; sets the stage for replacing RNNs | [26] |
| 2017 (Jan) | Shazeer et al., "Outrageously Large Neural Networks" — sparsely-gated mixture-of-experts layer (arXiv 1701.06538, 23 Jan 2017) | MoE at 100B+ parameters; the technique later returns in Switch Transformer, Mixtral, DeepSeek | [27] |
| 2017 (12 Jun) | Vaswani et al., "Attention Is All You Need" (arXiv 1706.03762); published at NIPS 2017 | Introduces the Transformer; all eight authors are Google employees at the time | [1][2][3] |
| 2017 (Oct) | Micikevicius et al. (Nvidia/Baidu), "Mixed Precision Training" (arXiv 1710.03740, 10 Oct 2017) | FP16 training with loss scaling on Volta Tensor Cores — the numeric recipe every large Transformer run inherits | [95] |
| 2018 (15 Feb) | Peters et al., ELMo — deep contextualised word representations (arXiv 1802.05365; NAACL 2018) | Contextual embeddings from a bidirectional LSTM; the last big pre-Transformer NLP win. Howard & Ruder's ULMFiT (arXiv 1801.06146, 18 Jan 2018) had shown a month earlier that LM pre-training + fine-tuning transfers to text classification | [4][46] |
| 2018 (Feb–Mar) | Brundage et al. (Oxford/Cambridge/OpenAI…), "The Malicious Use of Artificial Intelligence" (arXiv 1802.07228, 20 Feb 2018); Gebru et al., "Datasheets for Datasets" (arXiv 1803.09010, 23 Mar 2018) | Misuse forecasting and dataset documentation: the two policy-facing reports that frame the GPT-2 release debate and model cards | [96][97] |
| 2018 (20 Apr) | Wang, Bowman et al., GLUE benchmark (arXiv 1804.07461; NYU/UW/DeepMind); SuperGLUE follows on 2 May 2019 (arXiv 1905.00537) after models pass GLUE's human baseline | Shared leaderboard that BERT, XLNet, RoBERTa and T5 race up; benchmarks become the era's scoreboard | [47][48] |
| 2018 (Jun) | OpenAI releases GPT-1 paper "Improving Language Understanding by Generative Pre-Training" (117M parameters) | Decoder-only Transformer + generative pre-training + task fine-tuning | [5][6] |
| 2018 (11 Oct) | Devlin et al., BERT (arXiv 1810.04805); state of the art on GLUE, SQuAD v1.1/v2.0, SWAG | Encoder-only bidirectional pre-training; becomes the workhorse of industrial NLP and Google Search | [7][8] |
| 2018 (Oct) | GitHub creation of Google's JAX (repo created 25 Oct 2018): composable grad/vmap/jit transformations of NumPy, compiled via XLA to GPU/TPU | Google's research framework for grad/vmap/jit program transformations; its XLA/TPU path becomes a main alternative to PyTorch for large-model research | [98] |
| 2018 (Nov) | Huang et al. (Google), "GPipe: Efficient Training of Giant Neural Networks using Pipeline Parallelism" (arXiv 1811.06965, 16 Nov 2018) | Pipeline model parallelism — with Megatron's tensor parallelism and ZeRO, one of the three axes of giant-model training | [99] |
| 2019 (Feb) | Houlsby et al. (Google), "Parameter-Efficient Transfer Learning for NLP" (arXiv 1902.00751, 2 Feb 2019) — adapters | Small trainable modules inserted into a frozen BERT: the start of parameter-efficient fine-tuning that leads to prefix-tuning and LoRA | [100] |
| 2019 (Apr) | Child, Gray, Radford & Sutskever (OpenAI), "Generating Long Sequences with Sparse Transformers" (arXiv 1904.10509, 23 Apr 2019) | Factorised sparse attention reaches sequences tens of thousands long; opens the efficient-attention line (Reformer, Longformer, Performer) | [101] |
| 2019 (Feb) | OpenAI announces GPT-2 (1.5B parameters, trained on 8M web pages) but initially withholds the full model; 774M released 20 Aug, full 1.5B on 5 Nov 2019 | First "too dangerous to release" staged-release controversy; zero-shot task transfer | [28][29] |
| 2019 (13 Mar) | Rich Sutton posts the essay "The Bitter Lesson" | Names the scaling creed — general methods that leverage computation beat built-in human knowledge; the era's one-page manifesto | [49][50] |
| 2019 (Jun) | Strubell, Ganesh & McCallum (UMass), "Energy and Policy Considerations for Deep Learning in NLP" (arXiv 1906.02243, 5 Jun 2019) | First widely cited carbon and cost estimate for training large NLP models — the environmental strand of the critique that Stochastic Parrots extends | [102] |
| 2019 (Jan–Oct) | The BERT-improvement wave: Transformer-XL (CMU/Google, arXiv 1901.02860, 9 Jan), XLNet (19 Jun, arXiv 1906.08237), RoBERTa (Facebook AI, 26 Jul, arXiv 1907.11692), DistilBERT (Hugging Face, 2 Oct, arXiv 1910.01108) | Better pre-training recipes, longer context and distillation for deployment; each tops GLUE in turn | [53][54][55][56] |
| 2019 (Aug–Nov) | Encoder variants multiply: Sentence-BERT (Reimers & Gurevych, arXiv 1908.10084, 27 Aug); ALBERT (Lan et al., Google, arXiv 1909.11942, 26 Sep); BART (Lewis et al., Facebook AI, arXiv 1910.13461, 29 Oct); XLM-R cross-lingual pre-training at scale (Conneau et al., arXiv 1911.02116, 5 Nov) | Sentence embeddings for retrieval, parameter sharing, denoising seq2seq pre-training and 100-language encoders extend BERT in four directions | [103][104][105][106] |
| 2019 (Sep–Nov) | Salesforce's CTRL, a 1.63B conditional LM (Keskar et al., arXiv 1909.05858, 11 Sep 2019); Microsoft's DialoGPT (Zhang et al., arXiv 1911.00536, 1 Nov 2019) | Control codes steer generation; GPT-2-style dialogue pre-training on Reddit — the first big labs to follow OpenAI's decoder recipe | [107][108] |
| 2019 (22 Jul) | OpenAI restructures earlier in 2019 as the "capped-profit" OpenAI LP (returns capped at 100×); Microsoft invests $1B and becomes its exclusive cloud provider (22 Jul 2019) | Funding structure that pays for GPT-3-scale compute; start of the Microsoft–OpenAI axis | [51][52] |
| 2019 (17 Sep)–2020 (13 Feb) | Nvidia's Megatron-LM (8.3B, tensor/model parallelism, arXiv 1909.08053) and Microsoft's ZeRO optimizer sharding / DeepSpeed (arXiv 1910.02054, Oct 2019) → Turing-NLG 17B (13 Feb 2020); the two stacks later jointly train Megatron-Turing NLG 530B (arXiv 2201.11990) | The systems engineering that makes 100B+ dense models trainable on GPU clusters | [57][58][59][60] |
| 2019 (23 Oct) | Raffel et al., T5 "Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer" (arXiv 1910.10683); introduces the C4 corpus | Casts every NLP task as text-to-text; systematic study of transfer-learning design choices | [30][31] |
| 2019 (Nov–Dec) | He et al. (FAIR), MoCo — "Momentum Contrast for Unsupervised Visual Representation Learning" (arXiv 1911.05722, 13 Nov 2019); Nakkiran et al. (Harvard/OpenAI), "Deep Double Descent" (arXiv 1912.02292, 4 Dec 2019) | Contrastive self-supervision starts to rival supervised ImageNet pre-training; double descent says bigger models can generalise better | [110][111] |
| 2019 | Hugging Face's `transformers` library (open-source) becomes the de facto hub for sharing pretrained Transformer models | Open distribution layer for the whole era; company founded 2016 in New York | [32][33] |
| 2019 (Oct) | Wolf et al., "HuggingFace's Transformers: State-of-the-art Natural Language Processing" (arXiv 1910.03771, 9 Oct 2019) | The library's paper of record, giving a citable date for the de facto model hub | [109] |
| 2020 (23 Jan) | Kaplan et al., "Scaling Laws for Neural Language Models" (arXiv 2001.08361) | Loss falls as a power law in parameters, data and compute; makes scale a research strategy | [9][10] |
| 2020 (Jan–Apr) | Efficient attention: Reformer (Kitaev, Kaiser & Levskaya, arXiv 2001.04451, 13 Jan 2020); Longformer (Beltagy, Peters & Cohan, AI2, arXiv 2004.05150, 10 Apr 2020); Performer (Choromanski et al., arXiv 2009.14794, 30 Sep 2020) | Hashing, local-plus-global and kernel approximations attack attention's quadratic cost — the long-context problem FlashAttention later solves in hardware | [112][113][114] |
| 2020 (Feb–Apr) | Retrieval meets pre-training: REALM (Guu et al., Google, arXiv 2002.08909, 10 Feb 2020) and Dense Passage Retrieval (Karpukhin et al., Facebook AI, arXiv 2004.04906, 10 Apr 2020) | Learned dense retrievers feed Transformers with documents — the components RAG (May 2020) assembles | [115][116] |
| 2020 (Feb–Jun) | Self-supervised vision: SimCLR (Chen, Kornblith, Norouzi & Hinton, arXiv 2002.05709, 13 Feb 2020); BYOL (Grill et al., DeepMind, arXiv 2006.07733, 13 Jun 2020) | Contrastive and non-contrastive image pre-training close the gap with supervised ImageNet features | [117][118] |
| 2020 (Mar) | Clark, Luong, Le & Manning (Stanford/Google), ELECTRA (arXiv 2003.10555, 23 Mar 2020) | Replaced-token detection pre-trains encoders far more compute-efficiently than BERT's masked LM | [119] |
| 2020 (Apr) | Roller et al. (Facebook AI), BlenderBot — "Recipes for building an open-domain chatbot" (arXiv 2004.13637, 28 Apr 2020), open-sourced up to 9.4B parameters | Facebook's open answer to Meena: the largest open dialogue model of 2020 | [120] |
| 2020 (14 May) | Nvidia announces the Ampere architecture and A100 GPU (third-gen tensor cores with TF32/bfloat16, 40 GB HBM2; 80 GB version 16 Nov 2020) | Workhorse accelerator of GPT-3-era training — OPT, BLOOM and YaLM are all trained on A100 clusters; hardware river (file 09d) | [61][62] |
| 2020 (28 May) | Brown et al., GPT-3, "Language Models are Few-Shot Learners" (arXiv 2005.14165), 175B parameters; API access announced 11 Jun 2020 | In-context/few-shot learning without gradient updates; first LLM sold as an API | [11][12] |
| 2020 (May) | Carion et al. (Facebook AI), DETR — "End-to-End Object Detection with Transformers" (arXiv 2005.12872, 26 May 2020) | The Transformer enters object detection, replacing anchors and non-maximum suppression with set prediction | [121] |
| 2020 (Jun) | Baevski, Zhou, Mohamed & Auli (Facebook AI), wav2vec 2.0 (arXiv 2006.11477, 20 Jun 2020) | Self-supervised speech pre-training: strong recognition with ten minutes of labelled audio | [122] |
| 2020 (19 Jun)–2021 (20 Dec) | Diffusion headwaters: Ho, Jain & Abbeel, DDPM (Berkeley, arXiv 2006.11239); Dhariwal & Nichol, "Diffusion Models Beat GANs on Image Synthesis" (OpenAI, arXiv 2105.05233, 11 May 2021); Nichol et al., GLIDE text-guided diffusion (arXiv 2112.10741, 20 Dec 2021) | Diffusion displaces GANs and, guided by CLIP, leads directly to DALL-E 2 (Apr 2022) and the generative-media district of file 08 | [82][83][84] |
| 2020 (7 Sep) | Hendrycks et al., MMLU — 57-subject, ~16k-question multiple-choice benchmark (arXiv 2009.03300) | Becomes the standard capability yardstick from GPT-3 to GPT-4; benchmark street | [63] |
| 2020 (Oct) | Henighan, Kaplan et al. (OpenAI), "Scaling Laws for Autoregressive Generative Modeling" (arXiv 2010.14701, 28 Oct 2020) | Power laws hold for images, video, maths and multimodal models, not just text | [123] |
| 2020 (22 Oct) | Dosovitskiy et al., Vision Transformer, "An Image is Worth 16x16 Words" (arXiv 2010.11929; ICLR 2021) | Transformers displace CNNs at the top of image classification | [13] |
| 2021 (Mar–Apr) | Vision Transformers mature: Swin Transformer (Liu et al., Microsoft Research Asia, arXiv 2103.14030, 25 Mar 2021); DINO self-supervised ViTs (Caron et al., Facebook AI, arXiv 2104.14294, 29 Apr 2021) | Hierarchical shifted-window ViTs become the general vision backbone; self-distilled ViTs learn object segmentation unprompted | [126][127] |
| 2020 (30 Nov) | AlphaFold 2 wins CASP14 with GDT scores above 90 for roughly two-thirds of targets | Attention-based model solves a 50-year grand challenge in biology; Nature paper follows July 2021 | [14][15] |
| 2020 (Dec)–2021 (Mar) | Google forces out Timnit Gebru, co-lead of its Ethical AI team (Dec 2020), after demanding she retract the paper she co-wrote with Bender, McMillan-Major & Mitchell, "On the Dangers of Stochastic Parrots" (published FAccT, Mar 2021) | Landmark critique of LLM scale, data and environmental cost; the ethics-vs-scale rift becomes a public labour dispute | [38][67] |
| 2020 (31 Dec) | EleutherAI releases The Pile (825 GB open training corpus, arXiv 2101.00027); GPT-Neo/GPT-J (6B) follow in 2021 and GPT-NeoX-20B in Apr 2022 (arXiv 2204.06745) | Grassroots open replication of GPT-3-class models begins | [22][73] |
| 2021 (Jan–Apr) | Prompt-based adaptation: Prefix-Tuning (Li & Liang, Stanford, arXiv 2101.00190, 1 Jan 2021); Prompt Tuning (Lester, Al-Rfou & Constant, Google, arXiv 2104.08691, 18 Apr 2021) | Training only a few continuous prompt vectors matches fine-tuning as models grow — a scale-dependent adaptation route | [124][125] |
| 2021 (5 Jan) | OpenAI announces DALL-E (text-to-image, 12B-parameter GPT-3 variant) and CLIP (contrastive image–text pre-training) | Language-supervised vision; CLIP becomes the conditioning backbone for later diffusion models | [16][17] |
| 2021 (11 Jan) | Fedus, Zoph & Shazeer, Switch Transformer (arXiv 2101.03961) — trillion-parameter sparse MoE, building on GShard (Jun 2020, arXiv 2006.16668) | Demonstrates sparsity as a route past dense scaling limits | [34][93] |
| 2021 (Jan) | Dario and Daniela Amodei and five other OpenAI researchers found Anthropic (San Francisco); $124M raised May 2021 | Safety-focused frontier lab splits from OpenAI; Claude is trained by summer 2022 but withheld until Mar 2023 (file 08) | [69] |
| 2021 (Apr–Jul) | China's GPT-3-class models: Huawei PanGu-α (up to 200B, arXiv 2104.12369, 26 Apr); BAAI Wu Dao 2.0 (1.75-trillion-parameter MoE, 31 May 2021); Baidu ERNIE 3.0 (arXiv 2107.02137, 5 Jul) | State-backed BAAI and the big platforms enter the scaling race; origin of the "Chinese shore" of file 08 | [74][75][76] |
| 2021 (18 May) | Google announces LaMDA at I/O 2021 (successor to Meena, Jan 2020, arXiv 2001.09977); Meena's builders Noam Shazeer & Daniel De Freitas leave to found Character.AI (Nov 2021; public beta 16 Sep 2022) | Dialogue-specialised LLM; June 2022 Lemoine "sentience" episode previews public reaction to chatbots; Google's reluctance to ship drives talent out | [35][87][88] |
| 2021 (Jun) | Chen et al. (Berkeley/FAIR/Google), "Decision Transformer: Reinforcement Learning via Sequence Modeling" (arXiv 2106.01345, 2 Jun 2021) | Offline RL recast as conditional sequence modelling — the Transformer absorbs reinforcement learning | [128] |
| 2021 (Jun) | Hu et al. (Microsoft), "LoRA: Low-Rank Adaptation of Large Language Models" (arXiv 2106.09685, 17 Jun 2021) | Trains low-rank update matrices instead of full weights, cutting trainable parameters ~10,000× on GPT-3; later the default open-model fine-tuning method | [129] |
| 2021 (29 Jun) | GitHub Copilot technical preview, powered by OpenAI Codex (Codex paper arXiv 2107.03374, 7 Jul 2021) | First mass-market LLM product; code generation becomes a flagship use case; paid general availability 21 Jun 2022; class-action copyright suit filed Nov 2022 | [18][36][90] |
| 2021 (16 Aug) | Stanford CRFM, "On the Opportunities and Risks of Foundation Models" (arXiv 2108.07258) | Coins "foundation model" as the umbrella term for large pretrained models | [37] |
| 2021 (Sep) | Lin, Hilton & Evans (Oxford/OpenAI), TruthfulQA (arXiv 2109.07958, 8 Sep 2021) | A benchmark where larger models were less truthful — evidence that scale alone does not fix imitative falsehoods | [130] |
| 2021 (Oct) | Cobbe et al. (OpenAI), "Training Verifiers to Solve Math Word Problems" (arXiv 2110.14168, 27 Oct 2021) — introduces GSM8K | The grade-school maths benchmark and the generate-then-verify idea behind later reasoning models | [131] |
| 2021 (Nov) | Schuhmann et al., LAION-400M open image–text dataset (arXiv 2111.02114, 3 Nov 2021); LAION-5B follows (arXiv 2210.08402, 16 Oct 2022) | Volunteer-built CLIP-filtered web datasets that make open CLIP and Stable Diffusion training possible | [132][133] |
| 2021 (Nov) | He et al. (FAIR), "Masked Autoencoders Are Scalable Vision Learners" (arXiv 2111.06377, 11 Nov 2021) | BERT-style masked pre-training finally works for images with ViTs | [134] |
| 2021 (8 Dec) | DeepMind publishes Gopher (280B, arXiv 2112.11446), a taxonomy of ethical and social risks of LMs, and RETRO retrieval-augmented LM (arXiv 2112.04426) | DeepMind enters LLM scaling; Gopher is the baseline Chinchilla will beat three months later | [70][71] |
| 2021 (Dec) | Du et al. (Google), GLaM — 1.2T-parameter mixture-of-experts LM (arXiv 2112.06905, 13 Dec 2021); Nakano et al. (OpenAI), WebGPT — browser-assisted QA with human feedback (arXiv 2112.09332, 17 Dec 2021) | Sparse MoE matches GPT-3 at a fraction of the energy; an LLM that browses and cites — an early tool-use agent trained with RLHF | [135][136] |
| 2022 (28 Jan) | Wei et al., "Chain-of-Thought Prompting Elicits Reasoning" (arXiv 2201.11903) | Shows step-by-step prompting unlocks multi-step reasoning in large models | [39] |
| 2022 (Jan) | Thoppilan et al. (Google), "LaMDA: Language Models for Dialog Applications" (arXiv 2201.08239, 20 Jan 2022) | The paper behind the May 2021 LaMDA announcement: 137B dialogue model with safety and groundedness fine-tuning | [137] |
| 2022 (Feb) | Perez et al. (DeepMind), "Red Teaming Language Models with Language Models" (arXiv 2202.03286, 7 Feb 2022) | Automated red-teaming: one LM generates test cases that surface another's harmful outputs | [138] |
| 2022 (2 Feb) | DeepMind AlphaCode (arXiv 2203.07814) ranks in the top 54% of Codeforces competitors; Science, Dec 2022 | Competitive-programming milestone via massive sampling + filtering; code becomes the second front after Codex | [78] |
| 2022 (4 Mar) | Ouyang et al., InstructGPT, "Training language models to follow instructions with human feedback" (arXiv 2203.02155); builds on instruction-tuning precursors FLAN (Google, Sep 2021, arXiv 2109.01652) and T0 (BigScience, Oct 2021, arXiv 2110.08207) | RLHF recipe (SFT → reward model → PPO) that ChatGPT will use eight months later | [19][91][92] |
| 2022 (29 Mar) | Hoffmann et al., Chinchilla, "Training Compute-Optimal Large Language Models" (arXiv 2203.15556): 70B params on 1.4T tokens beats 280B Gopher | Revises scaling laws: models had been under-trained on data | [20][21] |
| 2022 (Mar–May) | Wang et al. (Google), self-consistency decoding (arXiv 2203.11171, 21 Mar 2022); Kojima et al. (Tokyo/Google), "Large Language Models are Zero-Shot Reasoners" (arXiv 2205.11916, 24 May 2022) — "Let's think step by step" | Sampling many reasoning chains and voting, and zero-shot chain-of-thought, extend CoT without new training | [139][140] |
| 2022 (5 Apr) | Chowdhery et al., PaLM (arXiv 2204.02311), 540B parameters trained on Pathways/TPU v4 pods | Largest dense LM of the era; strong chain-of-thought results; Minerva (Jun 2022, arXiv 2206.14858) fine-tunes PaLM on maths/science text | [23][79] |
| 2022 (Apr) | Ahn et al. (Google/Everyday Robots), SayCan — "Do As I Can, Not As I Say" (arXiv 2204.01691, 4 Apr 2022); Bai et al. (Anthropic), "Training a Helpful and Harmless Assistant with RLHF" (arXiv 2204.05862, 12 Apr 2022) | LLM planning grounded in robot affordances; Anthropic's first large RLHF paper and public HH preference dataset | [141][142] |
| 2022 (May–Jun) | Google text-to-image: Imagen diffusion (Saharia et al., arXiv 2205.11487, 23 May 2022) and Parti autoregressive (Yu et al., arXiv 2206.10789, 22 Jun 2022); Tay et al., UL2 unified pre-training (arXiv 2205.05131, 10 May 2022) | Frozen large text encoders drive photorealistic image generation; mixture-of-denoisers pre-training unifies encoder and decoder objectives | [143][144][145] |
| 2022 (3 May) | Meta AI releases OPT-175B (arXiv 2205.01068): weights to researchers on request, smaller sizes open, plus the full training logbook | First GPT-3-scale weights out of a big lab; precursor of Meta's Llama strategy (file 08) | [72] |
| 2022 (12 May) | DeepMind's Gato (arXiv 2205.06175) — a single Transformer for text, images, Atari and robot arms; alongside Perceiver (Mar 2021, arXiv 2103.03206) and Flamingo few-shot VLM (29 Apr 2022, arXiv 2204.14198) | Early "generalist agent" claim; bridge to embodied/agentic era | [40][80][81] |
| 2022 (27 May) | Dao, Fu, Ermon, Rudra & Ré (Stanford), "FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness" (arXiv 2205.14135) | IO-aware tiling computes exact attention faster with linear memory — the kernel that makes long-context training standard | [146] |
| 2022 (Jun–Nov) | Evaluation becomes a discipline: BIG-bench (204 tasks, ~450 authors, arXiv 2206.04615, 9 Jun); Wei et al., "Emergent Abilities of Large Language Models" (arXiv 2206.07682, 15 Jun); Stanford CRFM HELM (arXiv 2211.09110, 16 Nov) | "Emergence" frames the scaling debate for the next era; HELM standardises multi-metric evaluation | [64][65][66] |
| 2022 (Jul) | BigScience releases BLOOM (176B, 46 languages, RAIL licence) via Hugging Face, trained Mar–Jul 2022 on France's Jean Zay public supercomputer; Yandex open-sources YaLM-100B (Jun 2022, 800 A100s) | Largest open-access LLM of the period; open-science, state-funded counterweight to GPT-3 | [41][77][94] |
| 2022 (Sep) | OpenAI open-sources Whisper speech recognition (paper arXiv 2212.04356, Dec 2022) | Transformer conquers speech; notable as an OpenAI open-weights release | [42] |
| 2022 (Oct) | Zeng et al. (Tsinghua/Zhipu), GLM-130B open bilingual model (arXiv 2210.02414, 5 Oct 2022); Chung et al. (Google), Flan-PaLM/Flan-T5 — "Scaling Instruction-Finetuned Language Models" (arXiv 2210.11416, 20 Oct 2022) | An open Chinese–English 130B model whose weights run inference on consumer-GPU servers; instruction tuning on 1,800 tasks, with Flan-T5 checkpoints released openly | [147][148] |
| 2022 (15 Nov) | Meta AI releases Galactica (120B LLM for science, arXiv 2211.09085); public demo withdrawn after three days amid criticism of confident fabrications | Public "hallucination" backlash two weeks before ChatGPT; cautionary tale for LLM deployment | [85][86] |

## Key people
- **Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan Gomez, Łukasz Kaiser, Illia Polosukhin** (Google Brain / Google Research, 2017) — the eight "equal contribution" authors of the Transformer paper; all eight later left Google for startups. [2][3]
- **Jeremy Howard & Sebastian Ruder** (fast.ai / Insight Centre, Dublin) — ULMFiT (Jan 2018), the pre-train-then-fine-tune recipe for text classification. [46]
- **Alec Radford** (OpenAI) — first author of GPT-1 (2018) and GPT-2 (2019); also led CLIP and Whisper. [5][28][17]
- **Jacob Devlin** (Google AI Language) — first author of BERT (2018). [7]
- **Jared Kaplan** (Johns Hopkins / OpenAI) — co-authored "Scaling Laws for Neural Language Models" (2020); later an Anthropic co-founder. [9][43]
- **Tom Brown & Dario Amodei** (OpenAI) — led the 31-author GPT-3 paper (2020); Amodei's team also wrote the RLHF-precursor "Deep RL from Human Preferences" (2017); Amodei left to co-found Anthropic (Jan 2021). [11][44][69]
- **Samuel R. Bowman** (NYU) — GLUE (2018) and SuperGLUE (2019) benchmarks. [47][48]
- **Richard Sutton** (University of Alberta) — "The Bitter Lesson" (13 Mar 2019), the scaling school's founding text. [49][50]
- **Bryan Catanzaro & Mohammad Shoeybi** (Nvidia) — Megatron-LM tensor parallelism (2019); with Microsoft's DeepSpeed team, Megatron-Turing NLG 530B. [57][60]
- **Dan Hendrycks** (UC Berkeley) — MMLU (2020), the era's standard capability benchmark. [63]
- **Jonathan Ho, Prafulla Dhariwal & Alex Nichol** (Berkeley / OpenAI) — DDPM (2020), "Diffusion Models Beat GANs" (2021), GLIDE (2021): the diffusion headwaters. [82][83][84]
- **Jack Rae** (DeepMind) — led Gopher (2021), DeepMind's first 100B+ LM. [70]
- **Percy Liang & Rishi Bommasani** (Stanford CRFM) — foundation-models report (2021) and HELM (2022). [37][66]
- **Colin Raffel** (Google) — first author of T5 and the C4 corpus (2019). [30]
- **Alexey Dosovitskiy** (Google Brain, Berlin) — first author of the Vision Transformer (2020). [13]
- **John Jumper & Demis Hassabis** (DeepMind) — led AlphaFold 2 (CASP14 2020; Nature 2021); shared the 2024 Nobel Prize in Chemistry with David Baker. [14][15][45]
- **Jordan Hoffmann & Laurent Sifre** (DeepMind) — Chinchilla compute-optimal scaling (2022). [20]
- **Long Ouyang & Jan Leike** (OpenAI) — InstructGPT / RLHF paper (2022). [19]
- **Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, Margaret Mitchell** — "Stochastic Parrots" (FAccT 2021), the era's defining critique; Mitchell & Gebru also authored "Model Cards for Model Reporting" (Oct 2018); Gebru forced out of Google Dec 2020. [38][67][68]
- **Clément Delangue, Julien Chaumond, Thomas Wolf** (Hugging Face, founded 2016) — built the `transformers` library and model hub. [32][33]
- **Connor Leahy & EleutherAI collective** (formed 2020 on Discord) — The Pile, GPT-Neo, GPT-J: open GPT-3 replication. [22]
- **Jeff Dean & Noam Shazeer** (Google) — mixture-of-experts scaling (2017), Switch Transformer (2021), PaLM/Pathways (2022); Shazeer left in 2021 to co-found Character.AI. [27][34][23][88]

## Key papers / artifacts
- Vaswani, A. et al. *Attention Is All You Need*. NIPS 2017 (arXiv 1706.03762, 12 Jun 2017). https://arxiv.org/abs/1706.03762 [1]
- Peters, M. E. et al. *Deep contextualized word representations* (ELMo). NAACL 2018 (arXiv 1802.05365). https://arxiv.org/abs/1802.05365 [4]
- Radford, A., Narasimhan, K., Salimans, T., Sutskever, I. *Improving Language Understanding by Generative Pre-Training* (GPT-1). OpenAI, June 2018. https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf [5]
- Devlin, J., Chang, M.-W., Lee, K., Toutanova, K. *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding*. NAACL 2019 (arXiv 1810.04805, 11 Oct 2018). https://arxiv.org/abs/1810.04805 [7]
- Radford, A. et al. *Language Models are Unsupervised Multitask Learners* (GPT-2). OpenAI, Feb 2019. https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf [28]
- Raffel, C. et al. *Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer* (T5). JMLR 21, 2020 (arXiv 1910.10683). https://arxiv.org/abs/1910.10683 [30]
- Kaplan, J. et al. *Scaling Laws for Neural Language Models*. arXiv 2001.08361, 23 Jan 2020. https://arxiv.org/abs/2001.08361 [9]
- Brown, T. et al. *Language Models are Few-Shot Learners* (GPT-3). NeurIPS 2020 (arXiv 2005.14165, 28 May 2020). https://arxiv.org/abs/2005.14165 [11]
- Dosovitskiy, A. et al. *An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale* (ViT). ICLR 2021 (arXiv 2010.11929). https://arxiv.org/abs/2010.11929 [13]
- Jumper, J. et al. *Highly accurate protein structure prediction with AlphaFold*. Nature 596, 2021. https://www.nature.com/articles/s41586-021-03819-2 [15]
- Radford, A. et al. *Learning Transferable Visual Models From Natural Language Supervision* (CLIP). ICML 2021 (arXiv 2103.00020). https://arxiv.org/abs/2103.00020 [17]
- Ramesh, A. et al. *Zero-Shot Text-to-Image Generation* (DALL-E). ICML 2021 (arXiv 2102.12092). https://arxiv.org/abs/2102.12092 [16]
- Chen, M. et al. *Evaluating Large Language Models Trained on Code* (Codex). arXiv 2107.03374, 7 Jul 2021. https://arxiv.org/abs/2107.03374 [18]
- Bommasani, R. et al. *On the Opportunities and Risks of Foundation Models*. Stanford CRFM, arXiv 2108.07258, 2021. https://arxiv.org/abs/2108.07258 [37]
- Bender, E. M., Gebru, T., McMillan-Major, A., Mitchell, M. *On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?* FAccT 2021. https://en.wikipedia.org/wiki/Stochastic_parrot [38]
- Wei, J. et al. *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*. NeurIPS 2022 (arXiv 2201.11903). https://arxiv.org/abs/2201.11903 [39]
- Ouyang, L. et al. *Training language models to follow instructions with human feedback* (InstructGPT). NeurIPS 2022 (arXiv 2203.02155, 4 Mar 2022). https://arxiv.org/abs/2203.02155 [19]
- Hoffmann, J. et al. *Training Compute-Optimal Large Language Models* (Chinchilla). NeurIPS 2022 (arXiv 2203.15556, 29 Mar 2022). https://arxiv.org/abs/2203.15556 [20]
- Chowdhery, A. et al. *PaLM: Scaling Language Modeling with Pathways*. arXiv 2204.02311, 5 Apr 2022. https://arxiv.org/abs/2204.02311 [23]
- Wang, A., Singh, A., Michael, J., Hill, F., Levy, O., Bowman, S. R. *GLUE: A Multi-Task Benchmark and Analysis Platform for Natural Language Understanding*. ICLR 2019 (arXiv 1804.07461). https://arxiv.org/abs/1804.07461 [47]
- Sutton, R. *The Bitter Lesson*. Essay, 13 Mar 2019. http://www.incompleteideas.net/IncIdeas/BitterLesson.html [49]
- Liu, Y. et al. *RoBERTa: A Robustly Optimized BERT Pretraining Approach*. arXiv 1907.11692, Jul 2019. https://arxiv.org/abs/1907.11692 [54]
- Shoeybi, M. et al. *Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism*. arXiv 1909.08053, Sep 2019. https://arxiv.org/abs/1909.08053 [57]
- Ho, J., Jain, A., Abbeel, P. *Denoising Diffusion Probabilistic Models*. NeurIPS 2020 (arXiv 2006.11239). https://arxiv.org/abs/2006.11239 [82]
- Hendrycks, D. et al. *Measuring Massive Multitask Language Understanding* (MMLU). ICLR 2021 (arXiv 2009.03300). https://arxiv.org/abs/2009.03300 [63]
- Rae, J. W. et al. *Scaling Language Models: Methods, Analysis & Insights from Training Gopher*. arXiv 2112.11446, Dec 2021. https://arxiv.org/abs/2112.11446 [70]
- Zhang, S. et al. *OPT: Open Pre-trained Transformer Language Models*. arXiv 2205.01068, May 2022. https://arxiv.org/abs/2205.01068 [72]
- Wei, J. et al. *Emergent Abilities of Large Language Models*. TMLR 2022 (arXiv 2206.07682). https://arxiv.org/abs/2206.07682 [65]
- Liang, P. et al. *Holistic Evaluation of Language Models* (HELM). arXiv 2211.09110, Nov 2022. https://arxiv.org/abs/2211.09110 [66]
- Hugging Face. *Transformers* library (GitHub). https://github.com/huggingface/transformers [32]

## Schools of thought / sub-clusters
- **Encoder camp (BERT lineage)** — bidirectional masked-LM pre-training for understanding tasks (BERT, XLNet, RoBERTa, DistilBERT, T5's encoder side), scored on GLUE/SuperGLUE; dominant in search and industrial NLP 2018–2021; borders: statistical/neural NLP of 2010–2016 to the west (word2vec, ULMFiT, ELMo), retrieval-augmented generation (Lewis et al. 2020, RETRO 2021) to the east. [4][7][30][46][47][48][53][54][55][71][89]
- **Decoder / generative camp (GPT lineage)** — autoregressive next-token prediction at ever-larger scale (GPT-1/2/3, Codex); wins the era by turning scale into in-context learning; borders: RLHF/InstructGPT and ChatGPT to the east (file 08). [5][11][19][28]
- **Scaling-law empiricists** — Sutton's "Bitter Lesson" (2019) as creed, Kaplan (2020), Gopher (2021) and Chinchilla (2022) as method: capability as a function of compute, measured on MMLU/BIG-bench and debated as "emergence" (2022); borders: hardware/compute river (TPUs, A100/H100) and the compute-governance debate of file 08. [9][20][49][63][64][65][70]
- **Sparse / mixture-of-experts engineers** — Shazeer's MoE layer (2017), GShard (2020), Switch Transformer (2021), BAAI's Wu Dao 2.0 (2021); borders: Mixtral and DeepSeek in file 08. [27][34][74][93]
- **Systems & infrastructure engineers** — Megatron-LM tensor parallelism (Nvidia 2019), ZeRO/DeepSpeed (Microsoft 2019), the A100 (2020), Pathways/TPU v4 (Google 2022): the people who make 100B+ training runs possible; borders: hardware river (file 09d) to the south, the compute hinterland of file 08 to the east. [23][57][58][61]
- **Multimodal & scientific Transformers** — ViT, CLIP, DALL-E, AlphaFold 2, Perceiver, Flamingo, Gato, Whisper: attention as a universal substrate; the diffusion headwaters (DDPM 2020 → GLIDE 2021) rise on this bank; borders: computer-vision lineage (file 09g), diffusion/generative-media district in file 08, robotics VLA models. [13][14][16][17][40][42][80][81][82]
- **Alignment and critique tributaries** — RLHF (Christiano 2017 → InstructGPT 2022) and the Anthropic split (2021) on one bank; "Stochastic Parrots", model cards (2018), foundation-model risk reports and the Galactica backlash (Nov 2022) on the other; borders: AI safety/ethics river (file 09c) and the alignment plateau of file 08. [19][37][38][44][68][69][85]
- **Open-replication commons** — EleutherAI (The Pile, GPT-J, GPT-NeoX-20B), Meta's OPT-175B, BigScience BLOOM, Yandex YaLM-100B, Hugging Face hub; borders: the open-vs-closed road (file 09e), Llama/Mistral in file 08. [22][32][41][72][73][77]
- **National-champion scalers outside the Bay Area** — BAAI Wu Dao (Beijing), Huawei PanGu-α, Baidu ERNIE 3.0, Yandex YaLM, BigScience on France's Jean Zay: state- or platform-backed replies to GPT-3, 2021–22; borders: the Chinese shore (DeepSeek/Qwen) and European shore (Mistral) of file 08; China's 2017 national AI plan in file 06. [74][75][76][77][94]

## Map notes
- Suggested A1 label: **"The Transformer Plateau"** (alt. "Attention Highlands"). A2 countries: *Google/Brain-DeepMind* (BERT, T5, PaLM, AlphaFold, Chinchilla), *OpenAI* (GPT series, CLIP, DALL-E, Codex, InstructGPT), *the Open Commons* (Hugging Face, EleutherAI, BigScience). A3 cities: BERT, GPT-2, GPT-3, T5, ViT, CLIP, AlphaFold 2, Chinchilla, PaLM, Gopher, OPT-175B, BLOOM. Candidate A2 additions after review: *Microsoft–Nvidia systems axis* (Megatron, DeepSpeed, A100, Turing-NLG, the $1B OpenAI deal) and a *Chinese enclave* (BAAI/Wu Dao, PanGu, ERNIE) that becomes the Chinese shore of file 08.
- Rivers/borders/bridges: the **Attention River** rises at Bahdanau 2014 (deep-learning era) and becomes navigable at Vaswani 2017; the **Scaling Law fault line** (Kaplan 2020) is a sharp escarpment separating the "bigger is better" plateau from the RNN lowlands to the west; the **RLHF canal** (2017 preferences paper → InstructGPT 2022) is the crossing into the chatbot era; the **CLIP bridge** connects this continent to the diffusion/generative-media district.
- The eastern border with file 08 should be drawn at **30 November 2022 (ChatGPT release)** — technically nothing new, sociologically everything new.
- A **benchmark street** runs the length of the plateau (GLUE 2018 → SuperGLUE 2019 → MMLU 2020 → BIG-bench/HELM 2022) and should be drawn as one continuous A4 feature rather than scattered points; the **diffusion headwaters** (DDPM Jun 2020 → GLIDE Dec 2021) sit on this side of the CLIP bridge, with DALL-E 2 / Imagen / Stable Diffusion / Midjourney on the file-08 side.
- Open questions for curation: (1) whether AlphaFold 2 lives here or in a "science AI" enclave; (2) how much room to give the pre-2017 attention/seq2seq headwaters vs. the deep-learning file; (3) whether the GPT-2 staged-release controversy should be drawn as the first fort on the open-vs-closed road.

## Sources
[1] Attention Is All You Need — arXiv 1706.03762 — https://arxiv.org/abs/1706.03762 (accessed 2026-09-06)
[2] Wikipedia: Attention Is All You Need — https://en.wikipedia.org/wiki/Attention_Is_All_You_Need (accessed 2026-09-06)
[3] Wikipedia: Transformer (deep learning architecture) — https://en.wikipedia.org/wiki/Transformer_%28deep_learning_architecture%29 (accessed 2026-09-06)
[4] Deep contextualized word representations (ELMo) — arXiv 1802.05365 — https://arxiv.org/abs/1802.05365 (accessed 2026-09-06)
[5] Improving Language Understanding by Generative Pre-Training (GPT-1 paper PDF) — https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf (accessed 2026-09-06)
[6] Wikipedia: GPT-1 — https://en.wikipedia.org/wiki/GPT-1 (accessed 2026-09-06)
[7] BERT: Pre-training of Deep Bidirectional Transformers — arXiv 1810.04805 — https://arxiv.org/abs/1810.04805 (accessed 2026-09-06)
[8] Wikipedia: BERT (language model) — https://en.wikipedia.org/wiki/BERT_%28language_model%29 (accessed 2026-09-06)
[9] Scaling Laws for Neural Language Models — arXiv 2001.08361 — https://arxiv.org/abs/2001.08361 (accessed 2026-09-06)
[10] Wikipedia: Neural scaling law — https://en.wikipedia.org/wiki/Neural_scaling_law (accessed 2026-09-06)
[11] Language Models are Few-Shot Learners (GPT-3) — arXiv 2005.14165 — https://arxiv.org/abs/2005.14165 (accessed 2026-09-06)
[12] Wikipedia: GPT-3 — https://en.wikipedia.org/wiki/GPT-3 (accessed 2026-09-06)
[13] An Image is Worth 16x16 Words (ViT) — arXiv 2010.11929 — https://arxiv.org/abs/2010.11929 (accessed 2026-09-06)
[14] Wikipedia: AlphaFold — https://en.wikipedia.org/wiki/AlphaFold (accessed 2026-09-06)
[15] Highly accurate protein structure prediction with AlphaFold — Nature, 2021 — https://www.nature.com/articles/s41586-021-03819-2 (accessed 2026-09-06)
[16] Zero-Shot Text-to-Image Generation (DALL-E) — arXiv 2102.12092; Wikipedia: DALL-E — https://en.wikipedia.org/wiki/DALL-E (accessed 2026-09-06)
[17] Learning Transferable Visual Models From Natural Language Supervision (CLIP) — arXiv 2103.00020 — https://arxiv.org/abs/2103.00020 (accessed 2026-09-06)
[18] Evaluating Large Language Models Trained on Code (Codex) — arXiv 2107.03374 — https://arxiv.org/abs/2107.03374 (accessed 2026-09-06)
[19] Training language models to follow instructions with human feedback (InstructGPT) — arXiv 2203.02155 — https://arxiv.org/abs/2203.02155 (accessed 2026-09-06)
[20] Training Compute-Optimal Large Language Models (Chinchilla) — arXiv 2203.15556 — https://arxiv.org/abs/2203.15556 (accessed 2026-09-06)
[21] Wikipedia: Chinchilla (language model) — https://en.wikipedia.org/wiki/Chinchilla_%28language_model%29 (accessed 2026-09-06)
[22] Wikipedia: EleutherAI — https://en.wikipedia.org/wiki/EleutherAI (accessed 2026-09-06)
[23] PaLM: Scaling Language Modeling with Pathways — arXiv 2204.02311 — https://arxiv.org/abs/2204.02311 (accessed 2026-09-06)
[24] Neural Machine Translation by Jointly Learning to Align and Translate (Bahdanau, Cho, Bengio) — arXiv 1409.0473 — https://arxiv.org/abs/1409.0473 (accessed 2026-09-06)
[25] Sequence to Sequence Learning with Neural Networks (Sutskever, Vinyals, Le) — arXiv 1409.3215 — https://arxiv.org/abs/1409.3215 (accessed 2026-09-06)
[26] Wikipedia: Google Neural Machine Translation — https://en.wikipedia.org/wiki/Google_Neural_Machine_Translation (accessed 2026-09-06)
[27] Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer — arXiv 1701.06538 — https://arxiv.org/abs/1701.06538 (accessed 2026-09-06)
[28] Language Models are Unsupervised Multitask Learners (GPT-2 paper PDF) — https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf (accessed 2026-09-06)
[29] Wikipedia: GPT-2 — https://en.wikipedia.org/wiki/GPT-2 (accessed 2026-09-06)
[30] Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer (T5) — arXiv 1910.10683 — https://arxiv.org/abs/1910.10683 (accessed 2026-09-06)
[31] Wikipedia: T5 (language model) — https://en.wikipedia.org/wiki/T5_%28language_model%29 (accessed 2026-09-06)
[32] Hugging Face Transformers (GitHub) — https://github.com/huggingface/transformers (accessed 2026-09-06)
[33] Wikipedia: Hugging Face — https://en.wikipedia.org/wiki/Hugging_Face (accessed 2026-09-06)
[34] Switch Transformers: Scaling to Trillion Parameter Models — arXiv 2101.03961 — https://arxiv.org/abs/2101.03961 (accessed 2026-09-06)
[35] Wikipedia: LaMDA — https://en.wikipedia.org/wiki/LaMDA (accessed 2026-09-06)
[36] Introducing GitHub Copilot: your AI pair programmer — GitHub Blog, 29 Jun 2021 — https://github.blog/news-insights/product-news/introducing-github-copilot-ai-pair-programmer/ (accessed 2026-09-06)
[37] On the Opportunities and Risks of Foundation Models — arXiv 2108.07258 — https://arxiv.org/abs/2108.07258 (accessed 2026-09-06)
[38] Wikipedia: Stochastic parrot (Bender, Gebru, McMillan-Major, Mitchell, FAccT 2021) — https://en.wikipedia.org/wiki/Stochastic_parrot (accessed 2026-09-06)
[39] Chain-of-Thought Prompting Elicits Reasoning in Large Language Models — arXiv 2201.11903 — https://arxiv.org/abs/2201.11903 (accessed 2026-09-06)
[40] A Generalist Agent (Gato) — arXiv 2205.06175 — https://arxiv.org/abs/2205.06175 (accessed 2026-09-06)
[41] Introducing The World's Largest Open Multilingual Language Model: BLOOM — Hugging Face blog — https://huggingface.co/blog/bloom (accessed 2026-09-06)
[42] Robust Speech Recognition via Large-Scale Weak Supervision (Whisper) — arXiv 2212.04356; Wikipedia: Whisper (speech recognition system) — https://en.wikipedia.org/wiki/Whisper_%28speech_recognition_system%29 (accessed 2026-09-06)
[43] Wikipedia: Jared Kaplan — https://en.wikipedia.org/wiki/Jared_Kaplan (accessed 2026-09-06)
[44] Deep Reinforcement Learning from Human Preferences (Christiano et al., 2017) — arXiv 1706.03741 — https://arxiv.org/abs/1706.03741 (accessed 2026-09-06)
[45] Press release: The Nobel Prize in Chemistry 2024 (Baker, Hassabis, Jumper) — https://www.nobelprize.org/prizes/chemistry/2024/press-release/ (accessed 2026-09-06)
[46] Universal Language Model Fine-tuning for Text Classification (ULMFiT, Howard & Ruder) — arXiv 1801.06146 — https://arxiv.org/abs/1801.06146 (accessed 2026-09-06)
[47] GLUE: A Multi-Task Benchmark and Analysis Platform for Natural Language Understanding — arXiv 1804.07461 — https://arxiv.org/abs/1804.07461 (accessed 2026-09-06); GLUE Benchmark site — https://gluebenchmark.com/
[48] SuperGLUE: A Stickier Benchmark for General-Purpose Language Understanding Systems — arXiv 1905.00537 — https://arxiv.org/abs/1905.00537 (accessed 2026-09-06)
[49] Sutton, R., The Bitter Lesson (13 Mar 2019) — http://www.incompleteideas.net/IncIdeas/BitterLesson.html (accessed 2026-09-06)
[50] Wikipedia: Bitter lesson — https://en.wikipedia.org/wiki/Bitter_lesson (accessed 2026-09-06)
[51] Wikipedia: OpenAI (2019 capped-profit restructuring; Microsoft $1B) — https://en.wikipedia.org/wiki/OpenAI (accessed 2026-09-06)
[52] OpenAI forms exclusive computing partnership with Microsoft — Microsoft News, 22 Jul 2019 — https://news.microsoft.com/source/2019/07/22/openai-forms-exclusive-computing-partnership-with-microsoft-to-build-new-azure-ai-supercomputing-technologies/ (accessed 2026-09-06)
[53] XLNet: Generalized Autoregressive Pretraining for Language Understanding — arXiv 1906.08237 — https://arxiv.org/abs/1906.08237 (accessed 2026-09-06); Wikipedia: XLNet — https://en.wikipedia.org/wiki/XLNet
[54] RoBERTa: A Robustly Optimized BERT Pretraining Approach — arXiv 1907.11692 — https://arxiv.org/abs/1907.11692 (accessed 2026-09-06)
[55] DistilBERT, a distilled version of BERT — arXiv 1910.01108 — https://arxiv.org/abs/1910.01108 (accessed 2026-09-06)
[56] Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context — arXiv 1901.02860 — https://arxiv.org/abs/1901.02860 (accessed 2026-09-06)
[57] Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism — arXiv 1909.08053 — https://arxiv.org/abs/1909.08053 (accessed 2026-09-06); GitHub — https://github.com/NVIDIA/Megatron-LM
[58] ZeRO: Memory Optimizations Toward Training Trillion Parameter Models — arXiv 1910.02054 — https://arxiv.org/abs/1910.02054 (accessed 2026-09-06); DeepSpeed (GitHub) — https://github.com/deepspeedai/DeepSpeed
[59] Turing-NLG: A 17-billion-parameter language model by Microsoft — Microsoft Research blog, 13 Feb 2020 — https://www.microsoft.com/en-us/research/blog/turing-nlg-a-17-billion-parameter-language-model-by-microsoft/ (accessed 2026-09-06)
[60] Using DeepSpeed and Megatron to Train Megatron-Turing NLG 530B — arXiv 2201.11990 — https://arxiv.org/abs/2201.11990 (accessed 2026-09-06)
[61] Wikipedia: Ampere (microarchitecture) (A100, announced 14 May 2020) — https://en.wikipedia.org/wiki/Ampere_%28microarchitecture%29 (accessed 2026-09-06)
[62] NVIDIA Ampere Architecture In-Depth — NVIDIA Technical Blog, 14 May 2020 — https://developer.nvidia.com/blog/nvidia-ampere-architecture-in-depth/ (accessed 2026-09-06)
[63] Measuring Massive Multitask Language Understanding (MMLU) — arXiv 2009.03300 — https://arxiv.org/abs/2009.03300 (accessed 2026-09-06); Wikipedia: MMLU — https://en.wikipedia.org/wiki/MMLU
[64] Beyond the Imitation Game: Quantifying and extrapolating the capabilities of language models (BIG-bench) — arXiv 2206.04615 — https://arxiv.org/abs/2206.04615 (accessed 2026-09-06); GitHub — https://github.com/google/BIG-bench
[65] Emergent Abilities of Large Language Models — arXiv 2206.07682 — https://arxiv.org/abs/2206.07682 (accessed 2026-09-06)
[66] Holistic Evaluation of Language Models (HELM) — arXiv 2211.09110 — https://arxiv.org/abs/2211.09110 (accessed 2026-09-06); Stanford CRFM HELM — https://crfm.stanford.edu/helm/
[67] Wikipedia: Timnit Gebru (departure from Google, Dec 2020) — https://en.wikipedia.org/wiki/Timnit_Gebru (accessed 2026-09-06)
[68] Model Cards for Model Reporting (Mitchell et al., Oct 2018) — arXiv 1810.03993 — https://arxiv.org/abs/1810.03993 (accessed 2026-09-06)
[69] Wikipedia: Anthropic (founded Jan 2021) — https://en.wikipedia.org/wiki/Anthropic (accessed 2026-09-06)
[70] Scaling Language Models: Methods, Analysis & Insights from Training Gopher — arXiv 2112.11446 — https://arxiv.org/abs/2112.11446 (accessed 2026-09-06); DeepMind blog, 8 Dec 2021 — https://deepmind.google/blog/language-modelling-at-scale-gopher-ethical-considerations-and-retrieval/
[71] Improving language models by retrieving from trillions of tokens (RETRO) — arXiv 2112.04426 — https://arxiv.org/abs/2112.04426 (accessed 2026-09-06)
[72] OPT: Open Pre-trained Transformer Language Models — arXiv 2205.01068 — https://arxiv.org/abs/2205.01068 (accessed 2026-09-06); Meta AI blog, 3 May 2022 — https://ai.meta.com/blog/democratizing-access-to-large-scale-language-models-with-opt-175b/
[73] GPT-NeoX-20B: An Open-Source Autoregressive Language Model — arXiv 2204.06745 — https://arxiv.org/abs/2204.06745 (accessed 2026-09-06); GitHub — https://github.com/EleutherAI/gpt-neox
[74] Wikipedia: Wu Dao (BAAI; Wu Dao 2.0 announced 31 May 2021) — https://en.wikipedia.org/wiki/Wu_Dao (accessed 2026-09-06)
[75] PanGu-α: Large-scale Autoregressive Pretrained Chinese Language Models — arXiv 2104.12369 — https://arxiv.org/abs/2104.12369 (accessed 2026-09-06)
[76] ERNIE 3.0: Large-scale Knowledge Enhanced Pre-training for Language Understanding and Generation — arXiv 2107.02137 — https://arxiv.org/abs/2107.02137 (accessed 2026-09-06)
[77] YaLM-100B: Pretrained language model with 100B parameters (Yandex, GitHub, repository created 22 Jun 2022) — https://github.com/yandex/YaLM-100B (accessed 2026-09-06)
[78] Competition-Level Code Generation with AlphaCode — arXiv 2203.07814 — https://arxiv.org/abs/2203.07814 (accessed 2026-09-06); DeepMind blog, 2 Feb 2022 — https://deepmind.google/blog/competitive-programming-with-alphacode/
[79] Solving Quantitative Reasoning Problems with Language Models (Minerva) — arXiv 2206.14858 — https://arxiv.org/abs/2206.14858 (accessed 2026-09-06)
[80] Flamingo: a Visual Language Model for Few-Shot Learning — arXiv 2204.14198 — https://arxiv.org/abs/2204.14198 (accessed 2026-09-06)
[81] Perceiver: General Perception with Iterative Attention — arXiv 2103.03206 — https://arxiv.org/abs/2103.03206 (accessed 2026-09-06); Wikipedia: Perceiver — https://en.wikipedia.org/wiki/Perceiver
[82] Denoising Diffusion Probabilistic Models (Ho, Jain, Abbeel) — arXiv 2006.11239 — https://arxiv.org/abs/2006.11239 (accessed 2026-09-06)
[83] Diffusion Models Beat GANs on Image Synthesis (Dhariwal & Nichol) — arXiv 2105.05233 — https://arxiv.org/abs/2105.05233 (accessed 2026-09-06)
[84] GLIDE: Towards Photorealistic Image Generation and Editing with Text-Guided Diffusion Models — arXiv 2112.10741 — https://arxiv.org/abs/2112.10741 (accessed 2026-09-06)
[85] Galactica: A Large Language Model for Science — arXiv 2211.09085 — https://arxiv.org/abs/2211.09085 (accessed 2026-09-06)
[86] Why Meta's latest large language model only survived three days online — MIT Technology Review, 18 Nov 2022 — https://www.technologyreview.com/2022/11/18/1063487/meta-large-language-model-ai-only-survived-three-days-gpt-3-science/ (accessed 2026-09-06)
[87] Towards a Human-like Open-Domain Chatbot (Meena) — arXiv 2001.09977 — https://arxiv.org/abs/2001.09977 (accessed 2026-09-06)
[88] Wikipedia: Character.ai (founded Nov 2021; beta 16 Sep 2022) — https://en.wikipedia.org/wiki/Character.ai (accessed 2026-09-06)
[89] Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (Lewis et al.) — arXiv 2005.11401 — https://arxiv.org/abs/2005.11401 (accessed 2026-09-06)
[90] Wikipedia: GitHub Copilot (GA 21 Jun 2022; lawsuit Nov 2022) — https://en.wikipedia.org/wiki/GitHub_Copilot (accessed 2026-09-06)
[91] Finetuned Language Models Are Zero-Shot Learners (FLAN) — arXiv 2109.01652 — https://arxiv.org/abs/2109.01652 (accessed 2026-09-06)
[92] Multitask Prompted Training Enables Zero-Shot Task Generalization (T0) — arXiv 2110.08207 — https://arxiv.org/abs/2110.08207 (accessed 2026-09-06)
[93] GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding — arXiv 2006.16668 — https://arxiv.org/abs/2006.16668 (accessed 2026-09-06)
[94] Wikipedia: BLOOM (language model) (Jean Zay, Mar–Jul 2022) — https://en.wikipedia.org/wiki/BLOOM_%28language_model%29 (accessed 2026-09-06)
[95] Micikevicius et al., Mixed Precision Training — arXiv 1710.03740 (10 Oct 2017) — https://arxiv.org/abs/1710.03740 (accessed 2026-09-23)
[96] Brundage et al., The Malicious Use of Artificial Intelligence: Forecasting, Prevention, and Mitigation — arXiv 1802.07228 (20 Feb 2018) — https://arxiv.org/abs/1802.07228 (accessed 2026-09-23)
[97] Gebru et al., Datasheets for Datasets — arXiv 1803.09010 (23 Mar 2018) — https://arxiv.org/abs/1803.09010 (accessed 2026-09-23)
[98] GitHub, jax-ml/jax repository (created 25 Oct 2018 per GitHub API; composable transformations of NumPy programs, JIT to GPU/TPU) — https://github.com/jax-ml/jax (accessed 2026-09-23)
[99] Huang et al., GPipe: Efficient Training of Giant Neural Networks using Pipeline Parallelism — arXiv 1811.06965 (16 Nov 2018) — https://arxiv.org/abs/1811.06965 (accessed 2026-09-23)
[100] Houlsby et al., Parameter-Efficient Transfer Learning for NLP — arXiv 1902.00751 (2 Feb 2019) — https://arxiv.org/abs/1902.00751 (accessed 2026-09-23)
[101] Child et al., Generating Long Sequences with Sparse Transformers — arXiv 1904.10509 (23 Apr 2019) — https://arxiv.org/abs/1904.10509 (accessed 2026-09-23)
[102] Strubell et al., Energy and Policy Considerations for Deep Learning in NLP — arXiv 1906.02243 (5 Jun 2019) — https://arxiv.org/abs/1906.02243 (accessed 2026-09-23)
[103] Reimers et al., Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks — arXiv 1908.10084 (27 Aug 2019) — https://arxiv.org/abs/1908.10084 (accessed 2026-09-23)
[104] Lan et al., ALBERT: A Lite BERT for Self-supervised Learning of Language Representations — arXiv 1909.11942 (26 Sep 2019) — https://arxiv.org/abs/1909.11942 (accessed 2026-09-23)
[105] Lewis et al., BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension — arXiv 1910.13461 (29 Oct 2019) — https://arxiv.org/abs/1910.13461 (accessed 2026-09-23)
[106] Conneau et al., Unsupervised Cross-lingual Representation Learning at Scale — arXiv 1911.02116 (5 Nov 2019) — https://arxiv.org/abs/1911.02116 (accessed 2026-09-23)
[107] Keskar et al., CTRL: A Conditional Transformer Language Model for Controllable Generation — arXiv 1909.05858 (11 Sep 2019) — https://arxiv.org/abs/1909.05858 (accessed 2026-09-23)
[108] Zhang et al., DialoGPT: Large-Scale Generative Pre-training for Conversational Response Generation — arXiv 1911.00536 (1 Nov 2019) — https://arxiv.org/abs/1911.00536 (accessed 2026-09-23)
[109] Wolf et al., HuggingFace's Transformers: State-of-the-art Natural Language Processing — arXiv 1910.03771 (9 Oct 2019) — https://arxiv.org/abs/1910.03771 (accessed 2026-09-23)
[110] He et al., Momentum Contrast for Unsupervised Visual Representation Learning — arXiv 1911.05722 (13 Nov 2019) — https://arxiv.org/abs/1911.05722 (accessed 2026-09-23)
[111] Nakkiran et al., Deep Double Descent: Where Bigger Models and More Data Hurt — arXiv 1912.02292 (4 Dec 2019) — https://arxiv.org/abs/1912.02292 (accessed 2026-09-23)
[112] Kitaev et al., Reformer: The Efficient Transformer — arXiv 2001.04451 (13 Jan 2020) — https://arxiv.org/abs/2001.04451 (accessed 2026-09-23)
[113] Beltagy et al., Longformer: The Long-Document Transformer — arXiv 2004.05150 (10 Apr 2020) — https://arxiv.org/abs/2004.05150 (accessed 2026-09-23)
[114] Choromanski et al., Rethinking Attention with Performers — arXiv 2009.14794 (30 Sep 2020) — https://arxiv.org/abs/2009.14794 (accessed 2026-09-23)
[115] Guu et al., REALM: Retrieval-Augmented Language Model Pre-Training — arXiv 2002.08909 (10 Feb 2020) — https://arxiv.org/abs/2002.08909 (accessed 2026-09-23)
[116] Karpukhin et al., Dense Passage Retrieval for Open-Domain Question Answering — arXiv 2004.04906 (10 Apr 2020) — https://arxiv.org/abs/2004.04906 (accessed 2026-09-23)
[117] Chen et al., A Simple Framework for Contrastive Learning of Visual Representations — arXiv 2002.05709 (13 Feb 2020) — https://arxiv.org/abs/2002.05709 (accessed 2026-09-23)
[118] Grill et al., Bootstrap your own latent: A new approach to self-supervised Learning — arXiv 2006.07733 (13 Jun 2020) — https://arxiv.org/abs/2006.07733 (accessed 2026-09-23)
[119] Clark et al., ELECTRA: Pre-training Text Encoders as Discriminators Rather Than Generators — arXiv 2003.10555 (23 Mar 2020) — https://arxiv.org/abs/2003.10555 (accessed 2026-09-23)
[120] Roller et al., Recipes for building an open-domain chatbot — arXiv 2004.13637 (28 Apr 2020) — https://arxiv.org/abs/2004.13637 (accessed 2026-09-23)
[121] Carion et al., End-to-End Object Detection with Transformers — arXiv 2005.12872 (26 May 2020) — https://arxiv.org/abs/2005.12872 (accessed 2026-09-23)
[122] Baevski et al., wav2vec 2.0: A Framework for Self-Supervised Learning of Speech Representations — arXiv 2006.11477 (20 Jun 2020) — https://arxiv.org/abs/2006.11477 (accessed 2026-09-23)
[123] Henighan et al., Scaling Laws for Autoregressive Generative Modeling — arXiv 2010.14701 (28 Oct 2020) — https://arxiv.org/abs/2010.14701 (accessed 2026-09-23)
[124] Li et al., Prefix-Tuning: Optimizing Continuous Prompts for Generation — arXiv 2101.00190 (1 Jan 2021) — https://arxiv.org/abs/2101.00190 (accessed 2026-09-23)
[125] Lester et al., The Power of Scale for Parameter-Efficient Prompt Tuning — arXiv 2104.08691 (18 Apr 2021) — https://arxiv.org/abs/2104.08691 (accessed 2026-09-23)
[126] Liu et al., Swin Transformer: Hierarchical Vision Transformer using Shifted Windows — arXiv 2103.14030 (25 Mar 2021) — https://arxiv.org/abs/2103.14030 (accessed 2026-09-23)
[127] Caron et al., Emerging Properties in Self-Supervised Vision Transformers — arXiv 2104.14294 (29 Apr 2021) — https://arxiv.org/abs/2104.14294 (accessed 2026-09-23)
[128] Chen et al., Decision Transformer: Reinforcement Learning via Sequence Modeling — arXiv 2106.01345 (2 Jun 2021) — https://arxiv.org/abs/2106.01345 (accessed 2026-09-23)
[129] Hu et al., LoRA: Low-Rank Adaptation of Large Language Models — arXiv 2106.09685 (17 Jun 2021) — https://arxiv.org/abs/2106.09685 (accessed 2026-09-23)
[130] Lin et al., TruthfulQA: Measuring How Models Mimic Human Falsehoods — arXiv 2109.07958 (8 Sep 2021) — https://arxiv.org/abs/2109.07958 (accessed 2026-09-23)
[131] Cobbe et al., Training Verifiers to Solve Math Word Problems — arXiv 2110.14168 (27 Oct 2021) — https://arxiv.org/abs/2110.14168 (accessed 2026-09-23)
[132] Schuhmann et al., LAION-400M: Open Dataset of CLIP-Filtered 400 Million Image-Text Pairs — arXiv 2111.02114 (3 Nov 2021) — https://arxiv.org/abs/2111.02114 (accessed 2026-09-23)
[133] Schuhmann et al., LAION-5B: An open large-scale dataset for training next generation image-text models — arXiv 2210.08402 (16 Oct 2022) — https://arxiv.org/abs/2210.08402 (accessed 2026-09-23)
[134] He et al., Masked Autoencoders Are Scalable Vision Learners — arXiv 2111.06377 (11 Nov 2021) — https://arxiv.org/abs/2111.06377 (accessed 2026-09-23)
[135] Du et al., GLaM: Efficient Scaling of Language Models with Mixture-of-Experts — arXiv 2112.06905 (13 Dec 2021) — https://arxiv.org/abs/2112.06905 (accessed 2026-09-23)
[136] Nakano et al., WebGPT: Browser-assisted question-answering with human feedback — arXiv 2112.09332 (17 Dec 2021) — https://arxiv.org/abs/2112.09332 (accessed 2026-09-23)
[137] Thoppilan et al., LaMDA: Language Models for Dialog Applications — arXiv 2201.08239 (20 Jan 2022) — https://arxiv.org/abs/2201.08239 (accessed 2026-09-23)
[138] Perez et al., Red Teaming Language Models with Language Models — arXiv 2202.03286 (7 Feb 2022) — https://arxiv.org/abs/2202.03286 (accessed 2026-09-23)
[139] Wang et al., Self-Consistency Improves Chain of Thought Reasoning in Language Models — arXiv 2203.11171 (21 Mar 2022) — https://arxiv.org/abs/2203.11171 (accessed 2026-09-23)
[140] Kojima et al., Large Language Models are Zero-Shot Reasoners — arXiv 2205.11916 (24 May 2022) — https://arxiv.org/abs/2205.11916 (accessed 2026-09-23)
[141] Ahn et al., Do As I Can, Not As I Say: Grounding Language in Robotic Affordances — arXiv 2204.01691 (4 Apr 2022) — https://arxiv.org/abs/2204.01691 (accessed 2026-09-23)
[142] Bai et al., Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback — arXiv 2204.05862 (12 Apr 2022) — https://arxiv.org/abs/2204.05862 (accessed 2026-09-23)
[143] Saharia et al., Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding — arXiv 2205.11487 (23 May 2022) — https://arxiv.org/abs/2205.11487 (accessed 2026-09-23)
[144] Yu et al., Scaling Autoregressive Models for Content-Rich Text-to-Image Generation — arXiv 2206.10789 (22 Jun 2022) — https://arxiv.org/abs/2206.10789 (accessed 2026-09-23)
[145] Tay et al., UL2: Unifying Language Learning Paradigms — arXiv 2205.05131 (10 May 2022) — https://arxiv.org/abs/2205.05131 (accessed 2026-09-23)
[146] Dao et al., FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness — arXiv 2205.14135 (27 May 2022) — https://arxiv.org/abs/2205.14135 (accessed 2026-09-23)
[147] Zeng et al., GLM-130B: An Open Bilingual Pre-trained Model — arXiv 2210.02414 (5 Oct 2022) — https://arxiv.org/abs/2210.02414 (accessed 2026-09-23)
[148] Chung et al., Scaling Instruction-Finetuned Language Models — arXiv 2210.11416 (20 Oct 2022) — https://arxiv.org/abs/2210.11416 (accessed 2026-09-23)
