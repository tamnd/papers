---
paper: yeh-1991-branchprediction
title: Two-Level Adaptive Training Branch Prediction
authors:
  - Tse-Yu Yeh
  - Yale N. Patt
year: 1991
venue: MICRO
field: architecture
section: "3"
section_title: Implementation Methods
tag: "0387"
kind: section
lang: en
source: http://classweb.ece.umd.edu/enee646/yeh+patt-adaptive-training-1991.pdf
pdf_sha256: 31a1e6a4b5f27f0523a80a4f004afe037d8e698a56335242059eb2b3868d5669
pdf_pages: 4-10
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 14141a0272616146d7ba80bed6b9aa34404e115e99267c98ad923c3c7bd66c62
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

### 3.1 Implementations of the Per-address History Register Table {#yeh-1991-branchprediction-s3-1 .section tag=0388}

It is not feasible to have a big enough history register table for each static branch to have its own history register in real implementations. Therefore, two approaches are proposed for implementing the Per-address History Register Table.

The first approach is to implement the per-address register table as a set-associative cache. A fixed number of entries in the table are grouped together as a set. Within a set, the Least-Recently-Used (LRU) algorithm is used for replacement. The lower part of a branch address is used to index into the table and the higher part is used as a tag which is recorded in the entry allocated for the branch. The per-address history register table implemented in this way is called the Associative History Register Table (AHRT). When a conditional branch is to be predicted, the branch’s entry in the AHRT is located first. If the branch has an entry in the AHRT, the contents of the corresponding history register is used to address the pattern table. If the branch does not have an entry in the AHRT, a new entry is allocated for the branch. There is an extra cost for implementing the tag store in this approach.

The second approach is to implement the history register table as a hash table. The address of a conditional branch is used for hashing into the table. The per-address history table using this approach is called the Hash History Register Table (HHRT). Since collisions can occur when accessing a hash table, this implementation results in more interference in the execution history. As one would expect, the prediction accuracy for this approach is lower than what would be obtained with an AHRT, but the cost of the tag store is saved.

In this study, the above two practical approaches and the Ideal History Register Table (IHRT), in which there is a history register for each static conditional branch, were simulated for the Two-Level Adaptive Training Branch Predictor. The AHRT was simulated with two configurations: 512-entry 4-way set-associative and 256-entry 4-way set-associative. The HHRT was also simulated with 512 entries and 256 entries. The IHRT simulation data is provided to show how much accuracy is lost due to the history interference in the practical history register table designs.

### 3.2 Prediction Latency {#yeh-1991-branchprediction-s3-2 .section tag=0389}

The Two-Level Adaptive Training Branch Predictor needs two sequential table lookups to make a prediction. It is hard to squeeze the two lookups into one cycle, which is usually the requirement for a high-performance processor in determining the next instruction address. The solution to this problem is to perform the pattern table lookup with the updated history pattern of a branch at the time the history register is updated, produce a prediction from the pattern table, and store the prediction as a prediction bit in the history register table with the history register for the branch. Therefore, the next time the branch must be predicted, the prediction is available in the history register table, and the pattern table does not have to be accessed that cycle.

Another problem occurs when the prediction of a branch is required before the result of the previous execution of the branch has been confirmed. This case appears very often when a tight loop is being executed by a deep-pipelined superscalar machine, but not usually otherwise. Since this kind of branch has a high tendency to be taken, the branch is predicted taken and the machine does not have to stall until the previous branch result is confirmed.

Figure 3: Distribution of dynamic instructions. {#yeh-1991-branchprediction-fig-3 .figure tag=038A}

Figure 4: Distribution of dynamic branch instructions. {#yeh-1991-branchprediction-fig-4 .figure tag=038B}

| Benchmark Name | Number of Static Cnd. Br. | Benchmark Name | Number of Static Cnd. Br. |
| --- | --- | --- | --- |
| eqntott | 277 | espresso | 556 |
| gcc | 6922 | li | 489 |
| doduc | 1149 | fpppp | 653 |
| matrix300 | 213 | spice2g6 | 606 |
| tomcatv | 370 |  |  |

Table 1: The number of static conditional branches in each benchmark. {#yeh-1991-branchprediction-tab-1 .table tag=038C}

ing point benchmarks and four are integer benchmarks. The floating point benchmarks include doduc, fpppp, matrix300, spice2g6 and tomcatv and the integer ones include eqntott, espresso, gcc, and li. Nasa7 is not included because it takes too long to capture the branch behavior of all seven kernels. Among the five floating point benchmarks, matrix300 and tomcatv have repetitive loop execution; thus, a very high prediction accuracy is attainable. The integer benchmarks tend to have many conditional branches and irregular branch behavior. Therefore, it is on the integer benchmarks where the mettle of the branch predictor is tested.

Since this study focuses on the prediction for conditional branches, all benchmarks except fpppp and gcc were simulated for twenty million conditional branch instructions. The benchmarks fpppp and gcc finish execution before twenty millions conditional branches are executed. The number of dynamic instructions simulated for the benchmarks range from fifty million to 1.8 billion.

The dynamic instruction distribution is shown in Figure 3. About 24 percent of the dynamic instructions for the integer benchmarks and about 5 percent of the dynamic instructions for the floating point benchmarks are branch instructions.

The distribution of the dynamic branch instructions

| Model Name | HRT Implementation |  | PT Implementation |  |
| --- | --- | --- | --- | --- |
|  | # of Entries | Entry Content | # of Entries | Entry Content |
| AT(AHRT(256,12SR), PT(2^{12},A2),) | 256 | 12-bit SR | 2^{12} | Atm A2 |
| AT(AHRT(512,12SR), PT(2^{12},A2),) | 512 | 12-bit SR | 2^{12} | Atm A2 |
| AT(AHRT(512,12SR), PT(2^{12},A3),) | 512 | 12-bit SR | 2^{12} | Atm A3 |
| AT(AHRT(512,12SR), PT(2^{12},A4),) | 512 | 12-bit SR | 2^{12} | Atm A4 |
| AT(AHRT(512,12SR), PT(2^{12},LT),) | 512 | 12-bit SR | 2^{12} | Atm LT |
| AT(AHRT(512,10SR), PT(2^{10},A2),) | 512 | 10-bit SR | 2^{10} | Atm A2 |
| AT(AHRT(512,8SR), PT(2^{8},A2),) | 512 | 8-bit SR | 2^{8} | Atm A2 |
| AT(AHRT(512,6SR), PT(2^{6},A2),) | 512 | 6-bit SR | 2^{6} | Atm A2 |
| AT(HHRT(256,12SR), PT(2^{12},A2),) | 256 | 12-bit SR | 2^{12} | Atm A2 |
| AT(HHRT(512,12SR), PT(2^{12},A2),) | 512 | 12-bit SR | 2^{12} | Atm A2 |
| AT(IHRT(.12SR), PT(2^{12},A2),) | \infty | 12-bit SR | 2^{12} | Atm A2 |
| ST(AHRT(512,12SR), PT(2^{12},PB),Same) | 512 | 12-bit SR | 2^{12} | PB |
| ST(HHRT(512,12SR), PT(2^{12},PB),Same) | 512 | 12-bit SR | 2^{12} | PB |
| ST(IHRT(.12SR), PT(2^{12},PB),Same) | \infty | 12-bit SR | 2^{12} | PB |
| ST(AHRT(512,12SR), PT(2^{12},PB),Diff) | 512 | 12-bit SR | 2^{12} | PB |
| ST(HHRT(512,12SR), PT(2^{12},PB),Diff) | 512 | 12-bit SR | 2^{12} | PB |
| ST(IHRT(.12SR), PT(2^{12},PB),Diff) | \infty | 12-bit SR | 2^{12} | PB |
| LS(AHRT(512,A2),) | 512 | Atm A2 |  |  |
| LS(AHRT(512,LT),) | 512 | Atm LT |  |  |
| LS(HHRT(512,A2),) | 512 | Atm A2 |  |  |
| LS(HHRT(512,LT),) | 512 | Atm LT |  |  |
| LS(IHRT(.A2),) | \infty | Atm A2 |  |  |
| LS(IHRT(.LT),) | \infty | Atm LT |  |  |

AT - Two-Level Adaptive Training, ST - Static Training, LS - Lee and Smith’s Branch Target Buffer Design, AHRT - Four-way Set-Associative History Register Table, HHRT - Hash History Register Table, IHRT - Ideal History Register Table, SR - Shift Register, Atm - Automaton, LT - Last-Time, PB - Preset Prediction Bit.

Table 2: Configurations of simulated branch predictors. {#yeh-1991-branchprediction-tab-2 .table tag=038D}

is shown in Figure 4. As can be seen from the distribution, about 80 percent of the dynamic branch instructions are conditional branches. The conditional branch is the branch class that should be studied to improve the prediction accuracy. The number of static conditional branches in the trace tapes of the benchmarks are listed in Table 1.

4.2 Simulation Model

Several configurations were simulated for the Two-Level Adaptive Training scheme. For the per-address history register table (PHRT), two practical implementations, the associative HRT (AHRT) and the hash HRT (HHRT), along with the ideal HRT (IHRT) were simulated. In order to distinguish the different schemes, the naming convention for the branch prediction schemes is Scheme(History(Size, Entry_Content)), Pattern(Size, Entry_Content), Data). Scheme specifies the scheme, for example, Two-Level Adaptive Training (AT), Static Training (ST), or Lee and Smith’s Branch Target Buffer design (LS). In History(Size, Entry_Content), History is the implementation for keeping history information of branches, for example, IHRT, AHRT, or HHRT. Size specifies the number of entries in the implementation, and Entry_Content specifies the content in each entry. The content of an entry in the history register table can be any automaton shown in Figure 2 or a history register. In Pattern(Size, Entry_Content), Pattern is the implementation for keeping history information for history patterns, Size specifies the number of entries in the implementation, and Entry_Content specifies the content in each entry. The content of an entry in the pattern history table can be any automaton shown in Figure 2. For Lee and Smith’s Branch Target Buffer designs, the Pattern part is not included, because there is no pattern history information kept in their designs. Data specifies how the data sets are used. When Data is specified as Same, the same data set is used for both training and testing. When Data is specified as Diff, different data sets are used for training and testing. If Data is not specified, no training data set is needed for the shemes, as in Two-Level Adaptive Training schemes or Lee and Smith’s Branch Target Buffer designs. The configuration and scheme of each simulation model in this study are listed in Table 2.

Since about 60 percent of branches are taken according to our simulation results, the contents of the history register usually should contain more 1’s than 0’s. Accordingly, all the bits in the history register of each entry in the HRT are initialized to 1’s at the beginning of program execution. During execution, when an entry is re-allocated to a different static branch, the history register is not re-initialized.

The pattern history bits in the pattern table entries are also initialized at the beginning of execution. Since taken branches are more likely, for those pattern tables using automata, A1, A2, A3, and A4, all entries are initialized to state 3. For Last-Time, all entries are initialized to state 1 such that the branches at the beginning of execution will be more likely to be predicted taken.

In addition to the Two-Level Adaptive Training schemes, Lee and Smith’s Static Training schemes and Branch Target Buffer designs, and some dynamic and static branch prediction schemes were simulated for comparison purposes. Lee and Smith’s Static Training scheme is similar to the Two-Level Adaptive Training scheme with an IHRT but with the important difference that the prediction for a given pattern is pre-determined by profiling. The two practical approaches for the HRT were also simulated for Static Training with the same accessing method introduced above.

Lee and Smith’s Branch Target Buffer designs were simulated with automata A2, A3, A4, and Last-Time. The static branch prediction schemes simulated include the Always Taken, Backward Taken and Forward Not taken, and a simple profiling scheme. The profiling scheme is done by counting the frequency of taken and not-taken for each static branch in the profiling execution. The predicted direction of a branch is the one the branch takes most frequently. Since the same data set was used for profiling and execution in this study, the prediction accuracy was calculated by taking the ratio of the sum of the larger number in the two numbers for two possible directions of every static branch over the total number of the dynamic conditional branch instructions.

5 Simulation Results

The simulation results presented in this section were run with the Two-Level Adaptive Training schemes, the Static Training Schemes, the Branch Target Buffer designs, and some static branch prediction schemes. Figures 5 through 10 show the prediction accuracy across the nine benchmarks. On the horizontal axis, the category labeled as "Tot G Mean" shows the geometric mean across all the benchmarks, "Int G Mean" shows the geometric mean across all integer benchmarks, and "FP G Mean" shows the geometric mean across all floating point benchmarks. The vertical axis shows the prediction accuracy scaled from 76 percent to 100 percent. This section concludes with a comparison between different branch prediction schemes.

5.1 Two-Level Adaptive Training

The Two-Level Adaptive Training schemes were simulated with different state transition automata, different HRT implementations, and different history register lengths to show their effects on prediction accuracy. The simulations of the Two-Level Adaptive Training scheme using an IHRT demonstrate the accuracy the scheme can achieve without history table miss effect and is used as a comparison to Lee and Smith's Static Training scheme which also uses the ideal history register table.

5.1.1 Effect of State Transition Automata

Figure 5 shows the efficiency of different state transition automata. Four state transition automata, $A2, A3, A4$, and *Last-Time* were simulated. $A1$ is not included, because early experiments indicated it was inferior to the other four-state automata, $A2, A3,$ and $A4$. The scheme using *Last-Time* performs about 1 percent worse than the ones using the other automata which achieve similar accuracy around 97 percent. The four-state finite-state machines maintain more history information than the *Last-Time* which only records what happened last time; $A2, A3,$ and $A4$ are therefore more tolerant to noise in the execution history.

Figure.

Figure 5: Two-Level Adaptive Training schemes using different state transition automata. {#yeh-1991-branchprediction-fig-5 .figure tag=038E}

Figure.

Figure 6: Two-Level Adaptive Training schemes using different history register table implementations. {#yeh-1991-branchprediction-fig-6 .figure tag=038F}

In order to show the curves clearly in the following figures, each scheme is shown with the state transition automata $A2$ which usually performs the best among the state transition automata used in this study.

5.1.2 Effect of History Register Table Implementation

Figure 6 shows the effects of the HRT implementations on the prediction accuracy of the Two-Level Adaptive Training schemes. Every scheme in the graph was simulated with the same history register length. With the equivalent history register length, the IHRT scheme performs the best, the 512-entry AHRT scheme the second, the 512-entry HHRT scheme the third, the 256-entry AHRT scheme the fourth and the 256-entry HHRT scheme the worst, in the decreasing order of the HRT hit ratio. This is due to the increasing interference in the branch history as the hit ratio decreases.

Figure 7: Two-Level Adaptive Training schemes using history registers of different lengths. {#yeh-1991-branchprediction-fig-7 .figure tag=0390}

5.1.3 Effect of History Register Length

Figure 7 shows the effect of history register length on the prediction accuracy of Two-Level Adaptive Training schemes. The Two-Level Adaptive Training schemes using four different history register lengths were simulated. The accuracy increases for about 0.5 percent by lengthening the history registers for 2 bits. According to the simulation results, increasing the history register length often improves the prediction accuracy until the accuracy asymptote is reached.

5.2 Static Training

Static Training Branch Prediction examines the history pattern of the last $n$ executions of a branch and the statistics gathered from profiling the program with a training data set to calculate the probabilities the branch will be taken or not-taken with the given history pattern to predict the branch path.

Although the accounting required to gather the the training statistics can be done in software, the Static Training scheme needs to keep track of the execution history of every static branch in the program, which requires hardware support. History registers must be used to keep track of the branch execution history of each static branch during run-time. When a branch is being predicted, its recorded history pattern is used to index the branch pattern table which contains preset branch prediction information. The preset prediction bit is then used for predicting the branch. Because the number of static branches varies from one program to another, the number of history registers required changes, which requires the hardware to offer a big enough table like IHRT to hold all the static branches in the programs. In order to consider the effects of practical implementations, in addition to the IHRT, the two practical HRT

| Benchmark Name | Training Data Set | Testing Data Set |
| --- | --- | --- |
| eqntott | NA | int_pri_3.eqn |
| espresso | cps | bca |
| gcc | cexp.i | dbxout.i |
| li | tower of hanoi | eight queens |
| doduc | tiny doducin | doducin |
| fpppp | NA | natoms |
| matrix300 | NA | NA |
| spice2g6 | short greycode.in | greycode.in |
| tomcatv | NA | NA |

Table 3: Training and testing data sets of each benchmark. {#yeh-1991-branchprediction-tab-3 .table tag=0391}

implementations used in this study were simulated with the Static Training schemes. The cost to implement Static Training is not any less expensive than for Two-Level Adaptive Training, because the history register table and pattern table required by both schemes are similar. However, the state transition logic in the pattern table is simpler for the Static Training scheme.

In order to show the effects of the training data sets, the simulation results for the schemes (with *Same* in their names) which were trained and tested on the same data set and those for the schemes (with *Diff* in their names) which were trained and tested on different data sets are both presented. All the testing data sets are the same as those used by other schemes in order for a fair comparison. In the schemes which were trained and executed on the same data set, the results are the best the Static Training schemes can achieve with that data set, because the best predictions for branches are known beforehand.

Five of nine benchmarks were trained with other applicable data sets. The other four benchmarks, eqntott, matrix300, fpppp, and tomcatv, are excluded because there are no other applicable data sets or the applicable data sets are too similar to each other. The data sets used in training and testing are shown in Table 3.

The Static Training schemes with similar configurations to the Two-Level Adaptive Training schemes in Figure 6 are shown in Figure 8. The highest prediction accuracy of the schemes using the same data set for training and execution is about 97 percent. This is achieved by the Static Training scheme using 12 bit history registers and an IHRT. The accuracy is about the same as that achieved by the Two-Level Adaptive Training scheme using 12 bit history registers and an 512-entry 4-way AHRT. However, when different data sets are used for training and execution, the prediction accuracy for *gcc* and *espresso* is about 1 percent lower respectively. The drop in the accuracy for *li* is more significant. It is about 5 percent lower. For the floating point benchmarks, the degradations are not so apparent due to the regular branch behavior of the programs. The degradations are within 0.5 percent. Since the data

Figure 8: Prediction accuracy of Static Training schemes. {#yeh-1991-branchprediction-fig-8 .figure tag=0392}

Figure 9: Prediction accuracy of Branch Target Buffer designs, BTFN, Always Taken, and the Profiling scheme. {#yeh-1991-branchprediction-fig-9 .figure tag=0393}

for the Static Training Schemes using different data sets for training and testing is not complete, the average accuracy for the schemes is not graphed.

5.3 Other Schemes

Figure 9 shows the simulation results of Lee and Smith’s Branch Target Buffer designs, Backward Taken and Forward Not taken (BTFN), Always Taken, and the profiling scheme. The Branch Target Buffer designs were simulated with automata, $A1$, $A2$, $A3$, $A4$, and *Last-Time*. Only the results of the designs using $A2$ and *Last-Time* are shown in the figure, because the results of the designs using $A3$ and $A4$ are similar to those of the designs using $A2$. The designs using $A1$ predict about 2 to 3 percent lower than those using $A2$. Three buffer configurations, similar to IHRT, AHRT, and HHRT, were simulated. Using an IHRT in those schemes sets the upper bound at 93 percent for the same schemes with practical HRT implementations. Using *Last-Time* is about 4 percent lower than using *A2*.

BTFN and Always Taken predict poorly compared to the other schemes. Some of the data points fall below 76 percent.

The Backward Taken and Forward Not taken scheme (BTFN) is effective for the loop-bound benchmarks like matrix300 and tomcatv but not for other benchmarks. For the loop-bound benchmarks, the prediction accuracy is as high as 98 percent. However, for the other benchmarks, its accuracy is often lower than 70 percent. The average accuracy is approximate 69 percent.

The accuracy of the Always Taken scheme changes quite markedly from one benchmark to another. Its average is about 60 percent.

The simple profiling scheme simulated here is to run the program once to accumulate the statistics of how many times the branch is taken and how many times the branch is not taken for each branch. The prediction bit in the opcode of the branch is set or cleared depending on whether the taken branch count is larger than the not-taken branch count or not. The run-time prediction of the branch is made according to the prediction bit. The average of this scheme is about 92.5 percent. This scheme is fairly simple but at the cost of profiling and low prediction accuracy.

Figure 10: Comparison of branch prediction schemes {#yeh-1991-branchprediction-fig-10 .figure tag=0394}

bound at 93 percent for the same schemes with practical HRT implementations. Using *Last-Time* is about 4 percent lower than using *A2*.

BTFN and Always Taken predict poorly compared to the other schemes. Some of the data points fall below 76 percent.

The Backward Taken and Forward Not taken scheme (BTFN) is effective for the loop-bound benchmarks like matrix300 and tomcatv but not for other benchmarks. For the loop-bound benchmarks, the prediction accuracy is as high as 98 percent. However, for the other benchmarks, its accuracy is often lower than 70 percent. The average accuracy is approximate 69 percent.

The accuracy of the Always Taken scheme changes quite markedly from one benchmark to another. Its average is about 60 percent.

The simple profiling scheme simulated here is to run the program once to accumulate the statistics of how many times the branch is taken and how many times the branch is not taken for each branch. The prediction bit in the opcode of the branch is set or cleared depending on whether the taken branch count is larger than the not-taken branch count or not. The run-time prediction of the branch is made according to the prediction bit. The average of this scheme is about 92.5 percent. This scheme is fairly simple but at the cost of profiling and low prediction accuracy.

5.4 Comparison of Schemes

Figure 10 illustrates the comparison between the schemes mentioned above. The 512-entry 4-way AHRT was chosen for all the uses of HRT, because it is simple enough to be implemented. Two-Level Adaptive and Static training schemes are chosen on the basis of similar costs. At the top is the Two-Level Adaptive Training scheme whose average prediction accuracy is about 97 percent. As can be seen from the graph, the

Static Training scheme predicts about 1 to 5 percent lower than the top curve. The profiling scheme predicts almost as well as Lee and Smith’s Branch Target Buffer design with accuracy around 92.5 percent. The scheme which predicts a branch with the last result of the execution of the branch achieves about 89 percent accuracy.

6 Concluding Remarks

This paper proposes a new branch predictor, Two-Level Adaptive Training. The scheme predicts a branch by examining the history of the last $n$ branches and the branch behavior for the last $s$ occurrences of that unique pattern of the last $n$ branches.

The Two-Level Adaptive Training schemes were simulated with three HRT configurations: the IHRT which is an ideal history register table large enough to hold all static branches, the AHRT which is a set-associative cache, and the HHRT which is a hash table. The IHRT data was included to obtain upper bounds for each of the other schemes. A scheme using an AHRT usually has higher prediction accuracy than the same scheme using an HHRT of the same size, because the AHRT has lower miss rate than the HHRT.

Each Two-Level Adaptive Training scheme was simulated with various history register lengths. As seen from the simulation results, prediction accuracy is usually improved by lengthening the history register.

In addition to the Two-Level Adaptive Training scheme, several other dynamic or static branch prediction schemes such as Lee and Smith’s Static Training schemes, Branch Target Buffer designs, Always Taken, Backward Taken and Forward Not taken, and a simple profiling scheme were simulated.

The Two-Level Adaptive Training scheme has been shown to have an average prediction accuracy of 97 percent on nine benchmarks from the SPEC benchmark suite. The prediction accuracy is about 4 percent better than most of the other static or dynamic branch prediction schemes, which means more than a 100 percent reduction in the number of pipeline flushes required. Since a prediction miss causes flushing of the speculative execution already in progress, the performance improvement on a high-performance processor can be considerable by using the Two-Level Adaptive Training scheme.

Deep-pipelining and superscalar execution are effective methods for exploiting instruction level parallelism to improve single processor performance. This effectiveness, however, depends critically on the accuracy of a good branch predictor. Two-Level Adaptive Training Branch Prediction is proposed as a way to support high performance processors by minimizing the penalty associated with mispredicted branches.
