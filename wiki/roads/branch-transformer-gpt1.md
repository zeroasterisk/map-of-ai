---
type: Lineage Road
title: The Transformer–GPT Decoder Fork
description: Alec Radford et al. (June 2018) adapted Vaswani et al.'s 2017 Transformer into a decoder-only architecture for
  generative pre-training (GPT-1), and Kaplan et al.'s Scaling Laws (Jan 2020) directly guided the training of GPT-3 (May
  2020).
road_id: branch-transformer-gpt1
road_tier: branch
stop_count: 4
status: active
generated:
  by: gemini-4-argon/1.0
  at: '2026-10-08T20:15:00Z'
verified:
- by: human:zeroasterisk
  at: '2026-10-08T20:15:00Z'
sources:
- resource: https://arxiv.org/abs/1706.03762
  title: Vaswani et al., Attention Is All You Need, arXiv 1706.03762 [1]
- resource: https://en.wikipedia.org/wiki/Attention_Is_All_You_Need
  title: 'Wikipedia: Attention Is All You Need [2]'
- resource: https://en.wikipedia.org/wiki/Transformer_%28deep_learning_architecture%29
  title: 'Wikipedia: Transformer [3]'
- resource: https://arxiv.org/abs/2001.08361
  title: Kaplan et al., Scaling Laws, arXiv 2001.08361 [9]
- resource: https://en.wikipedia.org/wiki/Neural_scaling_law
  title: 'Wikipedia: Neural scaling law [10]'
- resource: https://arxiv.org/abs/2005.14165
  title: Brown et al., GPT-3, arXiv 2005.14165 [11]
- resource: https://en.wikipedia.org/wiki/GPT-3
  title: 'Wikipedia: GPT-3 [12]'
---

# The Transformer–GPT Decoder Fork

**Road ID**: `branch-transformer-gpt1` · **Hierarchy Class**: `branch` · **Stops**: `4` · [Back to Roads Index](/roads/index.md)

## Historical & Architectural Rationale

Alec Radford et al. (June 2018) adapted Vaswani et al.'s 2017 Transformer into a decoder-only architecture for generative pre-training (GPT-1), and Kaplan et al.'s Scaling Laws (Jan 2020) directly guided the training of GPT-3 (May 2020).

## 3-Test Knowledge Graph Audit

- **Lawyer Test**: Cites public academic paper lineage (`Attention Is All You Need` -> `Improving Language Understanding by Generative Pre-Training` -> `Scaling Laws for Neural Language Models` -> `Language Models are Few-Shot Learners`).
- **Reddit Test**: The foundational fork of modern LLMs: how Google Brain's 2017 Transformer paper was adapted into OpenAI's decoder-only GPT line.
- **Individuals Involved Test**: Explicitly cited in the first paragraphs of Radford et al. (2018), Kaplan et al. (2020), and Brown et al. (2020).

## Ordered Milestone Stops (West → East)

| # | Year | Milestone | Province | One-Line Summary |
|---|------|-----------|----------|------------------|
| 1 | `2017.45` | [Attention Is All You Need](/milestones/attention-is-all-you-need-2017.md) | [The Mixture-of-Experts Delta](/provinces/sparse-moe-engineers.md) | Vaswani et al. (12 Jun 2017): self-attention replaces recurrence — the Transformer; eight Google authors |
| 2 | `2018.45` | [GPT-1](/milestones/gpt1-2018.md) | [The Autoregressive Ridge](/provinces/decoder-generative-school.md) | Radford et al. (Jun 2018): decoder-only Transformer, generative pre-training, 117 M parameters |
| 3 | `2020.06` | [Scaling Laws](/milestones/scaling-laws-2020.md) | [The Scaling-Law Fault Line](/provinces/scaling-law-empiricists.md) | Kaplan et al. (23 Jan 2020): loss is a power law in parameters, data, compute |
| 4 | `2020.41` | [GPT-3](/milestones/gpt3-2020.md) | [The Autoregressive Ridge](/provinces/decoder-generative-school.md) | Brown et al. (28 May 2020): 175 B parameters; few-shot in-context learning; API 11 Jun |

## Directed Road Segments

- [Attention Is All You Need](/milestones/attention-is-all-you-need-2017.md) (`2017.45`) → [GPT-1](/milestones/gpt1-2018.md) (`2018.45`)
- [GPT-1](/milestones/gpt1-2018.md) (`2018.45`) → [Scaling Laws](/milestones/scaling-laws-2020.md) (`2020.06`)
- [Scaling Laws](/milestones/scaling-laws-2020.md) (`2020.06`) → [GPT-3](/milestones/gpt3-2020.md) (`2020.41`)
