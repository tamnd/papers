---
paper: mccabe-1976-complexity
title: A Complexity Measure
authors:
  - Thomas J. McCabe
year: 1976
venue: IEEE Transactions on Software Engineering
field: software
section: I
section_title: INTRODUCTION
tag: 03A7
kind: section
lang: en
source: http://www.literateprogramming.com/mccabe.pdf
pdf_sha256: be2ac1035940dfc7fa231e23b33bfa3c2f3e3d8ef3112e20cf92a35a7af537f6
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 938fe49074603a3f652ce800b4db7dbe5741868cf877373d5b66be68a788e2c5
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

THERE is a critical question facing software engineering today: How to modularize a software system so the resulting modules are both testable and maintainable? That the issues of testability and maintainability are important is borne out by the fact that we often spend half of the development time in testing [2] and can spend most of our dollars maintaining systems [3]. What is needed is a mathematical technique that will provide a quantitative basis for modularization and allow us to identify software modules that will be difficult to test or maintain. This paper reports on an effort to develop such a mathematical technique which is based on program control flow.

One currently used practice that attempts to ensure a reasonable modularization is to limit programs by physical size (e.g., IBM-50 lines, TRW-2 pages). This technique is not adequate, which can be demonstrated by imagining a 50 line program consisting of 25 consecutive “IF THEN” constructs. Such a program could have as many as 33.5 million distinct control paths, only a small percentage of which would probably ever be tested. Many such examples of live Fortran programs that are physically small but untestable have been identified and analyzed by the tools described in this paper.
