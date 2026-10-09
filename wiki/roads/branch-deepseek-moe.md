---
type: Lineage Road
title: The DeepSeek MoE, GRPO & R1 Reasoning Road
description: Traces DeepSeek's sparse Mixture-of-Experts and Group Relative Policy Optimization (GRPO) reasoning lineage from
  foundational Sparsely-Gated MoE (2017) through DeepSeekMath & GRPO (Feb 2024), DeepSeek-V2 MLA/MoE (May 2024), DeepSeek-V3
  (Dec 2024), to DeepSeek-R1 (Jan 2025) and Moonshot Kimi K2 (Jul 2025).
road_id: branch-deepseek-moe
road_tier: branch
stop_count: 6
status: active
generated:
  by: gemini-4-argon/1.0
  at: '2026-10-08T20:15:00Z'
verified:
- by: human:zeroasterisk
  at: '2026-10-08T20:15:00Z'
sources:
- resource: https://arxiv.org/abs/1701.06538
  title: Shazeer et al., Outrageously Large Neural Networks, arXiv 1701.06538 [27]
- resource: https://arxiv.org/abs/2412.19437
  title: DeepSeek-V3 Technical Report, arXiv 2412.19437 [52]
- resource: https://en.wikipedia.org/wiki/DeepSeek
  title: 'Wikipedia: DeepSeek [13]'
- resource: https://arxiv.org/abs/2507.20534
  title: 'Kimi Team, Kimi K2: Open Agentic Intelligence, arXiv 2507.20534 [109]'
- resource: https://en.wikipedia.org/wiki/Kimi_%28chatbot%29
  title: 'Wikipedia: Kimi (chatbot) [64]'
---

# The DeepSeek MoE, GRPO & R1 Reasoning Road

**Road ID**: `branch-deepseek-moe` · **Hierarchy Class**: `branch` · **Stops**: `6` · [Back to Roads Index](/roads/index.md)

## Historical & Architectural Rationale

Traces DeepSeek's sparse Mixture-of-Experts and Group Relative Policy Optimization (GRPO) reasoning lineage from foundational Sparsely-Gated MoE (2017) through DeepSeekMath & GRPO (Feb 2024), DeepSeek-V2 MLA/MoE (May 2024), DeepSeek-V3 (Dec 2024), to DeepSeek-R1 (Jan 2025) and Moonshot Kimi K2 (Jul 2025).

## 3-Test Knowledge Graph Audit

- **Lawyer Test**: Eliminates the false nearest-neighbor spur `grpo-2024 -> imo-silver-2024` (which linked DeepSeek's GRPO to Google DeepMind's AlphaProof/AlphaGeometry 2) and separates DeepSeek from Meta Llama and Google Gemma.
- **Reddit Test**: Connects `grpo-2024` (introduced in DeepSeekMath, Feb 2024) directly to `deepseek-v2-2024 -> deepseek-v3-2024 -> deepseek-r1-2025 -> kimi-k2-2025`, the exact architecture and RL pipeline of DeepSeek-R1.
- **Individuals Involved Test**: Zhihong Shao, Daya Guo, Liang Wenfeng, and the DeepSeek / Moonshot teams are credited accurately along their own MoE + GRPO lineage.

## Ordered Milestone Stops (West → East)

| # | Year | Milestone | Province | One-Line Summary |
|---|------|-----------|----------|------------------|
| 1 | `2017.06` | [sparsely-gated MoE](/milestones/sparse-moe-2017.md) | [The Mixture-of-Experts Delta](/provinces/sparse-moe-engineers.md) | Shazeer et al. (23 Jan 2017): "Outrageously Large Neural Networks", MoE at 100 B+ parameters |
| 2 | `2024.1` | [DeepSeekMath · GRPO](/milestones/grpo-2024.md) | [Reasoning Ridge](/provinces/reasoning-test-time-compute.md) | DeepSeekMath introduces GRPO (Feb 2024): group-relative policy optimization later used for R1 |
| 3 | `2024.35` | [DeepSeek-V2](/milestones/deepseek-v2-2024.md) | [The Open-Weights Commons](/provinces/open-weights-movement.md) | Multi-head latent attention + cheap MoE (7 May 2024) start a Chinese API price war |
| 4 | `2024.99` | [DeepSeek-V3](/milestones/deepseek-v3-2024.md) | [The Open-Weights Commons](/provinces/open-weights-movement.md) | 671 B-parameter open MoE (26 Dec 2024) trained at reported ~$5.6 M GPU cost |
| 5 | `2025.05` | [DeepSeek-R1](/milestones/deepseek-r1-2025.md) | [Reasoning Ridge](/provinces/reasoning-test-time-compute.md) | MIT-licensed DeepSeek-R1 (20 Jan 2025) matches o1 via pure RL; tops App Store 27 Jan |
| 6 | `2025.55` | [Kimi K2](/milestones/kimi-k2-2025.md) | [The Open-Weights Commons](/provinces/open-weights-movement.md) | Moonshot's 1 T-parameter open MoE (Jul 2025): trillion-parameter open weights |

## Directed Road Segments

- [sparsely-gated MoE](/milestones/sparse-moe-2017.md) (`2017.06`) → [DeepSeekMath · GRPO](/milestones/grpo-2024.md) (`2024.1`)
- [DeepSeekMath · GRPO](/milestones/grpo-2024.md) (`2024.1`) → [DeepSeek-V2](/milestones/deepseek-v2-2024.md) (`2024.35`)
- [DeepSeek-V2](/milestones/deepseek-v2-2024.md) (`2024.35`) → [DeepSeek-V3](/milestones/deepseek-v3-2024.md) (`2024.99`)
- [DeepSeek-V3](/milestones/deepseek-v3-2024.md) (`2024.99`) → [DeepSeek-R1](/milestones/deepseek-r1-2025.md) (`2025.05`)
- [DeepSeek-R1](/milestones/deepseek-r1-2025.md) (`2025.05`) → [Kimi K2](/milestones/kimi-k2-2025.md) (`2025.55`)
