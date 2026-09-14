---
paper: denning-1968-workingset
title: The Working Set Model for Program Behavior
authors:
  - Peter J. Denning
year: 1968
venue: Communications of the ACM
field: systems
section_title: Front Matter
tag: 004E
kind: front
lang: zh
source: https://doi.org/10.1145/800001.811670
pdf_sha256: 3585991156b07c7e878ea9dff16ef7721401adff09ee328f5ee247b016289e0f
pdf_pages: 1-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 93772936f1f56afe78a8f1d3ebd21aae51c2b5369503960297bee59d045f4b91
translated_from: content/en/denning-1968-workingset/00_front.md
source_content_sha256: 1a0f412b8f796cd2bda77a1d352f7e118a00f27155e048d18edd6ba0345da370
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: 7271f7a32ca37292fd19d5ef38fdc1daa670346e7d1f46fdd75a6f589873c903
prompt_sha256: da0c2696badfbe5d93fdc534847b1b0ca3b25ec37e0ce29843665f6e701c278e
---

程序行为的工作集模型

Peter J. Denning

麻省理工学院，剑桥，马萨诸塞州

现代计算机系统中缺少对资源分配的一般处理的最基本原因，可能是缺乏一个足够的程序行为模型。本文提出并发展了一种新模型，即“工作集模型”。与一个进程相关联的页面的工作集，被定义为其最近使用的页面集合，为分页内存的动态管理提供了至关重要的知识。我们说明“进程”和“工作集”是同一持续计算活动的表现形式；随后定义“处理器需求”和“内存需求”；并将资源分配表述为在需求与可用设备之间进行平衡的问题。

关键词和短语：一般操作系统概念，多处理，多道程序设计，操作系统，程序行为，程序模型，资源分配，调度，存储分配

CR 分类：4.30，4.32

1. 引言

资源分配是一项棘手的工作。最近，人们对进程调度和主内存管理进行了大量讨论，然而技术的发展却沿着这两个方向独立推进。没有人会否认，需要一种统一的方法。本文将说明，建立一种统一的方法是可能的。从观察到每个正在运行的程序会同时对所有系统资源，特别是处理器和内存，提出需求开始，我们最终定义“系统需求”；资源分配问题将由在需求与可用资源之间进行平衡构成。
