---
type: Lineage Road
title: The CMU Sphinx, Rabiner HMM & Statistical Speech-to-MT Spur
description: Connects Kai-Fu Lee's speaker-independent continuous HMM speech recognizer CMU Sphinx (1988) and Lawrence Rabiner's
  IEEE tutorial on Hidden Markov Models in Speech Recognition (1989) to Fred Jelinek and Peter Brown's IBM Candide statistical
  machine translation system (1990), which directly transferred noisy-channel HMM/n-gram speech modeling to text translation.
road_id: spur-hmm-speech-foundations
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
- resource: https://en.wikipedia.org/wiki/CMU_Sphinx
  title: 'Wikipedia: CMU Sphinx [74]'
- resource: https://doi.org/10.1109/5.18626
  title: Rabiner 1989 [23]
- resource: https://aclanthology.org/J90-2002/
  title: Brown et al. 1990 [26]
---

# The CMU Sphinx, Rabiner HMM & Statistical Speech-to-MT Spur

**Road ID**: `spur-hmm-speech-foundations` · **Hierarchy Class**: `spur` · **Stops**: `3` · [Back to Roads Index](/roads/index.md)

## Historical & Architectural Rationale

Connects Kai-Fu Lee's speaker-independent continuous HMM speech recognizer CMU Sphinx (1988) and Lawrence Rabiner's IEEE tutorial on Hidden Markov Models in Speech Recognition (1989) to Fred Jelinek and Peter Brown's IBM Candide statistical machine translation system (1990), which directly transferred noisy-channel HMM/n-gram speech modeling to text translation.

## 3-Test Knowledge Graph Audit

- **Lawyer Test**: Foundational CMU, AT&T Bell Labs, and IBM Yorktown Heights statistical speech/NLP publications.
- **Reddit Test**: Stays local inside `statistical-corpus-basin` (`dy < 25`) and highlights how IBM Candide (1990) emerged directly out of the 1988–1989 HMM speech recognition breakthrough.
- **Individuals Involved Test**: Kai-Fu Lee, Lawrence Rabiner, Fred Jelinek, and Peter Brown's noisy-channel speech-to-translation lineage.

## Ordered Milestone Stops (West → East)

| # | Year | Milestone | Province | One-Line Summary |
|---|------|-----------|----------|------------------|
| 1 | `1988.7` | [CMU Sphinx](/milestones/cmu-sphinx-1988.md) | [The Statistical Corpus Basin](/provinces/statistical-corpus-basin.md) | Kai-Fu Lee: first continuous speaker-independent speech recognizer |
| 2 | `1989.2` | [Rabiner HMM Tutorial](/milestones/rabiner-hmm-1989.md) | [The Statistical Corpus Basin](/provinces/statistical-corpus-basin.md) | Lawrence Rabiner publishes canonical HMM tutorial for speech |
| 3 | `1990.5` | [IBM Candide SMT](/milestones/ibm-candide-1990.md) | [The Statistical Corpus Basin](/provinces/statistical-corpus-basin.md) | Brown et al.: statistical translation replaces linguistic rules |

## Directed Road Segments

- [CMU Sphinx](/milestones/cmu-sphinx-1988.md) (`1988.7`) → [Rabiner HMM Tutorial](/milestones/rabiner-hmm-1989.md) (`1989.2`)
- [Rabiner HMM Tutorial](/milestones/rabiner-hmm-1989.md) (`1989.2`) → [IBM Candide SMT](/milestones/ibm-candide-1990.md) (`1990.5`)
