---
paper: shannon-1948-communication
title: A Mathematical Theory of Communication
authors:
  - Claude E. Shannon
year: 1948
venue: Bell System Technical Journal
field: theory
section: "29"
section_title: THE CALCULATION OF RATES
tag: 04F9
kind: appendix
lang: en
source: https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf
pdf_sha256: 6e4e3411984f3edf99dbfe8b941cb5e8a321379ff0cae6ae5c1f592ad8882ca8
pdf_pages: 50-51
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 3c831e8d901c3a3d54ddb2c6c07e9b2ddf9e096be35a81936ecbcd147ae50851
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The definition of the rate is similar in many respects to the definition of channel capacity. In the former

$$
R = \min_{P_x(y)} \iint P(x, y) \log \frac{P(x, y)}{P(x)P(y)}\, dx dy
$$

with $P(x)$ and $v_1 = \iint P(x, y)\rho(x, y)\, dx dy$ fixed. In the latter

$$
C = \max_{P(x)} \iint P(x, y) \log \frac{P(x, y)}{P(x)P(y)}\, dx dy
$$

with $P_x(y)$ fixed and possibly one or more other constraints (e.g., an average power limitation) of the form $K = \iint P(x, y)\lambda(x, y)\, dx dy$.

A partial solution of the general maximizing problem for determining the rate of a source can be given. Using Lagrange’s method we consider

$$
\iint \left[ P(x, y) \log \frac{P(x, y)}{P(x)P(y)} + \mu P(x, y)\rho(x, y) + \nu(x)P(x, y) \right]\, dx dy.
$$

The variational equation (when we take the first variation on P(x, y)) leads to

$$
P_y(x) = B(x)e^{-\lambda \rho(x,y)}
$$

where $\lambda$ is determined to give the required fidelity and B(x) is chosen to satisfy

$$
\int B(x)e^{-\lambda \rho(x,y)} dx = 1.
$$

This shows that, with best encoding, the conditional probability of a certain cause for various received y, $P_y(x)$ will decline exponentially with the distance function $\rho(x, y)$ between the x and y in question.

In the special case where the distance function $\rho(x, y)$ depends only on the (vector) difference between x and y,

$$
\rho(x, y) = \rho(x - y)
$$

we have

$$
\int B(x)e^{-\lambda \rho(x-y)} dx = 1.
$$

Hence B(x) is constant, say $\alpha$, and

$$
P_y(x) = \alpha e^{-\lambda \rho(x-y)}.
$$

Unfortunately these formal solutions are difficult to evaluate in particular cases and seem to be of little value. In fact, the actual calculation of rates has been carried out in only a few very simple cases.

If the distance function $\rho(x, y)$ is the mean square discrepancy between x and y and the message ensemble is white noise, the rate can be determined. In that case we have

$$
R = \min [H(x) - H_y(x)] = H(x) - \max H_y(x)
$$

with $N = \overline{(x - y)^2}$. But the Max $H_y(x)$ occurs when $y - x$ is a white noise, and is equal to $W_1 \log 2 \pi e N$ where $W_1$ is the bandwidth of the message ensemble. Therefore

$$
\begin{align*}
R &= W_1 \log 2 \pi e Q - W_1 \log 2 \pi e N \\
  &= W_1 \log \frac{Q}{N}
\end{align*}
$$

where Q is the average message power. This proves the following:

Theorem 22: *The rate for a white noise source of power Q and band W₁ relative to an R.M.S. measure of fidelity is* {#shannon-1948-communication-thm-22 .statement tag=04FA}

$$
R = W_1 \log \frac{Q}{N}
$$

*where N is the allowed mean square error between original and recovered messages.*

More generally with any message source we can obtain inequalities bounding the rate relative to a mean square error criterion.

Theorem 23: *The rate for any source of band W₁ is bounded by* {#shannon-1948-communication-thm-23 .statement tag=04FB}

$$
W_1 \log \frac{Q_1}{N} \leq R \leq W_1 \log \frac{Q}{N}
$$

*where Q is the average power of the source, Q₁ its entropy power and N the allowed mean square error.*

The lower bound follows from the fact that the Max $H_y(x)$ for a given $\overline{(x - y)^2} = N$ occurs in the white noise case. The upper bound results if we place points (used in the proof of Theorem 21) not in the best way but at random in a sphere of radius $\sqrt{Q - N}$.
