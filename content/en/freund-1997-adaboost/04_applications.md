---
paper: freund-1997-adaboost
title: A Decision-Theoretic Generalization of On-Line Learning and an Application to Boosting
authors:
  - Yoav Freund
  - Robert E. Schapire
year: 1997
venue: Journal of Computer and System Sciences
field: ai-ml
section: "3"
section_title: APPLICATIONS
tag: 085C
kind: section
lang: en
source: https://doi.org/10.1006/jcss.1997.1504
pdf_sha256: 01f49de027c4c2c146869da85f8e8482d6b723344cb80ce957d11e93c615e7cc
pdf_pages: 5-6
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 6d96f769370c8245744c00015bc9711bc1b2ba494bccb15599f805c4a71a4530
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The framework described up to this point is quite general and can be applied in a wide variety of learning problems.

Consider the following set-up used by Chung [5]. We are given a decision space $\Delta$, a space of outcomes $\Omega$, and a bounded loss function $\lambda : \Delta \times \Omega \to [0, 1]$. (Actually, our results require only that $\lambda$ be bounded, but, by rescaling, we can assume that its range is $[0, 1]$.) At every time step $t$, the learning algorithm selects a decision $\delta^t \in \Delta$, receives an outcome $\omega^t \in \Omega$, and suffers loss $\lambda(\delta^t, \omega^t)$. More generally, we may allow the learner to select a distribution $\mathcal{D}^t$ over the space of decisions, in which case it suffers the expected loss of a decision randomly selected according to $\mathcal{D}^t$; that is, its expected loss is $\Lambda(\mathcal{D}^t, \omega^t)$ where

$$
\Lambda(\mathcal{D}, \omega) = E_{\delta \sim \mathcal{D}}[\lambda(\delta, \omega)].
$$

To decide on distribution $\mathcal{D}^t$, we assume that the learner has access to a set of $N$ experts. At every time step $t$, expert $i$ produces its own distribution $\mathcal{E}_i^{t}$ on $\Delta$, and suffers loss $\Lambda(\mathcal{E}_i^{t}, \omega^t)$.

The goal of the learner is to combine the distributions produced by the experts so as to suffer expected loss “not much worse” than that of the best expert.

The results of Section 2 provide a method for solving this problem. Specifically, we run algorithm Hedge($\beta$), treating each expert as a strategy. At every time step, Hedge($\beta$) produces a distribution $p^t$ on the set of experts which is used to construct the mixture distribution

$$
\mathcal{D}^t = \sum_{i=1}^N p_i^t \mathcal{E}_i^t.
$$

For any outcome $\omega^t$, the loss suffered by Hedge($\beta$) will then be

$$
\Lambda(\mathcal{D}^t, \omega^t) = \sum_{i=1}^N p_i^t \Lambda(\mathcal{E}_i^t, \omega^t).
$$

Thus, if we define $\ell_i^t = \Lambda(\mathcal{E}_i^t, \omega^t)$ then the loss suffered by the learner is $p^t \cdot \ell^t$, i.e., exactly the mixture loss that was analyzed in Section 2.

Hence, the bounds of Section 2 can be applied to our current framework. For instance, applying Eq. (11), we obtain the following:

**Theorem 5.** *For any loss function $\lambda$, for any set of experts, and for any sequence of outcomes, the expected loss of Hedge($\beta$) if used as described above is at most* {#freund-1997-adaboost-thm-5 .statement tag=085D}

$$
\sum_{t=1}^T \Lambda(\mathcal{D}^t, \omega^t) \leq \min_i \sum_{t=1}^T \Lambda(\mathcal{E}_i^t, \omega^t) + \sqrt{2\tilde{L} \ln N} + \ln N
$$

*where $\tilde{L} \leq T$ is an assumed bound on the expected loss of the best expert, and $\beta = g(\tilde{L}/\ln N)$.*

Example 1. In the $k$-ary prediction problem, $\Delta = \Omega = \{1, 2, ..., k\}$, and $\lambda(\delta, \omega)$ is 1 if $\delta \neq \omega$ and 0 otherwise. In other words, the problem is to predict a sequence of letters over an alphabet of size $k$. The loss function $\lambda$ is 1 if a mistake was made, and 0 otherwise. Thus, $\Lambda(\mathcal{D}, \omega)$ is the probability (with respect to $\mathcal{D}$) of a prediction that disagrees with $\omega$. The cumulative loss of the learner, or of any expert, is therefore the expected number of mistakes on the entire sequence. So, in this case, Theorem 2 states that the expected number of mistakes of the learning algorithm will exceed the expected number of mistakes of the best expert by at most $O(\sqrt{T \ln N})$, or possibly much less if the loss of the best expert can be bounded ahead of time. {#freund-1997-adaboost-ex-1 .statement tag=085E}

Bounds of this type were previously proved in the binary case ($k = 2$) by Littlestone and Warmuth [20] using the same algorithm. Their algorithm was later improved by Vovk [25] and Cesa-Bianchi *et al.* [4]. The main result of this section is a proof that such bounds can be shown to hold for any bounded loss function.

Example 2. The loss function $\lambda$ may represent an arbitrary matrix game, such as “rock, paper, scissors.” Here, $\Delta = \Omega = \{R, P, S\}$, and the loss function is defined by the matrix: {#freund-1997-adaboost-ex-2 .statement tag=085F}

$$
\begin{array}{ccc}
 & \omega \\
 & R & P & S \\
\delta & R & \frac{1}{2} & 1 & 0 \\
 & P & 0 & \frac{1}{2} & 1 \\
 & S & 1 & 0 & \frac{1}{2}
\end{array}
$$

The decision $\delta$ represents the learner’s play, and the outcome $\omega$ is the adversary’s play; then $\lambda(\delta, \omega)$, the learner’s loss, is 1 if the learner loses the round, 0 if it wins the round, and 1/2 if the round is tied. (For instance, $\lambda(S, P) = 0$ since “scissors cut paper.”) So the cumulative loss of the learner

(or an expert) is the expected number of losses in a series of rounds of game play (counting ties as half a loss). Our results show then that, in repeated play, the expected number of rounds lost by our algorithm will converge quickly to the expected number that would have been lost by the best of the experts (for the particular sequence of moves that were actually played by the adversary).

Example 3. Suppose that $\Delta$ and $\Omega$ are finite, and that $\lambda$ represents a game matrix as in the last example. Suppose further that we create one expert for each decision $\delta \in \Delta$ and that expert always recommends playing $\delta$. In game-theoretic terminology such experts would be identified with *pure* strategies. Von Neumann’s classical min-max theorem states that for any fixed game matrix there exists a distribution over the actions, also called a *mixed* strategy, which achieves the min-max optimal value of the expected loss against *any* adversarial strategy. This min-max value is also called the *value of the game*. {#freund-1997-adaboost-ex-3 .statement tag=0860}

Suppose that we use algorithm **Hedge**($\beta$) to choose distributions over the actions when playing a matrix game repeatedly. In this case, Theorem 2 implies that the gap between the learner’s average per-round loss can never be much larger than that of the best pure strategy, and that the maximal gap decreases to zero at the rate $O(1/\sqrt{T \log |\Delta|})$. However, the expected loss of the optimal mixed strategy is a fixed convex combination of the losses of the pure strategies, thus it can never be smaller than the loss of the *best* pure strategy for a particular sequence of events. We conclude that the expected per-trial loss of **Hedge**($\beta$) is upper bounded by the value of the game plus $O(1/\sqrt{T \log |\Delta|})$. In other words, the algorithm can never perform much worse that an algorithm that uses the optimal mixed strategy for the game, and it can be better if the adversary does not play optimally. Moreover, this holds true even if the learner knows nothing at all about the game that is being played (so that $\lambda$ is unknown to the learner), and even if the adversarial opponent has complete knowledge both of the game that is being played and the algorithm that is being used by the learner. Algorithms with similar properties (but weaker convergence bounds) were first devised by Blackwell [2] and Hannan [14]. For more details see our related paper [13].

Example 4. Suppose that $\Delta = \Omega$ is the unit ball in $\mathbb{R}^n$, and that $\lambda(\delta, \omega) = \| \delta - \omega \|$. Thus, the problem here is to predict the location of a point $\omega$, and the loss suffered is the Euclidean distance between the predicted point $\delta$ and the actual outcome $\omega$. Theorem 2 can be applied if probabilistic predictions are allowed. However, in this setting it is more natural to require that the learner and each expert predict a single point (rather than a measure on the space of possible points). Essentially, this is the problem of “tracking” a sequence of points $\omega^1, ..., \omega^T$ where the loss function measures the distance to the predicted point. {#freund-1997-adaboost-ex-4 .statement tag=0861}

To see how to handle the problem of finding deterministic predictions, notice that the loss function $\lambda(\delta, \omega)$ is convex with respect to $\delta$:

$$
\|(a \delta_1 + (1-a) \delta_2) - \omega\| \leq a \|\delta_1 - \omega\| + (1-a)\|\delta_2 - \omega\|
$$

for any $a \in [0, 1]$ and any $\omega \in \Omega$. Thus we can do as follows. At time $t$, the learner predicts with the weighted average of the experts’ predictions: $\delta^t = \sum_{i=1}^N p_i^t \varepsilon_i^t$ where $\varepsilon_i^t \in \mathbb{R}^n$ is the prediction of the $i$th expert at time $t$. Regardless of the outcome $\omega^t$, Eq. (13) implies that

$$
\|\delta^t - \omega^t\| \leq \sum_{i=1}^N p_i^t \|\varepsilon_i^t - \omega^t\|.
$$

Since Theorem 2 provides an upper bound on the right hand side of this inequality, we also obtain upper bounds for the left hand side. Thus, our results in this case give explicit bounds on the total error (i.e., distance between predicted and observed points) for the learner relative to the best of a team of experts.

In the one-dimensional case ($n = 1$), this case was previously analyzed by Littlestone and Warmuth [20], and later improved upon by Kivinen and Warmuth [19].

This result depends only on the convexity and the bounded range of the loss function $\lambda(\delta, \omega)$ with respect to $\delta$. Thus, it can also be applied, for example, to the squared-distance loss function $\lambda(\delta, \omega) = \| \delta - \omega \|^2$, as well as the log loss function $\lambda(\delta, \omega) = -\ln(\delta \cdot \omega)$ used by Cover [6] for the design of “universal” investment portfolios. (In this last case, $\Delta$ is the set of probability vectors on $n$ points, and $\Omega = [1/B, B]^n$ for some constant $B > 1$.)

In many of the cases listed above, superior algorithms or analyses are known. Although weaker in specific cases, it should be emphasized that our results are far more general, and can be applied in settings that exhibit considerably less structure, such as the horse-racing example described in the introduction.
