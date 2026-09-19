---
paper: shannon-1948-communication
title: A Mathematical Theory of Communication
authors:
  - Claude E. Shannon
year: 1948
venue: Bell System Technical Journal
field: theory
section: "8"
section_title: REPRESENTATION OF THE ENCODING AND DECODING OPERATIONS
tag: 04D3
kind: section
lang: en
source: https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf
pdf_sha256: 6e4e3411984f3edf99dbfe8b941cb5e8a321379ff0cae6ae5c1f592ad8882ca8
pdf_pages: 15-16
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 9f4fa847617b9a7b7db9ba4f604a7e80fbb82aa172e52c9a68b5f408cf2e2d53
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

We have yet to represent mathematically the operations performed by the transmitter and receiver in encoding and decoding the information. Either of these will be called a discrete transducer. The input to the transducer is a sequence of input symbols and its output a sequence of output symbols. The transducer may have an internal memory so that its output depends not only on the present input symbol but also on the past history. We assume that the internal memory is finite, i.e., there exist a finite number m of possible states of the transducer and that its output is a function of the present state and the present input symbol. The next state will be a second function of these two quantities. Thus a transducer can be described by two functions:

$$
y_n = f(x_n, \alpha_n)
$$

$$
\alpha_{n+1} = g(x_n, \alpha_n)
$$

where

$x_n$ is the n\textsuperscript{th} input symbol,

$\alpha_n$ is the state of the transducer when the n\textsuperscript{th} input symbol is introduced,

$y_n$ is the output symbol (or sequence of output symbols) produced when $x_n$ is introduced if the state is $\alpha_n$.

If the output symbols of one transducer can be identified with the input symbols of a second, they can be connected in tandem and the result is also a transducer. If there exists a second transducer which operates on the output of the first and recovers the original input, the first transducer will be called non-singular and the second will be called its inverse.

Theorem 7: *The output of a finite state transducer driven by a finite state statistical source is a finite state statistical source, with entropy (per unit time) less than or equal to that of the input. If the transducer is non-singular they are equal.* {#shannon-1948-communication-thm-7 .statement tag=04D4}

Let $\alpha$ represent the state of the source, which produces a sequence of symbols $x_i$; and let $\beta$ be the state of the transducer, which produces, in its output, blocks of symbols $y_j$. The combined system can be represented by the “product state space” of pairs $(\alpha, \beta)$. Two points in the space $(\alpha_1, \beta_1)$ and $(\alpha_2, \beta_2)$, are connected by a line if $\alpha_1$ can produce an x which changes $\beta_1$ to $\beta_2$, and this line is given the probability of that x in this case. The line is labeled with the block of $y_j$ symbols produced by the transducer. The entropy of the output can be calculated as the weighted sum over the states. If we sum first on $\beta$ each resulting term is less than or equal to the corresponding term for $\alpha$, hence the entropy is not increased. If the transducer is non-singular let its output be connected to the inverse transducer. If $H'_1, H'_2$ and $H'_3$ are the output entropies of the source, the first and second transducers respectively, then $H'_1 \geq H'_2 \geq H'_3 = H'_1$ and therefore $H'_1 = H'_2$.

Suppose we have a system of constraints on possible sequences of the type which can be represented by a linear graph as in Fig. 2. If probabilities $p_{ij}^{(s)}$ were assigned to the various lines connecting state i to state j this would become a source. There is one particular assignment which maximizes the resulting entropy (see Appendix 4).

Theorem 8: *Let the system of constraints considered as a channel have a capacity* $C = \log W$. *If we assign* {#shannon-1948-communication-thm-8 .statement tag=04D5}

$$
p_{ij}^{(s)} = \frac{B_j}{B_i} W^{-\ell_{ij}^{(s)}}
$$

*where* $\ell_{ij}^{(s)}$ *is the duration of the* $s^{th}$ *symbol leading from state i to state j and the* $B_i$ *satisfy*

$$
B_i = \sum_{s,j} B_j W^{-\ell_{ij}^{(s)}}
$$

*then* $H$ *is maximized and equal to* $C$.

By proper assignment of the transition probabilities the entropy of symbols on a channel can be maximized at the channel capacity.
