---
paper: shannon-1948-communication
title: A Mathematical Theory of Communication
authors:
  - Claude E. Shannon
year: 1948
venue: Bell System Technical Journal
field: theory
section: "11"
section_title: REPRESENTATION OF A NOISY DISCRETE CHANNEL
tag: 04D9
kind: section
lang: en
source: https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf
pdf_sha256: 6e4e3411984f3edf99dbfe8b941cb5e8a321379ff0cae6ae5c1f592ad8882ca8
pdf_pages: "19"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 6de5367399be4446d8cfeaa917e0a811dcdaf0ce70ab409754b2618e05ac4942
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

We now consider the case where the signal is perturbed by noise during transmission or at one or the other of the terminals. This means that the received signal is not necessarily the same as that sent out by the transmitter. Two cases may be distinguished. If a particular transmitted signal always produces the same received signal, i.e., the received signal is a definite function of the transmitted signal, then the effect may be called distortion. If this function has an inverse — no two transmitted signals producing the same received signal — distortion may be corrected, at least in principle, by merely performing the inverse functional operation on the received signal.

The case of interest here is that in which the signal does not always undergo the same change in transmission. In this case we may assume the received signal E to be a function of the transmitted signal S and a second variable, the noise N.

$$
E = f(S, N)
$$

The noise is considered to be a chance variable just as the message was above. In general it may be represented by a suitable stochastic process. The most general type of noisy discrete channel we shall consider is a generalization of the finite state noise-free channel described previously. We assume a finite number of states and a set of probabilities

$$
p_{\alpha, i}(\beta, j).
$$

This is the probability, if the channel is in state $\alpha$ and symbol i is transmitted, that symbol j will be received and the channel left in state $\beta$. Thus $\alpha$ and $\beta$ range over the possible states, i over the possible transmitted signals and j over the possible received signals. In the case where successive symbols are independently perturbed by the noise there is only one state, and the channel is described by the set of transition probabilities $p_i(j)$, the probability of transmitted symbol i being received as j.

If a noisy channel is fed by a source there are two statistical processes at work: the source and the noise. Thus there are a number of entropies that can be calculated. First there is the entropy $H(x)$ of the source or of the input to the channel (these will be equal if the transmitter is non-singular). The entropy of the output of the channel, i.e., the received signal, will be denoted by $H(y)$. In the noiseless case $H(y) = H(x)$. The joint entropy of input and output will be $H(xy)$. Finally there are two conditional entropies $H_x(y)$ and $H_y(x)$, the entropy of the output when the input is known and conversely. Among these quantities we have the relations

$$
H(x, y) = H(x) + H_x(y) = H(y) + H_y(x).
$$

All of these entropies can be measured on a per-second or a per-symbol basis.
