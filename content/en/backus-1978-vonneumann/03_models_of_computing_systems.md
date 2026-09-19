---
paper: backus-1978-vonneumann
title: Can Programming Be Liberated from the von Neumann Style? A Functional Style and Its Algebra of Programs
authors:
  - John Backus
year: 1978
venue: Communications of the ACM (Turing Award lecture)
field: languages
section: "2"
section_title: Models of Computing Systems
tag: 041C
kind: section
lang: en
source: https://www.cs.cmu.edu/~crary/819-f09/Backus78.pdf
pdf_sha256: 2e412a7986c7fd1bdd060d90d035faa9ecc8a29675f99206c243da90954ca423
pdf_pages: 2-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 1c5869757e936db55f4a0cc8f7b0d772ca06b525822ad36c46a1e36cc538135f
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Underlying every programming language is a model of a computing system that its programs control. Some models are pure abstractions, some are represented by hardware, and others by compiling or interpretive programs. Before we examine conventional languages more closely, it is useful to make a brief survey of existing models as an introduction to the current universe of alternatives. Existing models may be crudely classified by the criteria outlined below.

### 2.1 Criteria for Models {#backus-1978-vonneumann-s2-1 .section tag=041D}

2.1.1 Foundations. Is there an elegant and concise mathematical description of the model? Is it useful in proving helpful facts about the behavior of the model? Or is the model so complex that its description is bulky and of little mathematical use?

2.1.2 History sensitivity. Does the model include a notion of storage, so that one program can save information that can affect the behavior of a later program? That is, is the model history sensitive?

2.1.3 Type of semantics. Does a program successively transform states (which are not programs) until a terminal state is reached (state-transition semantics)? Are states simple or complex? Or can a “program” be successively reduced to simpler “programs” to yield a final

“normal form program,” which is the result (reduction semantics)?

2.1.4 Clarity and conceptual usefulness of programs. Are programs of the model clear expressions of a process or computation? Do they embody concepts that help us to formulate and reason about processes?

### 2.2 Classification of Models {#backus-1978-vonneumann-s2-2 .section tag=041E}

Using the above criteria we can crudely characterize three classes of models for computing systems—simple operational models, applicative models, and von Neumann models.

2.2.1 Simple operational models. Examples: Turing machines, various automata. Foundations: concise and useful. History sensitivity: have storage, are history sensitive. Semantics: state transition with very simple states. Program clarity: programs unclear and conceptually not helpful.

2.2.2 Applicative models. Examples: Church’s lambda calculus [5], Curry’s system of combinators [6], pure Lisp [17], functional programming systems described in this paper. Foundations: concise and useful. History sensitivity: no storage, not history sensitive. Semantics: reduction semantics, no states. Program clarity: programs can be clear and conceptually useful.

2.2.3 Von Neumann models. Examples: von Neumann computers, conventional programming languages. Foundations: complex, bulky, not useful. History sensitivity: have storage, are history sensitive. Semantics: state transition with complex states. Program clarity: programs can be moderately clear, are not very useful conceptually.

The above classification is admittedly crude and debatable. Some recent models may not fit easily into any of these categories. For example, the data-flow languages developed by Arvind and Gostelow [1], Dennis [7], Kosinski [13], and others partly fit the class of simple operational models, but their programs are clearer than those of earlier models in the class and it is perhaps possible to argue that some have reduction semantics. In any event, this classification will serve as a crude map of the territory to be discussed. We shall be concerned only with applicative and von Neumann models.
