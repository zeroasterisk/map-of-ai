---
type: Lineage Road
title: The OpenAI Multimodal, DALL-E, Whisper & Sora Road
description: Pure OpenAI multimodal generation lineage from GPT-3 (2020) through DALL-E & CLIP (Jan 2021), GLIDE (Dec 2021),
  DALL-E 2 (Apr 2022), Whisper (Sep 2022), DALL-E 3 (Sep 2023), Sora (Feb 2024), to Sora 2 (Sep 2025).
road_id: branch-openai-media
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
- resource: https://arxiv.org/abs/2005.14165
  title: Brown et al., GPT-3, arXiv 2005.14165 [11]
- resource: https://en.wikipedia.org/wiki/GPT-3
  title: 'Wikipedia: GPT-3 [12]'
- resource: https://en.wikipedia.org/wiki/Whisper_%28speech_recognition_system%29
  title: 'Wikipedia: Whisper (speech recognition system) [42]'
- resource: https://web.archive.org/web/2025/https://openai.com/index/sora-2/
  title: OpenAI, Sora 2 is here, 30 Sep 2025 (archived) [112]
- resource: https://simonwillison.net/2025/Sep/30/sora-2/
  title: Simon Willison, Sora 2, 30 Sep 2025 [112]
---

# The OpenAI Multimodal, DALL-E, Whisper & Sora Road

**Road ID**: `branch-openai-media` · **Hierarchy Class**: `branch` · **Stops**: `8` · [Back to Roads Index](/roads/index.md)

## Historical & Architectural Rationale

Pure OpenAI multimodal generation lineage from GPT-3 (2020) through DALL-E & CLIP (Jan 2021), GLIDE (Dec 2021), DALL-E 2 (Apr 2022), Whisper (Sep 2022), DALL-E 3 (Sep 2023), Sora (Feb 2024), to Sora 2 (Sep 2025).

## 3-Test Knowledge Graph Audit

- **Lawyer Test**: 100% OpenAI multimodal lineage; `sora-2024` now connects directly to `sora2-2025` instead of routing through Google's `imagen3-2024`, `notebooklm-audio-2024`, and `veo3-2025`.
- **Reddit Test**: Keeps OpenAI's image, audio, and video models (`DALL-E -> GLIDE -> DALL-E 2 -> Whisper -> DALL-E 3 -> Sora -> Sora 2`) on a single clean OpenAI multimodal branch.
- **Individuals Involved Test**: Aditya Ramesh, Alec Radford, Prafulla Dhariwal, Bill Peebles, and Tim Brooks's OpenAI multimodal work is cleanly linked.

## Ordered Milestone Stops (West → East)

| # | Year | Milestone | Province | One-Line Summary |
|---|------|-----------|----------|------------------|
| 1 | `2020.41` | [GPT-3](/milestones/gpt3-2020.md) | [The Autoregressive Ridge](/provinces/decoder-generative-school.md) | Brown et al. (28 May 2020): 175 B parameters; few-shot in-context learning; API 11 Jun |
| 2 | `2021.01` | [DALL-E · CLIP](/milestones/dalle-clip-2021.md) | [The Attention Promontory](/provinces/multimodal-scientific-transformers.md) | OpenAI (5 Jan 2021): text-to-image DALL-E and contrastive image–text CLIP — the CLIP bridge |
| 3 | `2021.97` | [GLIDE](/milestones/glide-2021.md) | [The Attention Promontory](/provinces/multimodal-scientific-transformers.md) | Nichol et al. (20 Dec 2021): text-guided diffusion, the step before DALL-E 2 |
| 4 | `2022.27` | [DALL-E 2](/milestones/dalle2-2022.md) | [The Diffusion Shoreline](/provinces/diffusion-media-district.md) | OpenAI announces DALL-E 2 (6 Apr 2022): photoreal text-to-image starts the "AI art" year |
| 5 | `2022.71` | [Whisper](/milestones/whisper-2022.md) | [The Attention Promontory](/provinces/multimodal-scientific-transformers.md) | OpenAI open-sources Whisper speech recognition (Sep 2022): the Transformer conquers speech |
| 6 | `2023.72` | [DALL-E 3](/milestones/dalle3-2023.md) | [The Diffusion Shoreline](/provinces/diffusion-media-district.md) | OpenAI integrates DALL-E 3 with ChatGPT (Sep 2023) using synthetic recaptioning for prompt adherence |
| 7 | `2024.12` | [Sora](/milestones/sora-2024.md) | [The Diffusion Shoreline](/provinces/diffusion-media-district.md) | OpenAI previews Sora text-to-video (15 Feb 2024): minute-long video, "world simulator" framing |
| 8 | `2025.75` | [Sora 2](/milestones/sora2-2025.md) | [The Diffusion Shoreline](/provinces/diffusion-media-district.md) | OpenAI launches Sora 2 (30 Sep 2025) with synchronized audio and physics-aware video synthesis |

## Directed Road Segments

- [GPT-3](/milestones/gpt3-2020.md) (`2020.41`) → [DALL-E · CLIP](/milestones/dalle-clip-2021.md) (`2021.01`)
- [DALL-E · CLIP](/milestones/dalle-clip-2021.md) (`2021.01`) → [GLIDE](/milestones/glide-2021.md) (`2021.97`)
- [GLIDE](/milestones/glide-2021.md) (`2021.97`) → [DALL-E 2](/milestones/dalle2-2022.md) (`2022.27`)
- [DALL-E 2](/milestones/dalle2-2022.md) (`2022.27`) → [Whisper](/milestones/whisper-2022.md) (`2022.71`)
- [Whisper](/milestones/whisper-2022.md) (`2022.71`) → [DALL-E 3](/milestones/dalle3-2023.md) (`2023.72`)
- [DALL-E 3](/milestones/dalle3-2023.md) (`2023.72`) → [Sora](/milestones/sora-2024.md) (`2024.12`)
- [Sora](/milestones/sora-2024.md) (`2024.12`) → [Sora 2](/milestones/sora2-2025.md) (`2025.75`)
