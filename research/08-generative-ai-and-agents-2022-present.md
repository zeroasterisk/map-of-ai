# Generative AI and Agents (November 2022–present)

> **Status:** verified
> **Date range:** 2022–2026 (map's eastern coastline; "present" = September 2026)
> **Map placement (proposed):** X = 2022–2026; Y = connectionist/scaling pole for the model districts, mixed for the agent/tooling coast (LLMs re-absorb symbolic-era ideas: planning, tool use, search, protocols)
> **Altitude:** A1 continent ("The Generative Coast"), A2 country (OpenAI, Anthropic, Google DeepMind, Meta, Mistral, DeepSeek/Qwen, Nvidia), A3 city (ChatGPT, GPT-4, Llama, Claude, Gemini, Stable Diffusion, o1/R1, MCP), A4 street (individual model releases, benchmarks, policy instruments)

## One-paragraph summary
ChatGPT's release on 30 November 2022 turned the pre-assembled ingredients of the previous era (GPT-3.5 + RLHF) into a mass consumer product that reached 100 million monthly users within two months, and the four years since have been a compressed arms race across three fronts [1][2]. On the *model* front, frontier labs shipped multimodal generalists — GPT-4 (14 Mar 2023), Claude (Mar 2023), Gemini (6 Dec 2023), GPT-4o (May 2024) — while diffusion models (DALL-E 2, Midjourney, Stable Diffusion in 2022; Sora video in 2024) made image, audio and video generation ordinary [3][4][5][6][7][8]. On the *openness* front, Meta's LLaMA weights leaked in March 2023 and Llama 2/3 were then released deliberately; Mistral, Qwen and DeepSeek followed, and DeepSeek-R1 (20 Jan 2025) showed an open-weights Chinese lab matching OpenAI's o1 reasoning model at a fraction of the reported cost [9][10][11][12][13]. On the *agency* front, "test-time compute" reasoning models (o1, Sep 2024), computer-use (Oct 2024), the Model Context Protocol (Nov 2024) and terminal coding agents (Claude Code, 2025) turned chat assistants into systems that plan, call tools and act — reviving symbolic-era questions about planning and world models inside a connectionist substrate [14][15][16][17]. Around all of this grew an unprecedented governance and hardware superstructure: the Bletchley Declaration (Nov 2023), the EU AI Act (in force 1 Aug 2024), Nvidia's Hopper→Blackwell cycle and multi-trillion-dollar valuation, and the 2024 Nobel Prizes in Physics (Hopfield, Hinton) and Chemistry (Baker, Hassabis, Jumper) that formally canonised deep learning [18][19][20][21][22][23].

## Timeline of key events
| Year | Event | Why it matters | Source |
|------|-------|----------------|--------|
| 2022 (6 Apr) | OpenAI announces DALL-E 2 | Diffusion-based text-to-image at photoreal quality; starts the "AI art" year | [7] |
| 2022 (12 Jul) | Midjourney opens public beta (David Holz) | Discord-native generative art reaches millions | [24] |
| 2022 (22 Aug) | Stability AI publicly releases Stable Diffusion (weights + code; CompVis latent diffusion, arXiv 2112.10752) | Open-weights image generation; forks the generative-media map into open and closed halves | [8][25] |
| 2022 (30 Nov) | OpenAI releases ChatGPT (GPT-3.5 + RLHF) | 100M monthly users in two months; the "iPhone moment" for LLMs | [1][2] |
| 2022 (15 Dec) | Anthropic publishes "Constitutional AI: Harmlessness from AI Feedback" (arXiv 2212.08073) | RLAIF: model-written critiques against a written constitution; alternative to pure RLHF | [26] |
| 2023 (7 Feb) | Microsoft launches "the new Bing" with Bing Chat (GPT-4-based) | Search + chat; first big-tech LLM product outside OpenAI | [27] |
| 2023 (24 Feb) | Meta announces LLaMA (7B–65B, research licence; arXiv 2302.13971); weights leaked via 4chan torrent on 3 Mar 2023 | Ignites the open-weights ecosystem: Alpaca (13 Mar), Vicuna (30 Mar), llama.cpp | [9][28][29][30] |
| 2023 (14 Mar) | OpenAI releases GPT-4 (multimodal; technical report arXiv 2303.08774); Anthropic releases Claude the same day; Google opens Bard waitlist 21 Mar | Frontier-model race becomes a three-way contest | [3][4][31][32] |
| 2023 (22 Mar) | Future of Life Institute "Pause Giant AI Experiments" open letter; 30 May: CAIS Statement on AI Risk ("risk of extinction") | Existential-risk framing enters mainstream politics | [33][34] |
| 2023 (5 Apr) | Meta releases Segment Anything (SAM; arXiv 2304.02643) | Promptable vision foundation model; brings "foundation model" idea to segmentation | [35] |
| 2023 (20 Apr) | Google Brain and DeepMind merge into Google DeepMind | Consolidation for the Gemini programme | [36] |
| 2023 (29 May) | Rafailov et al., Direct Preference Optimization (arXiv 2305.18290) | Simpler alternative to RLHF's reward-model + PPO loop; widely adopted by open models | [37] |
| 2023 (18 Jul) | Meta releases Llama 2 (7B/13B/70B) under a commercial-use licence, with Microsoft | Open weights become a deliberate corporate strategy | [9][38] |
| 2023 (28 Jul) | Google DeepMind's RT-2 vision-language-action model (arXiv 2307.15818) | Web-scale VLM controls a robot arm; founding VLA paper | [39] |
| 2023 (27 Sep) | Mistral AI releases Mistral 7B (Apache 2.0; arXiv 2310.06825); Mixtral 8x7B MoE follows 11 Dec 2023 | European open-weights champion; sparse MoE returns to the frontier | [12][40][41] |
| 2023 (30 Oct) | US Executive Order 14110 on Safe, Secure, and Trustworthy AI (rescinded 20 Jan 2025) | First comprehensive US federal AI directive; compute-threshold reporting | [42] |
| 2023 (1–2 Nov) | Bletchley Declaration signed at the UK AI Safety Summit by 28 countries and the EU | First inter-governmental statement on frontier-AI risk | [18] |
| 2023 (17–22 Nov) | OpenAI board fires CEO Sam Altman; he is reinstated five days later | Governance crisis of the leading lab; safety-vs-commerce tensions exposed | [43] |
| 2023 (6 Dec) | Google announces Gemini 1.0 (Ultra/Pro/Nano; report arXiv 2312.11805); Bard renamed Gemini Feb 2024; Gemini 1.5 (1M-token context) Feb 2024 | Natively multimodal frontier model; long context becomes a competitive axis | [5][44][45] |
| 2024 (15 Feb) | OpenAI previews Sora text-to-video (public release Dec 2024) | Minute-long coherent video; "world simulator" framing | [6] |
| 2024 (4 Mar) | Anthropic releases Claude 3 family (Haiku, Sonnet, Opus) | First Anthropic models to top GPT-4 on standard benchmarks | [46] |
| 2024 (13 Mar) | EU AI Act passes European Parliament; Council approval 21 May; in force 1 Aug 2024 | World's first comprehensive AI regulation (risk tiers, GPAI obligations) | [19] |
| 2024 (18 Mar) | Nvidia announces Blackwell (B200/GB200) at GTC; Hopper H100 announced Mar 2022 | Compute supply becomes the strategic bottleneck; Nvidia passes $1T (2023) and later $4T (2025) market cap | [21][22][47] |
| 2024 (18 Apr) | Meta releases Llama 3 (8B/70B, ~15T training tokens); Llama 3.1 405B follows 23 Jul 2024 (arXiv 2407.21783) | Open weights reach GPT-4 class | [9][48] |
| 2024 (13 May) | OpenAI releases GPT-4o ("omni": real-time voice, vision, text) | Native multimodality and low-latency voice as product | [49] |
| 2024 (12 Sep) | OpenAI o1-preview — "reasoning model" trained with RL to think before answering | Test-time compute becomes a new scaling axis; full o1 5 Dec 2024 | [14] |
| 2024 (8–9 Oct) | Nobel Prize in Physics to Hopfield & Hinton; Chemistry to Baker, Hassabis & Jumper (AlphaFold) | Scientific establishment canonises neural networks | [23][50] |
| 2024 (22 Oct) | Anthropic ships "computer use" with Claude 3.5 Sonnet (public beta) | Model drives a desktop via screenshots and clicks; first frontier GUI agent | [15] |
| 2024 (25 Nov) | Anthropic open-sources the Model Context Protocol (MCP); OpenAI adopts it Mar 2025 | Standard plumbing for tool-using agents | [16][51] |
| 2024 (26 Dec) | DeepSeek-V3 (671B MoE, open weights; arXiv 2412.19437) | Frontier-class open model trained at reported ~$5.6M GPU cost | [13][52] |
| 2025 (20 Jan) | DeepSeek-R1 (arXiv 2501.12948, MIT-licensed) matches o1 on reasoning; tops US App Store 27 Jan | Open reasoning model from China; large one-day Nvidia stock drop; "DeepSeek moment" | [11][13] |
| 2025 (Feb–May) | Anthropic Claude Code (Feb 2025; GA May 2025 with Claude 4); Karpathy coins "vibe coding" (Feb 2025); OpenAI Operator (23 Jan 2025) & Deep Research | Agentic coding and browsing become everyday products | [17][53][54][55] |
| 2025 (5 Mar) | ACM announces 2024 Turing Award to Andrew Barto and Richard Sutton for reinforcement learning | RL, the engine of RLHF and reasoning models, receives the field's top honour | [56][57] |
| 2025 (12 Mar) | Google DeepMind Gemini Robotics (VLA built on Gemini 2.0) | Frontier multimodal models move into physical robots | [58] |
| 2025 (16 Apr) | OpenAI releases o3 and o4-mini (o3 announced 20 Dec 2024) | Reasoning models with native tool use inside the chain of thought | [59] |
| 2025 (28 Apr) | Alibaba releases Qwen3 family under Apache 2.0 | Chinese open-weights ecosystem broadens beyond DeepSeek | [60] |
| 2025 (5 Aug) | OpenAI releases gpt-oss-120b / 20b under Apache 2.0 — its first open-weights LMs since GPT-2 | Open-vs-closed line blurs at the frontier lab most identified with closure | [61] |
| 2025 (7 Aug) | OpenAI launches GPT-5, replacing GPT-4o, GPT-4.5 and o3 in ChatGPT | Unified reasoning + non-reasoning routing model | [62] |

### Needs verification (recent, mid-2025 → Sept 2026)
Items below appear in Wikipedia extracts fetched on 2026-09-06 but have not been cross-checked against a second primary source; treat as provisional for the map's easternmost strip.
- Sora 2 released to select US/Canada users, end of September 2025 [6].
- Gemini 3.1 Pro released 19 Feb 2026; Gemma 4 (open weights) April 2026 [45][63].
- Meta Superintelligence Labs releases "Muse Spark" as a replacement for Llama, April 2026; Llama 4 released April 2025 [9].
- Kimi K2.5 (Moonshot AI, one-trillion parameters) January 2026; Qwen3.8 (2.4T) by August 2026 [64][60].
- ChatGPT reported at 900 million weekly active users, February 2026 [1].
- Anthropic "Claude Cowork" agentic tool for non-programmers; Claude web version 20 Oct 2025 [4].

## Key people
- **Sam Altman** (OpenAI CEO) — led ChatGPT/GPT-4 commercialisation; fired 17 Nov 2023 and reinstated 22 Nov 2023. [43][65]
- **Ilya Sutskever** (OpenAI chief scientist to 2024) — GPT-series architect; board member in the Altman ouster; later founded Safe Superintelligence. [43][65]
- **Dario & Daniela Amodei** (Anthropic, founded 2021) — Claude, Constitutional AI, Responsible Scaling; safety-focused frontier lab. [4][66]
- **Demis Hassabis** (Google DeepMind CEO) — merged Brain+DeepMind (2023), led Gemini; 2024 Nobel Chemistry laureate with John Jumper. [36][50]
- **Yann LeCun & Mark Zuckerberg** (Meta) — drove the open-weights Llama strategy (2023–2025). [9][38]
- **Arthur Mensch, Guillaume Lample, Timothée Lacroix** (Mistral AI, founded Apr 2023, Paris) — Mistral 7B, Mixtral. [12]
- **Liang Wenfeng** (DeepSeek, founded Jul 2023, Hangzhou; funded by hedge fund High-Flyer) — DeepSeek-V3 and R1. [13]
- **Emad Mostaque** (Stability AI) and **Robin Rombach et al.** (CompVis, LMU Munich) — Stable Diffusion / latent diffusion. [8][25][67]
- **David Holz** (Midjourney) — generative art at consumer scale. [24]
- **Jensen Huang** (Nvidia CEO) — Hopper/Blackwell; Nvidia becomes the first $4T–$5T company (2025). [21][22][47]
- **Geoffrey Hinton** — left Google May 2023 warning of AI risk; 2024 Nobel Physics laureate with John Hopfield. [23][68]
- **Andrew Barto & Richard Sutton** — 2024 ACM Turing Award for reinforcement learning (announced Mar 2025). [56][57]
- **Andrej Karpathy** (ex-OpenAI/Tesla) — coined "vibe coding" (Feb 2025); popular educator of the LLM era. [54]
- **Dan Hendrycks** (Center for AI Safety, founded 2022) — organised the May 2023 Statement on AI Risk. [34]
- **Timnit Gebru & Emily Bender** — continuing critique of scale, hype and harms carried over from "Stochastic Parrots". [69]

## Key papers / artifacts
- OpenAI. *Introducing ChatGPT*. 30 Nov 2022. https://openai.com/index/chatgpt/ (403 to bots) [1]
- OpenAI. *GPT-4 Technical Report*. arXiv 2303.08774, Mar 2023. https://arxiv.org/abs/2303.08774 [31]
- Touvron, H. et al. *LLaMA: Open and Efficient Foundation Language Models*. arXiv 2302.13971, Feb 2023. https://arxiv.org/abs/2302.13971 [28]
- Touvron, H. et al. *Llama 2: Open Foundation and Fine-Tuned Chat Models*. arXiv 2307.09288, Jul 2023. https://arxiv.org/abs/2307.09288 [38]
- Grattafiori, A. et al. *The Llama 3 Herd of Models*. arXiv 2407.21783, Jul 2024. https://arxiv.org/abs/2407.21783 [48]
- Bai, Y. et al. *Constitutional AI: Harmlessness from AI Feedback*. arXiv 2212.08073, Dec 2022. https://arxiv.org/abs/2212.08073 [26]
- Rafailov, R. et al. *Direct Preference Optimization: Your Language Model is Secretly a Reward Model*. NeurIPS 2023 (arXiv 2305.18290). https://arxiv.org/abs/2305.18290 [37]
- Rombach, R. et al. *High-Resolution Image Synthesis with Latent Diffusion Models*. CVPR 2022 (arXiv 2112.10752). https://arxiv.org/abs/2112.10752 [25]
- Stability AI. *Stable Diffusion Public Release*. 22 Aug 2022. https://stability.ai/news/stable-diffusion-public-release [8]
- Jiang, A. Q. et al. *Mistral 7B*. arXiv 2310.06825, Oct 2023. https://arxiv.org/abs/2310.06825 [40]
- Jiang, A. Q. et al. *Mixtral of Experts*. arXiv 2401.04088, Jan 2024. https://arxiv.org/abs/2401.04088 [41]
- Gemini Team. *Gemini: A Family of Highly Capable Multimodal Models*. arXiv 2312.11805, Dec 2023. https://arxiv.org/abs/2312.11805 [44]
- DeepSeek-AI. *DeepSeek-V3 Technical Report*. arXiv 2412.19437, Dec 2024. https://arxiv.org/abs/2412.19437 [52]
- DeepSeek-AI. *DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning*. arXiv 2501.12948, Jan 2025. https://arxiv.org/abs/2501.12948 [11]
- Brohan, A. et al. *RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control*. arXiv 2307.15818, Jul 2023. https://arxiv.org/abs/2307.15818 [39]
- Kirillov, A. et al. *Segment Anything*. ICCV 2023 (arXiv 2304.02643). https://arxiv.org/abs/2304.02643 [35]
- Yao, S. et al. *ReAct: Synergizing Reasoning and Acting in Language Models*. ICLR 2023 (arXiv 2210.03629). https://arxiv.org/abs/2210.03629 [70]
- Lewis, P. et al. *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. NeurIPS 2020 (arXiv 2005.11401). https://arxiv.org/abs/2005.11401 [71]
- Hu, E. J. et al. *LoRA: Low-Rank Adaptation of Large Language Models*. ICLR 2022 (arXiv 2106.09685). https://arxiv.org/abs/2106.09685 [72]
- Anthropic. *Introducing the Model Context Protocol*. 25 Nov 2024. https://www.anthropic.com/news/model-context-protocol [16]
- European Union. *Regulation (EU) 2024/1689 (Artificial Intelligence Act)*. OJ, 12 Jul 2024. https://eur-lex.europa.eu/eli/reg/2024/1689/oj [73]

## Schools of thought / sub-clusters
- **Closed frontier labs (scaling + RLHF)** — OpenAI, Anthropic, Google DeepMind: proprietary weights, API distribution, safety cases and staged deployment; borders: Transformer Plateau to the west (GPT-3, InstructGPT), alignment plateau and policy coast to the north. [1][3][4][5]
- **Open-weights movement** — Meta (Llama), Mistral, DeepSeek, Qwen, Stability, EleutherAI/Hugging Face commons, llama.cpp/Ollama local-inference tooling; borders: the open-vs-closed road (file 09e) and the earlier open-source frameworks district (TensorFlow/PyTorch); the OSI's 2024 Open Source AI Definition contests whether "open weights" is truly open. [9][12][13][30][74]
- **Diffusion / generative-media district** — DALL-E 2, Midjourney, Stable Diffusion, Sora, Veo; conditioning inherited via the CLIP bridge from file 07; borders: computer-vision lineage (file 09g), copyright litigation and deepfake ethics (file 09c). [6][7][8][24][25]
- **Reasoning & test-time-compute school** — o1/o3, DeepSeek-R1, Gemini "thinking" models: RL on verifiable rewards, long chains of thought, inference-time scaling as a new axis; borders: the reinforcement-learning river (file 09a) and game-playing highlands (AlphaZero/MuZero search-plus-learning). [11][14][59]
- **Agents & tooling coast** — ReAct, function calling, RAG, MCP, computer use, Operator, Claude Code, coding agents; the most "mixed" Y-position of the era because it re-imports symbolic planning, tool APIs and protocols; borders: symbolic/planning eras (STRIPS, Shakey) far to the west via a long "road", and robotics/VLA (RT-2, Gemini Robotics, π0, Helix) to the embodied shore. [15][16][17][39][58][70][71]
- **Alignment & interpretability plateau** — Constitutional AI, DPO, RLHF refinements, mechanistic interpretability, evals and red-teaming; borders: AI safety river (file 09c), Bletchley/EU AI Act policy coast. [26][37][75]
- **Policy & governance coast** — Bletchley (2023), EO 14110 (2023, rescinded 2025), EU AI Act (2024), safety institutes; borders: ethics tributaries from Weizenbaum→Stochastic Parrots and existential-risk tributaries from Bostrom/FLI/CAIS. [18][19][33][34][42]
- **Compute & hardware hinterland** — Nvidia Hopper/Blackwell, TPU generations, export controls, data-centre build-out; borders: hardware river (file 09d). [21][22][47]

## Map notes
- Suggested A1 label: **"The Generative Coast"** (the map's eastern seaboard; the ocean beyond is the unknown future). A2 countries: *OpenAI*, *Anthropic*, *Google DeepMind*, *Meta/Llama Commons*, *Mistral & the European Shore*, *DeepSeek/Qwen (the Chinese Shore)*, *Nvidia hinterland*. A3 cities: ChatGPT (the port city, 30 Nov 2022), GPT-4, Claude 3, Gemini, Llama 2/3, Stable Diffusion, Sora, o1, DeepSeek-R1, MCP.
- Rivers/borders/bridges: the **RLHF canal** enters from file 07 at InstructGPT and widens into the "alignment plateau"; the **Open-weights road** forks sharply at the LLaMA leak (3 Mar 2023) and splits the continent into an open north and a closed south; the **Reasoning ridge** (Sep 2024–Jan 2025: o1 → R1) is where the RL river re-joins the LLM mainstream; the **Agents causeway** (MCP, computer use, coding agents) runs out to the robotics/VLA islands.
- Draw the western border at **30 Nov 2022 (ChatGPT)** with the prior file; draw the eastern edge as an open coastline dated **Sept 2026** with a "here be dragons" strip for the unverified recent items.
- Open questions for curation: (1) whether the Nobel/Turing 2024 canonisation belongs here or as a monument straddling several eras; (2) how much of the governance material (Bletchley, EU AI Act) to draw here vs. on the ethics river in file 09; (3) whether "reasoning models" merit their own A2 country by 2026; (4) whether Chinese labs should be a single "shore" or several cities (DeepSeek, Qwen, Kimi).

## Sources
[1] Wikipedia: ChatGPT — https://en.wikipedia.org/wiki/ChatGPT (accessed 2026-09-06); OpenAI, Introducing ChatGPT — https://openai.com/index/chatgpt/ (403 to bots)
[2] Wikipedia: AI boom — https://en.wikipedia.org/wiki/AI_boom (accessed 2026-09-06)
[3] Wikipedia: GPT-4 — https://en.wikipedia.org/wiki/GPT-4 (accessed 2026-09-06)
[4] Wikipedia: Claude (language model) — https://en.wikipedia.org/wiki/Claude_%28language_model%29 (accessed 2026-09-06); Anthropic, Introducing Claude, 14 Mar 2023 — https://www.anthropic.com/news/introducing-claude
[5] Introducing Gemini: our largest and most capable AI model — Google blog, 6 Dec 2023 — https://blog.google/technology/ai/google-gemini-ai/ (accessed 2026-09-06)
[6] Wikipedia: Sora (text-to-video model) — https://en.wikipedia.org/wiki/Sora_%28text-to-video_model%29 (accessed 2026-09-06)
[7] Wikipedia: DALL-E — https://en.wikipedia.org/wiki/DALL-E (accessed 2026-09-06)
[8] Stable Diffusion Public Release — Stability AI, 22 Aug 2022 — https://stability.ai/news/stable-diffusion-public-release (accessed 2026-09-06)
[9] Wikipedia: Llama (language model) — https://en.wikipedia.org/wiki/Llama_%28language_model%29 (accessed 2026-09-06)
[10] Introducing LLaMA: A foundational, 65-billion-parameter language model — Meta AI, 24 Feb 2023 — https://ai.meta.com/blog/large-language-model-llama-meta-ai/ (accessed 2026-09-06)
[11] DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning — arXiv 2501.12948 — https://arxiv.org/abs/2501.12948 (accessed 2026-09-06)
[12] Wikipedia: Mistral AI — https://en.wikipedia.org/wiki/Mistral_AI (accessed 2026-09-06)
[13] Wikipedia: DeepSeek — https://en.wikipedia.org/wiki/DeepSeek (accessed 2026-09-06)
[14] Wikipedia: OpenAI o1 — https://en.wikipedia.org/wiki/OpenAI_o1 (accessed 2026-09-06)
[15] Introducing computer use, a new Claude 3.5 Sonnet, and Claude 3.5 Haiku — Anthropic, 22 Oct 2024 — https://www.anthropic.com/news/3-5-models-and-computer-use (accessed 2026-09-06)
[16] Introducing the Model Context Protocol — Anthropic, 25 Nov 2024 — https://www.anthropic.com/news/model-context-protocol (accessed 2026-09-06)
[17] Wikipedia: Claude (language model), "Claude Code" section — https://en.wikipedia.org/wiki/Claude_%28language_model%29 (accessed 2026-09-06)
[18] The Bletchley Declaration by Countries Attending the AI Safety Summit, 1–2 November 2023 — GOV.UK — https://www.gov.uk/government/publications/ai-safety-summit-2023-the-bletchley-declaration/the-bletchley-declaration-by-countries-attending-the-ai-safety-summit-1-2-november-2023 (accessed 2026-09-06)
[19] Wikipedia: Artificial Intelligence Act — https://en.wikipedia.org/wiki/Artificial_Intelligence_Act (accessed 2026-09-06)
[20] Wikipedia: Nvidia — https://en.wikipedia.org/wiki/Nvidia (accessed 2026-09-06)
[21] Wikipedia: Hopper (microarchitecture) (H100) — https://en.wikipedia.org/wiki/Hopper_%28microarchitecture%29 (accessed 2026-09-06)
[22] Wikipedia: Blackwell (microarchitecture) — https://en.wikipedia.org/wiki/Blackwell_%28microarchitecture%29 (accessed 2026-09-06)
[23] Press release: The Nobel Prize in Physics 2024 — https://www.nobelprize.org/prizes/physics/2024/press-release/ (accessed 2026-09-06)
[24] Wikipedia: Midjourney — https://en.wikipedia.org/wiki/Midjourney (accessed 2026-09-06)
[25] High-Resolution Image Synthesis with Latent Diffusion Models — arXiv 2112.10752 — https://arxiv.org/abs/2112.10752 (accessed 2026-09-06)
[26] Constitutional AI: Harmlessness from AI Feedback — arXiv 2212.08073 — https://arxiv.org/abs/2212.08073 (accessed 2026-09-06)
[27] Wikipedia: Microsoft Copilot (Bing Chat launch, 7 Feb 2023) — https://en.wikipedia.org/wiki/Microsoft_Copilot (accessed 2026-09-06)
[28] LLaMA: Open and Efficient Foundation Language Models — arXiv 2302.13971 — https://arxiv.org/abs/2302.13971 (accessed 2026-09-06)
[29] Alpaca: A Strong, Replicable Instruction-Following Model — Stanford CRFM, 13 Mar 2023 — https://crfm.stanford.edu/2023/03/13/alpaca.html (accessed 2026-09-06)
[30] llama.cpp (GitHub) — https://github.com/ggml-org/llama.cpp (accessed 2026-09-06); Vicuna — LMSYS, 30 Mar 2023 — https://lmsys.org/blog/2023-03-30-vicuna/
[31] GPT-4 Technical Report — arXiv 2303.08774 — https://arxiv.org/abs/2303.08774 (accessed 2026-09-06)
[32] Wikipedia: Google Gemini (Bard launch 21 Mar 2023; rename Feb 2024) — https://en.wikipedia.org/wiki/Google_Gemini (accessed 2026-09-06)
[33] Pause Giant AI Experiments: An Open Letter — Future of Life Institute, Mar 2023 — https://futureoflife.org/open-letter/pause-giant-ai-experiments/ (accessed 2026-09-06)
[34] Statement on AI Risk — Center for AI Safety, 30 May 2023 — https://www.safe.ai/work/statement-on-ai-risk (accessed 2026-09-06)
[35] Segment Anything — arXiv 2304.02643 — https://arxiv.org/abs/2304.02643 (accessed 2026-09-06)
[36] Wikipedia: Google DeepMind — https://en.wikipedia.org/wiki/Google_DeepMind (accessed 2026-09-06)
[37] Direct Preference Optimization — arXiv 2305.18290 — https://arxiv.org/abs/2305.18290 (accessed 2026-09-06)
[38] Llama 2: Open Foundation and Fine-Tuned Chat Models — arXiv 2307.09288 — https://arxiv.org/abs/2307.09288 (accessed 2026-09-06)
[39] RT-2: Vision-Language-Action Models — arXiv 2307.15818 — https://arxiv.org/abs/2307.15818 (accessed 2026-09-06); DeepMind blog — https://deepmind.google/discover/blog/rt-2-new-model-translates-vision-and-language-into-action/
[40] Mistral 7B — arXiv 2310.06825 — https://arxiv.org/abs/2310.06825 (accessed 2026-09-06); Mistral blog, 27 Sep 2023 — https://mistral.ai/news/announcing-mistral-7b
[41] Mixtral of Experts — arXiv 2401.04088 — https://arxiv.org/abs/2401.04088 (accessed 2026-09-06); Mistral blog, 11 Dec 2023 — https://mistral.ai/news/mixtral-of-experts
[42] Wikipedia: Executive Order 14110 — https://en.wikipedia.org/wiki/Executive_Order_14110 (accessed 2026-09-06)
[43] Wikipedia: Removal of Sam Altman from OpenAI — https://en.wikipedia.org/wiki/Removal_of_Sam_Altman_from_OpenAI (accessed 2026-09-06)
[44] Gemini: A Family of Highly Capable Multimodal Models — arXiv 2312.11805 — https://arxiv.org/abs/2312.11805 (accessed 2026-09-06)
[45] Wikipedia: Gemini (language model) — https://en.wikipedia.org/wiki/Gemini_%28language_model%29 (accessed 2026-09-06)
[46] Introducing the next generation of Claude (Claude 3) — Anthropic, 4 Mar 2024 — https://www.anthropic.com/news/claude-3-family (accessed 2026-09-06)
[47] NVIDIA Blackwell Platform Arrives to Power a New Era of Computing — Nvidia Newsroom, 18 Mar 2024 — https://nvidianews.nvidia.com/news/nvidia-blackwell-platform-arrives-to-power-a-new-era-of-computing (accessed 2026-09-06)
[48] The Llama 3 Herd of Models — arXiv 2407.21783 — https://arxiv.org/abs/2407.21783 (accessed 2026-09-06)
[49] Wikipedia: GPT-4o — https://en.wikipedia.org/wiki/GPT-4o (accessed 2026-09-06)
[50] Press release: The Nobel Prize in Chemistry 2024 — https://www.nobelprize.org/prizes/chemistry/2024/press-release/ (accessed 2026-09-06)
[51] Wikipedia: Model Context Protocol — https://en.wikipedia.org/wiki/Model_Context_Protocol (accessed 2026-09-06)
[52] DeepSeek-V3 Technical Report — arXiv 2412.19437 — https://arxiv.org/abs/2412.19437 (accessed 2026-09-06)
[53] Wikipedia: OpenAI (Operator, Deep Research, Jan–Feb 2025) — https://en.wikipedia.org/wiki/OpenAI (accessed 2026-09-06)
[54] Wikipedia: Vibe coding — https://en.wikipedia.org/wiki/Vibe_coding (accessed 2026-09-06)
[55] Introducing Claude 4 — Anthropic, 22 May 2025 — https://www.anthropic.com/news/claude-4 (accessed 2026-09-06)
[56] Wikipedia: Richard S. Sutton — https://en.wikipedia.org/wiki/Richard_S._Sutton (accessed 2026-09-06)
[57] Wikipedia: Andrew Barto — https://en.wikipedia.org/wiki/Andrew_Barto (accessed 2026-09-06)
[58] Wikipedia: Gemini Robotics — https://en.wikipedia.org/wiki/Gemini_Robotics (accessed 2026-09-06); DeepMind blog — https://deepmind.google/discover/blog/gemini-robotics-brings-ai-into-the-physical-world/
[59] Wikipedia: OpenAI o3 — https://en.wikipedia.org/wiki/OpenAI_o3 (accessed 2026-09-06)
[60] Wikipedia: Qwen — https://en.wikipedia.org/wiki/Qwen (accessed 2026-09-06)
[61] Wikipedia: Products and applications of OpenAI (GPT-OSS) — https://en.wikipedia.org/wiki/Products_and_applications_of_OpenAI (accessed 2026-09-06)
[62] Wikipedia: GPT-5 — https://en.wikipedia.org/wiki/GPT-5 (accessed 2026-09-06)
[63] Wikipedia: Gemma (language model) — https://en.wikipedia.org/wiki/Gemma_%28language_model%29 (accessed 2026-09-06)
[64] Wikipedia: Kimi (chatbot) — https://en.wikipedia.org/wiki/Kimi_%28chatbot%29 (accessed 2026-09-06)
[65] Wikipedia: OpenAI — https://en.wikipedia.org/wiki/OpenAI (accessed 2026-09-06)
[66] Wikipedia: Anthropic — https://en.wikipedia.org/wiki/Anthropic (accessed 2026-09-06)
[67] Wikipedia: Stability AI — https://en.wikipedia.org/wiki/Stability_AI (accessed 2026-09-06)
[68] Wikipedia: Geoffrey Hinton — https://en.wikipedia.org/wiki/Geoffrey_Hinton (accessed 2026-09-06)
[69] Wikipedia: Stochastic parrot — https://en.wikipedia.org/wiki/Stochastic_parrot (accessed 2026-09-06)
[70] ReAct: Synergizing Reasoning and Acting in Language Models — arXiv 2210.03629 — https://arxiv.org/abs/2210.03629 (accessed 2026-09-06)
[71] Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks — arXiv 2005.11401 — https://arxiv.org/abs/2005.11401 (accessed 2026-09-06)
[72] LoRA: Low-Rank Adaptation of Large Language Models — arXiv 2106.09685 — https://arxiv.org/abs/2106.09685 (accessed 2026-09-06)
[73] Regulation (EU) 2024/1689 — EUR-Lex — https://eur-lex.europa.eu/eli/reg/2024/1689/oj (accessed 2026-09-06)
[74] The Open Source AI Definition — Open Source Initiative, 2024 — https://opensource.org/ai/open-source-ai-definition (accessed 2026-09-06)
[75] Wikipedia: Mechanistic interpretability — https://en.wikipedia.org/wiki/Mechanistic_interpretability (accessed 2026-09-06)
