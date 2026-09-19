---
paper: hochreiter-1997-lstm
title: Long Short-Term Memory
authors:
  - Sepp Hochreiter
  - Jurgen Schmidhuber
year: 1997
venue: Neural Computation
field: ai-ml
section_title: Appendix
kind: appendix
lang: en
source: doi:10.1162/neco.1997.9.8.1735
pdf_sha256: ceb9e53dbc0493f5b3bf5520ed940f3e6b526064d17b2118d77e51f79c0edcc6
pdf_pages: 23-30
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: cb6f474c098c44307f98e41ccd023bdfef76a2cc4b6dfbd84fd3723a29ead228
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

A.1 ALGORITHM DETAILS

In what follows, the index $k$ ranges over output units, $i$ ranges over hidden units, $c_j$ stands for the $j$-th memory cell block, $c_j^v$ denotes the $v$-th unit of memory cell block $c_j$, $u, l, m$ stand for arbitrary units, $t$ ranges over all time steps of a given input sequence.

The gate unit logistic sigmoid (with range [0, 1]) used in the experiments is

$$
f(x) = \frac{1}{1 + \exp(-x)} .
$$

The function $h$ (with range $[-1, 1]$) used in the experiments is

$$
h(x) = \frac{2}{1 + \exp(-x)} - 1 .
$$

The function $g$ (with range $[-2, 2]$) used in the experiments is

$$
g(x) = \frac{4}{1 + \exp(-x)} - 2 .
$$

Forward pass.
The net input and the activation of hidden unit $i$ are

$$
net_i(t) = \sum_u w_{iu} y^u(t-1)
$$

$$
y^i(t) = f_i(net_i(t)) .
$$

The net input and the activation of $in_j$ are

$$
net_{in_j}(t) = \sum_u w_{in_ju} y^u(t-1)
$$

$$
y^{in_j}(t) = f_{in_j}(net_{in_j}(t)) .
$$

The net input and the activation of $out_j$ are

$$
net_{out_j}(t) = \sum_u w_{out_ju} y^u(t-1)
$$

$$
y^{out_j}(t) = f_{out_j}(net_{out_j}(t)) .
$$

The net input $net_{c_j^v}$, the internal state $s_{c_j^v}$, and the output activation $y^{c_j^v}$ of the $v$-th memory cell of memory cell block $c_j$ are:

$$
net_{c_j^v}(t) = \sum_u w_{c_j^vu} y^u(t-1)
$$

$$
s_{c_j^v}(t) = s_{c_j^v}(t-1) + y^{in_j}(t) g \left( net_{c_j^v}(t) \right)
$$

$$
y^{c_j^v}(t) = y^{out_j}(t) h(s_{c_j^v}(t)) .
$$

The net input and the activation of output unit $k$ are

$$
net_k(t) = \sum_{u: u \text{ not a gate}} w_{ku} y^u(t-1)
$$

$$
y^k(t) = f_k(net_k(t)) .
$$

The backward pass to be described later is based on the following truncated backprop formulae.

Approximate derivatives for truncated backprop. The truncated version (see Section 4) only approximates the partial derivatives, which is reflected by the “$\approx_{tr}$” signs in the notation below. It truncates error flow once it leaves memory cells or gate units. Truncation ensures that there are no loops across which an error that left some memory cell through its input or input gate can reenter the cell through its output or output gate. This in turn ensures constant error flow through the memory cell’s CEC.

In the truncated backprop version, the following derivatives are replaced by zero:

$$
\frac{\partial net_{in_j}(t)}{\partial y^u(t-1)} \approx_{tr} 0 \quad \forall u,
$$

$$
\frac{\partial net_{out_j}(t)}{\partial y^u(t-1)} \approx_{tr} 0 \quad \forall u,
$$

and

$$
\frac{\partial net_{c_j}(t)}{\partial y^u(t-1)} \approx_{tr} 0 \quad \forall u.
$$

Therefore we get

$$
\frac{\partial y^{in_j}(t)}{\partial y^u(t-1)} = f'_{in_j}(net_{in_j}(t)) \frac{\partial net_{in_j}(t)}{\partial y^u(t-1)} \approx_{tr} 0 \quad \forall u,
$$

$$
\frac{\partial y^{out_j}(t)}{\partial y^u(t-1)} = f'_{out_j}(net_{out_j}(t)) \frac{\partial net_{out_j}(t)}{\partial y^u(t-1)} \approx_{tr} 0 \quad \forall u,
$$

and

$$
\frac{\partial y^{c_j}(t)}{\partial y^u(t-1)} = \frac{\partial y^{c_j}(t)}{\partial net_{out_j}(t)} \frac{\partial net_{out_j}(t)}{\partial y^u(t-1)} + \frac{\partial y^{c_j}(t)}{\partial net_{in_j}(t)} \frac{\partial net_{in_j}(t)}{\partial y^u(t-1)} + \frac{\partial y^{c_j}(t)}{\partial net_{c_j}(t)} \frac{\partial net_{c_j}(t)}{\partial y^u(t-1)} \approx_{tr} 0 \quad \forall u.
$$

This implies for all $w_{lm}$ not on connections to $c_j^v, in_j, out_j$ (that is, $l \notin \{c_j^v, in_j, out_j\}$):

$$
\frac{\partial y^{c_j^v}(t)}{\partial w_{lm}} = \sum_u \frac{\partial y^{c_j^v}(t)}{\partial y^u(t-1)} \frac{\partial y^u(t-1)}{\partial w_{lm}} \approx_{tr} 0.
$$

The truncated derivatives of output unit $k$ are:

$$
\frac{\partial y^k(t)}{\partial w_{lm}} = f'_k(net_k(t)) \left( \sum_{u: u \text{ not a gate}} w_{ku} \frac{\partial y^u(t-1)}{\partial w_{lm}} + \delta_{kl} y^m(t-1) \right) \approx_{tr}
$$

$$
f'_k(net_k(t)) \left( \sum_j \sum_{v=1}^{S_j} \delta_{c_j^v l} w_{kc_j^v} \frac{\partial y^{c_j^v}(t-1)}{\partial w_{lm}} + \sum_j (\delta_{in_j l} + \delta_{out_j l}) \sum_{v=1}^{S_j} w_{kc_j^v} \frac{\partial y^{c_j^v}(t-1)}{\partial w_{lm}} + \sum_{i: i \text{ hidden unit}} w_{ki} \frac{\partial y^i(t-1)}{\partial w_{lm}} + \delta_{kl} y^m(t-1) \right) =
$$

$$
f'_k(net_k(t)) \begin{cases}
y^m(t-1) & l = k \\
w_{kc_j^v} \frac{\partial y^{c_j^v}(t-1)}{\partial w_{lm}} & l = c_j^v \\
\sum_{v=1}^{S_j} w_{kc_j^v} \frac{\partial y^{c_j^v}(t-1)}{\partial w_{lm}} & l = in_j \text{ OR } l = out_j \\
\sum_{i: i \text{ hidden unit}} w_{ki} \frac{\partial y^i(t-1)}{\partial w_{lm}} & l \text{ otherwise }
\end{cases},
$$

where $\delta$ is the Kronecker delta ($\delta_{ab} = 1$ if $a = b$ and 0 otherwise), and $S_j$ is the size of memory cell block $c_j$. The truncated derivatives of a hidden unit $i$ that is not part of a memory cell are:

$$
\frac{\partial y^i(t)}{\partial w_{lm}} = f'_i(net_i(t)) \frac{\partial net_i(t)}{\partial w_{lm}} \approx_{tr} \delta_{li} f'_i(net_i(t)) y^m(t-1) .
$$

(Note: here it would be possible to use the full gradient without affecting constant error flow through internal states of memory cells.)

Cell block $c_j$'s truncated derivatives are:

$$
\frac{\partial y^{in_j}(t)}{\partial w_{lm}} = f'_{in_j}(net_{in_j}(t)) \frac{\partial net_{in_j}(t)}{\partial w_{lm}} \approx_{tr} \delta_{in_j l} f'_{in_j}(net_{in_j}(t)) y^m(t-1) .
$$

(12)

$$
\frac{\partial y^{out_j}(t)}{\partial w_{lm}} = f'_{out_j}(net_{out_j}(t)) \frac{\partial net_{out_j}(t)}{\partial w_{lm}} \approx_{tr} \delta_{out_j l} f'_{out_j}(net_{out_j}(t)) y^m(t-1) .
$$

(13)

$$
\frac{\partial s_{c_j^v}(t)}{\partial w_{lm}} = \frac{\partial s_{c_j^v}(t-1)}{\partial w_{lm}} + \frac{\partial y^{in_j}(t)}{\partial w_{lm}} g\left(net_{c_j^v}(t)\right) + y^{in_j}(t) g'\left(net_{c_j^v}(t)\right) \frac{\partial net_{c_j^v}(t)}{\partial w_{lm}} \approx_{tr}
$$

$$
\left(\delta_{in_j l} + \delta_{c_j^v l}\right) \frac{\partial s_{c_j^v}(t-1)}{\partial w_{lm}} + \delta_{in_j l} \frac{\partial y^{in_j}(t)}{\partial w_{lm}} g\left(net_{c_j^v}(t)\right) +
\delta_{c_j^v l} y^{in_j}(t) g'\left(net_{c_j^v}(t)\right) \frac{\partial net_{c_j^v}(t)}{\partial w_{lm}} =
$$

$$
\left(\delta_{in_j l} + \delta_{c_j^v l}\right) \frac{\partial s_{c_j^v}(t-1)}{\partial w_{lm}} + \delta_{in_j l} f'_{in_j}(net_{in_j}(t)) \ g\left(net_{c_j^v}(t)\right) y^m(t-1) +
\delta_{c_j^v l} \ y^{in_j}(t) \ g'\left(net_{c_j^v}(t)\right) y^m(t-1) .
$$

$$
\frac{\partial y^{c_j^v}(t)}{\partial w_{lm}} = \frac{\partial y^{out_j}(t)}{\partial w_{lm}} h(s_{c_j^v}(t)) + h'(s_{c_j^v}(t)) \frac{\partial s_{c_j^v}(t)}{\partial w_{lm}} y^{out_j}(t) \approx_{tr}
$$

(15)

$$
\delta_{out_j l} \frac{\partial y^{out_j}(t)}{\partial w_{lm}} h(s_{c_j^v}(t)) + \left(\delta_{in_j l} + \delta_{c_j^v l}\right) h'(s_{c_j^v}(t)) \frac{\partial s_{c_j^v}(t)}{\partial w_{lm}} y^{out_j}(t) .
$$

To efficiently update the system at time $t$, the only (truncated) derivatives that need to be stored at time $t-1$ are $\frac{\partial s_{c_j^v}(t-1)}{\partial w_{lm}}$, where $l = c_j^v$ or $l = in_j$.

Backward pass. We will describe the backward pass only for the particularly efficient “truncated gradient version” of the LSTM algorithm. For simplicity we will use equal signs even where approximations are made according to the truncated backprop equations above.

The squared error at time $t$ is given by

$$
E(t) = \sum_{k: k \text{ output unit}} \left(t^k(t) - y^k(t)\right)^2 ,
$$

(16) where $t^k(t)$ is output unit $k$'s target at time $t$.

Time $t$'s contribution to $w_{lm}$'s gradient-based update with learning rate $\alpha$ is

$$
\Delta w_{lm}(t) = -\alpha \frac{\partial E(t)}{\partial w_{lm}} .
$$

(17)

We define some unit $l$'s error at time step $t$ by

$$
e_l(t) := -\frac{\partial E(t)}{\partial net_l(t)} .
$$

(18)

Using (almost) standard backprop, we first compute updates for weights to output units ($l = k$), weights to hidden units ($l = i$) and weights to output gates ($l = out_j$). We obtain (compare formulae (10), (11), (13)):

$$
l = k \text{ (output)} : \quad e_k(t) = f'_k(net_k(t)) \ (t^k(t) - y^k(t)) ,
$$

(19)

$$
l = i \text{ (hidden)} : \quad e_i(t) = f'_i(net_i(t)) \sum_{k: k \text{ output unit}} w_{ki} e_k(t) ,
$$

(20)

$$
l = out_j \ (\text{output gates}) :
$$

$$
e_{out_j}(t) = f'_{out_j}(net_{out_j}(t)) \left( \sum_{v=1}^{S_j} h(s_{c_j^v}(t)) \sum_{k: k \text{ output unit}} w_{kc_j^v} e_k(t) \right).
$$

For all possible $l$ time $t$'s contribution to $w_{lm}$'s update is

$$
\Delta w_{lm}(t) = \alpha \ e_l(t) \ y^m(t-1) .
$$

The remaining updates for weights to input gates ($l = in_j$) and to cell units ($l = c_j^v$) are less conventional. We define some internal state $s_{c_j^v}$'s error:

$$
e_{s_{c_j^v}} := - \frac{\partial E(t)}{\partial s_{c_j^v}(t)} =
f_{out_j}(net_{out_j}(t)) \ h'(s_{c_j^v}(t)) \sum_{k: k \text{ output unit}} w_{kc_j^v} e_k(t) .
$$

We obtain for $l = in_j$ or $l = c_j^v,\ v = 1, \ldots, S_j$

$$
-\frac{\partial E(t)}{\partial w_{lm}} = \sum_{v=1}^{S_j} e_{s_{c_j^v}}(t) \frac{\partial s_{c_j^v}(t)}{\partial w_{lm}} .
$$

The derivatives of the internal states with respect to weights and the corresponding weight updates are as follows (compare expression (14)):

$$
l = in_j \ (\text{input gates}) :
$$

$$
\frac{\partial s_{c_j^v}(t)}{\partial w_{in_j m}} = \frac{\partial s_{c_j^v}(t-1)}{\partial w_{in_j m}} + g(net_{c_j^v}(t)) \ f'_{in_j}(net_{in_j}(t)) \ y^m(t-1) ;
$$

therefore time $t$'s contribution to $w_{in_j m}$'s update is (compare expression (10)):

$$
\Delta w_{in_j m}(t) = \alpha \sum_{v=1}^{S_j} e_{s_{c_j^v}}(t) \frac{\partial s_{c_j^v}(t)}{\partial w_{in_j m}} .
$$

Similarly we get (compare expression (14)):

$$
l = c_j^v \ (\text{memory cells}) :
$$

$$
\frac{\partial s_{c_j^v}(t)}{\partial w_{c_j^v m}} = \frac{\partial s_{c_j^v}(t-1)}{\partial w_{c_j^v m}} + g'(net_{c_j^v}(t)) \ f_{in_j}(net_{in_j}(t)) \ y^m(t-1) ;
$$

therefore time $t$'s contribution to $w_{c_j^v m}$'s update is (compare expression (10)):

$$
\Delta w_{c_j^v m}(t) = \alpha e_{s_{c_j^v}}(t) \frac{\partial s_{c_j^v}(t)}{\partial w_{c_j^v m}} .
$$

All we need to implement for the backward pass are equations (19), (20), (21), (22), (23), (25), (26), (27), (28). Each weight's total update is the sum of the contributions of all time steps.

**Computational complexity.** LSTM's update complexity per time step is

$$
O(KH + KCS + HI + CSI) = O(W),
$$

where $K$ is the number of output units, $C$ is the number of memory cell blocks, $S > 0$ is the size of the memory cell blocks, $H$ is the number of hidden units, $I$ is the (maximal) number of units forward-connected to memory cells, gate units and hidden units, and

$$
W = KH + KCS + CSI + 2CI + HI = O(KH + KCS + CSI + HI)
$$

is the number of weights. Expression (29) is obtained by considering all computations of the backward pass: equation (19) needs $K$ steps; (20) needs $KH$ steps; (21) needs $KSC$ steps; (22) needs $K(H + C)$ steps for output units, $HI$ steps for hidden units, $CI$ steps for output gates; (23) needs $KCS$ steps; (25) needs $CSI$ steps; (26) needs $CSI$ steps; (27) needs $CSI$ steps; (28) needs $CSI$ steps. The total is $K + 2KH + KC + 2KSC + HI + CI + 4CSI$ steps, or $O(KH + KSC + HI + CSI)$ steps. We conclude: LSTM algorithm’s update complexity per time step is just like BPTT’s for a fully recurrent net.

At a given time step, only the $2CSI$ most recent $\frac{\partial s_{cv}}{\partial w_{lm}}$ values from equations (25) and (27) need to be stored. Hence LSTM’s storage complexity also is $O(W)$ — it does not depend on the input sequence length.

A.2 ERROR FLOW

We compute how much an error signal is scaled while flowing back through a memory cell for $q$ time steps. As a by-product, this analysis reconfirms that the error flow within a memory cell’s CEC is indeed constant, provided that truncated backprop cuts off error flow trying to leave memory cells (see also Section 3.2). The analysis also highlights a potential for undesirable long-term drifts of $s_{cj}$ (see (2) below), as well as the beneficial, countermanding influence of negatively biased input gates (see (3) below).

Using the truncated backprop learning rule, we obtain

$$
1 + \frac{\partial y^{in_j}(t-k)}{\partial s_{cj}(t-k-1)} g\left(net_{cj}(t-k)\right) + y^{in_j}(t-k)g'\left(net_{cj}(t-k)\right)
$$

$$
1 + \sum_u \left[ \frac{\partial y^{in_j}(t-k)}{\partial y^u(t-k-1)} \frac{\partial y^u(t-k-1)}{\partial s_{cj}(t-k-1)} \right] g\left(net_{cj}(t-k)\right)
$$

$$
y^{in_j}(t-k)g'\left(net_{cj}(t-k)\right) \sum_u \left[ \frac{\partial net_{cj}(t-k)}{\partial y^u(t-k-1)} \frac{\partial y^u(t-k-1)}{\partial s_{cj}(t-k-1)} \right] \approx_{tr} 1.
$$

The $\approx_{tr}$ sign indicates equality due to the fact that truncated backprop replaces by zero the following derivatives: $\frac{\partial y^{in_j}(t-k)}{\partial y^u(t-k-1)} \forall u$ and $\frac{\partial net_{cj}(t-k)}{\partial y^u(t-k-1)} \forall u$.

In what follows, an error $\vartheta_j(t)$ starts flowing back at $c_j$'s output. We redefine

$$
\vartheta_j(t) := \sum_i w_{icj} \vartheta_i(t+1) .
$$

Following the definitions/conventions of Section 3.1, we compute error flow for the truncated backprop learning rule. The error occurring at the output gate is

$$
\vartheta_{out_j}(t) \approx_{tr} \frac{\partial y^{out_j}(t)}{\partial net_{out_j}(t)} \frac{\partial y^{cj}(t)}{\partial y^{out_j}(t)} \vartheta_j(t) .
$$

The error occurring at the internal state is

$$
\vartheta_{sc_j}(t) = \frac{\partial s_{cj}(t+1)}{\partial s_{cj}(t)} \vartheta_{sc_j}(t+1) + \frac{\partial y^{cj}(t)}{\partial s_{cj}(t)} \vartheta_j(t) .
$$

Since we use truncated backprop we have $\vartheta_j(t) = \sum_i, i$ no gate and no memory cell $w_{icj} \vartheta_i(t+1)$; therefore we get

$$
\frac{\partial \vartheta_j(t)}{\partial \vartheta_{sc_j}(t+1)} = \sum_i w_{icj} \frac{\partial \vartheta_i(t+1)}{\partial \vartheta_{sc_j}(t+1)} \approx_{tr} 0 .
$$

The previous equations (33) and (34) imply constant error flow through internal states of memory cells:

$$
\frac{\partial \vartheta_{s_{c_j}}(t)}{\partial \vartheta_{s_{c_j}}(t+1)} = \frac{\partial s_{c_j}(t+1)}{\partial s_{c_j}(t)} \approx_{tr} 1 .
$$

The error occurring at the memory cell input is

$$
\vartheta_{c_j}(t) = \frac{\partial g(net_{c_j}(t))}{\partial net_{c_j}(t)} \frac{\partial s_{c_j}(t)}{\partial g(net_{c_j}(t))} \vartheta_{s_{c_j}}(t) .
$$

The error occurring at the input gate is

$$
\vartheta_{in_j}(t) \approx_{tr} \frac{\partial y^{in_j}(t)}{\partial net_{in_j}(t)} \frac{\partial s_{c_j}(t)}{\partial y^{in_j}(t)} \vartheta_{s_{c_j}}(t) .
$$

No external error flow. Errors are propagated back from units $l$ to unit $v$ along outgoing connections with weights $w_{lv}$. This “external error” (note that for conventional units there is nothing but external error) at time $t$ is

$$
\vartheta_v^e(t) = \frac{\partial y^v(t)}{\partial net_v(t)} \sum_l \frac{\partial net_l(t+1)}{\partial y^v(t)} \vartheta_l(t+1) .
$$

We obtain

$$
\frac{\partial y^v(t-1)}{\partial net_v(t-1)} \left( \frac{\partial \vartheta_{out_j}(t)}{\partial \vartheta_j(t)} \frac{\partial net_{out_j}(t)}{\partial y^v(t-1)} + \frac{\partial \vartheta_{in_j}(t)}{\partial \vartheta_j(t)} \frac{\partial net_{in_j}(t)}{\partial y^v(t-1)} + \frac{\partial \vartheta_{c_j}(t)}{\partial \vartheta_j(t)} \frac{\partial net_{c_j}(t)}{\partial y^v(t-1)} \right) \approx_{tr} 0 .
$$

We observe: the error $\vartheta_j$ arriving at the memory cell output is *not* backpropagated to units $v$ via external connections to $in_j, out_j, c_j$.

**Error flow within memory cells.** We now focus on the error back flow within a memory cell’s CEC. This is actually the only type of error flow that can bridge several time steps. Suppose error $\vartheta_j(t)$ arrives at $c_j$’s output at time $t$ and is propagated back for $q$ steps until it reaches $in_j$ or the memory cell input $g(net_{c_j})$. It is scaled by a factor of $\frac{\partial \vartheta_v(t-q)}{\partial \vartheta_j(t)}$, where $v = in_j, c_j$. We first compute

$$
\frac{\partial \vartheta_{s_{c_j}}(t-q)}{\partial \vartheta_j(t)} \approx_{tr} \begin{cases}
\frac{\partial y^{c_j}(t)}{\partial s_{c_j}(t)} & q = 0 \\
\frac{\partial s_{c_j}(t-q+1)}{\partial s_{c_j}(t-q)} \frac{\partial \vartheta_{s_{c_j}}(t-q+1)}{\partial \vartheta_j(t)} & q > 0
\end{cases} .
$$

Expanding equation (40), we obtain

$$
\frac{\partial \vartheta_v(t-q)}{\partial \vartheta_j(t)} \approx_{tr} \frac{\partial \vartheta_v(t-q)}{\partial \vartheta_{s_{c_j}}(t-q)} \frac{\partial \vartheta_{s_{c_j}}(t-q)}{\partial \vartheta_j(t)} \approx_{tr}
$$

$$
\frac{\partial \vartheta_v(t-q)}{\partial \vartheta_{s_{c_j}}(t-q)} \left( \prod_{m=q}^1 \frac{\partial s_{c_j}(t-m+1)}{\partial s_{c_j}(t-m)} \right) \frac{\partial y^{c_j}(t)}{\partial s_{c_j}(t)} \approx_{tr}
$$

$$
y^{out_j}(t) h'(s_{c_j}(t)) \left\{ \begin{array}{ll}
g'(net_{c_j}(t-q)) y^{in_j}(t-q) & v = c_j \\
g(net_{c_j}(t-q)) f'_{in_j}(net_{in_j}(t-q)) & v = in_j
\end{array} \right. .
$$

Consider the factors in the previous equation’s last expression. Obviously, error flow is scaled only at times $t$ (when it enters the cell) and $t-q$ (when it leaves the cell), but not in between (constant error flow through the CEC). We observe:

(1) The output gate’s effect is: $y^{out_j}(t)$ scales down those errors that can be reduced early during training without using the memory cell. Likewise, it scales down those errors resulting from using (activating/deactivating) the memory cell at later training stages — without the output gate, the memory cell might for instance suddenly start causing avoidable errors in situations that already seemed under control (because it was easy to reduce the corresponding errors without memory cells). See “output weight conflict” and “abuse problem” in Sections 3/4.

(2) If there are large positive or negative $s_{c_j}(t)$ values (because $s_{c_j}$ has drifted since time step $t-q$), then $h'(s_{c_j}(t))$ may be small (assuming that $h$ is a logistic sigmoid). See Section 4. Drifts of the memory cell’s internal state $s_{c_j}$ can be countermanded by negatively biasing the input gate $in_j$ (see Section 4 and next point). Recall from Section 4 that the precise bias value does not matter much.

(3) $y^{in_j}(t-q)$ and $f'_{in_j}(net_{in_j}(t-q))$ are small if the input gate is negatively biased (assume $f_{in_j}$ is a logistic sigmoid). However, the potential significance of this is negligible compared to the potential significance of drifts of the internal state $s_{c_j}$.

Some of the factors above may scale down LSTM’s overall error flow, but not in a manner that depends on the length of the time lag. The flow will still be much more effective than an exponentially (of order $q$) decaying flow without memory cells.
