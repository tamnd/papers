---
paper: hochreiter-1997-lstm
title: Long Short-Term Memory
authors:
  - Sepp Hochreiter
  - Jurgen Schmidhuber
year: 1997
venue: Neural Computation
field: ai-ml
section: "4"
section_title: LONG SHORT-TERM MEMORY
tag: "0886"
kind: section
lang: en
source: doi:10.1162/neco.1997.9.8.1735
pdf_sha256: ceb9e53dbc0493f5b3bf5520ed940f3e6b526064d17b2118d77e51f79c0edcc6
pdf_pages: 6-9
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 3a47a500c8303d4ffa56cfe50d038fc98d367d1366f644a075d21719ddd20d46
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Memory cells and gate units. To construct an architecture that allows for constant error flow through special, self-connected units without the disadvantages of the naive approach, we extend the constant error carrousel CEC embodied by the self-connected, linear unit $j$ from Section 3.2 by introducing additional features. A multiplicative *input gate unit* is introduced to protect the memory contents stored in $j$ from perturbation by irrelevant inputs. Likewise, a multiplicative *output gate unit* is introduced which protects other units from perturbation by currently irrelevant memory contents stored in $j$.

The resulting, more complex unit is called a *memory cell* (see Figure 1). The $j$-th memory cell is denoted $c_j$. Each memory cell is built around a central linear unit with a fixed self-connection (the CEC). In addition to $net_{c_j}$, $c_j$ gets input from a multiplicative unit $out_j$ (the “output gate”), and from another multiplicative unit $in_j$ (the “input gate”). $in_j$’s activation at time $t$ is denoted by $y^{in_j}(t)$, $out_j$’s by $y^{out_j}(t)$. We have

$$
y^{out_j}(t) = f_{out_j}(net_{out_j}(t));\ y^{in_j}(t) = f_{in_j}(net_{in_j}(t));
$$

where

$$
net_{out_j}(t) = \sum_u w_{out_ju} y^u(t-1),
$$

and

$$
net_{in_j}(t) = \sum_u w_{in_ju} y^u(t-1).
$$

We also have

$$
net_{c_j}(t) = \sum_u w_{c_ju} y^u(t-1).
$$

The summation indices $u$ may stand for input units, gate units, memory cells, or even conventional hidden units if there are any (see also paragraph on “network topology” below). All these different types of units may convey useful information about the current state of the net. For instance, an input gate (output gate) may use inputs from other memory cells to decide whether to store (access) certain information in its memory cell. There even may be recurrent self-connections like $w_{c_j c_j}$. It is up to the user to define the network topology. See Figure 2 for an example.

At time $t$, $c_j$'s output $y^{c_j}(t)$ is computed as

$$
y^{c_j}(t) = y^{out_j}(t) h(s_{c_j}(t)),
$$

where the “internal state” $s_{c_j}(t)$ is

$$
s_{c_j}(0) = 0, \quad s_{c_j}(t) = s_{c_j}(t-1) + y^{in_j}(t) g\left(net_{c_j}(t)\right) \text{ for } t > 0.
$$

The differentiable function $g$ squashes $net_{c_j}$; the differentiable function $h$ scales memory cell outputs computed from the internal state $s_{c_j}$.

Figure.

Figure 1: Architecture of memory cell $c_j$ (the box) and its gate units $in_j, out_j$. The self-recurrent connection (with weight 1.0) indicates feedback with a delay of 1 time step. It builds the basis of the “constant error carousel” CEC. The gate units open and close access to CEC. See text and appendix A.1 for details. {#hochreiter-1997-lstm-fig-1 .figure tag=0887}

Why gate units? To avoid input weight conflicts, $in_j$ controls the error flow to memory cell $c_j$'s input connections $w_{c_j i}$. To circumvent $c_j$'s output weight conflicts, $out_j$ controls the error flow from unit $j$'s output connections. In other words, the net can use $in_j$ to decide when to keep or override information in memory cell $c_j$, and $out_j$ to decide when to access memory cell $c_j$ and when to prevent other units from being perturbed by $c_j$ (see Figure 1).

Error signals trapped within a memory cell’s CEC cannot change – but different error signals flowing into the cell (at different times) via its output gate may get superimposed. The output gate will have to learn which errors to trap in its CEC, by appropriately scaling them. The input gate will have to learn when to release errors, again by appropriately scaling them. Essentially, the multiplicative gate units open and close access to constant error flow through CEC.

Distributed output representations typically do require output gates. Not always are both gate types necessary, though — one may be sufficient. For instance, in Experiments 2a and 2b in Section 5, it will be possible to use input gates only. In fact, output gates are not required in case of local output encoding — preventing memory cells from perturbing already learned outputs can be done by simply setting the corresponding weights to zero. Even in this case, however, output gates can be beneficial: they prevent the net’s attempts at storing long time lag memories (which are usually hard to learn) from perturbing activations representing easily learnable short time lag memories. (This will prove quite useful in Experiment 1, for instance.)

Network topology. We use networks with one input layer, one hidden layer, and one output layer. The (fully) self-connected hidden layer contains memory cells and corresponding gate units (for convenience, we refer to both memory cells and gate units as being located in the hidden layer). The hidden layer may also contain “conventional” hidden units providing inputs to gate units and memory cells. All units (except for gate units) in all layers have directed connections (serve as inputs) to all units in the layer above (or to all higher layers – Experiments 2a and 2b).

Memory cell blocks. S memory cells sharing the same input gate and the same output gate form a structure called a “memory cell block of size S”. Memory cell blocks facilitate information storage — as with conventional neural nets, it is not so easy to code a distributed input within a single cell. Since each memory cell block has as many gate units as a single memory cell (namely two), the block architecture can be even slightly more efficient (see paragraph “computational complexity”). A memory cell block of size 1 is just a simple memory cell. In the experiments (Section 5), we will use memory cell blocks of various sizes.

Learning. We use a variant of RTRL (e.g., Robinson and Fallside 1987) which properly takes into account the altered, multiplicative dynamics caused by input and output gates. However, to ensure non-decaying error backprop through internal states of memory cells, as with truncated BPTT (e.g., Williams and Peng 1990), errors arriving at “memory cell net inputs” (for cell c_j, this includes net_{c_j}, net_{in_j}, net_{out_j}) do not get propagated back further in time (although they do serve to change the incoming weights). Only within^2 memory cells, errors are propagated back through previous internal states s_{c_j}. To visualize this: once an error signal arrives at a memory cell output, it gets scaled by output gate activation and h'. Then it is within the memory cell’s CEC, where it can flow back indefinitely without ever being scaled. Only when it leaves the memory cell through the input gate and g, it is scaled once more by input gate activation and g'. It then serves to change the incoming weights before it is truncated (see appendix for explicit formulae).

Computational complexity. As with Mozer’s focused recurrent backprop algorithm (Mozer 1989), only the derivatives $\frac{\partial s_{c_j}}{\partial w_{il}}$ need to be stored and updated. Hence the LSTM algorithm is very efficient, with an excellent update complexity of $O(W)$, where W the number of weights (see details in appendix A.1). Hence, LSTM and BPTT for fully recurrent nets have the same update complexity per time step (while RTRL’s is much worse). Unlike full BPTT, however, LSTM is local in space and time^3: there is no need to store activation values observed during sequence processing in a stack with potentially unlimited size.

Abuse problem and solutions. In the beginning of the learning phase, error reduction may be possible without storing information over time. The network will thus tend to abuse memory cells, e.g., as bias cells (i.e., it might make their activations constant and use the outgoing connections as adaptive thresholds for other units). The potential difficulty is: it may take a long time to release abused memory cells and make them available for further learning. A similar “abuse problem” appears if two memory cells store the same (redundant) information. There are at least two solutions to the abuse problem: (1) Sequential network construction (e.g., Fahlman 1991): a memory cell and the corresponding gate units are added to the network whenever the

^2For intra-cellular backprop in a quite different context see also Doya and Yoshizawa (1989).
^3Following Schmidhuber (1989), we say that a recurrent net algorithm is local in space if the update complexity per time step and weight does not depend on network size. We say that a method is local in time if its storage requirements do not depend on input sequence length. For instance, RTRL is local in time but not in space. BPTT is local in space but not in time.

Figure 2: Example of a net with 8 input units, 4 output units, and 2 memory cell blocks of size 2. in1 marks the input gate, out1 marks the output gate, and cell1/block1 marks the first memory cell of block 1. cell1/block1’s architecture is identical to the one in Figure 1, with gate units in1 and out1 (note that by rotating Figure 1 by 90 degrees anti-clockwise, it will match with the corresponding parts of Figure 1). The example assumes dense connectivity: each gate unit and each memory cell see all non-output units. For simplicity, however, outgoing weights of only one type of unit are shown for each layer. With the efficient, truncated update rule, error flows only through connections to output units, and through fixed self-connections within cell blocks (not shown here — see Figure 1). Error flow is truncated once it “wants” to leave memory cells or gate units. Therefore, no connection shown above serves to propagate error back to the unit from which the connection originates (except for connections to output units), although the connections themselves are modifiable. That’s why the truncated LSTM algorithm is so efficient, despite its ability to bridge very long time lags. See text and appendix A.1 for details. Figure 2 actually shows the architecture used for Experiment 6a — only the bias of the non-input units is omitted. {#hochreiter-1997-lstm-fig-2 .figure tag=0888}

error stops decreasing (see Experiment 2 in Section 5). (2) Output gate bias: each output gate gets a negative initial bias, to push initial memory cell activations towards zero. Memory cells with more negative bias automatically get “allocated” later (see Experiments 1, 3, 4, 5, 6 in Section 5).

Internal state drift and remedies. If memory cell $c_j$'s inputs are mostly positive or mostly negative, then its internal state $s_j$ will tend to drift away over time. This is potentially dangerous, for the $h'(s_j)$ will then adopt very small values, and the gradient will vanish. One way to circumvent this problem is to choose an appropriate function $h$. But $h(x) = x$, for instance, has the disadvantage of unrestricted memory cell output range. Our simple but effective way of solving drift problems at the beginning of learning is to initially bias the input gate $in_j$ towards zero. Although there is a tradeoff between the magnitudes of $h'(s_j)$ on the one hand and of $y^{in_j}$ and $f_{in_j}'$ on the other, the potential negative effect of input gate bias is negligible compared to the one of the drifting effect. With logistic sigmoid activation functions, there appears to be no need for fine-tuning the initial bias, as confirmed by Experiments 4 and 5 in Section 5.4.
