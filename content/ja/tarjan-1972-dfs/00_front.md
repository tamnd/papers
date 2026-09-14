---
paper: tarjan-1972-dfs
title: Depth-First Search and Linear Graph Algorithms
authors:
  - Robert Tarjan
year: 1972
venue: SIAM Journal on Computing
field: algorithms
section_title: Front Matter
tag: "0042"
kind: front
lang: ja
source: https://sites.cs.ucsb.edu/~gilbert/cs240a/old/cs240aSpr2011/slides/TarjanDFS.pdf
pdf_sha256: d0ee53bb4bf82602cb5dd7bd08f39927f6d0253cb30c79aaa84378ac6b94f064
pdf_pages: 1-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 948129fee533c5f260ea4ad2d49c2b5d0cb67d09615982e0dc1c1c6fe8f56fc5
translated_from: content/en/tarjan-1972-dfs/00_front.md
source_content_sha256: a6bb930a7d126f94c5bf7a8bffeab75ba66f08f01883677a22d1abde48aab6bd
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: 81be60ea3284bdc3129ecda2524a99e799d0b3ec06fd0a74a1fb3922eda78382
prompt_sha256: 28abc9ae7c2a46d63213afc528700760d76ff5866e775238c90c95b3052a886f
---

深さ優先探索と線形グラフアルゴリズム*

要約。深さ優先探索または「バックトラッキング」を問題を解くための手法として用いる価値を、二つの例によって示す。向き付きグラフの強連結成分を求めるアルゴリズムの改良版と、無向グラフの二重連結成分を求めるアルゴリズムを提示する。両方のアルゴリズムの空間および時間要件は、ある定数 $k_1, k_2,$ および $k_3$ に対して $k_1 V + k_2 E + k_3$ によって上界付けられる。ただし、$V$ は調べているグラフの頂点数であり、$E$ は辺数である。
