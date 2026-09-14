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
lang: zh
source: https://doi.org/10.1145/357401.357402
pdf_sha256: 3204a1a562d9d3b72ba112f20caddfd34991d6e1e39939ace6a3e7c016519768
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 945daca46e532736fb8de170e6f5e32a08ffd66ecba80710b7bb9268531c28e3
translated_from: content/en/saltzer-1984-endtoend/00_front.md
source_content_sha256: 5a38e3114bff08798d2d0cbd283c3deca3d00dd9fa9557b5948408e65f0e55e9
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: 7271f7a32ca37292fd19d5ef38fdc1daa670346e7d1f46fdd75a6f589873c903
prompt_sha256: da0c2696badfbe5d93fdc534847b1b0ca3b25ec37e0ce29843665f6e701c278e
---

系统设计中的端到端论点

J.H. Saltzer、D.P. Reed 和 D.D. Clark*

M.I.T. 计算机科学实验室

本文提出了一项设计原则，用于指导分布式计算机系统中各模块之间的功能配置。该原则称为端到端论点，指出与在系统低层提供功能的成本相比，将功能置于低层可能是冗余的，或者价值很小。本文讨论的示例包括比特错误恢复、使用加密实现安全、抑制重复消息、从系统崩溃中恢复以及传送确认。支持这些功能的低层机制只有作为性能增强手段时才具有合理性。
