---
paper: backus-1978-vonneumann
title: Can Programming Be Liberated from the von Neumann Style? A Functional Style and Its Algebra of Programs
authors:
  - John Backus
year: 1978
venue: Communications of the ACM (Turing Award lecture)
field: languages
section: "15"
section_title: Remarks About Computer Design
tag: "0580"
kind: section
lang: en
source: https://www.cs.cmu.edu/~crary/819-f09/Backus78.pdf
pdf_sha256: 2e412a7986c7fd1bdd060d90d035faa9ecc8a29675f99206c243da90954ca423
pdf_pages: 26-27
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 959b7776545d4d594c054854cc7ce8c2581a143cbf2a5b7e49072f0e0da37128
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The dominance of von Neumann languages has left designers with few intellectual models for practical computer designs beyond variations of the von Neumann computer. Data flow models [1] [7] [13] are one alternative class of history-sensitive models. The substitution rules of lambda-calculus based languages present serious problems for the machine designer. Berkling [3] has developed a modified lambda calculus that has three kinds of applications and that makes renaming of variables unnecessary. He has developed a machine to evaluate expressions of this language. Further experience is needed to show how sound a basis this language is for an effective programming style and how efficient his machine can be.

Magó [15] has developed a novel applicative machine built from identical components (of two kinds). It evaluates, directly, FP-like and other applicative expressions from the bottom up. It has no von Neumann store and no address register, hence no bottleneck; it is capable of evaluating many applications in parallel; its built-in operations resemble FP operators more than von Neumann computer operations. It is the farthest departure from the von Neumann computer that I have seen.

There are numerous indications that the applicative style of programming can become more powerful than the von Neumann style. Therefore it is important for programmers to develop a new class of history-sensitive models of computing systems that embody such a style and avoid the inherent efficiency problems that seem to attach to lambda-calculus based systems. Only when these models and their applicative languages have proved their superiority over conventional languages will we have the economic basis to develop the new kind of computer that can best implement them. Only then, perhaps, will we be able to fully utilize large-scale integrated circuits in a computer design not limited by the von Neumann bottleneck.
