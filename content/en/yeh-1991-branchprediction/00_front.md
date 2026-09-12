---
paper: yeh-1991-branchprediction
title: Two-Level Adaptive Training Branch Prediction
authors:
  - Tse-Yu Yeh
  - Yale N. Patt
year: 1991
venue: MICRO
field: architecture
section_title: Front Matter
tag: 005D
kind: front
lang: en
source: http://classweb.ece.umd.edu/enee646/yeh+patt-adaptive-training-1991.pdf
pdf_sha256: 31a1e6a4b5f27f0523a80a4f004afe037d8e698a56335242059eb2b3868d5669
pdf_pages: 2-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 77f01ba23f7fb2676aa3ab71579793567f744938bfe7faf7f122b68de788ffbc
prompt_sha256: 329630a0b9175a55e4af1b8e281a3e67eeab250f8d643953b7dcde99743c7628
---

There is serious performance degradation in deep-pipelined and/or superscalar machines caused by prediction misses due to the large amount of speculative work that has to be discarded [1, 8]. This is the motivation for proposing a new, higher-accuracy dynamic branch prediction scheme. The new scheme uses two levels of branch history information to make predictions. The first level is the history of the last $n$ branches. The second is the branch behavior for the last $s$ occurrences of that unique pattern of the last $n$ branches. The history information is collected on the fly without executing the program beforehand, eliminating the major disadvantage of Static Training Prediction. The scheme proposed here is called Two-Level Adaptive Training Branch Prediction, because predictions are based not only on the record of the last $n$ branches, but moreover on the record of the last $s$ occurrences of the particular record of the last $n$ branches.

Trace-driven simulations were used in this study. The Two-Level Adaptive Training branch prediction scheme as well as the other dynamic and static branch prediction schemes were simulated on the SPEC benchmark suite. By using Two-Level Adaptive Training Branch Prediction, the average prediction accuracy for the benchmarks reaches 97 percent, while most of the other schemes achieve under 93 percent. This represents more than 100 percent reduction in mispredictions by using the Two-Level Adaptive Training scheme. This reduction can lead directly to a large performance gain on a high-performance processor.
