---
paper: shannon-1948-communication
title: A Mathematical Theory of Communication
authors:
  - Claude E. Shannon
year: 1948
venue: Bell System Technical Journal
field: theory
section: "21"
section_title: Entropy of an Ensemble of Functions
tag: "04E9"
kind: appendix
lang: en
source: https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf
pdf_sha256: 6e4e3411984f3edf99dbfe8b941cb5e8a321379ff0cae6ae5c1f592ad8882ca8
pdf_pages: 38-39
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 1e52de4ec86fc552e574e7582779576eff68c3d5e3d266dbbaf14d6e14d56819
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Consider an ergodic ensemble of functions limited to a certain band of width W cycles per second. Let

$$
p(x_1, \ldots, x_n)
$$

be the density distribution function for amplitudes x₁, ..., xₙ at n successive sample points. We define the entropy of the ensemble per degree of freedom by

$$
H' = -\lim_{n \to \infty} \frac{1}{n} \int \cdots \int p(x_1, \ldots, x_n) \log p(x_1, \ldots, x_n) dx_1 \ldots dx_n.
$$

We may also define an entropy H per second by dividing, not by n, but by the time T in seconds for n samples. Since n = 2TW, H = 2WH'.

With white thermal noise p is Gaussian and we have

$$
H' = \log \sqrt{2 \pi e N},
$$

$$
H = W \log 2 \pi e N.
$$

For a given average power N, white noise has the maximum possible entropy. This follows from the maximizing properties of the Gaussian distribution noted above.

The entropy for a continuous stochastic process has many properties analogous to that for discrete processes. In the discrete case the entropy was related to the logarithm of the probability of long sequences, and to the number of reasonably probable sequences of long length. In the continuous case it is related in a similar fashion to the logarithm of the probability density for a long series of samples, and the volume of reasonably high probability in the function space.

More precisely, if we assume p(x₁, ..., xₙ) continuous in all the xᵢ for all n, then for sufficiently large n

$$
\left| \frac{\log p}{n} - H' \right| < \epsilon
$$

for all choices of $(x_1, \ldots, x_n)$ apart from a set whose total probability is less than $\delta$, with $\delta$ and $\epsilon$ arbitrarily small. This follows form the ergodic property if we divide the space into a large number of small cells.

The relation of $H$ to volume can be stated as follows: Under the same assumptions consider the n dimensional space corresponding to $p(x_1, \ldots, x_n)$. Let $V_n(q)$ be the smallest volume in this space which includes in its interior a total probability q. Then

$$
\lim_{n \to \infty} \frac{\log V_n(q)}{n} = H'
$$

provided q does not equal 0 or 1.

These results show that for large n there is a rather well-defined volume (at least in the logarithmic sense) of high probability, and that within this volume the probability density is relatively uniform (again in the logarithmic sense).

In the white noise case the distribution function is given by

$$
p(x_1, \ldots, x_n) = \frac{1}{(2\pi N)^{n/2}} \exp - \frac{1}{2N} \sum x_i^2.
$$

Since this depends only on $\sum x_i^2$ the surfaces of equal probability density are spheres and the entire distribution has spherical symmetry. The region of high probability is a sphere of radius $\sqrt{nN}$. As $n \to \infty$ the probability of being outside a sphere of radius $\sqrt{n(N + \epsilon)}$ approaches zero and $\frac{1}{n}$ times the logarithm of the volume of the sphere approaches $\log \sqrt{2\pi e N}$.

In the continuous case it is convenient to work not with the entropy $H$ of an ensemble but with a derived quantity which we will call the entropy power. This is defined as the power in a white noise limited to the same band as the original ensemble and having the same entropy. In other words if $H'$ is the entropy of an ensemble its entropy power is

$$
N_1 = \frac{1}{2\pi e} \exp 2H'.
$$

In the geometrical picture this amounts to measuring the high probability volume by the squared radius of a sphere having the same volume. Since white noise has the maximum entropy for a given power, the entropy power of any noise is less than or equal to its actual power.
