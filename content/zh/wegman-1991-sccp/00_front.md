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
lang: zh
source: https://www.cs.utexas.edu/users/lin/cs380c/wegman.pdf
pdf_sha256: 40929436cdf1c477f2318221df5d0aa71488db4a01cc448b184e0aba8bf95ddb
pdf_pages: "2"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 4d8cac2635622870ae3b2bae386090ccc182ed17aba33a73aff1b9eb7e9f5260
translated_from: content/en/wegman-1991-sccp/00_front.md
source_content_sha256: 94ce5b5dba477ad2c0e4754f4c994d52f8979f20334977030a8748c85db9197d
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: fcb84f53aa78484b92ff53c9baf55147dd1cf39c33fa0b3519c4a3322d452302
prompt_sha256: da0c2696badfbe5d93fdc534847b1b0ca3b25ec37e0ce29843665f6e701c278e
---

虽然通常很容易证明常量传播问题是不可判定的（例如参见 Kam 和 Ullman [25]），但该问题存在许多合理的实例，它们是可判定的，并且存在计算效率较高的算法。我们在本文中给出了四种这样的算法。这里给出的每个算法都是保守的，即可能无法找到所有常量，但找到的每个常量在程序的所有可能执行中都是常量。

在介绍了一些预备知识之后，我们在第 3 节中按照能力递增的顺序介绍这些算法；每个后续算法至少能找到前一个算法所找到的常量。前三种算法是对他人工作的重新表述；第四种算法是新的，并包含前三种算法各自的最佳特性。这些算法属于已知的最简单、最快且功能最强大的全局常量传播算法之列。在第 4 节中，我们证明了我们的算法是正确的，并且至少与具有多项式时间界的最佳已有算法一样强大。在第 5 节中，我们讨论了一些常见的实现问题。

在第 6 节中，我们探索了若干种在大于单个过程的范围内执行常量传播的技术。在第 6.2 节中，我们讨论了常量传播与过程集成之间的关系。第 6.3 节给出了一种新的算法，该算法执行一种形式的过程间数据流分析，其中别名信息与常量传播结合收集。

第 7 节概述了一些开放问题，第 8 节总结了本文。

### 1. {#wegman-1991-sccp-s-1 .section tag=012F}
