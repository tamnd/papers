---
paper: shannon-1948-communication
title: A Mathematical Theory of Communication
authors:
  - Claude E. Shannon
year: 1948
venue: Bell System Technical Journal
field: theory
section_title: Appendix 1
kind: appendix
lang: en
source: https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf
pdf_sha256: 6e4e3411984f3edf99dbfe8b941cb5e8a321379ff0cae6ae5c1f592ad8882ca8
pdf_pages: "28"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 02889d5296373a8293939c4158bb9203425cfd858227d1260f78ef6aa4c0dcc1
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

**THE GROWTH OF THE NUMBER OF BLOCKS OF SYMBOLS WITH A FINITE STATE CONDITION**

Let $N_i(L)$ be the number of blocks of symbols of length $L$ ending in state i. Then we have

$$
N_j(L)=\sum_{i,s}N_i(L-b_{ij}^{(s)})
$$

where $b_{ij}^1,b_{ij}^2,\ldots,b_{ij}^m$ are the length of the symbols which may be chosen in state i and lead to state j. These are linear difference equations and the behavior as $L\rightarrow\infty$ must be of the type

$$
N_j=A_jW^L.
$$

Substituting in the difference equation

$$
A_jW^L=\sum_{i,s}A_iW^{L-b_{ij}^{(s)}}
$$

or

$$
A_j=\sum_{i,s}A_iW^{-b_{ij}^{(s)}}
$$

$$
\sum_i\left(\sum_sW^{-b_{ij}^{(s)}}-\delta_{ij}\right)A_i=0.
$$

For this to be possible the determinant

$$
D(W)=|a_{ij}|=\left|\sum_sW^{-b_{ij}^{(s)}}-\delta_{ij}\right|
$$

must vanish and this determines $W$, which is, of course, the largest real root of $D=0$.

The quantity C is then given by

$$
C=\lim_{L\rightarrow\infty}\frac{\log\sum A_jW^L}{L}=\log W
$$

and we also note that the same growth properties result if we require that all blocks start in the same (arbitrarily chosen) state.
