---
paper: shannon-1948-communication
title: A Mathematical Theory of Communication
authors:
  - Claude E. Shannon
year: 1948
venue: Bell System Technical Journal
field: theory
section: "2"
section_title: THE DISCRETE SOURCE OF INFORMATION
tag: 04C8
kind: section
lang: en
source: https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf
pdf_sha256: 6e4e3411984f3edf99dbfe8b941cb5e8a321379ff0cae6ae5c1f592ad8882ca8
pdf_pages: 4-7
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: bf2dbcd6b49c0f8fe70f2e3dd36d0a0a3a4247c8edb5c639c540acdf36eabfda
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

We have seen that under very general conditions the logarithm of the number of possible signals in a discrete channel increases linearly with time. The capacity to transmit information can be specified by giving this rate of increase, the number of bits per second required to specify the particular signal used.

We now consider the information source. How is an information source to be described mathematically, and how much information in bits per second is produced in a given source? The main point at issue is the effect of statistical knowledge about the source in reducing the required capacity of the channel, by the use of proper encoding of the information. In telegraphy, for example, the messages to be transmitted consist of sequences of letters. These sequences, however, are not completely random. In general, they form sentences and have the statistical structure of, say, English. The letter E occurs more frequently than Q, the sequence TH more frequently than XP, etc. The existence of this structure allows one to make a saving in time (or channel capacity) by properly encoding the message sequences into signal sequences. This is already done to a limited extent in telegraphy by using the shortest channel symbol, a dot, for the most common English letter E; while the infrequent letters, Q, X, Z are represented by longer sequences of dots and dashes. This idea is carried still further in certain commercial codes where common words and phrases are represented by four- or five-letter code groups with a considerable saving in average time. The standardized greeting and anniversary telegrams now in use extend this to the point of encoding a sentence or two into a relatively short sequence of numbers.

We can think of a discrete source as generating the message, symbol by symbol. It will choose successive symbols according to certain probabilities depending, in general, on preceding choices as well as the particular symbols in question. A physical system, or a mathematical model of a system which produces such a sequence of symbols governed by a set of probabilities, is known as a stochastic process.$^3$ We may consider a discrete source, therefore, to be represented by a stochastic process. Conversely, any stochastic process which produces a discrete sequence of symbols chosen from a finite set may be considered a discrete source. This will include such cases as:

1. Natural written languages such as English, German, Chinese.

2. Continuous information sources that have been rendered discrete by some quantizing process. For example, the quantized speech from a PCM transmitter, or a quantized television signal.

3. Mathematical cases where we merely define abstractly a stochastic process which generates a sequence of symbols. The following are examples of this last type of source.

(A) Suppose we have five letters A, B, C, D, E which are chosen each with probability .2, successive choices being independent. This would lead to a sequence of which the following is a typical example.
B D C B C E C C C A D C B D D A A E C E E A
A B B D A E E C A C E E B A E E C B C E A D.
This was constructed with the use of a table of random numbers.$^4$

(B) Using the same five letters let the probabilities be .4, .1, .2, .2, .1, respectively, with successive choices independent. A typical message from this source is then:
A A A C D C B D C E A A D A D A C E D A
E A D C A B E D A D D C E C A A A A A D.

(C) A more complicated structure is obtained if successive symbols are not chosen independently but their probabilities depend on preceding letters. In the simplest case of this type a choice depends only on the preceding letter and not on ones before that. The statistical structure can then be described by a set of transition probabilities $p_i(j)$, the probability that letter i is followed by letter j. The indices i and j range over all the possible symbols. A second equivalent way of specifying the structure is to give the “digram” probabilities $p(i, j)$, i.e., the relative frequency of the digram i j. The letter frequencies $p(i)$, (the probability of letter i), the transition probabilities

$^3$See, for example, S. Chandrasekhar, “Stochastic Problems in Physics and Astronomy,” Reviews of Modern Physics, v. 15, No. 1, January 1943, p. 1.
$^4$Kendall and Smith, Tables of Random Sampling Numbers, Cambridge, 1939.

p_i(j) and the digram probabilities p(i, j) are related by the following formulas:

$$
p(i) = \sum_j p(i, j) = \sum_j p(j, i) = \sum_j p(j)p_j(i)
$$

$$
p(i, j) = p(i)p_i(j)
$$

$$
\sum_j p_i(j) = \sum_i p(i) = \sum_{i,j} p(i, j) = 1.
$$

As a specific example suppose there are three letters A, B, C with the probability tables:

```text
pᵢ(j)  j  p(i)  p(i, j)  j
  A  B  C      A  B  C
A  0  \frac{4}{5}  \frac{1}{5}  A  \frac{9}{27}  A  0  \frac{4}{15}  \frac{1}{15}
i B  \frac{1}{2}  \frac{1}{2}  0  B  \frac{16}{27}  i B  \frac{8}{27}  \frac{8}{27}  0
C  \frac{1}{2}  \frac{2}{5}  \frac{1}{10}  C  \frac{2}{27}  C  \frac{1}{27}  \frac{4}{135}  \frac{1}{135}
```

A typical message from this source is the following:
ABBABABABABABABBABBBBABBABABABABABBACACABBABBBBABABACBBBBABA.

The next increase in complexity would involve trigram frequencies but no more. The choice of a letter would depend on the preceding two letters but not on the message before that point. A set of trigram frequencies p(i, j, k) or equivalently a set of transition probabilities p_{ij}(k) would be required. Continuing in this way one obtains successively more complicated stochastic processes. In the general n-gram case a set of n-gram probabilities p(i_1, i_2, ..., i_n) or of transition probabilities p_{i_1, i_2, ..., i_{n-1}}(i_n) is required to specify the statistical structure.

(D) Stochastic processes can also be defined which produce a text consisting of a sequence of "words." Suppose there are five letters A, B, C, D, E and 16 "words" in the language with associated probabilities:

.10 A   .16 BEBE   .11 CABED   .04 DEB
.04 ADEB   .04 BED   .05 CEED   .15 DEED
.05 ADEE   .02 BEED   .08 DAB   .01 EAB
.01 BADD   .05 CA   .04 DAD   .05 EE

Suppose successive "words" are chosen independently and are separated by a space. A typical message might be:
DAB EE A BEBE DEED DEB ADEE ADEE EE DEB BEBE BEBE BEBE ADEE BED DEED DEED CEED ADEE A DEED DEED BEBE CABED BEBE BED DAB DEED ADEB.

If all the words are of finite length this process is equivalent to one of the preceding type, but the description may be simpler in terms of the word structure and probabilities. We may also generalize here and introduce transition probabilities between words, etc.

These artificial languages are useful in constructing simple problems and examples to illustrate various possibilities. We can also approximate to a natural language by means of a series of simple artificial languages. The zero-order approximation is obtained by choosing all letters with the same probability and independently. The first-order approximation is obtained by choosing successive letters independently but each letter having the same probability that it has in the natural language.5 Thus, in the first-order approximation to English, E is chosen with probability .12 (its frequency in normal English) and W with probability .02, but there is no influence between adjacent letters and no tendency to form the preferred

5Letter, digram and trigram frequencies are given in Secret and Urgent by Fletcher Pratt, Blue Ribbon Books, 1939. Word frequencies are tabulated in Relative Frequency of English Speech Sounds, G. Dewey, Harvard University Press, 1923.

digrams such as TH, ED, etc. In the second-order approximation, digram structure is introduced. After a letter is chosen, the next one is chosen in accordance with the frequencies with which the various letters follow the first one. This requires a table of digram frequencies $p_i(j)$. In the third-order approximation, trigram structure is introduced. Each letter is chosen with probabilities which depend on the preceding two letters.
