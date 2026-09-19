---
paper: shannon-1948-communication
title: A Mathematical Theory of Communication
authors:
  - Claude E. Shannon
year: 1948
venue: Bell System Technical Journal
field: theory
section: "6"
section_title: Choice, Uncertainty and Entropy
tag: 04CC
kind: section
lang: en
source: https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf
pdf_sha256: 6e4e3411984f3edf99dbfe8b941cb5e8a321379ff0cae6ae5c1f592ad8882ca8
pdf_pages: 10-12
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: f422fc058488cf90fd3f80ffd45f488c943c4a7b5fa7bb85b1f2f1c25d8563b6
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

We have represented a discrete information source as a Markoff process. Can we define a quantity which will measure, in some sense, how much information is “produced” by such a process, or better, at what rate information is produced?

Suppose we have a set of possible events whose probabilities of occurrence are $p_1, p_2, \ldots, p_n$. These probabilities are known but that is all we know concerning which event will occur. Can we find a measure of how much “choice” is involved in the selection of the event or of how uncertain we are of the outcome?

If there is such a measure, say $H(p_1, p_2, \ldots, p_n)$, it is reasonable to require of it the following properties:

1. H should be continuous in the $p_i$.

2. If all the $p_i$ are equal, $p_i = \frac{1}{n}$, then H should be a monotonic increasing function of n. With equally likely events there is more choice, or uncertainty, when there are more possible events.

3. If a choice be broken down into two successive choices, the original H should be the weighted sum of the individual values of H. The meaning of this is illustrated in Fig. 6. At the left we have three

Figure.

Fig. 6 — Decomposition of a choice from three possibilities.

possibilities $p_1 = \frac{1}{2}, p_2 = \frac{1}{3}, p_3 = \frac{1}{6}$. On the right we first choose between two possibilities each with probability $\frac{1}{2}$, and if the second occurs make another choice with probabilities $\frac{2}{3}, \frac{1}{3}$. The final results have the same probabilities as before. We require, in this special case, that

$$
H(\frac{1}{2}, \frac{1}{3}, \frac{1}{6}) = H(\frac{1}{2}, \frac{1}{2}) + \frac{1}{2} H(\frac{2}{3}, \frac{1}{3}).
$$

The coefficient $\frac{1}{2}$ is because this second choice only occurs half the time.

In Appendix 2, the following result is established:

Theorem 2: *The only H satisfying the three above assumptions is of the form:* {#shannon-1948-communication-thm-2 .statement tag=04CD}

$$
H = -K \sum_{i=1}^{n} p_i \log p_i
$$

*where K is a positive constant.*

This theorem, and the assumptions required for its proof, are in no way necessary for the present theory. It is given chiefly to lend a certain plausibility to some of our later definitions. The real justification of these definitions, however, will reside in their implications.

Quantities of the form $H = - \sum p_i \log p_i$ (the constant K merely amounts to a choice of a unit of measure) play a central role in information theory as measures of information, choice and uncertainty. The form of H will be recognized as that of entropy as defined in certain formulations of statistical mechanics$^8$ where $p_i$ is the probability of a system being in cell i of its phase space. H is then, for example, the H in Boltzmann’s famous H theorem. We shall call $H = - \sum p_i \log p_i$ the entropy of the set of probabilities $p_1, \ldots, p_n$. If x is a chance variable we will write $H(x)$ for its entropy; thus x is not an argument of a function but a label for a number, to differentiate it from $H(y)$ say, the entropy of the chance variable y.

The entropy in the case of two possibilities with probabilities p and q = 1 − p, namely

$$
H = -(p \log p + q \log q)
$$

is plotted in Fig. 7 as a function of p.

Figure.

Fig. 7 — Entropy in the case of two possibilities with probabilities p and (1 − p).

The quantity H has a number of interesting properties which further substantiate it as a reasonable measure of choice or information.

1. $H = 0$ if and only if all the $p_i$ but one are zero, this one having the value unity. Thus only when we are certain of the outcome does H vanish. Otherwise H is positive.
2. For a given n, H is a maximum and equal to log n when all the $p_i$ are equal (i.e., $\frac{1}{n}$). This is also intuitively the most uncertain situation.

$^8$See, for example, R. C. Tolman, Principles of Statistical Mechanics, Oxford, Clarendon, 1938.

3. Suppose there are two events, x and y, in question with m possibilities for the first and n for the second. Let p(i, j) be the probability of the joint occurrence of i for the first and j for the second. The entropy of the joint event is

$$
H(x, y) = - \sum_{i,j} p(i, j) \log p(i, j)
$$

while

$$
H(x) = - \sum_{i,j} p(i, j) \log \sum_j p(i, j)
$$

$$
H(y) = - \sum_{i,j} p(i, j) \log \sum_i p(i, j).
$$

It is easily shown that

$$
H(x, y) \leq H(x) + H(y)
$$

with equality only if the events are independent (i.e., p(i, j) = p(i)p(j)). The uncertainty of a joint event is less than or equal to the sum of the individual uncertainties.

4. Any change toward equalization of the probabilities $p_1, p_2, \ldots, p_n$ increases H. Thus if $p_1 < p_2$ and we increase $p_1$, decreasing $p_2$ an equal amount so that $p_1$ and $p_2$ are more nearly equal, then H increases. More generally, if we perform any “averaging” operation on the $p_i$ of the form

$$
p'_i = \sum_j a_{ij} p_j
$$

where $\sum_i a_{ij} = \sum_j a_{ij} = 1$, and all $a_{ij} \geq 0$, then H increases (except in the special case where this transformation amounts to no more than a permutation of the $p_j$ with H of course remaining the same).

5. Suppose there are two chance events x and y as in 3, not necessarily independent. For any particular value i that x can assume there is a conditional probability $p_i(j)$ that y has the value j. This is given by

$$
p_i(j) = \frac{p(i, j)}{\sum_j p(i, j)}.
$$

We define the conditional entropy of y, $H_x(y)$ as the average of the entropy of y for each value of x, weighted according to the probability of getting that particular x. That is

$$
H_x(y) = - \sum_{i,j} p(i, j) \log p_i(j).
$$

This quantity measures how uncertain we are of y on the average when we know x. Substituting the value of $p_i(j)$ we obtain

$$
H_x(y) = - \sum_{i,j} p(i, j) \log p(i, j) + \sum_{i,j} p(i, j) \log \sum_j p(i, j)
$$

$$
= H(x, y) - H(x)
$$

or

$$
H(x, y) = H(x) + H_x(y).
$$

The uncertainty (or entropy) of the joint event x, y is the uncertainty of x plus the uncertainty of y when x is known.

6. From 3 and 5 we have

$$
H(x) + H(y) \geq H(x, y) = H(x) + H_x(y).
$$

Hence

$$
H(y) \geq H_x(y).
$$

The uncertainty of y is never increased by knowledge of x. It will be decreased unless x and y are independent events, in which case it is not changed.
