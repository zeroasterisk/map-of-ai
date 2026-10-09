---
type: Lineage Road
title: The Model Cards & FAccT Critique Spur
description: Traces the Ethical AI and FAccT research lineage of Margaret Mitchell, Timnit Gebru, and Emily Bender from Model
  Cards for Model Reporting (Oct 2018) through the December 2020 Google Ethical AI controversy (`gebru-exit-2020`) to the
  resulting FAccT paper 'On the Dangers of Stochastic Parrots' (Mar 2021).
road_id: spur-ethical-ai-facct
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
- resource: https://arxiv.org/abs/1810.03993
  title: Mitchell et al., Model Cards, arXiv 1810.03993 [68]
- resource: https://en.wikipedia.org/wiki/Timnit_Gebru
  title: 'Wikipedia: Timnit Gebru [67]'
- resource: https://en.wikipedia.org/wiki/Stochastic_parrot
  title: 'Wikipedia: Stochastic parrot [38]'
---

# The Model Cards & FAccT Critique Spur

**Road ID**: `spur-ethical-ai-facct` · **Hierarchy Class**: `spur` · **Stops**: `3` · [Back to Roads Index](/roads/index.md)

## Historical & Architectural Rationale

Traces the Ethical AI and FAccT research lineage of Margaret Mitchell, Timnit Gebru, and Emily Bender from Model Cards for Model Reporting (Oct 2018) through the December 2020 Google Ethical AI controversy (`gebru-exit-2020`) to the resulting FAccT paper 'On the Dangers of Stochastic Parrots' (Mar 2021).

## 3-Test Knowledge Graph Audit

- **Lawyer Test**: Eliminates the false nearest-neighbor spur `gebru-exit-2020 -> anthropic-2021` (which falsely linked Timnit Gebru's departure from Google to the founding of Anthropic by former OpenAI researchers).
- **Reddit Test**: Connects `model-cards-2018 -> gebru-exit-2020 -> stochastic-parrots-2021`, which are literally the same co-authors and the exact paper at the center of the December 2020 dispute.
- **Individuals Involved Test**: Timnit Gebru, Margaret Mitchell, Emily Bender, and Angelina McMillan-Major's work is connected solely to their own co-authored scholarship.

## Ordered Milestone Stops (West → East)

| # | Year | Milestone | Province | One-Line Summary |
|---|------|-----------|----------|------------------|
| 1 | `2018.76` | [Model Cards](/milestones/model-cards-2018.md) | [The Human-Feedback Tributaries](/provinces/alignment-critique-tributaries.md) | Mitchell, Gebru et al. (Oct 2018): standardised model reporting for released models |
| 2 | `2020.93` | [Gebru forced out](/milestones/gebru-exit-2020.md) | [The Human-Feedback Tributaries](/provinces/alignment-critique-tributaries.md) | Google forces out its Ethical AI co-lead (Dec 2020) over the Stochastic Parrots paper |
| 3 | `2021.18` | [Stochastic Parrots](/milestones/stochastic-parrots-2021.md) | [The Human-Feedback Tributaries](/provinces/alignment-critique-tributaries.md) | Bender, Gebru, McMillan-Major & Mitchell (FAccT, Mar 2021): the era's defining critique of scale |

## Directed Road Segments

- [Model Cards](/milestones/model-cards-2018.md) (`2018.76`) → [Gebru forced out](/milestones/gebru-exit-2020.md) (`2020.93`)
- [Gebru forced out](/milestones/gebru-exit-2020.md) (`2020.93`) → [Stochastic Parrots](/milestones/stochastic-parrots-2021.md) (`2021.18`)
