---
paper: lamport-1998-paxos
title: The Part-Time Parliament
authors:
  - Leslie Lamport
year: 1998
venue: ACM TOCS
field: systems
section_title: Front Matter
tag: "0002"
kind: front
lang: zh
source: https://lamport.azurewebsites.net/pubs/lamport-paxos.pdf
pdf_sha256: cd9544e9615bcd417a2c10063671cecca0b28ad4bc5db3f64467a83ecc7028d3
pdf_pages: 1-3
extraction: native
extraction_model: pdftotext version 26.09.0
content_sha256: fe6d2da27409a6d703b1ddd9653d18c33ff0637625c21376e95e965a4ae3dc10
translated_from: content/en/lamport-1998-paxos/00_front.md
source_content_sha256: 6fac3ffae0952fb7c9d43c72bac006ed766ea295dfe0b80314b76a08bf5a7a76
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: 7271f7a32ca37292fd19d5ef38fdc1daa670346e7d1f46fdd75a6f589873c903
prompt_sha256: da0c2696badfbe5d93fdc534847b1b0ca3b25ec37e0ce29843665f6e701c278e
---

兼职议会

Leslie Lamport

本文发表于《ACM Transactions on Computer Systems》16，2（1998年5月），133-169页。2000年8月29日进行了小幅修正。

兼职议会

LESLIE LAMPORT Digital Equipment Corporation

最近在帕克索斯岛上的考古发现表明，尽管其兼职立法者四处奔波，议会仍然能够正常运作。尽管立法者经常离开议事厅，并且他们的信使经常遗忘信息，他们仍维护了议会记录的一致副本。帕克索斯议会的协议为设计分布式系统时实现状态机方法提供了一种新方式。类别和主题描述：C2.4［计算机通信网络］：分布式系统——网络操作系统；D4.5［操作系统］：可靠性——容错；J.1［行政数据处理］：政府 通用术语：设计，可靠性 其他关键词和短语：状态机，三阶段提交，投票

这篇投稿最近在TOCS编辑部的一个文件柜后面被发现。尽管它年代久远，主编仍认为它值得发表。由于作者目前正在希腊群岛进行实地考察，无法联系到他，我被要求为其出版做准备。

作者似乎是一名考古学家，对计算机科学只有浅显的兴趣。这很遗憾；尽管他所描述的鲜为人知的古代帕克索斯文明对大多数计算机科学家而言并无太大兴趣，但其立法系统是如何在异步环境中实现分布式计算机系统的一个优秀模型。
