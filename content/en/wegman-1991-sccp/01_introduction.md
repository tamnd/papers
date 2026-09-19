---
paper: wegman-1991-sccp
title: Constant Propagation with Conditional Branches
authors:
  - Mark N. Wegman
  - F. Kenneth Zadeck
year: 1991
venue: ACM TOPLAS
field: languages
section: "1"
section_title: INTRODUCTION
tag: 05B8
kind: section
lang: en
source: https://www.cs.utexas.edu/users/lin/cs380c/wegman.pdf
pdf_sha256: 40929436cdf1c477f2318221df5d0aa71488db4a01cc448b184e0aba8bf95ddb
pdf_pages: 1-2
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: c57686a8c77aa56c768addd908fe2b661d478462338bffcf2604e3058a8cc1f1
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Constant propagation is a well-known global flow analysis problem. The goal of constant propagation is to discover values that are constant on all possible executions of a program and to propagate these constant values as far forward through the program as possible. Expressions whose operands are all constants can be evaluated at compile time and the results propagated further. Using the algorithms presented in this paper can produce smaller and faster compiled programs.

A preliminary version of this paper appeared in Conference Record of the Twelfth ACM Symposium on Principles of Programming Languages, 1985.
Authors’ current addresses: Mark N. Wegman, IBM T. J. Watson Research Center, P.O. Box 704, Yorktown Heights, NY 10598; F. Kenneth Zadeck, Dept. of Computer Science, Brown University, P.O. Box 1910, Providence, RI 02912.
Permission to copy without fee all or part of this material is granted provided that the copies are not made or distributed for direct commercial advantage, the ACM copyright notice and the title of the publication and its date appear, and notice is given that copying is by permission of the Association for Computing Machinery. To copy otherwise, or to republish, requires a fee and/or specific permission.
© 1991 ACM 0164-0925/91/0400-0181 \$1.25

While the constant propagation problem is easily shown to be undecidable in general (see Kam and Ullman [25], for example), there are many reasonable instances of the problem that are decidable and for which computationally efficient algorithms exist. We present four such algorithms in this paper. Each algorithm presented here is conservative in the sense that all constants may not be found, but each constant found is constant over all possible executions of the program.

After some preliminaries, the algorithms are presented in Section 3 in order of increasing power; each successive algorithm finds at least the constants found by the previous algorithm. The first three algorithms are reformulations of the work of others; the fourth is new and contains the best features of each of the previous three. These algorithms are among the simplest, fastest, and most powerful global constant propagation algorithms known. In Section 4 our algorithm is proven to be correct and at least as powerful as the best prior algorithms with polynomial-time bounds. In Section 5 some common implementation problems are discussed.

In Section 6 several techniques are explored to perform constant propagation over an area larger than single procedures. In Section 6.2 the relationship between constant propagation and procedure integration is discussed. Section 6.3 gives a new algorithm that performs a form of interprocedural data flow analysis in which aliasing information is gathered in conjunction with constant propagation.

Section 7 outlines some open problems and Section 8 concludes the paper.

### 1.1 Uses for Constant Propagation Algorithms {#wegman-1991-sccp-s1-1 .section tag=0424}

Constant propagation techniques serve several purposes in optimizing compilers:

—Expressions evaluated at compile time need not be evaluated at execution time. If such expressions are inside loops, a single evaluation at compile time can save many evaluations at execution time.
—Code that is never executed can be deleted. Unreachable code (a form of dead code) is discovered by identifying conditional branches that always take one of the possible branch paths.
—Detection of paths never taken simplifies the control flow of a program. The simplified control structure can aid the transformation of the program into a form suitable for vector processing (see Furtney and Pratt [20] and Pratt [31]) or parallel processing (see Ellis [17]).
—Since many of the parameters to procedures are constants, using constant propagation with procedure integration can avoid the expansion of code that often results from naive implementations of procedure integration.
—Constant propagation can be done over a variety of domains, for example, over the type fields of values.
