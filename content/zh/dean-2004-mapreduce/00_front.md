---
paper: dean-2004-mapreduce
title: 'MapReduce: Simplified Data Processing on Large Clusters'
authors:
  - Jeffrey Dean
  - Sanjay Ghemawat
year: 2004
venue: OSDI
field: systems
section_title: Front Matter
kind: front
lang: zh
source: https://www.usenix.org/legacy/events/osdi04/tech/full_papers/dean/dean.pdf
pdf_sha256: 9cfef3ef1b8fe1a1b66c7221f56c2eeca0b15d6608ea68b0c85a38bfbffd8ce5
pdf_pages: "1"
extraction: vision
extraction_model: gpt-5
content_sha256: 1e8119e96bd8d0ec555171db6f4cf00ed6da19b38483c4312d784a858bf3c429
translated_from: content/en/dean-2004-mapreduce/00_front.md
source_content_sha256: 50e40e1d76bad207cd63412840af8cf2e0fc4432de8ad0628778084393f54a7f
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: 7271f7a32ca37292fd19d5ef38fdc1daa670346e7d1f46fdd75a6f589873c903
prompt_sha256: da0c2696badfbe5d93fdc534847b1b0ca3b25ec37e0ce29843665f6e701c278e
---

**MapReduce：大规模集群上的简化数据处理**

Jeffrey Dean 和 Sanjay Ghemawat jeff@google.com, sanjay@google.com

*Google, Inc.*

摘要

MapReduce 是一种用于处理和生成大型数据集的编程模型及其相关实现。用户指定一个 *map* 函数，该函数处理一个键/值对以生成一组中间键/值对，并指定一个 *reduce* 函数，该函数合并与同一个中间键关联的所有中间值。正如本文所示，许多现实世界任务都可以用该模型表示。

以这种函数式风格编写的程序会自动并行化，并在大型廉价机器集群上执行。运行时系统负责输入数据分区、在一组机器间调度程序执行、处理机器故障以及管理所需的机器间通信等细节。这使得没有并行和分布式系统经验的程序员也可以轻松利用大型分布式系统的资源。

我们的 MapReduce 实现在大型廉价机器集群上运行，并具有很高的可扩展性：典型的 MapReduce 计算会在数千台机器上处理许多 TB 的数据。程序员发现该系统易于使用：已经实现了数百个 MapReduce 程序，并且每天在 Google 的集群上执行超过一千个 MapReduce 作业。
