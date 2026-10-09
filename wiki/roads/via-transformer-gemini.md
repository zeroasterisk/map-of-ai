---
type: Lineage Road
title: The Attention, Transformer & Google Gemini High Road
description: 'Pure Google Brain / Google Research / Google DeepMind sequence-to-sequence, Transformer, MoE, and Gemini flagship
  lineage: word2vec (2013), seq2seq (2014), GNMT (2016), Sparsely-Gated MoE (2017), Attention Is All You Need (2017), BERT
  (2018), T5 (2019), GShard (2020), Switch Transformer (2021), LaMDA (2021), Google FLAN (2021), PaLM (2022), Minerva (2022),
  PaLM 2 (2023), Gemini 1.0 (2023), Gemini 1.5 Pro (2024), Gemini 2.0 Flash (2024), Gemini 2.5 Pro (2025), Gemini 3.0 (2025),
  Gemini 3.1 Pro (2026), and Gemini 4 Argon (2026).'
road_id: via-transformer-gemini
road_tier: trunk
stop_count: 21
status: active
generated:
  by: gemini-4-argon/1.0
  at: '2026-10-08T20:15:00Z'
verified:
- by: human:zeroasterisk
  at: '2026-10-08T20:15:00Z'
sources:
- resource: https://arxiv.org/abs/1301.3781
  title: Mikolov et al., word2vec [22]
- resource: https://arxiv.org/abs/2109.01652
  title: Wei et al., FLAN, arXiv 2109.01652 [91]
- resource: https://arxiv.org/abs/2110.08207
  title: Sanh et al., T0, arXiv 2110.08207 [92]
- resource: https://deepmind.google/technologies/gemini/
  title: Google DeepMind, Gemini 4 Argon, Sep 2026 [115]
---

# The Attention, Transformer & Google Gemini High Road

**Road ID**: `via-transformer-gemini` · **Hierarchy Class**: `trunk` · **Stops**: `21` · [Back to Roads Index](/roads/index.md)

## Historical & Architectural Rationale

Pure Google Brain / Google Research / Google DeepMind sequence-to-sequence, Transformer, MoE, and Gemini flagship lineage: word2vec (2013), seq2seq (2014), GNMT (2016), Sparsely-Gated MoE (2017), Attention Is All You Need (2017), BERT (2018), T5 (2019), GShard (2020), Switch Transformer (2021), LaMDA (2021), Google FLAN (2021), PaLM (2022), Minerva (2022), PaLM 2 (2023), Gemini 1.0 (2023), Gemini 1.5 Pro (2024), Gemini 2.0 Flash (2024), Gemini 2.5 Pro (2025), Gemini 3.0 (2025), Gemini 3.1 Pro (2026), and Gemini 4 Argon (2026).

## 3-Test Knowledge Graph Audit

- **Lawyer Test**: 100% Google / Google DeepMind architectural and flagship model lineage; unbundles `flan-t0-2021` to `Google FLAN` and removes all nearest-neighbor links from `gpt4o-mini` or `grok4` into Gemini.
- **Reddit Test**: Shows the complete internal evolution from Google Brain's `word2vec -> seq2seq -> Transformer -> BERT -> T5 -> Switch -> PaLM` directly into `Gemini 1.0 -> 1.5 -> 2.0 -> 2.5 -> 3.0 -> 3.1 -> 4 Argon`.
- **Individuals Involved Test**: Credits Google Brain and Google DeepMind researchers continuously without interleaving competitor models.

## Ordered Milestone Stops (West → East)

| # | Year | Milestone | Province | One-Line Summary |
|---|------|-----------|----------|------------------|
| 1 | `2013.05` | [word2vec](/milestones/word2vec-2013.md) | [The Attention Headwaters](/provinces/neural-nlp-sequence-school.md) | Mikolov, Chen, Corrado & Dean: cheap word embeddings (arXiv 1301.3781) |
| 2 | `2014.7` | [seq2seq](/milestones/seq2seq-2014.md) | [The Attention Headwaters](/provinces/neural-nlp-sequence-school.md) | Sutskever, Vinyals & Le: LSTM encoder–decoder translates whole sentences |
| 3 | `2016.74` | [GNMT](/milestones/gnmt-2016.md) | [The Attention Headwaters](/provinces/neural-nlp-sequence-school.md) | Google's LSTM + attention translation in production (Nov 2016) |
| 4 | `2017.06` | [sparsely-gated MoE](/milestones/sparse-moe-2017.md) | [The Mixture-of-Experts Delta](/provinces/sparse-moe-engineers.md) | Shazeer et al. (23 Jan 2017): "Outrageously Large Neural Networks", MoE at 100 B+ parameters |
| 5 | `2017.45` | [Attention Is All You Need](/milestones/attention-is-all-you-need-2017.md) | [The Mixture-of-Experts Delta](/provinces/sparse-moe-engineers.md) | Vaswani et al. (12 Jun 2017): self-attention replaces recurrence — the Transformer; eight Google authors |
| 6 | `2018.78` | [BERT](/milestones/bert-2018.md) | [The BERT Escarpment](/provinces/encoder-understanding-school.md) | Devlin et al. (11 Oct 2018): encoder-only bidirectional pre-training tops GLUE, SQuAD, SWAG |
| 7 | `2019.81` | [T5 · C4](/milestones/t5-2019.md) | [The BERT Escarpment](/provinces/encoder-understanding-school.md) | Raffel et al. (23 Oct 2019): every NLP task as text-to-text; introduces the C4 corpus |
| 8 | `2020.5` | [GShard](/milestones/gshard-2020.md) | [The Mixture-of-Experts Delta](/provinces/sparse-moe-engineers.md) | Lepikhin et al. (Jun 2020): conditional computation + automatic sharding for giant MoE models |
| 9 | `2021.03` | [Switch Transformer](/milestones/switch-transformer-2021.md) | [The Mixture-of-Experts Delta](/provinces/sparse-moe-engineers.md) | Fedus, Zoph & Shazeer (11 Jan 2021): trillion-parameter sparse MoE — sparsity past dense limits |
| 10 | `2021.38` | [LaMDA](/milestones/lamda-2021.md) | [The Autoregressive Ridge](/provinces/decoder-generative-school.md) | Google's dialogue LLM announced at I/O (18 May 2021), successor to Meena |
| 11 | `2021.72` | [Google FLAN](/milestones/flan-t0-2021.md) | [The Autoregressive Ridge](/provinces/decoder-generative-school.md) | Google Research introduces FLAN (Finetuned Language Net) zero-shot instruction tuning across 60+ NLP tasks (Sep 2021) |
| 12 | `2022.26` | [PaLM · Pathways](/milestones/palm-2022.md) | [The Megatron Yards](/provinces/systems-infrastructure-axis.md) | Chowdhery et al. (5 Apr 2022): 540 B parameters on TPU v4 pods |
| 13 | `2022.5` | [Minerva](/milestones/minerva-2022.md) | [The Megatron Yards](/provinces/systems-infrastructure-axis.md) | Google (Jun 2022): PaLM fine-tuned on maths and science text for quantitative reasoning |
| 14 | `2023.36` | [PaLM 2](/milestones/palm2-2023.md) | [The Closed Frontier](/provinces/closed-frontier-labs.md) | Google unveils PaLM 2 at I/O (10 May 2023) powering Bard, Med-PaLM 2, and Sec-PaLM |
| 15 | `2023.93` | [Gemini 1.0](/milestones/gemini-2023.md) | [The Closed Frontier](/provinces/closed-frontier-labs.md) | Google announces natively multimodal Gemini 1.0 Ultra, Pro, and Nano (6 Dec 2023) |
| 16 | `2024.12` | [Gemini 1.5 Pro](/milestones/gemini15-2024.md) | [The Closed Frontier](/provinces/closed-frontier-labs.md) | Gemini 1.5 Pro (15 Feb 2024): sparse MoE unlocks 1 M to 2 M token context |
| 17 | `2024.94` | [Gemini 2.0 Flash](/milestones/gemini20-flash-2024.md) | [The Closed Frontier](/provinces/closed-frontier-labs.md) | Google ships Gemini 2.0 Flash (11 Dec 2024) built for the agentic era |
| 18 | `2025.23` | [Gemini 2.5 Pro](/milestones/gemini25-2025.md) | [Reasoning Ridge](/provinces/reasoning-test-time-compute.md) | Gemini 2.5 Pro "thinking" model (25 Mar 2025): Google takes the reasoning lead |
| 19 | `2025.88` | [Gemini 3.0](/milestones/gemini3-2025.md) | [The Closed Frontier](/provinces/closed-frontier-labs.md) | Google DeepMind launches Gemini 3.0 (18 Nov 2025) across Search, Cloud, and Workspace |
| 20 | `2026.14` | [Gemini 3.1 Pro](/milestones/gemini31-pro-2026.md) | [The Closed Frontier](/provinces/closed-frontier-labs.md) | Google releases Gemini 3.1 Pro (19 Feb 2026) advancing multimodal coding and tool use |
| 21 | `2026.72` | [Gemini 4 Argon](/milestones/gemini4-argon-2026.md) | [The Closed Frontier](/provinces/closed-frontier-labs.md) | Google DeepMind ships Gemini 4 Argon (Sep 2026): first-principles engineering, visuals, and agents |

## Directed Road Segments

- [word2vec](/milestones/word2vec-2013.md) (`2013.05`) → [seq2seq](/milestones/seq2seq-2014.md) (`2014.7`)
- [seq2seq](/milestones/seq2seq-2014.md) (`2014.7`) → [GNMT](/milestones/gnmt-2016.md) (`2016.74`)
- [GNMT](/milestones/gnmt-2016.md) (`2016.74`) → [sparsely-gated MoE](/milestones/sparse-moe-2017.md) (`2017.06`)
- [sparsely-gated MoE](/milestones/sparse-moe-2017.md) (`2017.06`) → [Attention Is All You Need](/milestones/attention-is-all-you-need-2017.md) (`2017.45`)
- [Attention Is All You Need](/milestones/attention-is-all-you-need-2017.md) (`2017.45`) → [BERT](/milestones/bert-2018.md) (`2018.78`)
- [BERT](/milestones/bert-2018.md) (`2018.78`) → [T5 · C4](/milestones/t5-2019.md) (`2019.81`)
- [T5 · C4](/milestones/t5-2019.md) (`2019.81`) → [GShard](/milestones/gshard-2020.md) (`2020.5`)
- [GShard](/milestones/gshard-2020.md) (`2020.5`) → [Switch Transformer](/milestones/switch-transformer-2021.md) (`2021.03`)
- [Switch Transformer](/milestones/switch-transformer-2021.md) (`2021.03`) → [LaMDA](/milestones/lamda-2021.md) (`2021.38`)
- [LaMDA](/milestones/lamda-2021.md) (`2021.38`) → [Google FLAN](/milestones/flan-t0-2021.md) (`2021.72`)
- [Google FLAN](/milestones/flan-t0-2021.md) (`2021.72`) → [PaLM · Pathways](/milestones/palm-2022.md) (`2022.26`)
- [PaLM · Pathways](/milestones/palm-2022.md) (`2022.26`) → [Minerva](/milestones/minerva-2022.md) (`2022.5`)
- [Minerva](/milestones/minerva-2022.md) (`2022.5`) → [PaLM 2](/milestones/palm2-2023.md) (`2023.36`)
- [PaLM 2](/milestones/palm2-2023.md) (`2023.36`) → [Gemini 1.0](/milestones/gemini-2023.md) (`2023.93`)
- [Gemini 1.0](/milestones/gemini-2023.md) (`2023.93`) → [Gemini 1.5 Pro](/milestones/gemini15-2024.md) (`2024.12`)
- [Gemini 1.5 Pro](/milestones/gemini15-2024.md) (`2024.12`) → [Gemini 2.0 Flash](/milestones/gemini20-flash-2024.md) (`2024.94`)
- [Gemini 2.0 Flash](/milestones/gemini20-flash-2024.md) (`2024.94`) → [Gemini 2.5 Pro](/milestones/gemini25-2025.md) (`2025.23`)
- [Gemini 2.5 Pro](/milestones/gemini25-2025.md) (`2025.23`) → [Gemini 3.0](/milestones/gemini3-2025.md) (`2025.88`)
- [Gemini 3.0](/milestones/gemini3-2025.md) (`2025.88`) → [Gemini 3.1 Pro](/milestones/gemini31-pro-2026.md) (`2026.14`)
- [Gemini 3.1 Pro](/milestones/gemini31-pro-2026.md) (`2026.14`) → [Gemini 4 Argon](/milestones/gemini4-argon-2026.md) (`2026.72`)
