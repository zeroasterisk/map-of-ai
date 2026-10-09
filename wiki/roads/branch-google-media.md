---
type: Lineage Road
title: The Google Vision Transformer, Imagen, Veo & Genie World-Model Road
description: 'Pure Google / Google DeepMind visual, audio, video, and interactive world-model lineage: T5 (2019), Vision Transformer
  (ViT, 2020), Google Imagen (2022), DreamFusion 3D (2022), Imagen 3 (2024), NotebookLM Audio Overviews (2024), Veo 3 (2025),
  and Genie 3 (2025).'
road_id: branch-google-media
road_tier: branch
stop_count: 8
status: active
generated:
  by: gemini-4-argon/1.0
  at: '2026-10-08T20:15:00Z'
verified:
- by: human:zeroasterisk
  at: '2026-10-08T20:15:00Z'
sources:
- resource: https://arxiv.org/abs/1910.10683
  title: Raffel et al., T5, arXiv 1910.10683 [30]
- resource: https://en.wikipedia.org/wiki/T5_%28language_model%29
  title: 'Wikipedia: T5 [31]'
- resource: https://arxiv.org/abs/2408.07009
  title: Imagen 3 Team, Imagen 3 Technical Report, arXiv 2408.07009 [108]
- resource: https://deepmind.google/discover/blog/genie-3-a-new-frontier-for-world-models/
  title: Google DeepMind, Genie 3, 5 Aug 2025 [108]
---

# The Google Vision Transformer, Imagen, Veo & Genie World-Model Road

**Road ID**: `branch-google-media` · **Hierarchy Class**: `branch` · **Stops**: `8` · [Back to Roads Index](/roads/index.md)

## Historical & Architectural Rationale

Pure Google / Google DeepMind visual, audio, video, and interactive world-model lineage: T5 (2019), Vision Transformer (ViT, 2020), Google Imagen (2022), DreamFusion 3D (2022), Imagen 3 (2024), NotebookLM Audio Overviews (2024), Veo 3 (2025), and Genie 3 (2025).

## 3-Test Knowledge Graph Audit

- **Lawyer Test**: 100% Google Research / Google DeepMind generative media and world-model lineage; never routes through OpenAI Sora or Stability AI.
- **Reddit Test**: Shows how T5 text encoders and ViT backbones directly powered Google Imagen (`imagen-2022` uses frozen T5-XXL), DreamFusion, Imagen 3, Veo 3, and Genie 3.
- **Individuals Involved Test**: Alexey Dosovitskiy, Chitwan Saharia, Ben Poole, and the Google DeepMind Veo/Genie teams have a dedicated Google media road.

## Ordered Milestone Stops (West → East)

| # | Year | Milestone | Province | One-Line Summary |
|---|------|-----------|----------|------------------|
| 1 | `2019.81` | [T5 · C4](/milestones/t5-2019.md) | [The BERT Escarpment](/provinces/encoder-understanding-school.md) | Raffel et al. (23 Oct 2019): every NLP task as text-to-text; introduces the C4 corpus |
| 2 | `2020.81` | [Vision Transformer](/milestones/vit-2020.md) | [The Attention Promontory](/provinces/multimodal-scientific-transformers.md) | Dosovitskiy et al. (22 Oct 2020): an image is worth 16×16 words; Transformers displace CNNs |
| 3 | `2022.39` | [Google Imagen](/milestones/imagen-2022.md) | [The Diffusion Shoreline](/provinces/diffusion-media-district.md) | Saharia et al. (May 2022) show frozen T5 text encoders dramatically boost diffusion fidelity |
| 4 | `2022.75` | [DreamFusion 3D](/milestones/dreamfusion-2022.md) | [The Diffusion Shoreline](/provinces/diffusion-media-district.md) | Poole et al. (Sep 2022): Score Distillation Sampling lifts 2D diffusion into 3D NeRFs |
| 5 | `2024.62` | [Google Imagen 3](/milestones/imagen3-2024.md) | [The Diffusion Shoreline](/provinces/diffusion-media-district.md) | Google DeepMind releases Imagen 3 (Aug 2024) with photoreal lighting and crisp typography |
| 6 | `2024.7` | [NotebookLM Audio](/milestones/notebooklm-audio-2024.md) | [The Diffusion Shoreline](/provinces/diffusion-media-district.md) | Google's NotebookLM Audio Overviews (11 Sep 2024) turn source docs into two-host AI podcasts |
| 7 | `2025.38` | [Veo 3](/milestones/veo3-2025.md) | [The Diffusion Shoreline](/provinces/diffusion-media-district.md) | Google's Veo 3 (20 May 2025) generates high-definition video with synchronized native audio |
| 8 | `2025.6` | [Genie 3](/milestones/genie3-2025.md) | [The Diffusion Shoreline](/provinces/diffusion-media-district.md) | Genie 3 (5 Aug 2025): a real-time interactive 3D world model |

## Directed Road Segments

- [T5 · C4](/milestones/t5-2019.md) (`2019.81`) → [Vision Transformer](/milestones/vit-2020.md) (`2020.81`)
- [Vision Transformer](/milestones/vit-2020.md) (`2020.81`) → [Google Imagen](/milestones/imagen-2022.md) (`2022.39`)
- [Google Imagen](/milestones/imagen-2022.md) (`2022.39`) → [DreamFusion 3D](/milestones/dreamfusion-2022.md) (`2022.75`)
- [DreamFusion 3D](/milestones/dreamfusion-2022.md) (`2022.75`) → [Google Imagen 3](/milestones/imagen3-2024.md) (`2024.62`)
- [Google Imagen 3](/milestones/imagen3-2024.md) (`2024.62`) → [NotebookLM Audio](/milestones/notebooklm-audio-2024.md) (`2024.7`)
- [NotebookLM Audio](/milestones/notebooklm-audio-2024.md) (`2024.7`) → [Veo 3](/milestones/veo3-2025.md) (`2025.38`)
- [Veo 3](/milestones/veo3-2025.md) (`2025.38`) → [Genie 3](/milestones/genie3-2025.md) (`2025.6`)
