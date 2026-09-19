---
paper: shannon-1948-communication
title: A Mathematical Theory of Communication
authors:
  - Claude E. Shannon
year: 1948
venue: Bell System Technical Journal
field: theory
section: "16"
section_title: THE CHANNEL CAPACITY IN CERTAIN SPECIAL CASES
tag: "04E2"
kind: section
lang: en
source: https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf
pdf_sha256: 6e4e3411984f3edf99dbfe8b941cb5e8a321379ff0cae6ae5c1f592ad8882ca8
pdf_pages: 26-27
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 5e29dbe694d29d96a3b1fae06f5a23e5d0f79714197cc42e269c8080ad547774
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

If the noise affects successive channel symbols independently it can be described by a set of transition probabilities $p_{ij}$. This is the probability, if symbol i is sent, that j will be received. The maximum channel rate is then given by the maximum of

$$
-\sum_{i,j} P_i p_{ij} \log \sum_i P_i p_{ij} + \sum_{i,j} P_i p_{ij} \log p_{ij}
$$

where we vary the $P_i$ subject to $\sum P_i = 1$. This leads by the method of Lagrange to the equations,

$$
\sum_j p_{sj} \log \frac{p_{sj}}{\sum_i P_i p_{ij}} = \mu \qquad s = 1, 2, \ldots .
$$

Multiplying by $P_s$ and summing on s shows that $\mu = C$. Let the inverse of $p_{sj}$ (if it exists) be $h_{st}$ so that $\sum_s h_{st} p_{sj} = \delta_{tj}$. Then:

$$
\sum_{s,j} h_{st} p_{sj} \log p_{sj} - \log \sum_i P_i p_{it} = C \sum_s h_{st} .
$$

Hence:

$$
\sum_i P_i p_{it} = \exp \left[ -C \sum_s h_{st} + \sum_{s,j} h_{st} p_{sj} \log p_{sj} \right]
$$

or,

$$
P_i = \sum_t h_{it} \exp \left[ -C \sum_s h_{st} + \sum_{s,j} h_{st} p_{sj} \log p_{sj} \right].
$$

This is the system of equations for determining the maximizing values of $P_i$, with $C$ to be determined so that $\sum P_i = 1$. When this is done $C$ will be the channel capacity, and the $P_i$ the proper probabilities for the channel symbols to achieve this capacity.

If each input symbol has the same set of probabilities on the lines emerging from it, and the same is true of each output symbol, the capacity can be easily calculated. Examples are shown in Fig. 12. In such a case $H_x(y)$ is independent of the distribution of probabilities on the input symbols, and is given by $- \sum p_i \log p_i$ where the $p_i$ are the values of the transition probabilities from any input symbol. The channel capacity is

$$
\operatorname{Max} [H(y) - H_x(y)] = \operatorname{Max} H(y) + \sum p_i \log p_i.
$$

The maximum of $H(y)$ is clearly $\log m$ where $m$ is the number of output symbols, since it is possible to make them all equally probable by making the input symbols equally probable. The channel capacity is therefore

$$
C = \log m + \sum p_i \log p_i.
$$

Fig. 12 — Examples of discrete channels with the same transition probabilities for each input and for each output.

In Fig. 12a it would be

$$
C = \log 4 - \log 2 = \log 2.
$$

This could be achieved by using only the 1st and 3d symbols. In Fig. 12b

$$
\begin{align*}
C &= \log 4 - \frac{2}{3} \log 3 - \frac{1}{3} \log 6 \\
&= \log 4 - \log 3 - \frac{1}{3} \log 2 \\
&= \log \frac{1}{3} 2^{\frac{5}{3}}.
\end{align*}
$$

In Fig. 12c we have

$$
\begin{align*}
C &= \log 3 - \frac{1}{2} \log 2 - \frac{1}{3} \log 3 - \frac{1}{6} \log 6 \\
&= \log \frac{3}{2^{\frac{1}{2}} 3^{\frac{1}{3}} 6^{\frac{1}{6}}}.
\end{align*}
$$

Suppose the symbols fall into several groups such that the noise never causes a symbol in one group to be mistaken for a symbol in another group. Let the capacity for the nth group be $C_n$ (in bits per second) when we use only the symbols in this group. Then it is easily shown that, for best use of the entire set, the total probability $P_n$ of all symbols in the nth group should be

$$
P_n = \frac{2^{C_n}}{\sum 2^{C_n}}.
$$

Within a group the probability is distributed just as it would be if these were the only symbols being used. The channel capacity is

$$
C = \log \sum 2^{C_n}.
$$
