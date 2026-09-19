---
paper: karp-1972-reducibility
title: Reducibility Among Combinatorial Problems
authors:
  - Richard M. Karp
year: 1972
venue: Complexity of Computer Computations
field: theory
section: "20"
section_title: PARTITION
tag: 051D
kind: appendix
lang: en
source: https://doi.org/10.1007/978-1-4684-2001-2_9
pdf_sha256: ae57cf641ae4f1924bdc4d7ef865edb2411c44e3040e8e546d01f1545e288e89
pdf_pages: "17"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 16c0046f1eb5009d0a331070b741dc963cec0d2651836e9490c9d6ffb2eb8362
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

INPUT: $(c_1, c_2, \ldots, c_s) \in Z^s$
PROPERTY: There is a set $I \subseteq \{1, 2, \ldots, s\}$ such that

$$
\sum_{h \in I} c_h = \sum_{h \notin I} c_h.
$$
