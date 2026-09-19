---
paper: shannon-1948-communication
title: A Mathematical Theory of Communication
authors:
  - Claude E. Shannon
year: 1948
venue: Bell System Technical Journal
field: theory
section: "20"
section_title: Entropy of a Continuous Distribution
tag: "04E8"
kind: appendix
lang: en
source: https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf
pdf_sha256: 6e4e3411984f3edf99dbfe8b941cb5e8a321379ff0cae6ae5c1f592ad8882ca8
pdf_pages: 35-38
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 8666b61aa747ff74c3eafceccbcb7d1e6022ecca44b962a026cf9d095a065879
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The entropy of a discrete set of probabilities p_1, ..., p_n has been defined as:

$$
H = - \sum p_i \log p_i.
$$

In an analogous manner we define the entropy of a continuous distribution with the density distribution function p(x) by:

$$
H = - \int_{-\infty}^{\infty} p(x) \log p(x) dx.
$$

With an n dimensional distribution p(x_1, ..., x_n) we have

$$
H = - \int \cdots \int p(x_1, ..., x_n) \log p(x_1, ..., x_n) dx_1 \cdots dx_n.
$$

If we have two arguments x and y (which may themselves be multidimensional) the joint and conditional entropies of p(x,y) are given by

$$
H(x, y) = - \iint p(x, y) \log p(x, y) dxdy
$$

and

$$
H_x(y) = - \iint p(x, y) \log \frac{p(x, y)}{p(x)} dxdy \\
H_y(x) = - \iint p(x, y) \log \frac{p(x, y)}{p(y)} dxdy
$$

where

$$
p(x) = \int p(x, y) dy \\
p(y) = \int p(x, y) dx.
$$

The entropies of continuous distributions have most (but not all) of the properties of the discrete case. In particular we have the following:

1. If x is limited to a certain volume v in its space, then H(x) is a maximum and equal to log v when p(x) is constant (1/v) in the volume.

2. With any two variables x, y we have

$$
H(x, y) \leq H(x) + H(y)
$$

with equality if (and only if) x and y are independent, i.e., $p(x, y) = p(x)p(y)$ (apart possibly from a set of points of probability zero).

3. Consider a generalized averaging operation of the following type:

$$
p'(y) = \int a(x, y)p(x)\, dx
$$

with

$$
\int a(x, y)\, dx = \int a(x, y)\, dy = 1, \qquad a(x, y) \geq 0.
$$

Then the entropy of the averaged distribution $p'(y)$ is equal to or greater than that of the original distribution $p(x)$.

4. We have

$$
H(x, y) = H(x) + H_x(y) = H(y) + H_y(x)
$$

and

$$
H_x(y) \leq H(y).
$$

5. Let $p(x)$ be a one-dimensional distribution. The form of $p(x)$ giving a maximum entropy subject to the condition that the standard deviation of x be fixed at $\sigma$ is Gaussian. To show this we must maximize

$$
H(x) = - \int p(x) \log p(x)\, dx
$$

with

$$
\sigma^2 = \int p(x)x^2\, dx \quad \text{and} \quad 1 = \int p(x)\, dx
$$

as constraints. This requires, by the calculus of variations, maximizing

$$
\int \left[ -p(x) \log p(x) + \lambda p(x)x^2 + \mu p(x) \right] dx.
$$

The condition for this is

$$
-1 - \log p(x) + \lambda x^2 + \mu = 0
$$

and consequently (adjusting the constants to satisfy the constraints)

$$
p(x) = \frac{1}{\sqrt{2\pi}\sigma} e^{-(x^2/2\sigma^2)}.
$$

Similarly in n dimensions, suppose the second order moments of $p(x_1, \ldots, x_n)$ are fixed at $A_{ij}$:

$$
A_{ij} = \int \cdots \int x_i x_j p(x_1, \ldots, x_n)\, dx_1 \cdots dx_n.
$$

Then the maximum entropy occurs (by a similar calculation) when $p(x_1, \ldots, x_n)$ is the n dimensional Gaussian distribution with the second order moments $A_{ij}$.

6. The entropy of a one-dimensional Gaussian distribution whose standard deviation is $\sigma$ is given by

$$
H(x) = \log \sqrt{2 \pi e \sigma}.
$$

This is calculated as follows:

$$
p(x) = \frac{1}{\sqrt{2 \pi \sigma}} e^{-(x^2 / 2 \sigma^2)}
$$

$$
-\log p(x) = \log \sqrt{2 \pi \sigma} + \frac{x^2}{2 \sigma^2}
$$

$$
H(x) = - \int p(x) \log p(x) dx
$$

$$
= \int p(x) \log \sqrt{2 \pi \sigma} dx + \int p(x) \frac{x^2}{2 \sigma^2} dx
$$

$$
= \log \sqrt{2 \pi \sigma} + \frac{\sigma^2}{2 \sigma^2}
$$

$$
= \log \sqrt{2 \pi \sigma} + \log \sqrt{e}
$$

$$
= \log \sqrt{2 \pi e \sigma}.
$$

Similarly the n dimensional Gaussian distribution with associated quadratic form $a_{ij}$ is given by

$$
p(x_1, \ldots, x_n) = \frac{|a_{ij}|^{1/2}}{(2 \pi)^{n/2}} \exp \left( -\frac{1}{2} \sum a_{ij} x_i x_j \right)
$$

and the entropy can be calculated as

$$
H = \log (2 \pi e)^{n/2} |a_{ij}|^{-1/2}
$$

where $|a_{ij}|$ is the determinant whose elements are $a_{ij}$.

7. If x is limited to a half line ($p(x) = 0$ for $x \leq 0$) and the first moment of x is fixed at a:

$$
a = \int_0^\infty p(x) x dx,
$$

then the maximum entropy occurs when

$$
p(x) = \frac{1}{a} e^{-(x/a)}
$$

and is equal to $\log a$.

8. There is one important difference between the continuous and discrete entropies. In the discrete case the entropy measures in an absolute way the randomness of the chance variable. In the continuous case the measurement is relative to the coordinate system. If we change coordinates the entropy will in general change. In fact if we change to coordinates $y_1 \cdots y_n$ the new entropy is given by

$$
H(y) = \int \cdots \int p(x_1, \ldots, x_n) J \left( \frac{x}{y} \right) \log p(x_1, \ldots, x_n) J \left( \frac{x}{y} \right) dy_1 \cdots dy_n
$$

where $J \left( \frac{x}{y} \right)$ is the Jacobian of the coordinate transformation. On expanding the logarithm and changing the variables to $x_1 \cdots x_n$, we obtain:

$$
H(y) = H(x) - \int \cdots \int p(x_1, \ldots, x_n) \log J \left( \frac{x}{y} \right) dx_1 \ldots dx_n.
$$

Thus the new entropy is the old entropy less the expected logarithm of the Jacobian. In the continuous case the entropy can be considered a measure of randomness relative to an assumed standard, namely the coordinate system chosen with each small volume element dx₁ ⋯ dxₙ given equal weight. When we change the coordinate system the entropy in the new system measures the randomness when equal volume elements dy₁ ⋯ dyₙ in the new system are given equal weight.

In spite of this dependence on the coordinate system the entropy concept is as important in the continuous case as the discrete case. This is due to the fact that the derived concepts of information rate and channel capacity depend on the difference of two entropies and this difference does not depend on the coordinate frame, each of the two terms being changed by the same amount.

The entropy of a continuous distribution can be negative. The scale of measurements sets an arbitrary zero corresponding to a uniform distribution over a unit volume. A distribution which is more confined than this has less entropy and will be negative. The rates and capacities will, however, always be non-negative.

9. A particular case of changing coordinates is the linear transformation

$$
y_j = \sum_i a_{ij} x_i.
$$

In this case the Jacobian is simply the determinant $|a_{ij}|^{-1}$ and

$$
H(y) = H(x) + \log |a_{ij}|.
$$

In the case of a rotation of coordinates (or any measure preserving transformation) J = 1 and H(y) = H(x).
