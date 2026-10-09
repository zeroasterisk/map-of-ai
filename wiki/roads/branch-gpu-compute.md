---
type: Lineage Road
title: The PyTorch, Megatron, FlashAttention & Nvidia GPU Compute Road
description: 'Connects TensorFlow (2015) and PyTorch (2017) to the GPU distributed training & inference hardware/kernel stack:
  Nvidia Megatron-LM (2019), Microsoft ZeRO/DeepSpeed (2019), Turing-NLG (2020), Nvidia A100 (2020), LoRA (2021), Megatron-Turing
  NLG 530B (2022), Nvidia Hopper H100 (2022), Tri Dao''s FlashAttention (2022), Speculative Decoding (2023), Kwon et al.''s
  vLLM/PagedAttention (2023), Nvidia Blackwell B200 (2024), FlashAttention-3 (2024), and Nvidia Vera Rubin (2026).'
road_id: branch-gpu-compute
road_tier: branch
stop_count: 15
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
- resource: https://arxiv.org/abs/2201.11990
  title: Smith et al., Megatron-Turing NLG 530B, arXiv 2201.11990 [60]
- resource: https://en.wikipedia.org/wiki/Rubin_%28microarchitecture%29
  title: 'Wikipedia: Rubin (microarchitecture) [22]'
---

# The PyTorch, Megatron, FlashAttention & Nvidia GPU Compute Road

**Road ID**: `branch-gpu-compute` · **Hierarchy Class**: `branch` · **Stops**: `15` · [Back to Roads Index](/roads/index.md)

## Historical & Architectural Rationale

Connects TensorFlow (2015) and PyTorch (2017) to the GPU distributed training & inference hardware/kernel stack: Nvidia Megatron-LM (2019), Microsoft ZeRO/DeepSpeed (2019), Turing-NLG (2020), Nvidia A100 (2020), LoRA (2021), Megatron-Turing NLG 530B (2022), Nvidia Hopper H100 (2022), Tri Dao's FlashAttention (2022), Speculative Decoding (2023), Kwon et al.'s vLLM/PagedAttention (2023), Nvidia Blackwell B200 (2024), FlashAttention-3 (2024), and Nvidia Vera Rubin (2026).

## 3-Test Knowledge Graph Audit

- **Lawyer Test**: Dedicated GPU & CUDA systems stack; removes the false spur `flashattention3-2024 -> ai-diffusion-rule-2025`.
- **Reddit Test**: Every node is a canonical GPU training/inference systems milestone (`Megatron -> DeepSpeed -> A100 -> H100 -> FlashAttention -> vLLM -> Blackwell -> FlashAttention-3 -> Vera Rubin`).
- **Individuals Involved Test**: Tri Dao, Woosuk Kwon, Samyam Rajbhandari, and Nvidia's architecture teams are connected along the exact CUDA/GPU stack they built.

## Ordered Milestone Stops (West → East)

| # | Year | Milestone | Province | One-Line Summary |
|---|------|-----------|----------|------------------|
| 1 | `2015.86` | [TensorFlow Open-Sourced](/milestones/tensorflow-2015.md) | [The Corporate Lab Colonies](/provinces/industrial-lab-founders.md) | Google open-sources TensorFlow (Nov 2015) under Apache 2.0 for distributed deep learning |
| 2 | `2017.05` | [PyTorch Released](/milestones/pytorch-2017.md) | [The Eastern Coast Forts](/provinces/chinese-state-response.md) | Paszke, Chintala and FAIR release PyTorch (Jan 2017) with eager autograd execution |
| 3 | `2019.71` | [Megatron-LM](/milestones/megatron-lm-2019.md) | [The Megatron Yards](/provinces/systems-infrastructure-axis.md) | Nvidia (17 Sep 2019): tensor / model parallelism trains an 8.3 B-parameter GPT-2 |
| 4 | `2019.77` | [ZeRO · DeepSpeed](/milestones/zero-deepspeed-2019.md) | [The Megatron Yards](/provinces/systems-infrastructure-axis.md) | Microsoft (Oct 2019): optimizer-state sharding toward trillion-parameter training |
| 5 | `2020.12` | [Turing-NLG 17 B](/milestones/turing-nlg-2020.md) | [The Megatron Yards](/provinces/systems-infrastructure-axis.md) | Microsoft (13 Feb 2020): the largest LM yet, trained on the DeepSpeed + Megatron stack |
| 6 | `2020.37` | [Nvidia A100](/milestones/a100-2020.md) | [The Megatron Yards](/provinces/systems-infrastructure-axis.md) | Ampere / A100 (14 May 2020): TF32 + bfloat16 tensor cores; workhorse of GPT-3-era training |
| 7 | `2021.46` | [LoRA Adaptation](/milestones/lora-hu-2021.md) | [The Megatron Yards](/provinces/systems-infrastructure-axis.md) | Hu et al. (Jun 2021) introduce Low-Rank Adaptation (LoRA) for efficient LLM fine-tuning |
| 8 | `2022.08` | [Megatron-Turing NLG 530 B](/milestones/mt-nlg-2022.md) | [The Megatron Yards](/provinces/systems-infrastructure-axis.md) | Nvidia + Microsoft (Jan 2022): the two stacks jointly train a 530 B dense model |
| 9 | `2022.2` | [Hopper H100](/milestones/h100-2022.md) | [The Compute Hinterland](/provinces/compute-hardware-hinterland.md) | Nvidia announces Hopper H100 (Mar 2022): the GPU of the LLM boom |
| 10 | `2022.41` | [FlashAttention](/milestones/flashattention-2022.md) | [The Compute Hinterland](/provinces/compute-hardware-hinterland.md) | Dao et al. (May 2022): IO-aware tiled exact attention in SRAM unlocks long-context training |
| 11 | `2023.04` | [Speculative Decoding](/milestones/speculative-decoding-2023.md) | [The Compute Hinterland](/provinces/compute-hardware-hinterland.md) | Leviathan et al. & Chen et al. (Jan 2023) accelerate LLM decoding 2–3x via draft verification |
| 12 | `2023.47` | [vLLM · PagedAttention](/milestones/vllm-pagedattention-2023.md) | [The Compute Hinterland](/provinces/compute-hardware-hinterland.md) | Kwon et al. (Jun 2023): OS-style virtual memory paging for KV cache boosts LLM throughput |
| 13 | `2024.21` | [Blackwell B200](/milestones/blackwell-2024.md) | [The Compute Hinterland](/provinces/compute-hardware-hinterland.md) | Nvidia announces Blackwell B200/GB200 at GTC (18 Mar 2024); $4 T market cap 2025 |
| 14 | `2024.53` | [FlashAttention-3](/milestones/flashattention3-2024.md) | [The Compute Hinterland](/provinces/compute-hardware-hinterland.md) | Shah et al. (Jul 2024) exploit Hopper asynchronous Tensor Cores and FP8 for 75% H100 utilization |
| 15 | `2026.21` | [Nvidia Vera Rubin](/milestones/nvidia-rubin-2026.md) | [The Compute Hinterland](/provinces/compute-hardware-hinterland.md) | Nvidia unveils Vera Rubin NVL144 rack architecture with HBM4 memory at GTC (Mar 2026) |

## Directed Road Segments

- [TensorFlow Open-Sourced](/milestones/tensorflow-2015.md) (`2015.86`) → [PyTorch Released](/milestones/pytorch-2017.md) (`2017.05`)
- [PyTorch Released](/milestones/pytorch-2017.md) (`2017.05`) → [Megatron-LM](/milestones/megatron-lm-2019.md) (`2019.71`)
- [Megatron-LM](/milestones/megatron-lm-2019.md) (`2019.71`) → [ZeRO · DeepSpeed](/milestones/zero-deepspeed-2019.md) (`2019.77`)
- [ZeRO · DeepSpeed](/milestones/zero-deepspeed-2019.md) (`2019.77`) → [Turing-NLG 17 B](/milestones/turing-nlg-2020.md) (`2020.12`)
- [Turing-NLG 17 B](/milestones/turing-nlg-2020.md) (`2020.12`) → [Nvidia A100](/milestones/a100-2020.md) (`2020.37`)
- [Nvidia A100](/milestones/a100-2020.md) (`2020.37`) → [LoRA Adaptation](/milestones/lora-hu-2021.md) (`2021.46`)
- [LoRA Adaptation](/milestones/lora-hu-2021.md) (`2021.46`) → [Megatron-Turing NLG 530 B](/milestones/mt-nlg-2022.md) (`2022.08`)
- [Megatron-Turing NLG 530 B](/milestones/mt-nlg-2022.md) (`2022.08`) → [Hopper H100](/milestones/h100-2022.md) (`2022.2`)
- [Hopper H100](/milestones/h100-2022.md) (`2022.2`) → [FlashAttention](/milestones/flashattention-2022.md) (`2022.41`)
- [FlashAttention](/milestones/flashattention-2022.md) (`2022.41`) → [Speculative Decoding](/milestones/speculative-decoding-2023.md) (`2023.04`)
- [Speculative Decoding](/milestones/speculative-decoding-2023.md) (`2023.04`) → [vLLM · PagedAttention](/milestones/vllm-pagedattention-2023.md) (`2023.47`)
- [vLLM · PagedAttention](/milestones/vllm-pagedattention-2023.md) (`2023.47`) → [Blackwell B200](/milestones/blackwell-2024.md) (`2024.21`)
- [Blackwell B200](/milestones/blackwell-2024.md) (`2024.21`) → [FlashAttention-3](/milestones/flashattention3-2024.md) (`2024.53`)
- [FlashAttention-3](/milestones/flashattention3-2024.md) (`2024.53`) → [Nvidia Vera Rubin](/milestones/nvidia-rubin-2026.md) (`2026.21`)
