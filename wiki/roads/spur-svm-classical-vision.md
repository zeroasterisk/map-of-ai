---
type: Lineage Road
title: The Support Vector Machine, SIFT & HOG Vision Spur
description: Traces statistical learning theory and classical feature-engineered computer vision from Nilsson's Learning Machines
  (1965) to Boser-Guyon-Vapnik's Kernel SVM & Cortes-Vapnik's Soft-Margin SVM (`svm-optimal-margin-1998`, `soft-margin-svm-1998`),
  David Lowe's SIFT descriptors (1999), Dalal & Triggs's HOG + linear SVM pedestrian detector (2005), and the launch of the
  ImageNet Large Scale Visual Recognition Challenge (ILSVRC, 2010, where SIFT+SVM was the baseline beaten by AlexNet in 2012).
road_id: spur-svm-classical-vision
road_tier: spur
stop_count: 6
status: active
generated:
  by: gemini-4-argon/1.0
  at: '2026-10-08T20:15:00Z'
verified:
- by: human:zeroasterisk
  at: '2026-10-08T20:15:00Z'
sources:
- resource: https://ai.stanford.edu/~nilsson/OnlinePubs-Nils/PublishedPapers/LearningMachines.pdf
  title: Nilsson, Learning Machines, 1965 [15]
- resource: https://doi.org/10.1109/ICCV.1999.790410
  title: Lowe, Object Recognition from Local Scale-Invariant Features, ICCV 1999 [40]
- resource: https://en.wikipedia.org/wiki/ImageNet_Large_Scale_Visual_Recognition_Challenge
  title: 'Wikipedia: ILSVRC [9]'
---

# The Support Vector Machine, SIFT & HOG Vision Spur

**Road ID**: `spur-svm-classical-vision` · **Hierarchy Class**: `spur` · **Stops**: `6` · [Back to Roads Index](/roads/index.md)

## Historical & Architectural Rationale

Traces statistical learning theory and classical feature-engineered computer vision from Nilsson's Learning Machines (1965) to Boser-Guyon-Vapnik's Kernel SVM & Cortes-Vapnik's Soft-Margin SVM (`svm-optimal-margin-1998`, `soft-margin-svm-1998`), David Lowe's SIFT descriptors (1999), Dalal & Triggs's HOG + linear SVM pedestrian detector (2005), and the launch of the ImageNet Large Scale Visual Recognition Challenge (ILSVRC, 2010, where SIFT+SVM was the baseline beaten by AlexNet in 2012).

## 3-Test Knowledge Graph Audit

- **Lawyer Test**: Removes Vapnik's SVMs from the neural network trunk (`via-western-connectionist`) and gives kernel methods + SIFT/HOG their own dedicated statistical-vision road.
- **Reddit Test**: Fixes the conflation of Kernel SVMs with LeNet-5 ConvNets and shows how SIFT (1999) + HOG/SVM (2005) formed the pre-AlexNet computer vision standard at ILSVRC 2010.
- **Individuals Involved Test**: Vladimir Vapnik, Isabelle Guyon, Corinna Cortes, David Lowe, and Navneet Dalal & Bill Triggs are connected along their own kernel & feature-descriptor paradigm.

## Ordered Milestone Stops (West → East)

| # | Year | Milestone | Province | One-Line Summary |
|---|------|-----------|----------|------------------|
| 1 | `1965.2` | [Learning Machines](/milestones/nilsson-learning-machines-1965.md) | [The Perceptron Escarpment](/provinces/early-perceptron-strip.md) | Nils Nilsson's monograph codifies linear and piecewise-linear pattern classifiers |
| 2 | `1998.2` | [Kernel SVM](/milestones/svm-optimal-margin-1998.md) | [The Support Vector Escarpment](/provinces/support-vector-escarpment.md) | Boser, Guyon & Vapnik apply Mercer kernels to maximal margins |
| 3 | `1998.5` | [Soft-Margin SVM](/milestones/soft-margin-svm-1998.md) | [The Support Vector Escarpment](/provinces/support-vector-escarpment.md) | Cortes & Vapnik introduce soft-margin support-vector networks |
| 4 | `1999.7` | [SIFT Keypoints](/milestones/sift-lowe-1999.md) | [The Support Vector Escarpment](/provinces/support-vector-escarpment.md) | David Lowe introduces SIFT scale-invariant features for computer vision |
| 5 | `2005.5` | [HOG Pedestrian Detector](/milestones/hog-dalal-triggs-2005.md) | [The Support Vector Escarpment](/provinces/support-vector-escarpment.md) | Dalal and Triggs combine Histograms of Oriented Gradients with linear SVMs |
| 6 | `2010.5` | [ILSVRC begins](/milestones/ilsvrc-2010.md) | [The ImageNet Escarpment](/provinces/gpu-convnet-school.md) | first ImageNet challenge: 1,000 classes; 2010–11 winners are SVM pipelines |

## Directed Road Segments

- [Learning Machines](/milestones/nilsson-learning-machines-1965.md) (`1965.2`) → [Kernel SVM](/milestones/svm-optimal-margin-1998.md) (`1998.2`)
- [Kernel SVM](/milestones/svm-optimal-margin-1998.md) (`1998.2`) → [Soft-Margin SVM](/milestones/soft-margin-svm-1998.md) (`1998.5`)
- [Soft-Margin SVM](/milestones/soft-margin-svm-1998.md) (`1998.5`) → [SIFT Keypoints](/milestones/sift-lowe-1999.md) (`1999.7`)
- [SIFT Keypoints](/milestones/sift-lowe-1999.md) (`1999.7`) → [HOG Pedestrian Detector](/milestones/hog-dalal-triggs-2005.md) (`2005.5`)
- [HOG Pedestrian Detector](/milestones/hog-dalal-triggs-2005.md) (`2005.5`) → [ILSVRC begins](/milestones/ilsvrc-2010.md) (`2010.5`)
