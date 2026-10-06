# Coverage matrix — transformer-plateau

Continent: `transformer-plateau` · Research file: `research/07-transformers-and-llms-2017-2022.md` · Date: 2026-09-18 · Schools of thought bullets: 9 · Units: P2-T9 (header), P3-T9 (Table 1)

Check A-M2: `awk '/^## Schools of thought/{f=1;next} /^## /{f=0} f&&/^- /{n++} END{print n}' research/07-transformers-and-llms-2017-2022.md` → 9 = Table 1 rows.

## Table 1 — schools of thought → countries (P3-T9)

| # | school bullet | decision | entity id | reason |
|---|---|---|---|---|
| 1 | Encoder camp (BERT lineage) | country | `encoder-understanding-school` | own lineage (ULMFiT/ELMo → BERT → RoBERTa/T5) and own benchmark street (GLUE/SuperGLUE); ends 2020 where RAG/RETRO hand to the decoder camp |
| 2 | Decoder / generative camp (GPT lineage) | country | `decoder-generative-school` | the winning ridge (GPT-1/2/3 → Codex → InstructGPT); continuous with the coast's `closed-frontier-labs` across the 30 Nov 2022 border |
| 3 | Scaling-law empiricists | country | `scaling-law-empiricists` | distinct method (power laws, compute-optimal training) and distinct debate (emergence); research/07 map notes' "fault line" |
| 4 | Sparse / mixture-of-experts engineers | country | `sparse-moe-engineers` | own architectural idiom (Shazeer 2017 → GShard → Switch); pre-dates the Transformer and returns as Mixtral/DeepSeek, so kept separate from the systems yards |
| 5 | Systems & infrastructure engineers | country | `systems-infrastructure-axis` | Megatron-LM / ZeRO-DeepSpeed / A100 / Pathways; drawn as harbour territory (S2a) on the `compute-hardware-hinterland` A-K7 precedent so the plateau's southern road lands on the raster |
| 6 | Multimodal & scientific Transformers | country | `multimodal-scientific-transformers` | attention leaving language (ViT, CLIP, AlphaFold 2, Gato, Whisper); AlphaFold kept inside rather than a "science AI" enclave (research/07 open question 1) |
| 7 | Alignment and critique tributaries | country | `alignment-critique-tributaries` | two thin northern tributaries (RLHF; Stochastic Parrots / foundation-model critique) with distinct sources; the plateau's own northern cape, hands to `alignment-interpretability-plateau` |
| 8 | Open-replication commons | country | `open-replication-commons` | EleutherAI / Hugging Face / OPT / BLOOM / YaLM; the open-vs-closed road's first waystations, continuous with the coast's `open-weights-movement` (both Cb) |
| 9 | National-champion scalers outside the Bay Area | country | `national-champion-scalers` | own citations ([74]–[77], [94]) and subject (institutional geography, not openness), so not merged; but `spatial: false` — a 2021–22 enclave would need the commons' Cb cells — surfaced as a `related_facts` hover note on `open-replication-commons` (tooling-guild / pretraining-foothills precedent) |

Decisions: 9 country (8 spatial + 1 `spatial: false`) · 0 merged-into · 0 dropped. Country count 9 = SPEC.md §4.3 upper bound.

Placement (one lane each on the plateau's own grid rows — the atlas grid gives the plateau N2b–S2a from 2017, N2a from 2019.6, and S1/S2a only until 2021.3; it never owns N1): N2a alignment/critique (2017–22, drawn 2019.6–) · N2b scaling laws (2019–) · Ca decoder/GPT (2018–) · Cb encoder/BERT (2018–20) then open-replication commons (2020–) · S1a sparse MoE (2017–21) · S1b multimodal (2020–) · S2a systems yards (2019–22, drawn to 2021.3). `site/atlas.html` `kEnd` now snaps a country's end to the next continent column boundary when within the 0.8-yr LICENSE slack (2022 → 2022.8 belt; 2021 → 2021.3 seam) so no orphan slivers of parent land remain; `SUBCOLS` gained 2018 and 2020.

Notes for P3-T12 review (A-K7 band/biome judgement calls): `alignment-critique-tributaries` N2a rather than a literal N1 (the plateau's territory never reaches N1; parent band still lists N1 for the continent span); `multimodal-scientific-transformers` S1b rather than a literal S2 (S2a is owned only to 2021.3, the school runs 2020–22); `scaling-law-empiricists` N2b grassland; `systems-infrastructure-axis` harbour territory vs "hardware → roads"; `encoder-understanding-school` forest and `open-replication-commons` grassland inside a jungle continent; `national-champion-scalers` highland, non-spatial. Research/07 "Map notes" suggest A2 labels by lineage ("GPT-Land / BERT-Land", "Scaling Law fault line", "Alignment tributary"); P3-T9 follows the `## Schools of thought` bullets per SPEC.md A-K2 — institutions (OpenAI, Google Brain, DeepMind, Meta AI, EleutherAI, BAAI) become cities (P4).

## Table 2 — cities (P4-T9, not started)
