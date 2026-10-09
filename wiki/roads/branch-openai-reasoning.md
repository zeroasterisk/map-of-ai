---
type: Lineage Road
title: The OpenAI o1, o3 & Test-Time Reasoning Branch
description: Traces OpenAI's reinforcement-learned chain-of-thought reasoning models from GPT-4o (May 2024) through o1-preview
  (Sep 2024), full o1 & o3 preview (Dec 2024), and o3 / o4-mini (Apr 2025) into GPT-5 (Aug 2025).
road_id: branch-openai-reasoning
road_tier: branch
stop_count: 5
status: active
generated:
  by: gemini-4-argon/1.0
  at: '2026-10-08T20:15:00Z'
verified:
- by: human:zeroasterisk
  at: '2026-10-08T20:15:00Z'
sources:
- resource: https://en.wikipedia.org/wiki/GPT-4o
  title: 'Wikipedia: GPT-4o [49]'
- resource: https://en.wikipedia.org/wiki/OpenAI_o1
  title: 'Wikipedia: OpenAI o1 [14]'
- resource: https://en.wikipedia.org/wiki/OpenAI_o3
  title: 'Wikipedia: OpenAI o3 [59]'
- resource: https://en.wikipedia.org/wiki/GPT-5
  title: 'Wikipedia: GPT-5 [62]'
---

# The OpenAI o1, o3 & Test-Time Reasoning Branch

**Road ID**: `branch-openai-reasoning` · **Hierarchy Class**: `branch` · **Stops**: `5` · [Back to Roads Index](/roads/index.md)

## Historical & Architectural Rationale

Traces OpenAI's reinforcement-learned chain-of-thought reasoning models from GPT-4o (May 2024) through o1-preview (Sep 2024), full o1 & o3 preview (Dec 2024), and o3 / o4-mini (Apr 2025) into GPT-5 (Aug 2025).

## 3-Test Knowledge Graph Audit

- **Lawyer Test**: 100% OpenAI reasoning model lineage; removes the false spur `o1-2024 -> turing-rl-2025` (Sutton & Barto's Turing Award).
- **Reddit Test**: Cleanly separates OpenAI's `o1-preview -> o1 -> o3 -> gpt5` reasoning line from DeepSeek-R1 (`branch-deepseek-moe`) and academic Sutton & Barto RL (`branch-sutton-barto-turing`).
- **Individuals Involved Test**: Noam Brown, Hunter Lightman, and OpenAI's reasoning team are connected along their actual o-series releases.

## Ordered Milestone Stops (West → East)

| # | Year | Milestone | Province | One-Line Summary |
|---|------|-----------|----------|------------------|
| 1 | `2024.36` | [GPT-4o](/milestones/gpt4o-2024.md) | [The Closed Frontier](/provinces/closed-frontier-labs.md) | GPT-4o "omni" (13 May 2024): real-time voice, vision and text in one model |
| 2 | `2024.7` | [o1-preview](/milestones/o1-preview-2024.md) | [Reasoning Ridge](/provinces/reasoning-test-time-compute.md) | OpenAI o1-preview (12 Sep 2024): RL-trained to think before answering; test-time compute scales |
| 3 | `2024.93` | [o1 & o3 preview](/milestones/o1-2024.md) | [Reasoning Ridge](/provinces/reasoning-test-time-compute.md) | Full o1 ships (5 Dec 2024); o3 announced 20 Dec at 87.5 % on ARC-AGI |
| 4 | `2025.29` | [o3 · o4-mini](/milestones/o3-2025.md) | [Reasoning Ridge](/provinces/reasoning-test-time-compute.md) | o3 and o4-mini (16 Apr 2025): native tool use inside the chain of thought |
| 5 | `2025.6` | [GPT-5](/milestones/gpt5-2025.md) | [The Closed Frontier](/provinces/closed-frontier-labs.md) | GPT-5 (7 Aug 2025) unifies GPT-4o and o3-series reasoning behind one adaptive router |

## Directed Road Segments

- [GPT-4o](/milestones/gpt4o-2024.md) (`2024.36`) → [o1-preview](/milestones/o1-preview-2024.md) (`2024.7`)
- [o1-preview](/milestones/o1-preview-2024.md) (`2024.7`) → [o1 & o3 preview](/milestones/o1-2024.md) (`2024.93`)
- [o1 & o3 preview](/milestones/o1-2024.md) (`2024.93`) → [o3 · o4-mini](/milestones/o3-2025.md) (`2025.29`)
- [o3 · o4-mini](/milestones/o3-2025.md) (`2025.29`) → [GPT-5](/milestones/gpt5-2025.md) (`2025.6`)
