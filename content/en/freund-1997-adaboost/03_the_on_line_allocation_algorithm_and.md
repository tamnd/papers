---
paper: freund-1997-adaboost
title: A Decision-Theoretic Generalization of On-Line Learning and an Application to Boosting
authors:
  - Yoav Freund
  - Robert E. Schapire
year: 1997
venue: Journal of Computer and System Sciences
field: ai-ml
section: "2"
section_title: THE ON-LINE ALLOCATION ALGORITHM AND ITS ANALYSIS
tag: 04A2
kind: section
lang: en
source: https://doi.org/10.1006/jcss.1997.1504
pdf_sha256: 01f49de027c4c2c146869da85f8e8482d6b723344cb80ce957d11e93c615e7cc
pdf_pages: 2-5
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: f0a5a26ccba6806afef2da26423bb33b71dd2f15025f018a29334b00eac2e7e2
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

In this section, we present our algorithm, called Hedge($\beta$), for the on-line allocation problem. The algorithm and its analysis are direct generalizations of Littlestone and Warmuth’s weighted majority algorithm [20].

The pseudo-code for Hedge(β) is shown in Fig. 1. The algorithm maintains a weight vector whose value at time t is denoted $\mathbf{w}^t = \langle w_1^t, ..., w_N^t \rangle$. At all times, all weights will be nonnegative. All of the weights of the initial weight vector $\mathbf{w}^1$ must be nonnegative and sum to one, so that $\sum_{i=1}^N w_i^1 = 1$. Besides these conditions, the initial weight vector may be arbitrary, and may be viewed as a “prior” over the set of strategies. Since our bounds are strongest for those strategies receiving the greatest initial weight, we will want to choose the initial weights so as to give the most weight to those strategies which we expect are most likely to perform the best. Naturally, if we have no reason to favor any of the strategies, we can set all of the initial weights equally so that $w_i^1 = 1/N$. Note that the weights on future trials need not sum to one.

Our algorithm allocates among the strategies using the current weight vector, after normalizing. That is, at time t, Hedge(β) chooses the distribution vector

$$
\mathbf{p}^t = \frac{\mathbf{w}^t}{\sum_{i=1}^N w_i^t}.
$$

After the loss vector $\ell^t$ has been received, the weight vector $\mathbf{w}^t$ is updated using the multiplicative rule

$$
w_i^{t+1} = w_i^t \cdot \beta^{\ell_i^t}.
$$

More generally, it can be shown that our analysis is applicable with only minor modification to an alternative update rule of the form

$$
w_i^{t+1} = w_i^t \cdot U_\beta(\ell_i^t)
$$

where $U_\beta : [0, 1] \to [0, 1]$ is any function, parameterized by $\beta \in [0, 1]$ satisfying

$$
\beta^r \leq U_\beta(r) \leq 1 - (1 - \beta) r
$$

for all $r \in [0, 1]$.

### 2.1. Analysis {#freund-1997-adaboost-s2-1 .section tag=04A3}

The analysis of Hedge(β) mimics directly that given by Littlestone and Warmuth [20]. The main idea is to derive upper and lower bounds on $\sum_{i=1}^N w_i^{T+1}$ which, together, imply an upper bound on the loss of the algorithm. We begin with an upper bound.

Lemma 1. For any sequence of loss vectors $\ell^1, ..., \ell^T$, {#freund-1997-adaboost-lem-1 .statement tag=04A4}

$$
\ln \left( \sum_{i=1}^N w_i^{T+1} \right) \leq -(1-\beta) L_{\mathrm{Hedge}(\beta)}.
$$

Algorithm Hedge(β)
Parameters: $\beta \in [0, 1]$
initial weight vector $\mathbf{w}^1 \in [0, 1]^N$ with $\sum_{i=1}^N w_i^1 = 1$
number of trials $T$
Do for $t = 1, 2, ..., T$

1. Choose allocation

$$
\mathbf{p}' = \frac{\mathbf{w}'}{\sum_{i=1}^N w_i'}
$$

2. Receive loss vector $\ell' \in [0, 1]^N$ from environment.
3. Suffer loss $\mathbf{p}' \cdot \ell'$.
4. Set the new weights vector to be

$$
w_i^{t+1} = w_i^t \beta^{\ell_i^t}
$$

FIG. 1. The on-line allocation algorithm.

Proof. By a convexity argument, it can be shown that

$$
\alpha^r \leq 1 - (1 - \alpha) r
$$

for $\alpha \geq 0$ and $r \in [0, 1]$. Combined with Eqs. (1) and (2), this implies

$$
\begin{align*}
\sum_{i=1}^N w_i^{t+1} &= \sum_{i=1}^N w_i^t \beta^{\ell_i^t} \\
&\leq \sum_{i=1}^N w_i^t (1 - (1 - \beta) \ell_i^t) \\
&= \left( \sum_{i=1}^N w_i^t \right) (1 - (1 - \beta) \mathbf{p}^t \cdot \ell^t).
\end{align*}
$$

Applying repeatedly for $t = 1, ..., T$ yields

$$
\sum_{i=1}^N w_i^{T+1} \leq \prod_{t=1}^T (1 - (1 - \beta) \mathbf{p}^t \cdot \ell^t) \\
\leq \exp \left( - (1 - \beta) \sum_{t=1}^T \mathbf{p}^t \cdot \ell^t \right)
$$

since $1 + x \leq e^x$ for all $x$. The lemma follows immediately. □

Thus,

$$
L_{\mathrm{Hedge}(\beta)} \leq \frac{-\ln (\sum_{i=1}^N w_i^{T+1})}{1-\beta}.
$$

Note that, from Eq. (2),

$$
w_i^{T+1} = w_i^1 \prod_{t=1}^T \beta^{\ell_i^t} = w_i^1 \beta^{L_i}.
$$

This is all that is needed to complete our analysis.

THEOREM 2. For any sequence of loss vectors $\ell^1, ..., \ell^T$, and for any $i \in \{1, ..., N\}$, we have

$$
L_{\mathrm{Hedge}(\beta)} \leq \frac{-\ln(w_i^1) - L_i \ln \beta}{1 - \beta}.
$$

More generally, for any nonempty set $S \subseteq \{1, ..., N\}$, we have

$$
L_{\mathrm{Hedge}(\beta)} \leq \frac{-\ln(\sum_{i \in S} w_i^1) - (\ln \beta) \max_{i \in S} L_i}{1 - \beta}.
$$

Proof. We prove the more general statement (8) since Eq. (7) follows in the special case that $S = \{i\}$.

From Eq. (6),

$$
\begin{align*}
\sum_{i=1}^N w_i^{T+1} &\geq \sum_{i \in S} w_i^{T+1} \\
&= \sum_{i \in S} w_i^1 \beta^{L_i} \\
&\geq \beta^{\max_{i \in S} L_i} \sum_{i \in S} w_i^1.
\end{align*}
$$

The theorem now follows immediately from Eq. (5). □

The simpler bound (7) states that Hedge($\beta$) does not perform “too much worse” than the best strategy $i$ for the sequence. The difference in loss depends on our choice of $\beta$ and on the initial weight $w_i^1$ of each strategy. If each weight is set equally so that $w_i^1 = 1/N$, then this bound becomes

$$
L_{\mathrm{Hedge}(\beta)} \leq \frac{\min_i L_i \ln(1/\beta) + \ln N}{1 - \beta}.
$$

Since it depends only logarithmically on $N$, this bound is reasonable even for a very large number of strategies.

The more complicated bound (8) is a generalization of the simpler bound that is especially applicable when the number of strategies is infinite. Naturally, for uncountable collections of strategies, the sum appearing in Eq. (8) can be replaced by an integral, and the maximum by a supremum.

The bound given in Eq. (9) can be written as

$$
L_{\mathrm{Hedge}(\beta)} \leq c \min_i L_i + a \ln N,
$$

where $c = \ln(1/\beta)/(1 - \beta)$ and $a = 1/(1 - \beta)$. Vovk [24] analyzes prediction algorithms that have performance bounds of this form, and proves tight upper and lower bounds for the achievable values of $c$ and $a$. Using Vovk’s results, we can show that the constants $a$ and $c$ achieved by Hedge($\beta$) are optimal.

THEOREM 3. Let $B$ be an algorithm for the on-line allocation problem with an arbitrary number of strategies. Suppose that there exists positive real numbers $a$ and $c$ such that for any number of strategies $N$ and for any sequence of loss vectors $\ell^1, ..., \ell^T$

$$
L_B \leq c \min_i L_i + a \ln N.
$$

Then for all $\beta \in (0, 1)$, either

$$
c \geq \frac{\ln(1/\beta)}{1 - \beta} \quad \text{or} \quad a \geq \frac{1}{(1 - \beta)}.
$$

The proof is given in the appendix.

### 2.2. How to Choose $\beta$ {#freund-1997-adaboost-s2-2 .section tag=0859}

So far, we have analyzed Hedge($\beta$) for a given choice of $\beta$, and we have proved reasonable bounds for any choice of $\beta$. In practice, we will often want to choose $\beta$ so as to maximally exploit any prior knowledge we may have about the specific problem at hand.

The following lemma will be helpful for choosing $\beta$ using the bounds derived above.

LEMMA 4. Suppose $0 \leq L \leq \tilde{L}$ and $0 < R \leq \tilde{R}$. Let $\beta = g(\tilde{L}/\tilde{R})$ where $g(z) = 1/(1 + \sqrt{2/z})$. Then

$$
\frac{-L \ln \beta + R}{1 - \beta} \leq L + \sqrt{2 \tilde{L} \tilde{R}} + R.
$$

Proof. (Sketch) It can be shown that $-\ln \beta \leq (1 - \beta^2)/(2\beta)$ for $\beta \in (0, 1]$. Applying this approximation and the given choice of $\beta$ yields the result. □

Lemma 4 can be applied to any of the bounds above since all of these bounds have the form given in the lemma. For example, suppose we have $N$ strategies, and we also know a prior bound $\tilde{L}$ on the loss of the best strategy. Then, combining Eq. (9) and Lemma 4, we have {#freund-1997-adaboost-lem-4 .statement tag=085A}

$$
L_{\mathrm{Hedge}(\beta)} \leq \min_i L_i + \sqrt{2 \tilde{L} \ln N} + \ln N
$$

for $\beta = g(\tilde{L}/\ln N)$. In general, if we know ahead of time the number of trials $T$, then we can use $\tilde{L} = T$ as an upper bound on the cumulative loss of each strategy $i$.

Dividing both sides of Eq. (11) by $T$, we obtain an explicit bound on the rate at which the average per-trial loss of Hedge($\beta$) approaches the average loss for the best strategy:

$$
\frac{L_{\mathrm{Hedge}(\beta)}}{T} \leq \min_i \frac{L_i}{T} + \frac{\sqrt{2 \tilde{L} \ln N}}{T} + \frac{\ln N}{T}.
$$

Since $\tilde{L} \leq T$, this gives a worst case rate of convergence of $O(\sqrt{(\ln N)/T})$. However, if $\tilde{L}$ is close to zero, then the rate of convergence will be much faster, roughly, $O((\ln N)/T)$.

Lemma 4 can also be applied to the other bounds given in Theorem 2 to obtain analogous results. {#freund-1997-adaboost-lem-4-2 .statement tag=085B}

The bound given in Eq. (11) can be improved in special cases in which the loss is a function of a prediction and an outcome and this function is of a special form (see Example 4 below). However, for the general case, one cannot improve the square-root term $\sqrt{2\tilde{L} \ln N}$, by more than a constant factor. This is a corollary of the lower bound given by Cesa-Bianchi *et al.* ([4], Theorem 7) who analyze an on-line prediction problem that can be seen as a special case of the on-line allocation model.
