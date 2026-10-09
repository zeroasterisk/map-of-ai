---
type: Lineage Road
title: The Hugging Face, EleutherAI, BigScience & AI2 Open Commons Spur
description: Traces the open-source LLM replication and fully open training-data commons from GPT-2 (Feb 2019), Hugging Face
  Transformers (Oct 2019), and DistilBERT (Oct 2019) through EleutherAI's The Pile 825 GB dataset (Dec 2020), GPT-J 6B (Jun
  2021), GPT-NeoX-20B (Feb 2022), Yandex YaLM 100B (Jun 2022), BigScience's multilingual BLOOM 176B (Jul 2022), and TII's
  Falcon 40B (May 2023) to AI2's fully open-data/open-code OLMo (Feb 2024).
road_id: spur-eleuther-bigscience
road_tier: spur
stop_count: 10
status: active
generated:
  by: gemini-4-argon/1.0
  at: '2026-10-08T20:15:00Z'
verified:
- by: human:zeroasterisk
  at: '2026-10-08T20:15:00Z'
sources:
- resource: https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf
  title: Radford et al., GPT-2 paper [28]
- resource: https://en.wikipedia.org/wiki/GPT-2
  title: 'Wikipedia: GPT-2 [29]'
- resource: https://arxiv.org/abs/2204.06745
  title: Black et al., GPT-NeoX-20B, arXiv 2204.06745 [73]
- resource: https://arxiv.org/abs/2402.00838
  title: 'Groeneveld et al., OLMo: Accelerating the Science of Language Models, arXiv 2402.00838 [48]'
---

# The Hugging Face, EleutherAI, BigScience & AI2 Open Commons Spur

**Road ID**: `spur-eleuther-bigscience` · **Hierarchy Class**: `spur` · **Stops**: `10` · [Back to Roads Index](/roads/index.md)

## Historical & Architectural Rationale

Traces the open-source LLM replication and fully open training-data commons from GPT-2 (Feb 2019), Hugging Face Transformers (Oct 2019), and DistilBERT (Oct 2019) through EleutherAI's The Pile 825 GB dataset (Dec 2020), GPT-J 6B (Jun 2021), GPT-NeoX-20B (Feb 2022), Yandex YaLM 100B (Jun 2022), BigScience's multilingual BLOOM 176B (Jul 2022), and TII's Falcon 40B (May 2023) to AI2's fully open-data/open-code OLMo (Feb 2024).

## 3-Test Knowledge Graph Audit

- **Lawyer Test**: Community and open-science replication milestones (`Hugging Face`, `EleutherAI`, `BigScience`, `TII`, `AI2`).
- **Reddit Test**: Traces the exact pre-Llama and open-science community LLM movement (`Hugging Face -> The Pile -> GPT-J -> GPT-NeoX -> BLOOM -> Falcon -> OLMo`).
- **Individuals Involved Test**: Thomas Wolf, Victor Sanh, Stella Biderman, Connor Leahy, Leo Gao, Teven Le Scao, and Hanna Hajishirzi's open-science efforts are linked in exact chronological order.

## Ordered Milestone Stops (West → East)

| # | Year | Milestone | Province | One-Line Summary |
|---|------|-----------|----------|------------------|
| 1 | `2019.12` | [GPT-2](/milestones/gpt2-2019.md) | [The Autoregressive Ridge](/provinces/decoder-generative-school.md) | 1.5 B parameters on 8 M web pages (Feb 2019); withheld as "too dangerous" |
| 2 | `2019.6` | [Hugging Face transformers](/milestones/hf-transformers-2019.md) | [The Eleutherian Commons](/provinces/open-replication-commons.md) | the open-source library becomes the de facto hub for sharing pretrained Transformers |
| 3 | `2019.75` | [DistilBERT](/milestones/distilbert-2019.md) | [The BERT Escarpment](/provinces/encoder-understanding-school.md) | Hugging Face (2 Oct 2019): distillation for deployment — 40 % smaller, 60 % faster |
| 4 | `2020.99` | [The Pile](/milestones/the-pile-2020.md) | [The Eleutherian Commons](/provinces/open-replication-commons.md) | EleutherAI (31 Dec 2020): 825 GB open training corpus — grassroots GPT-3 replication begins |
| 5 | `2021.45` | [GPT-Neo · GPT-J](/milestones/gpt-j-2021.md) | [The Eleutherian Commons](/provinces/open-replication-commons.md) | EleutherAI's open GPT-3-style models (2021), GPT-J at 6 B parameters |
| 6 | `2022.27` | [GPT-NeoX-20B](/milestones/gpt-neox-2022.md) | [The Eleutherian Commons](/provinces/open-replication-commons.md) | EleutherAI (Apr 2022): open-source autoregressive 20 B model and training code |
| 7 | `2022.47` | [YaLM-100B](/milestones/yalm-2022.md) | [The Eleutherian Commons](/provinces/open-replication-commons.md) | Yandex open-sources a 100 B model (Jun 2022) trained on 800 A100s |
| 8 | `2022.54` | [BLOOM](/milestones/bloom-2022.md) | [The Eleutherian Commons](/provinces/open-replication-commons.md) | BigScience (Jul 2022): 176 B, 46 languages, RAIL licence, trained on France's Jean Zay |
| 9 | `2023.41` | [Falcon 40B & 180B](/milestones/falcon-40b-2023.md) | [The Open-Weights Commons](/provinces/open-weights-movement.md) | TII releases Apache-2.0 Falcon 40B (May 2023) and 180B trained on RefinedWeb |
| 10 | `2024.09` | [AI2 OLMo & Dolma](/milestones/olmo-ai2-2024.md) | [The Open-Weights Commons](/provinces/open-weights-movement.md) | Allen Institute releases OLMo (1 Feb 2024) with open weights, training code, and Dolma corpus |

## Directed Road Segments

- [GPT-2](/milestones/gpt2-2019.md) (`2019.12`) → [Hugging Face transformers](/milestones/hf-transformers-2019.md) (`2019.6`)
- [Hugging Face transformers](/milestones/hf-transformers-2019.md) (`2019.6`) → [DistilBERT](/milestones/distilbert-2019.md) (`2019.75`)
- [DistilBERT](/milestones/distilbert-2019.md) (`2019.75`) → [The Pile](/milestones/the-pile-2020.md) (`2020.99`)
- [The Pile](/milestones/the-pile-2020.md) (`2020.99`) → [GPT-Neo · GPT-J](/milestones/gpt-j-2021.md) (`2021.45`)
- [GPT-Neo · GPT-J](/milestones/gpt-j-2021.md) (`2021.45`) → [GPT-NeoX-20B](/milestones/gpt-neox-2022.md) (`2022.27`)
- [GPT-NeoX-20B](/milestones/gpt-neox-2022.md) (`2022.27`) → [YaLM-100B](/milestones/yalm-2022.md) (`2022.47`)
- [YaLM-100B](/milestones/yalm-2022.md) (`2022.47`) → [BLOOM](/milestones/bloom-2022.md) (`2022.54`)
- [BLOOM](/milestones/bloom-2022.md) (`2022.54`) → [Falcon 40B & 180B](/milestones/falcon-40b-2023.md) (`2023.41`)
- [Falcon 40B & 180B](/milestones/falcon-40b-2023.md) (`2023.41`) → [AI2 OLMo & Dolma](/milestones/olmo-ai2-2024.md) (`2024.09`)
