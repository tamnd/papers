---
paper: hochreiter-1997-lstm
title: Long Short-Term Memory
authors:
  - Sepp Hochreiter
  - Jurgen Schmidhuber
year: 1997
venue: Neural Computation
field: ai-ml
section: "5"
section_title: EXPERIMENTS
tag: "0889"
kind: section
lang: en
source: doi:10.1162/neco.1997.9.8.1735
pdf_sha256: ceb9e53dbc0493f5b3bf5520ed940f3e6b526064d17b2118d77e51f79c0edcc6
pdf_pages: 9-22
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: dc40bb8d4fa860186621207d12addf44553580a87a257e42325064d03dc8b451
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Introduction. Which tasks are appropriate to demonstrate the quality of a novel long time lag algorithm? First of all, minimal time lags between relevant input signals and corresponding teacher signals must be long for *all* training sequences. In fact, many previous recurrent net algorithms sometimes manage to generalize from very short training sequences to very long test sequences. See, e.g., Pollack (1991). But a real long time lag problem does not have *any* short time lag exemplars in the training set. For instance, Elman’s training procedure, BPTT, offline RTRL, online RTRL, etc., fail miserably on real long time lag problems. See, e.g., Hochreiter (1991) and Mozer (1992). A second important requirement is that the tasks should be complex enough such that they cannot be solved quickly by simple-minded strategies such as random weight guessing.

**Guessing can outperform many long time lag algorithms.** Recently we discovered (Schmidhuber and Hochreiter 1996, Hochreiter and Schmidhuber 1996, 1997) that many long time lag tasks used in previous work can be solved more quickly by simple random weight guessing than by the proposed algorithms. For instance, guessing solved a variant of Bengio and Frasconi’s “parity problem” (1994) problem much faster$^4$ than the seven methods tested by Bengio et al. (1994) and Bengio and Frasconi (1994). Similarly for some of Miller and Giles’ problems (1993). Of course, this does not mean that guessing is a good algorithm. It just means that some previously used problems are not extremely appropriate to demonstrate the quality of previously proposed algorithms.

**What’s common to Experiments 1–6.** All our experiments (except for Experiment 1) involve long minimal time lags — there are no short time lag training exemplars facilitating learning. Solutions to most of our tasks are sparse in weight space. They require either many parameters/inputs or high weight precision, such that random weight guessing becomes infeasible.

We always use on-line learning (as opposed to batch learning), and logistic sigmoids as activation functions. For Experiments 1 and 2, initial weights are chosen in the range $[-0.2, 0.2]$, for the other experiments in $[-0.1, 0.1]$. Training sequences are generated randomly according to the various task descriptions. In slight deviation from the notation in Appendix A1, each discrete time step of each input sequence involves three processing steps: (1) use current input to set the input units. (2) Compute activations of hidden units (including input gates, output gates, memory cells). (3) Compute output unit activations. Except for Experiments 1, 2a, and 2b, sequence elements are randomly generated on-line, and error signals are generated only at sequence ends. Net activations are reset after each processed input sequence.

For comparisons with recurrent nets taught by gradient descent, we give results only for RTRL, except for comparison 2a, which also includes BPTT. Note, however, that untruncated BPTT (see, e.g., Williams and Peng 1990) computes exactly the same gradient as offline RTRL. With long time lag problems, offline RTRL (or BPTT) and the online version of RTRL (no activation resets, online weight changes) lead to almost identical, negative results (as confirmed by additional simulations in Hochreiter 1991; see also Mozer 1992). This is because offline RTRL, online RTRL, and full BPTT all suffer badly from exponential error decay.

Our LSTM architectures are selected quite arbitrarily. If nothing is known about the complexity of a given problem, a more systematic approach would be: start with a very small net consisting of one memory cell. If this does not work, try two cells, etc. Alternatively, use sequential network construction (e.g., Fahlman 1991).

**Outline of experiments.**

• Experiment 1 focuses on a standard benchmark test for recurrent nets: the embedded Reber grammar. Since it allows for training sequences with short time lags, it is *not* a long time lag problem. We include it because (1) it provides a nice example where LSTM’s output gates are truly beneficial, and (2) it is a popular benchmark for recurrent nets that has been used by many authors — we want to include at least one experiment where conventional BPTT and RTRL do not fail completely (LSTM, however, clearly outperforms them). The embedded Reber grammar’s minimal time lags represent a border case in the sense that it is still possible to learn to bridge them with conventional algorithms. Only slightly longer

\footnotetext{4It should be mentioned, however, that different input representations and different types of noise may lead to worse guessing performance (Yoshua Bengio, personal communication, 1996).}

minimal time lags would make this almost impossible. The more interesting tasks in our paper, however, are those that RTRL, BPTT, etc. cannot solve at all.

• Experiment 2 focuses on noise-free and noisy sequences involving numerous input symbols distracting from the few important ones. The most difficult task (Task 2c) involves hundreds of distractor symbols at random positions, and minimal time lags of 1000 steps. LSTM solves it, while BPTT and RTRL already fail in case of 10-step minimal time lags (see also, e.g., Hochreiter 1991 and Mozer 1992). For this reason RTRL and BPTT are omitted in the remaining, more complex experiments, all of which involve much longer time lags.

• Experiment 3 addresses long time lag problems with noise and signal on the same input line. Experiments 3a/3b focus on Bengio et al.’s 1994 “2-sequence problem”. Because this problem actually can be solved quickly by random weight guessing, we also include a far more difficult 2-sequence problem (3c) which requires to learn real-valued, conditional expectations of noisy targets, given the inputs.

• Experiments 4 and 5 involve distributed, continuous-valued input representations and require learning to store precise, real values for very long time periods. Relevant input signals can occur at quite different positions in input sequences. Again minimal time lags involve hundreds of steps. Similar tasks never have been solved by other recurrent net algorithms.

• Experiment 6 involves tasks of a different complex type that also has not been solved by other recurrent net algorithms. Again, relevant input signals can occur at quite different positions in input sequences. The experiment shows that LSTM can extract information conveyed by the temporal order of widely separated inputs.

Subsection 5.7 will provide a detailed summary of experimental conditions in two tables for reference.

### 5.1 EXPERIMENT 1: EMBEDDED REBER GRAMMAR {#hochreiter-1997-lstm-s5-1 .section tag=088A}

Task. Our first task is to learn the “embedded Reber grammar”, e.g. Smith and Zipser (1989), Cleeremans et al. (1989), and Fahlman (1991). Since it allows for training sequences with short time lags (of as few as 9 steps), it is *not* a long time lag problem. We include it for two reasons: (1) it is a popular recurrent net benchmark used by many authors — we wanted to have at least one experiment where RTRL and BPTT do not fail completely, and (2) it shows nicely how output gates can be beneficial.

Figure.

Figure 3: *Transition diagram for the Reber grammar.* {#hochreiter-1997-lstm-fig-3 .figure tag=088B}

Starting at the leftmost node of the directed graph in Figure 4, symbol strings are generated sequentially (beginning with the empty string) by following edges — and appending the associated

Figure.

Figure 4: *Transition diagram for the embedded Reber grammar. Each box represents a copy of the Reber grammar (see Figure 3).* {#hochreiter-1997-lstm-fig-4 .figure tag=088C}

symbols to the current string — until the rightmost node is reached. Edges are chosen randomly if there is a choice (probability: 0.5). The net’s task is to read strings, one symbol at a time, and to permanently predict the next symbol (error signals occur at every time step). To correctly predict the symbol before last, the net has to remember the second symbol.

Comparison. We compare LSTM to “Elman nets trained by Elman’s training procedure” (ELM) (results taken from Cleeremans et al. 1989), Fahlman’s “Recurrent Cascade-Correlation” (RCC) (results taken from Fahlman 1991), and RTRL (results taken from Smith and Zipser (1989), where only the few successful trials are listed). It should be mentioned that Smith and Zipser actually make the task easier by increasing the probability of short time lag exemplars. We didn’t do this for LSTM.

Training/Testing. We use a local input/output representation (7 input units, 7 output units). Following Fahlman, we use 256 training strings and 256 separate test strings. The training set is generated randomly; training exemplars are picked randomly from the training set. Test sequences are generated randomly, too, but sequences already used in the training set are not used for testing. After string presentation, all activations are reinitialized with zeros. A trial is considered successful if all string symbols of all sequences in both test set and training set are predicted correctly — that is, if the output unit(s) corresponding to the possible next symbol(s) is(are) always the most active ones.

Architectures. Architectures for RTRL, ELM, RCC are reported in the references listed above. For LSTM, we use 3 (4) memory cell blocks. Each block has 2 (1) memory cells. The output layer’s only incoming connections originate at memory cells. Each memory cell and each gate unit receives incoming connections from all memory cells and gate units (the hidden layer is fully connected — less connectivity may work as well). The input layer has forward connections to all units in the hidden layer. The gate units are biased. These architecture parameters make it easy to store at least 3 input signals (architectures 3-2 and 4-1 are employed to obtain comparable numbers of weights for both architectures: 264 for 4-1 and 276 for 3-2). Other parameters may be appropriate as well, however. All sigmoid functions are logistic with output range [0, 1], except for $h$, whose range is $[ -1, 1 ]$, and $g$, whose range is $[ -2, 2 ]$. All weights are initialized in $[ -0.2, 0.2 ]$, except for the output gate biases, which are initialized to -1, -2, and -3, respectively (see abuse problem, solution (2) of Section 4). We tried learning rates of 0.1, 0.2 and 0.5.

Results. We use 3 different, randomly generated pairs of training and test sets. With each such pair we run 10 trials with different initial weights. See Table 1 for results (mean of 30 trials). Unlike the other methods, LSTM always learns to solve the task. Even when we ignore the unsuccessful trials of the other approaches, LSTM learns much faster.

Importance of output gates. The experiment provides a nice example where the output gate is truly beneficial. Learning to store the first T or P should not perturb activations representing the more easily learnable transitions of the original Reber grammar. This is the job of the output gates. Without output gates, we did not achieve fast learning.

### 5.2 EXPERIMENT 2: NOISE-FREE AND NOISY SEQUENCES {#hochreiter-1997-lstm-s5-2 .section tag=088D}

Task 2a: noise-free sequences with long time lags. There are $p + 1$ possible input symbols denoted $a_1, ..., a_{p-1}, a_p = x, a_{p+1} = y$. $a_i$ is “locally” represented by the $p + 1$-dimensional vector whose $i$-th component is 1 (all other components are 0). A net with $p + 1$ input units and $p + 1$ output units sequentially observes input symbol sequences, one at a time, permanently trying to predict the next symbol — error signals occur at every single time step. To emphasize the “long time lag problem”, we use a training set consisting of only two very similar sequences: $(y, a_1, a_2, ..., a_{p-1}, y)$ and $(x, a_1, a_2, ..., a_{p-1}, x)$. Each is selected with probability 0.5. To predict the final element, the net has to learn to store a representation of the first element for $p$ time steps.

We compare “Real-Time Recurrent Learning” for fully recurrent nets (RTRL), “Back-Propagation Through Time” (BPTT), the sometimes very successful 2-net “Neural Sequence Chunker” (CH, Schmidhuber 1992b), and our new method (LSTM). In all cases, weights are initialized in [-0.2,0.2]. Due to limited computation time, training is stopped after 5 million sequence presen-

| method | hidden units | # weights | learning rate | % of success | success after |
| --- | --- | --- | --- | --- | --- |
| RTRL | 3 | ≈ 170 | 0.05 | “some fraction” | 173,000 |
| RTRL | 12 | ≈ 494 | 0.1 | “some fraction” | 25,000 |
| ELM | 15 | ≈ 435 |  | 0 | &gt;200,000 |
| RCC | 7-9 | ≈ 119-198 |  | 50 | 182,000 |
| LSTM | 4 blocks, size 1 | 264 | 0.1 | 100 | 39,740 |
| LSTM | 3 blocks, size 2 | 276 | 0.1 | 100 | 21,730 |
| LSTM | 3 blocks, size 2 | 276 | 0.2 | 97 | 14,060 |
| LSTM | 4 blocks, size 1 | 264 | 0.5 | 97 | 9,500 |
| LSTM | 3 blocks, size 2 | 276 | 0.5 | 100 | 8,440 |

Table 1: *EXPERIMENT 1: Embedded Reber grammar: percentage of successful trials and number of sequence presentations until success for RTRL (results taken from Smith and Zipser 1989), “Elman net trained by Elman’s procedure” (results taken from Cleeremans et al. 1989), “Recurrent Cascade-Correlation” (results taken from Fahlman 1991) and our new approach (LSTM). Weight numbers in the first 4 rows are estimates — the corresponding papers do not provide all the technical details. Only LSTM almost always learns to solve the task (only two failures out of 150 trials). Even when we ignore the unsuccessful trials of the other approaches, LSTM learns much faster (the number of required training examples in the bottom row varies between 3,800 and 24,100).* {#hochreiter-1997-lstm-tab-1 .table tag=088E}

tations. A successful run is one that fulfills the following criterion: after training, during 10,000 successive, randomly chosen input sequences, the maximal absolute error of all output units is always below 0.25.

Architectures. RTRL: one self-recurrent hidden unit, $p+1$ non-recurrent output units. Each layer has connections from all layers below. All units use the logistic activation function sigmoid in [0,1].

BPTT: same architecture as the one trained by RTRL.

CH: both net architectures like RTRL’s, but one has an additional output for predicting the hidden unit of the other one (see Schmidhuber 1992b for details).

LSTM: like with RTRL, but the hidden unit is replaced by a memory cell and an input gate (no output gate required). $g$ is the logistic sigmoid, and $h$ is the identity function $h : h(x) = x, \forall x$. Memory cell and input gate are added once the error has stopped decreasing (see abuse problem: solution (1) in Section 4).

Results. Using RTRL and a short 4 time step delay ($p = 4$), $\frac{7}{9}$ of all trials were successful. *No trial was successful with $p = 10$*. With *long* time lags, only the neural sequence chunker and LSTM achieved successful trials, while BPTT and RTRL failed. With $p = 100$, the 2-net sequence chunker solved the task in only $\frac{1}{3}$ of all trials. LSTM, however, always learned to solve the task. Comparing successful trials only, LSTM learned much faster. See Table 2 for details. It should be mentioned, however, that a *hierarchical* chunker can also always quickly solve this task (Schmidhuber 1992c, 1993).

**Task 2b: no local regularities.** With the task above, the chunker sometimes learns to correctly predict the final element, but only because of predictable local regularities in the input stream that allow for compressing the sequence. In an additional, more difficult task (involving many more different possible sequences), we remove compressibility by replacing the deterministic subsequence $(a_1, a_2, \ldots, a_{p-1})$ by a *random* subsequence (of length $p-1$) over the alphabet $a_1, a_2, \ldots, a_{p-1}$. We obtain 2 classes (two sets of sequences) $\{(y, a_{i_1}, a_{i_2}, \ldots, a_{i_{p-1}}, y) \mid 1 \leq i_1, i_2, \ldots, i_{p-1} \leq p-1\}$ and $\{(x, a_{i_1}, a_{i_2}, \ldots, a_{i_{p-1}}, x) \mid 1 \leq i_1, i_2, \ldots, i_{p-1} \leq p-1\}$. Again, every next sequence element has to be predicted. The only totally predictable targets, however, are $x$ and $y$, which occur at sequence ends. Training exemplars are chosen randomly from the 2 classes. Architectures and parameters are the same as in Experiment 2a. A successful run is one that fulfills the following criterion: after training, during 10,000 successive, randomly chosen input

| Method | Delay $p$ | Learning rate | # weights | % Successful trials | Success after |
| --- | --- | --- | --- | --- | --- |
| RTRL | 4 | 1.0 | 36 | 78 | 1,043,000 |
| RTRL | 4 | 4.0 | 36 | 56 | 892,000 |
| RTRL | 4 | 10.0 | 36 | 22 | 254,000 |
| RTRL | 10 | 1.0-10.0 | 144 | 0 | &gt; 5,000,000 |
| RTRL | 100 | 1.0-10.0 | 10404 | 0 | &gt; 5,000,000 |
| BPTT | 100 | 1.0-10.0 | 10404 | 0 | &gt; 5,000,000 |
| CH | 100 | 1.0 | 10506 | 33 | 32,400 |
| LSTM | 100 | 1.0 | 10504 | 100 | 5,040 |

Table 2: *Task 2a: Percentage of successful trials and number of training sequences until success, for “Real-Time Recurrent Learning” (RTRL), “Back-Propagation Through Time” (BPTT), neural sequence chunking (CH), and the new method (LSTM). Table entries refer to means of 18 trials. With 100 time step delays, only CH and LSTM achieve successful trials. Even when we ignore the unsuccessful trials of the other approaches, LSTM learns much faster.* {#hochreiter-1997-lstm-tab-2 .table tag=088F}

sequences, the maximal absolute error of all output units is below 0.25 at sequence end.

Results. As expected, the chunker failed to solve this task (so did BPTT and RTRL, of course). LSTM, however, was always successful. On average (mean of 18 trials), success for $p = 100$ was achieved after 5,680 sequence presentations. This demonstrates that LSTM does not require sequence regularities to work well.

**Task 2c:** very long time lags — no local regularities. This is the most difficult task in this subsection. To our knowledge no other recurrent net algorithm can solve it. Now there are $p+4$ possible input symbols denoted $a_1, ..., a_{p-1}, a_p, a_{p+1} = e, a_{p+2} = b, a_{p+3} = x, a_{p+4} = y$. $a_1, ..., a_p$ are also called *“distractor symbols”*. Again, $a_i$ is locally represented by the $p+4$-dimensional vector whose $i$th component is 1 (all other components are 0). A net with $p+4$ input units and 2 output units sequentially observes input symbol sequences, one at a time. Training sequences are randomly chosen from the union of two very similar subsets of sequences: $\{(b, y, a_{i_1}, a_{i_2}, ..., a_{i_{q+k}}, e, y) \mid 1 \leq i_1, i_2, ..., i_{q+k} \leq q\}$ and $\{(b, x, a_{i_1}, a_{i_2}, ..., a_{i_{q+k}}, e, x) \mid 1 \leq i_1, i_2, ..., i_{q+k} \leq q\}$. To produce a training sequence, we (1) randomly generate a sequence prefix of length $q + 2$, (2) randomly generate a sequence suffix of additional elements ($\neq b, e, x, y$) with probability $\frac{9}{10}$ or, alternatively, an $e$ with probability $\frac{1}{10}$. In the latter case, we (3) conclude the sequence with $x$ or $y$, depending on the second element. For a given $k$, this leads to a uniform distribution on the possible sequences with length $q + k + 4$. The minimal sequence length is $q + 4$; the expected length is

$$
4 + \sum_{k=0}^{\infty} \frac{1}{10} \left( \frac{9}{10} \right)^k (q + k) = q + 14.
$$

The expected number of occurrences of element $a_i, 1 \leq i \leq p$, in a sequence is $\frac{q+10}{p} \approx \frac{q}{p}$. The goal is to predict the last symbol, which always occurs after the “trigger symbol” $e$. Error signals are generated only at sequence ends. To predict the final element, the net has to learn to store a representation of the second element for at least $q + 1$ time steps (until it sees the trigger symbol $e$). Success is defined as “prediction error (for final sequence element) of both output units always below 0.2, for 10,000 successive, randomly chosen input sequences”.

**Architecture/Learning.** The net has $p + 4$ input units and 2 output units. Weights are initialized in [-0.2,0.2]. To avoid too much learning time variance due to different weight initializations, the hidden layer gets two memory cells (two cell blocks of size 1 — although one would be sufficient). There are no other hidden units. The output layer receives connections only from memory cells. Memory cells and gate units receive connections from input units, memory cells and gate units (i.e., the hidden layer is fully connected). No bias weights are used. $h$ and $g$ are logistic sigmoids with output ranges $[−1, 1]$ and $[−2, 2]$, respectively. The learning rate is 0.01.

| $q$ (time lag −1) | $p$ (# random inputs) | $\frac{q}{p}$ | # weights | Success after |
| --- | --- | --- | --- | --- |
| 50 | 50 | 1 | 364 | 30,000 |
| 100 | 100 | 1 | 664 | 31,000 |
| 200 | 200 | 1 | 1264 | 33,000 |
| 500 | 500 | 1 | 3064 | 38,000 |
| 1,000 | 1,000 | 1 | 6064 | 49,000 |
| 1,000 | 500 | 2 | 3064 | 49,000 |
| 1,000 | 200 | 5 | 1264 | 75,000 |
| 1,000 | 100 | 10 | 664 | 135,000 |
| 1,000 | 50 | 20 | 364 | 203,000 |

Table 3: Task 2c: LSTM with very long minimal time lags $q + 1$ and a lot of noise. $p$ is the number of available distractor symbols ($p + 4$ is the number of input units). $\frac{q}{p}$ is the expected number of occurrences of a given distractor symbol in a sequence. The rightmost column lists the number of training sequences required by LSTM (BPTT, RTRL and the other competitors have no chance of solving this task). If we let the number of distractor symbols (and weights) increase in proportion to the time lag, learning time increases very slowly. The lower block illustrates the expected slow-down due to increased frequency of distractor symbols. {#hochreiter-1997-lstm-tab-3 .table tag=0890}

Note that the minimal time lag is $q + 1$ — the net never sees short training sequences facilitating the classification of long test sequences.

Results. 20 trials were made for all tested pairs $(p, q)$. Table 3 lists the mean of the number of training sequences required by LSTM to achieve success (BPTT and RTRL have no chance of solving non-trivial tasks with minimal time lags of 1000 steps).

Scaling. Table 3 shows that if we let the number of input symbols (and weights) increase in proportion to the time lag, learning time increases very slowly. This is a another remarkable property of LSTM not shared by any other method we are aware of. Indeed, RTRL and BPTT are far from scaling reasonably — instead, they appear to scale exponentially, and appear quite useless when the time lags exceed as few as 10 steps.

Distractor influence. In Table 3, the column headed by $\frac{q}{p}$ gives the expected frequency of distractor symbols. Increasing this frequency decreases learning speed, an effect due to weight oscillations caused by frequently observed input symbols.

### 5.3 EXPERIMENT 3: NOISE AND SIGNAL ON SAME CHANNEL {#hochreiter-1997-lstm-s5-3 .section tag=0891}

This experiment serves to illustrate that LSTM does not encounter fundamental problems if noise and signal are mixed on the same input line. We initially focus on Bengio et al.’s simple 1994 “2-sequence problem”; in Experiment 3c we will then pose a more challenging 2-sequence problem.

Task 3a (“2-sequence problem”). The task is to observe and then classify input sequences. There are two classes, each occurring with probability 0.5. There is only one input line. Only the first N real-valued sequence elements convey relevant information about the class. Sequence elements at positions $t > N$ are generated by a Gaussian with mean zero and variance 0.2. Case $N = 1$: the first sequence element is 1.0 for class 1, and -1.0 for class 2. Case $N = 3$: the first three elements are 1.0 for class 1 and -1.0 for class 2. The target at the sequence end is 1.0 for class 1 and 0.0 for class 2. Correct classification is defined as “absolute output error at sequence end below 0.2”. Given a constant T, the sequence length is randomly selected between T and T + T/10 (a difference to Bengio et al.’s problem is that they also permit shorter sequences of length T/2).

Guessing. Bengio et al. (1994) and Bengio and Frasconi (1994) tested 7 different methods on the 2-sequence problem. We discovered, however, that random weight guessing easily outper-

| T | N | stop: ST1 | stop: ST2 | # weights | ST2: fraction misclassified |
| --- | --- | --- | --- | --- | --- |
| 100 | 3 | 27,380 | 39,850 | 102 | 0.000195 |
| 100 | 1 | 58,370 | 64,330 | 102 | 0.000117 |
| 1000 | 3 | 446,850 | 452,460 | 102 | 0.000078 |

Table 4: *Task 3a: Bengio et al.’s 2-sequence problem. T is minimal sequence length. N is the number of information-conveying elements at sequence begin. The column headed by ST1 (ST2) gives the number of sequence presentations required to achieve stopping criterion ST1 (ST2). The rightmost column lists the fraction of misclassified post-training sequences (with absolute error > 0.2) from a test set consisting of 2560 sequences (tested after ST2 was achieved). All values are means of 10 trials. We discovered, however, that this problem is so simple that random weight guessing solves it faster than LSTM and any other method for which there are published results.* {#hochreiter-1997-lstm-tab-4 .table tag=0892}

forms them all, because the problem is so simple⁵. See Schmidhuber and Hochreiter (1996) and Hochreiter and Schmidhuber (1996, 1997) for additional results in this vein.

**LSTM architecture.** We use a 3-layer net with 1 input unit, 1 output unit, and 3 cell blocks of size 1. The output layer receives connections only from memory cells. Memory cells and gate units receive inputs from input units, memory cells and gate units, and have bias weights. Gate units and output unit are logistic sigmoid in [0, 1], $h$ in $[ -1, 1 ]$, and $g$ in $[ -2, 2 ]$.

**Training/Testing.** All weights (except the bias weights to gate units) are randomly initialized in the range $[ -0.1, 0.1 ]$. The first input gate bias is initialized with $-1.0$, the second with $-3.0$, and the third with $-5.0$. The first output gate bias is initialized with $-2.0$, the second with $-4.0$ and the third with $-6.0$. The precise initialization values hardly matter though, as confirmed by additional experiments. The learning rate is 1.0. All activations are reset to zero at the beginning of a new sequence.

We stop training (and judge the task as being solved) according to the following criteria: ST1: none of 256 sequences from a randomly chosen test set is misclassified. ST2: ST1 is satisfied, and mean absolute test set error is below 0.01. In case of ST2, an additional test set consisting of 2560 randomly chosen sequences is used to determine the fraction of misclassified sequences.

**Results.** See Table 4. The results are means of 10 trials with different weight initializations in the range $[ -0.1, 0.1 ]$. LSTM is able to solve this problem, though by far not as fast as random weight guessing (see paragraph “Guessing” above). Clearly, this trivial problem does not provide a very good testbed to compare performance of various non-trivial algorithms. Still, it demonstrates that LSTM does not encounter fundamental problems when faced with signal and noise on the same channel.

**Task 3b.** Architecture, parameters, etc. like in Task 3a, but now with Gaussian noise (mean 0 and variance 0.2) added to the information-conveying elements ($t \leq N$). We stop training (and judge the task as being solved) according to the following, slightly redefined criteria: ST1: less than 6 out of 256 sequences from a randomly chosen test set are misclassified. ST2: ST1 is satisfied, and mean absolute test set error is below 0.04. In case of ST2, an additional test set consisting of 2560 randomly chosen sequences is used to determine the fraction of misclassified sequences.

**Results.** See Table 5. The results represent means of 10 trials with different weight initializations. LSTM easily solves the problem.

**Task 3c.** Architecture, parameters, etc. like in Task 3a, but with a few essential changes that make the task non-trivial: the targets are 0.2 and 0.8 for class 1 and class 2, respectively, and there is Gaussian noise on the *targets* (mean 0 and variance 0.1; st.dev. 0.32). To minimize mean squared error, the system has to learn the *conditional expectations of the targets* given the inputs. Misclassification is defined as “absolute difference between output and noise-free target (0.2 for

⁵It should be mentioned, however, that different input representations and different types of noise may lead to worse guessing performance (Yoshua Bengio, personal communication, 1996).

| T | N | stop: ST1 | stop: ST2 | # weights | ST2: fraction misclassified |
| --- | --- | --- | --- | --- | --- |
| 100 | 3 | 41,740 | 43,250 | 102 | 0.00828 |
| 100 | 1 | 74,950 | 78,430 | 102 | 0.01500 |
| 1000 | 1 | 481,060 | 485,080 | 102 | 0.01207 |

Table 5: *Task 3b: modified 2-sequence problem. Same as in Table 4, but now the information-conveying elements are also perturbed by noise.* {#hochreiter-1997-lstm-tab-5 .table tag=0893}

| T | N | stop | # weights | fraction misclassified | av. difference to mean |
| --- | --- | --- | --- | --- | --- |
| 100 | 3 | 269,650 | 102 | 0.00558 | 0.014 |
| 100 | 1 | 565,640 | 102 | 0.00441 | 0.012 |

Table 6: *Task 3c: modified, more challenging 2-sequence problem. Same as in Table 4, but with noisy real-valued targets. The system has to learn the conditional expectations of the targets given the inputs. The rightmost column provides the average difference between network output and expected target. Unlike 3a and 3b, this task cannot be solved quickly by random weight guessing.* {#hochreiter-1997-lstm-tab-6 .table tag=0894}

class 1 and 0.8 for class 2) > 0.1. ” The network output is considered acceptable if the mean absolute difference between noise-free target and output is below 0.015. Since this requires high weight precision, *Task 3c (unlike 3a and 3b) cannot be solved quickly by random guessing*.

**Training/Testing.** The learning rate is 0.1. We stop training according to the following criterion: none of 256 sequences from a randomly chosen test set is misclassified, and mean absolute difference between noise free target and output is below 0.015. An additional test set consisting of 2560 randomly chosen sequences is used to determine the fraction of misclassified sequences.

**Results.** See Table 6. The results represent means of 10 trials with different weight initializations. Despite the noisy targets, LSTM still can solve the problem by learning the expected target values.

### 5.4 EXPERIMENT 4: ADDING PROBLEM {#hochreiter-1997-lstm-s5-4 .section tag=0895}

The difficult task in this section is of a type that has never been solved by other recurrent net algorithms. It shows that LSTM can solve long time lag problems involving distributed, continuous-valued representations.

**Task.** Each element of each input sequence is a pair of components. The first component is a real value randomly chosen from the interval [−1, 1]; the second is either 1.0, 0.0, or -1.0, and is used as a marker: at the end of each sequence, the task is to output the sum of the first components of those pairs that are *marked* by second components equal to 1.0. Sequences have random lengths between the minimal sequence length $T$ and $T + \frac{T}{10}$. In a given sequence exactly two pairs are marked as follows: we first randomly select and mark one of the first ten pairs (whose first component we call $X_1$). Then we randomly select and mark one of the first $\frac{T}{2} - 1$ still unmarked pairs (whose first component we call $X_2$). The second components of all remaining pairs are zero except for the first and final pair, whose second components are -1. (In the rare case where the *first* pair of the sequence gets marked, we set $X_1$ to zero.) An error signal is generated only at the sequence end: the target is $0.5 + \frac{X_1 + X_2}{4.0}$ (the sum $X_1 + X_2$ scaled to the interval [0, 1]). A sequence is processed correctly if the absolute error at the sequence end is below 0.04.

**Architecture.** We use a 3-layer net with 2 input units, 1 output unit, and 2 cell blocks of size 2. The output layer receives connections only from memory cells. Memory cells and gate units receive inputs from memory cells and gate units (i.e., the hidden layer is fully connected — less connectivity may work as well). The input layer has forward connections to all units in the hidden

| T | minimal lag | # weights | # wrong predictions | Success after |
| --- | --- | --- | --- | --- |
| 100 | 50 | 93 | 1 out of 2560 | 74,000 |
| 500 | 250 | 93 | 0 out of 2560 | 209,000 |
| 1000 | 500 | 93 | 1 out of 2560 | 853,000 |

Table 7: *EXPERIMENT 4: Results for the Adding Problem.* *T* is the minimal sequence length, *T/2* the minimal time lag. “*# wrong predictions*” is the number of incorrectly processed sequences (*error > 0.04*) from a test set containing 2560 sequences. *The rightmost column gives the number of training sequences required to achieve the stopping criterion. All values are means of 10 trials. For T = 1000 the number of required training examples varies between 370,000 and 2,020,000, exceeding 700,000 in only 3 cases.* {#hochreiter-1997-lstm-tab-7 .table tag=0896}

layer. All non-input units have bias weights. These architecture parameters make it easy to store at least 2 input signals (a cell block size of 1 works well, too). All activation functions are logistic with output range [0, 1], except for $h$, whose range is [−1, 1], and $g$, whose range is [−2, 2].

State drift versus initial bias. Note that the task requires storing the precise values of real numbers for long durations — the system must learn to protect memory cell contents against even minor internal state drift (see Section 4). To study the significance of the drift problem, we make the task even more difficult by biasing all non-input units, thus artificially inducing internal state drift. All weights (including the bias weights) are randomly initialized in the range [−0.1, 0.1]. Following Section 4’s remedy for state drifts, the first input gate bias is initialized with −3.0, the second with −6.0 (though the precise values hardly matter, as confirmed by additional experiments).

Training/Testing. The learning rate is 0.5. Training is stopped once the average training error is below 0.01, and the 2000 most recent sequences were processed correctly.

Results. With a test set consisting of 2560 randomly chosen sequences, the average test set error was always below 0.01, and there were never more than 3 incorrectly processed sequences. Table 7 shows details.

The experiment demonstrates: (1) LSTM is able to work well with distributed representations. (2) LSTM is able to learn to perform calculations involving *continuous* values. (3) Since the system manages to store continuous values without deterioration for minimal delays of $\frac{T}{2}$ time steps, there is no significant, harmful internal state drift.

### 5.5 EXPERIMENT 5: MULTIPLICATION PROBLEM {#hochreiter-1997-lstm-s5-5 .section tag=0897}

One may argue that LSTM is a bit biased towards tasks such as the Adding Problem from the previous subsection. Solutions to the Adding Problem may exploit the CEC’s built-in integration capabilities. Although this CEC property may be viewed as a feature rather than a disadvantage (integration seems to be a natural subtask of many tasks occurring in the real world), the question arises whether LSTM can also solve tasks with inherently non-integrative solutions. To test this, we change the problem by requiring the final target to equal the product (instead of the sum) of earlier marked inputs.

Task. Like the task in Section 5.4, except that the first component of each pair is a real value randomly chosen from the interval [0, 1]. In the rare case where the first pair of the input sequence gets marked, we set $X_1$ to 1.0. The target at sequence end is the product $X_1 \times X_2$.

Architecture. Like in Section 5.4. All weights (including the bias weights) are randomly initialized in the range [−0.1, 0.1].

Training/Testing. The learning rate is 0.1. We test performance twice: as soon as less than $n_{seq}$ of the 2000 most recent training sequences lead to absolute errors exceeding 0.04, where $n_{seq} = 140$, and $n_{seq} = 13$. Why these values? $n_{seq} = 140$ is sufficient to learn storage of the relevant inputs. It is not enough though to fine-tune the precise final outputs. $n_{seq} = 13$, however,

| T | minimal lag | # weights | $n_{seq}$ | # wrong predictions | MSE | Success after |
| --- | --- | --- | --- | --- | --- | --- |
| 100 | 50 | 93 | 140 | 139 out of 2560 | 0.0223 | 482,000 |
| 100 | 50 | 93 | 13 | 14 out of 2560 | 0.0139 | 1,273,000 |

Table 8: *EXPERIMENT 5: Results for the Multiplication Problem.* *T* is the minimal sequence length, *T*/2 the minimal time lag. *We test on a test set containing 2560 sequences as soon as less than $n_{seq}$ of the 2000 most recent training sequences lead to error > 0.04.* "*# wrong predictions*" is the number of test sequences with error > 0.04. *MSE* is the mean squared error on the test set. *The rightmost column lists numbers of training sequences required to achieve the stopping criterion. All values are means of 10 trials.* {#hochreiter-1997-lstm-tab-8 .table tag=0898}

leads to quite satisfactory results.

**Results.** For $n_{seq}$ = 140 ($n_{seq}$ = 13) with a test set consisting of 2560 randomly chosen sequences, the average test set error was always below 0.026 (0.013), and there were never more than 170 (15) incorrectly processed sequences. Table 8 shows details. (A net with additional standard hidden units or with a hidden layer above the memory cells may learn the fine-tuning part more quickly.)

The experiment demonstrates: LSTM can solve tasks involving both continuous-valued representations and non-integrative information processing.

### 5.6 EXPERIMENT 6: TEMPORAL ORDER {#hochreiter-1997-lstm-s5-6 .section tag=0899}

In this subsection, LSTM solves other difficult (but artificial) tasks that have never been solved by previous recurrent net algorithms. The experiment shows that LSTM is able to extract information conveyed by the temporal order of widely separated inputs.

**Task 6a:** two relevant, widely separated symbols. The goal is to classify sequences. Elements and targets are represented locally (input vectors with only one non-zero bit). The sequence starts with an *E*, ends with a *B* (the “trigger symbol”) and otherwise consists of randomly chosen symbols from the set {a, b, c, d} except for two elements at positions $t_{1}$ and $t_{2}$ that are either *X* or *Y*. The sequence length is randomly chosen between 100 and 110, $t_{1}$ is randomly chosen between 10 and 20, and $t_{2}$ is randomly chosen between 50 and 60. There are 4 sequence classes Q, R, S, U which depend on the temporal order of X and Y. The rules are: X, X → Q; X, Y → R; Y, X → S; Y, Y → U.

**Task 6b:** three relevant, widely separated symbols. Again, the goal is to classify sequences. Elements/targets are represented locally. The sequence starts with an *E*, ends with a *B* (the “trigger symbol”), and otherwise consists of randomly chosen symbols from the set {a, b, c, d} except for three elements at positions $t_{1}$, $t_{2}$ and $t_{3}$ that are either *X* or *Y*. The sequence length is randomly chosen between 100 and 110, $t_{1}$ is randomly chosen between 10 and 20, $t_{2}$ is randomly chosen between 33 and 43, and $t_{3}$ is randomly chosen between 66 and 76. There are 8 sequence classes Q, R, S, U, V, A, B, C which depend on the temporal order of the Xs and Ys. The rules are: X, X, X → Q; X, X, Y → R; X, Y, X → S; X, Y, Y → U; Y, X, X → V; Y, X, Y → A; Y, Y, X → B; Y, Y, Y → C.

There are as many output units as there are classes. Each class is locally represented by a binary target vector with one non-zero component. With both tasks, error signals occur only at the end of a sequence. The sequence is classified correctly if the final absolute error of all output units is below 0.3.

**Architecture.** We use a 3-layer net with 8 input units, 2 (3) cell blocks of size 2 and 4 (8) output units for Task 6a (6b). Again all non-input units have bias weights, and the output layer receives connections from memory cells only. Memory cells and gate units receive inputs from input units, memory cells and gate units (i.e., the hidden layer is fully connected — less connectivity may work as well). The architecture parameters for Task 6a (6b) make it easy to store at least 2 (3) input signals. All activation functions are logistic with output range [0, 1], except for $h$, whose range is [−1, 1], and $g$, whose range is [−2, 2].

Training/Testing. The learning rate is 0.5 (0.1) for Experiment 6a (6b). Training is stopped once the average training error falls below 0.1 and the 2000 most recent sequences were classified correctly. All weights are initialized in the range [−0.1, 0.1]. The first input gate bias is initialized with −2.0, the second with −4.0, and (for Experiment 6b) the third with −6.0 (again, we confirmed by additional experiments that the precise values hardly matter).

Results. With a test set consisting of 2560 randomly chosen sequences, the average test set error was always below 0.1, and there were never more than 3 incorrectly classified sequences. Table 9 shows details.

The experiment shows that LSTM is able to extract information conveyed by the temporal order of widely separated inputs. In Task 6a, for instance, the delays between first and second relevant input and between second relevant input and sequence end are at least 30 time steps.

| task | # weights | # wrong predictions | Success after |
| --- | --- | --- | --- |
| Task 6a | 156 | 1 out of 2560 | 31,390 |
| Task 6b | 308 | 2 out of 2560 | 571,100 |

Table 9: EXPERIMENT 6: Results for the Temporal Order Problem. “# wrong predictions” is the number of incorrectly classified sequences (error > 0.3 for at least one output unit) from a test set containing 2560 sequences. The rightmost column gives the number of training sequences required to achieve the stopping criterion. The results for Task 6a are means of 20 trials; those for Task 6b of 10 trials. {#hochreiter-1997-lstm-tab-9 .table tag=089A}

Typical solutions. In Experiment 6a, how does LSTM distinguish between temporal orders $(X, Y)$ and $(Y, X)$? One of many possible solutions is to store the first $X$ or $Y$ in cell block 1, and the second $X/Y$ in cell block 2. Before the first $X/Y$ occurs, block 1 can see that it is still empty by means of its recurrent connections. After the first $X/Y$, block 1 can close its input gate. Once block 1 is filled and closed, this fact will become visible to block 2 (recall that all gate units and all memory cells receive connections from all non-output units).

Typical solutions, however, require only one memory cell block. The block stores the first $X$ or $Y$; once the second $X/Y$ occurs, it changes its state depending on the first stored symbol. Solution type 1 exploits the connection between memory cell output and input gate unit — the following events cause different input gate activations: “$X$ occurs in conjunction with a filled block”; “$X$ occurs in conjunction with an empty block”. Solution type 2 is based on a strong positive connection between memory cell output and memory cell input. The previous occurrence of $X$ ($Y$) is represented by a positive (negative) internal state. Once the input gate opens for the second time, so does the output gate, and the memory cell output is fed back to its own input. This causes $(X, Y)$ to be represented by a positive internal state, because $X$ contributes to the new internal state twice (via current internal state and cell output feedback). Similarly, $(Y, X)$ gets represented by a negative internal state.

### 5.7 SUMMARY OF EXPERIMENTAL CONDITIONS {#hochreiter-1997-lstm-s5-7 .section tag=089B}

The two tables in this subsection provide an overview of the most important LSTM parameters and architectural details for Experiments 1–6. The conditions of the simple experiments 2a and 2b differ slightly from those of the other, more systematic experiments, due to historical reasons.

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Task | p | lag | b | s | in | out | w | c | ogb | igb | bias | h | g | $\alpha$ |
| 1-1 | 9 | 9 | 4 | 1 | 7 | 7 | 264 | F | -1,-2,-3,-4 | r | ga | h1 | g2 | 0.1 |
| 1-2 | 9 | 9 | 3 | 2 | 7 | 7 | 276 | F | -1,-2,-3 | r | ga | h1 | g2 | 0.1 |

to be continued on next page

| continued from previous page |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Task | p | lag | b | s | in | out | w | c | ogb | igb | bias | h | g | α |
| 1-3 | 9 | 9 | 3 | 2 | 7 | 7 | 276 | F | -1,-2,-3 | r | ga | h1 | g2 | 0.2 |
| 1-4 | 9 | 9 | 4 | 1 | 7 | 7 | 264 | F | -1,-2,-3,-4 | r | ga | h1 | g2 | 0.5 |
| 1-5 | 9 | 9 | 3 | 2 | 7 | 7 | 276 | F | -1,-2,-3 | r | ga | h1 | g2 | 0.5 |
| 2a | 100 | 100 | 1 | 1 | 101 | 101 | 10504 | B | no og | none | none | id | g1 | 1.0 |
| 2b | 100 | 100 | 1 | 1 | 101 | 101 | 10504 | B | no og | none | none | id | g1 | 1.0 |
| 2c-1 | 50 | 50 | 2 | 1 | 54 | 2 | 364 | F | none | none | none | h1 | g2 | 0.01 |
| 2c-2 | 100 | 100 | 2 | 1 | 104 | 2 | 664 | F | none | none | none | h1 | g2 | 0.01 |
| 2c-3 | 200 | 200 | 2 | 1 | 204 | 2 | 1264 | F | none | none | none | h1 | g2 | 0.01 |
| 2c-4 | 500 | 500 | 2 | 1 | 504 | 2 | 3064 | F | none | none | none | h1 | g2 | 0.01 |
| 2c-5 | 1000 | 1000 | 2 | 1 | 1004 | 2 | 6064 | F | none | none | none | h1 | g2 | 0.01 |
| 2c-6 | 1000 | 1000 | 2 | 1 | 504 | 2 | 3064 | F | none | none | none | h1 | g2 | 0.01 |
| 2c-7 | 1000 | 1000 | 2 | 1 | 204 | 2 | 1264 | F | none | none | none | h1 | g2 | 0.01 |
| 2c-8 | 1000 | 1000 | 2 | 1 | 104 | 2 | 664 | F | none | none | none | h1 | g2 | 0.01 |
| 2c-9 | 1000 | 1000 | 2 | 1 | 54 | 2 | 364 | F | none | none | none | h1 | g2 | 0.01 |
| 3a | 100 | 100 | 3 | 1 | 1 | 1 | 102 | F | -2,-4,-6 | -1,-3,-5 | b1 | h1 | g2 | 1.0 |
| 3b | 100 | 100 | 3 | 1 | 1 | 1 | 102 | F | -2,-4,-6 | -1,-3,-5 | b1 | h1 | g2 | 1.0 |
| 3c | 100 | 100 | 3 | 1 | 1 | 1 | 102 | F | -2,-4,-6 | -1,-3,-5 | b1 | h1 | g2 | 0.1 |
| 4-1 | 100 | 50 | 2 | 2 | 2 | 1 | 93 | F | r | -3,-6 | all | h1 | g2 | 0.5 |
| 4-2 | 500 | 250 | 2 | 2 | 2 | 1 | 93 | F | r | -3,-6 | all | h1 | g2 | 0.5 |
| 4-3 | 1000 | 500 | 2 | 2 | 2 | 1 | 93 | F | r | -3,-6 | all | h1 | g2 | 0.5 |
| 5 | 100 | 50 | 2 | 2 | 2 | 1 | 93 | F | r | r | all | h1 | g2 | 0.1 |
| 6a | 100 | 40 | 2 | 2 | 8 | 4 | 156 | F | r | -2,-4 | all | h1 | g2 | 0.5 |
| 6b | 100 | 24 | 3 | 2 | 8 | 8 | 308 | F | r | -2,-4,-6 | all | h1 | g2 | 0.1 |

Table 10: *Summary of experimental conditions for LSTM, Part I.* *1st column*: task number. *2nd column*: minimal sequence length p. *3rd column*: minimal number of steps between most recent relevant input information and teacher signal. *4th column*: number of cell blocks b. *5th column*: block size s. *6th column*: number of input units in. *7th column*: number of output units out. *8th column*: number of weights w. *9th column*: c describes connectivity: “F” means “output layer receives connections from memory cells; memory cells and gate units receive connections from input units, memory cells and gate units”; “B” means “each layer receives connections from all layers below”. *10th column*: initial output gate bias ogb, where “r” stands for “randomly chosen from the interval [−0.1,0.1]” and “no og” means “no output gate used”. *11th column*: initial input gate bias igb (see 10th column). *12th column*: which units have bias weights? “b1” stands for “all hidden units”, “ga” for “only gate units”, and “all” for “all non-input units”. *13th column*: the function h, where “id” is identity function, “h1” is logistic sigmoid in [−2,2]. *14th column*: the logistic function g, where “g1” is sigmoid in [0,1], “g2” in [−1,1]. *15th column*: learning rate α. {#hochreiter-1997-lstm-tab-10 .table tag=089C}

| 1 | 2 | 3 | 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- |
| Task | select | interval | test set size | stopping criterion | success |
| 1 | t1 | [−0.2,0.2] | 256 | training & test correctly pred. | see text |
| 2a | t1 | [−0.2,0.2] | no test set | after 5 million exemplars | ABS(0.25) |
| 2b | t2 | [−0.2,0.2] | 10000 | after 5 million exemplars | ABS(0.25) |
| 2c | t2 | [−0.2,0.2] | 10000 | after 5 million exemplars | ABS(0.2) |
| 3a | t3 | [−0.1,0.1] | 2560 | ST1 and ST2 (see text) | ABS(0.2) |
| 3b | t3 | [−0.1,0.1] | 2560 | ST1 and ST2 (see text) | ABS(0.2) |
| 3c | t3 | [−0.1,0.1] | 2560 | ST1 and ST2 (see text) | see text |
| 4 | t3 | [−0.1,0.1] | 2560 | ST3(0.01) | ABS(0.04) |
| 5 | t3 | [−0.1,0.1] | 2560 | see text | ABS(0.04) |
| 6a | t3 | [−0.1,0.1] | 2560 | ST3(0.1) | ABS(0.3) |
| 6b | t3 | [−0.1,0.1] | 2560 | ST3(0.1) | ABS(0.3) |

Table 11: Summary of experimental conditions for LSTM, Part II. 1st column: task number. 2nd column: training exemplar selection, where “t1” stands for “randomly chosen from training set”, “t2” for “randomly chosen from 2 classes”, and “t3” for “randomly generated on-line”. 3rd column: weight initialization interval. 4th column: test set size. 5th column: stopping criterion for training, where “ST3(β)” stands for “average training error below β and the 2000 most recent sequences were processed correctly”. 6th column: success (correct classification) criterion, where “ABS(β)” stands for “absolute error of all output units at sequence end is below β”. {#hochreiter-1997-lstm-tab-11 .table tag=089D}
