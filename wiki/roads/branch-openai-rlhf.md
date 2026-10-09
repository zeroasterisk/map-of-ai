---
type: Lineage Road
title: The OpenAI Gym, PPO & RLHF Alignment Road
description: Traces OpenAI's reinforcement learning and alignment lineage from OpenAI founded (2015) and OpenAI Gym (2016)
  through Schulman et al.'s PPO (July 2017), Christiano et al.'s Deep RL from Human Preferences (June 2017, chronological
  order), Ouyang et al.'s InstructGPT (2022), Rafailov et al.'s DPO (2023), OpenAI Preparedness Framework (2023), to Deliberative
  Alignment (2024).
road_id: branch-openai-rlhf
road_tier: branch
stop_count: 8
status: active
generated:
  by: gemini-4-argon/1.0
  at: '2026-10-08T20:15:00Z'
verified:
- by: human:zeroasterisk
  at: '2026-10-08T20:15:00Z'
sources:
- resource: https://en.wikipedia.org/wiki/OpenAI
  title: 'Wikipedia: OpenAI [45]'
- resource: https://arxiv.org/abs/2203.02155
  title: Ouyang et al., InstructGPT, arXiv 2203.02155 [19]
- resource: https://arxiv.org/abs/2412.16339
  title: Guan et al., Deliberative Alignment, arXiv 2412.16339 [88]
---

# The OpenAI Gym, PPO & RLHF Alignment Road

**Road ID**: `branch-openai-rlhf` · **Hierarchy Class**: `branch` · **Stops**: `8` · [Back to Roads Index](/roads/index.md)

## Historical & Architectural Rationale

Traces OpenAI's reinforcement learning and alignment lineage from OpenAI founded (2015) and OpenAI Gym (2016) through Schulman et al.'s PPO (July 2017), Christiano et al.'s Deep RL from Human Preferences (June 2017, chronological order), Ouyang et al.'s InstructGPT (2022), Rafailov et al.'s DPO (2023), OpenAI Preparedness Framework (2023), to Deliberative Alignment (2024).

## 3-Test Knowledge Graph Audit

- **Lawyer Test**: Keeps OpenAI's RLHF and Preparedness alignment lineage distinct from Anthropic's Constitutional AI and RSP.
- **Reddit Test**: Fixes the chronological order (`human-preferences-2017` 2017.45 -> `ppo-schulman-2017` 2017.55) and shows how DPO (2023) directly reformulated the Christiano/InstructGPT RLHF objective.
- **Individuals Involved Test**: Paul Christiano, John Schulman, Long Ouyang, and Rafael Rafailov's RLHF/DPO lineage is accurately represented.

## Ordered Milestone Stops (West → East)

| # | Year | Milestone | Province | One-Line Summary |
|---|------|-----------|----------|------------------|
| 1 | `2015.92` | [OpenAI founded](/milestones/openai-2015.md) | [The Corporate Lab Colonies](/provinces/industrial-lab-founders.md) | non-profit founded Dec 2015 by Musk, Altman, Sutskever, Brockman and others |
| 2 | `2016.45` | [OpenAI Gym](/milestones/gym-2016.md) | [The AlphaGo Delta](/provinces/deep-rl-delta.md) | Brockman et al.: the shared benchmark arena for deep RL |
| 3 | `2017.45` | [RL from Human Preferences](/milestones/human-preferences-2017.md) | [The Human-Feedback Tributaries](/provinces/alignment-critique-tributaries.md) | Christiano et al. (Jun 2017): reward models from human comparisons; the RLHF canal's source |
| 4 | `2017.55` | [PPO Algorithm](/milestones/ppo-schulman-2017.md) | [The AlphaGo Delta](/provinces/deep-rl-delta.md) | John Schulman et al. introduce Proximal Policy Optimization (PPO) for stable deep RL |
| 5 | `2022.17` | [InstructGPT](/milestones/instructgpt-2022.md) | [The Autoregressive Ridge](/provinces/decoder-generative-school.md) | Ouyang et al. (4 Mar 2022): SFT → reward model → PPO; ChatGPT's RLHF recipe |
| 6 | `2023.41` | [DPO](/milestones/dpo-2023.md) | [The Alignment Plateau](/provinces/alignment-interpretability-plateau.md) | Rafailov et al. (29 May 2023): direct preference optimisation replaces RLHF's reward model + PPO |
| 7 | `2023.96` | [Preparedness Framework](/milestones/openai-preparedness-2023.md) | [The Alignment Plateau](/provinces/alignment-interpretability-plateau.md) | OpenAI publishes its Preparedness Framework (18 Dec 2023) scoring CBRN, cyber, and autonomy |
| 8 | `2024.97` | [Deliberative Alignment](/milestones/deliberative-alignment-2024.md) | [The Alignment Plateau](/provinces/alignment-interpretability-plateau.md) | Guan et al. (Dec 2024) train reasoning models to explicitly reason over safety specifications |

## Directed Road Segments

- [OpenAI founded](/milestones/openai-2015.md) (`2015.92`) → [OpenAI Gym](/milestones/gym-2016.md) (`2016.45`)
- [OpenAI Gym](/milestones/gym-2016.md) (`2016.45`) → [RL from Human Preferences](/milestones/human-preferences-2017.md) (`2017.45`)
- [RL from Human Preferences](/milestones/human-preferences-2017.md) (`2017.45`) → [PPO Algorithm](/milestones/ppo-schulman-2017.md) (`2017.55`)
- [PPO Algorithm](/milestones/ppo-schulman-2017.md) (`2017.55`) → [InstructGPT](/milestones/instructgpt-2022.md) (`2022.17`)
- [InstructGPT](/milestones/instructgpt-2022.md) (`2022.17`) → [DPO](/milestones/dpo-2023.md) (`2023.41`)
- [DPO](/milestones/dpo-2023.md) (`2023.41`) → [Preparedness Framework](/milestones/openai-preparedness-2023.md) (`2023.96`)
- [Preparedness Framework](/milestones/openai-preparedness-2023.md) (`2023.96`) → [Deliberative Alignment](/milestones/deliberative-alignment-2024.md) (`2024.97`)
