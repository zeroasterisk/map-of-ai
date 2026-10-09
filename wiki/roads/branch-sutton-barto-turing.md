---
type: Lineage Road
title: The Sutton & Barto Reinforcement Learning Turing Award Road
description: Traces Rich Sutton and Andrew Barto's foundational reinforcement learning work from Barto-Sutton-Anderson Actor-Critic
  (1983), Sutton's TD(lambda) (1988), Watkins's Q-Learning (1989), Sutton's Dyna architecture (1990), Tesauro's TD-Gammon
  (1992), Williams's REINFORCE (1992), and Sutton & Barto's RL textbook (1998) through Sutton's Bitter Lesson essay (2019)
  to the March 2025 ACM A.M. Turing Award (`turing-rl-2025`).
road_id: branch-sutton-barto-turing
road_tier: branch
stop_count: 9
status: active
generated:
  by: gemini-4-argon/1.0
  at: '2026-10-08T20:15:00Z'
verified:
- by: human:zeroasterisk
  at: '2026-10-08T20:15:00Z'
sources:
- resource: https://doi.org/10.1109/TSMC.1983.6313077
  title: Barto et al. 1983 [60]
- resource: https://doi.org/10.1145/203330.203343
  title: Tesauro 1995 [29]
- resource: https://en.wikipedia.org/wiki/Richard_S._Sutton
  title: 'Wikipedia: Richard S. Sutton [56]'
- resource: https://en.wikipedia.org/wiki/Andrew_Barto
  title: 'Wikipedia: Andrew Barto [57]'
---

# The Sutton & Barto Reinforcement Learning Turing Award Road

**Road ID**: `branch-sutton-barto-turing` · **Hierarchy Class**: `branch` · **Stops**: `9` · [Back to Roads Index](/roads/index.md)

## Historical & Architectural Rationale

Traces Rich Sutton and Andrew Barto's foundational reinforcement learning work from Barto-Sutton-Anderson Actor-Critic (1983), Sutton's TD(lambda) (1988), Watkins's Q-Learning (1989), Sutton's Dyna architecture (1990), Tesauro's TD-Gammon (1992), Williams's REINFORCE (1992), and Sutton & Barto's RL textbook (1998) through Sutton's Bitter Lesson essay (2019) to the March 2025 ACM A.M. Turing Award (`turing-rl-2025`).

## 3-Test Knowledge Graph Audit

- **Lawyer Test**: Eliminates the false nearest-neighbor spur `o1-2024 -> turing-rl-2025` (which linked OpenAI's o1 to Sutton & Barto's ACM Turing Award).
- **Reddit Test**: Traces the exact RL milestones cited by the ACM in awarding the 2024/2025 Turing Award to Richard S. Sutton and Andrew G. Barto.
- **Individuals Involved Test**: Rich Sutton and Andy Barto's 40-year collaboration is connected directly from Actor-Critic (1983) and TD(lambda) (1988) to their textbook, The Bitter Lesson, and the Turing Award.

## Ordered Milestone Stops (West → East)

| # | Year | Milestone | Province | One-Line Summary |
|---|------|-----------|----------|------------------|
| 1 | `1983.8` | [Actor-Critic Cart-Pole](/milestones/actor-critic-1983.md) | [The Temporal Difference Valley](/provinces/temporal-difference-valley.md) | Barto, Sutton & Anderson balance cart-pole with adaptive elements |
| 2 | `1988.6` | [TD(λ) Formulation](/milestones/td-lambda-1988.md) | [The Temporal Difference Valley](/provinces/temporal-difference-valley.md) | Richard Sutton formalizes temporal-difference learning methods |
| 3 | `1989.8` | [Q-Learning](/milestones/q-learning-1989.md) | [The Temporal Difference Valley](/provinces/temporal-difference-valley.md) | Chris Watkins formulates model-free Q-learning for MDPs |
| 4 | `1990.5` | [Sutton Dyna Architecture](/milestones/dyna-architecture-1990.md) | [The Temporal Difference Valley](/provinces/temporal-difference-valley.md) | Richard Sutton's Dyna integrates model-free reinforcement learning with world-model planning |
| 5 | `1992.6` | [TD-Gammon](/milestones/td-gammon-1992.md) | [The Temporal Difference Valley](/provinces/temporal-difference-valley.md) | Gerald Tesauro: neural net plays master backgammon via TD(λ) |
| 6 | `1992.8` | [REINFORCE](/milestones/reinforce-1992.md) | [The Temporal Difference Valley](/provinces/temporal-difference-valley.md) | Ronald Williams derives foundational policy-gradient algorithm |
| 7 | `1998.7` | [Sutton & Barto RL](/milestones/sutton-barto-book-1998.md) | [The Support Vector Escarpment](/provinces/support-vector-escarpment.md) | Reinforcement Learning: An Introduction becomes standard RL text |
| 8 | `2019.2` | [The Bitter Lesson](/milestones/bitter-lesson-2019.md) | [The Scaling-Law Fault Line](/provinces/scaling-law-empiricists.md) | Sutton (13 Mar 2019): general methods that leverage computation win — the scaling creed |
| 9 | `2025.18` | [Turing Award: RL](/milestones/turing-rl-2025.md) | [Reasoning Ridge](/provinces/reasoning-test-time-compute.md) | 2024 ACM Turing Award to Barto and Sutton for reinforcement learning (5 Mar 2025) |

## Directed Road Segments

- [Actor-Critic Cart-Pole](/milestones/actor-critic-1983.md) (`1983.8`) → [TD(λ) Formulation](/milestones/td-lambda-1988.md) (`1988.6`)
- [TD(λ) Formulation](/milestones/td-lambda-1988.md) (`1988.6`) → [Q-Learning](/milestones/q-learning-1989.md) (`1989.8`)
- [Q-Learning](/milestones/q-learning-1989.md) (`1989.8`) → [Sutton Dyna Architecture](/milestones/dyna-architecture-1990.md) (`1990.5`)
- [Sutton Dyna Architecture](/milestones/dyna-architecture-1990.md) (`1990.5`) → [TD-Gammon](/milestones/td-gammon-1992.md) (`1992.6`)
- [TD-Gammon](/milestones/td-gammon-1992.md) (`1992.6`) → [REINFORCE](/milestones/reinforce-1992.md) (`1992.8`)
- [REINFORCE](/milestones/reinforce-1992.md) (`1992.8`) → [Sutton & Barto RL](/milestones/sutton-barto-book-1998.md) (`1998.7`)
- [Sutton & Barto RL](/milestones/sutton-barto-book-1998.md) (`1998.7`) → [The Bitter Lesson](/milestones/bitter-lesson-2019.md) (`2019.2`)
- [The Bitter Lesson](/milestones/bitter-lesson-2019.md) (`2019.2`) → [Turing Award: RL](/milestones/turing-rl-2025.md) (`2025.18`)
