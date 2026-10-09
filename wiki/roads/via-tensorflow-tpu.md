---
type: Lineage Road
title: The Google Brain, TensorFlow, JAX & TPU Compute Turnpike
description: Pure Google systems & custom silicon lineage from Google Brain founding (2011), the 'cat' unsupervised network
  (2012), and DistBelief (2012) through TensorFlow open-sourced (2015), Google TPU v1 (2016), Google JAX (2018), PaLM on Pathways
  TPU v4 pods (2022), TPU v5p & Trillium (2024), to 7th-gen TPU Ironwood (2025).
road_id: via-tensorflow-tpu
road_tier: trunk
stop_count: 9
status: active
generated:
  by: gemini-4-argon/1.0
  at: '2026-10-08T20:15:00Z'
verified:
- by: human:zeroasterisk
  at: '2026-10-08T20:15:00Z'
sources:
- resource: https://en.wikipedia.org/wiki/Google_Brain
  title: 'Wikipedia: Google Brain [14]'
- resource: https://arxiv.org/abs/1704.04760
  title: Jouppi et al., In-Datacenter Performance Analysis of a TPU, ISCA 2017 [49]
- resource: https://en.wikipedia.org/wiki/Tensor_Processing_Unit
  title: 'Wikipedia: Tensor Processing Unit (Ironwood) [45]'
---

# The Google Brain, TensorFlow, JAX & TPU Compute Turnpike

**Road ID**: `via-tensorflow-tpu` · **Hierarchy Class**: `trunk` · **Stops**: `9` · [Back to Roads Index](/roads/index.md)

## Historical & Architectural Rationale

Pure Google systems & custom silicon lineage from Google Brain founding (2011), the 'cat' unsupervised network (2012), and DistBelief (2012) through TensorFlow open-sourced (2015), Google TPU v1 (2016), Google JAX (2018), PaLM on Pathways TPU v4 pods (2022), TPU v5p & Trillium (2024), to 7th-gen TPU Ironwood (2025).

## 3-Test Knowledge Graph Audit

- **Lawyer Test**: Separates Google's proprietary TPU silicon and TensorFlow/JAX compiler stack from Nvidia GPUs (`Blackwell`, `Vera Rubin`) and OpenAI's `Stargate`.
- **Reddit Test**: Eliminates the old zig-zag between Google TPUs and Nvidia GPUs; Nvidia GPUs and CUDA/FlashAttention kernels now travel on their own dedicated `branch-gpu-compute` road.
- **Individuals Involved Test**: Jeff Dean, Norm Jouppi, and the Google Brain / JAX / TPU teams have a clean, uninterrupted systems lineage.

## Ordered Milestone Stops (West → East)

| # | Year | Milestone | Province | One-Line Summary |
|---|------|-----------|----------|------------------|
| 1 | `2011.5` | [Google Brain](/milestones/google-brain-2011.md) | [The Corporate Lab Colonies](/provinces/industrial-lab-founders.md) | Dean, Corrado & Ng start the project at Google X |
| 2 | `2012.45` | [the “cat” network](/milestones/cat-2012.md) | [The Corporate Lab Colonies](/provinces/industrial-lab-founders.md) | Le et al.: 10 M YouTube frames on 16,000 cores, unsupervised |
| 3 | `2012.9` | [DistBelief](/milestones/distbelief-2012.md) | [The Corporate Lab Colonies](/provinces/industrial-lab-founders.md) | Dean et al.: distributed training system, TensorFlow's predecessor |
| 4 | `2015.86` | [TensorFlow Open-Sourced](/milestones/tensorflow-2015.md) | [The Corporate Lab Colonies](/provinces/industrial-lab-founders.md) | Google open-sources TensorFlow (Nov 2015) under Apache 2.0 for distributed deep learning |
| 5 | `2016.38` | [Google TPU v1 Unveiled](/milestones/google-tpu-v1-2016.md) | [The Eastern Coast Forts](/provinces/chinese-state-response.md) | Google unveils its custom ASIC Tensor Processing Unit at I/O (May 2016) |
| 6 | `2018.9` | [Google JAX](/milestones/jax-bradbury-2018.md) | [The Megatron Yards](/provinces/systems-infrastructure-axis.md) | Bradbury et al. release JAX: composable Autograd and XLA compilation for accelerators |
| 7 | `2022.26` | [PaLM · Pathways](/milestones/palm-2022.md) | [The Megatron Yards](/provinces/systems-infrastructure-axis.md) | Chowdhery et al. (5 Apr 2022): 540 B parameters on TPU v4 pods |
| 8 | `2024.37` | [TPU v5p & Trillium](/milestones/tpu-trillium-2024.md) | [The Compute Hinterland](/provinces/compute-hardware-hinterland.md) | Google Cloud announces 6th-gen Trillium TPU at I/O (14 May 2024) with 4.7× peak compute |
| 9 | `2025.27` | [TPU Ironwood](/milestones/tpu-ironwood-2025.md) | [The Compute Hinterland](/provinces/compute-hardware-hinterland.md) | Google unveils 7th-gen Ironwood TPU (9 Apr 2025): 4,614 TFLOPs per chip for inference |

## Directed Road Segments

- [Google Brain](/milestones/google-brain-2011.md) (`2011.5`) → [the “cat” network](/milestones/cat-2012.md) (`2012.45`)
- [the “cat” network](/milestones/cat-2012.md) (`2012.45`) → [DistBelief](/milestones/distbelief-2012.md) (`2012.9`)
- [DistBelief](/milestones/distbelief-2012.md) (`2012.9`) → [TensorFlow Open-Sourced](/milestones/tensorflow-2015.md) (`2015.86`)
- [TensorFlow Open-Sourced](/milestones/tensorflow-2015.md) (`2015.86`) → [Google TPU v1 Unveiled](/milestones/google-tpu-v1-2016.md) (`2016.38`)
- [Google TPU v1 Unveiled](/milestones/google-tpu-v1-2016.md) (`2016.38`) → [Google JAX](/milestones/jax-bradbury-2018.md) (`2018.9`)
- [Google JAX](/milestones/jax-bradbury-2018.md) (`2018.9`) → [PaLM · Pathways](/milestones/palm-2022.md) (`2022.26`)
- [PaLM · Pathways](/milestones/palm-2022.md) (`2022.26`) → [TPU v5p & Trillium](/milestones/tpu-trillium-2024.md) (`2024.37`)
- [TPU v5p & Trillium](/milestones/tpu-trillium-2024.md) (`2024.37`) → [TPU Ironwood](/milestones/tpu-ironwood-2025.md) (`2025.27`)
