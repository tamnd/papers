---
paper: freund-1997-adaboost
title: A Decision-Theoretic Generalization of On-Line Learning and an Application to Boosting
authors:
  - Yoav Freund
  - Robert E. Schapire
year: 1997
venue: Journal of Computer and System Sciences
field: ai-ml
section: "5"
section_title: Set the new weights vector to be
tag: "0864"
kind: section
lang: en
source: https://doi.org/10.1006/jcss.1997.1504
pdf_sha256: 01f49de027c4c2c146869da85f8e8482d6b723344cb80ce957d11e93c615e7cc
pdf_pages: 8-20
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 59a1087c65cb49b05ac154f78bb65639990a56553350f469bf3090ae51736ac6
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

$$
w_i^{t+1} = w_i^t \beta_t^{1 - |h_t(x_i) - y_i|}
$$

Output the hypothesis

$$
h_f(x) = \begin{cases}
1 & \text{if } \sum_{t=1}^T (\log 1/\beta_t) h_t(x) \geq \frac{1}{2} \sum_{t=1}^T \log 1/\beta_t \\
0 & \text{otherwise.}
\end{cases}
$$

FIG. 2. The adaptive boosting algorithm.

algorithm generates the next weight vector $\mathbf{w}^{t+1}$, and the process repeats. After T such iterations, the final hypothesis $h_f$ is output. The hypothesis $h_f$ combines the outputs of the T weak hypotheses using a weighted majority vote.

We call the algorithm AdaBoost because, unlike previous algorithms, it adjusts adaptively to the errors of the weak hypotheses returned by WeakLearn. If WeakLearn is a PAC weak learning algorithm in the sense defined above, then $\varepsilon_t \leq 1/2 - \gamma$ for all $t$ (assuming the examples have been generated appropriately with $y_i = c(x_i)$ for some $c \in \mathcal{C}$). However, such a bound on the error need not be known ahead of time. Our results hold for any $\varepsilon_t \in [0, 1]$, and depend only on the performance of the weak learner on those distributions that are *actually generated* during the boosting process.

The parameter $\beta_t$ is chosen as a function of $\varepsilon_t$ and is used for updating the weight vector. The update rule reduces the probability assigned to those examples on which the hypothesis makes a good prediction and increases the probability of the examples on which the prediction is poor.$^2$

Note that AdaBoost, unlike boost-by-majority, combines the weak hypotheses by summing their probabilistic predictions. Drucker, Schapire and Simard [9], in experiments they performed using boosting to improve the performance of a real-valued neural network, observed that summing the outcomes of the networks and then selecting the best prediction performs better than selecting the best prediction of each network and then combining them with a majority rule. It is interesting that the new boosting algorithm’s final hypothesis uses the same combination rule that was observed to be better in practice, but which previously lacked theoretical justification.

Since it was first introduced, several successful experiments have been conducted using AdaBoost, including work by the authors [12], Drucker and Cortes [8], Jackson and Craven [16], Quinlan [21], and Breiman [3].

4.2. *Analysis*

Comparing Figs. 1 and 2, there is an obvious similarity between the algorithms Hedge($\beta$) and AdaBoost. This similarity reflects a surprising “dual” relationship between the on-line allocation model and the problem of boosting. Put another way, there is a direct mapping or reduction of the boosting problem to the on-line allocation problem. In such a reduction, one might naturally expect a correspondence relating the strategies to the weak hypotheses and the trials (and associated loss vectors) to the examples in the training set. However, the reduction we have used is reversed: the “strategies” correspond to the examples, and the trials are associated with the weak hypotheses. Another reversal is in the definition of the loss: in Hedge($\beta$) the loss $\ell_i^t$ is small if the ith strategy suggests a *good* action on the tth trial while in AdaBoost the “loss” $\ell_i^t = 1 - |h_t(x_i) - y_i|$ appearing in the weight-update rule (Step 5) is small if the tth hypothesis suggests a *bad* prediction on the ith example. The reason is that in Hedge($\beta$) the weight associated with a strategy is increased if the strategy is successful while in AdaBoost the weight associated with an example is increased if the example is “hard.”

The main technical difference between the two algorithms is that in AdaBoost the parameter $\beta$ is no longer fixed ahead of time but rather changes at each iteration according to $\varepsilon_t$. If we are given ahead of time the information that $\varepsilon_t \leq 1/2 - \gamma$ for some $\gamma > 0$ and for all $t = 1, ..., T$, then we could instead directly apply algorithm Hedge($\beta$) and its analysis as follows: Fix $\beta$ to be $1 - \gamma$, and set $\ell_i^t = 1 - |h_t(x_i) - y_i|$, and $h_f$ as in AdaBoost, but with equal weight assigned to all T hypotheses. Then $\mathbf{p}' \cdot \ell^t$ is exactly the accuracy of $h_t$ on distribution $\mathbf{p}'$, which, by assumption, is at least $1/2 + \gamma$. Also, letting $S = \{ i : h_f(x_i) \neq y_i \}$, it is straightforward to show that if $i \in S$ then

$$
\frac{L_i}{T} = \frac{1}{T} \sum_{t=1}^T \ell_i^t = 1 - \frac{1}{T} \sum_{t=1}^T |y_i - h_t(x_i)| \\
= 1 - \left| y_i - \frac{1}{T} \sum_{t=1}^T h_t(x_i) \right| \leq 1/2
$$

$^2$ Furthermore, if $h_t$ is Boolean (with range $\{0, 1\}$), then it can be shown that this update rule exactly removes the advantage of the last hypothesis. That is, the error of $h_t$ on distribution $\mathbf{p}'^{t+1}$ is exactly 1/2.

by $h_f$'s definition, and since $y_i \in \{0, 1\}$. Thus, by Theorem 2,

$$
T \cdot (1/2 + \gamma) \leq \sum_{t=1}^T p^t \cdot \ell^t 
$$

$$
\leq \frac{-\ln(\sum_{i \in S} D(i)) + (\gamma + \gamma^2)(T/2)}{\gamma}
$$

since $-\ln(\beta) = -\ln(1-\gamma) \leq \gamma + \gamma^2$ for $\gamma \in [0, 1/2]$. This implies that the error $\varepsilon = \sum_{i \in S} D(i)$ of $h_f$ is at most $e^{-T\gamma^2/2}$.

The boosting algorithm **AdaBoost** has two advantages over this direct application of **Hedge($\beta$)**. First, by giving a more refined analysis and choice of $\beta$, we obtain a significantly superior bound on the error $\varepsilon$. Second, the algorithm does not require prior knowledge of the accuracy of the hypotheses that **WeakLearn** will generate. Instead, it measures the accuracy of $h_t$ at each iteration and sets its parameters accordingly. The update factor $\beta_t$ decreases with $\varepsilon_t$ which causes the difference between the distributions $p^t$ and $p^{t+1}$ to increase. Decreasing $\beta_t$ also increases the weight $\ln(1/\beta_t)$ which is associated with $h_t$ in the final hypothesis. This makes intuitive sense: more accurate hypotheses cause larger changes in the generated distributions and have more influence on the outcome of the final hypothesis.

We now give our analysis of the performance of **AdaBoost**. Note that this theorem applies also if, for some hypotheses, $\varepsilon_t \geq 1/2$.

**Theorem 6.** *Suppose the weak learning algorithm WeakLearn, when called by AdaBoost, generates hypotheses with errors $\varepsilon_1, ..., \varepsilon_T$ (as defined in Step 3 of Fig. 2.) Then the error $\varepsilon = \Pr_{i \sim D}[h_f(x_i) \neq y_i]$ of the final hypothesis $h_f$ output by AdaBoost is bounded above by* {#freund-1997-adaboost-thm-6 .statement tag=0865}

$$
\varepsilon \leq 2^T \prod_{t=1}^T \sqrt{\varepsilon_t (1-\varepsilon_t)}. \tag{14}
$$
{#freund-1997-adaboost-eq-14 .equation tag=0866}

*Proof.* We adapt the main arguments from Lemma 1 and Theorem 2. We use $p^t$ and $w^t$ as they are defined in Fig. 2.

Similar to Eq. (4), the update rule given in Step 5 in Fig. 2 implies that

$$
\sum_{i=1}^N w_i^{t+1} = \sum_{i=1}^N w_i^t \beta_t^{1-|h_t(x_i)-y_i|}
$$

$$
\leq \sum_{i=1}^N w_i^t (1-(1-\beta_t)(1-|h_t(x_i)-y_i|))
$$

$$
= \left( \sum_{i=1}^N w_i^t \right) (1-(1-\varepsilon_t)(1-\beta_t)). \tag{15}
$$
{#freund-1997-adaboost-eq-15 .equation tag=0867}

Combining this inequality over $t = 1, ..., T$, we get that

$$
\sum_{i=1}^N w_i^{T+1} \leq \prod_{t=1}^T (1-(1-\varepsilon_t)(1-\beta_t)). \tag{16}
$$
{#freund-1997-adaboost-eq-16 .equation tag=0868}

The final hypothesis $h_f$, as defined in Fig. 2, makes a mistake on instance $i$ only if

$$
\prod_{t=1}^T \beta_t^{-|h_t(x_i)-y_i|} \geq \left( \prod_{t=1}^T \beta_t \right)^{-1/2} \tag{17}
$$
{#freund-1997-adaboost-eq-17 .equation tag=0869}

(since $y_i \in \{0, 1\}$). The final weight of any instance $i$ is

$$
w_i^{T+1} = D(i) \prod_{t=1}^T \beta_t^{1-|h_t(x_i)-y_i|}. \tag{18}
$$
{#freund-1997-adaboost-eq-18 .equation tag=086A}

Combining Eqs. (17) and (18) we can lower bound the sum of the final weights by the sum of the final weights of the examples on which $h_f$ is incorrect:

$$
\sum_{i=1}^N w_i^{T+1} \geq \sum_{i: h_f(x_i) \neq y_i} w_i^{T+1}
$$

$$
\geq \left( \sum_{i: h_f(x_i) \neq y_i} D(i) \right) \left( \prod_{t=1}^T \beta_t \right)^{1/2}
$$

$$
= \varepsilon \cdot \left( \prod_{t=1}^T \beta_t \right)^{1/2} \tag{19}
$$
{#freund-1997-adaboost-eq-19 .equation tag=086B}

where $\varepsilon$ is the error of $h_f$. Combining Eqs. (16) and (19), we get that

$$
\varepsilon \leq \prod_{t=1}^T \frac{1-(1-\varepsilon_t)(1-\beta_t)}{\sqrt{\beta_t}}. \tag{20}
$$
{#freund-1997-adaboost-eq-20 .equation tag=086C}

As all the factors in the product are positive, we can minimize the right hand side by minimizing each factor separately. Setting the derivative of the $t$th factor to zero, we find that the choice of $\beta_t$ which minimizes the right hand side is $\beta_t = \varepsilon_t/(1-\varepsilon_t)$. Plugging this choice of $\beta_t$ into Eq. (20) we get Eq. (14), completing the proof. $\blacksquare$

The bound on the error given in Theorem 6, can also be written in the form

$$
\varepsilon \leq \prod_{t=1}^T \sqrt{1-4\gamma_t^2}
$$

$$
= \exp \left( -\sum_{t=1}^T \mathrm{KL}(1/2 \parallel 1/2-\gamma_t) \right)
$$

$$
\leq \exp \left( -2 \sum_{t=1}^T \gamma_t^2 \right) \tag{21}
$$
{#freund-1997-adaboost-eq-21 .equation tag=086D}

where $\mathrm{KL}(a \parallel b) = a \ln(a/b) + (1-a) \ln((1-a)/(1-b))$ is the Kullback–Leibler divergence, and where $\varepsilon_t$ has been replaced by $1/2 - \gamma_t$. In the case where the errors of all the hypotheses are equal to $1/2 - \gamma$, Eq. (21) simplifies to

$$
\varepsilon \leq (1 - 4\gamma^2)^{T/2}
$$

$$
= \exp(- T \cdot \mathrm{KL}(1/2 \parallel 1/2 - \gamma))
$$

$$
\leq \exp(- 2T\gamma^2).
$$

This is a form of the Chernoff bound for the probability that less than $T/2$ coin flips turn out “heads” in $T$ tosses of a random coin whose probability for “heads” is $1/2 - \gamma$. This bound has the same asymptotic behavior as the bound given for the boost-by-majority algorithm [11]. From Eq. (22) we get that the number of iterations of the boosting algorithm that is sufficient to achieve error $\varepsilon$ of $h_f$ is

$$
T = \left\lceil \frac{1}{\mathrm{KL}(1/2 \parallel 1/2 - \gamma)} \ln \frac{1}{\varepsilon} \right\rceil
$$

$$
\leq \left| \frac{1}{2\gamma^2} \ln \frac{1}{\varepsilon} \right|.
$$

Note, however, that when the errors of the hypotheses generated by WeakLearn are not uniform, Theorem 6 implies that the final error depends on the error of all of the weak hypotheses. Previous bounds on the errors of boosting algorithms depended only on the maximal error of the weakest hypothesis and ignored the advantage that can be gained from the hypotheses whose errors are smaller. This advantage seems to be very relevant to practical applications of boosting, because there one expects the error of the learning algorithm to increase as the distributions fed to WeakLearn shift more and more away from the target distribution.

4.3. *Generalization Error*

We now come back to discussing the error of the final hypothesis outside the training set. Theorem 6 guarantees that the error of $h_f$ on the sample is small; however, the quantity that interests us is the generalization error of $h_f$, which is the error of $h_f$ over the whole instance space $X$; that is, $\varepsilon_g = \Pr_{(x, y) \sim \mathcal{P}}[h_f(x) \neq y]$. In order to make $\varepsilon_g$ close to the empirical error $\hat{\varepsilon}$ on the training set, we have to restrict the choice of $h_f$ in some way. One natural way of doing this in the context of boosting is to restrict the weak learner to choose its hypotheses from some simple class of functions and restrict $T$, the number of weak hypotheses that are combined to make $h_f$. The choice of the class of weak hypotheses is specific to the learning problem at hand and should reflect our knowledge about the properties of the unknown concept. As for the choice of $T$, various general methods can be devised. One popular method is to use an upper bound on the VC-dimension of the concept class. This method is sometimes called “structural risk minimization.” See Vapnik’s book [23] for an extensive discussion of the theory of structural risk minimization. For our purposes, we quote Vapnik’s Theorem 6.7:

**Theorem 7** (Vapnik). *Let $H$ be a class of binary functions over some domain $X$. Let $d$ be the VC-dimension of $H$. Let $\mathcal{P}$ be a distribution over the pairs $X \times \{0, 1\}$. For $h \in H$, define the (generalization) error of $h$ with respect to $\mathcal{P}$ to be* {#freund-1997-adaboost-thm-7 .statement tag=086E}

$$
\varepsilon_g(h) \doteq \Pr_{(x, y) \sim \mathcal{P}}[h(x) \neq y].
$$

*Let $S = \{(x_1, y_1), ..., (x_N, y_N)\}$ be a sample (training set) of $N$ independent random examples drawn from $X \times \{0, 1\}$ according to $\mathcal{P}$. Define the empirical error of $h$ with respect to the sample $S$ to be*

$$
\hat{\varepsilon}(h) \doteq \frac{|\{i : h(x_i) \neq y_i\}|}{N}.
$$

*Then, for any $\delta > 0$ we have that*

$$
\Pr \left[ \exists h \in H : |\hat{\varepsilon}(h) - \varepsilon_g(h)| \right.
$$

$$
\left. > 2 \sqrt{\frac{d(\ln 2N/d + 1) + \ln 9/\delta}{N}} \right] \leq \delta
$$

*where the probability is computed with respect to the random choice of the sample $S$.*

Let $\theta : \mathbb{R} \to \{0, 1\}$ be defined by

$$
\theta(x) = \begin{cases}
1 & \text{if } x \geq 0 \\
0 & \text{otherwise}
\end{cases}
$$

and, for any class $H$ of functions, let $\Theta_T(H)$ be the class of all functions defined as a linear threshold of $T$ functions in $H$:

$$
\Theta_T(H) = \left\{ \theta \left( \sum_{t=1}^T a_t h_t - b \right) : b, a_1, ..., a_T \in \mathbb{R}; \right.
$$

$$
\left. h_1, ..., h_T \in H \right\}.
$$

Clearly, if all hypotheses generated by WeakLearn belong to some class $H$, then the final hypothesis of AdaBoost, after $T$ rounds of boosting, belongs to $\Theta_T(H)$. Thus, the next theorem provides an upper bound on the VC-dimension of the class of final hypotheses generated by AdaBoost in terms of the weak hypothesis class.

THEOREM 8. *Let H be a class of binary functions of VC-dimension d \geq 2. Then the VC-dimension of $\Theta_T(H)$ is at most $2(d+1)(T+1)\log_2(e(T+1))$ (where e is the base of the natural logarithm).

Therefore, if the hypotheses generated by **WeakLearn** are chosen from a class of VC-dimension $d \geq 2$, then the final hypotheses generated by **AdaBoost** after T iterations belong to a class of VC-dimension at most $2(d+1)(T+1)\log_2[e(T+1)]$.

*Proof.* We use a result about the VC-dimension of computation networks proved by Baum and Haussler [1]. We can view the final hypothesis output by **AdaBoost** as a function that is computed by a two-layer feed-forward network where the computation units of the first layer are the weak hypotheses and the computation unit of the second layer is the linear threshold function which combines the weak hypotheses. The VC-dimension of the set of linear threshold functions over $\mathbb{R}^T$ is $T+1$ [26]. Thus the sum over all computation units of the VC-dimensions of the classes of functions associated with each unit is $Td + (T+1) < (T+1)(d+1)$. Baum and Haussler’s Theorem 1 [1] implies that the number of different functions that can be realized by $h \in \Theta_T(H)$ when the domain is restricted to a set of size m is at most $((T+1)\ em/(T+1)(d+1))^{(T+1)(d+1)}$. If $d \geq 2$, $T \geq 1$ and we set $m = \lceil 2(T+1)(d+1)\log_2[e(T+1)] \rceil$, then the number of realizable functions is smaller than $2^m$ which implies that the VC-dimension of $\Theta_T(H)$ is smaller than m. $\blacksquare$

Following the guidelines of structural risk minimization we can do the following (assuming we know a reasonable upper bound on the VC-dimension of the class of weak hypotheses). Let $h_f^T$ be the hypothesis generated by running **AdaBoost** for T iterations. By combining the observed empirical error of $h_f^T$ with the bounds given in Theorems 7 and 8, we can compute an upper bound on the generalization error of $h_f^T$ for all T. We would then select the hypothesis $h_f^T$ that minimizes the guaranteed upper bound.

While structural risk minimization is a mathematically sound method, the upper bounds on $\varepsilon_g$ that are generated in this way might be larger than the actual value and so the chosen number of iterations T might be much smaller than the optimal value, leading to inferior performance. A simple alternative is to use “cross-validation” in which a fraction of the training set is left outside the set used to generate $h_f$ as the so-called “validation” set. The value of T is then chosen to be the one for which the error of the final hypothesis on the validation set is minimized. (For an extensive analysis of the relations between different methods for selecting model complexity in learning, see Kearns *et al.* [17].)

Some initial experiments using **AdaBoost** on real-world problems conducted by ourselves and Drucker and Cortes [8] indicate that **AdaBoost** tends not to over-fit; on many problems, even after hundreds of rounds of boosting, the generalization error continues to drop, or at least does not increase.

4.4. *A Bayesian Interpretation*

The final hypothesis generated by **AdaBoost** is closely related to one suggested by a Bayesian analysis. As usual, we assume that examples $(x, y)$ are being generated according to some distribution $\mathcal{P}$ on $X \times \{0, 1\}$; all probabilities in this subsection are taken with respect to $\mathcal{P}$. Suppose we are given a set of $\{0, 1\}$-valued hypotheses $h_1, ..., h_T$ and that our goal is to combine the predictions of these hypotheses in the optimal way. Then, given an instance $x$ and the hypothesis predictions $h_t(x)$, the Bayes optimal decision rule says that we should predict the label with the highest likelihood, given the hypothesis values, i.e., we should predict 1 if

$$
\Pr[y = 1 | h_1(x), ..., h_T(x)] > \Pr[y = 0 | h_1(x), ..., h_T(x)],
$$

and otherwise we should predict 0.

This rule is especially easy to compute if we assume that the errors of the different hypotheses are independent of one another and of the target concept, that is, if we assume that the event $h_t(x) \neq y$ is conditionally independent of the actual label $y$ and the predictions of all the other hypotheses $h_1(x), ..., h_{t-1}(x), h_{t+1}(x), ..., h_T(x)$. In this case, by applying Bayes rule, we can rewrite the Bayes optimal decision rule in a particularly simple form in which we predict 1 if

$$
\Pr[y = 1] \prod_{t : h_t(x) = 0} \varepsilon_t \prod_{t : h_t(x) = 1} (1 - \varepsilon_t)
$$

$$
> \Pr[y = 0] \prod_{t : h_t(x) = 0} (1 - \varepsilon_t) \prod_{t : h_t(x) = 1} \varepsilon_t,
$$

and 0 otherwise. Here $\varepsilon_t = \Pr[h_t(x) \neq y]$. We add to the set of hypotheses the trivial hypothesis $h_0$ which always predicts the value 1. We can then replace $\Pr[y = 0]$ by $\varepsilon_0$. Taking the logarithm of both sides in this inequality and rearranging the terms, we find that the Bayes optimal decision rule is *identical* to the combination rule that is generated by **AdaBoost**.

If the errors of the different hypotheses are dependent, then the Bayes optimal decision rule becomes much more complicated. However, in practice, it is common to use the simple rule described above even when there is no justification for assuming independence. (This is sometimes called “naive Bayes.”) An interesting and more principled alternative to this practice would be to use the algorithm **AdaBoost** to find a combination rule which, by Theorem 6, has a guaranteed non-trivial accuracy.

4.5. Improving the Error Bound

We show in this section how the bound given in Theorem 6 can be improved by a factor of two. The main idea of this improvement is to replace the “hard” {0, 1}-valued decision used by $h_f$ by a “soft” threshold.

To be more precise, let

$$
r(x) = \frac{\sum_{t=1}^T (\log \frac{1}{\beta_t}) h_t(x)}{\sum_{t=1}^T \log \frac{1}{\beta_t}}
$$

be a weighted average of the weak hypotheses $h_t$. We will here consider final hypotheses of the form $h_f(x) = F(r(x))$ where $F : [0, 1] \to [0, 1]$. For the version of AdaBoost given in Fig. 2, $F(r)$ is the hard threshold that equals 1 if $r \geq 1/2$ and 0 otherwise. In this section, we will instead use soft threshold functions that take values in [0, 1]. As mentioned above, when $h_f(x) \in [0, 1]$, we can interpret $h_f$ as a randomized hypothesis and $h_f(x)$ as the probability of predicting 1. Then the error $E_{i \sim D}[|h_f(x_i) - y_i|]$ is simply the probability of an incorrect prediction.

Theorem 9. Let $\varepsilon_1, ..., \varepsilon_T$ be as in Theorem 6, and let $r(x_i)$ be as defined above. Let the modified final hypothesis be defined by $h_f(x) = F(r(x))$ where $F$ satisfies the following for $r \in [0, 1]$: {#freund-1997-adaboost-thm-9 .statement tag=086F}

$$
F(1 - r) = 1 - F(r); \quad \text{and} \quad F(r) \leq \frac{1}{2} \left( \prod_{t=1}^T \beta_t \right)^{1/2 - r}.
$$

Then the error $\varepsilon$ of $h_f$ is bounded above by

$$
\varepsilon \leq 2^{T-1} \prod_{t=1}^T \sqrt{\varepsilon_t (1 - \varepsilon_t)}.
$$

For instance, it can be shown that the sigmoid function $F(r) = (1 + \prod_{t=1}^T \beta_t^{2r-1})^{-1}$ satisfies the conditions of the theorem.

Proof. By our assumptions on $F$, the error of $h_f$ is

$$
\varepsilon = \sum_{i=1}^N D(i) \cdot |F(r(x_i)) - y_i|
$$

$$
= \sum_{i=1}^N D(i) F(|r(x_i) - y_i|)
$$

$$
\leq \frac{1}{2} \sum_{i=1}^N \left( D(i) \prod_{t=1}^T \beta_t^{1/2 - |r(x_i) - y_i|} \right).
$$

Since $y_i \in \{0, 1\}$ and by definition of $r(x_i)$, this implies that

$$
\varepsilon \leq \frac{1}{2} \sum_{i=1}^N \left( D(i) \prod_{t=1}^T \beta_t^{1/2 - |h_t(x_i) - y_i|} \right)
$$

$$
= \frac{1}{2} \left( \sum_{i=1}^N w_i^{T+1} \right) \prod_{t=1}^T \beta_t^{-1/2}
$$

$$
\leq \frac{1}{2} \prod_{t=1}^T ((1 - (1 - \varepsilon_t)(1 - \beta_t))) \beta_t^{-1/2}.
$$

The last two steps follow from Eqs. (18) and (16), respectively. The theorem now follows from our choice of $\beta_t$.

5. BOOSTING FOR MULTI-CLASS AND REGRESSION PROBLEMS

So far, we have restricted our attention to binary classification problems in which the set of labels $Y$ contains only two elements. In this section, we describe two possible extensions of AdaBoost to the multi-class case in which $Y$ is any finite set of class labels. We also give an extension for a regression problem in which $Y$ is a real bounded interval.

We start with the multiple-label classification problem. Let $Y = \{1, 2, ..., k\}$ be the set of possible labels. The boosting algorithms we present output hypotheses $h_f : X \to Y$, and the error of the final hypothesis is measured in the usual way as the probability of an incorrect prediction.

The first extension of AdaBoost, which we call AdaBoost.M1, is the most direct. The weak learner generates hypotheses which assign to each instance one of the $k$ possible labels. We require that each weak hypothesis have prediction error less than 1/2 (with respect to the distribution on which it was trained). Provided this requirement can be met, we are able to prove that the error of the combined final hypothesis decreases exponentially, as in the binary case. Intuitively, however, this requirement on the performance of the weak learner is stronger than might be desired. In the binary case ($k = 2$), a random guess will be correct with probability 1/2, but when $k > 2$, the probability of a correct random prediction is only $1/k < 1/2$. Thus, our requirement that the accuracy of the weak hypothesis be greater than 1/2 is significantly stronger than simply requiring that the weak hypothesis perform better than random guessing.

In fact, when the performance of the weak learner is measured only in terms of error rate, this difficulty is unavoidable as is shown by the following informal example (also presented by Schapire [22]): Consider a learning problem where $Y = \{0, 1, 2\}$ and suppose that it is “easy” to predict whether the label is 2 but “hard” to predict whether the label is 0 or 1. Then a hypothesis which predicts correctly whenever the label is 2 and otherwise guesses randomly between 0 and 1 is guaranteed to be correct at least half of the time (significantly beating the 1/3 accuracy achieved by guessing entirely at random). On the other hand, boosting this learner to an arbitrary accuracy is infeasible since we assumed that it is hard to distinguish 0- and 1-labelled instances.

As a more natural example of this problem, consider classification of handwritten digits in an OCR application. It may be easy for the weak learner to tell that a particular image of a “7” is not a “0” but hard to tell for sure if it is a “7” or a “9”. Part of the problem here is that, although the boosting algorithm can focus the attention of the weak learner on the harder examples, it has no way of forcing the weak learner to discriminate between particular labels that may be especially hard to distinguish.

In our second version of multi-class boosting, we attempt to overcome this difficulty by extending the communication between the boosting algorithm and the weak learner. First, we allow the weak learner to generate more expressive hypotheses whose output is a vector in $[0, 1]^k$, rather than a single label in $Y$. Intuitively, the $y$th component of this vector represents a “degree of belief” that the correct label is $y$. The components with large values (close to 1) correspond to those labels considered to be plausible. Likewise, labels considered implausible are assigned a small value (near 0), and questionable labels may be assigned a value near 1/2. If several labels are considered plausible (or implausible), then they all may be assigned large (or small) values.

While we give the weak learning algorithm more expressive power, we also place a more complex requirement on the performance of the weak hypotheses. Rather than using the usual prediction error, we ask that the weak hypotheses do well with respect to a more sophisticated error measure that we call the pseudo-loss. This pseudo-loss varies from example to example, and from one round to the next. On each iteration, the pseudo-loss function is supplied to the weak learner by the boosting algorithm, along with the distribution on the examples. By manipulating the pseudo-loss function, the boosting algorithm can focus the weak learner on the labels that are hardest to discriminate. The boosting algorithm AdaBoost.M2, described in Section 5.2, is based on these ideas and achieves boosting if each weak hypothesis has pseudo-loss slightly better than random guessing (with respect to the pseudo-loss measure that was supplied to the weak learner).

In addition to the two extensions described in this paper, we mention an alternative, standard approach which would be to convert the given multi-class problem into several binary problems, and then to use boosting separately on each of the binary problems. There are several standard ways of making such a conversion, one of the most successful being the error-correcting output coding approach advocated by Dietterich and Bakiri [7].

Finally, in Section 5.3 we extend AdaBoost to boosting regression algorithms. In this case $Y = [0, 1]$, and the error of a hypothesis is defined as $E_{(x, y) \sim P}[(h(x) - y)^2]$. We describe a boosting algorithm AdaBoost.R. which, using methods similar to those used in AdaBoost.M2, boosts the performance of a weak regression algorithm.

### 5.1. *First Multi-class Extension* {#freund-1997-adaboost-s5-1 .section tag=0870}

In our first and most direct extension to the multi-class case, the goal of the weak learner is to generate on round $t$ a hypothesis $h_t : X \to Y$ with low classification error $\varepsilon_t \doteq \Pr_{i \sim p^t}[h_t(x_i) \neq y_i]$. Our extended boosting algorithm, called AdaBoost.M1, is shown in Fig. 3, and differs only slightly from AdaBoost. The main difference is in the replacement of the error $|h_t(x_i) - y_i|$ for the binary case by $[\![h_t(x_i) \neq y_i]\!]$ where, for any predicate $\pi$, we define $[\![\pi]\!]$ to be 1 if $\pi$ holds and 0 otherwise. Also, the final hypothesis $h_f$, for a given instance $x$, now outputs the label $y$ that maximizes the sum of the weights of the weak hypotheses predicting that label.

In the case of binary classification ($k = 2$), a weak hypothesis $h$ with error significantly larger than 1/2 is of equal value to one with error significantly less than 1/2 since $h$ can be replaced by $1 - h$. However, for $k > 2$, a hypothesis $h_t$ with error $\varepsilon_t \geq 1/2$ is useless to the boosting algorithm. If

Algorithm AdaBoost.M1
Input: sequence of $N$ examples $\langle (x_1, y_1), ..., (x_N, y_N) \rangle$ with labels $y_i \in Y = \{1, ..., k\}$
distribution $D$ over the $N$ examples
weak learning algorithm WeakLearn
integer $T$ specifying number of iterations
Initialize the weight vector: $w_i^1 = D(i)$ for $i = 1, ..., N$.
Do for $t = 1, 2, ..., T$

1. Set

$$
p' = \frac{w'}{\sum_{i=1}^N w'_i}
$$

2. Call WeakLearn, providing it with the distribution $p'$; get back a hypothesis $h_t : X \to Y$.
3. Calculate the error of $h_t$: $\varepsilon_t = \sum_{i=1}^N p'_i [\![h_t(x_i) \neq y_i]\!]$.
If $\varepsilon_t > 1/2$, then set $T = t - 1$ and abort loop.
4. Set $\beta_t = \varepsilon_t / (1 - \varepsilon_t)$.
5. Set the new weights vector to be

$$
w_i^{t+1} = w_i^t \beta_t^{1 - [\![h_t(x_i) \neq y_i]\!]}
$$

Output the hypothesis

$$
h_f(x) = \arg\max_{y \in Y} \sum_{t=1}^T \left( \log \frac{1}{\beta_t} \right) [\![h_t(x) = y]\!].
$$

FIG. 3. A first multi-class extension of AdaBoost.

such a weak hypothesis is returned by the weak learner, our algorithm simply halts, using only the weak hypotheses that were already computed.

Theorem 10. Suppose the weak learning algorithm WeakLearn, when called by AdaBoost.M1, generates hypotheses with errors $\varepsilon_1, ..., \varepsilon_T$, where $\varepsilon_t$ is as defined in Fig. 3. Assume each $\varepsilon_t \leq 1/2$. Then the error $\varepsilon = \Pr_{i \sim D}[h_f(x_i) \neq y_i]$ of the final hypothesis $h_f$ output by AdaBoost.M1 is bounded above by {#freund-1997-adaboost-thm-10 .statement tag=0871}

$$
\varepsilon \leq 2^T \prod_{t=1}^T \sqrt{\varepsilon_t(1-\varepsilon_t)}.
$$

Proof. To prove this theorem, we reduce our setup for AdaBoost.M1 to an instantiation of AdaBoost, and then apply Theorem 6. For clarity, we mark with tildes variables in the reduced AdaBoost space. For each of the given examples $(x_i, y_i)$, we define an AdaBoost example $(\tilde{x}_i, \tilde{y}_i)$ in which $\tilde{x}_i = i$ and $\tilde{y}_i = 0$. We define the AdaBoost distribution $\tilde{D}$ over examples to be equal to the AdaBoost.M1 distribution $D$. On the $t$th round, we provide AdaBoost with a hypothesis $\tilde{h}_t$ defined by the rule

$$
\tilde{h}_t(i) = [h_t(x_i) \neq y_i]
$$

in terms of the $t$th hypothesis $h_t$ which was returned to AdaBoost.M1 by WeakLearn.

Given this setup, it can be easily proved by induction on the number of rounds that the weight vectors, distributions and errors computed by AdaBoost and AdaBoost.M1 are identical so that $\tilde{w}^t = w^t$, $\tilde{p}^t = p^t$, $\tilde{\varepsilon}_t = \varepsilon_t$ and $\tilde{\beta}_t = \beta_t$.

Suppose that AdaBoost.M1’s final hypothesis $h_f$ makes a mistake on instance $i$ so that $h_f(x_i) \neq y_i$. Then, by definition of $h_f$,

$$
\sum_{t=1}^T \alpha_t [h_t(x_i) = y_i] \leq \sum_{t=1}^T \alpha_t [h_t(x_i) = h_f(x_i)]
$$

where $\alpha_t = \ln(1/\beta_t)$. This implies

$$
\sum_{t=1}^T \alpha_t [h_t(x_i) = y_i] \leq \frac{1}{2} \sum_{t=1}^T \alpha_t,
$$

using the fact that each $\alpha_t \geq 0$ since $\varepsilon_t \leq 1/2$. By definition of $\tilde{h}_t$, this implies

$$
\sum_{t=1}^T \alpha_t \tilde{h}_t(i) \geq \frac{1}{2} \sum_{t=1}^T \alpha_t,
$$

so $\tilde{h}_f(i) = 1$ by definition of the final AdaBoost hypothesis.

Therefore,

$$
\Pr_{i \sim D}[h_f(x_i) \neq y_i] \leq \Pr_{i \sim D}[\tilde{h}_f(i) = 1].
$$

Since each AdaBoost instance has a 0-label, $\Pr_{i \sim D}[\tilde{h}_f(i) = 1]$ is exactly the error of $\tilde{h}_f$. Applying Theorem 6, we can obtain a bound on this error, completing the proof. ■

It is possible, for this version of the boosting algorithm, to allow hypotheses which generate for each $x$, not only a predicted class label $h(x) \in Y$, but also a “confidence” $\kappa(x) \in [0, 1]$. The learner then suffers loss $1/2 - \kappa(x)/2$ if its prediction is correct and $1/2 + \kappa(x)/2$ otherwise. (Details omitted.)

### 5.2. Second Multi-class Extension {#freund-1997-adaboost-s5-2 .section tag=0872}

In this section we describe a second alternative extension of AdaBoost to the case where the label space $Y$ is finite. This extension requires more elaborate communication between the boosting algorithm and the weak learning algorithm. The advantage of doing this is that it gives the weak learner more flexibility in making its predictions. In particular, it sometimes enables the weak learner to make useful contributions to the accuracy of the final hypothesis even when the weak hypothesis does not predict the correct label with probability greater than 1/2.

As described above, the weak learner generates hypotheses which have the form $h : X \times Y \to [0, 1]$. Roughly speaking, $h(x, y)$ measures the degree to which it is believed that $y$ is the correct label associated with instance $x$. If, for a given $x$, $h(x, y)$ attains the same value for all $y$ then we say that the hypothesis is *uninformative* on instance $x$. On the other hand, any deviation from strict equality is potentially informative, because it predicts some labels to be more plausible than others. As will be seen, any such information is potentially useful for the boosting algorithm.

Below, we formalize the goal of the weak learner by defining a pseudo-loss which measures the goodness of the weak hypotheses. To motivate our definition, we first consider the following setup. For a fixed training example $(x_i, y_i)$, we use a given hypothesis $h$ to answer $k-1$ binary questions. For each of the incorrect labels $y \neq y_i$ we ask the question:

“Which is the label of $x_i$: $y_i$ or $y$?”

In other words, we ask that the correct label $y_i$ be discriminated from the incorrect label $y$.

Assume momentarily that $h$ only takes values in $\{0, 1\}$. Then if $h(x_i, y) = 0$ and $h(x_i, y_i) = 1$, we interpret $h$'s answer to the question above to be $y_i$ (since $h$ deems $y_i$ to be a plausible label for $x_i$, but $y$ is considered implausible). Likewise, if $h(x_i, y) = 1$ and $h(x_i, y_i) = 0$ then the answer is $y$. If $h(x_i, y) = h(x_i, y_i)$, then one of the two answers is chosen uniformly at random.

In the more general case that $h$ takes values in $[0, 1]$, we interpret $h(x, y)$ as a randomized decision for the procedure above. That is, we first choose a random bit $b(x, y)$ which is 1 with probability $h(x, y)$ and 0 otherwise. We then apply the above procedure to the stochastically chosen binary function $b$. The probability of choosing the incorrect answer $y$ to the question above is

$$
\Pr[b(x_i, y_i) = 0 \land b(x_i, y) = 1] + \frac{1}{2} \Pr[b(x_i, y_i) = b(x_i, y)]
= \frac{1}{2}(1 - h(x_i, y_i) + h(x_i, y)).
$$

If the answers to all $k - 1$ questions are considered equally important, then it is natural to define the loss of the hypothesis to be the average, over all $k - 1$ questions, of the probability of an incorrect answer:

$$
\frac{1}{k-1} \sum_{y \neq y_i} \frac{1}{2} (1 - h(x_i, y_i) + h(x_i, y))
= \frac{1}{2} \left( 1 - h(x_i, y_i) + \frac{1}{k-1} \sum_{y \neq y_i} h(x_i, y) \right).
\tag{24}
$$
{#freund-1997-adaboost-eq-24 .equation tag=0873}

However, as was discussed in the introduction to Section 5, different discrimination questions are likely to have different importance in different situations. For example, considering the OCR problem described earlier, it might be that at some point during the boosting process, some example of the digit “7” has been recognized as being either a “7” or a “9”. At this stage the question that discriminates between “7” (the correct label) and “9” is clearly much more important than the other eight questions that discriminate “7” from the other digits.

A natural way of attaching different degrees of importance to the different questions is to assign a weight to each question. So, for each instance $x_i$ and incorrect label $y \neq y_i$, we assign a weight $q(i, y)$ which we associate with the question that discriminates label $y$ from the correct label $y_i$. We then replace the average used in Eq. (24) with an average weighted according to $q(i, y)$; the resulting formula is called the *pseudo-loss* of $h$ on training instance $i$ with respect to $q$:

$$
\mathrm{ploss}_q(h, i) \doteq \frac{1}{2} \left( 1 - h(x_i, y_i) + \sum_{y \neq y_i} q(i, y) \, h(x_i, y) \right).
$$

The function $q = \{1, ..., N\} \times Y \to [0, 1]$, called the *label weighting function*, assigns to each example $i$ in the training set a probability distribution over the $k - 1$ discrimination problems defined above. So, for all $i$,

$$
\sum_{y \neq y_i} q(i, y) = 1.
$$

The weak learner’s goal is to minimize the expected pseudo-loss for given distribution $D$ and weighting function $q$:

$$
\mathrm{ploss}_{D, q}(h) := \mathbb{E}_{i \sim D} \left[ \mathrm{ploss}_q(h, i) \right].
$$

As we have seen, by manipulating both the distribution on instances, and the label weighting function $q$, our boosting algorithm effectively forces the weak learner to focus not only on the hard instances, but also on the incorrect class labels that are hardest to eliminate. Conversely, this pseudo-loss measure may make it easier for the weak learner to get a weak advantage. For instance, if the weak learner can simply determine that a particular instance does *not* belong to a certain class (even if it has no idea which of the remaining classes is the correct one), then, depending on $q$, this may be enough to gain a weak advantage.

Theorem 11, the main result of this section, shows that a weak learner can be boosted if it can consistently produce weak hypotheses with pseudo-losses smaller than 1/2. Note that pseudo-loss 1/2 can be achieved trivially by any uninformative hypothesis. Furthermore, a weak hypothesis $h$ with pseudo-loss $\varepsilon > 1/2$ is also beneficial to boosting since it can be replaced by the hypothesis $1 - h$ whose pseudo-loss is $1 - \varepsilon < 1/2$. {#freund-1997-adaboost-thm-11 .statement tag=0874}

**Example 5.** As a simple example illustrating the use of pseudo-loss, suppose we seek an *oblivious* weak hypothesis, i.e., a weak hypothesis whose value depends only on the class label $y$ so that $h(x, y) = h(y)$ for all $x$. Although oblivious hypotheses per se are generally too weak to be of interest, it may often be appropriate to find the best oblivious hypothesis on a *part* of the instance space (such as the set of instances covered by a leaf of a decision tree). {#freund-1997-adaboost-ex-5 .statement tag=0875}

Let $D$ be the target distribution, and $q$ the label weighting function. For notational convenience, let us define $q(i, y_i) = -1$ for all $i$ so that

$$
\mathrm{ploss}_q(h, i) = \frac{1}{2} \left( 1 + \sum_{y \in Y} q(i, y) \, h(x_i, y) \right).
$$

Setting $\delta(y) = \sum_i D(i) \, q(i, y)$, it can be verified that for an oblivious hypothesis $h$,

$$
\mathrm{ploss}_{D, q}(h) = \frac{1}{2} \left( 1 + \sum_{y \in Y} h(y) \, \delta(y) \right),
$$

which is clearly minimized by the choice

$$
h(y) = \begin{cases}
1 & \text{if } \delta(y) < 0 \\
0 & \text{otherwise}.
\end{cases}
$$

Suppose now that $q(i, y) = 1/(k-1)$ for $y \neq y_i$, and let $d(y) = \Pr_{i \sim D}[y_i = y]$ be the proportion of examples with label $y$. Then it can be verified that $h$ will always have pseudo-loss strictly smaller than 1/2 except in the case of a uniform distribution of labels ($d(y) = 1/k$ for all $y$). In contrast, when the weak learner’s goal is minimization of prediction error (as in Section 5.1), it can be shown that an oblivious hypothesis with prediction error strictly less than 1/2 can only be found when one label $y$ covers more than 1/2 the distribution ($d(y) > 1/2$). So in this case, it is much easier to find a hypothesis with small pseudo-loss rather than small prediction error.

On the other hand, if $q(i, y) = 0$ for some values of $y$, then the quality of prediction on these labels is of no consequence. In particular, if $q(i, y) = 0$ for all but one incorrect label for each instance $i$, then in order to make the pseudo-loss smaller than 1/2 the hypothesis has to predict the correct label with probability larger than 1/2, which means that in this case the pseudo-loss criterion is as stringent as the usual prediction error. However, as discussed above, this case is unavoidable because a hard binary classification problem can always be embedded in a multi-class problem.

This example suggests that it may often be significantly easier to find weak hypotheses with small pseudo-loss rather than hypotheses whose prediction error is small. On the other hand, our theoretical bound for boosting using the prediction error (Theorem 10) is stronger than the bound for ploss (Theorem 11). Empirical tests [12] have shown that pseudo-loss is generally more successful when the weak learners use very restricted hypotheses. However, for more powerful weak learners, such as decision-tree learning algorithms, there is little difference between using pseudo-loss and prediction error.

Our algorithm called AdaBoost.M2, is shown in Fig. 4. Here, we maintain weights $w_{i, y}^t$ for each instance $i$ and each label $y \in Y - \{ y_i \}$. The weak learner must be provided both with a distribution $D_t$ and a label weight function $q_t$. Both of these are computed using the weight vector $w^t$ as shown in Step 1. The weak learner’s goal then is to minimize the pseudo-loss $\varepsilon_t$, as defined in Step 3. The weights are updated as shown in Step 5. The final hypothesis $h_f$ outputs, for a given instance $x$, the label $y$ that maximizes a weighted average of the weak hypothesis values $h_t(x, y)$.

**THEOREM 11.** *Suppose the weak learning algorithm WeakLearn, when called by AdaBoost.M2 generates hypotheses with pseudo-losses $\varepsilon_1, ..., \varepsilon_T$, where $\varepsilon_t$ is as defined in Fig. 4. Then the error $\varepsilon = \Pr_{i \sim D}[h_f(x_i) \neq y_i]$ of the final hypothesis $h_f$ output by AdaBoost.M2 is bounded above by*

$$
\varepsilon \leq (k-1) 2^T \prod_{t=1}^T \sqrt{\varepsilon_t (1-\varepsilon_t)}.
$$

*Proof.* As in the proof of Theorem 10, we reduce to an instance of AdaBoost and apply Theorem 6. As before, we mark AdaBoost variables with a tilde.

**Algorithm AdaBoost.M2**
**Input:** sequence of $N$ examples $\langle (x_1, y_1), ..., (x_N, y_N) \rangle$ with labels $y_i \in Y = \{ 1, ..., k \}$
distribution $D$ over the $N$ examples
weak learning algorithm **WeakLearn**
integer $T$ specifying number of iterations
Initialize the weight vector: $w_{i, y}^1 = D(i)/(k-1)$ for $i = 1, ..., N, y \in Y - \{ y_i \}$.
Do for $t = 1, 2, ..., T$

1. Set $W_i^t = \sum_{y \neq y_i} w_{i, y}^t$;

$$
q_t(i, y) = \frac{w_{i, y}^t}{W_i^t}
$$

for $y \neq y_i$; and set

$$
D_t(i) = \frac{W_i^t}{\sum_{i=1}^N W_i^t}.
$$

2. Call **WeakLearn**, providing it with the distribution $D_t$ and label weighting function $q_t$; get back a hypothesis $h_t : X \times Y \to [0, 1]$.
3. Calculate the pseudo-loss of $h_t$:

$$
\varepsilon_t = \frac{1}{2} \sum_{i=1}^N D_t(i) \left( 1 - h_t(x_i, y_i) + \sum_{y \neq y_i} q_t(i, y) h_t(x_i, y) \right).
$$

4. Set $\beta_t = \varepsilon_t/(1-\varepsilon_t)$.
5. Set the new weights vector to be

$$
w_{i, y}^{t+1} = w_{i, y}^t \beta_t^{(1/2)(1+h_t(x_i, y_i)-h_t(x_i, y))}
$$

for $i = 1, ..., N, y \in Y - \{ y_i \}$.

**Output** the hypothesis

$$
h_f(x) = \arg \max_{y \in Y} \sum_{t=1}^T \left( \log \frac{1}{\beta_t} \right) h_t(x, y).
$$

FIG. 4. A second multi-class extension of AdaBoost.

For each training instance $(x_i, y_i)$ and for each incorrect label $y \in Y - \{ y_i \}$, we define one AdaBoost instance $\tilde{x}_{i, y} = (i, y)$ with associated label $\tilde{y}_{i, y} = 0$. Thus, there are $\tilde{N} = N(k-1)$ AdaBoost instances, each indexed by a pair $(i, y)$. The distribution over these instances is defined to be $\tilde{D}(i, y) = D(i)/(k-1)$. The $t$th hypothesis $\tilde{h}_t$ provided to AdaBoost for this reduction is defined by the rule

$$
\tilde{h}_t(i, y) = \frac{1}{2}(1-h_t(x_i, y_i)+h_t(x_i, y)).
$$

With this setup, it can be verified that the computed distributions and errors will be identical so that $\tilde{w}_{i, y}^t = w_{i, y}^t, \tilde{p}_{i, y}^t = p_{i, y}^t, \tilde{\varepsilon}_t = \varepsilon_t$ and $\tilde{\beta}_t = \beta_t$.

Suppose now that $h_f(x_i)\neq y_i$ for some example i. Then, by definition of $h_f$,

$$
\sum_{t=1}^{T}\alpha_t h_t(x_i,y_i)\leq \sum_{t=1}^{T}\alpha_t h_t(x_i,h_f(x_i)),
$$

where $\alpha_t=\ln(1/\beta_t)$. This implies that

$$
\sum_{t=1}^{T}\alpha_t\tilde h_t(i,h_f(x_i))=
\frac{1}{2}\sum_{t=1}^{T}\alpha_t(1-h_t(x_i,y_i)+h_t(x_i,h_f(x_i)))
$$

$$
\geq \frac{1}{2}\sum_{t=1}^{T}\alpha_t
$$

so $\tilde h_f(i,h_f(x_i))=1$ by definition of $\tilde h_f$.

Therefore,

$$
\Pr_{i\sim D}[h_f(x_i)\neq y_i]\leq \Pr_{(i,y)\sim\tilde D}[\exists y:y\neq y_i:\tilde h_f(i,y)=1].
$$

Since all AdaBoost instances have a 0-label, and by definition of $\tilde D$, the error of $\tilde h_f$ is

$$
\Pr_{(i,y)\sim\tilde D}[\tilde h_f(i,y)=1]
$$

$$
\geq \frac{1}{k-1}\Pr_{i\sim D}[\exists y\neq y_i:\tilde h_f(i,y)=1].
$$

Applying Theorem 6 to bound the error of $\tilde h_f$, this completes the proof. ▪

Although we omit the details, the bound for AdaBoost.M2 can be improved by a factor of two in a manner similar to that described in Section 4.5.

### 5.3. Boosting Regression Algorithms {#freund-1997-adaboost-s5-3 .section tag=0876}

In this section we show how boosting can be used for a regression problem. In this setting, the label space is $Y=[0,1]$. As before, the learner receives examples $(x,y)$ chosen at random according to some distribution $\mathcal P$, and its goal is to find a hypothesis $h:X\rightarrow Y$ which, given some $x$ value, predicts approximately the value $y$ that is likely to be seen. More precisely, the learner attempts to find an $h$ with small mean squared error (MSE):

$$
E_{(x,y)\sim\mathcal P}[(h(x)-y)^2]. \tag{25}
$$
{#freund-1997-adaboost-eq-25 .equation tag=0877}

Our methods can be applied to any reasonable bounded error measure, but, for the sake of concreteness, we concentrate here on the squared error measure.

Following our approach for classification problems, we assume that the learner has been provided with a training set $(x_1,y_1),...,(x_N,y_N)$ of examples distributed according to

$\mathcal P$, and we focus only on the minimization of the empirical MSE:

$$
\frac{1}{N}\sum_{i=1}^{N}(h(x_i)-y_i)^2.
$$

Using techniques similar to those outlined in Section 4.3, the true MSE given in Eq. (25) can be related to the empirical MSE.

To derive a boosting algorithm in this context, we reduce the given regression problem to a binary classification problem, and then apply AdaBoost. As was done for the reductions used in the proofs of Theorems 10 and 11, we mark with tildes all variables in the reduced (AdaBoost) space. For each example $(x_i,y_i)$ in the training set, we define a continuum of examples indexed by pairs $(i,y)$ for all $y\in[0,1]$: the associated instance is $\tilde x_{i,y}=(x_i,y)$, and the label is $\tilde y_{i,y}=[y>y_i]$. (Recall that $[\pi]$ is 1 if predicate $\pi$ holds and 0 otherwise.) Although it is obviously infeasible to explicitly maintain an infinitely large training set, we will see later how this method can be implemented efficiently. Also, although the results of Section 4 only dealt with finitely large training sets, the extension to infinite training sets is straightforward.

Thus, informally, each instance $(x_i,y_i)$ is mapped to an infinite set of binary questions, one for each $y\in Y$, and each of the form: “Is the correct label $y_i$ bigger or smaller than $y$?”

In a similar manner, each hypothesis $h:X\rightarrow Y$ is reduced to a binary-valued hypothesis $\tilde h:X\times Y\rightarrow\{0,1\}$ defined by the rule

$$
\tilde h(x,y)=[y\geq h(x)].
$$

Thus, $\tilde h$ attempts to answer these binary questions in a natural way using the estimated value $h(x)$.

Finally, as was done for classification problems, we assume we are given a distribution $D$ over the training set; ordinarily, this will be uniform so that $D(i)=1/N$. In our reduction, this distribution is mapped to a density $\tilde D$ over pairs $(i,y)$ in such a way that minimization of classification error in the reduced space is equivalent to minimization of MSE for the original problem. To do this, we define

$$
\tilde D(i,y)=\frac{D(i)|y-y_i|}{Z}
$$

where $Z$ is a normalization constant:

$$
Z=\sum_{i=1}^{N}D(i)\int_{0}^{1}|y-y_i|\,dy.
$$

It is straightforward to show that $1/4\leq Z\leq1/2$.

If we calculate the binary error of $\tilde{h}$ with respect to the density $\tilde{D}$, we find that, as desired, it is directly proportional to the mean squared error:

$$
\sum_{i=1}^N \int_0^1 |\tilde{y}_{i,y} - \tilde{h}(\tilde{x}_{i,y})| \tilde{D}(i, y) \, dy
$$

$$
= \frac{1}{Z} \sum_{i=1}^N D(i) \left| \int_{y_i}^{h(x_i)} |y - y_i| \, dy \right|
$$

$$
= \frac{1}{2Z} \sum_{i=1}^N D(i)(h(x_i) - y_i)^2.
$$

The constant of proportionality is $1/(2Z) \in [1, 2]$.

Unravelling this reduction, we obtain the regression boosting procedure **AdaBoost.R** shown in Fig. 5. As prescribed by the reduction, **AdaBoost.R** maintains a weight $w_{i,y}^t$ for each instance $i$ and label $y \in Y$. The initial weight function $w^1$ is exactly the density $\tilde{D}$ defined above. By normalizing the weights $w^t$, a density $p^t$ is defined at Step 1 and provided to the weak learner at Step 2. The goal of the weak learner is to find a hypothesis $h_t : X \to Y$ that minimizes the loss $\varepsilon_t$ defined in Step 3. Finally, at Step 5, the weights are updated as prescribed by the reduction.

The definition of $\varepsilon_t$ at Step 3 follows directly from the reduction above; it is exactly the classification error of $\tilde{h}_f$ in the reduced space. Note that, similar to **AdaBoost.M2**, **AdaBoost.R** not only varies the distribution over the examples $(x_i, y_i)$, but also modifies from round to round the definition of the loss suffered by a hypothesis on each example. Thus, although our ultimate goal is minimization of the squared error, the weak learner must be able to handle loss functions that are more complicated than MSE.

The final hypothesis $h_f$ also is consistent with the reduction. Each reduced weak hypothesis $\tilde{h}_f(x, y)$ is non-decreasing as a function of $y$. Thus, the final hypothesis $\tilde{h}_f$ generated by **AdaBoost** in the reduced space, being the threshold of a weighted sum of these hypotheses, also is non-decreasing as a function of $y$. As the output of $\tilde{h}_f$ is binary, this implies that for every $x$ there is one value of $y$ for which $\tilde{h}_f(x, y') = 0$ for all $y' < y$ and $\tilde{h}_f(x, y') = 1$ for all $y' > y$. This is exactly the value of $y$ given by $h_f(x)$ as defined in the figure. Note that $h_f$ is actually computing a *weighted median* of the weak hypotheses.

At first, it might seem impossible to maintain weights $w_{i,y}^t$ over an uncountable set of points. However, on closer inspection, it can be seen that, when viewed as a function of $y$, $w_{i,y}^t$ is a piece-wise linear function. For $t = 1$, $w_{i,y}^1$ has two linear pieces, and each update at Step 5 potentially breaks one of the pieces in two at the point $h_t(x_i)$. Initializing, storing and updating such piece-wise linear functions are all straightforward operations. Also, the integrals which appear in the figure can be evaluated explicitly since these only involve integration of piece-wise linear functions.

Algorithm **AdaBoost.R**
Input: sequence of $N$ examples $\langle (x_1, y_1), ..., (x_N, y_N) \rangle$ with labels $y_i \in Y = [0, 1]$
distribution $D$ over the examples
weak learning algorithm **WeakLearn**
integer $T$ specifying number of iterations
Initialize the weight vector:

$$
w_{i,y}^1 = \frac{D(i) |y - y_i|}{Z}
$$

for $i = 1, ..., N, y \in Y$, where

$$
Z = \sum_{i=1}^N D(i) \int_0^1 |y - y_i| \, dy.
$$

Do for $t = 1, 2, ..., T$
1. Set

$$
p^t = \frac{w^t}{\sum_{i=1}^N \int_0^1 w_{i,y}^t \, dy}.
$$

2. Call **WeakLearn**, providing it with the density $p^t$; get back a hypothesis $h_t : X \times Y$.
3. Calculate the loss of $h_t$:

$$
\varepsilon_t = \sum_{i=1}^N \left| \int_{y_i}^{h_t(x_i)} p_{i,y}^t \, dy \right|.
$$

If $\varepsilon_t > 1/2$, then set $T = t - 1$ and abort the loop.
4. Set $\beta_t = \varepsilon_t / (1 - \varepsilon_t)$.
5. Set the new weights vector to be

$$
w_{i,y}^{t+1} = \begin{cases}
w_{i,y}^t & \text{if } y_i \leq y \leq h_t(x_i) \text{ or } h_t(x_i) \leq y \leq y_i \\
w_{i,y}^t \beta_t & \text{otherwise.}
\end{cases}
$$

for $i = 1, ..., N, y \in Y$.

Output the hypothesis

$$
h_f(x) = \inf \left\{ y \in Y : \sum_{t : h_t(x) \leq y} \log(1/\beta_t) \geq \frac{1}{2} \sum_t \log(1/\beta_t) \right\}.
$$

FIG. 5. An extension of AdaBoost to regression problems.

The following theorem describes our performance guarantee for **AdaBoost.R**. The proof follows from the reduction described above coupled with a direct application of Theorem 6.

**Theorem 12.** *Suppose the weak learning algorithm **WeakLearn**, when called by **AdaBoost.R**, generates hypotheses with errors $\varepsilon_1, ..., \varepsilon_T$, where $\varepsilon_t$ is as defined in Fig. 5. Then the mean squared error $\varepsilon = \mathbb{E}_{i \sim D}[(h_f(x_i) - y_i)^2]$ of* the final hypothesis $h_f$ output by **AdaBoost.R** *is bounded above* by {#freund-1997-adaboost-thm-12 .statement tag=0878}

$$
\varepsilon \leq 2^T \prod_{t=1}^T \sqrt{\varepsilon_t(1-\varepsilon_t)}.
$$

An unfortunate property of this setup is that there is no trivial way to generate a hypothesis whose loss is 1/2. This is a similar situation to the one we encountered with algorithm **AdaBoost.M1**. A remedy to this problem might be to allow weak hypotheses from a more general class of functions. One simple generalization is to allow for weak hypotheses that are defined by two functions: $h : X \to [0, 1]$ as before, and $\kappa : X \to [0, 1]$ which associates a measure of confidence to each prediction of $h$. The reduced hypothesis which we associate with this pair of functions is

$$
\tilde{h}(x, y) = \begin{cases}
(1 + \kappa(x))/2 & \text{if } h(x) \geq y \\
(1 - \kappa(x))/2 & \text{otherwise}.
\end{cases}
$$

These hypotheses are used in the same way as the ones defined before and a slight variation of algorithm **AdaBoost.R** can be used to boost the accuracy of these more general weak learners (details omitted). The advantage of this variant is that any hypothesis for which $\kappa(x)$ is identically zero has pseudo-loss exactly 1/2 and slight deviations from this hypothesis can be used to encode very weak predictions.

The method presented in this section for boosting with square loss can be used with any reasonable bounded loss function $L : Y \times Y \to [0, 1]$. Here, $L(y', y)$ is a measure of the “discrepancy” between the observed label $y$ and a predicted label $y'$; for instance, above we used $L(y', y) = (y' - y)^2$. The goal of learning is to find a hypothesis $h$ with small average loss $\mathrm{E}_{(x, y) \sim \mathcal{P}}[L(h(x), y)]$. Assume, for any $y$, that $L(y, y) = 0$ and that $L(y', y)$ is differentiable with respect to $y'$, non-increasing for $y' \leq y$ and non-decreasing for $y' \geq y$. Then, to modify **AdaBoost.R** to handle such a loss function, we need only replace $|y - y_i|$ in the initialization step with $|\partial L(y, y_i)/\partial y|$. The rest of the algorithm is unchanged, and the modifications needed for the analysis are straightforward.

APPENDIX: PROOF OF THEOREM 3

We start with a brief review of a framework used by Vovk [24], which is very similar to the framework used in Section 3. In this framework, an on-line decision problem consists of a decision space $\Delta$, an outcome space $\Omega$ and a loss function $\lambda : \Delta \times \Omega \to [0, \infty]$, which associates a loss to each decision and outcome pair. At each trial $t$ the learning algorithm receives the decisions $\varepsilon_1^t, ..., \varepsilon_N^t \in \Delta$ of $N$ experts, and then generates its own decision $\delta^t \in \Delta$. Upon receiving an outcome $\omega^t \in \Omega$, the learner and each expert $i$ incur loss $\lambda(\delta^t, \omega^t)$ and $\lambda(\varepsilon_i^t, \omega^t)$, respectively. The goal of the learning algorithm is to generate decisions in such a way that its cumulative loss will not be much larger than the cumulative loss of the best expert. The following four properties are assumed to hold:

1. $\Delta$ is a compact topological space.
2. For each $\omega$, the function $\delta \to \lambda(\delta, \omega)$ is continuous.
3. There exists $\delta$ such that, for all $\omega$, $\lambda(\delta, \omega) < \infty$.
4. There exists no $\delta$ such that, for all $\omega$, $\lambda(\delta, \omega) = 0$.

We now give Vovk’s main result [24]. Let a decision problem defined by $\Omega, \Delta$ and $\lambda$ obey Assumptions 1–4. Let $c$ and $a$ be positive real numbers. We say that the decision problem is *(c, a)*-bounded if there exists an algorithm $A$ such that for any finite set of experts and for any finite sequence of trials, the cumulative loss of the algorithm is bounded by

$$
\sum_{t=1}^T \lambda(\delta^t, \omega^t) \leq c \min_i \sum_{t=1}^T \lambda(\varepsilon_i^t, \omega^t) + a \ln N,
$$

where $N$ is the number of experts.

We say that a distribution $\mathcal{D}$ is *simple* if it is non-zero on a finite set denoted $\mathrm{dom}(\mathcal{D})$. Let $\mathcal{S}$ be the set of simple distributions over $\Delta$. Vovk defines the following function $c : (0, 1) \to [0, \infty]$ which characterizes the hardness of any decision problem:

$$
c(\beta) = \sup_{\mathcal{D} \in \mathcal{S}} \inf_{\delta \in \Delta} \sup_{\omega \in \Omega} \frac{\lambda(\delta, \omega)}{\log_\beta \sum_{\varepsilon \in \mathrm{dom}(\mathcal{D})} \beta^{\lambda(\varepsilon, \omega)} \mathcal{D}(\varepsilon)}.
$$

He then proves the following powerful theorem:

**Theorem 13** (Vovk). *A decision problem is* *(c, a)*-bounded *if and only if for all* $\beta \in (0, 1)$, $c \geq c(\beta)$ *or* $a \geq c(\beta)/\ln(1/\beta)$. {#freund-1997-adaboost-thm-13 .statement tag=0879}

*Proof of Theorem 3.* The proof consists of the following three steps: We first define a decision problem that conforms to Vovk’s framework. We then show a lower bound on the function $c(\beta)$ for this problem. Finally, we show how any algorithm $A$ for the on-line allocation problem can be used to generate decisions in the defined problem, and so we get from Theorem 13 a lower bound on the worst case cumulative loss of $A$.

The decision problem is defined as follows. We fix an integer $K > 1$ and set $\Delta = S_K$ where $S_K$ is the $K$ dimensional simplex, i.e., $S_K = \{ \mathbf{x} \in [0, 1]^K : \sum_{i=1}^K x_i = 1 \}$. We set $\Omega$ to be the set of unit vectors in $\mathbb{R}^K$, i.e., $\Omega = \{ \mathbf{e}_1, ..., \mathbf{e}_K \}$ where $\mathbf{e}_i \in \{0, 1\}^K$ has a 1 in the $i$th component, and 0 in all other components. Finally, we define the loss function to be $\lambda(\delta, \mathbf{e}_i) = \delta \cdot \mathbf{e}_i = \delta_i$. One can easily verify that these definitions conform to Assumptions 1–4.

To prove a lower bound on $c(\beta)$ for this decision problem we choose a particular simple distribution over the decision space $\Delta$. Let $\mathcal{D}$ be the uniform distribution over the unit vectors, i.e., $\mathrm{dom}(\mathcal{D}) = \{ \mathbf{e}_1, ..., \mathbf{e}_K \}$. For this distribution, we can explicitly calculate

$$
c(\beta) \geq \inf_{\delta \in \Delta} \sup_{\omega \in \Omega} \frac{\lambda(\delta, \omega)}{\log_\beta \sum_{\varepsilon \in \mathrm{dom}(\mathcal{D})} \beta^{\lambda(\varepsilon, \omega)} \mathcal{D}(\varepsilon)}. \tag{28}
$$
{#freund-1997-adaboost-eq-28 .equation tag=087A}

First, it is easy to see that the denominator in Eq. (28) is a constant:

$$
\sum_{\varepsilon \in \mathrm{dom}(\mathcal{D})} \beta^{\lambda(\varepsilon, \omega)} \mathcal{D}(\varepsilon) = \frac{\beta}{K} + \frac{K-1}{K}. \tag{29}
$$
{#freund-1997-adaboost-eq-29 .equation tag=087B}

For any probability vector $\delta \in \Delta$, there must exist one component $i$ for which $\delta_i \leq 1/K$. Thus

$$
\inf_{\delta \in \Delta} \sup_{\omega \in \Omega} \lambda(\delta, \omega) = 1/K. \tag{30}
$$
{#freund-1997-adaboost-eq-30 .equation tag=087C}

Combining Eqs. (28), (29), (30), we get that

$$
c(\beta) \geq \frac{\ln(1/\beta)}{K \ln(1 - (1-\beta)/K)}. \tag{31}
$$
{#freund-1997-adaboost-eq-31 .equation tag=087D}

We now show how an on-line allocation algorithm $A$ can be used as a subroutine for solving this decision problem. We match each of the $N$ experts of the decision problem with a strategy of the allocation problem. Each iteration $t$ of the decision problem proceeds as follows.

1. Each of the $N$ experts generates a decision $\varepsilon_i^t \in S_K$.
2. The algorithm $A$ generates a distribution $\mathbf{p}^t \in S_N$.
3. The learner chooses the decision $\delta^t = \sum_{i=1}^N p_i^t \varepsilon_i^t$.
4. The outcome $\omega^t \in \Omega$ is generated.
5. The learner incurs loss $\delta^t \cdot \omega^t$, and each expert suffers loss $\varepsilon_i^t \cdot \omega^t$.
6. Algorithm $A$ receives the loss vector $\ell^t$ where $\ell_i^t = \varepsilon_i^t \cdot \omega^t$, and incurs loss

$$
\mathbf{p}^t \cdot \ell^t = \sum_{i=1}^N p_i^t (\varepsilon_i^t \cdot \omega^t)
= \left( \sum_{i=1}^N p_i^t \varepsilon_i^t \right) \cdot \omega^t = \delta^t \cdot \omega^t.
$$

Observe that the loss incurred by the learner in the decision problem is equal to the loss incurred by $A$. Thus, if for algorithm $A$ we have an upper bound of the form

$$
L_A \leq c \min_i L_i + a \ln N,
$$

then the decision problem is $(c, a)$)-bounded. On the other hand, using the lower bound given by Theorem 13 and the lower bound on $c(\beta)$ given in Eq. (31), we get that for any $K$ and any $\beta$, either

$$
c \geq \frac{\ln(1/\beta)}{K \ln(1 - (1-\beta)/K)} \quad \text{or} \quad a \geq \frac{1}{K \ln(1 - (1-\beta)/K)}. \tag{32}
$$
{#freund-1997-adaboost-eq-32 .equation tag=087E}

As $K$ is a free parameter we can let $K \to \infty$ and the denominators in Eq. (22) become $1 - \beta$ which gives the statement of the theorem. ■
