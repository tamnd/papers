---
paper: backus-1978-vonneumann
title: Can Programming Be Liberated from the von Neumann Style? A Functional Style and Its Algebra of Programs
authors:
  - John Backus
year: 1978
venue: Communications of the ACM (Turing Award lecture)
field: languages
section: "6"
section_title: Language Frameworks versus Changeable Parts
tag: "0564"
kind: section
lang: en
source: https://www.cs.cmu.edu/~crary/819-f09/Backus78.pdf
pdf_sha256: 2e412a7986c7fd1bdd060d90d035faa9ecc8a29675f99206c243da90954ca423
pdf_pages: "5"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: f7818d3c8e4d5a350e408fc8aa20ad27d35812ab66bbd9ba76b7679527239e57
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Let us distinguish two parts of a programming language. First, its framework which gives the overall rules of the system, and second, its changeable parts, whose existence is anticipated by the framework but whose particular behavior is not specified by it. For example, the for statement, and almost all other statements, are part of Algol’s framework but library functions and user-defined procedures are changeable parts. Thus the framework of a language describes its fixed features and provides a general environment for its changeable features.

Now suppose a language had a small framework which could accommodate a great variety of powerful features entirely as changeable parts. Then such a framework could support many different features and styles without being changed itself. In contrast to this pleasant possibility, von Neumann languages always seem to have an immense framework and very limited changeable parts. What causes this to happen? The answer concerns two problems of von Neumann languages.

The first problem results from the von Neumann style of word-at-a-time programming, which requires that words flow back and forth to the state, just like the flow through the von Neumann bottleneck. Thus a von Neumann language must have a semantics closely coupled to the state, in which every detail of a computation changes the state. The consequence of this semantics closely coupled to states is that every detail of every feature must be built into the state and its transition rules.

Thus every feature of a von Neumann language must be spelled out in stupefying detail in its framework. Furthermore, many complex features are needed to prop up the basically weak word-at-a-time style. The result is the inevitable rigid and enormous framework of a von Neumann language.
