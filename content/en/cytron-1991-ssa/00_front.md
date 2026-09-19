---
paper: cytron-1991-ssa
title: Efficiently Computing Static Single Assignment Form and the Control Dependence Graph
authors:
  - Ron Cytron
  - Jeanne Ferrante
  - Barry K. Rosen
  - Mark N. Wegman
  - F. Kenneth Zadeck
year: 1991
venue: ACM TOPLAS
field: languages
section_title: Front Matter
tag: 004B
kind: front
lang: en
source: https://www.cs.utexas.edu/~pingali/CS380C/2010/papers/ssaCytron.pdf
pdf_sha256: 307512bb537628c2b326b23aa02109e7562bfc619509e942e015054ab58eb9ab
pdf_pages: 1-2
extraction: vision
extraction_model: gpt-5
content_sha256: 00e3f8081ba45233dd31103f548536087de453c39cf525c1d25607ec069d9d7f
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Efficiently Computing Static Single Assignment Form and the Control Dependence Graph

RON CYTRON, JEANNE FERRANTE, BARRY K. ROSEN, and MARK N. WEGMAN
IBM Research Division
and
F. KENNETH ZADECK
Brown University

In optimizing compilers, data structure choices directly influence the power and efficiency of practical program optimization. A poor choice of data structure can inhibit optimization or slow compilation to the point that advanced optimization features become undesirable. Recently, static single assignment form and the control dependence graph have been proposed to represent data flow and control flow properties of programs. Each of these previously unrelated techniques lends efficiency and power to a useful class of program optimizations. Although both of these structures are attractive, the difficulty of their construction and their potential size have discouraged their use. We present new algorithms that efficiently compute these data structures for arbitrary control flow graphs. The algorithms use dominance frontiers, a new concept that may have other applications. We also give analytical and experimental evidence that all of these data structures are usually linear in the size of the original program. This paper thus presents strong evidence that these structures can be of practical use in optimization.

Categories and Subject Descriptors: D.3.3 [Programming Languages]: Language Constructs—control structures; data types and structures; procedures, functions and subroutines; D.3.4 [Programming Languages]: Processors—compilers; optimization; I.1.2 [Algebraic Manipulation]: Algorithms—analysis of algorithms; I.2.2 [Artificial Intelligence]: Automatic Programming—program transformation

A preliminary version of this paper, “An Efficient Method of Computing Static Single Assignment Form,” appeared in the Conference Record of the 16th ACM Symposium on Principles of Programming Languages (Jan. 1989).
F. K. Zadeck’s work on this paper was partially supported by the IBM Corporation, the Office of Naval Research, and the Defense Advanced Research Projects Agency under contract N00014-83-K-0146 and ARPA order 6320, Amendment 1.
Authors’ addresses: R. Cytron, J. Ferrante, and M. N. Wegman, Computer Sciences Department, IBM Research Division, P. O. Box 704, Yorktown Heights, NY 10598; B. K. Rosen, Mathematical Sciences Department, IBM Research Division, P. O. Box 218, Yorktown Heights, NY 10598; F. K. Zadeck, Computer Science Department, P.O. Box 1910, Brown University, Providence, RI 02912.
Permission to copy without fee all or part of this material is granted provided that the copies are not made or distributed for direct commercial advantage, the ACM copyright notice and the title of the publication and its date appear, and notice is given that copying is by permission of the Association for Computing Machinery. To copy otherwise, or to republish, requires a fee and/or specific permission.
© 1991 ACM 0164-0925/91/1000-0451 \$01.50

General Terms: Algorithms, Languages
Additional Key Words and Phrases: Control dependence, control flow graph, def-use chain, dominator, optimizing compilers
