---
paper: wegman-1991-sccp
title: Constant Propagation with Conditional Branches
authors:
  - Mark N. Wegman
  - F. Kenneth Zadeck
year: 1991
venue: ACM TOPLAS
field: languages
section: "8"
section_title: CONCLUSIONS
tag: 05D7
kind: section
lang: en
source: https://www.cs.utexas.edu/users/lin/cs380c/wegman.pdf
pdf_sha256: 40929436cdf1c477f2318221df5d0aa71488db4a01cc448b184e0aba8bf95ddb
pdf_pages: "28"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 058681bc1b592b6d5bf309284d6f15cae9169eb9afccc757c1f6b371d1bc1e07
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The work presented here is based on three fundamental results concerning constant propagation: Kildall’s definition of the problem involving the three-layered lattice, Reif and Lewis’s algorithm involving a sparse representation of propagation space, and Wegbreit’s algorithm, which used the result of conditional operations to improve the class of constants found. We have added two relevant results of our own. The first result is that a careful ordering of propagation in concert with symbolic execution of the conditional expressions can increase the number of constants found with no penalty in time or space. The second is the use of static single assignment form for constant propagation.

We have used these five results to craft an algorithm that is efficient in both time and space, and yet finds a very broad class of constants. Moreover, we have shown how to use this algorithm to perform procedure integration and interprocedural analysis.
