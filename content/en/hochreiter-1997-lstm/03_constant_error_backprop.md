---
paper: hochreiter-1997-lstm
title: Long Short-Term Memory
authors:
  - Sepp Hochreiter
  - Jurgen Schmidhuber
year: 1997
venue: Neural Computation
field: ai-ml
section: "3"
section_title: CONSTANT ERROR BACKPROP
tag: "0883"
kind: section
lang: en
source: doi:10.1162/neco.1997.9.8.1735
pdf_sha256: ceb9e53dbc0493f5b3bf5520ed940f3e6b526064d17b2118d77e51f79c0edcc6
pdf_pages: 3-6
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: ed610673f81daabeab757454759f99fd10ecb73342e148a0a5903d13f1968e97
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

### 3.1 EXPONENTIALLY DECAYING ERROR {#hochreiter-1997-lstm-s3-1 .section tag=0884}

Conventional BPTT (e.g. Williams and Zipser 1992). Output unit $k$'s target at time $t$ is denoted by $d_k(t)$. Using mean squared error, $k$'s error signal is

$$
\vartheta_k(t) = f'_k(net_k(t))(d_k(t) - y^k(t)),
$$

where

$$
y^i(t) = f_i(net_i(t))
$$

is the activation of a non-input unit $i$ with differentiable activation function $f_i$,

$$
net_i(t) = \sum_j w_{ij} y^j(t-1)
$$

is unit $i$'s current net input, and $w_{ij}$ is the weight on the connection from unit $j$ to $i$. Some non-output unit $j$'s backpropagated error signal is

$$
\vartheta_j(t) = f'_j(net_j(t)) \sum_i w_{ij} \vartheta_i(t+1).
$$

The corresponding contribution to $w_{jl}$'s total weight update is $\alpha \vartheta_j(t)y^l(t-1)$, where $\alpha$ is the learning rate, and $l$ stands for an arbitrary unit connected to unit $j$.

Outline of Hochreiter’s analysis (1991, page 19-21). Suppose we have a fully connected net whose non-input unit indices range from 1 to $n$. Let us focus on local error flow from unit $u$ to unit $v$ (later we will see that the analysis immediately extends to global error flow). The error occurring at an arbitrary unit $u$ at time step $t$ is propagated “back into time” for $q$ time steps, to an arbitrary unit $v$. This will scale the error by the following factor:

$$
\frac{\partial \vartheta_v(t-q)}{\partial \vartheta_u(t)} = \begin{cases}
f'_v(net_v(t-1))w_{uv} & q = 1 \\
f'_v(net_v(t-q)) \sum_{l=1}^n \frac{\partial \vartheta_l(t-q+1)}{\partial \vartheta_u(t)} w_{lv} & q > 1
\end{cases}.
$$

With $l_q = v$ and $l_0 = u$, we obtain:

$$
\frac{\partial \vartheta_v(t-q)}{\partial \vartheta_u(t)} = \sum_{l_1=1}^n \ldots \sum_{l_{q-1}=1}^n \prod_{m=1}^q f'_{l_m}(net_{l_m}(t-m)) w_{l_m l_{m-1}}
$$

(proof by induction). The sum of the $n^{q-1}$ terms $\prod_{m=1}^q f'_{l_m}(net_{l_m}(t-m)) w_{l_m l_{m-1}}$ determines the total error back flow (note that since the summation terms may have different signs, increasing the number of units $n$ does not necessarily increase error flow).

Intuitive explanation of equation (2). If

$$
|f'_{l_m}(net_{l_m}(t-m)) w_{l_m l_{m-1}}| > 1.0
$$

for all $m$ (as can happen, e.g., with linear $f_{l_m}$) then the largest product increases exponentially with $q$. That is, the error blows up, and conflicting error signals arriving at unit $v$ can lead to oscillating weights and unstable learning (for error blow-ups or bifurcations see also Pineda 1988, Baldi and Pineda 1991, Doya 1992). On the other hand, if

$$
|f'_{l_m}(net_{l_m}(t-m)) w_{l_m l_{m-1}}| < 1.0
$$

for all $m$, then the largest product *decreases* exponentially with $q$. That is, the error vanishes, and nothing can be learned in acceptable time.

If $f_{l_m}$ is the logistic sigmoid function, then the maximal value of $f'_{l_m}$ is 0.25. If $y^{l_{m-1}}$ is constant and not equal to zero, then $|f'_{l_m}(net_{l_m}) w_{l_m l_{m-1}}|$ takes on maximal values where

$$
w_{l_m l_{m-1}} = \frac{1}{y^{l_{m-1}}} \coth(\frac{1}{2} net_{l_m}),
$$

goes to zero for $|w_{l_m l_{m-1}}| \to \infty$, and is less than 1.0 for $|w_{l_m l_{m-1}}| < 4.0$ (e.g., if the absolute maximal weight value $w_{max}$ is smaller than 4.0). Hence with conventional logistic sigmoid activation functions, the error flow tends to vanish as long as the weights have absolute values below 4.0, especially in the beginning of the training phase. In general the use of larger initial weights will not help though — as seen above, for $|w_{l_m l_{m-1}}| \to \infty$ the relevant derivative goes to zero “faster” than the absolute weight can grow (also, some weights will have to change their signs by crossing zero). Likewise, increasing the learning rate does not help either — it will not change the ratio of long-range error flow and short-range error flow. BPTT is too sensitive to recent distractions. (A very similar, more recent analysis was presented by Bengio et al. 1994).

Global error flow. The local error flow analysis above immediately shows that global error flow vanishes, too. To see this, compute

$$
\sum_{u: \text{ u output unit}} \frac{\partial \vartheta_v(t-q)}{\partial \vartheta_u(t)}.
$$

Weak upper bound for scaling factor. The following, slightly extended vanishing error analysis also takes $n$, the number of units, into account. For $q > 1$, formula (2) can be rewritten as

$$
(W_{u^T})^T F'(t-1) \prod_{m=2}^{q-1} (WF'(t-m)) W_v f'_v(net_v(t-q)),
$$

where the weight matrix $W$ is defined by $[W]_{ij} := w_{ij}$, $v$'s outgoing weight vector $W_v$ is defined by $[W_v]_i := [W]_{iv} = w_{iv}$, $u$'s incoming weight vector $W_{u^T}$ is defined by $[W_{u^T}]_i := [W]_{ui} = w_{ui}$, and for $m = 1, \ldots, q$, $F'(t-m)$ is the diagonal matrix of first order derivatives defined as: $[F'(t-m)]_{ij} := 0$ if $i \neq j$, and $[F'(t-m)]_{ij} := f'_i(net_i(t-m))$ otherwise. Here $T$ is the transposition operator, $[A]_{ij}$ is the element in the $i$-th column and $j$-th row of matrix $A$, and $[x]_i$ is the $i$-th component of vector $x$.

Using a matrix norm $\| \cdot \|_A$ compatible with vector norm $\| \cdot \|_x$, we define

$$
f'_{max} := \max_{m=1,\ldots,q} \{ \| F'(t-m) \|_A \}.
$$

For $\max_{i=1,\ldots,n} \{ |x_i| \} \leq \| x \|_x$ we get $|x^T y| \leq n \| x \|_x \| y \|_x$. Since

$$
|f'_v(net_v(t-q))| \leq \| F'(t-q) \|_A \leq f'_{max},
$$

we obtain the following inequality:

$$
\left| \frac{\partial \vartheta_v(t-q)}{\partial \vartheta_u(t)} \right| \leq n (f'_{max})^q \| W_v \|_x \| W_{u^T} \|_x \| W \|_A^{q-2} \leq n (f'_{max} \| W \|_A)^q.
$$

This inequality results from

$$
\| W_v \|_x = \| We_v \|_x \leq \| W \|_A \| e_v \|_x \leq \| W \|_A
$$

and

$$
\| W_{u^T} \|_x = \| e_u W \|_x \leq \| W \|_A \| e_u \|_x \leq \| W \|_A,
$$

where $e_k$ is the unit vector whose components are 0 except for the $k$-th component, which is 1. Note that this is a weak, extreme case upper bound — it will be reached only if all $\| F'(t-m) \|_A$ take on maximal values, and if the contributions of all paths across which error flows back from unit $u$ to unit $v$ have the same sign. Large $\| W \|_A$, however, typically result in small values of $\| F'(t-m) \|_A$, as confirmed by experiments (see, e.g., Hochreiter 1991).

For example, with norms

$$
\| W \|_A := \max_r \sum_s |w_{rs}|
$$

and

$$
\| x \|_x := \max_r |x_r|,
$$

we have $f'_{max} = 0.25$ for the logistic sigmoid. We observe that if

$$
|w_{ij}| \leq w_{max} < \frac{4.0}{n} \quad \forall i, j,
$$

then $\| W \|_A \leq nw_{max} < 4.0$ will result in exponential decay — by setting $\tau := (\frac{nw_{max}}{4.0}) < 1.0$, we obtain

$$
\left| \frac{\partial \vartheta_v(t-q)}{\partial \vartheta_u(t)} \right| \leq n (\tau)^q.
$$

We refer to Hochreiter’s 1991 thesis for additional results.

### 3.2 CONSTANT ERROR FLOW: NAIVE APPROACH {#hochreiter-1997-lstm-s3-2 .section tag=0885}

A single unit. To avoid vanishing error signals, how can we achieve constant error flow through a single unit $j$ with a single connection to itself? According to the rules above, at time $t$, $j$'s local error back flow is $\vartheta_j(t) = f'_j(net_j(t)) \vartheta_j(t+1) w_{jj}$. To enforce *constant* error flow through $j$, we require

$$
f'_j(net_j(t)) w_{jj} = 1.0.
$$

Note the similarity to Mozer’s fixed time constant system (1992) — a time constant of 1.0 is appropriate for potentially infinite time lags¹.

The constant error carrousel. Integrating the differential equation above, we obtain $f_j(net_j(t)) = \frac{net_j(t)}{w_{jj}}$ for arbitrary $net_j(t)$. This means: $f_j$ has to be linear, and unit $j$'s activation has to remain constant:

$$
y_j(t+1) = f_j(net_j(t+1)) = f_j(w_{jj} y^j(t)) = y^j(t).
$$

¹ We do not use the expression “time constant” in the differential sense, as, e.g., Pearlmutter (1995).

In the experiments, this will be ensured by using the identity function $f_j : f_j(x) = x, \forall x$, and by setting $w_{jj} = 1.0$. We refer to this as the constant error carrousel (CEC). CEC will be LSTM’s central feature (see Section 4).

Of course unit $j$ will not only be connected to itself but also to other units. This invokes two obvious, related problems (also inherent in all other gradient-based approaches):

1. Input weight conflict: for simplicity, let us focus on a single additional input weight $w_{ji}$. Assume that the total error can be reduced by switching on unit $j$ in response to a certain input, and keeping it active for a long time (until it helps to compute a desired output). Provided $i$ is non-zero, since the same incoming weight has to be used for both storing certain inputs *and* ignoring others, $w_{ji}$ will often receive conflicting weight update signals during this time (recall that $j$ is linear): these signals will attempt to make $w_{ji}$ participate in (1) storing the input (by switching on $j$) *and* (2) protecting the input (by preventing $j$ from being switched off by irrelevant later inputs). This conflict makes learning difficult, and calls for a more context-sensitive mechanism for controlling “write operations” through input weights.

2. Output weight conflict: assume $j$ is switched on and currently stores some previous input. For simplicity, let us focus on a single additional outgoing weight $w_{kj}$. The same $w_{kj}$ has to be used for both retrieving $j$’s content at certain times *and* preventing $j$ from disturbing $k$ at other times. As long as unit $j$ is non-zero, $w_{kj}$ will attract conflicting weight update signals generated during sequence processing: these signals will attempt to make $w_{kj}$ participate in (1) accessing the information stored in $j$ *and* — at different times — (2) protecting unit $k$ from being perturbed by $j$. For instance, with many tasks there are certain “short time lag errors” that can be reduced in early training stages. However, at later training stages $j$ may suddenly start to cause avoidable errors in situations that already seemed under control by attempting to participate in reducing more difficult “long time lag errors”. Again, this conflict makes learning difficult, and calls for a more context-sensitive mechanism for controlling “read operations” through output weights.

Of course, input and output weight conflicts are not specific for long time lags, but occur for short time lags as well. Their effects, however, become particularly pronounced in the long time lag case: as the time lag increases, (1) stored information must be protected against perturbation for longer and longer periods, and — especially in advanced stages of learning — (2) more and more already correct outputs also require protection against perturbation.

Due to the problems above the naive approach does not work well except in case of certain simple problems involving local input/output representations and non-repeating input patterns (see Hochreiter 1991 and Silva et al. 1996). The next section shows how to do it right.
