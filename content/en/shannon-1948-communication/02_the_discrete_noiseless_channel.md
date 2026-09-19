---
paper: shannon-1948-communication
title: A Mathematical Theory of Communication
authors:
  - Claude E. Shannon
year: 1948
venue: Bell System Technical Journal
field: theory
section: "1"
section_title: THE DISCRETE NOISELESS CHANNEL
tag: 04C6
kind: section
lang: en
source: https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf
pdf_sha256: 6e4e3411984f3edf99dbfe8b941cb5e8a321379ff0cae6ae5c1f592ad8882ca8
pdf_pages: 3-4
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: e39fb765255260af17b601ed2f09ccd02218b21f6b3e628c04a74b6c152d9a68
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Teletype and telegraphy are two simple examples of a discrete channel for transmitting information. Generally, a discrete channel will mean a system whereby a sequence of choices from a finite set of elementary symbols S₁, ..., Sₙ can be transmitted from one point to another. Each of the symbols Sᵢ is assumed to have a certain duration in time tᵢ seconds (not necessarily the same for different Sᵢ, for example the dots and dashes in telegraphy). It is not required that all possible sequences of the Sᵢ be capable of transmission on the system; certain sequences only may be allowed. These will be possible signals for the channel. Thus in telegraphy suppose the symbols are: (1) A dot, consisting of line closure for a unit of time and then line open for a unit of time; (2) A dash, consisting of three time units of closure and one unit open; (3) A letter space consisting of, say, three units of line open; (4) A word space of six units of line open. We might place the restriction on allowable sequences that no spaces follow each other (for if two letter spaces are adjacent, it is identical with a word space). The question we now consider is how one can measure the capacity of such a channel to transmit information.

In the teletype case where all symbols are of the same duration, and any sequence of the 32 symbols is allowed the answer is easy. Each symbol represents five bits of information. If the system transmits n symbols per second it is natural to say that the channel has a capacity of 5n bits per second. This does not mean that the teletype channel will always be transmitting information at this rate — this is the maximum possible rate and whether or not the actual rate reaches this maximum depends on the source of information which feeds the channel, as will appear later.

In the more general case with different lengths of symbols and constraints on the allowed sequences, we make the following definition:
Definition: The capacity C of a discrete channel is given by

$$
C = \lim_{T \to \infty} \frac{\log N(T)}{T}
$$

where N(T) is the number of allowed signals of duration T.

It is easily seen that in the teletype case this reduces to the previous result. It can be shown that the limit in question will exist as a finite number in most cases of interest. Suppose all sequences of the symbols S₁, ..., Sₙ are allowed and these symbols have durations t₁, ..., tₙ. What is the channel capacity? If N(t) represents the number of sequences of duration t we have

$$
N(t) = N(t - t_1) + N(t - t_2) + \cdots + N(t - t_n).
$$

The total number is equal to the sum of the numbers of sequences ending in S₁, S₂, ..., Sₙ and these are N(t − t₁), N(t − t₂), ..., N(t − tₙ), respectively. According to a well-known result in finite differences, N(t) is then asymptotic for large t to X₀ᵗ where X₀ is the largest real solution of the characteristic equation:

$$
X^{-t_1} + X^{-t_2} + \cdots + X^{-t_n} = 1
$$

and therefore

$$
C = \log X_0.
$$

In case there are restrictions on allowed sequences we may still often obtain a difference equation of this type and find C from the characteristic equation. In the telegraphy case mentioned above

$$
N(t) = N(t-2) + N(t-4) + N(t-5) + N(t-7) + N(t-8) + N(t-10)
$$

as we see by counting sequences of symbols according to the last or next to the last symbol occurring. Hence C is $-\log \mu_0$ where $\mu_0$ is the positive root of $1 = \mu^2 + \mu^4 + \mu^5 + \mu^7 + \mu^8 + \mu^{10}$. Solving this we find $C = 0.539$.

A very general type of restriction which may be placed on allowed sequences is the following: We imagine a number of possible states $a_1, a_2, \ldots, a_m$. For each state only certain symbols from the set $S_1, \ldots, S_n$ can be transmitted (different subsets for the different states). When one of these has been transmitted the state changes to a new state depending both on the old state and the particular symbol transmitted. The telegraph case is a simple example of this. There are two states depending on whether or not a space was the last symbol transmitted. If so, then only a dot or a dash can be sent next and the state always changes. If not, any symbol can be transmitted and the state changes if a space is sent, otherwise it remains the same. The conditions can be indicated in a linear graph as shown in Fig. 2. The junction points correspond to the

Figure.

Fig. 2 — Graphical representation of the constraints on telegraph symbols.

states and the lines indicate the symbols possible in a state and the resulting state. In Appendix 1 it is shown that if the conditions on allowed sequences can be described in this form C will exist and can be calculated in accordance with the following result:

Theorem 1: *Let* $b_{ij}^{(s)}$ *be the duration of the s*$^{th}$ *symbol which is allowable in state i and leads to state j.* *Then the channel capacity C is equal to* $\log W$ *where W is the largest real root of the determinant equation:* {#shannon-1948-communication-thm-1 .statement tag=04C7}

$$
\left| \sum_s W^{-b_{ij}^{(s)}} - \delta_{ij} \right| = 0
$$

*where* $\delta_{ij} = 1$ *if* $i = j$ *and is zero otherwise.*

For example, in the telegraph case (Fig. 2) the determinant is:

$$
\begin{vmatrix}
-1 & (W^{-2} + W^{-4}) \\
(W^{-3} + W^{-6}) & (W^{-2} + W^{-4} - 1)
\end{vmatrix} = 0.
$$

On expansion this leads to the equation given above for this case.
