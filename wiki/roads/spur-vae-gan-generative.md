---
type: Lineage Road
title: The VAE, GAN & Autoregressive Deep Generative Spur
description: Traces the 2013–2017 deep generative modeling shoreline from Kingma & Welling's Variational Autoencoder (VAE,
  Dec 2013) and Goodfellow et al.'s GANs (Jun 2014) through DeepDream (2015), Gatys et al.'s Neural Style Transfer (2015),
  Radford et al.'s DCGAN (2015), van den Oord et al.'s PixelRNN/PixelCNN (2016) and WaveNet (2016), to Isola & Zhu's pix2pix
  and CycleGAN (2017).
road_id: spur-vae-gan-generative
road_tier: spur
stop_count: 8
status: active
generated:
  by: gemini-4-argon/1.0
  at: '2026-10-08T20:15:00Z'
verified:
- by: human:zeroasterisk
  at: '2026-10-08T20:15:00Z'
sources:
- resource: https://arxiv.org/abs/1312.6114
  title: Kingma & Welling, arXiv 1312.6114 [27]
- resource: https://arxiv.org/abs/1511.06434
  title: Radford, Metz & Chintala, DCGAN [73]
- resource: https://arxiv.org/abs/1703.10593
  title: Zhu, Park, Isola & Efros, CycleGAN, arXiv 1703.10593 [74]
---

# The VAE, GAN & Autoregressive Deep Generative Spur

**Road ID**: `spur-vae-gan-generative` · **Hierarchy Class**: `spur` · **Stops**: `8` · [Back to Roads Index](/roads/index.md)

## Historical & Architectural Rationale

Traces the 2013–2017 deep generative modeling shoreline from Kingma & Welling's Variational Autoencoder (VAE, Dec 2013) and Goodfellow et al.'s GANs (Jun 2014) through DeepDream (2015), Gatys et al.'s Neural Style Transfer (2015), Radford et al.'s DCGAN (2015), van den Oord et al.'s PixelRNN/PixelCNN (2016) and WaveNet (2016), to Isola & Zhu's pix2pix and CycleGAN (2017).

## 3-Test Knowledge Graph Audit

- **Lawyer Test**: Published deep generative modeling papers (`VAE -> GAN -> DCGAN -> PixelRNN -> WaveNet -> pix2pix/CycleGAN`).
- **Reddit Test**: Fixes the backward-in-time `vae-2013 <- gan-2014` edge from the old nearest-neighbor graph and traces the exact pre-diffusion generative shoreline.
- **Individuals Involved Test**: Diederik Kingma, Max Welling, Ian Goodfellow, Alec Radford, Aäron van den Oord, and Phillip Isola are linked in strict publication order.

## Ordered Milestone Stops (West → East)

| # | Year | Milestone | Province | One-Line Summary |
|---|------|-----------|----------|------------------|
| 1 | `2013.97` | [VAE](/milestones/vae-2013.md) | [The Generative Shoreline](/provinces/deep-generative-shoreline.md) | Kingma & Welling: auto-encoding variational Bayes (Dec 2013) |
| 2 | `2014.45` | [GAN](/milestones/gan-2014.md) | [The Generative Shoreline](/provinces/deep-generative-shoreline.md) | Goodfellow et al. (Montréal): generative adversarial networks (Jun 2014) |
| 3 | `2015.46` | [DeepDream](/milestones/deepdream-2015.md) | [The Generative Shoreline](/provinces/deep-generative-shoreline.md) | Mordvintsev, Olah & Tyka: the first viral neural-art moment |
| 4 | `2015.65` | [style transfer](/milestones/style-transfer-2015.md) | [The Generative Shoreline](/provinces/deep-generative-shoreline.md) | Gatys, Ecker & Bethge (Tübingen): A Neural Algorithm of Artistic Style |
| 5 | `2015.88` | [DCGAN](/milestones/dcgan-2015.md) | [The Generative Shoreline](/provinces/deep-generative-shoreline.md) | Radford, Metz & Chintala make GANs practical for images |
| 6 | `2016.07` | [PixelRNN](/milestones/pixelrnn-2016.md) | [The Generative Shoreline](/provinces/deep-generative-shoreline.md) | van den Oord et al.: autoregressive image likelihoods |
| 7 | `2016.7` | [WaveNet](/milestones/wavenet-2016.md) | [The Generative Shoreline](/provinces/deep-generative-shoreline.md) | DeepMind generates raw audio sample by sample (Sep 2016) |
| 8 | `2017.25` | [pix2pix & CycleGAN](/milestones/pix2pix-cyclegan-2017.md) | [The Generative Shoreline](/provinces/deep-generative-shoreline.md) | Isola, Zhu and Efros introduce conditional and unpaired adversarial image translation |

## Directed Road Segments

- [VAE](/milestones/vae-2013.md) (`2013.97`) → [GAN](/milestones/gan-2014.md) (`2014.45`)
- [GAN](/milestones/gan-2014.md) (`2014.45`) → [DeepDream](/milestones/deepdream-2015.md) (`2015.46`)
- [DeepDream](/milestones/deepdream-2015.md) (`2015.46`) → [style transfer](/milestones/style-transfer-2015.md) (`2015.65`)
- [style transfer](/milestones/style-transfer-2015.md) (`2015.65`) → [DCGAN](/milestones/dcgan-2015.md) (`2015.88`)
- [DCGAN](/milestones/dcgan-2015.md) (`2015.88`) → [PixelRNN](/milestones/pixelrnn-2016.md) (`2016.07`)
- [PixelRNN](/milestones/pixelrnn-2016.md) (`2016.07`) → [WaveNet](/milestones/wavenet-2016.md) (`2016.7`)
- [WaveNet](/milestones/wavenet-2016.md) (`2016.7`) → [pix2pix & CycleGAN](/milestones/pix2pix-cyclegan-2017.md) (`2017.25`)
