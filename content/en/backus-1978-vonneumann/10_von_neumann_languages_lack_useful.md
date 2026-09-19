---
paper: backus-1978-vonneumann
title: Can Programming Be Liberated from the von Neumann Style? A Functional Style and Its Algebra of Programs
authors:
  - John Backus
year: 1978
venue: Communications of the ACM (Turing Award lecture)
field: languages
section: "9"
section_title: Von Neumann Languages Lack Useful Mathematical Properties
tag: "0567"
kind: section
lang: en
source: https://www.cs.cmu.edu/~crary/819-f09/Backus78.pdf
pdf_sha256: 2e412a7986c7fd1bdd060d90d035faa9ecc8a29675f99206c243da90954ca423
pdf_pages: 6-7
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 784f8f515e27a38e459e97cb623392be38be47342345f1384284d000c87b75e8
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

So far we have discussed the gross size and inflexibility of von Neumann languages; another important defect is their lack of useful mathematical properties and the obstacles they present to reasoning about programs. Although a great amount of excellent work has been published on proving facts about programs, von Neumann languages have almost no properties that are helpful in this direction and have many properties that are obstacles (e.g., side effects, aliasing).

Denotational semantics [23] and its foundations [20, 21] provide an extremely helpful mathematical understanding of the domain and function spaces implicit in programs. When applied to an applicative language (such as that of the “recursive programs” of [16]), its foundations provide powerful tools for describing the language and for proving properties of programs. When applied to a von Neumann language, on the other hand, it provides a precise semantic description and is helpful in identifying trouble spots in the language. But the complexity of the language is mirrored in the complexity of the description, which is a bewildering collection of productions, domains, functions, and equations that is only slightly more helpful in proving facts about programs than the reference manual of the language, since it is less ambiguous.

Axiomatic semantics [[hoare-1969-axiomatic]] precisely restates the inelegant properties of von Neumann programs (i.e., transformations on states) as transformations on predicates. The word-at-a-time, repetitive game is not thereby changed, merely the playing field. The complexity of this axiomatic game of proving facts about von Neumann programs makes the successes of its practitioners all the more admirable. Their success rests on two factors in addition to their ingenuity: First, the game is restricted to small, weak subsets of full von Neumann languages that have states vastly simpler than real ones. Second, the new playing field (predicates and their transformations) is richer, more orderly and effective than the old (states and their transformations). But restricting the game and transferring it to a more effective domain does not enable it to handle real programs (with the necessary complexities of procedure calls and aliasing), nor does it eliminate the clumsy properties of the basic von Neumann style. As axiomatic semantics is extended to cover more of a typical von Neumann language, it begins to lose its effectiveness with the increasing complexity that is required.

Thus denotational and axiomatic semantics are descriptive formalisms whose foundations embody elegant and powerful concepts; but using them to describe a von Neumann language can not produce an elegant and powerful language any more than the use of elegant and modern machines to build an Edsel can produce an elegant and modern car.

In any case, proofs about programs use the language of logic, not the language of programming. Proofs talk about programs but cannot involve them directly since the axioms of von Neumann languages are so unusable. In contrast, many ordinary proofs are derived by algebraic methods. These methods require a language that has certain algebraic properties. Algebraic laws can then be used in a rather mechanical way to transform a problem into its solution. For example, to solve the equation

$$
ax + bx = a + b
$$

for $x$ (given that $a+b \neq 0$), we mechanically apply the distributive, identity, and cancellation laws, in succession, to obtain

$$
(a + b)x = a + b \\
(a + b)x = (a + b)1 \\
x = 1.
$$

Thus we have proved that $x = 1$ without leaving the “language” of algebra. Von Neumann languages, with their grotesque syntax, offer few such possibilities for transforming programs.

As we shall see later, programs can be expressed in a language that has an associated algebra. This algebra can be used to transform programs and to solve some equations whose “unknowns” are programs, in much the same way one solves equations in high school algebra. Algebraic transformations and proofs use the language of the programs themselves, rather than the language of logic, which talks about programs.
