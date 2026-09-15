---
paper: razborov-1997-naturalproofs
title: Natural Proofs
authors:
  - Alexander A. Razborov
  - Steven Rudich
year: 1997
venue: Journal of Computer and System Sciences
field: theory
section: "6"
section_title: Conclusion
tag: "0226"
kind: section
lang: en
source: https://doi.org/10.1006/jcss.1997.1494
pdf_sha256: 6cf137cf878d01654aeff5dbf031e97a624cd72367b87415ff61080447de7682
pdf_pages: "22"
extraction: vision
extraction_model: gpt-5
content_sha256: efcbd05c12e4414a17dfcede98b7576ac55312df78d523f5128ab4e9e9b44780
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

We do not conclude that researchers should give up on proving serious lower bounds. Quite the contrary, by classifying a large number of techniques that are unable to do the job we hope to focus research in a more fruitful direction. Pessimism will only be warranted if a long period of time passes without the discovery of a non-naturalizing lower bound proof.

As long as we use natural proofs we have to cope with a duality: any lower bound proof must implicitly argue a proportionately strong upper bound. In particular, we have shown that a natural proof against complexity class implicitly shows that does not contain strong pseudo-random function generators. In fact, the proof gives an algorithm to break any such generator. Seen this way, even a natural proof against NC 1 (or TC 0 ) becomes dicult or impossible. In [16] it is argued based on the hardness of subset sum that a pseudo-random function should exist in TC 0 NC 1 . Consider the plausible conjecture that there exists a (pseudo-random) function f 2 NC 1 (or TC 0 ) such that G ( x ) = n;s f ( s # x ) is a pseudo-random function generator. A natural proof that P 6 = NC 1 or P 6 = TC 0 would give an algorithm to break it. Thus, we see that working on lower bounds using natural methods is like breaking a secret code determined by the class we are working against!

With this duality in mind, it is no coincidence that the technical lemmas of [14, 36, 29] yield much of the machinery for the learning result of [20].
