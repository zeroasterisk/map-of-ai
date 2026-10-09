---
type: Lineage Road
title: The Mistral 7B & Mixtral European Open-Weights Spur
description: 'Traces Mistral AI''s open-weights releases founded by former Meta LLaMA and Google DeepMind researchers: branching
  from LLaMA (Feb 2023) to Mistral 7B (Sep 2023) and Mixtral 8x7B Sparse MoE (Dec 2023).'
road_id: spur-mistral-open
road_tier: spur
stop_count: 3
status: active
generated:
  by: gemini-4-argon/1.0
  at: '2026-10-08T20:15:00Z'
verified:
- by: human:zeroasterisk
  at: '2026-10-08T20:15:00Z'
sources:
- resource: https://arxiv.org/abs/2302.13971
  title: Touvron et al., LLaMA, arXiv 2302.13971 [28]
- resource: https://en.wikipedia.org/wiki/Llama_%28language_model%29
  title: 'Wikipedia: Llama (language model) [9]'
- resource: https://ai.meta.com/blog/large-language-model-llama-meta-ai/
  title: Meta AI, Introducing LLaMA, 24 Feb 2023 [10]
- resource: https://arxiv.org/abs/2310.06825
  title: Jiang et al., Mistral 7B, arXiv 2310.06825 [40]
- resource: https://mistral.ai/news/announcing-mistral-7b
  title: Mistral blog, 27 Sep 2023 [40]
- resource: https://en.wikipedia.org/wiki/Mistral_AI
  title: 'Wikipedia: Mistral AI [12]'
- resource: https://arxiv.org/abs/2401.04088
  title: Jiang et al., Mixtral of Experts, arXiv 2401.04088 [41]
- resource: https://mistral.ai/news/mixtral-of-experts
  title: Mistral blog, 11 Dec 2023 [41]
---

# The Mistral 7B & Mixtral European Open-Weights Spur

**Road ID**: `spur-mistral-open` · **Hierarchy Class**: `spur` · **Stops**: `3` · [Back to Roads Index](/roads/index.md)

## Historical & Architectural Rationale

Traces Mistral AI's open-weights releases founded by former Meta LLaMA and Google DeepMind researchers: branching from LLaMA (Feb 2023) to Mistral 7B (Sep 2023) and Mixtral 8x7B Sparse MoE (Dec 2023).

## 3-Test Knowledge Graph Audit

- **Lawyer Test**: Separates Mistral AI's Apache-2.0 open-weights models (`mistral7b-2023`, `mixtral-2023`) from Meta Llama, Google Gemma, and DeepSeek.
- **Reddit Test**: Reflects the historical fact that Mistral AI's founders (Guillaume Lample and Timothée Lacroix, co-creators of Meta's LLaMA, with Arthur Mensch from DeepMind) launched Mistral 7B and Mixtral 8x7B in late 2023.
- **Individuals Involved Test**: Arthur Mensch, Guillaume Lample, and Timothée Lacroix's Mistral AI lineage is cleanly represented.

## Ordered Milestone Stops (West → East)

| # | Year | Milestone | Province | One-Line Summary |
|---|------|-----------|----------|------------------|
| 1 | `2023.15` | [LLaMA leak](/milestones/llama-leak-2023.md) | [The Open-Weights Commons](/provinces/open-weights-movement.md) | Meta's LLaMA (24 Feb 2023) leaks via 4chan torrent 3 Mar; the open-weights ecosystem ignites |
| 2 | `2023.74` | [Mistral 7B](/milestones/mistral7b-2023.md) | [The Open-Weights Commons](/provinces/open-weights-movement.md) | Mistral 7B under Apache 2.0 (27 Sep 2023): Europe's open-weights champion |
| 3 | `2023.95` | [Mixtral 8x7B](/milestones/mixtral-2023.md) | [The Open-Weights Commons](/provinces/open-weights-movement.md) | Mixtral 8x7B (11 Dec 2023): open sparse mixture-of-experts matches GPT-3.5 |

## Directed Road Segments

- [LLaMA leak](/milestones/llama-leak-2023.md) (`2023.15`) → [Mistral 7B](/milestones/mistral7b-2023.md) (`2023.74`)
- [Mistral 7B](/milestones/mistral7b-2023.md) (`2023.74`) → [Mixtral 8x7B](/milestones/mixtral-2023.md) (`2023.95`)
