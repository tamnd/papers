---
paper: shannon-1948-communication
title: A Mathematical Theory of Communication
authors:
  - Claude E. Shannon
year: 1948
venue: Bell System Technical Journal
field: theory
section_title: Appendix 2
kind: appendix
lang: en
source: https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf
pdf_sha256: 6e4e3411984f3edf99dbfe8b941cb5e8a321379ff0cae6ae5c1f592ad8882ca8
pdf_pages: 28-29
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 6a88f326d975e4ad0dd34a5e8c4dc618c51ab7ae792fc8e5b5fc813b40bae7d6
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

**DERIVATION OF H = − Σ pᵢ log pᵢ**

Let $H(\frac{1}{n},\frac{1}{n},\ldots,\frac{1}{n})=A(n)$. From condition (3) we can decompose a choice from $s^m$ equally likely possibilities into a series of $m$ choices from $s$ equally likely possibilities and obtain

$$
A(s^m)=mA(s).
$$

Similarly

$$
A(t^n) = nA(t).
$$

We can choose n arbitrarily large and find an m to satisfy

$$
s^m \leq t^n < s^{(m+1)}.
$$

Thus, taking logarithms and dividing by n log s,

$$
\frac{m}{n} \leq \frac{\log t}{\log s} \leq \frac{m}{n} + \frac{1}{n} \quad \text{or} \quad \left| \frac{m}{n} - \frac{\log t}{\log s} \right| < \epsilon
$$

where $\epsilon$ is arbitrarily small. Now from the monotonic property of A(n),

$$
A(s^m) \leq A(t^n) \leq A(s^{m+1}) \\
mA(s) \leq nA(t) \leq (m+1)A(s).
$$

Hence, dividing by nA(s),

$$
\frac{m}{n} \leq \frac{A(t)}{A(s)} \leq \frac{m}{n} + \frac{1}{n} \quad \text{or} \quad \left| \frac{m}{n} - \frac{A(t)}{A(s)} \right| < \epsilon
$$

$$
\left| \frac{A(t)}{A(s)} - \frac{\log t}{\log s} \right| < 2\epsilon \qquad A(t) = K \log t
$$

where K must be positive to satisfy (2).

Now suppose we have a choice from n possibilities with commeasurable probabilities $p_i = \frac{n_i}{\sum n_i}$ where the $n_i$ are integers. We can break down a choice from $\sum n_i$ possibilities into a choice from n possibilities with probabilities $p_1, \ldots, p_n$ and then, if the ith was chosen, a choice from $n_i$ with equal probabilities. Using condition (3) again, we equate the total choice from $\sum n_i$ as computed by two methods

$$
K \log \sum n_i = H(p_1, \ldots, p_n) + K \sum p_i \log n_i.
$$

Hence

$$
H = K \left[ \sum p_i \log \sum n_i - \sum p_i \log n_i \right]
= -K \sum p_i \log \frac{n_i}{\sum n_i} = -K \sum p_i \log p_i.
$$

If the $p_i$ are incommeasurable, they may be approximated by rationals and the same expression must hold by our continuity assumption. Thus the expression holds in general. The choice of coefficient K is a matter of convenience and amounts to the choice of a unit of measure.
