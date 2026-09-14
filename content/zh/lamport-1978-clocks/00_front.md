---
paper: lamport-1978-clocks
title: Time, Clocks, and the Ordering of Events in a Distributed System
authors:
  - Leslie Lamport
year: 1978
venue: Communications of the ACM
field: systems
section_title: Front Matter
tag: 004F
kind: front
lang: zh
source: https://lamport.azurewebsites.net/pubs/time-clocks.pdf
pdf_sha256: c55e7cab4230aa3d7126748a149b2db6f0d7a67296d5eccfdd50a210299a96b2
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 9210a48c15b41644a3520a7de3c6edffd5b073058b91d8d82696e5490d146666
translated_from: content/en/lamport-1978-clocks/00_front.md
source_content_sha256: 4b7ae7f50483519411ec5d2ce1d6efe1cc22702f57cad988b4035630cf300048
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: 7271f7a32ca37292fd19d5ef38fdc1daa670346e7d1f46fdd75a6f589873c903
prompt_sha256: da0c2696badfbe5d93fdc534847b1b0ca3b25ec37e0ce29843665f6e701c278e
---

分布式系统中事件的时间、时钟与排序

Leslie Lamport
Massachusetts Computer Associates, Inc.

本文考察了分布式系统中一个事件发生在另一个事件之前的概念，并证明它定义了事件的偏序。给出了一个用于同步逻辑时钟系统的分布式算法，该系统可用于对事件进行全序排序。利用这种全序排序，本文说明了一种解决同步问题的方法。随后，该算法被专门化用于同步物理时钟，并推导出时钟可能产生的最大不同步界限。

关键词和短语：分布式系统，计算机网络，时钟同步，多进程系统

CR 分类：4.32，5.29
