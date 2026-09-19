---
paper: shannon-1948-communication
title: A Mathematical Theory of Communication
authors:
  - Claude E. Shannon
year: 1948
venue: Bell System Technical Journal
field: theory
section_title: Appendix 3
kind: appendix
lang: en
source: https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf
pdf_sha256: 6e4e3411984f3edf99dbfe8b941cb5e8a321379ff0cae6ae5c1f592ad8882ca8
pdf_pages: 29-30
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: d8686218b04de5ba7fbead254aaff8395cc54fc89ff0b2b4f14e22204f68ffc8
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

THEOREMS ON ERGODIC SOURCES

If it is possible to go from any state with $P > 0$ to any other along a path of probability $p > 0$, the system is ergodic and the strong law of large numbers can be applied. Thus the number of times a given path $p_{ij}$ in the network is traversed in a long sequence of length N is about proportional to the probability of being at i, say $P_i$, and then choosing this path, $P_i p_{ij} N$. If N is large enough the probability of percentage error $\pm \delta$ in this is less than $\epsilon$ so that for all but a set of small probability the actual numbers lie within the limits

$$
(P_i p_{ij} \pm \delta)N.
$$

Hence nearly all sequences have a probability p given by

$$
p = \prod p_{ij}^{(P_i p_{ij} \pm \delta)N}
$$

and $\frac{\log p}{N}$ is limited by

$$
\frac{\log p}{N} = \sum (P_i p_{ij} \pm \delta) \log p_{ij}
$$

or

$$
\left| \frac{\log p}{N} - \sum P_i p_{ij} \log p_{ij} \right| < \eta.
$$

This proves Theorem 3.

Theorem 4 follows immediately from this on calculating upper and lower bounds for n(q) based on the possible range of values of p in Theorem 3. {#shannon-1948-communication-thm-4-2 .statement tag=04E4}

In the mixed (not ergodic) case if

$$
L = \sum p_i L_i
$$

and the entropies of the components are $H_1 \geq H_2 \geq \cdots \geq H_n$ we have the

Theorem: $\lim_{N \to \infty} \frac{\log n(q)}{N} = \varphi(q)$ *is a decreasing step function*,

$$
\varphi(q) = H_s \quad \text{*in the interval*} \quad \sum_1^{s-1} \alpha_i < q < \sum_1^s \alpha_i.
$$

To prove Theorems 5 and 6 first note that $F_N$ is monotonic decreasing because increasing N adds a subscript to a conditional entropy. A simple substitution for $p_{B_i}(S_j)$ in the definition of $F_N$ shows that

$$
F_N = N G_N - (N-1) G_{N-1}
$$

and summing this for all N gives $G_N = \frac{1}{N} \sum F_n$. Hence $G_N \geq F_N$ and $G_N$ monotonic decreasing. Also they must approach the same limit. By using Theorem 3 we see that $\lim_{N \to \infty} G_N = H$.
