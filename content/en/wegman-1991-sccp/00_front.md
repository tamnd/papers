---
paper: wegman-1991-sccp
title: Constant Propagation with Conditional Branches
authors:
  - Mark N. Wegman
  - F. Kenneth Zadeck
year: 1991
venue: ACM TOPLAS
field: languages
section_title: Front Matter
tag: 004C
kind: front
lang: en
source: https://www.cs.utexas.edu/users/lin/cs380c/wegman.pdf
pdf_sha256: 40929436cdf1c477f2318221df5d0aa71488db4a01cc448b184e0aba8bf95ddb
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: dad93cee9691a1ba2ffd31656835d2688ff3f4afe3f06b2bd344da941d32c082
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Constant Propagation with Conditional Branches

MARK N. WEGMAN and F. KENNETH ZADECK
IBM T. J. Watson Research Center

Constant propagation is a well-known global flow analysis problem. The goal of constant propagation is to discover values that are constant on all possible executions of a program and to propagate these constant values as far forward through the program as possible. Expressions whose operands are all constants can be evaluated at compile time and the results propagated further. Using the algorithms presented in this paper can produce smaller and faster compiled programs. The same algorithms can be used for other kinds of analyses (e.g., type determination). We present four algorithms in this paper, all conservative in the sense that all constants may not be found, but each constant found is constant over all possible executions of the program. These algorithms are among the simplest, fastest, and most powerful global constant propagation algorithms known. We also present a new algorithm that performs a form of interprocedural data flow analysis in which aliasing information is gathered in conjunction with constant propagation. Several variants of this algorithm are considered.

Categories and Subject Descriptors: D.3.3 [Programming Languages]: Language Constructs and Features—data types and structures; procedures, functions and subroutines; D.3.4 [Programming Languages]: Processors—code generation; compilers; optimization; preprocessors; I.2.2 [Artificial Intelligence]: Automatic Programming—program transformation
General Terms: Algorithms, Design, Languages, Theory
Additional Key Words and Phrases: Abstract interpretation, code optimization, constant propagation, control flow graph, interprocedural analysis, procedure integration, static single assignment form, type determination
