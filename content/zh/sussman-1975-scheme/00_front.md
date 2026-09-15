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
content_sha256: 82f2e7c9dbf1bd5eb9c18c506a79536c631378b42cfb0a7553145fbcb5e1fe9a
translated_from: content/en/sussman-1975-scheme/00_front.md
source_content_sha256: 3d6c1645013adada5ed8396c103bb95dcd22e4e3723d8c5352a4ba786fc9c140
translation_model: gpt-5
translation_run: 20260915T020405Z
glossary_version: 6
glossary_terms_sha256: fcb84f53aa78484b92ff53c9baf55147dd1cf39c33fa0b3519c4a3322d452302
prompt_sha256: da0c2696badfbe5d93fdc534847b1b0ca3b25ec37e0ce29843665f6e701c278e
---

SCHEME

扩展 Lambda 演算的解释器

Gerald Jay Sussman 和 Guy Lewis Steele Jr.

摘要：

受 ACTORS [Greif and Hewitt] [Smith and Hewitt] 启发，我们实现了一个类似 LISP 的编程语言 SCHEME 的解释器。该编程语言基于 Lambda 演算 [Church]，但扩展了副作用、多进程以及进程同步机制。该实现的目的在于教学。我们希望：

(1) 通过澄清像 LISP 这样的递归宿主语言中非递归控制结构的嵌入方式，减轻由 Micro-PLANNER、CONNIVER 等造成的困惑。

(2) 解释如何使用这些控制结构，而不涉及模式匹配和数据库操作等问题。

(3) 为编程语义和风格中的某些问题提供一个简单具体的实验领域。

本文组织为若干部分。第一部分是一个简短的“参考手册”，包含 SCHEME 所有特殊特性的规范。接下来，我们给出一系列程序示例，用以说明各种程序设计风格以及如何使用它们。这将引出一些语义问题，我们将在第三部分尝试用 Lambda 演算对其进行澄清。在第四部分，我们将对基于 Lambda 演算的编程语言的解释器实现者所面临的问题进行总体讨论。最后，我们将给出一个完全注释的 SCHEME 解释器，该解释器使用 MacLISP [Moon] 编写，以使程序员了解在类似 LISP 这样的递归语言中实现非递归控制结构的技巧。
