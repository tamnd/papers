---
paper: freund-1997-adaboost
title: A Decision-Theoretic Generalization of On-Line Learning and an Application to Boosting
authors:
  - Yoav Freund
  - Robert E. Schapire
year: 1997
venue: Journal of Computer and System Sciences
field: ai-ml
section: "4"
section_title: BOOSTING
tag: "0862"
kind: section
lang: en
source: https://doi.org/10.1006/jcss.1997.1504
pdf_sha256: 01f49de027c4c2c146869da85f8e8482d6b723344cb80ce957d11e93c615e7cc
pdf_pages: 6-8
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: d9daa55f17ca008d933f70612519d9f9b89669522e256ad2dc06a079165a4162
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

In this section we show how the algorithm presented in Section 2 for the on-line allocation problem can be modified to boost the performance of weak learning algorithms.

We very briefly review the PAC learning model (see, for instance, Kearns and Vazirani [18] for a more detailed description). Let $X$ be a set called the *domain*. A *concept* is a Boolean function $c : X \to \{0, 1\}$. A *concept class* $\mathcal{C}$ is a collection of concepts. The learner has access to an oracle which provides labelled examples of the form $(x, c(x))$ where $x$ is chosen randomly according to some fixed but unknown and arbitrary distribution $\mathcal{D}$ on the domain $X$, and $c \in \mathcal{C}$ is the target concept. After some amount of time, the learner must output a hypothesis $h : X \to [0, 1]$. The value $h(x)$ can be interpreted as a randomized prediction of the label of $x$ that is 1 with probability $h(x)$ and 0 with probability $1 - h(x)$. (Although we assume here that we have direct access to the bias of this prediction, our results can be extended to the case that $h$ is instead a random mapping into $\{0, 1\}$.) The error of the hypothesis $h$ is the expected value $E_{x \sim \mathcal{D}}(|h(x) - c(x)|)$ where $x$ is chosen according to $\mathcal{D}$. If $h(x)$ is interpreted as a stochastic prediction, then this is simply the probability of an incorrect prediction.

A strong PAC-learning algorithm is an algorithm that, given $\varepsilon, \delta > 0$ and access to random examples, outputs with probability $1 - \delta$ a hypothesis with error at most $\varepsilon$. Further, the running time must be polynomial in $1/\varepsilon, 1/\delta$ and other relevant parameters (namely, the “size” of the examples received, and the “size” or “complexity” of the target concept). A weak PAC-learning algorithm satisfies the same conditions but only for $\varepsilon \geq 1/2 - \gamma$ where $\gamma > 0$ is either a constant, or decreases as $1/p$ where $p$ is a polynomial in the relevant parameters. We use WeakLearn to denote a generic weak learning algorithm.

Schapire [22] showed that any weak learning algorithm can be efficiently transformed or “boosted” into a strong learning algorithm. Later, Freund [10, 11] presented the “boost-by-majority” algorithm that is considerably more efficient than Schapire’s. Both algorithms work by calling a given weak learning algorithm WeakLearn multiple times, each time presenting it with a different distribution over the domain $X$, and finally combining all of the generated hypotheses into a single hypothesis. The intuitive idea is to alter the distribution over the domain $X$ in a way that increases the probability of the “harder” parts of the space, thus forcing the weak learner to generate new hypotheses that make less mistakes on these parts.

An important, practical deficiency of the boost-by-majority algorithm is the requirement that the bias $\gamma$ of the weak learning algorithm WeakLearn be known ahead of time. Not only is this worst-case bias usually unknown in practice, but the bias that can be achieved by WeakLearn will typically vary considerably from one distribution to the next. Unfortunately, the boost-by-majority algorithm cannot take advantage of hypotheses computed by WeakLearn with error significantly smaller than the presumed worst-case bias of $1/2 - \gamma$.

In this section, we present a new boosting algorithm which was derived from the on-line allocation algorithm of Section 2. This new algorithm is very nearly as efficient as boost-by-majority. However, unlike boost-by-majority, the accuracy of the final hypothesis produced by the new algorithm depends on the accuracy of all the hypotheses returned by WeakLearn, and so is able to more fully exploit the power of the weak learning algorithm.

Also, this new algorithm gives a clean method for handling real-valued hypotheses which often are produced by neural networks and other learning algorithms.

### 4.1. The New Boosting Algorithm {#freund-1997-adaboost-s4-1 .section tag=0863}

Although boosting has its roots in the PAC model, for the remainder of the paper, we adopt a more general learning framework in which the learner receives examples $(x_i, y_i)$ chosen randomly according to some fixed but unknown distribution $\mathcal{P}$ on $X \times Y$, where $Y$ is a set of possible labels. As usual, the goal is to learn to predict the label $y$ given an instance $x$.

We start by describing our new boosting algorithm in the simplest case that the label set $Y$ consists of just two possible labels, $Y = \{0, 1\}$. In later sections, we give extensions of the algorithm for more general label sets.

Freund [11] describes two frameworks in which boosting can be applied: boosting by filtering and boosting by sampling. In this paper, we use the boosting by sampling framework, which is the natural framework for analyzing “batch” learning, i.e., learning using a fixed training set which is stored in the computer’s memory.

We assume that a sequence of $N$ training examples (labelled instances) $(x_1, y_1), ..., (x_N, y_N)$ is drawn randomly from $X \times Y$ according to distribution $\mathcal{P}$. We use boosting to find a hypothesis $h_f$ which is consistent with most of the sample (i.e., $h_f(x_i) = y_i$ for most $1 \leq i \leq N$). In general, a hypothesis which is accurate on the training set might not be accurate on examples outside the training set; this problem is sometimes referred to as “over-fitting.” Often, however, overfitting can be avoided by restricting the hypothesis to be simple. We will come back to this problem in Section 4.3.

The new boosting algorithm is described in Fig. 2. The goal of the algorithm is to find a final hypothesis with low error relative to a given distribution $D$ over the training examples. Unlike the distribution $\mathcal{P}$ which is over $X \times Y$ and is set by “nature,” the distribution $D$ is only over the instances in the training set and is controlled by the learner. Ordinarily, this distribution will be set to be uniform so that $D(i) = 1/N$. The algorithm maintains a set of weights $w^t$ over the training examples. On iteration $t$ a distribution $p^t$ is computed by normalizing these weights. This distribution is fed to the weak learner WeakLearn which generates a hypothesis $h_t$ that (we hope) has small error with respect to the distribution.\footnote{Some learning algorithms can be generalized to use a given distribution directly. For instance, gradient based algorithms can use the probability associated with each example to scale the update step size which is based on the example. If the algorithm cannot be generalized in this way, the training sample can be re-sampled to generate a new set of training examples that is distributed according to the given distribution. The computation required to generate each re-sampled example takes $O(\log N)$ time.} Using the new hypothesis $h_t$, the boosting

Algorithm AdaBoost
Input: sequence of N labeled examples $\langle (x_1, y_1), ..., (x_N, y_N) \rangle$
    distribution D over the N examples
    weak learning algorithm WeakLearn
    integer T specifying number of iterations
Initialize the weight vector: $w_i^1 = D(i)$ for $i = 1, ..., N$.
Do for $t = 1, 2, ..., T$

1. Set

$$
\mathbf{p}' = \frac{\mathbf{w}'}{\sum_{i=1}^N w_i'}
$$

2. Call WeakLearn, providing it with the distribution $\mathbf{p}'$; get back a hypothesis $h_t : X \to [0, 1]$.

3. Calculate the error of $h_t$: $\varepsilon_t = \sum_{i=1}^N p_i' |h_t(x_i) - y_i|$.

4. Set $\beta_t = \varepsilon_t / (1 - \varepsilon_t)$.
