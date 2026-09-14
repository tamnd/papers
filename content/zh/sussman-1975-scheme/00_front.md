---
paper: sussman-1975-scheme
title: 'Scheme: An Interpreter for Extended Lambda Calculus'
authors:
  - Gerald Jay Sussman
  - Guy L. Steele Jr.
year: 1975
venue: MIT AI Memo 349
field: languages
section_title: Front Matter
tag: "0047"
kind: front
lang: zh
source: https://dspace.mit.edu/server/api/core/bitstreams/70ab0fe6-0e7a-41ef-99fb-ac2c9481a05e/content
pdf_sha256: c2961e078943a26ae1f752b202290f561578b7ecf8b24b8929e3c1f99e6b2c52
pdf_pages: 1-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 6573aff32cf9306ac3492bef4d8a92d256f5171c009ed85e13df56f53aa8352f
translated_from: content/en/sussman-1975-scheme/00_front.md
source_content_sha256: 326c3043a5d2c15ce603ddfd07ea950af19f0f9587bb0f8c53dce7b8a3d04f66
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: fcb84f53aa78484b92ff53c9baf55147dd1cf39c33fa0b3519c4a3322d452302
prompt_sha256: da0c2696badfbe5d93fdc534847b1b0ca3b25ec37e0ce29843665f6e701c278e
---

麻省理工学院

人工智能实验室

AI Memo No. 349

1975年12月

SCHEME

扩展 λ 演算的解释器

作者

Gerald Jay Sussman 和 Guy Lewis Steele Jr.

摘要：

受 ACTORS [Greif and Hewitt] [Smith and Hewitt] 的启发，我们实现了一个类似 LISP 的编程语言 SCHEME 的解释器。SCHEME 基于 λ 演算 [Church]，并扩展了副作用、多进程和进程同步。该实现旨在用于教学。我们的目标是：

(1) 通过阐明如何将非递归控制结构嵌入 LISP 这样的递归宿主语言，来消除 Micro-PLANNER、CONNIVER 等造成的困惑。

(2) 说明如何使用这些控制结构，而不涉及模式匹配和数据库操作等问题。

(3) 为编程语义和编程风格中的某些问题提供一个简单而具体的实验领域。

本文分为若干节。第一节是一份简短的“参考手册”，其中包含 SCHEME 所有非标准特性的规范。接下来，我们给出一系列编程示例，用于说明各种编程风格以及如何使用这些风格。这些示例将引出一些语义问题，我们将在第三节中尝试用 λ 演算加以澄清。第四节将总体讨论基于 λ 演算的语言的解释器实现者所面临的问题。
