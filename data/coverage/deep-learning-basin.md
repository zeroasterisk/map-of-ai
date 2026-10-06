# Coverage matrix — deep-learning-basin

Continent: `deep-learning-basin` · Research file: `research/06-deep-learning-revolution-2006-2017.md` · Date: 2026-09-11 · Schools of thought bullets: 9 · Units: P2-T8 (header), P3-T8 (Table 1)

Check A-M2: `awk '/^## Schools of thought/{f=1;next} /^## /{f=0} f&&/^- /{n++} END{print n}' research/06-deep-learning-revolution-2006-2017.md` → 9 = Table 1 rows.

## Table 1 — schools of thought → countries (P3-T8)

| # | school bullet | decision | entity id | reason |
|---|---|---|---|---|
| 1 | Unsupervised pre-training / energy-model school (2006–2011) | country | `pretraining-foothills` | distinct era (pre-2012) and method (layer-wise pre-training, RBMs); the "foothills" of research/06 map notes |
| 2 | GPU supervised ConvNet school (2009–2015) | country | `gpu-convnet-school` | the ILSVRC escarpment; SPEC.md §2.10 worked example; detection/segmentation province kept inside it rather than split (would exceed 9 countries) |
| 3 | Neural NLP / sequence school (2011–2016) | country | `neural-nlp-sequence-school` | own band (C) and own lineage (word2vec → seq2seq → attention → GNMT); Attention River source |
| 4 | Deep reinforcement learning school (2013–2017) | country | `deep-rl-delta` | own band (S1) and biome (wetland); AlphaGo delta |
| 5 | Deep generative modelling shoreline (2013–2017) | country | `deep-generative-shoreline` | VAE/GAN/autoregressive family is a distinct lineage that seeds the Generative Coast; kept separate from bullet 1 despite the "reborn" link because eras don't overlap |
| 6 | Speech-recognition converts (2009–2016) | country | `speech-recognition-converts` | first sector fully converted; distinct sources (Microsoft/IBM/Baidu) from the vision school |
| 7 | Tooling and infrastructure guild | country | `tooling-guild` | harbour biome per AXES.md palette; spans the parent's whole time range (2007–2017) |
| 8 | The industrial-lab founders (2011–2015) | country | `industrial-lab-founders` | institutional rather than methodological; kept as its own province because research/06 map notes name the labs as A2 countries |
| 9 | The Chinese and state response (2014–2017) | country | `chinese-state-response` | eastern-coast forts; the only non-Anglo-Canadian province and the policy hand-off to files 07–08 |

Decisions: 9 country · 0 merged-into · 0 dropped. Country count 9 = SPEC.md §4.3 upper bound.

Notes for P3-T12 review (A-K7 band/biome judgement calls): `chinese-state-response` biome grassland vs forest; `industrial-lab-founders` span C–S1; `tooling-guild` span S1–S2. Research/06 "Map notes" suggested A2 labels by *institution* (Toronto–Montréal–NYU, Stanford/ImageNet, IDSIA, Google Brain, DeepMind, FAIR, OpenAI); P3-T8 follows the `## Schools of thought` bullets instead, per SPEC.md A-K2 — institutions become cities (P4) inside these countries.

## Table 2 — cities (P4-T4, not started)
