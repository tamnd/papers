---
paper: cytron-1991-ssa
title: Efficiently Computing Static Single Assignment Form and the Control Dependence Graph
authors:
  - Ron Cytron
  - Jeanne Ferrante
  - Barry K. Rosen
  - Mark N. Wegman
  - F. Kenneth Zadeck
year: 1991
venue: ACM TOPLAS
field: languages
section_title: Front Matter
tag: 004B
kind: front
lang: ja
source: https://www.cs.utexas.edu/~pingali/CS380C/2010/papers/ssaCytron.pdf
pdf_sha256: 307512bb537628c2b326b23aa02109e7562bfc619509e942e015054ab58eb9ab
pdf_pages: 2-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 707826f771efe86ee78a0ecaffdc2d416feccd5a9a6fc94acc598f4dfab63202
translated_from: content/en/cytron-1991-ssa/00_front.md
source_content_sha256: cb78a10f4d23a546d27c2bc0b9089d4c80ae88412348f20f31845a48fa971fc6
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: 07dd8f2ee4792b6dc2b4d5c388a078378107a558371bfe6613a7ad1bb7578218
prompt_sha256: 28abc9ae7c2a46d63213afc528700760d76ff5866e775238c90c95b3052a886f
---

一般用語：アルゴリズム、言語
追加キーワードおよびフレーズ：制御依存関係、制御フローグラフ、定義使用チェーン、支配者、最適化コンパイラ

最適化コンパイラにおいて、データ構造の選択は、実用的なプログラム最適化の能力と効率に直接影響を与える。データ構造の選択を誤ると、最適化が妨げられたり、コンパイルが遅くなったりして、高度な最適化機能が望ましくないものとなる可能性がある。近年、静的単一代入形式 (SSA) [5, 43] と制御依存グラフ [24] が、プログラムのデータフローおよび制御フローの特性を表現するために提案されている。これらの、従来は互いに関連していなかった技法は、それぞれ有用なプログラム最適化の一群に効率性と能力をもたらす。これら2つの構造はいずれも魅力的であるが、その構築の困難さと潜在的なサイズが、その利用を妨げてきた [4]。本論文では、任意の制御フローグラフに対してこれらのデータ構造を効率的に計算する新しいアルゴリズムを提示する。これらのアルゴリズムは、他の応用にも利用できる可能性のある新しい概念である支配フロンティアを用いる。また、すべての支配フロンティアのサイズの総和が、通常、元のプログラムのサイズに対して線形であることを示す解析的および実験的な証拠も提示する。したがって本論文は、SSA形式と制御依存関係が最適化において実用的に利用できることを示す強力な証拠を提示する。
