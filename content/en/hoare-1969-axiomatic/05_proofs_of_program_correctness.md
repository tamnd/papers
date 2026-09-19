---
paper: hoare-1969-axiomatic
title: An Axiomatic Basis for Computer Programming
authors:
  - C. A. R. Hoare
year: 1969
venue: Communications of the ACM
field: languages
section: "5"
section_title: Proofs of Program Correctness
tag: 031A
kind: section
lang: en
source: https://www.cs.cmu.edu/~crary/819-f09/Hoare69.pdf
pdf_sha256: f9b85de3537c0f1239cbe767cfd26ad49f2be07f0cc9021a6e46adfffb81dc12
pdf_pages: "4"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: ea9fa63bdec9c029655ac2ac2960da2b7feec9cd564d9e10de547b9790a41c62
edited: true
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The most important property of a program is whether it accomplishes the intentions of its user. If these intentions can be described rigorously by making assertions about the values of variables at the end (or at intermediate points) of the execution of the program, then the techniques described in this paper may be used to prove the correctness of the program, provided that the implementation of the programming language conforms to the axioms and rules which have been used in the proof. This fact itself might also be established by deductive reasoning, using an axiom set which describes the logical properties of the hardware circuits. When the correctness of a program, its compiler, and the hardware of the computer have all been established with mathematical certainty, it will be possible to place great reliance on the results of the program, and predict their properties with a confidence limited only by the reliability of the electronics.

The practice of supplying proofs for nontrivial programs will not become widespread until considerably more powerful proof techniques become available, and even then will not be easy. But the practical advantages of program proving will eventually outweigh the difficulties, in view of the increasing costs of programming error. At present, the method which a programmer uses to convince himself of the correctness of his program is to try it out in particular cases and to modify it if the results produced do not correspond to his intentions. After he has found a reasonably wide variety of example cases on which the program seems to work, he believes that it will always work. The time spent in this program testing is often more than half the time spent on the entire programming project; and with a realistic costing of machine time, two thirds (or more) of the cost of the project is involved in removing errors during this phase.

The cost of removing errors discovered after a program has gone into use is often greater, particularly in the case of items of computer manufacturer’s software for which a large part of the expense is borne by the user. And finally, the cost of error in certain types of program may be almost

| TABLE III |  |  |
| --- | --- | --- |
| Line number | Formal proof | Justification |
| 1 | true $\supset x = x + y \times 0$ | Lemmas 1 |
| 2 | $x = x + y \times 0 \{ r := x \} x = r + y \times 0$ | D0 |
| 3 | $x = r + y \times 0 \{ q := 0 \} x = r + y \times q$ | D0 |
| 4 | true $\{ r := x \} x = r + y \times 0$ | D1 (1, 2) |
| 5 | true $\{ r := x; \ q := 0 \} x = r + y \times q$ | D2 (4, 3) |
| 6 | $x = r + y \times q \land y \leq r \supset x = (r-y) + y \times (1+q)$ | Lemmas 2 |
| 7 | $x = (r-y) + y \times (1+q) \{ r := r-y \} x = r + y \times (1+q)$ | D0 |
| 8 | $x = r + y \times (1+q) \{ q := 1+q \} x = r + y \times q$ | D0 |
| 9 | $x = (r-y) + y \times (1+q) \{ r := r-y; \ q := 1+q \} x = r + y \times q$ | D2 (7, 8) |
| 10 | $x = r + y \times q \land y \leq r \{ r := r-y; \ q := 1+q \} x = r + y \times q$ | D1 (6, 9) |
| 11 | $x = r + y \times q \{ \text{while } y \leq r \text{ do}$ | D3 (10) |
|  | $(r := r-y; \ q := 1+q) \}$ |  |
|  | $\neg y \leq r \land x = r + y \times q$ |  |
| 12 | true $\{ ((r := x; \ q := 0); \ \text{while } y \leq r \text{ do}$ | D2 (5, 11) |
|  | $(r := r-y; \ q := 1+q)) \} \neg y \leq r \land x = r + y \times q$ |  |
