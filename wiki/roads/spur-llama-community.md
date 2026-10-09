---
type: Lineage Road
title: The Local Llama, llama.cpp, LLaVA & QLoRA Community Spur
description: 'Traces the March–May 2023 open-source community explosion sparked by Meta''s LLaMA release (`llama-leak-2023`):
  Georgi Gerganov''s `llama.cpp` & Stanford Alpaca (`llamacpp-alpaca-2023`), Liu et al.''s LLaVA visual instruction tuning
  on LLaMA (`llava-2023`), and Dettmers et al.''s 4-bit QLoRA fine-tuning (`qlora-2023`).'
road_id: spur-llama-community
road_tier: spur
stop_count: 4
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
- resource: https://arxiv.org/abs/2304.08485
  title: Liu et al., Visual Instruction Tuning (LLaVA), arXiv 2304.08485 [82]
- resource: https://arxiv.org/abs/2305.14314
  title: Dettmers et al., QLoRA, arXiv 2305.14314 [30]
---

# The Local Llama, llama.cpp, LLaVA & QLoRA Community Spur

**Road ID**: `spur-llama-community` · **Hierarchy Class**: `spur` · **Stops**: `4` · [Back to Roads Index](/roads/index.md)

## Historical & Architectural Rationale

Traces the March–May 2023 open-source community explosion sparked by Meta's LLaMA release (`llama-leak-2023`): Georgi Gerganov's `llama.cpp` & Stanford Alpaca (`llamacpp-alpaca-2023`), Liu et al.'s LLaVA visual instruction tuning on LLaMA (`llava-2023`), and Dettmers et al.'s 4-bit QLoRA fine-tuning (`qlora-2023`).

## 3-Test Knowledge Graph Audit

- **Lawyer Test**: Open-source community ecosystem explicitly built on LLaMA weights/architectures.
- **Reddit Test**: The founding mythos of `r/LocalLLaMA`: `LLaMA -> llama.cpp / Alpaca -> LLaVA -> QLoRA`.
- **Individuals Involved Test**: Georgi Gerganov, Percy Liang/Tatsu Hashimoto (Alpaca), Haotian Liu (LLaVA), and Tim Dettmers (QLoRA) are linked directly to the LLaMA release they built upon.

## Ordered Milestone Stops (West → East)

| # | Year | Milestone | Province | One-Line Summary |
|---|------|-----------|----------|------------------|
| 1 | `2023.15` | [LLaMA leak](/milestones/llama-leak-2023.md) | [The Open-Weights Commons](/provinces/open-weights-movement.md) | Meta's LLaMA (24 Feb 2023) leaks via 4chan torrent 3 Mar; the open-weights ecosystem ignites |
| 2 | `2023.22` | [llama.cpp · Alpaca · Vicuna](/milestones/llamacpp-alpaca-2023.md) | [The Open-Weights Commons](/provinces/open-weights-movement.md) | llama.cpp (10 Mar), Alpaca (13 Mar), Vicuna (30 Mar): local inference and cheap fine-tunes |
| 3 | `2023.3` | [LLaVA](/milestones/llava-2023.md) | [The Open-Weights Commons](/provinces/open-weights-movement.md) | Visual instruction tuning grafts a vision encoder onto an open LLM (17 Apr 2023) |
| 4 | `2023.39` | [QLoRA](/milestones/qlora-2023.md) | [The Open-Weights Commons](/provinces/open-weights-movement.md) | Dettmers et al. (May 2023): 4-bit NormalFloat quantization fine-tunes 65B models on one GPU |

## Directed Road Segments

- [LLaMA leak](/milestones/llama-leak-2023.md) (`2023.15`) → [llama.cpp · Alpaca · Vicuna](/milestones/llamacpp-alpaca-2023.md) (`2023.22`)
- [llama.cpp · Alpaca · Vicuna](/milestones/llamacpp-alpaca-2023.md) (`2023.22`) → [LLaVA](/milestones/llava-2023.md) (`2023.3`)
- [LLaVA](/milestones/llava-2023.md) (`2023.3`) → [QLoRA](/milestones/qlora-2023.md) (`2023.39`)
