---
paper: hoare-1969-axiomatic
title: An Axiomatic Basis for Computer Programming
authors:
  - C. A. R. Hoare
year: 1969
venue: Communications of the ACM
field: languages
section: "2"
section_title: Computer Arithmetic
tag: "0312"
kind: section
lang: en
source: https://www.cs.cmu.edu/~crary/819-f09/Hoare69.pdf
pdf_sha256: f9b85de3537c0f1239cbe767cfd26ad49f2be07f0cc9021a6e46adfffb81dc12
pdf_pages: 1-2
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 46050c021ee404aca234eba52d42fa9af86cdff72cfbcef15018f2b05893361b
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The first requirement in valid reasoning about a program is to know the properties of the elementary operations which it invokes, for example, addition and multiplication of integers. Unfortunately, in several respects computer arithmetic is not the same as the arithmetic familiar to mathematicians, and it is necessary to exercise some care in selecting an appropriate set of axioms. For example, the axioms displayed in Table I are rather a small selection of axioms relevant to integers. From this incomplete set of axioms it is possible to deduce such simple theorems as:

$$
x = x + y \times 0 \\
y \leq r \supset r + y \times q = (r - y) + y \times (1 + q)
$$

The proof of the second of these is:

A5 $(r - y) + y \times (1 + q)$

$$
= (r - y) + (y \times 1 + y \times q)
$$

A9

$$
= (r - y) + (y + y \times q)
$$

A3

$$
= ((r - y) + y) + y \times q
$$

A6

$$
= r + y \times q \quad \text{provided } y \leq r
$$

The axioms A1 to A9 are, of course, true of the traditional infinite set of integers in mathematics. However, they are also true of the finite sets of “integers” which are manipulated by computers provided that they are confined to nonnegative numbers. Their truth is independent of the size of the set; furthermore, it is largely independent of the choice of technique applied in the event of “overflow”; for example:
(1) Strict interpretation: the result of an overflowing operation does not exist; when overflow occurs, the offending program never completes its operation. Note that in this case, the equalities of A1 to A9 are strict, in the sense that both sides exist or fail to exist together.
(2) Firm boundary: the result of an overflowing operation is taken as the maximum value represented.
(3) Modulo arithmetic: the result of an overflowing operation is computed modulo the size of the set of integers represented.

These three techniques are illustrated in Table II by addition and multiplication tables for a trivially small model in which 0, 1, 2, and 3 are the only integers represented.

It is interesting to note that the different systems satisfying axioms A1 to A9 may be rigorously distinguished from each other by choosing a particular one of a set of mutually exclusive supplementary axioms. For example, infinite arithmetic satisfies the axiom:

A10$_I$ $\neg \exists x \forall y \quad (y \leq x),$ where all finite arithmetics satisfy:

A10$_F$ $\forall x \quad (x \leq \max)$ where “max” denotes the largest integer represented.

Similarly, the three treatments of overflow may be distinguished by a choice of one of the following axioms relating to the value of max + 1:

A11$_s$ $\neg \exists x \quad (x = \max + 1)$ (strict interpretation)

A11$_B$ $\max + 1 = \max$ (firm boundary)

A11$_M$ $\max + 1 = 0$ (modulo arithmetic)

Having selected one of these axioms, it is possible to use it in deducing the properties of programs; however,

| TABLE I |  |  |  |
| --- | --- | --- | --- |
| A1 | $x + y = y + x$ | addition is commutative |  |
| A2 | $x \times y = y \times x$ | multiplication is commutative |  |
| A3 | $(x + y) + z = x + (y + z)$ | addition is associative |  |
| A4 | $(x \times y) \times z = x \times (y \times z)$ | multiplication is associative |  |
| A5 | $x \times (y + z) = x \times y + x \times z$ | multiplication distributes through addition |  |
| A6 | $y \leq x \supset (x - y) + y = x$ | addition cancels subtraction |  |
| A7 | $x + 0 = x$ |  |  |
| A8 | $x \times 0 = 0$ |  |  |
| A9 | $x \times 1 = x$ |  |  |

| TABLE II |  |  |  |
| --- | --- | --- | --- |
| 1. Strict Interpretation |  |  |  |
| + | 0 1 2 3 | × | 0 1 2 3 |
| 0 | 0 1 2 3 | 0 | 0 0 0 0 |
| 1 | 1 2 3 * | 1 | 0 1 2 3 |
| 2 | 2 3 * * | 2 | 0 2 * * |
| 3 | 3 * * * | 3 | 0 3 * * |
| * nonexistent |  |  |  |
| 2. Firm Boundary |  |  |  |
| + | 0 1 2 3 | × | 0 1 2 3 |
| 0 | 0 1 2 3 | 0 | 0 0 0 0 |
| 1 | 1 2 3 3 | 1 | 0 1 2 3 |
| 2 | 2 3 3 3 | 2 | 0 2 3 3 |
| 3 | 3 3 3 3 | 3 | 0 3 3 3 |
| 3. Modulo Arithmetic |  |  |  |
| + | 0 1 2 3 | × | 0 1 2 3 |
| 0 | 0 1 2 3 | 0 | 0 0 0 0 |
| 1 | 1 2 3 0 | 1 | 0 1 2 3 |
| 2 | 2 3 0 1 | 2 | 0 2 0 2 |
| 3 | 3 0 1 2 | 3 | 0 3 2 1 |

these properties will not necessarily obtain, unless the program is executed on an implementation which satisfies the chosen axiom.
