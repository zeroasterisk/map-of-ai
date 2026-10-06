# Coverage matrix — generative-coast

Continent: `generative-coast` · Research file: `research/08-generative-ai-and-agents-2022-present.md` · Date: 2026-09-13 · Schools of thought bullets: 8 · Units: P2-T10 (header), P3-T10 (Table 1)

Check A-M2: `awk '/^## Schools of thought/{f=1;next} /^## /{f=0} f&&/^- /{n++} END{print n}' research/08-generative-ai-and-agents-2022-present.md` → 8 = Table 1 rows.

## Table 1 — schools of thought → countries (P3-T10)

| # | school bullet | decision | entity id | reason |
|---|---|---|---|---|
| 1 | Closed frontier labs (scaling + RLHF) | country | `closed-frontier-labs` | OpenAI, Anthropic, Google DeepMind: proprietary weights, API distribution, safety cases, staged deployment; the ChatGPT port city sits here; the "closed south" of research/08's open-weights road |
| 2 | Open-weights movement | country | `open-weights-movement` | Meta/Llama, Mistral, DeepSeek, Qwen, Stability, EleutherAI/HF commons, llama.cpp/Ollama; forks off at the LLaMA leak (3 Mar 2023) as the "open north" |
| 3 | Diffusion / generative-media district | country | `diffusion-media-district` | DALL-E 2, Midjourney, Stable Diffusion/SDXL/SD3, Sora/Sora 2, Veo 3, Genie world models, ElevenLabs/Suno/Udio; the S2 perception shoreline that continues the basin's deep-generative-shoreline |
| 4 | Reasoning & test-time-compute school | country | `reasoning-test-time-compute` | o1/o3, DeepSeek-R1, Gemini "thinking" models: RL on verifiable rewards, inference-time scaling; AXES.md §3 lists "o1/R1-style reasoning" in N2, so it gets its own N2 ridge (research/08 open question 3 answered: yes, own A2 by 2026) |
| 5 | Agents & tooling coast | country | `agents-tooling-coast` | ReAct, Toolformer, LangChain/AutoGPT, function calling, RAG, MCP/A2A, computer use, Operator, Devin/Cursor/Claude Code/Cowork, SWE-bench/GAIA/Arena; the "most mixed Y-position" of the era → S1 + biome mixed |
| 6 | Alignment & interpretability plateau | country | `alignment-interpretability-plateau` | Constitutional AI, DPO, RLHF refinements, Responsible Scaling Policy, mechanistic interpretability, evals/red-teaming; the RLHF canal from file 07 widens into this plateau (research/08 map notes) |
| 7 | Policy & governance coast | country | `policy-governance-coast` | Bletchley 2023, EO 14110/14179, EU AI Act, safety institutes, Paris Action Summit, NYT/Getty/RIAA ip-rights docket; N1 safety/ethics ridge along the northern edge (research/08 open question 2: drawn here, not only on the file-09 ethics river) |
| 8 | Compute & hardware hinterland | country | `compute-hardware-hinterland` | Nvidia Hopper/Blackwell, TPU generations, Groq LPU, export controls (Oct 2022 → Jan 2025 diffusion rule), Stargate build-out; spans the parent's whole time range like `tooling-guild` did for the basin, but drawn spatial (a southern hinterland lane) so the density test has all 8 on the raster |

Decisions: 8 country · 0 merged-into · 0 dropped. Country count 8 < SPEC.md §4.3 upper bound of 9.

Notes for P3-T12 review (A-K7 band/biome judgement calls): `policy-governance-coast` biome highland (hand-authored rules — the only non-neural terrain on the coast) vs grassland; `alignment-interpretability-plateau` biome mixed (written constitutions + RL) vs jungle; `compute-hardware-hinterland` is drawn as territory (S2c) although AXES.md §3 says "frameworks/hardware → roads, not places" — deliberate for the Phase-1 density stress-test, revisit when the hardware river (file 09d) is drawn; `reasoning-test-time-compute` starts 2024 (GRPO Feb 2024 / o1 Sep 2024) so N2 west of it stays parent jungle. Research/08 "Map notes" suggested A2 labels by *institution* (OpenAI, Anthropic, Google DeepMind, Meta/Llama Commons, Mistral & the European Shore, DeepSeek/Qwen, Nvidia hinterland); P3-T10 follows the `## Schools of thought` bullets instead, per SPEC.md A-K2 — institutions become cities (P4) inside these countries.

## Table 2 — cities (P4-T10, not started)
