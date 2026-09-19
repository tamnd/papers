---
paper: yeh-1991-branchprediction
title: Two-Level Adaptive Training Branch Prediction
authors:
  - Tse-Yu Yeh
  - Yale N. Patt
year: 1991
venue: MICRO
field: architecture
section: "2"
section_title: Two-Level Adaptive Training Branch Prediction
tag: "0384"
kind: section
lang: en
source: http://classweb.ece.umd.edu/enee646/yeh+patt-adaptive-training-1991.pdf
pdf_sha256: 31a1e6a4b5f27f0523a80a4f004afe037d8e698a56335242059eb2b3868d5669
pdf_pages: 2-4
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: c9a9f91788d4cef53f30590cf91f7084e07e461898d7e1015ee1b2ba57c15779
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The Two-Level Adaptive Training Branch Prediction scheme has the following characteristics:

• Branch prediction is based on the history of branches executed during the current execution of the program.

• Execution history pattern information is collected on the fly of the program execution by updating the pattern history information in the branch history pattern table of the predictor. Therefore, no pre-runs of the program are necessary.

### 2.1 Concept of Two-Level Adaptive Training Branch Prediction {#yeh-1991-branchprediction-s2-1 .section tag=0385}

The Two-Level Adaptive Training scheme has two major data structures, the branch history register (HR) and the branch history pattern table (PT), similar to those used in the Static Training scheme of Lee and Smith [13]. In Two-Level Adaptive Training, instead of accumulating statistics by profiling the programs, the execution history information on which branch predictions are based is collected by updating the contents of the history registers and the pattern history bits in the entries of the pattern table depending on the outcomes of the branches. The history register is a shift register which shifts in bits representing the branch results of the most recent history information. All the history registers are contained in a history register table (HRT). The pattern history bits represent the most recent branch results for the particular contents of the history register. Branch predictions are made by checking the pattern history bits in the pattern table entry indexed by the content of the history register for the particular branch that is being predicted.

Since the history register table is indexed by branch instruction addresses, the history register table is called a per-address history register table (PHRT). The pattern table is called a global pattern table, because all the history registers access the same pattern table.

Figure 1: The structure of the Two-Level Adaptive Training scheme. {#yeh-1991-branchprediction-fig-1 .figure tag=0386}

The structure of Two-Level Adaptive Training Branch Prediction is shown in Figure 1. The prediction of a branch $B_i$ is based on the history pattern of the last $k$ outcomes of executing the branch; therefore, $k$ bits are needed in the history register for each branch to keep track of the history. If the branch was taken, then a "1" is recorded; if not, a "0" is recorded. Since there are $k$ bits in the history register, at most $2^k$ different patterns appear in the history register. In order to keep track of the history of the patterns, there are $2^k$ entries in the pattern table; each entry is indexed by one distinct history pattern.

When a conditional branch $B_i$ is being predicted, the contents of its history register, $HR_i$, whose content is denoted as $R_{i,c-k}R_{i,c-k+1}......R_{i,c-1}$ for the last $k$ outcomes of executing the branch, is used to address the pattern table. The pattern history bits $S_c$ in the addressed entry $PTR_{i,c-k}R_{i,c-k+1}......R_{i,c-1}$ in the pattern table are then used for predicting the branch. The prediction of the branch is

$$
z_c = \lambda(S_c),
$$

where $\lambda$ is the prediction decision function.

After the conditional branch is resolved, the outcome $R_{i,c}$ is shifted left into the history register $HR_i$ in the least significant bit position and is also used to update the pattern history bits in the pattern table entry $PTR_{i,c-k}R_{i,c-k+1}......R_{i,c-1}$. After being updated, the content of the history register becomes $R_{i,c-k+1}R_{i,c-k+2}......R_{i,c}$ and the state represented by the pattern history bits becomes $S_{c+1}$. The transition of the pattern history bits in the pattern table entry is done by the state transition function $\delta$ which takes

$$
S_{c+1} = \delta(S_c, R_{i,c})
$$

in the old pattern history bits and the outcome of the branch as inputs to generate the new pattern history bits. Therefore, the new pattern history bits $S_{c+1}$ become

$$
S_{c+1} = \delta(S_c, R_{i,c})
$$

A straightforward combinational logic circuit is used to implement the function $\delta$ to update the pattern history bits in the entries of the pattern table. The transition function $\delta$, pattern history bits $S$ and the outcome $R$ of the branch comprise a finite-state machine, which can be characterized by equations 1 and 2. Since the prediction is based on the pattern history bits, the finite-state machine is a Moore machine with the output $z$ characterized by equation 1.

The state transition diagrams of the finite-state machines used in this study for updating the pattern history in the pattern table entry are shown in the Figure 2. The automaton Last-Time stores in the pattern history bit only the outcome of the last execution of the branch when the history pattern appeared. The next time the same history pattern appears the prediction will be what happened last time. Only one bit is needed to store the pattern history information. The automaton A1 records the results of the last two times the same history pattern appeared. Only when there is no taken branch recorded, the next execution of the branch when the history register has the same history pattern will be predicted as not taken; otherwise, the branch will be predicted as taken. The automaton A2 is a saturating up-down counter, which is also used, but differently, in Lee and Smith's Branch Target Buffer design [13]. The counter is incremented when the branch is taken and is decremented when the branch is not taken. The next execution of the branch will be predicted as taken when the counter value is greater than or equal to two; otherwise, the branch will be predicted as not taken. Automata $A3$ and $A4$ are both similar to $A2$.

Both Static Training and Two-Level Adaptive Training are dynamic branch predictors, because their predictions are based on run-time information, i.e. the dynamic branch history. The major difference between these two schemes is that the pattern history information in the pattern table changes dynamically in Two-Level Adaptive Training but is preset in Static Training from profiling. In Static Training, the input to the prediction decision function, $\lambda$, for a given branch history pattern is determined before execution. Therefore, the output of $\lambda$ is determined before execution for a given branch history pattern. That is, the same branch predictions are made if the same history pattern appears at different times during execution. Two-Level Adaptive Training, on the other hand, updates the appropriate pattern history information with the actual result of each branch. As a result, given the same branch history pattern, different pattern history information can be found in the pattern table; therefore, there can be different inputs to the prediction decision function for Two-Level Adaptive Training. Predictions of Two-Level Adaptive Training change adaptively in accordance with the program execution behavior.

Since the pattern history bits change in Two-Level Adaptive Training, the predictor can adjust to the current branch execution behavior of the program to make proper predictions. With the updates, Two-Level Adaptive Training can still be highly accurate over many different programs and data sets. Static Training, on the contrary, may not predict well if changing data sets results in different execution behavior.
