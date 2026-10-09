---
type: Lineage Road
title: The TensorFlow & TPU–Transformer Road
description: Vaswani et al. implemented and trained the original 2017 Transformer in TensorFlow (`tensor2tensor`) on Google
  infrastructure following the deployment of TPU v1.
road_id: branch-tf-transformer
road_tier: branch
stop_count: 3
status: active
generated:
  by: gemini-4-argon/1.0
  at: '2026-10-08T20:15:00Z'
verified:
- by: human:zeroasterisk
  at: '2026-10-08T20:15:00Z'
sources:
- resource: https://arxiv.org/abs/1603.04467
  title: Abadi et al., TensorFlow, arXiv 1603.04467 [44]
- resource: https://arxiv.org/abs/1704.04760
  title: Jouppi et al., In-Datacenter Performance Analysis of a TPU, ISCA 2017 [49]
- resource: https://arxiv.org/abs/1706.03762
  title: Vaswani et al., Attention Is All You Need, arXiv 1706.03762 [1]
- resource: https://en.wikipedia.org/wiki/Attention_Is_All_You_Need
  title: 'Wikipedia: Attention Is All You Need [2]'
- resource: https://en.wikipedia.org/wiki/Transformer_%28deep_learning_architecture%29
  title: 'Wikipedia: Transformer [3]'
---

# The TensorFlow & TPU–Transformer Road

**Road ID**: `branch-tf-transformer` · **Hierarchy Class**: `branch` · **Stops**: `3` · [Back to Roads Index](/roads/index.md)

## Historical & Architectural Rationale

Vaswani et al. implemented and trained the original 2017 Transformer in TensorFlow (`tensor2tensor`) on Google infrastructure following the deployment of TPU v1.

## 3-Test Knowledge Graph Audit

- **Lawyer Test**: 100% internal Google Brain systems-to-architecture connection.
- **Reddit Test**: Historically exact: `tensor2tensor` in TensorFlow was the reference implementation released alongside 'Attention Is All You Need'.
- **Individuals Involved Test**: Matches Lukasz Kaiser, Ashish Vaswani, and Jeff Dean's published Google Brain workflow.

## Ordered Milestone Stops (West → East)

| # | Year | Milestone | Province | One-Line Summary |
|---|------|-----------|----------|------------------|
| 1 | `2015.86` | [TensorFlow Open-Sourced](/milestones/tensorflow-2015.md) | [The Corporate Lab Colonies](/provinces/industrial-lab-founders.md) | Google open-sources TensorFlow (Nov 2015) under Apache 2.0 for distributed deep learning |
| 2 | `2016.38` | [Google TPU v1 Unveiled](/milestones/google-tpu-v1-2016.md) | [The Eastern Coast Forts](/provinces/chinese-state-response.md) | Google unveils its custom ASIC Tensor Processing Unit at I/O (May 2016) |
| 3 | `2017.45` | [Attention Is All You Need](/milestones/attention-is-all-you-need-2017.md) | [The Mixture-of-Experts Delta](/provinces/sparse-moe-engineers.md) | Vaswani et al. (12 Jun 2017): self-attention replaces recurrence — the Transformer; eight Google authors |

## Directed Road Segments

- [TensorFlow Open-Sourced](/milestones/tensorflow-2015.md) (`2015.86`) → [Google TPU v1 Unveiled](/milestones/google-tpu-v1-2016.md) (`2016.38`)
- [Google TPU v1 Unveiled](/milestones/google-tpu-v1-2016.md) (`2016.38`) → [Attention Is All You Need](/milestones/attention-is-all-you-need-2017.md) (`2017.45`)
