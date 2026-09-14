---
paper: birrell-1984-rpc
title: Implementing Remote Procedure Calls
authors:
  - Andrew D. Birrell
  - Bruce Jay Nelson
year: 1984
venue: ACM TOCS
field: systems
section_title: Front Matter
tag: "0051"
kind: front
lang: zh
source: https://www.cs.cmu.edu/~dga/15-712/F07/papers/birrell842.pdf
pdf_sha256: 0c5058383786e2b3e8fa9894872358e362a6f6ffc58c06f29dc08b836318f432
pdf_pages: 2-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: eb022532cb268bf1d61a9516c80413e77aeb1af9bee625eb535d2a86ad98a3db
translated_from: content/en/birrell-1984-rpc/00_front.md
source_content_sha256: 443c55fbdd07742a112658c60d65e70a2b25966b03a3fec4d237d8c751d86d25
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: 7271f7a32ca37292fd19d5ef38fdc1daa670346e7d1f46fdd75a6f589873c903
prompt_sha256: da0c2696badfbe5d93fdc534847b1b0ca3b25ec37e0ce29843665f6e701c278e
---

仍然执行（取决于该环境的并行性细节以及 RPC 实现）。

这个想法有许多吸引人的方面。其中之一是清晰而简单的语义：这应当使构建分布式计算并使其正确实现变得更加容易。另一个方面是效率：过程调用似乎足够简单，因此通信可以非常快速。第三个方面是通用性：在单机计算中，过程通常是算法各部分之间通信的最重要机制。

RPC 的思想已经存在了许多年。至少从 1976 年以来，它已经在公开文献中被多次讨论过 [15]。Nelson 的博士论文 [13] 对 RPC 系统的设计可能性进行了广泛研究，并引用了许多早期关于 RPC 的工作。然而，完整规模的 RPC 实现比论文设计更为少见。近期值得注意的工作包括 Xerox NS 协议族中的 Courier [4]，以及 MIT 当前的工作 [10]。

本文源于为 Cedar 项目构建 RPC 工具的工作。由于之前的工作（特别是 Nelson 的论文及相关实验），我们认为自己理解了 RPC 工具设计者必须做出的选择。我们的任务是在特定目标和环境的背景下做出这些选择。在实践中，我们发现若干领域的理解还不充分，并且我们构建了一个设计具有若干新颖方面的系统。
