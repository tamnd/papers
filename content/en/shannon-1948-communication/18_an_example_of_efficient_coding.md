---
paper: shannon-1948-communication
title: A Mathematical Theory of Communication
authors:
  - Claude E. Shannon
year: 1948
venue: Bell System Technical Journal
field: theory
section: "17"
section_title: AN EXAMPLE OF EFFICIENT CODING
tag: "04E3"
kind: section
lang: en
source: https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf
pdf_sha256: 6e4e3411984f3edf99dbfe8b941cb5e8a321379ff0cae6ae5c1f592ad8882ca8
pdf_pages: 27-28
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: bd494b0ca240d63ba32885d28daab7f50df6bd737ddef0160df818842e52a062
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The following example, although somewhat unrealistic, is a case in which exact matching to a noisy channel is possible. There are two channel symbols, 0 and 1, and the noise affects them in blocks of seven symbols. A block of seven is either transmitted without error, or exactly one symbol of the seven is incorrect. These eight possibilities are equally likely. We have

$$
\begin{align*}
C &= \operatorname{Max} [H(y) - H_x(y)] \\
&= \frac{1}{7} [7 + \frac{8}{8} \log \frac{1}{8}] \\
&= \frac{4}{7} \text{ bits/symbol}.
\end{align*}
$$

An efficient code, allowing complete correction of errors and transmitting at the rate $C$, is the following (found by a method due to R. Hamming):

Let a block of seven symbols be X₁, X₂, . . . , X₇. Of these X₃, X₅, X₆ and X₇ are message symbols and chosen arbitrarily by the source. The other three are redundant and calculated as follows:

$$
X_4\text{ is chosen to make }\alpha=X_4+X_5+X_6+X_7\quad\text{even}
$$

$$
X_2\text{ “  “  “  “ }\beta=X_2+X_3+X_6+X_7\quad\text{“}
$$

$$
X_1\text{ “  “  “  “ }\gamma=X_1+X_3+X_5+X_7\quad\text{“}
$$

When a block of seven is received $\alpha,\beta$ and $\gamma$ are calculated and if even called zero, if odd called one. The binary number $\alpha\beta\gamma$ then gives the subscript of the $X_i$ that is incorrect (if 0 there was no error).
