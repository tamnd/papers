---
paper: boncz-2005-x100
title: 'MonetDB/X100: Hyper-Pipelining Query Execution'
authors:
  - Peter Boncz
  - Marcin Zukowski
  - Niels Nes
year: 2005
venue: CIDR
field: databases
section: "6"
section_title: Related Work
tag: "0784"
kind: section
lang: en
source: https://www.cidrdb.org/cidr2005/papers/P19.pdf
pdf_sha256: c509153c876aee8706e298d43e2fa93ade2696cc3102643b439af0f508bb52fc
pdf_pages: "12"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: dd0bb034981b224d87e03a918445b650c6e2e840bc5140a6b1a4741fd565f430
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

This research builds a bridge between the classical Volcano iterator model [[graefe-1994-volcano]] and the column-wise query processing model of MonetDB [4].

Apart from formalizing the iterator model of query processing, Volcano also generalized various forms of parallel query processing [20], where one of the possible strategies is to dedicate a separate process to each query operator. This differs from our approach in the sense that we reduce overhead by making a process spend *significant* time in each operator for each query processing iteration (i.e. processing a vector of tuples rather than a single one).

The work closest to our paper is [14], where a *blocked* execution path in DB2 is presented. Unlike MonetDB/X100, which is designed from the ground up for vectorized execution, the authors only use their approach to enhance aggregation and projection operations. In DB2, the tuple layout remains NSM, al-
