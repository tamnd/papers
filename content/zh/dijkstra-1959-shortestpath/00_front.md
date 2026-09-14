---
paper: dijkstra-1959-shortestpath
title: A Note on Two Problems in Connexion with Graphs
authors:
  - Edsger W. Dijkstra
year: 1959
venue: Numerische Mathematik
field: algorithms
section_title: Front Matter
tag: 003D
kind: front
lang: zh
source: https://ir.cwi.nl/pub/9256/9256D.pdf
pdf_sha256: ee0938a64a327cf6d60c25115ae98990417224408d9c062f09907a044e045ac0
pdf_pages: 1-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 9c4c2babc7bb93ed2306afc2136a4b1304dc96313c81f532afd8ddfe8c1f63bd
translated_from: content/en/dijkstra-1959-shortestpath/00_front.md
source_content_sha256: 584ada85ee4b242ab88f6aec897b92de14d45b2b822306bde835bf4e815a61ca
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: efacc7653691a9b863e3c4cb746743abfecf7d31e7791764c13a541e1906db0f
prompt_sha256: da0c2696badfbe5d93fdc534847b1b0ca3b25ec37e0ce29843665f6e701c278e
---

关于图的两个问题的一点注记

作者

E. W. DIJKSTRA

我们考虑$n$个点（节点），其中某些或所有点对由一条分支连接；每条分支的长度均已给定。我们限于考虑任意两个节点之间至少存在一条路径的情形。现在考虑两个问题。

问题1。构造连接这$n$个节点且总长度最小的树。（树是这样一种图：任意两个节点之间有且仅有一条路径。）

在我们这里给出的构造过程中，将分支划分为三个集合：

I. 确定归入正在构造的树中的分支（它们将构成一个子树）；

II. 将从中选取下一条加入集合I的分支的分支；

III. 其余分支（已拒绝或尚未考虑）。

将节点划分为两个集合：

A. 由集合I中的分支连接的节点，

B. 其余节点（集合II中恰有一条分支通向这些节点中的每一个）。

我们首先任意选择一个节点作为集合A的唯一成员，并将所有终止于该节点的分支置于集合II中。开始时，集合I为空。此后，我们反复执行以下两个步骤。

步骤1。从集合II中移除最短的分支，并将其加入集合I。
