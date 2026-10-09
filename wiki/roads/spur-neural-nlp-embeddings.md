---
type: Lineage Road
title: The Neural NLP, Bahdanau Attention & Subword BPE Spur
description: Traces the neural NLP and representation learning wave from Collobert & Weston's unified neural NLP architecture
  (2008) and Natural Language Processing (Almost) from Scratch (2011) through Mikolov's word2vec (2013), Cho et al.'s GRU
  (Jun 2014), Bahdanau-Cho-Bengio's additive neural attention for NMT (Sep 2014), Pennington-Socher-Manning's GloVe (Oct 2014),
  Vinyals et al.'s Show and Tell neural image captioning (Nov 2014), Kingma & Ba's Adam optimizer (Dec 2014), and Sennrich
  et al.'s Byte-Pair Encoding subword tokenization (Aug 2015) to Google's Neural Machine Translation system (GNMT, Sep 2016).
road_id: spur-neural-nlp-embeddings
road_tier: spur
stop_count: 10
status: active
generated:
  by: gemini-4-argon/1.0
  at: '2026-10-08T20:15:00Z'
verified:
- by: human:zeroasterisk
  at: '2026-10-08T20:15:00Z'
sources:
- resource: https://dl.acm.org/doi/10.1145/1390156.1390177
  title: Collobert & Weston 2008 [87]
- resource: https://aclanthology.org/D14-1162/
  title: Pennington, Socher & Manning, GloVe, EMNLP 2014 [88]
- resource: https://arxiv.org/abs/1609.08144
  title: Wu et al., GNMT, arXiv 1609.08144 [51]
---

# The Neural NLP, Bahdanau Attention & Subword BPE Spur

**Road ID**: `spur-neural-nlp-embeddings` · **Hierarchy Class**: `spur` · **Stops**: `10` · [Back to Roads Index](/roads/index.md)

## Historical & Architectural Rationale

Traces the neural NLP and representation learning wave from Collobert & Weston's unified neural NLP architecture (2008) and Natural Language Processing (Almost) from Scratch (2011) through Mikolov's word2vec (2013), Cho et al.'s GRU (Jun 2014), Bahdanau-Cho-Bengio's additive neural attention for NMT (Sep 2014), Pennington-Socher-Manning's GloVe (Oct 2014), Vinyals et al.'s Show and Tell neural image captioning (Nov 2014), Kingma & Ba's Adam optimizer (Dec 2014), and Sennrich et al.'s Byte-Pair Encoding subword tokenization (Aug 2015) to Google's Neural Machine Translation system (GNMT, Sep 2016).

## 3-Test Knowledge Graph Audit

- **Lawyer Test**: Published ICML/ICLR/EMNLP/ACL deep learning and neural MT papers.
- **Reddit Test**: Connects the essential building blocks of modern neural NLP (`Collobert & Weston -> word2vec -> GRU -> Bahdanau Attention -> GloVe -> Adam -> BPE -> GNMT`) in strict chronological order.
- **Individuals Involved Test**: Ronan Collobert, Jason Weston, Tomas Mikolov, Kyunghyun Cho, Dzmitry Bahdanau, Yoshua Bengio, Jeffrey Pennington, Diederik Kingma, Jimmy Ba, and Rico Sennrich are linked accurately.

## Ordered Milestone Stops (West → East)

| # | Year | Milestone | Province | One-Line Summary |
|---|------|-----------|----------|------------------|
| 1 | `2008.5` | [Unified NLP](/milestones/nlp-unified-2008.md) | [The Pre-training Foothills](/provinces/pretraining-foothills.md) | Collobert & Weston: unified neural architecture for NLP |
| 2 | `2011.5` | [NLP from scratch](/milestones/nlp-from-scratch-2011.md) | [The Attention Headwaters](/provinces/neural-nlp-sequence-school.md) | Collobert & Weston: one convnet for tagging, chunking, NER and SRL |
| 3 | `2013.05` | [word2vec](/milestones/word2vec-2013.md) | [The Attention Headwaters](/provinces/neural-nlp-sequence-school.md) | Mikolov, Chen, Corrado & Dean: cheap word embeddings (arXiv 1301.3781) |
| 4 | `2014.42` | [GRU enc–dec](/milestones/gru-2014.md) | [The Attention Headwaters](/provinces/neural-nlp-sequence-school.md) | Cho et al.: RNN encoder–decoder with the gated recurrent unit |
| 5 | `2014.67` | [attention](/milestones/attention-2014.md) | [The Attention Headwaters](/provinces/neural-nlp-sequence-school.md) | Bahdanau, Cho & Bengio: attention over the source — the Attention River rises |
| 6 | `2014.8` | [GloVe](/milestones/glove-2014.md) | [The Attention Headwaters](/provinces/neural-nlp-sequence-school.md) | Pennington, Socher & Manning (Stanford): the rival embedding |
| 7 | `2014.88` | [Show and Tell](/milestones/show-and-tell-2014.md) | [The Attention Headwaters](/provinces/neural-nlp-sequence-school.md) | Vinyals et al.: CNN encoder + LSTM decoder captions images |
| 8 | `2014.96` | [Adam Optimizer](/milestones/adam-optimizer-2014.md) | [The Attention Headwaters](/provinces/neural-nlp-sequence-school.md) | Kingma and Ba introduce Adam adaptive moment estimation for stochastic optimization |
| 9 | `2015.66` | [Subword BPE](/milestones/bpe-sennrich-2015.md) | [The Attention Headwaters](/provinces/neural-nlp-sequence-school.md) | Sennrich, Haddow and Birch adapt Byte Pair Encoding for open-vocabulary neural MT |
| 10 | `2016.74` | [GNMT](/milestones/gnmt-2016.md) | [The Attention Headwaters](/provinces/neural-nlp-sequence-school.md) | Google's LSTM + attention translation in production (Nov 2016) |

## Directed Road Segments

- [Unified NLP](/milestones/nlp-unified-2008.md) (`2008.5`) → [NLP from scratch](/milestones/nlp-from-scratch-2011.md) (`2011.5`)
- [NLP from scratch](/milestones/nlp-from-scratch-2011.md) (`2011.5`) → [word2vec](/milestones/word2vec-2013.md) (`2013.05`)
- [word2vec](/milestones/word2vec-2013.md) (`2013.05`) → [GRU enc–dec](/milestones/gru-2014.md) (`2014.42`)
- [GRU enc–dec](/milestones/gru-2014.md) (`2014.42`) → [attention](/milestones/attention-2014.md) (`2014.67`)
- [attention](/milestones/attention-2014.md) (`2014.67`) → [GloVe](/milestones/glove-2014.md) (`2014.8`)
- [GloVe](/milestones/glove-2014.md) (`2014.8`) → [Show and Tell](/milestones/show-and-tell-2014.md) (`2014.88`)
- [Show and Tell](/milestones/show-and-tell-2014.md) (`2014.88`) → [Adam Optimizer](/milestones/adam-optimizer-2014.md) (`2014.96`)
- [Adam Optimizer](/milestones/adam-optimizer-2014.md) (`2014.96`) → [Subword BPE](/milestones/bpe-sennrich-2015.md) (`2015.66`)
- [Subword BPE](/milestones/bpe-sennrich-2015.md) (`2015.66`) → [GNMT](/milestones/gnmt-2016.md) (`2016.74`)
