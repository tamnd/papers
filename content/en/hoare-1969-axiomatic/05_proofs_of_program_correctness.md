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
pdf_pages: 4-5
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 80f0d0cffb0d18009806d465512258932b7d40c04628f11992771af1dc53bed6
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The most important property of a program is whether it accomplishes the intentions of its user. If these intentions can be described rigorously by making assertions about the values of variables at the end (or at intermediate points) of the execution of the program, then the techniques described in this paper may be used to prove the correctness of the program, provided that the implementation of the programming language conforms to the axioms and rules which have been used in the proof. This fact itself might also be established by deductive reasoning, using an axiom set which describes the logical properties of the hardware circuits. When the correctness of a program, its compiler, and the hardware of the computer have all been established with mathematical certainty, it will be possible to place great reliance on the results of the program, and predict their properties with a confidence limited only by the reliability of the electronics.

The practice of supplying proofs for nontrivial programs will not become widespread until considerably more powerful proof techniques become available, and even then will not be easy. But the practical advantages of program proving will eventually outweigh the difficulties, in view of the increasing costs of programming error. At present, the method which a programmer uses to convince himself of the correctness of his program is to try it out in particular cases and to modify it if the results produced do not correspond to his intentions. After he has found a reasonably wide variety of example cases on which the program seems to work, he believes that it will always work. The time spent in this program testing is often more than half the time spent on the entire programming project; and with a realistic costing of machine time, two thirds (or more) of the cost of the project is involved in removing errors during this phase.

The cost of removing errors discovered after a program has gone into use is often greater, particularly in the case of items of computer manufacturer’s software for which a large part of the expense is borne by the user. And finally, the cost of error in certain types of program may be almost

```text
| Line number | Formal proof | Justification |
| --- | --- | --- |
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
|  | \( (r := r-y; \ q := 1+q) \} |  |
| 12 | $\neg y \leq r \land x = r + y \times q$ | D2 (5, 11) |
```

NOTES
1. The left hand column is used to number the lines, and the right hand column to justify each line, by appealing to an axiom, a lemma or a rule of inference applied to one or two previous lines, indicated in brackets. Neither of these columns is part of the formal proof. For example, line 2 is an instance of the axiom of assignment (D0); line 12 is obtained from lines 5 and 11 by application of the rule of composition (D2).
2. Lemma 1 may be proved from axioms A7 and A8.
3. Lemma 2 follows directly from the theorem proved in Sec. 2.

incalculable—a lost spacecraft, a collapsed building, a crashed aeroplane, or a world war. Thus the practice of program proving is not only a theoretical pursuit, followed in the interests of academic respectability, but a serious recommendation for the reduction of the costs associated with programming error.

The practice of proving programs is likely to alleviate some of the other problems which afflict the computing world. For example, there is the problem of program documentation, which is essential, firstly, to inform a potential user of a subroutine how to use it and what it accomplishes, and secondly, to assist in further development when it becomes necessary to update a program to meet changing circumstances or to improve it in the light of increased knowledge. The most rigorous method of formulating the purpose of a subroutine, as well as the conditions of its proper use, is to make assertions about the values of variables before and after its execution. The proof of the correctness of these assertions can then be used as a lemma in the proof of any program which calls the subroutine. Thus, in a large program, the structure of the whole can be clearly mirrored in the structure of its proof. Furthermore, when it becomes necessary to modify a program, it will always be valid to replace any subroutine by another which satisfies the same criterion of correctness. Finally, when examining the detail of the algorithm, it seems probable that the proof will be helpful in explaining not only *what* is happening but *why*.

Another problem which can be solved, insofar as it is soluble, by the practice of program proofs is that of transferring programs from one design of computer to another. Even when written in a so-called machine-independent programming language, many large programs inadvertently take advantage of some machine-dependent property of a particular implementation, and unpleasant and expensive surprises can result when attempting to transfer it to another machine. However, presence of a machine-dependent feature will always be revealed in advance by the failure of an attempt to prove the program from machine-independent axioms. The programmer will then have the choice of formulating his algorithm in a machine-independent fashion, possibly with the help of environment enquiries; or if this involves too much effort or inefficiency, he can deliberately construct a machine-dependent program, and rely for his proof on some machine-dependent axiom, for example, one of the versions of A11 (Section 2). In the latter case, the axiom must be explicitly quoted as one of the preconditions of successful use of the program. The program can still, with complete confidence, be transferred to any other machine which happens to satisfy the same machine-dependent axiom; but if it becomes necessary to transfer it to an implementation which does not, then all the places where changes are required will be clearly annotated by the fact that the proof at that point appeals to the truth of the offending machine-dependent axiom.

Thus the practice of proving programs would seem to lead to solution of three of the most pressing problems in software and programming, namely, reliability, documentation, and compatibility. However, program proving, certainly at present, will be difficult even for programmers of high caliber; and may be applicable only to quite simple program designs. As in other areas, reliability can be purchased only at the price of simplicity.
