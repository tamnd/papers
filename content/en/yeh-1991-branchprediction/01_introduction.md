---
paper: yeh-1991-branchprediction
title: Two-Level Adaptive Training Branch Prediction
authors:
  - Tse-Yu Yeh
  - Yale N. Patt
year: 1991
venue: MICRO
field: architecture
section: "1"
section_title: Introduction
tag: "0383"
kind: section
lang: en
source: http://classweb.ece.umd.edu/enee646/yeh+patt-adaptive-training-1991.pdf
pdf_sha256: 31a1e6a4b5f27f0523a80a4f004afe037d8e698a56335242059eb2b3868d5669
pdf_pages: 1-2
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: f2aa2cb6bfd3173c6846716ffe03dacb2a1e10e6af645e92e8875c445903688d
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Pipelining, at least as early as [18] and continuing to the present time [6], has been one of the most effective ways to improve performance on a single processor. On the other hand, branches impede machine performance due to pipeline stalls for unresolved branches. As pipelines get deeper or issuing bandwidth becomes greater, the negative effect of branches on performance increases.

Among different types of branches, conditional branches have to wait for the condition to be resolved and the target address to be calculated before the target instruction can be fetched. Unconditional branches have to wait for the target address to be calculated. In conventional computers, instruction issuing stalls until the target address is determined, resulting in pipeline bubbles. When the number of cycles taken to resolve a branch is large, the performance loss due to the pipeline stalls is considerable. There are two ways to reduce the loss: the first is to resolve the branch as early as possible to reduce the instruction fetch pipeline bubbles. The second is to provide fast fetching and decoding of the target instruction to reduce the execution pipeline bubbles. Branch prediction is a way to reduce the execution penalty due to branches by predicting, prefetching and initiating execution of the branch target before the branch is resolved.

Branch prediction schemes can be classified into static schemes and dynamic schemes depending on the information used to make predictions. Static branch prediction schemes can be as simple as predicting that all branches are not taken or predicting that all branches are taken. Predicting that all branches are taken can achieve approximately 68 percent prediction accuracy as reported by Lee and Smith [13]. In the dynamic instructions of the benchmarks used in this study, about 60 percent of conditional branches are taken. Static predictions can also be based on the opcode. Certain classes of branch instructions tend to branch more in one direction than the other. The branch direction can also be taken into consideration such as the Backward Taken and Forward Not Taken scheme [16] which is fairly effective in loop-bound programs, because it misses only once over all iterations of a loop. However, this scheme does not work well on programs with irregular branches. Profiling [12, 5] can also be used to predict the branch path by measuring the tendencies of the branches and presetting a static prediction bit in the opcode. However, program profiling has to be performed in advance with certain sample data sets which may have different branch tendencies than the data sets that occur at run-time.

Dynamic branch prediction takes advantage of the knowledge of branches’ run-time behavior to make predictions. Lee and Smith proposed a structure they called a Branch Target Buffer [13] which uses 2-bit saturating up-down counters to collect history information which is then used to make predictions. The execution history dynamically changes the state of the branch’s entry in the buffer. In their scheme, branch prediction is based on the state of the entry. The Branch Target Buffer design can also be simplified to record only the result of the last execution of the branch. Another dynamic scheme also proposed by Lee and Smith is the Static Training scheme [13] which uses the statistics collected from a pre-run of the program and a history pattern consisting of the last $n$ run-time execution results of the branch to make a prediction. The major disadvantage of the Static Training scheme is that the program has to be run first to accumulate the statistics and the same statistics may not be applicable to different data sets.

There is serious performance degradation in deep-pipelined and/or superscalar machines caused by prediction misses due to the large amount of speculative work that has to be discarded [1, 8]. This is the motivation for proposing a new, higher-accuracy dynamic branch prediction scheme. The new scheme uses two levels of branch history information to make predictions. The first level is the history of the last $n$ branches. The second is the branch behavior for the last $s$ occurrences of that unique pattern of the last $n$ branches. The history information is collected on the fly without executing the program beforehand, eliminating the major disadvantage of Static Training Prediction. The scheme proposed here is called Two-Level Adaptive Training Branch Prediction, because predictions are based not only on the record of the last $n$ branches, but moreover on the record of the last $s$ occurrences of the particular record of the last $n$ branches.

Trace-driven simulations were used in this study. The Two-Level Adaptive Training branch prediction scheme as well as the other dynamic and static branch prediction schemes were simulated on the SPEC benchmark suite. By using Two-Level Adaptive Training Branch Prediction, the average prediction accuracy for the benchmarks reaches 97 percent, while most of the other schemes achieve under 93 percent. This represents more than 100 percent reduction in mispredictions by using the Two-Level Adaptive Training scheme. This reduction can lead directly to a large performance gain on a high-performance processor.

Section two gives an introduction to the proposed Two-Level Adaptive Training Branch Prediction scheme. Section three discusses the methodology used in this study and the simulated prediction models. Section four reports the simulation results of a wide selection of schemes including both the dynamic and the static branch predictors. Section five contains some concluding remarks.
