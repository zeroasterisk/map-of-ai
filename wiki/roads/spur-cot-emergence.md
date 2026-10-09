---
type: Lineage Road
title: The Chain-of-Thought, Emergence & Test-Time Scaling Spur
description: Traces chain-of-thought prompting, emergent reasoning analysis, and academic test-time compute scaling from LaMDA
  (2021) to Wei et al.'s Chain-of-Thought Prompting (Jan 2022) and Emergent Abilities of Large Language Models (Jun 2022),
  Bubeck et al.'s Sparks of AGI (Mar 2023), Zelikman et al.'s Quiet-STaR internal rationale generation (Mar 2024), and Muennighoff
  et al.'s s1 Simple Test-Time Scaling with budget forcing (Jan 2025).
road_id: spur-cot-emergence
road_tier: spur
stop_count: 6
status: active
generated:
  by: gemini-4-argon/1.0
  at: '2026-10-08T20:15:00Z'
verified:
- by: human:zeroasterisk
  at: '2026-10-08T20:15:00Z'
sources:
- resource: https://en.wikipedia.org/wiki/LaMDA
  title: 'Wikipedia: LaMDA [35]'
- resource: https://arxiv.org/abs/2001.09977
  title: Adiwardana et al., Meena, arXiv 2001.09977 [87]
- resource: https://arxiv.org/abs/2303.12712
  title: Bubeck et al., Sparks of AGI, arXiv 2303.12712 [81]
- resource: https://arxiv.org/abs/2501.19393
  title: 'Muennighoff et al., s1: Simple test-time scaling, arXiv 2501.19393 [14]'
---

# The Chain-of-Thought, Emergence & Test-Time Scaling Spur

**Road ID**: `spur-cot-emergence` · **Hierarchy Class**: `spur` · **Stops**: `6` · [Back to Roads Index](/roads/index.md)

## Historical & Architectural Rationale

Traces chain-of-thought prompting, emergent reasoning analysis, and academic test-time compute scaling from LaMDA (2021) to Wei et al.'s Chain-of-Thought Prompting (Jan 2022) and Emergent Abilities of Large Language Models (Jun 2022), Bubeck et al.'s Sparks of AGI (Mar 2023), Zelikman et al.'s Quiet-STaR internal rationale generation (Mar 2024), and Muennighoff et al.'s s1 Simple Test-Time Scaling with budget forcing (Jan 2025).

## 3-Test Knowledge Graph Audit

- **Lawyer Test**: Academic published research papers on CoT prompting, emergence, and test-time compute scaling.
- **Reddit Test**: Stays compactly within the scaling/reasoning/alignment latitude band (`dy < 60`) without slashing vertically across the continent.
- **Individuals Involved Test**: Jason Wei, Sebastien Bubeck, Eric Zelikman, and Niklas Muennighoff's papers directly cite and build upon this CoT & emergence thread.

## Ordered Milestone Stops (West → East)

| # | Year | Milestone | Province | One-Line Summary |
|---|------|-----------|----------|------------------|
| 1 | `2021.38` | [LaMDA](/milestones/lamda-2021.md) | [The Autoregressive Ridge](/provinces/decoder-generative-school.md) | Google's dialogue LLM announced at I/O (18 May 2021), successor to Meena |
| 2 | `2022.07` | [Chain-of-Thought](/milestones/chain-of-thought-2022.md) | [The Human-Feedback Tributaries](/provinces/alignment-critique-tributaries.md) | Wei et al. (28 Jan 2022): step-by-step prompting unlocks multi-step reasoning in large models |
| 3 | `2022.46` | [Emergent Abilities](/milestones/emergent-2022.md) | [The Scaling-Law Fault Line](/provinces/scaling-law-empiricists.md) | Wei et al. (15 Jun 2022): "emergence" frames the scaling debate for the next era |
| 4 | `2023.22` | [Sparks of AGI](/milestones/sparks-agi-2023.md) | [The Alignment Plateau](/provinces/alignment-interpretability-plateau.md) | Microsoft Research argues GPT-4 shows early signs of general intelligence (22 Mar 2023) |
| 5 | `2024.21` | [Quiet-STaR](/milestones/quiet-star-2024.md) | [Reasoning Ridge](/provinces/reasoning-test-time-compute.md) | Zelikman et al. (Mar 2024) train language models to generate internal rationales before tokens |
| 6 | `2025.09` | [s1 Test-Time Scaling](/milestones/s1-test-time-scaling-2025.md) | [Reasoning Ridge](/provinces/reasoning-test-time-compute.md) | Muennighoff et al. (Feb 2025) elicit test-time reasoning on 1,000 curated examples with budget forcing |

## Directed Road Segments

- [LaMDA](/milestones/lamda-2021.md) (`2021.38`) → [Chain-of-Thought](/milestones/chain-of-thought-2022.md) (`2022.07`)
- [Chain-of-Thought](/milestones/chain-of-thought-2022.md) (`2022.07`) → [Emergent Abilities](/milestones/emergent-2022.md) (`2022.46`)
- [Emergent Abilities](/milestones/emergent-2022.md) (`2022.46`) → [Sparks of AGI](/milestones/sparks-agi-2023.md) (`2023.22`)
- [Sparks of AGI](/milestones/sparks-agi-2023.md) (`2023.22`) → [Quiet-STaR](/milestones/quiet-star-2024.md) (`2024.21`)
- [Quiet-STaR](/milestones/quiet-star-2024.md) (`2024.21`) → [s1 Test-Time Scaling](/milestones/s1-test-time-scaling-2025.md) (`2025.09`)
