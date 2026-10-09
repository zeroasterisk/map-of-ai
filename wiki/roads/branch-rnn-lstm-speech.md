---
type: Lineage Road
title: The Recurrent Net, LSTM & End-to-End Speech Road
description: Traces sequence and speech modeling from Waibel's TDNN (1989), Elman's Simple Recurrent Network (1990), Hochreiter's
  Vanishing Gradient diploma thesis (1991), and Hochreiter & Schmidhuber's LSTM (1997) through Hinton/Deng DNN acoustic models
  (2009), the Four Groups speech paper (2012), Graves-Mohamed-Hinton Deep Bidirectional LSTM speech (2013), and Baidu Deep
  Speech (2014) to Switchboard conversational parity (2016).
road_id: branch-rnn-lstm-speech
road_tier: branch
stop_count: 9
status: active
generated:
  by: gemini-4-argon/1.0
  at: '2026-10-08T20:15:00Z'
verified:
- by: human:zeroasterisk
  at: '2026-10-08T20:15:00Z'
sources:
- resource: https://doi.org/10.1109/29.21701
  title: Waibel et al., Phoneme Recognition Using Time-Delay Neural Networks, 1989 [18]
- resource: https://en.wikipedia.org/wiki/Deep_learning
  title: 'Wikipedia: Deep learning [1]'
- resource: https://ieeexplore.ieee.org/document/6296526
  title: Hinton et al., IEEE SPM 2012 [11]
- resource: https://arxiv.org/abs/1610.05256
  title: Xiong et al., arXiv 1610.05256 [95]
---

# The Recurrent Net, LSTM & End-to-End Speech Road

**Road ID**: `branch-rnn-lstm-speech` · **Hierarchy Class**: `branch` · **Stops**: `9` · [Back to Roads Index](/roads/index.md)

## Historical & Architectural Rationale

Traces sequence and speech modeling from Waibel's TDNN (1989), Elman's Simple Recurrent Network (1990), Hochreiter's Vanishing Gradient diploma thesis (1991), and Hochreiter & Schmidhuber's LSTM (1997) through Hinton/Deng DNN acoustic models (2009), the Four Groups speech paper (2012), Graves-Mohamed-Hinton Deep Bidirectional LSTM speech (2013), and Baidu Deep Speech (2014) to Switchboard conversational parity (2016).

## 3-Test Knowledge Graph Audit

- **Lawyer Test**: Academic and published speech recognition progression with zero corporate misattribution.
- **Reddit Test**: Explicitly honors Hochreiter & Schmidhuber's 1991/1997 vanishing-gradient and LSTM lineage into Graves's 2013 deep LSTM speech and Deep Speech.
- **Individuals Involved Test**: Sepp Hochreiter, Jürgen Schmidhuber, Alex Graves, Geoffrey Hinton, and Li Deng's sequence/speech work is linked in strict causal order.

## Ordered Milestone Stops (West → East)

| # | Year | Milestone | Province | One-Line Summary |
|---|------|-----------|----------|------------------|
| 1 | `1989.2` | [Time-Delay Neural Net](/milestones/waibel-tdnn-speech-1989.md) | [The Early ConvNet Ridge](/provinces/early-convnet-ridge.md) | Alex Waibel et al. introduce Time-Delay Neural Networks (TDNN) for speech recognition |
| 2 | `1990.2` | [Elman RNN](/milestones/elman-srn-1990.md) | [The PDP Basin](/provinces/pdp-cognitive-school.md) | Jeffrey Elman introduces simple recurrent networks for sequences |
| 3 | `1991.6` | [Vanishing Gradients](/milestones/vanishing-gradient-1991.md) | [The Early ConvNet Ridge](/provinces/early-convnet-ridge.md) | Sepp Hochreiter diagnoses why deep recurrent nets fail backprop |
| 4 | `1997.85` | [LSTM](/milestones/lstm-1997.md) | [The Early ConvNet Ridge](/provinces/early-convnet-ridge.md) | Hochreiter & Schmidhuber introduce Long Short-Term Memory nets |
| 5 | `2009.6` | [DNN acoustic models](/milestones/dnn-acoustic-2009.md) | [The Speech Conversion](/provinces/speech-recognition-converts.md) | Hinton's Toronto group + Li Deng (Microsoft) replace GMMs with deep nets |
| 6 | `2012.85` | [Four groups paper](/milestones/four-groups-2012.md) | [The Speech Conversion](/provinces/speech-recognition-converts.md) | Toronto, Microsoft, Google, IBM declare DNNs the standard; error rates fall ~30 % |
| 7 | `2013.25` | [deep LSTM speech](/milestones/deep-lstm-speech-2013.md) | [The Speech Conversion](/provinces/speech-recognition-converts.md) | Graves, Mohamed & Hinton: bidirectional LSTMs, no phonetic alignment |
| 8 | `2014.95` | [Deep Speech](/milestones/deep-speech-2014.md) | [The Speech Conversion](/provinces/speech-recognition-converts.md) | Baidu (Hannun et al.): end-to-end RNN recogniser on noisy speech at scale |
| 9 | `2016.8` | [Switchboard parity](/milestones/switchboard-2016.md) | [The Speech Conversion](/provinces/speech-recognition-converts.md) | Microsoft (Xiong et al.): 5.9 % word error rate, matching transcribers |

## Directed Road Segments

- [Time-Delay Neural Net](/milestones/waibel-tdnn-speech-1989.md) (`1989.2`) → [Elman RNN](/milestones/elman-srn-1990.md) (`1990.2`)
- [Elman RNN](/milestones/elman-srn-1990.md) (`1990.2`) → [Vanishing Gradients](/milestones/vanishing-gradient-1991.md) (`1991.6`)
- [Vanishing Gradients](/milestones/vanishing-gradient-1991.md) (`1991.6`) → [LSTM](/milestones/lstm-1997.md) (`1997.85`)
- [LSTM](/milestones/lstm-1997.md) (`1997.85`) → [DNN acoustic models](/milestones/dnn-acoustic-2009.md) (`2009.6`)
- [DNN acoustic models](/milestones/dnn-acoustic-2009.md) (`2009.6`) → [Four groups paper](/milestones/four-groups-2012.md) (`2012.85`)
- [Four groups paper](/milestones/four-groups-2012.md) (`2012.85`) → [deep LSTM speech](/milestones/deep-lstm-speech-2013.md) (`2013.25`)
- [deep LSTM speech](/milestones/deep-lstm-speech-2013.md) (`2013.25`) → [Deep Speech](/milestones/deep-speech-2014.md) (`2014.95`)
- [Deep Speech](/milestones/deep-speech-2014.md) (`2014.95`) → [Switchboard parity](/milestones/switchboard-2016.md) (`2016.8`)
