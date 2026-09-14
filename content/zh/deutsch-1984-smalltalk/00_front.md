---
paper: deutsch-1984-smalltalk
title: Efficient Implementation of the Smalltalk-80 System
authors:
  - L. Peter Deutsch
  - Allan M. Schiffman
year: 1984
venue: POPL
field: languages
section_title: Front Matter
tag: 004A
kind: front
lang: zh
source: https://doi.org/10.1145/800017.800542
pdf_sha256: 300584e302ee0fa5a006ee363d9e3f1b0df043c3259580e32dcd409e9a09871d
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: ddf1aabcc04285f18ee8e29acdb91c0dc0f2fbe55185fbd621475afa407d1b03
translated_from: content/en/deutsch-1984-smalltalk/00_front.md
source_content_sha256: 64032bbbb8fd182a69fb8ac6e35b65d90ee769ed62ed7b817d5f46f08accd2c1
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: fcb84f53aa78484b92ff53c9baf55147dd1cf39c33fa0b3519c4a3322d452302
prompt_sha256: da0c2696badfbe5d93fdc534847b1b0ca3b25ec37e0ce29843665f6e701c278e
---

Efficient Implementation of the Smalltalk-80 System

L. Peter Deutsch
Xerox PARC, Software Concepts Group

Allan M. Schiffman
Fairchild Laboratory for Artificial Intelligence Research

摘要

Smalltalk-80*编程语言包括动态存储分配、完全向上的 funargs 和通用多态过程；Smalltalk-80程序系统具有交互式执行、增量编译以及实现可移植性。这些现代程序系统的特性即使单独来看，也是最难以高效实现的特性之一。一个新的Smalltalk-80系统实现运行在基于小型微处理器的计算机上，在保持与现有实现完全（对象代码）兼容的同时，达到了高性能。本文讨论了项目过程中开发出的最重要的优化技术，其中许多技术适用于其他语言。其核心思想是以多种形式表示某些运行时状态（包括代码和数据），并在需要时在这些形式之间进行转换。

*Smalltalk-80是Xerox Corporation的商标。
