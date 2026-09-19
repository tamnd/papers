---
paper: shannon-1948-communication
title: A Mathematical Theory of Communication
authors:
  - Claude E. Shannon
year: 1948
venue: Bell System Technical Journal
field: theory
section_title: Appendix 6
kind: appendix
lang: en
source: https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf
pdf_sha256: 6e4e3411984f3edf99dbfe8b941cb5e8a321379ff0cae6ae5c1f592ad8882ca8
pdf_pages: 52-53
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 231a3d0df3390d94d8e6a5f99bf87cf686043ff766e33c90d17b12a005dce1b2
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The upper bound, $\overline{N}_3 \leq N_1 + N_2$, is due to the fact that the maximum possible entropy for a power $N_1 + N_2$ occurs when we have a white noise of this power. In this case the entropy power is $N_1 + N_2$.

To obtain the lower bound, suppose we have two distributions in n dimensions $p(x_i)$ and $q(x_i)$ with entropy powers $\overline{N}_1$ and $\overline{N}_2$. What form should p and q have to minimize the entropy power $\overline{N}_3$ of their convolution $r(x_i)$:

$$
r(x_i) = \int p(y_i)q(x_i - y_i) dy_i.
$$

The entropy $H_3$ of r is given by

$$
H_3 = - \int r(x_i) \log r(x_i) dx_i.
$$

We wish to minimize this subject to the constraints

$$
H_1 = - \int p(x_i) \log p(x_i) dx_i \\
H_2 = - \int q(x_i) \log q(x_i) dx_i.
$$

We consider then

$$
U = - \int [r(x) \log r(x) + \lambda p(x) \log p(x) + \mu q(x) \log q(x)] dx
$$

$$
\delta U = - \int [[1 + \log r(x)] \delta r(x) + \lambda [1 + \log p(x)] \delta p(x) + \mu [1 + \log q(x)] \delta q(x)] dx.
$$

If $p(x)$ is varied at a particular argument $x_i = s_i$, the variation in $r(x)$ is

$$
\delta r(x) = q(x_i - s_i)
$$

and

$$
\delta U = - \int q(x_i - s_i) \log r(x_i) dx_i - \lambda \log p(s_i) = 0
$$

and similarly when $q$ is varied. Hence the conditions for a minimum are

$$
\int q(x_i - s_i) \log r(x_i) dx_i = -\lambda \log p(s_i)
$$

$$
\int p(x_i - s_i) \log r(x_i) dx_i = -\mu \log q(s_i).
$$

If we multiply the first by $p(s_i)$ and the second by $q(s_i)$ and integrate with respect to $s_i$ we obtain

$$
H_3 = -\lambda H_1 \\
H_3 = -\mu H_2
$$

or solving for $\lambda$ and $\mu$ and replacing in the equations

$$
H_1 \int q(x_i - s_i) \log r(x_i) dx_i = -H_3 \log p(s_i)
$$

$$
H_2 \int p(x_i - s_i) \log r(x_i) dx_i = -H_3 \log q(s_i).
$$

Now suppose $p(x_i)$ and $q(x_i)$ are normal

$$
p(x_i) = \frac{|A_{ij}|^{n/2}}{(2\pi)^{n/2}} \exp - \frac{1}{2} \sum A_{ij} x_i x_j
$$

$$
q(x_i) = \frac{|B_{ij}|^{n/2}}{(2\pi)^{n/2}} \exp - \frac{1}{2} \sum B_{ij} x_i x_j.
$$

Then $r(x_i)$ will also be normal with quadratic form $C_{ij}$. If the inverses of these forms are $a_{ij}, b_{ij}, c_{ij}$ then

$$
c_{ij} = a_{ij} + b_{ij}.
$$

We wish to show that these functions satisfy the minimizing conditions if and only if $a_{ij} = K b_{ij}$ and thus give the minimum $H_3$ under the constraints. First we have

$$
\log r(x_i) = \frac{n}{2} \log \frac{1}{2\pi} |C_{ij}| - \frac{1}{2} \sum C_{ij} x_i x_j
$$

$$
\int q(x_i - s_i) \log r(x_i) dx_i = \frac{n}{2} \log \frac{1}{2\pi} |C_{ij}| - \frac{1}{2} \sum C_{ij} s_i s_j - \frac{1}{2} \sum C_{ij} b_{ij}.
$$

This should equal

$$
\frac{H_3}{H_1} \left[ \frac{n}{2} \log \frac{1}{2\pi} |A_{ij}| - \frac{1}{2} \sum A_{ij} s_i s_j \right]
$$

which requires $A_{ij} = \frac{H_1}{H_3} C_{ij}$. In this case $A_{ij} = \frac{H_1}{H_2} B_{ij}$ and both equations reduce to identities.
