---
paper: backus-1978-vonneumann
title: Can Programming Be Liberated from the von Neumann Style? A Functional Style and Its Algebra of Programs
authors:
  - John Backus
year: 1978
venue: Communications of the ACM (Turing Award lecture)
field: languages
section_title: Front Matter
tag: "0049"
kind: front
lang: zh
source: https://www.cs.cmu.edu/~crary/819-f09/Backus78.pdf
pdf_sha256: 2e412a7986c7fd1bdd060d90d035faa9ecc8a29675f99206c243da90954ca423
pdf_pages: 1-2
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 98934778f35199687afdcef7cef8d9f2e27c50461962ed0cfd1198e57a6c2a57
translated_from: content/en/backus-1978-vonneumann/00_front.md
source_content_sha256: 752feced1622b510f0705492c1cbfb9e3b6bd628b154c0b11f2d80acdd041ccc
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: fcb84f53aa78484b92ff53c9baf55147dd1cf39c33fa0b3519c4a3322d452302
prompt_sha256: da0c2696badfbe5d93fdc534847b1b0ca3b25ec37e0ce29843665f6e701c278e
---

从冯·诺依曼风格中解放编程？一种函数式风格及其程序代数

John Backus

IBM Research Laboratory, San Jose

传统编程语言变得越来越庞大，但并没有变得更强大。在最基本层面固有的缺陷使它们既臃肿又弱小：它们从共同祖先——冯·诺依曼计算机继承而来的原始逐字编程风格，它们将语义与状态转换紧密耦合，它们将编程划分为表达式世界和语句世界，它们无法有效地使用强大的组合形式从已有程序构建新程序，以及它们缺乏用于推理程序的有用数学性质。

一种替代性的函数式编程风格建立在使用组合形式创建程序之上。函数式程序处理结构化数据，通常是非重复和非递归的，以层次方式构造，不命名其参数，并且不需要复杂的过程声明机制即可具有普遍适用性。组合形式可以使用高级程序构建更高级的程序，这种风格是传统语言所无法实现的。

与函数式编程风格相关的是一种程序代数，其中变量的取值范围是程序，其运算是组合形式。该代数可以用于转换程序，并求解其“未知量”为程序的方程，其方式与高中代数中转换方程的方式大致相同。
