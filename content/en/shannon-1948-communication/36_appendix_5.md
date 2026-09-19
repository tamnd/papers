---
paper: shannon-1948-communication
title: A Mathematical Theory of Communication
authors:
  - Claude E. Shannon
year: 1948
venue: Bell System Technical Journal
field: theory
section_title: Appendix 5
kind: appendix
lang: en
source: https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf
pdf_sha256: 6e4e3411984f3edf99dbfe8b941cb5e8a321379ff0cae6ae5c1f592ad8882ca8
pdf_pages: "52"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 7b1449ee83121fe4b3f55767f1c8f6230d7ce66ecb14432cb25e44ba02d3c382
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Let S₁ be any measurable subset of the g ensemble, and S₂ the subset of the f ensemble which gives S₁ under the operation T. Then

$$
S_1 = TS_2.
$$

Let $H^\lambda$ be the operator which shifts all functions in a set by the time $\lambda$. Then

$$
H^\lambda S_1 = H^\lambda TS_2 = TH^\lambda S_2
$$

since T is invariant and therefore commutes with $H^\lambda$. Hence if m[S] is the probability measure of the set S

$$
m[H^\lambda S_1] = m[TH^\lambda S_2] = m[H^\lambda S_2]
= m[S_2] = m[S_1]
$$

where the second equality is by definition of measure in the g space, the third since the f ensemble is stationary, and the last by definition of g measure again.

To prove that the ergodic property is preserved under invariant operations, let S₁ be a subset of the g ensemble which is invariant under $H^\lambda$, and let S₂ be the set of all functions f which transform into S₁. Then

$$
H^\lambda S_1 = H^\lambda TS_2 = TH^\lambda S_2 = S_1
$$

so that $H^\lambda S_2$ is included in S₂ for all $\lambda$. Now, since

$$
m[H^\lambda S_2] = m[S_1]
$$

this implies

$$
H^\lambda S_2 = S_2
$$

for all $\lambda$ with $m[S_2] \neq 0, 1$. This contradiction shows that S₁ does not exist.
