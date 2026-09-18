---
paper: aho-1975-corasick
title: 'Efficient String Matching: An Aid to Bibliographic Search'
authors:
  - Alfred V. Aho
  - Margaret J. Corasick
year: 1975
venue: Communications of the ACM
field: algorithms
section: "8"
section_title: Concluding Remarks
tag: "0344"
kind: section
lang: en
source: https://cr.yp.to/bib/1975/aho.pdf
pdf_sha256: f04940c07d2a12726bce4147fd4217e876cd969ddf44094ad90c866893deed34
pdf_pages: "8"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: f6bb2d604be973dbd91492025018f71744ce7e30ec33e2911de5a264e3291b7a
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The pattern matching scheme described in this paper is well suited for applications in which we are looking for occurrences of large numbers of keywords in text strings. Since no additional information needs to be added to the text string, searches can be made over arbitrary files.

Some information retrieval systems compute an index or concordance for a text file to allow searches to be conducted without having to scan all of the text string [7]. In such systems making changes to the text file is expensive because after each change the index to the file must be updated. Consequently, such systems work best with long static text files and short patterns.

An interesting question from finite automata theory is: Given a regular expression $R$ of length $r$ and an input string $x$ of length $n$, how quickly can one determine whether $x$ is in the language denoted by $R$? One method for solving this problem is first to construct from $R$ a nondeterministic finite automaton $M$ and then to simulate the behavior of $M$ on the input $x$. This gives an $O(rn)$ solution [1].

Another approach along these lines is to construct from $R$ a nondeterministic finite automaton $M$, then to convert $M$ into a deterministic finite automaton $M'$ and then to simulate the behavior of $M'$ on $x$. The only difficulty with this approach is that $M'$ can have on the order of $2^r$ states. The simulation of $M'$ on the other hand is linear in $n$ of course. The overall complexity is $O(2^r + n)$.

Using Algorithm 4 we can construct a deterministic finite automaton directly from a regular expression $R$ in time that is linear in the length of $R$. However, the regular expression is now restricted to be the form $\Sigma^*(y_1 + y_2 + \cdots + y_k)\Sigma^*$ where $\Sigma$ is the input symbol alphabet. By "concatenating" a series of deterministic finite automata in tandem, we can extend this result to regular expressions of the form $\Sigma^*Y_1\Sigma^*Y_2\cdots\Sigma^*Y_m\Sigma^*$ where each $Y_i$ is a regular expression of the form $y_{i1} + y_{i2} + \cdots + y_{ik_i}$.

A related open question is what new classes of regular sets can be recognized in less than $O(rn)$ time. Along these lines, in [5] it is shown that regular expressions of the form $\Sigma^*y\Sigma^*$ where $y$ is a keyword with "don't care" symbols can be recognized in $O(n \log r \log \log r)$ time.
