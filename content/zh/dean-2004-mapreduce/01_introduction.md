---
paper: dean-2004-mapreduce
title: 'MapReduce: Simplified Data Processing on Large Clusters'
authors:
  - Jeffrey Dean
  - Sanjay Ghemawat
year: 2004
venue: OSDI
field: systems
section: "1"
section_title: 引言
kind: section
lang: zh
source: https://www.usenix.org/legacy/events/osdi04/tech/full_papers/dean/dean.pdf
pdf_sha256: 9cfef3ef1b8fe1a1b66c7221f56c2eeca0b15d6608ea68b0c85a38bfbffd8ce5
pdf_pages: 1-2
extraction: vision
extraction_model: gpt-5
content_sha256: ab312c350d329a991dd99f7080ad5d524bf9a6cc32074124231cd789ca66d07d
translated_from: content/en/dean-2004-mapreduce/01_introduction.md
source_content_sha256: ecd74842b3eddb127d86aec0b3f6588f7aaffeaf23a4676b745e58c293a81f7f
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: 7271f7a32ca37292fd19d5ef38fdc1daa670346e7d1f46fdd75a6f589873c903
prompt_sha256: da0c2696badfbe5d93fdc534847b1b0ca3b25ec37e0ce29843665f6e701c278e
---

在过去五年中，作者以及 Google 的许多人已经实现了数百个专用计算，这些计算处理大量原始数据，例如抓取的文档、网络请求日志等，以计算各种派生数据，例如倒排索引、Web 文档图结构的各种表示、每个主机抓取页面数量的摘要、某一天中最频繁查询的集合等。大多数此类计算在概念上都很直接。然而，输入数据通常很大，为了在合理的时间内完成计算，必须将这些计算分布到数百或数千台机器上。如何并行化计算、分发数据以及处理故障等问题，共同导致需要大量复杂代码来处理这些问题，从而掩盖了原本简单的计算。

针对这种复杂性，我们设计了一种新的抽象，使我们能够表达试图执行的简单计算，同时将并行化、容错、数据分布和负载均衡等繁琐细节隐藏在一个库中。我们的抽象受到了 Lisp 以及许多其他函数式语言中存在的 *map* 和 *reduce* 原语的启发。我们意识到，大多数计算都涉及对输入中的每个逻辑“记录”应用 *map* 操作，以计算一组中间键/值对，然后对共享同一键的所有值应用 *reduce* 操作，以适当地组合派生数据。我们使用带有用户指定 map 和 reduce 操作的函数式模型，使我们能够轻松并行化大型计算，并使用重新执行作为容错的主要机制。

这项工作的主要贡献是一个简单而强大的接口，它能够自动并行化和分发大规模计算，并结合了该接口的一种实现，该实现能够在大型廉价 PC 集群上达到高性能。

第 2 节描述了基本编程模型并给出了几个示例。第 3 节描述了针对我们的基于集群的计算环境定制的 MapReduce 接口实现。第 4 节描述了我们发现有用的编程模型的若干改进。第 5 节给出了我们的实现针对各种任务的性能测量结果。第 6 节探讨了 MapReduce 在 Google 内部的使用，包括我们将其作为重写生产索引系统基础时的经验。第 7 节讨论了相关工作和未来工作。
