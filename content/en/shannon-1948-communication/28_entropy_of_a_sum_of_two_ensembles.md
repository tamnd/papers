---
paper: shannon-1948-communication
title: A Mathematical Theory of Communication
authors:
  - Claude E. Shannon
year: 1948
venue: Bell System Technical Journal
field: theory
section: "23"
section_title: ENTROPY OF A SUM OF TWO ENSEMBLES
tag: 04EC
kind: appendix
lang: en
source: https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf
pdf_sha256: 6e4e3411984f3edf99dbfe8b941cb5e8a321379ff0cae6ae5c1f592ad8882ca8
pdf_pages: 40-41
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 5b1b5ebe96000c86f85545d0710e51f640888101697cac765c138f2bebab83b8
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

If we have two ensembles of functions $f_\alpha(t)$ and $g_\beta(t)$ we can form a new ensemble by "addition." Suppose the first ensemble has the probability density function $p(x_1, \ldots, x_n)$ and the second $q(x_1, \ldots, x_n)$. Then the density function for the sum is given by the convolution:

$$
r(x_1, \ldots, x_n) = \int \cdots \int p(y_1, \ldots, y_n) q(x_1 - y_1, \ldots, x_n - y_n) \, dy_1 \cdots dy_n.
$$

Physically this corresponds to adding the noises or signals represented by the original ensembles of functions.

The following result is derived in Appendix 6.

Theorem 15: *Let the average power of two ensembles be N₁ and N₂ and let their entropy powers be $\overline{N}_1$ and $\overline{N}_2$. Then the entropy power of the sum, $\overline{N}_3$, is bounded by* {#shannon-1948-communication-thm-15 .statement tag=04ED}

$$
\overline{N}_1 + \overline{N}_2 \leq \overline{N}_3 \leq N_1 + N_2.
$$

White Gaussian noise has the peculiar property that it can absorb any other noise or signal ensemble which may be added to it with a resultant entropy power approximately equal to the sum of the white noise power and the signal power (measured from the average signal value, which is normally zero), provided the signal power is small, in a certain sense, compared to noise.

Consider the function space associated with these ensembles having n dimensions. The white noise corresponds to the spherical Gaussian distribution in this space. The signal ensemble corresponds to another probability distribution, not necessarily Gaussian or spherical. Let the second moments of this distribution about its center of gravity be $a_{ij}$. That is, if $p(x_1, \ldots, x_n)$ is the density distribution function

$$
a_{ij} = \int \cdots \int p(x_i - \alpha_i)(x_j - \alpha_j) dx_1 \cdots dx_n
$$

where the $\alpha_i$ are the coordinates of the center of gravity. Now $a_{ij}$ is a positive definite quadratic form, and we can rotate our coordinate system to align it with the principal directions of this form. $a_{ij}$ is then reduced to diagonal form $b_{ii}$. We require that each $b_{ii}$ be small compared to N, the squared radius of the spherical distribution.

In this case the convolution of the noise and signal produce approximately a Gaussian distribution whose corresponding quadratic form is

$$
N + b_{ii}.
$$

The entropy power of this distribution is

$$
\left[ \prod (N + b_{ii}) \right]^{1/n}
$$

or approximately

$$
= \left[ (N)^n + \sum b_{ii} (N)^{n-1} \right]^{1/n}
$$

$$
\doteq N + \frac{1}{n} \sum b_{ii}.
$$

The last term is the signal power, while the first is the noise power.

PART IV: THE CONTINUOUS CHANNEL
