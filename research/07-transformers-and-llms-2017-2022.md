# Transformers and Large Language Models (2017–2022)

> **Status:** verified
> **Date range:** 2017–2022
> **Map placement (proposed):** X = 2017–2022; Y = connectionist/scaling pole (with a thin "alignment" tributary emerging at the eastern edge)
> **Altitude:** A1 continent ("The Transformer Plateau"), A2 country (Google/Brain, OpenAI, DeepMind, Hugging Face, EleutherAI), A3 city (BERT, GPT-2, GPT-3, T5, ViT, CLIP, AlphaFold 2, Chinchilla), A4 street (scaling-law papers, benchmarks, tokenizers)

## One-paragraph summary
In June 2017 eight Google researchers published "Attention Is All You Need", replacing recurrence with self-attention and giving deep learning a highly parallelisable sequence architecture: the Transformer [1][2]. Within eighteen months two pre-train-then-fine-tune recipes built on it — OpenAI's decoder-only GPT (June 2018) and Google's encoder-only BERT (October 2018) — swept NLP benchmarks and made "pretrained language model" the default starting point for any text task [4][5][6][7]. The era's central discovery was empirical rather than architectural: model quality improves smoothly and predictably with parameters, data and compute (Kaplan et al., January 2020), which justified GPT-3's 175-billion-parameter bet (May 2020) and its surprising few-shot, in-context learning [9][10][11]. The same architecture then crossed modalities — Vision Transformer (2020), CLIP and DALL-E (January 2021), AlphaFold 2's protein-structure breakthrough (CASP14, November 2020; Nature, July 2021), Codex/Copilot for code (2021) — while DeepMind's Chinchilla (March 2022) corrected the scaling recipe toward more data per parameter [12][13][14][15][17][20]. The period ends with the ingredients of the chatbot age assembled but not yet released to the public: InstructGPT's reinforcement learning from human feedback (March 2022), PaLM's 540B parameters and chain-of-thought reasoning (April 2022), and open-weights counter-movements (EleutherAI, BLOOM) that foreshadow the open-vs-closed rift of the next era [18][19][21][22][23].

## Timeline of key events
| Year | Event | Why it matters | Source |
|------|-------|----------------|--------|
| 2014 | Bahdanau, Cho & Bengio introduce attention for neural machine translation; Sutskever et al. publish seq2seq (Sept 2014) | Encoder–decoder + attention is the direct ancestor of the Transformer | [24][25] |
| 2016 (Nov) | Google Neural Machine Translation goes live in Google Translate | Shows neural sequence models at production scale; sets the stage for replacing RNNs | [26] |
| 2017 (Jan) | Shazeer et al., "Outrageously Large Neural Networks" — sparsely-gated mixture-of-experts layer (arXiv 1701.06538, 23 Jan 2017) | MoE at 100B+ parameters; the technique later returns in Switch Transformer, Mixtral, DeepSeek | [27] |
| 2017 (12 Jun) | Vaswani et al., "Attention Is All You Need" (arXiv 1706.03762); published at NIPS 2017 | Introduces the Transformer; all eight authors are Google employees at the time | [1][2][3] |
| 2018 (15 Feb) | Peters et al., ELMo — deep contextualised word representations (arXiv 1802.05365; NAACL 2018) | Contextual embeddings from a bidirectional LSTM; the last big pre-Transformer NLP win | [4] |
| 2018 (Jun) | OpenAI releases GPT-1 paper "Improving Language Understanding by Generative Pre-Training" (117M parameters) | Decoder-only Transformer + generative pre-training + task fine-tuning | [5][6] |
| 2018 (11 Oct) | Devlin et al., BERT (arXiv 1810.04805); state of the art on GLUE, SQuAD v1.1/v2.0, SWAG | Encoder-only bidirectional pre-training; becomes the workhorse of industrial NLP and Google Search | [7][8] |
| 2019 (Feb) | OpenAI announces GPT-2 (1.5B parameters, trained on 8M web pages) but initially withholds the full model; 774M released 20 Aug, full 1.5B on 5 Nov 2019 | First "too dangerous to release" staged-release controversy; zero-shot task transfer | [28][29] |
| 2019 (23 Oct) | Raffel et al., T5 "Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer" (arXiv 1910.10683); introduces the C4 corpus | Casts every NLP task as text-to-text; systematic study of transfer-learning design choices | [30][31] |
| 2019 | Hugging Face's `transformers` library (open-source) becomes the de facto hub for sharing pretrained Transformer models | Open distribution layer for the whole era; company founded 2016 in New York | [32][33] |
| 2020 (23 Jan) | Kaplan et al., "Scaling Laws for Neural Language Models" (arXiv 2001.08361) | Loss falls as a power law in parameters, data and compute; makes scale a research strategy | [9][10] |
| 2020 (28 May) | Brown et al., GPT-3, "Language Models are Few-Shot Learners" (arXiv 2005.14165), 175B parameters; API access announced 11 Jun 2020 | In-context/few-shot learning without gradient updates; first LLM sold as an API | [11][12] |
| 2020 (22 Oct) | Dosovitskiy et al., Vision Transformer, "An Image is Worth 16x16 Words" (arXiv 2010.11929; ICLR 2021) | Transformers displace CNNs at the top of image classification | [13] |
| 2020 (30 Nov) | AlphaFold 2 wins CASP14 with GDT scores above 90 for roughly two-thirds of targets | Attention-based model solves a 50-year grand challenge in biology; Nature paper follows July 2021 | [14][15] |
| 2020 (31 Dec) | EleutherAI releases The Pile (825 GB open training corpus); GPT-Neo/GPT-J follow in 2021 | Grassroots open replication of GPT-3-class models begins | [22] |
| 2021 (5 Jan) | OpenAI announces DALL-E (text-to-image, 12B-parameter GPT-3 variant) and CLIP (contrastive image–text pre-training) | Language-supervised vision; CLIP becomes the conditioning backbone for later diffusion models | [16][17] |
| 2021 (11 Jan) | Fedus, Zoph & Shazeer, Switch Transformer (arXiv 2101.03961) — trillion-parameter sparse MoE | Demonstrates sparsity as a route past dense scaling limits | [34] |
| 2021 (18 May) | Google announces LaMDA at I/O 2021 | Dialogue-specialised LLM; June 2022 Lemoine "sentience" episode previews public reaction to chatbots | [35] |
| 2021 (29 Jun) | GitHub Copilot technical preview, powered by OpenAI Codex (Codex paper arXiv 2107.03374, 7 Jul 2021) | First mass-market LLM product; code generation becomes a flagship use case | [18][36] |
| 2021 (16 Aug) | Stanford CRFM, "On the Opportunities and Risks of Foundation Models" (arXiv 2108.07258) | Coins "foundation model" as the umbrella term for large pretrained models | [37] |
| 2021 (Mar) | Bender, Gebru, McMillan-Major & Mitchell, "On the Dangers of Stochastic Parrots" (FAccT 2021) | Landmark critique of LLM scale, data and environmental cost; Gebru's exit from Google | [38] |
| 2022 (28 Jan) | Wei et al., "Chain-of-Thought Prompting Elicits Reasoning" (arXiv 2201.11903) | Shows step-by-step prompting unlocks multi-step reasoning in large models | [39] |
| 2022 (4 Mar) | Ouyang et al., InstructGPT, "Training language models to follow instructions with human feedback" (arXiv 2203.02155) | RLHF recipe (SFT → reward model → PPO) that ChatGPT will use eight months later | [19] |
| 2022 (29 Mar) | Hoffmann et al., Chinchilla, "Training Compute-Optimal Large Language Models" (arXiv 2203.15556): 70B params on 1.4T tokens beats 280B Gopher | Revises scaling laws: models had been under-trained on data | [20][21] |
| 2022 (5 Apr) | Chowdhery et al., PaLM (arXiv 2204.02311), 540B parameters trained on Pathways/TPU v4 pods | Largest dense LM of the era; strong chain-of-thought results | [23] |
| 2022 (12 May) | DeepMind's Gato (arXiv 2205.06175) — a single Transformer for text, images, Atari and robot arms | Early "generalist agent" claim; bridge to embodied/agentic era | [40] |
| 2022 (Jul) | BigScience releases BLOOM (176B, open, multilingual) via Hugging Face | Largest open-access LLM of the period; open-science counterweight to GPT-3 | [41] |
| 2022 (Sep) | OpenAI open-sources Whisper speech recognition (arXiv 2212.04356) | Transformer conquers speech; notable as an OpenAI open-weights release | [42] |

## Key people
- **Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan Gomez, Łukasz Kaiser, Illia Polosukhin** (Google Brain / Google Research, 2017) — the eight "equal contribution" authors of the Transformer paper; all eight later left Google for startups. [2][3]
- **Alec Radford** (OpenAI) — first author of GPT-1 (2018) and GPT-2 (2019); also led CLIP and Whisper. [5][28][17]
- **Jacob Devlin** (Google AI Language) — first author of BERT (2018). [7]
- **Jared Kaplan** (Johns Hopkins / OpenAI) — co-authored "Scaling Laws for Neural Language Models" (2020); later an Anthropic co-founder. [9][43]
- **Tom Brown & Dario Amodei** (OpenAI) — led the 31-author GPT-3 paper (2020); Amodei's team also wrote the RLHF-precursor "Deep RL from Human Preferences" (2017). [11][44]
- **Colin Raffel** (Google) — first author of T5 and the C4 corpus (2019). [30]
- **Alexey Dosovitskiy** (Google Brain, Berlin) — first author of the Vision Transformer (2020). [13]
- **John Jumper & Demis Hassabis** (DeepMind) — led AlphaFold 2 (CASP14 2020; Nature 2021); shared the 2024 Nobel Prize in Chemistry with David Baker. [14][15][45]
- **Jordan Hoffmann & Laurent Sifre** (DeepMind) — Chinchilla compute-optimal scaling (2022). [20]
- **Long Ouyang & Jan Leike** (OpenAI) — InstructGPT / RLHF paper (2022). [19]
- **Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, Margaret Mitchell** — "Stochastic Parrots" (FAccT 2021), the era's defining critique. [38]
- **Clément Delangue, Julien Chaumond, Thomas Wolf** (Hugging Face, founded 2016) — built the `transformers` library and model hub. [32][33]
- **Connor Leahy & EleutherAI collective** (formed 2020 on Discord) — The Pile, GPT-Neo, GPT-J: open GPT-3 replication. [22]
- **Jeff Dean & Noam Shazeer** (Google) — mixture-of-experts scaling (2017), Switch Transformer (2021), PaLM/Pathways (2022). [27][34][23]

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
- Hugging Face. *Transformers* library (GitHub). https://github.com/huggingface/transformers [32]

## Schools of thought / sub-clusters
- **Encoder camp (BERT lineage)** — bidirectional masked-LM pre-training for understanding tasks (BERT, RoBERTa, T5's encoder side); dominant in search and industrial NLP 2018–2021; borders: statistical/neural NLP of 2010–2016 to the west (word2vec, ELMo), retrieval-augmented generation to the east. [4][7][30]
- **Decoder / generative camp (GPT lineage)** — autoregressive next-token prediction at ever-larger scale (GPT-1/2/3, Codex); wins the era by turning scale into in-context learning; borders: RLHF/InstructGPT and ChatGPT to the east (file 08). [5][11][19][28]
- **Scaling-law empiricists** — Kaplan (2020) and Chinchilla (2022) treat capability as a function of compute; the intellectual engine of the "bitter lesson" school; borders: hardware/compute river (TPUs, A100/H100) and the compute-governance debate of file 08. [9][20]
- **Sparse / mixture-of-experts engineers** — Shazeer's MoE layer (2017), Switch Transformer (2021); borders: Mixtral and DeepSeek in file 08. [27][34]
- **Multimodal & scientific Transformers** — ViT, CLIP, DALL-E, AlphaFold 2, Gato, Whisper: attention as a universal substrate; borders: computer-vision lineage (file 09g), diffusion/generative-media district in file 08, robotics VLA models. [13][14][16][17][40][42]
- **Alignment and critique tributaries** — RLHF (Christiano 2017 → InstructGPT 2022) on one bank; "Stochastic Parrots", model cards and foundation-model risk reports on the other; borders: AI safety/ethics river (file 09c) and the alignment plateau of file 08. [19][37][38][44]
- **Open-replication commons** — EleutherAI (The Pile, GPT-J), BigScience BLOOM, Hugging Face hub; borders: the open-vs-closed road (file 09e), Llama/Mistral in file 08. [22][32][41]

## Map notes
- Suggested A1 label: **"The Transformer Plateau"** (alt. "Attention Highlands"). A2 countries: *Google/Brain-DeepMind* (BERT, T5, PaLM, AlphaFold, Chinchilla), *OpenAI* (GPT series, CLIP, DALL-E, Codex, InstructGPT), *the Open Commons* (Hugging Face, EleutherAI, BigScience). A3 cities: BERT, GPT-2, GPT-3, T5, ViT, CLIP, AlphaFold 2, Chinchilla, PaLM.
- Rivers/borders/bridges: the **Attention River** rises at Bahdanau 2014 (deep-learning era) and becomes navigable at Vaswani 2017; the **Scaling Law fault line** (Kaplan 2020) is a sharp escarpment separating the "bigger is better" plateau from the RNN lowlands to the west; the **RLHF canal** (2017 preferences paper → InstructGPT 2022) is the crossing into the chatbot era; the **CLIP bridge** connects this continent to the diffusion/generative-media district.
- The eastern border with file 08 should be drawn at **30 November 2022 (ChatGPT release)** — technically nothing new, sociologically everything new.
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
