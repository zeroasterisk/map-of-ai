# Knowledge Bundle Operational Log

## [2026-10-08] audit | Full 3-Test Road Knowledge Graph Audit & OKF v0.2 Reconstruction

- **Actor**: `gemini-4-argon/1.0` (verified by `human:zeroasterisk`)
- **Scope**: Audited all `399` legacy road edges across `475` milestones and `47` provinces; replaced the legacy nearest-neighbor spur generator and mixed-company trunks with `79` curated lineage roads (`492` unique directed edges, `100%` milestone coverage, `0` chronological reversals, `0` vertical spur slashes).

### Key Problematic Relationships Remediated

- **`gpt4o-2024 -> nobel-2024`** (*Generative Coast Parish Lane (nearest-neighbor spur)*) — **Failed**: Lawyer Test, Reddit Test, Individuals Involved Test
  - *Issue*: Implied OpenAI's GPT-4o led to or was associated with the 2024 Nobel Prizes awarded to Demis Hassabis & John Jumper (Google DeepMind, Chemistry for AlphaFold) and John Hopfield & Geoffrey Hinton (Physics for neural networks).
  - *Resolution*: Deleted nearest-neighbor spur generator. Connected `nobel-2024` exclusively to `alphafold3-2024` / `imo-silver-2024` on `via-deepmind-rl` and `hinton-leaves-2023` (`dbn-2006 -> dnnresearch-2013 -> vector-2017 -> hinton-leaves-2023 -> nobel-2024`) on `branch-hinton-nobel`.
- **`gpt4-2023 ('GPT-4 · Claude 1') on via-openai`** (*The OpenAI Post Road (`via-openai`)*) — **Failed**: Lawyer Test, Reddit Test, Individuals Involved Test
  - *Issue*: Bundling Anthropic's Claude 1 into the title of `gpt4-2023` on the OpenAI trunk implied Claude 1 was an OpenAI model.
  - *Resolution*: Renamed `gpt4-2023` to `'GPT-4'` on `via-openai`; Anthropic's Claude family runs exclusively on `via-anthropic-alignment`.
- **`microsoft-openai-2023 ('Microsoft $10 B · Bard') -> bing-chat-2023`** (*Generative Coast Parish Lane*) — **Failed**: Lawyer Test, Reddit Test
  - *Issue*: Bundling Google's Bard into the title of `microsoft-openai-2023` and linking it to Microsoft's `bing-chat-2023` conflated Microsoft's $10B OpenAI investment with Google Bard.
  - *Resolution*: Renamed `microsoft-openai-2023` to `'Microsoft $10 B OpenAI'` on `spur-microsoft-copilot-phi` (`openai-lp-2019 -> microsoft-openai-2023 -> bing-chat-2023 -> phi1-2023 -> phi3-2024`), while Google Bard is covered on `palm2-2023` (`via-transformer-gemini`).
- **`claude35-2024 -> grok2-2024, grok-2023 -> claude21-2023, grok3-2025 -> gpt45-2025, grok4-2025 -> gemini3-2025`** (*Generative Coast Parish Lane (nearest-neighbor spurs)*) — **Failed**: Lawyer Test, Reddit Test, Individuals Involved Test
  - *Issue*: Chained xAI's Grok models directly into and out of Anthropic's Claude 2.1 / Claude 3.5 Sonnet, OpenAI's GPT-4.5, and Google's Gemini 3.0.
  - *Resolution*: Created dedicated `spur-xai-grok` (`grok-2023 -> grok2-2024 -> grok3-2025 -> grok4-2025`) with zero cross-competitor model edges.
- **`mixtral-2023 -> gemma-2024 -> llama3-2024 -> deepseek-v2-2024 -> gemma2-2024 -> deepseek-v3-2024 -> deepseek-r1-2025 -> gemma3-2025 -> llama4-2025 -> gpt-oss-2025 -> gemma4-2026`** (*The FAIR, PyTorch & Open-Weights Highway (`via-fair-openweights`)*) — **Failed**: Lawyer Test, Reddit Test, Individuals Involved Test
  - *Issue*: Zig-zagged a single trunk across 5 competing organizations (Mistral, Google, Meta, DeepSeek, OpenAI), implying Google Gemma derived from Mistral Mixtral, Meta Llama 3 derived from Gemma, DeepSeek-V2 derived from Llama 3, and Gemma 4 derived from OpenAI `gpt-oss`.
  - *Resolution*: Split into 5 pure organizational roads: `via-fair-openweights` (Meta FAIR/PyTorch/Llama 1–4), `branch-google-gemma` (Gemini -> Gemma 1–4 -> dgem), `branch-deepseek-moe` (Sparse MoE -> GRPO -> DeepSeek-V2 -> V3 -> R1 -> Kimi K2), `spur-mistral-open` (Mistral 7B -> Mixtral), and `spur-openai-open-weights` (GPT-2 -> Whisper -> gpt-oss).
- **`sora-2024 -> imagen3-2024 -> notebooklm-audio-2024 -> veo3-2025 -> sora2-2025`** (*The ConvNet, GAN & Diffusion Media Coast Road (`via-vision-diffusion`)*) — **Failed**: Lawyer Test, Reddit Test, Individuals Involved Test
  - *Issue*: Routed OpenAI's Sora (2024) into Google's Imagen 3, NotebookLM Audio Overviews, and Veo 3, and then routed Google's Veo 3 into OpenAI's Sora 2.
  - *Resolution*: Kept `via-vision-diffusion` pure for academic/open-weights vision & diffusion (`ImageNet -> AlexNet -> ResNet -> DDPM -> Stable Diffusion -> ControlNet -> SDXL -> SD3/Flux.1`), created `branch-openai-media` (`GPT-3 -> DALL-E/CLIP -> GLIDE -> DALL-E 2 -> Whisper -> DALL-E 3 -> Sora -> Sora 2`), and created `branch-google-media` (`T5 -> ViT -> Imagen -> DreamFusion -> Imagen 3 -> NotebookLM Audio -> Veo 3 -> Genie 3`).
- **`blackwell-2024 -> tpu-trillium-2024 -> tpu-ironwood-2025 -> stargate-2025 -> nvidia-rubin-2026`** (*The TensorFlow, TPU & Compute Turnpike (`via-tensorflow-tpu`)*) — **Failed**: Lawyer Test, Reddit Test
  - *Issue*: Interleaved Nvidia GPUs (`Blackwell`, `Vera Rubin`), Google custom ASICs (`TPU Trillium`, `TPU Ironwood`), and OpenAI's `Stargate` datacenter venture on the same trunk.
  - *Resolution*: Kept `via-tensorflow-tpu` 100% Google (`Google Brain -> DistBelief -> TensorFlow -> TPU v1 -> JAX -> PaLM -> TPU Trillium -> TPU Ironwood`), moved Nvidia GPUs & CUDA kernels to `branch-gpu-compute`, and placed `stargate-2025` on `spur-stargate-datacenter` (`H100 -> Blackwell -> Stargate -> Vera Rubin`).
- **`gebru-exit-2020 -> anthropic-2021`** (*Generative Coast Parish Lane (nearest-neighbor spur)*) — **Failed**: Lawyer Test, Reddit Test, Individuals Involved Test
  - *Issue*: Connected Timnit Gebru's December 2020 departure from Google Ethical AI directly to the January 2021 founding of Anthropic (which was founded by Dario & Daniela Amodei and former OpenAI researchers).
  - *Resolution*: Connected `model-cards-2018 -> gebru-exit-2020 -> stochastic-parrots-2021` on `spur-ethical-ai-facct` and anchored `anthropic-2021` to `scaling-laws-2020` on `via-anthropic-alignment`.
- **`constitutional-ai-2022 -> hinton-leaves-2023`** (*Generative Coast Parish Lane (nearest-neighbor spur)*) — **Failed**: Reddit Test, Individuals Involved Test
  - *Issue*: Linked Anthropic's Constitutional AI paper to Geoffrey Hinton leaving Google Brain in May 2023.
  - *Resolution*: Connected `hinton-leaves-2023` on `branch-hinton-nobel` (`hopfield-1982 -> boltzmann-1985 -> dbn-2006 -> dnnresearch-2013 -> vector-2017 -> hinton-leaves-2023 -> nobel-2024`).
- **`o1-2024 -> turing-rl-2025`** (*Generative Coast Parish Lane (nearest-neighbor spur)*) — **Failed**: Reddit Test, Individuals Involved Test
  - *Issue*: Linked OpenAI's o1 release to Rich Sutton & Andrew Barto's 2025 ACM Turing Award for foundational reinforcement learning.
  - *Resolution*: Created `branch-sutton-barto-turing` (`actor-critic-1983 -> td-lambda-1988 -> q-learning-1989 -> dyna-1990 -> td-gammon-1992 -> reinforce-1992 -> sutton-barto-book-1998 -> bitter-lesson-2019 -> turing-rl-2025`).
- **`grpo-2024 -> imo-silver-2024`** (*Generative Coast Parish Lane (nearest-neighbor spur)*) — **Failed**: Lawyer Test, Reddit Test, Individuals Involved Test
  - *Issue*: Linked DeepSeek's Group Relative Policy Optimization (`grpo-2024`) to Google DeepMind's AlphaProof & AlphaGeometry 2 (`imo-silver-2024`).
  - *Resolution*: Connected `grpo-2024 -> deepseek-v2-2024 -> deepseek-v3-2024 -> deepseek-r1-2025` on `branch-deepseek-moe`, and `alphageometry-2024 -> alphafold3-2024 -> imo-silver-2024` on `via-deepmind-rl`.
- **`adk-gemini-cli-2025 -> claude-code-2025 and agent-skills-2025 -> cowork-2026 on via-agents-protocols`** (*The Agentic Tooling, MCP, A2A & AAIF Coast Road (`via-agents-protocols`)*) — **Failed**: Lawyer Test, Reddit Test, Individuals Involved Test
  - *Issue*: Chained Google's ADK & Gemini CLI directly into Anthropic's Claude Code (with a backward timestamp `2025.48 -> 2025.15`) and mixed vendor-specific products with open AAIF standards.
  - *Resolution*: Kept `via-agents-protocols` pure for open frameworks & standards (`LangChain/ReAct -> Toolformer -> Function Calling -> MCP -> A2A -> AP2 -> A2UI -> AAIF -> SKILL.md -> UCP -> Agent Plugins -> AX -> ARD`), with `spur-anthropic-agents` for Claude Code/Cowork and `spur-google-agents` for Google ADK/Gemini CLI.
- **`nyt-openai-2023 -> eu-ai-act-2024 -> riaa-suno-2024 and flashattention3-2024 -> ai-diffusion-rule-2025`** (*Generative Coast Parish Lane (nearest-neighbor spurs)*) — **Failed**: Lawyer Test, Reddit Test
  - *Issue*: Conflated private US copyright lawsuits (`NYT v. OpenAI`, `RIAA v. Suno`) with the European Union's statutory AI Act, and linked Tri Dao's Hopper CUDA kernel paper (`FlashAttention-3`) to the US BIS export control rule (`AI Diffusion Rule`).
  - *Resolution*: Separated statutory regulation onto `branch-policy-governance` and copyright lawsuits onto `spur-ip-copyright-litigation`, while `flashattention3-2024` stays on `branch-gpu-compute`.
- **`lstm-1997 -> svm-optimal-margin-1998 -> lenet5-mnist-1998`** (*The Cybernetic, Connectionist & Deep Learning Trunk Road (`via-western-connectionist`)*) — **Failed**: Reddit Test, Individuals Involved Test
  - *Issue*: Placed Vladimir Vapnik's non-neural Kernel Support Vector Machine directly between Hochreiter & Schmidhuber's LSTM and Yann LeCun's LeNet-5 ConvNet.
  - *Resolution*: Moved SVMs to `spur-svm-classical-vision` (`nilsson-1965 -> svm-optimal-margin-1998 -> soft-margin-svm-1998 -> sift-1999 -> hog-2005 -> ilsvrc-2010`) and connected `zip-code-convnet-1989 -> lenet5-mnist-1998` directly on `via-western-connectionist`.
