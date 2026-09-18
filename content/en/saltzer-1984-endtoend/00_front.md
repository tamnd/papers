---
paper: saltzer-1984-endtoend
title: End-To-End Arguments in System Design
authors:
  - J. H. Saltzer
  - D. P. Reed
  - D. D. Clark
year: 1984
venue: ACM TOCS
field: systems
section_title: Front Matter
tag: "0050"
kind: front
lang: en
source: https://doi.org/10.1145/357401.357402
pdf_sha256: 3204a1a562d9d3b72ba112f20caddfd34991d6e1e39939ace6a3e7c016519768
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 5a38e3114bff08798d2d0cbd283c3deca3d00dd9fa9557b5948408e65f0e55e9
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

END-TO-END ARGUMENTS IN SYSTEM DESIGN

J.H. Saltzer, D.P. Reed and D.D. Clark*

M.I.T. Laboratory for Computer Science

This paper presents a design principle that helps guide placement of functions among the modules of a distributed computer system. The principle, called the end-to-end argument, suggests that functions placed at low levels of a system may be redundant or of little value when compared with the cost of providing them at that low level. Examples discussed in the paper include bit error recovery, security using encryption, duplicate message suppression, recovery from system crashes, and delivery acknowledgement. Low level mechanisms to support these functions are justified only as performance enhancements.
