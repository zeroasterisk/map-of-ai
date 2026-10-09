---
type: Lineage Road
title: The Transfer Learning, GLUE & Encoder Pre-Training Spur
description: 'Traces the 2018–2020 NLP transfer-learning and bidirectional encoder wave in strict chronological order: Howard
  & Ruder''s ULMFiT (Jan 2018), Peters et al.''s ELMo (Feb 2018), the GLUE benchmark (Apr 2018), Devlin et al.''s BERT (Oct
  2018), Dai et al.''s Transformer-XL (Jan 2019), SuperGLUE (May 2019), Yang et al.''s XLNet (Jun 2019), Liu et al.''s RoBERTa
  (Jul 2019), Sanh et al.''s DistilBERT (Oct 2019), and He et al.''s DeBERTa (Jun 2020).'
road_id: spur-encoder-glue-benchmarks
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
- resource: https://arxiv.org/abs/1801.06146
  title: Howard & Ruder, ULMFiT, arXiv 1801.06146 [46]
- resource: https://arxiv.org/abs/1905.00537
  title: Wang et al., SuperGLUE, arXiv 1905.00537 [48]
- resource: https://arxiv.org/abs/2006.03654
  title: He et al., DeBERTa, arXiv 2006.03654 [54]
---

# The Transfer Learning, GLUE & Encoder Pre-Training Spur

**Road ID**: `spur-encoder-glue-benchmarks` · **Hierarchy Class**: `spur` · **Stops**: `10` · [Back to Roads Index](/roads/index.md)

## Historical & Architectural Rationale

Traces the 2018–2020 NLP transfer-learning and bidirectional encoder wave in strict chronological order: Howard & Ruder's ULMFiT (Jan 2018), Peters et al.'s ELMo (Feb 2018), the GLUE benchmark (Apr 2018), Devlin et al.'s BERT (Oct 2018), Dai et al.'s Transformer-XL (Jan 2019), SuperGLUE (May 2019), Yang et al.'s XLNet (Jun 2019), Liu et al.'s RoBERTa (Jul 2019), Sanh et al.'s DistilBERT (Oct 2019), and He et al.'s DeBERTa (Jun 2020).

## 3-Test Knowledge Graph Audit

- **Lawyer Test**: Published ACL/NAACL/ICLR/NeurIPS NLP papers and public GLUE/SuperGLUE leaderboards.
- **Reddit Test**: Captures the exact 2018–2020 GLUE/SuperGLUE leaderboard race (`ULMFiT -> ELMo -> GLUE -> BERT -> Transformer-XL -> SuperGLUE -> XLNet -> RoBERTa -> DistilBERT -> DeBERTa`).
- **Individuals Involved Test**: Jeremy Howard, Sebastian Ruder, Matthew Peters, Alex Wang, Samuel Bowman, Jacob Devlin, Zhilin Yang, Yinhan Liu, Victor Sanh, and Pengcheng He are linked in exact publication order.

## Ordered Milestone Stops (West → East)

| # | Year | Milestone | Province | One-Line Summary |
|---|------|-----------|----------|------------------|
| 1 | `2018.05` | [ULMFiT](/milestones/ulmfit-2018.md) | [The BERT Escarpment](/provinces/encoder-understanding-school.md) | Howard & Ruder: LM pre-training + fine-tuning transfers to text classification (18 Jan) |
| 2 | `2018.12` | [ELMo](/milestones/elmo-2018.md) | [The BERT Escarpment](/provinces/encoder-understanding-school.md) | Peters et al.: contextual embeddings from a bidirectional LSTM — the last pre-Transformer win |
| 3 | `2018.3` | [GLUE](/milestones/glue-2018.md) | [The BERT Escarpment](/provinces/encoder-understanding-school.md) | Wang, Bowman et al. (NYU/UW/DeepMind): the leaderboard BERT, XLNet, RoBERTa, T5 race up |
| 4 | `2018.78` | [BERT](/milestones/bert-2018.md) | [The BERT Escarpment](/provinces/encoder-understanding-school.md) | Devlin et al. (11 Oct 2018): encoder-only bidirectional pre-training tops GLUE, SQuAD, SWAG |
| 5 | `2019.02` | [Transformer-XL](/milestones/transformer-xl-2019.md) | [The BERT Escarpment](/provinces/encoder-understanding-school.md) | CMU/Google (9 Jan 2019): recurrence over segments for longer context |
| 6 | `2019.34` | [SuperGLUE](/milestones/superglue-2019.md) | [The BERT Escarpment](/provinces/encoder-understanding-school.md) | a stickier benchmark (2 May 2019) after models pass GLUE's human baseline |
| 7 | `2019.47` | [XLNet](/milestones/xlnet-2019.md) | [The BERT Escarpment](/provinces/encoder-understanding-school.md) | generalised autoregressive pre-training (19 Jun 2019) beats BERT on 20 tasks |
| 8 | `2019.57` | [RoBERTa](/milestones/roberta-2019.md) | [The BERT Escarpment](/provinces/encoder-understanding-school.md) | Facebook AI (26 Jul 2019): BERT trained longer on more data retakes GLUE |
| 9 | `2019.75` | [DistilBERT](/milestones/distilbert-2019.md) | [The BERT Escarpment](/provinces/encoder-understanding-school.md) | Hugging Face (2 Oct 2019): distillation for deployment — 40 % smaller, 60 % faster |
| 10 | `2020.45` | [DeBERTa](/milestones/deberta-2020.md) | [The BERT Escarpment](/provinces/encoder-understanding-school.md) | He et al. (Microsoft, Jun 2020): disentangled attention surpasses human baseline on SuperGLUE |

## Directed Road Segments

- [ULMFiT](/milestones/ulmfit-2018.md) (`2018.05`) → [ELMo](/milestones/elmo-2018.md) (`2018.12`)
- [ELMo](/milestones/elmo-2018.md) (`2018.12`) → [GLUE](/milestones/glue-2018.md) (`2018.3`)
- [GLUE](/milestones/glue-2018.md) (`2018.3`) → [BERT](/milestones/bert-2018.md) (`2018.78`)
- [BERT](/milestones/bert-2018.md) (`2018.78`) → [Transformer-XL](/milestones/transformer-xl-2019.md) (`2019.02`)
- [Transformer-XL](/milestones/transformer-xl-2019.md) (`2019.02`) → [SuperGLUE](/milestones/superglue-2019.md) (`2019.34`)
- [SuperGLUE](/milestones/superglue-2019.md) (`2019.34`) → [XLNet](/milestones/xlnet-2019.md) (`2019.47`)
- [XLNet](/milestones/xlnet-2019.md) (`2019.47`) → [RoBERTa](/milestones/roberta-2019.md) (`2019.57`)
- [RoBERTa](/milestones/roberta-2019.md) (`2019.57`) → [DistilBERT](/milestones/distilbert-2019.md) (`2019.75`)
- [DistilBERT](/milestones/distilbert-2019.md) (`2019.75`) → [DeBERTa](/milestones/deberta-2020.md) (`2020.45`)
