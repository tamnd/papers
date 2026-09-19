---
paper: karp-1972-reducibility
title: Reducibility Among Combinatorial Problems
authors:
  - Richard M. Karp
year: 1972
venue: Complexity of Computer Computations
field: theory
section: "19"
section_title: JOB SEQUENCING
tag: 051C
kind: appendix
lang: en
source: https://doi.org/10.1007/978-1-4684-2001-2_9
pdf_sha256: ae57cf641ae4f1924bdc4d7ef865edb2411c44e3040e8e546d01f1545e288e89
pdf_pages: 15-16
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 460757978a0f4384cbb93c9416875849bb48d470b80c29c077f8f3fd95eaf19c
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

INPUT: "execution time vector" (T₁,...,Tₚ) ∈ Z^P,
"deadline vector" (D₁,...,Dₚ) ∈ Z^P
"penalty vector" (P₁,...,Pₚ) ∈ Z^P
positive integer k
PROPERTY: There is a permutation π of {1,2,...,p} such that

$$
\left( \sum_{j=1}^p [ \text{if } T_{\pi(1)} + \cdots + T_{\pi(j)} > D_{\pi(j)} \text{ then } P_{\pi(j)} \text{ else } 0 ] \right) \leq k .
$$

Figure.

FIGURE 1 - Complete Problems
