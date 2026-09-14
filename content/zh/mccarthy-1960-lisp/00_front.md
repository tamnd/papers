---
paper: mccarthy-1960-lisp
title: Recursive Functions of Symbolic Expressions and Their Computation by Machine, Part I
authors:
  - John McCarthy
year: 1960
venue: Communications of the ACM
field: languages
section_title: Front Matter
tag: "0001"
kind: front
lang: zh
source: http://www-formal.stanford.edu/jmc/recursive.pdf
pdf_sha256: 3d981849e59505eff3f14397a177b409f5d978d43d114bdd67c956e74320fc92
pdf_pages: 1-3
extraction: native
extraction_model: pdftotext version 26.09.0
content_sha256: a763442027cb3b3cc9669a96fdaa8b0e520d0b9199a2b8c613c52df3db502396
translated_from: content/en/mccarthy-1960-lisp/00_front.md
source_content_sha256: 99ca45842e94baac0c4a8a87f87f893ac11b3ca331c2904346168b690e50dcd7
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: fcb84f53aa78484b92ff53c9baf55147dd1cf39c33fa0b3519c4a3322d452302
prompt_sha256: da0c2696badfbe5d93fdc534847b1b0ca3b25ec37e0ce29843665f6e701c278e
---

符号表达式的递归函数

及其机器计算，第一部分

John McCarthy，Massachusetts Institute of Technology，Cambridge，Mass. ∗

1960年4月

1 引言

麻省理工学院（M.I.T.）人工智能组为IBM 704计算机开发了一个称为LISP（LISt Processor）的编程系统。该系统旨在促进对一个称为Advice Taker的提出中的系统的实验，通过该系统，可以指示机器处理陈述句以及命令句，并且在执行其指令时表现出“常识”。Advice Taker的最初提议[1]发表于1958年11月。主要要求是一个用于操纵表示形式化陈述句和命令句的表达式的编程系统，从而使Advice Taker系统能够进行推导。

在开发过程中，LISP系统经历了几个简化阶段，最终建立在一种表示某类符号表达式的部分递归函数的方案之上。这种表示独立于IBM 704计算机或任何其他电子计算机，现在看来，从称为S表达式的表达式类以及称为S函数的函数开始阐述该系统是适宜的。

∗ 将本文置于由ARPA（ONR）资助的N00014-94-1-0775项目中的L A

TEX部分归属于Stanford University，John McCarthy自1962年以来一直在那里。根据CACM 1960年4月刊复制，并进行了少量符号修改。如果需要准确的排版，请参阅该处。
