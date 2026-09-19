---
paper: shannon-1948-communication
title: A Mathematical Theory of Communication
authors:
  - Claude E. Shannon
year: 1948
venue: Bell System Technical Journal
field: theory
section: "27"
section_title: FIDELITY EVALUATION FUNCTIONS
tag: 04F6
kind: appendix
lang: en
source: https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf
pdf_sha256: 6e4e3411984f3edf99dbfe8b941cb5e8a321379ff0cae6ae5c1f592ad8882ca8
pdf_pages: 47-49
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 26dd6d97c5536ac53141014f7ec723183b21aa55a5b5166ccbe55d134809efd6
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

In the case of a discrete source of information we were able to determine a definite rate of generating information, namely the entropy of the underlying stochastic process. With a continuous source the situation is considerably more involved. In the first place a continuously variable quantity can assume an infinite number of values and requires, therefore, an infinite number of binary digits for exact specification. This means that to transmit the output of a continuous source with exact recovery at the receiving point requires, in general, a channel of infinite capacity (in bits per second). Since, ordinarily, channels have a certain amount of noise, and therefore a finite capacity, exact transmission is impossible.

This, however, evades the real issue. Practically, we are not interested in exact transmission when we have a continuous source, but only in transmission to within a certain tolerance. The question is, can we assign a definite rate to a continuous source when we require only a certain fidelity of recovery, measured in a suitable way. Of course, as the fidelity requirements are increased the rate will increase. It will be shown that we can, in very general cases, define such a rate, having the property that it is possible, by properly encoding the information, to transmit it over a channel whose capacity is equal to the rate in question, and satisfy the fidelity requirements. A channel of smaller capacity is insufficient.

It is first necessary to give a general mathematical formulation of the idea of fidelity of transmission. Consider the set of messages of a long duration, say T seconds. The source is described by giving the probability density, in the associated space, that the source will select the message in question P(x). A given communication system is described (from the external point of view) by giving the conditional probability P_x(y) that if message x is produced by the source the recovered message at the receiving point will be y. The system as a whole (including source and transmission system) is described by the probability function P(x,y) of having message x and final output y. If this function is known, the complete characteristics of the system from the point of view of fidelity are known. Any evaluation of fidelity must correspond mathematically to an operation applied to P(x,y). This operation must at least have the properties of a simple ordering of systems; i.e., it must be possible to say of two systems represented by P_1(x,y) and P_2(x,y) that, according to our fidelity criterion, either (1) the first has higher fidelity, (2) the second has higher fidelity, or (3) they have equal fidelity. This means that a criterion of fidelity can be represented by a numerically valued function:

$$
v(P(x,y))
$$

whose argument ranges over possible probability functions P(x,y).

We will now show that under very general and reasonable assumptions the function v(P(x,y)) can be written in a seemingly much more specialized form, namely as an average of a function $\rho(x,y)$ over the set of possible values of x and y:

$$
v(P(x,y)) = \iint P(x,y) \rho(x,y) dx dy.
$$

To obtain this we need only assume (1) that the source and system are ergodic so that a very long sample will be, with probability nearly 1, typical of the ensemble, and (2) that the evaluation is “reasonable” in the sense that it is possible, by observing a typical input and output x_1 and y_1, to form a tentative evaluation on the basis of these samples; and if these samples are increased in duration the tentative evaluation will, with probability 1, approach the exact evaluation based on a full knowledge of P(x,y). Let the tentative evaluation be $\rho(x,y)$. Then the function $\rho(x,y)$ approaches (as $T \to \infty$) a constant for almost all (x,y) which are in the high probability region corresponding to the system:

$$
\rho(x,y) \to v(P(x,y))
$$

and we may also write

$$
\rho(x,y) \to \iint P(x,y) \rho(x,y) dx dy
$$

since

$$
\iint P(x,y) dx dy = 1.
$$

This establishes the desired result.

The function $\rho(x,y)$ has the general nature of a “distance” between x and y.\footnote{It is not a “metric” in the strict sense, however, since in general it does not satisfy either $\rho(x,y) = \rho(y,x)$ or $\rho(x,y) + \rho(y,z) \geq \rho(x,z)$.} It measures how undesirable it is (according to our fidelity criterion) to receive y when x is transmitted. The general result given above can be restated as follows: Any reasonable evaluation can be represented as an average of a distance function over the set of messages and recovered messages x and y weighted according to the probability P(x,y) of getting the pair in question, provided the duration T of the messages be taken sufficiently large.

The following are simple examples of evaluation functions:

\footnotetext{9}{It is not a “metric” in the strict sense, however, since in general it does not satisfy either $\rho(x,y) = \rho(y,x)$ or $\rho(x,y) + \rho(y,z) \geq \rho(x,z)$.}

1. R.M.S. criterion.

$$
v = \frac{1}{(x(t) - y(t))^2}.
$$

In this very commonly used measure of fidelity the distance function $\rho(x, y)$ is (apart from a constant factor) the square of the ordinary Euclidean distance between the points x and y in the associated function space.

$$
\rho(x, y) = \frac{1}{T} \int_0^T [x(t) - y(t)]^2 dt.
$$

2. Frequency weighted R.M.S. criterion. More generally one can apply different weights to the different frequency components before using an R.M.S. measure of fidelity. This is equivalent to passing the difference $x(t) - y(t)$ through a shaping filter and then determining the average power in the output. Thus let

$$
e(t) = x(t) - y(t)
$$

and

$$
f(t) = \int_{-\infty}^{\infty} e(\tau) k(t - \tau) d\tau
$$

then

$$
\rho(x, y) = \frac{1}{T} \int_0^T f(t)^2 dt.
$$

3. Absolute error criterion.

$$
\rho(x, y) = \frac{1}{T} \int_0^T |x(t) - y(t)| dt.
$$

4. The structure of the ear and brain determine implicitly an evaluation, or rather a number of evaluations, appropriate in the case of speech or music transmission. There is, for example, an “intelligibility” criterion in which $\rho(x, y)$ is equal to the relative frequency of incorrectly interpreted words when message $x(t)$ is received as $y(t)$. Although we cannot give an explicit representation of $\rho(x, y)$ in these cases it could, in principle, be determined by sufficient experimentation. Some of its properties follow from well-known experimental results in hearing, e.g., the ear is relatively insensitive to phase and the sensitivity to amplitude and frequency is roughly logarithmic.

5. The discrete case can be considered as a specialization in which we have tacitly assumed an evaluation based on the frequency of errors. The function $\rho(x, y)$ is then defined as the number of symbols in the sequence y differing from the corresponding symbols in x divided by the total number of symbols in x.
