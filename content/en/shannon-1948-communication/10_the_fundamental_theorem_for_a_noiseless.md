---
paper: shannon-1948-communication
title: A Mathematical Theory of Communication
authors:
  - Claude E. Shannon
year: 1948
venue: Bell System Technical Journal
field: theory
section: "9"
section_title: THE FUNDAMENTAL THEOREM FOR A NOISELESS CHANNEL
tag: 04D6
kind: section
lang: en
source: https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf
pdf_sha256: 6e4e3411984f3edf99dbfe8b941cb5e8a321379ff0cae6ae5c1f592ad8882ca8
pdf_pages: 16-17
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: dfc0535ee19631be66b32ac6b7297bd02cdb50969d8ec59f7dc19825f6360a4e
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

We will now justify our interpretation of $H$ as the rate of generating information by proving that $H$ determines the channel capacity required with most efficient coding.

Theorem 9: *Let a source have entropy* $H$ *(bits per symbol)* *and a channel have a capacity* $C$ *(bits per second)*. *Then it is possible to encode the output of the source in such a way as to transmit at the average rate* $\frac{C}{H} - \epsilon$ *symbols per second over the channel where* $\epsilon$ *is arbitrarily small. It is not possible to transmit at an average rate greater than* $\frac{C}{H}$. {#shannon-1948-communication-thm-9 .statement tag=04D7}

The converse part of the theorem, that $\frac{C}{H}$ cannot be exceeded, may be proved by noting that the entropy of the channel input per second is equal to that of the source, since the transmitter must be non-singular, and also this entropy cannot exceed the channel capacity. Hence $H' \leq C$ and the number of symbols per second $= H'/H \leq C/H$.

The first part of the theorem will be proved in two different ways. The first method is to consider the set of all sequences of N symbols produced by the source. For N large we can divide these into two groups, one containing less than $2^{(H+\eta)N}$ members and the second containing less than $2^{RN}$ members (where R is the logarithm of the number of different symbols) and having a total probability less than $\mu$. As N increases $\eta$ and $\mu$ approach zero. The number of signals of duration T in the channel is greater than $2^{(C-\theta)T}$ with $\theta$ small when T is large. if we choose

$$
T = \left( \frac{H}{C} + \lambda \right) N
$$

then there will be a sufficient number of sequences of channel symbols for the high probability group when N and T are sufficiently large (however small $\lambda$) and also some additional ones. The high probability group is coded in an arbitrary one-to-one way into this set. The remaining sequences are represented by larger sequences, starting and ending with one of the sequences not used for the high probability group. This special sequence acts as a start and stop signal for a different code. In between a sufficient time is allowed to give enough different sequences for all the low probability messages. This will require

$$
T_1 = \left( \frac{R}{C} + \varphi \right) N
$$

where $\varphi$ is small. The mean rate of transmission in message symbols per second will then be greater than

$$
\left[ (1-\delta) \frac{T}{N} + \delta \frac{T_1}{N} \right]^{-1} = \left[ (1-\delta) \left( \frac{H}{C} + \lambda \right) + \delta \left( \frac{R}{C} + \varphi \right) \right]^{-1}.
$$

As N increases $\delta, \lambda$ and $\varphi$ approach zero and the rate approaches $\frac{C}{H}$.

Another method of performing this coding and thereby proving the theorem can be described as follows: Arrange the messages of length N in order of decreasing probability and suppose their probabilities are $p_1 \geq p_2 \geq p_3 \cdots \geq p_n$. Let $P_s = \sum_{i=1}^{s-1} p_i$; that is $P_s$ is the cumulative probability up to, but not including, $p_s$. We first encode into a binary system. The binary code for message s is obtained by expanding $P_s$ as a binary number. The expansion is carried out to $m_s$ places, where $m_s$ is the integer satisfying:

$$
\log_2 \frac{1}{p_s} \leq m_s < 1 + \log_2 \frac{1}{p_s}
$$

Thus the messages of high probability are represented by short codes and those of low probability by long codes. From these inequalities we have

$$
\frac{1}{2^{m_s}} \leq p_s < \frac{1}{2^{m_s-1}}
$$

The code for $P_s$ will differ from all succeeding ones in one or more of its $m_s$ places, since all the remaining $P_i$ are at least $\frac{1}{2^{m_s}}$ larger and their binary expansions therefore differ in the first $m_s$ places. Consequently all the codes are different and it is possible to recover the message from its code. If the channel sequences are not already sequences of binary digits, they can be ascribed binary numbers in an arbitrary fashion and the binary code thus translated into signals suitable for the channel.

The average number $H'$ of binary digits used per symbol of original message is easily estimated. We have

$$
H' = \frac{1}{N} \sum m_s p_s.
$$

But,

$$
\frac{1}{N} \sum \left( \log_2 \frac{1}{p_s} \right) p_s \leq \frac{1}{N} \sum m_s p_s < \frac{1}{N} \sum \left( 1 + \log_2 \frac{1}{p_s} \right) p_s
$$

and therefore,

$$
G_N \leq H' < G_N + \frac{1}{N}
$$

As N increases $G_N$ approaches H, the entropy of the source and $H'$ approaches H.

We see from this that the inefficiency in coding, when only a finite delay of N symbols is used, need not be greater than $\frac{1}{N}$ plus the difference between the true entropy H and the entropy $G_N$ calculated for sequences of length N. The per cent excess time needed over the ideal is therefore less than

$$
\frac{G_N}{H} + \frac{1}{HN} - 1.
$$

This method of encoding is substantially the same as one found independently by R. M. Fano.\footnote{Technical Report No. 65, The Research Laboratory of Electronics, M.I.T., March 17, 1949.} His method is to arrange the messages of length N in order of decreasing probability. Divide this series into two groups of as nearly equal probability as possible. If the message is in the first group its first binary digit will be 0, otherwise 1. The groups are similarly divided into subsets of nearly equal probability and the particular subset determines the second binary digit. This process is continued until each subset contains only one message. It is easily seen that apart from minor differences (generally in the last digit) this amounts to the same thing as the arithmetic process described above.
