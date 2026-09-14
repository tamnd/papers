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
lang: ja
source: https://ir.cwi.nl/pub/9256/9256D.pdf
pdf_sha256: ee0938a64a327cf6d60c25115ae98990417224408d9c062f09907a044e045ac0
pdf_pages: 1-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 114ce59c92667f29552095e345cb7c909b0af73bf7591ec7b321cb0c2a6ce2dd
translated_from: content/en/dijkstra-1959-shortestpath/00_front.md
source_content_sha256: 584ada85ee4b242ab88f6aec897b92de14d45b2b822306bde835bf4e815a61ca
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: 81be60ea3284bdc3129ecda2524a99e799d0b3ec06fd0a74a1fb3922eda78382
prompt_sha256: 28abc9ae7c2a46d63213afc528700760d76ff5866e775238c90c95b3052a886f
---

グラフに関連する二つの問題についての覚え書き

By

E. W. DIJKSTRA

$n$ 個の点（ノード）を考える。そのいくつかまたはすべての対は分岐によって接続されており、各分岐の長さは与えられている。任意の二つのノード間に少なくとも一つの経路が存在する場合に限定する。ここで二つの問題を考える。

問題 1. $n$ 個のノード間における全長が最小の木を構成せよ。（木とは、任意の二つのノード間に一つだけの経路をもつグラフである。）

ここで提示する構成の過程において、分岐は三つの集合に分割される。

I. 構成中の木に確定的に割り当てられた分岐（これらは部分木を形成する）；

II. 集合 I に次に追加される分岐を選択する元となる分岐；

III. 残りの分岐（棄却されたもの、またはまだ考慮されていないもの）。

ノードは二つの集合に分割される：

A. 集合 I の分岐によって接続されたノード、

B. 残りのノード（集合 II の一つかつ唯一の分岐が、これらの各ノードへ向かう）。

構成は、集合 A の唯一のメンバーとして任意の一つのノードを選択し、このノードで終わるすべての分岐を集合 II に入れることによって開始する。開始時には、集合 I は空である。それ以後、次の二つのステップを繰り返し実行する。

ステップ 1. 集合 II の最短の分岐をこの集合から取り除き、集合 I に追加する。
