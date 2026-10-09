---
type: Lineage Road
title: The NeRF, DreamFusion & 3D Gaussian Splatting Spur
description: Traces neural 3D scene representation and reconstruction from Mildenhall et al.'s NeRF (Mar 2020) through Poole
  et al.'s DreamFusion text-to-3D NeRF via score distillation (Sep 2022) to Kerbl et al.'s real-time 3D Gaussian Splatting
  (Aug 2023).
road_id: spur-3d-radiance
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
- resource: https://arxiv.org/abs/2003.08934
  title: Mildenhall et al., NeRF, arXiv 2003.08934 [81]
- resource: https://arxiv.org/abs/2209.14988
  title: Poole et al., DreamFusion, arXiv 2209.14988 [25]
- resource: https://arxiv.org/abs/2308.04079
  title: Kerbl et al., 3D Gaussian Splatting, SIGGRAPH 2023 [35]
---

# The NeRF, DreamFusion & 3D Gaussian Splatting Spur

**Road ID**: `spur-3d-radiance` · **Hierarchy Class**: `spur` · **Stops**: `3` · [Back to Roads Index](/roads/index.md)

## Historical & Architectural Rationale

Traces neural 3D scene representation and reconstruction from Mildenhall et al.'s NeRF (Mar 2020) through Poole et al.'s DreamFusion text-to-3D NeRF via score distillation (Sep 2022) to Kerbl et al.'s real-time 3D Gaussian Splatting (Aug 2023).

## 3-Test Knowledge Graph Audit

- **Lawyer Test**: Published SIGGRAPH/ECCV/ICLR 3D computer graphics & vision papers.
- **Reddit Test**: The exact 3D neural rendering progression (`NeRF -> DreamFusion -> 3D Gaussian Splatting`).
- **Individuals Involved Test**: Ben Mildenhall, Ben Poole, and Bernhard Kerbl's papers directly build on and benchmark against one another.

## Ordered Milestone Stops (West → East)

| # | Year | Milestone | Province | One-Line Summary |
|---|------|-----------|----------|------------------|
| 1 | `2020.22` | [NeRF 3D Fields](/milestones/nerf-mildenhall-2020.md) | [The Attention Promontory](/provinces/multimodal-scientific-transformers.md) | Mildenhall et al. (Mar 2020) introduce Neural Radiance Fields (NeRF) for 3D view synthesis |
| 2 | `2022.75` | [DreamFusion 3D](/milestones/dreamfusion-2022.md) | [The Diffusion Shoreline](/provinces/diffusion-media-district.md) | Poole et al. (Sep 2022): Score Distillation Sampling lifts 2D diffusion into 3D NeRFs |
| 3 | `2023.61` | [3D Gaussian Splatting](/milestones/gaussian-splatting-2023.md) | [The Diffusion Shoreline](/provinces/diffusion-media-district.md) | Kerbl et al. (SIGGRAPH Aug 2023): real-time 3D radiance field rendering at 100+ fps |

## Directed Road Segments

- [NeRF 3D Fields](/milestones/nerf-mildenhall-2020.md) (`2020.22`) → [DreamFusion 3D](/milestones/dreamfusion-2022.md) (`2022.75`)
- [DreamFusion 3D](/milestones/dreamfusion-2022.md) (`2022.75`) → [3D Gaussian Splatting](/milestones/gaussian-splatting-2023.md) (`2023.61`)
