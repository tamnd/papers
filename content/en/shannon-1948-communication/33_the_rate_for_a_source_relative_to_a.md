---
paper: shannon-1948-communication
title: A Mathematical Theory of Communication
authors:
  - Claude E. Shannon
year: 1948
venue: Bell System Technical Journal
field: theory
section: "28"
section_title: THE RATE FOR A SOURCE RELATIVE TO A FIDELITY EVALUATION
tag: 04F7
kind: appendix
lang: en
source: https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf
pdf_sha256: 6e4e3411984f3edf99dbfe8b941cb5e8a321379ff0cae6ae5c1f592ad8882ca8
pdf_pages: 49-50
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 973ed18f2dfab94578a9d08bad05442a79e9dc64988e713925aa88a3e9f9b7a5
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

We are now in a position to define a rate of generating information for a continuous source. We are given $P(x)$ for the source and an evaluation v determined by a distance function $\rho(x, y)$ which will be assumed continuous in both x and y. With a particular system $P(x, y)$ the quality is measured by

$$
v = \iint \rho(x, y) P(x, y) dx dy.
$$

Furthermore the rate of flow of binary digits corresponding to $P(x, y)$ is

$$
R = \iint P(x, y) \log \frac{P(x, y)}{P(x)P(y)} dx dy.
$$

We define the rate $R_1$ of generating information for a given quality $v_1$ of reproduction to be the minimum of R when we keep v fixed at $v_1$ and vary $P_x(y)$. That is:

$$
R_1 = \min_{P_x(y)} \iint P(x, y) \log \frac{P(x, y)}{P(x)P(y)} dx dy
$$

subject to the constraint:

$$
v_1 = \iint P(x, y)\rho(x, y)\, dx dy.
$$

This means that we consider, in effect, all the communication systems that might be used and that transmit with the required fidelity. The rate of transmission in bits per second is calculated for each one and we choose that having the least rate. This latter rate is the rate we assign the source for the fidelity in question.

The justification of this definition lies in the following result:

Theorem 21: *If a source has a rate R₁ for a valuation v₁ it is possible to encode the output of the source and transmit it over a channel of capacity C with fidelity as near v₁ as desired provided R₁ ≤ C. This is not possible if R₁ > C.* {#shannon-1948-communication-thm-21 .statement tag=04F8}

The last statement in the theorem follows immediately from the definition of R₁ and previous results. If it were not true we could transmit more than C bits per second over a channel of capacity C. The first part of the theorem is proved by a method analogous to that used for Theorem 11. We may, in the first place, divide the (x, y) space into a large number of small cells and represent the situation as a discrete case. This will not change the evaluation function by more than an arbitrarily small amount (when the cells are very small) because of the continuity assumed for $\rho(x, y)$. Suppose that $P_1(x, y)$ is the particular system which minimizes the rate and gives R₁. We choose from the high probability y’s a set at random containing

$$
2^{(R_1 + \epsilon)T}
$$

members where $\epsilon \to 0$ as $T \to \infty$. With large T each chosen point will be connected by a high probability line (as in Fig. 10) to a set of x’s. A calculation similar to that used in proving Theorem 11 shows that with large T almost all x’s are covered by the fans from the chosen y points for almost all choices of the y’s. The communication system to be used operates as follows: The selected points are assigned binary numbers. When a message x is originated it will (with probability approaching 1 as $T \to \infty$) lie within at least one of the fans. The corresponding binary number is transmitted (or one of them chosen arbitrarily if there are several) over the channel by suitable coding means to give a small probability of error. Since $R_1 \leq C$ this is possible. At the receiving point the corresponding y is reconstructed and used as the recovered message.

The evaluation $v'_1$ for this system can be made arbitrarily close to $v_1$ by taking T sufficiently large. This is due to the fact that for each long sample of message x(t) and recovered message y(t) the evaluation approaches $v_1$ (with probability 1).

It is interesting to note that, in this system, the noise in the recovered message is actually produced by a kind of general quantizing at the transmitter and not produced by the noise in the channel. It is more or less analogous to the quantizing noise in PCM.
