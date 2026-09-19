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
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 1da855ad067eb809edce1ab44b5569ce547b5e4e3921ba65bf37977ae3d8c9f4
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Two-Level Adaptive Training Branch Prediction

Tse-Yu Yeh and Yale N. Patt
Department of Electrical Engineering and Computer Science
The University of Michigan
Ann Arbor, Michigan 48109-2122

Abstract

High-performance microarchitectures use, among other structures, deep pipelines to help speed up execution. The importance of a good branch predictor to the effectiveness of a deep pipeline in the presence of conditional branches is well-known. In fact, the literature contains proposals for a number of branch prediction schemes. Some are static in that they use opcode information and profiling statistics to make predictions. Others are dynamic in that they use run-time execution history to make predictions.

This paper proposes a new dynamic branch predictor, the Two-Level Adaptive Training scheme, which alters the branch prediction algorithm on the basis of information collected at run-time.

Several configurations of the Two-Level Adaptive Training Branch Predictor are introduced, simulated, and compared to simulations of other known static and dynamic branch prediction schemes. Two-Level Adaptive Training Branch Prediction achieves 97 percent accuracy on nine of the ten SPEC benchmarks, compared to less than 93 percent for other schemes. Since a prediction miss requires flushing of the speculative execution already in progress, the relevant metric is the miss rate. The miss rate is 3 percent for the Two-Level Adaptive Training scheme vs. 7 percent (best case) for the other schemes. This represents more than a 100 percent improvement in reducing the number of pipeline flushes required.

Permission to copy without fee all or part of this material is granted provided that the copies are not made or distributed for direct commercial advantage, the ACM copyright notice and the title of the publication and its date appear, and notice is given that copying is by permission of the Association for Computing Machinery. To copy otherwise, or to republish, requires a fee and/or specific permission.

© 1991 ACM 0-89791-460-0/91/0011/0051 \$1.50
