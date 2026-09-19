---
paper: shannon-1948-communication
title: A Mathematical Theory of Communication
authors:
  - Claude E. Shannon
year: 1948
venue: Bell System Technical Journal
field: theory
section: "13"
section_title: The Fundamental Theorem for a Discrete Channel with Noise
tag: 04DC
kind: section
lang: en
source: https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf
pdf_sha256: 6e4e3411984f3edf99dbfe8b941cb5e8a321379ff0cae6ae5c1f592ad8882ca8
pdf_pages: 22-24
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 6d9de66ff7fed46a652c357cbe03698ceb9311c9efdb73b130cc46de7b2f00ac
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

It may seem surprising that we should define a definite capacity C for a noisy channel since we can never send certain information in such a case. It is clear, however, that by sending the information in a redundant form the probability of errors can be reduced. For example, by repeating the message many times and by a statistical study of the different received versions of the message the probability of errors could be made very small. One would expect, however, that to make this probability of errors approach zero, the redundancy of the encoding must increase indefinitely, and the rate of transmission therefore approach zero. This is by no means true. If it were, there would not be a very well defined capacity, but only a capacity for a given frequency of errors, or a given equivocation; the capacity going down as the error requirements are made more stringent. Actually the capacity C defined above has a very definite significance. It is possible to send information at the rate C through the channel with as small a frequency of errors or equivocation as desired by proper encoding. This statement is not true for any rate greater than C. If an attempt is made to transmit at a higher rate than C, say C+R₁, then there will necessarily be an equivocation equal to or greater than the excess R₁. Nature takes payment by requiring just that much uncertainty, so that we are not actually getting any more than C through correctly.

The situation is indicated in Fig. 9. The rate of information into the channel is plotted horizontally and the equivocation vertically. Any point above the heavy line in the shaded region can be attained and those below cannot. The points on the line cannot in general be attained, but there will usually be two points on the line that can.

These results are the main justification for the definition of C and will now be proved.

**Theorem 11:** *Let a discrete channel have the capacity C and a discrete source the entropy per second H. If H ≤ C there exists a coding system such that the output of the source can be transmitted over the channel with an arbitrarily small frequency of errors (or an arbitrarily small equivocation). If H > C it is possible to encode the source so that the equivocation is less than H − C + ε where ε is arbitrarily small. There is no method of encoding which gives an equivocation less than H − C.* {#shannon-1948-communication-thm-11 .statement tag=04DD}

The method of proving the first part of this theorem is not by exhibiting a coding method having the desired properties, but by showing that such a code must exist in a certain group of codes. In fact we will average the frequency of errors over this group and show that this average can be made less than $\epsilon$. If the average of a set of numbers is less than $\epsilon$ there must exist at least one in the set which is less than $\epsilon$. This will establish the desired result.

Figure 9. The equivocation possible for a given input entropy to a channel. {#shannon-1948-communication-fig-9 .figure tag=04DE}

The capacity C of a noisy channel has been defined as

$$
C = \operatorname{Max}\left(H(x) - H_y(x)\right)
$$

where x is the input and y the output. The maximization is over all sources which might be used as input to the channel.

Let $S_0$ be a source which achieves the maximum capacity C. If this maximum is not actually achieved by any source let $S_0$ be a source which approximates to giving the maximum rate. Suppose $S_0$ is used as input to the channel. We consider the possible transmitted and received sequences of a long duration T. The following will be true:
1. The transmitted sequences fall into two classes, a high probability group with about $2^{TH(x)}$ members and the remaining sequences of small total probability.
2. Similarly the received sequences have a high probability set of about $2^{TH(y)}$ members and a low probability set of remaining sequences.
3. Each high probability output could be produced by about $2^{TH_y(x)}$ inputs. The probability of all other cases has a small total probability.

All the $\epsilon$'s and $\delta$'s implied by the words “small” and “about” in these statements approach zero as we allow T to increase and $S_0$ to approach the maximizing source.

The situation is summarized in Fig. 10 where the input sequences are points on the left and output sequences points on the right. The fan of cross lines represents the range of possible causes for a typical output.

Figure.

Fig. 10 — Schematic representation of the relations between inputs and outputs in a channel.

Now suppose we have another source producing information at rate R with $R < C$. In the period T this source will have $2^{TR}$ high probability messages. We wish to associate these with a selection of the possible channel inputs in such a way as to get a small frequency of errors. We will set up this association in all possible ways (using, however, only the high probability group of inputs as determined by the source S₀) and average the frequency of errors for this large class of possible coding systems. This is the same as calculating the frequency of errors for a random association of the messages and channel inputs of duration T. Suppose a particular output y₁ is observed. What is the probability of more than one message in the set of possible causes of y₁? There are $2^{TR}$ messages distributed at random in $2^{TH(x)}$ points. The probability of a particular point being a message is thus

$$
2^{T(R-H(x))}.
$$

The probability that none of the points in the fan is a message (apart from the actual originating message) is

$$
P = \left[1 - 2^{T(R-H(x))}\right]^{2^{TH(x)}}.
$$

Now $R < H(x) - H_y(x)$ so $R - H(x) = -H_y(x) - \eta$ with $\eta$ positive. Consequently

$$
P = \left[1 - 2^{-TH_y(x)-T\eta}\right]^{2^{TH_y(x)}}
$$

approaches (as $T \to \infty$)

$$
1 - 2^{-T\eta}.
$$

Hence the probability of an error approaches zero and the first part of the theorem is proved.

The second part of the theorem is easily shown by noting that we could merely send C bits per second from the source, completely neglecting the remainder of the information generated. At the receiver the neglected part gives an equivocation $H(x) - C$ and the part transmitted need only add $\epsilon$. This limit can also be attained in many other ways, as will be shown when we consider the continuous case.

The last statement of the theorem is a simple consequence of our definition of C. Suppose we can encode a source with $H(x) = C + a$ in such a way as to obtain an equivocation $H_y(x) = a - \epsilon$ with $\epsilon$ positive. Then $R = H(x) = C + a$ and

$$
H(x) - H_y(x) = C + \epsilon
$$

with $\epsilon$ positive. This contradicts the definition of C as the maximum of $H(x) - H_y(x)$.

Actually more has been proved than was stated in the theorem. If the average of a set of numbers is within $\epsilon$ of of their maximum, a fraction of at most $\sqrt{\epsilon}$ can be more than $\sqrt{\epsilon}$ below the maximum. Since $\epsilon$ is arbitrarily small we can say that almost all the systems are arbitrarily close to the ideal.
