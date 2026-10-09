---
type: Lineage Road
title: The Vision Transformer to Segment Anything (SAM) Spur
description: Connects the Vision Transformer (`vit-2020`) to Meta FAIR's Segment Anything Model (`sam-2023`, Kirillov et al.,
  Apr 2023), which pairs a MAE pre-trained ViT-H image encoder with a promptable mask decoder trained on 1.1 billion masks.
road_id: spur-meta-vision
road_tier: spur
stop_count: 2
status: active
generated:
  by: gemini-4-argon/1.0
  at: '2026-10-08T20:15:00Z'
verified:
- by: human:zeroasterisk
  at: '2026-10-08T20:15:00Z'
sources:
- resource: https://arxiv.org/abs/2010.11929
  title: Dosovitskiy et al., ViT, arXiv 2010.11929 [13]
- resource: https://arxiv.org/abs/2304.02643
  title: Kirillov et al., Segment Anything, arXiv 2304.02643 [35]
---

# The Vision Transformer to Segment Anything (SAM) Spur

**Road ID**: `spur-meta-vision` · **Hierarchy Class**: `spur` · **Stops**: `2` · [Back to Roads Index](/roads/index.md)

## Historical & Architectural Rationale

Connects the Vision Transformer (`vit-2020`) to Meta FAIR's Segment Anything Model (`sam-2023`, Kirillov et al., Apr 2023), which pairs a MAE pre-trained ViT-H image encoder with a promptable mask decoder trained on 1.1 billion masks.

## 3-Test Knowledge Graph Audit

- **Lawyer Test**: Cites public architectural lineage (SAM is built directly on a ViT-H backbone).
- **Reddit Test**: Stays compactly within the vision/media coast (`dy < 50`) and reflects SAM's actual ViT-H architecture.
- **Individuals Involved Test**: Alexander Kirillov, Kaiming He, and Ross Girshick built SAM directly on ViT-H.

## Ordered Milestone Stops (West → East)

| # | Year | Milestone | Province | One-Line Summary |
|---|------|-----------|----------|------------------|
| 1 | `2020.81` | [Vision Transformer](/milestones/vit-2020.md) | [The Attention Promontory](/provinces/multimodal-scientific-transformers.md) | Dosovitskiy et al. (22 Oct 2020): an image is worth 16×16 words; Transformers displace CNNs |
| 2 | `2023.26` | [Segment Anything](/milestones/sam-2023.md) | [The Diffusion Shoreline](/provinces/diffusion-media-district.md) | Meta's promptable vision foundation model SAM (5 Apr 2023) trained on 1B masks |

## Directed Road Segments

- [Vision Transformer](/milestones/vit-2020.md) (`2020.81`) → [Segment Anything](/milestones/sam-2023.md) (`2023.26`)
