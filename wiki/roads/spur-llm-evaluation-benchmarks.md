---
type: Lineage Road
title: The MMLU, BIG-bench & ARC Prize Reasoning Evaluation Spur
description: Traces frontier reasoning benchmarks from Hendrycks et al.'s MMLU (Sep 2020) and Srivastava et al.'s 204-task
  BIG-bench (Jun 2022) to Chollet & Knoop's $1 M ARC Prize on ARC-AGI (Jun 2024) and OpenAI's o1/o3 reasoning models evaluated
  on ARC-AGI (Dec 2024).
road_id: spur-llm-evaluation-benchmarks
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
- resource: https://arxiv.org/abs/2009.03300
  title: Hendrycks et al., MMLU, arXiv 2009.03300 [63]
- resource: https://arcprize.org/
  title: ARC Prize Foundation (arcprize.org), Jun 2024 [121]
- resource: https://en.wikipedia.org/wiki/OpenAI_o1
  title: 'Wikipedia: OpenAI o1 [14]'
- resource: https://en.wikipedia.org/wiki/OpenAI_o3
  title: 'Wikipedia: OpenAI o3 [59]'
---

# The MMLU, BIG-bench & ARC Prize Reasoning Evaluation Spur

**Road ID**: `spur-llm-evaluation-benchmarks` · **Hierarchy Class**: `spur` · **Stops**: `4` · [Back to Roads Index](/roads/index.md)

## Historical & Architectural Rationale

Traces frontier reasoning benchmarks from Hendrycks et al.'s MMLU (Sep 2020) and Srivastava et al.'s 204-task BIG-bench (Jun 2022) to Chollet & Knoop's $1 M ARC Prize on ARC-AGI (Jun 2024) and OpenAI's o1/o3 reasoning models evaluated on ARC-AGI (Dec 2024).

## 3-Test Knowledge Graph Audit

- **Lawyer Test**: Academic and public evaluation benchmarks (`MMLU -> BIG-bench -> ARC Prize -> o1/o3 preview`).
- **Reddit Test**: ARC Prize (June 2024) and the December 2024 o1/o3 ARC-AGI evaluation were the defining reasoning benchmark storyline of 2024.
- **Individuals Involved Test**: Dan Hendrycks, Aarohi Srivastava, and François Chollet's evaluation benchmarks are linked in chronological sequence.

## Ordered Milestone Stops (West → East)

| # | Year | Milestone | Province | One-Line Summary |
|---|------|-----------|----------|------------------|
| 1 | `2020.68` | [MMLU](/milestones/mmlu-2020.md) | [The Scaling-Law Fault Line](/provinces/scaling-law-empiricists.md) | Hendrycks et al. (7 Sep 2020): 57 subjects, ~16 k questions; the yardstick to GPT-4 |
| 2 | `2022.44` | [BIG-bench](/milestones/big-bench-2022.md) | [The Scaling-Law Fault Line](/provinces/scaling-law-empiricists.md) | 204 tasks, ~450 authors (9 Jun 2022): evaluation becomes a discipline |
| 3 | `2024.44` | [ARC Prize Launched](/milestones/arc-prize-2024.md) | [Reasoning Ridge](/provinces/reasoning-test-time-compute.md) | François Chollet and Mike Knoop launch the $1M ARC Prize for novel fluid reasoning (Jun 2024) |
| 4 | `2024.93` | [o1 & o3 preview](/milestones/o1-2024.md) | [Reasoning Ridge](/provinces/reasoning-test-time-compute.md) | Full o1 ships (5 Dec 2024); o3 announced 20 Dec at 87.5 % on ARC-AGI |

## Directed Road Segments

- [MMLU](/milestones/mmlu-2020.md) (`2020.68`) → [BIG-bench](/milestones/big-bench-2022.md) (`2022.44`)
- [BIG-bench](/milestones/big-bench-2022.md) (`2022.44`) → [ARC Prize Launched](/milestones/arc-prize-2024.md) (`2024.44`)
- [ARC Prize Launched](/milestones/arc-prize-2024.md) (`2024.44`) → [o1 & o3 preview](/milestones/o1-2024.md) (`2024.93`)
