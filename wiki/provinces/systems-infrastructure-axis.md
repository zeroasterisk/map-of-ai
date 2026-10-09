---
type: Cartographic Province
title: The Megatron Yards
description: The Megatron Yards
province_id: systems-infrastructure-axis
continent_id: transformer-plateau
time_range:
- 2018
- 2022
status: active
generated:
  by: gemini-4-argon/1.0
  at: '2026-10-08T20:15:00Z'
verified:
- by: human:zeroasterisk
  at: '2026-10-08T20:15:00Z'
sources:
- resource: https://github.com/jax-ml/jax
  title: 'Bradbury et al., JAX: composable transformations of Python+NumPy programs, 2018 [57]'
- resource: https://arxiv.org/abs/1909.08053
  title: Shoeybi et al., Megatron-LM, arXiv 1909.08053 [57]
---

# The Megatron Yards

**Province ID**: `systems-infrastructure-axis` · **Continent**: `transformer-plateau` · **Active Era**: `2018–2022` · [Back to Provinces Index](/provinces/index.md)



## Lineage Roads Traversing This Province

- [The PyTorch, Megatron, FlashAttention & Nvidia GPU Compute Road](/roads/branch-gpu-compute.md) (`branch`)
- [The Wafer-Scale & SRAM Inference Silicon Spur](/roads/spur-custom-inference-silicon.md) (`spur`)
- [The Google Brain, TensorFlow, JAX & TPU Compute Turnpike](/roads/via-tensorflow-tpu.md) (`trunk`)
- [The Attention, Transformer & Google Gemini High Road](/roads/via-transformer-gemini.md) (`trunk`)

## Milestones in This Province

- `2018.9` — [Google JAX](/milestones/jax-bradbury-2018.md): Bradbury et al. release JAX: composable Autograd and XLA compilation for accelerators
- `2019.71` — [Megatron-LM](/milestones/megatron-lm-2019.md): Nvidia (17 Sep 2019): tensor / model parallelism trains an 8.3 B-parameter GPT-2
- `2019.77` — [ZeRO · DeepSpeed](/milestones/zero-deepspeed-2019.md): Microsoft (Oct 2019): optimizer-state sharding toward trillion-parameter training
- `2020.12` — [Turing-NLG 17 B](/milestones/turing-nlg-2020.md): Microsoft (13 Feb 2020): the largest LM yet, trained on the DeepSpeed + Megatron stack
- `2020.37` — [Nvidia A100](/milestones/a100-2020.md): Ampere / A100 (14 May 2020): TF32 + bfloat16 tensor cores; workhorse of GPT-3-era training
- `2021.46` — [LoRA Adaptation](/milestones/lora-hu-2021.md): Hu et al. (Jun 2021) introduce Low-Rank Adaptation (LoRA) for efficient LLM fine-tuning
- `2022.08` — [Megatron-Turing NLG 530 B](/milestones/mt-nlg-2022.md): Nvidia + Microsoft (Jan 2022): the two stacks jointly train a 530 B dense model
- `2022.26` — [PaLM · Pathways](/milestones/palm-2022.md): Chowdhery et al. (5 Apr 2022): 540 B parameters on TPU v4 pods
- `2022.5` — [Minerva](/milestones/minerva-2022.md): Google (Jun 2022): PaLM fine-tuned on maths and science text for quantitative reasoning
