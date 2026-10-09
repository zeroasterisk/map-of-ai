---
type: Lineage Road
title: The Wafer-Scale & SRAM Inference Silicon Spur
description: Traces specialized non-GPU AI accelerator architectures from the 7nm datacenter era (`a100-2020`) to Groq's deterministic
  SRAM Language Processing Unit (`groq-2024`) and Cerebras's 4-trillion-transistor Wafer-Scale Engine 3 (`cerebras-wse3-2024`).
road_id: spur-custom-inference-silicon
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
- resource: https://developer.nvidia.com/blog/nvidia-ampere-architecture-in-depth/
  title: NVIDIA Technical Blog, Ampere In-Depth, 14 May 2020 [62]
- resource: https://en.wikipedia.org/wiki/Ampere_%28microarchitecture%29
  title: 'Wikipedia: Ampere (microarchitecture) [61]'
- resource: https://en.wikipedia.org/wiki/Groq
  title: 'Wikipedia: Groq [103]'
- resource: https://en.wikipedia.org/wiki/Cerebras
  title: 'Wikipedia: Cerebras Wafer Scale Engine 3 [103]'
---

# The Wafer-Scale & SRAM Inference Silicon Spur

**Road ID**: `spur-custom-inference-silicon` · **Hierarchy Class**: `spur` · **Stops**: `3` · [Back to Roads Index](/roads/index.md)

## Historical & Architectural Rationale

Traces specialized non-GPU AI accelerator architectures from the 7nm datacenter era (`a100-2020`) to Groq's deterministic SRAM Language Processing Unit (`groq-2024`) and Cerebras's 4-trillion-transistor Wafer-Scale Engine 3 (`cerebras-wse3-2024`).

## 3-Test Knowledge Graph Audit

- **Lawyer Test**: Stays within `compute-hardware-hinterland` and groups custom inference/wafer-scale silicon without implying corporate affiliation.
- **Reddit Test**: Groq LPU and Cerebras WSE-3 are the two flagship high-tok/s SRAM/wafer-scale inference alternatives in the 2024 hardware landscape.
- **Individuals Involved Test**: Jonathan Ross (Groq, previously TPU v1 architect) and Andrew Feldman (Cerebras) are situated cleanly in the hardware hinterland.

## Ordered Milestone Stops (West → East)

| # | Year | Milestone | Province | One-Line Summary |
|---|------|-----------|----------|------------------|
| 1 | `2020.37` | [Nvidia A100](/milestones/a100-2020.md) | [The Megatron Yards](/provinces/systems-infrastructure-axis.md) | Ampere / A100 (14 May 2020): TF32 + bfloat16 tensor cores; workhorse of GPT-3-era training |
| 2 | `2024.13` | [Groq LPU](/milestones/groq-2024.md) | [The Compute Hinterland](/provinces/compute-hardware-hinterland.md) | Groq's SRAM-based LPU inference chips; GroqCloud opens 19 Feb 2024 |
| 3 | `2024.19` | [Cerebras WSE-3](/milestones/cerebras-wse3-2024.md) | [The Compute Hinterland](/provinces/compute-hardware-hinterland.md) | Cerebras unveils 4-trillion-transistor Wafer Scale Engine 3 (13 Mar 2024) at 900,000 cores |

## Directed Road Segments

- [Nvidia A100](/milestones/a100-2020.md) (`2020.37`) → [Groq LPU](/milestones/groq-2024.md) (`2024.13`)
- [Groq LPU](/milestones/groq-2024.md) (`2024.13`) → [Cerebras WSE-3](/milestones/cerebras-wse3-2024.md) (`2024.19`)
