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
pdf_pages: 2-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: cb78a10f4d23a546d27c2bc0b9089d4c80ae88412348f20f31845a48fa971fc6
prompt_sha256: 329630a0b9175a55e4af1b8e281a3e67eeab250f8d643953b7dcde99743c7628
---

General Terms: Algorithms, Languages
Additional Key Words and Phrases: Control dependence, control flow graph, def-use chain, dominator, optimizing compilers

In optimizing compilers, data structure choices directly influence the power and efficiency of practical program optimization. A poor choice of data structure can inhibit optimization or slow compilation to the point where advanced optimization features become undesirable. Recently, static single assignment (SSA) form [5, 43] and the control dependence graph [24] have been proposed to represent data flow and control flow properties of programs. Each of these previously unrelated techniques lends efficiency and power to a useful class of program optimizations. Although both of these structures are attractive, the difficulty of their construction and their potential size have discouraged their use [4]. We present new algorithms that efficiently compute these data structures for arbitrary control flow graphs. The algorithms use dominance frontiers, a new concept that may have other applications. We also give analytical and experimental evidence that the sum of the sizes of all the dominance frontiers is usually linear in the size of the original program. This paper thus presents strong evidence that SSA form and control dependences can be of practical use in optimization.
