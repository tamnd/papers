---
paper: shannon-1948-communication
title: A Mathematical Theory of Communication
authors:
  - Claude E. Shannon
year: 1948
venue: Bell System Technical Journal
field: theory
section: "24"
section_title: THE CAPACITY OF A CONTINUOUS CHANNEL
tag: 04EE
kind: appendix
lang: en
source: https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf
pdf_sha256: 6e4e3411984f3edf99dbfe8b941cb5e8a321379ff0cae6ae5c1f592ad8882ca8
pdf_pages: 41-43
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 6567ee1caf972907c04da987ab1d0ff7b664e647faa985e8fb70590d3a82ac74
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

In a continuous channel the input or transmitted signals will be continuous functions of time $f(t)$ belonging to a certain set, and the output or received signals will be perturbed versions of these. We will consider only the case where both transmitted and received signals are limited to a certain band W. They can then be specified, for a time T, by 2TW numbers, and their statistical structure by finite dimensional distribution functions. Thus the statistics of the transmitted signal will be determined by

$$
P(x_1, \ldots, x_n) = P(x)
$$

and those of the noise by the conditional probability distribution

$$
P_{x_1, \ldots, x_n}(y_1, \ldots, y_n) = P_x(y).
$$

The rate of transmission of information for a continuous channel is defined in a way analogous to that for a discrete channel, namely

$$
R = H(x) - H_y(x)
$$

where $H(x)$ is the entropy of the input and $H_y(x)$ the equivocation. The channel capacity C is defined as the maximum of R when we vary the input over all possible ensembles. This means that in a finite dimensional approximation we must vary $P(x) = P(x_1, \ldots, x_n)$ and maximize

$$
-\int P(x) \log P(x) dx + \iint P(x, y) \log \frac{P(x, y)}{P(y)} dxdy.
$$

This can be written

$$
\iint P(x, y) \log \frac{P(x, y)}{P(x)P(y)} dxdy
$$

using the fact that $\iint P(x, y) \log P(x) dxdy = \int P(x) \log P(x) dx$. The channel capacity is thus expressed as follows:

$$
C = \lim_{T \to \infty} \max_{P(x)} \frac{1}{T} \iint P(x, y) \log \frac{P(x, y)}{P(x)P(y)} dxdy.
$$

It is obvious in this form that R and C are independent of the coordinate system since the numerator and denominator in $\log \frac{P(x, y)}{P(x)P(y)}$ will be multiplied by the same factors when x and y are transformed in any one-to-one way. This integral expression for C is more general than $H(x) - H_y(x)$. Properly interpreted (see Appendix 7) it will always exist while $H(x) - H_y(x)$ may assume an indeterminate form $\infty - \infty$ in some cases. This occurs, for example, if x is limited to a surface of fewer dimensions than n in its n dimensional approximation.

If the logarithmic base used in computing $H(x)$ and $H_y(x)$ is two then C is the maximum number of binary digits that can be sent per second over the channel with arbitrarily small equivocation, just as in the discrete case. This can be seen physically by dividing the space of signals into a large number of small cells, sufficiently small so that the probability density $P_x(y)$ of signal x being perturbed to point y is substantially constant over a cell (either of x or y). If the cells are considered as distinct points the situation is essentially the same as a discrete channel and the proofs used there will apply. But it is clear physically that this quantizing of the volume into individual points cannot in any practical situation alter the final answer significantly, provided the regions are sufficiently small. Thus the capacity will be the limit of the capacities for the discrete subdivisions and this is just the continuous capacity defined above.

On the mathematical side it can be shown first (see Appendix 7) that if u is the message, x is the signal, y is the received signal (perturbed by noise) and v is the recovered message then

$$
H(x) - H_y(x) \geq H(u) - H_v(u)
$$

regardless of what operations are performed on u to obtain x or on y to obtain v. Thus no matter how we encode the binary digits to obtain the signal, or how we decode the received signal to recover the message, the discrete rate for the binary digits does not exceed the channel capacity we have defined. On the other hand, it is possible under very general conditions to find a coding system for transmitting binary digits at the rate C with as small an equivocation or frequency of errors as desired. This is true, for example, if, when we take a finite dimensional approximating space for the signal functions, $P(x, y)$ is continuous in both x and y except at a set of points of probability zero.

An important special case occurs when the noise is added to the signal and is independent of it (in the probability sense). Then $P_x(y)$ is a function only of the difference $n = (y - x)$,

$$
P_x(y) = Q(y - x)
$$

and we can assign a definite entropy to the noise (independent of the statistics of the signal), namely the entropy of the distribution Q(n). This entropy will be denoted by H(n).

Theorem 16: *If the signal and noise are independent and the received signal is the sum of the transmitted signal and the noise then the rate of transmission is* {#shannon-1948-communication-thm-16 .statement tag=04EF}

$$
R = H(y) - H(n),
$$

*i.e., the entropy of the received signal less the entropy of the noise. The channel capacity is*

$$
C = \max_{P(x)} H(y) - H(n).
$$

We have, since y = x + n:

$$
H(x, y) = H(x, n).
$$

Expanding the left side and using the fact that x and n are independent

$$
H(y) + H_y(x) = H(x) + H(n).
$$

Hence

$$
R = H(x) - H_y(x) = H(y) - H(n).
$$

Since H(n) is independent of P(x), maximizing R requires maximizing H(y), the entropy of the received signal. If there are certain constraints on the ensemble of transmitted signals, the entropy of the received signal must be maximized subject to these constraints.
