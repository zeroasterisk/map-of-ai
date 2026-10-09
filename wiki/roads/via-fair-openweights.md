---
type: Lineage Road
title: The Meta FAIR, PyTorch & Llama Open-Weights Highway
description: 'Pure Meta FAIR / Meta AI research and open-weights lineage: FAIR founded by Yann LeCun (2013), PyTorch (2017),
  RoBERTa (2019), RAG (2020), OPT-175B (2022), ESMFold (2022), Galactica (2022), LLaMA (2023), Llama 2 (2023), Code Llama
  (2023), Llama 3 & 3.1 405B (2024), Llama 3.2 & 3.3 (2024), and Llama 4 (2025).'
road_id: via-fair-openweights
road_tier: trunk
stop_count: 13
status: active
generated:
  by: gemini-4-argon/1.0
  at: '2026-10-08T20:15:00Z'
verified:
- by: human:zeroasterisk
  at: '2026-10-08T20:15:00Z'
sources:
- resource: https://en.wikipedia.org/wiki/Yann_LeCun
  title: 'Wikipedia: Yann LeCun [59]'
- resource: https://arxiv.org/abs/2211.09085
  title: Taylor et al., Galactica, arXiv 2211.09085 [85]
- resource: https://www.technologyreview.com/2022/11/18/1063487/meta-large-language-model-ai-only-survived-three-days-gpt-3-science/
  title: MIT Technology Review, 18 Nov 2022 [86]
- resource: https://huggingface.co/api/models?author=meta-llama&search=Llama-4&limit=5
  title: Hugging Face model index, meta-llama/Llama-4 [117]
- resource: https://simonwillison.net/2025/Apr/5/llama-4-notes/
  title: Simon Willison, Initial impressions of Llama 4, 5 Apr 2025 [117]
---

# The Meta FAIR, PyTorch & Llama Open-Weights Highway

**Road ID**: `via-fair-openweights` · **Hierarchy Class**: `trunk` · **Stops**: `13` · [Back to Roads Index](/roads/index.md)

## Historical & Architectural Rationale

Pure Meta FAIR / Meta AI research and open-weights lineage: FAIR founded by Yann LeCun (2013), PyTorch (2017), RoBERTa (2019), RAG (2020), OPT-175B (2022), ESMFold (2022), Galactica (2022), LLaMA (2023), Llama 2 (2023), Code Llama (2023), Llama 3 & 3.1 405B (2024), Llama 3.2 & 3.3 (2024), and Llama 4 (2025).

## 3-Test Knowledge Graph Audit

- **Lawyer Test**: Removes Google Gemma, Mistral/Mixtral, DeepSeek, and OpenAI `gpt-oss` from the Meta Llama trunk so Meta's open-weights license line is never conflated with Google, DeepSeek, or OpenAI models.
- **Reddit Test**: Fixes the biggest open-weights complaint in the old graph (which chained `mixtral -> gemma -> llama3 -> deepseek-v2 -> gemma2 -> deepseek-v3 -> deepseek-r1 -> gemma3 -> llama4 -> gpt-oss -> gemma4` as if they were a single lineage).
- **Individuals Involved Test**: Yann LeCun and the Meta FAIR / Llama teams have a pure, unbroken FAIR -> PyTorch -> OPT -> Llama 1–4 highway.

## Ordered Milestone Stops (West → East)

| # | Year | Milestone | Province | One-Line Summary |
|---|------|-----------|----------|------------------|
| 1 | `2013.93` | [FAIR founded](/milestones/fair-2013.md) | [The Corporate Lab Colonies](/provinces/industrial-lab-founders.md) | LeCun becomes founding director of Facebook AI Research (9 Dec 2013) |
| 2 | `2017.05` | [PyTorch Released](/milestones/pytorch-2017.md) | [The Eastern Coast Forts](/provinces/chinese-state-response.md) | Paszke, Chintala and FAIR release PyTorch (Jan 2017) with eager autograd execution |
| 3 | `2019.57` | [RoBERTa](/milestones/roberta-2019.md) | [The BERT Escarpment](/provinces/encoder-understanding-school.md) | Facebook AI (26 Jul 2019): BERT trained longer on more data retakes GLUE |
| 4 | `2020.4` | [RAG](/milestones/rag-2020.md) | [The BERT Escarpment](/provinces/encoder-understanding-school.md) | Lewis et al.: retrieval-augmented generation — the eastern border of the encoder camp |
| 5 | `2022.34` | [OPT-175B](/milestones/opt-175b-2022.md) | [The Eleutherian Commons](/provinces/open-replication-commons.md) | Meta AI (3 May 2022): GPT-3-scale weights to researchers plus the full training logbook |
| 6 | `2022.55` | [ESM-2 & ESMFold](/milestones/esmfold-lin-2022.md) | [The Attention Promontory](/provinces/multimodal-scientific-transformers.md) | Meta AI's ESMFold predicts 600M metagenomic protein structures from single sequences |
| 7 | `2022.87` | [Galactica](/milestones/galactica-2022.md) | [The Human-Feedback Tributaries](/provinces/alignment-critique-tributaries.md) | Meta's 120 B science LLM (15 Nov 2022) withdrawn after three days of confident fabrications |
| 8 | `2023.15` | [LLaMA leak](/milestones/llama-leak-2023.md) | [The Open-Weights Commons](/provinces/open-weights-movement.md) | Meta's LLaMA (24 Feb 2023) leaks via 4chan torrent 3 Mar; the open-weights ecosystem ignites |
| 9 | `2023.55` | [Llama 2](/milestones/llama2-2023.md) | [The Open-Weights Commons](/provinces/open-weights-movement.md) | Llama 2 (18 Jul 2023) under a commercial licence: open weights become deliberate strategy |
| 10 | `2023.64` | [Code Llama](/milestones/codellama-2023.md) | [The Open-Weights Commons](/provinces/open-weights-movement.md) | Meta releases Code Llama (24 Aug 2023): open 7B–34B code models trained on 500B tokens |
| 11 | `2024.3` | [Llama 3 & 3.1 405B](/milestones/llama3-2024.md) | [The Open-Weights Commons](/provinces/open-weights-movement.md) | Llama 3 (18 Apr 2024) on 15T tokens; 405B Llama 3.1 (23 Jul) reaches GPT-4 class |
| 12 | `2024.93` | [Llama 3.2 & 3.3](/milestones/llama33-2024.md) | [The Open-Weights Commons](/provinces/open-weights-movement.md) | Meta ships multimodal Llama 3.2 (Sep 2024) and 70B Llama 3.3 matching 405B quality |
| 13 | `2025.26` | [Llama 4](/milestones/llama4-2025.md) | [The Open-Weights Commons](/provinces/open-weights-movement.md) | Llama 4 Scout & Maverick (5 Apr 2025): native multimodal MoE open-weights release |

## Directed Road Segments

- [FAIR founded](/milestones/fair-2013.md) (`2013.93`) → [PyTorch Released](/milestones/pytorch-2017.md) (`2017.05`)
- [PyTorch Released](/milestones/pytorch-2017.md) (`2017.05`) → [RoBERTa](/milestones/roberta-2019.md) (`2019.57`)
- [RoBERTa](/milestones/roberta-2019.md) (`2019.57`) → [RAG](/milestones/rag-2020.md) (`2020.4`)
- [RAG](/milestones/rag-2020.md) (`2020.4`) → [OPT-175B](/milestones/opt-175b-2022.md) (`2022.34`)
- [OPT-175B](/milestones/opt-175b-2022.md) (`2022.34`) → [ESM-2 & ESMFold](/milestones/esmfold-lin-2022.md) (`2022.55`)
- [ESM-2 & ESMFold](/milestones/esmfold-lin-2022.md) (`2022.55`) → [Galactica](/milestones/galactica-2022.md) (`2022.87`)
- [Galactica](/milestones/galactica-2022.md) (`2022.87`) → [LLaMA leak](/milestones/llama-leak-2023.md) (`2023.15`)
- [LLaMA leak](/milestones/llama-leak-2023.md) (`2023.15`) → [Llama 2](/milestones/llama2-2023.md) (`2023.55`)
- [Llama 2](/milestones/llama2-2023.md) (`2023.55`) → [Code Llama](/milestones/codellama-2023.md) (`2023.64`)
- [Code Llama](/milestones/codellama-2023.md) (`2023.64`) → [Llama 3 & 3.1 405B](/milestones/llama3-2024.md) (`2024.3`)
- [Llama 3 & 3.1 405B](/milestones/llama3-2024.md) (`2024.3`) → [Llama 3.2 & 3.3](/milestones/llama33-2024.md) (`2024.93`)
- [Llama 3.2 & 3.3](/milestones/llama33-2024.md) (`2024.93`) → [Llama 4](/milestones/llama4-2025.md) (`2025.26`)
