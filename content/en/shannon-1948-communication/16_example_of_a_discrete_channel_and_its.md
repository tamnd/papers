---
paper: shannon-1948-communication
title: A Mathematical Theory of Communication
authors:
  - Claude E. Shannon
year: 1948
venue: Bell System Technical Journal
field: theory
section: "15"
section_title: EXAMPLE OF A DISCRETE CHANNEL AND ITS CAPACITY
tag: "04E1"
kind: section
lang: en
source: https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf
pdf_sha256: 6e4e3411984f3edf99dbfe8b941cb5e8a321379ff0cae6ae5c1f592ad8882ca8
pdf_pages: 25-26
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: f7d5574008d80987458a76af8ab33972bfa9c5deae163f1b44406d77e49d0c49
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

A simple example of a discrete channel is indicated in Fig. 11. There are three possible symbols. The first is never affected by noise. The second and third each have probability p of coming through undisturbed, and q of being changed into the other of the pair. We have (letting $\alpha = -[p \log p + q \log q]$ and P and Q be the probabilities of using the first and second symbols)

$$
H(x) = -P \log P - 2Q \log Q \\
H_y(x) = 2Q \alpha.
$$

We wish to choose P and Q in such a way as to maximize $H(x) - H_y(x)$, subject to the constraint $P + 2Q = 1$. Hence we consider

$$
U = -P \log P - 2Q \log Q - 2Q \alpha + \lambda (P + 2Q)
$$

$$
\frac{\partial U}{\partial P} = -1 - \log P + \lambda = 0 \\
\frac{\partial U}{\partial Q} = -2 - 2 \log Q - 2\alpha + 2\lambda = 0.
$$

Eliminating $\lambda$

$$
\log P = \log Q + \alpha \\
P = Q e^\alpha = Q \beta
$$

$$
P = \frac{\beta}{\beta + 2} \qquad Q = \frac{1}{\beta + 2}.
$$

The channel capacity is then

$$
C = \log \frac{\beta + 2}{\beta}.
$$

Note how this checks the obvious values in the cases $p = 1$ and $p = \frac{1}{2}$. In the first, $\beta = 1$ and $C = \log 3$, which is correct since the channel is then noiseless with three possible symbols. If $p = \frac{1}{2}$, $\beta = 2$ and $C = \log 2$. Here the second and third symbols cannot be distinguished at all and act together like one symbol. The first symbol is used with probability $P = \frac{1}{2}$ and the second and third together with probability $\frac{1}{2}$. This may be distributed between them in any desired way and still achieve the maximum capacity.

For intermediate values of $p$ the channel capacity will lie between $\log 2$ and $\log 3$. The distinction between the second and third symbols conveys some information but not as much as in the noiseless case. The first symbol is used somewhat more frequently than the other two because of its freedom from noise.
