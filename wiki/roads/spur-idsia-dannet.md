---
type: Lineage Road
title: The IDSIA Max-Pooling GPU ConvNet (DanNet) Spur
description: Connects Schmidhuber's IDSIA lab from LSTM (1997) and early GPU deep nets (2009) to Cireșan, Meier, Masci, Gambardella
  & Schmidhuber's DanNet GPU max-pooling CNN (2011, first superhuman visual pattern recognition at IJCAI 2011) and AlexNet
  (2012).
road_id: spur-idsia-dannet
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
- resource: https://doi.org/10.1162/neco.1997.9.8.1735
  title: Hochreiter & Schmidhuber 1997 [23]
- resource: https://people.idsia.ch/~juergen/ijcnn2011.pdf
  title: Cireşan et al., IJCNN 2011 [12]
- resource: https://arxiv.org/abs/1202.2745
  title: Cireşan, Meier & Schmidhuber, CVPR 2012 [13]
- resource: https://proceedings.neurips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html
  title: Krizhevsky, Sutskever & Hinton, NIPS 2012 [17]
- resource: https://en.wikipedia.org/wiki/AlexNet
  title: 'Wikipedia: AlexNet [18]'
---

# The IDSIA Max-Pooling GPU ConvNet (DanNet) Spur

**Road ID**: `spur-idsia-dannet` · **Hierarchy Class**: `spur` · **Stops**: `4` · [Back to Roads Index](/roads/index.md)

## Historical & Architectural Rationale

Connects Schmidhuber's IDSIA lab from LSTM (1997) and early GPU deep nets (2009) to Cireșan, Meier, Masci, Gambardella & Schmidhuber's DanNet GPU max-pooling CNN (2011, first superhuman visual pattern recognition at IJCAI 2011) and AlexNet (2012).

## 3-Test Knowledge Graph Audit

- **Lawyer Test**: Published academic computer vision benchmarks.
- **Reddit Test**: Explicitly credits IDSIA's 2011 GPU CNN (`dannet-2011`) alongside `alexnet-2012` — one of the most frequently discussed historical lineages on `r/MachineLearning`.
- **Individuals Involved Test**: Dan Cireșan and Jürgen Schmidhuber's 2011 GPU CNN milestone is properly connected upstream of 2012 ImageNet.

## Ordered Milestone Stops (West → East)

| # | Year | Milestone | Province | One-Line Summary |
|---|------|-----------|----------|------------------|
| 1 | `1997.85` | [LSTM](/milestones/lstm-1997.md) | [The Early ConvNet Ridge](/provinces/early-convnet-ridge.md) | Hochreiter & Schmidhuber introduce Long Short-Term Memory nets |
| 2 | `2009.9` | [GPU deep nets](/milestones/gpu-dbn-2009.md) | [The ImageNet Escarpment](/provinces/gpu-convnet-school.md) | Raina, Madhavan & Ng: GPUs train a 100 M-parameter DBN up to 70× faster |
| 3 | `2011.5` | [IDSIA DanNet](/milestones/dannet-2011.md) | [The ImageNet Escarpment](/provinces/gpu-convnet-school.md) | Cireşan et al.: first superhuman result in a visual contest (IJCNN traffic signs) |
| 4 | `2012.75` | [AlexNet](/milestones/alexnet-2012.md) | [The ImageNet Escarpment](/provinces/gpu-convnet-school.md) | Krizhevsky, Sutskever & Hinton win ILSVRC 2012: 15.3 % top-5 error vs 26.2 % |

## Directed Road Segments

- [LSTM](/milestones/lstm-1997.md) (`1997.85`) → [GPU deep nets](/milestones/gpu-dbn-2009.md) (`2009.9`)
- [GPU deep nets](/milestones/gpu-dbn-2009.md) (`2009.9`) → [IDSIA DanNet](/milestones/dannet-2011.md) (`2011.5`)
- [IDSIA DanNet](/milestones/dannet-2011.md) (`2011.5`) → [AlexNet](/milestones/alexnet-2012.md) (`2012.75`)
