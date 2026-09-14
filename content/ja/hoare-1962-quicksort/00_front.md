---
paper: hoare-1962-quicksort
title: Quicksort
authors:
  - C. A. R. Hoare
year: 1962
venue: The Computer Journal
field: algorithms
section_title: Front Matter
tag: 003E
kind: front
lang: ja
source: https://www.cs.ox.ac.uk/files/6226/H2006%20-%20Historic%20Quicksort.pdf
pdf_sha256: 1b54e36fac02a0c19213e2858090fa1dca70688f5f99a2748357fd8329918bab
pdf_pages: 1-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 7b447e252d043fa01f288cdfad46492d5c609fb89493b2048d9d0962117167dc
translated_from: content/en/hoare-1962-quicksort/00_front.md
source_content_sha256: 5a2c556e140ce09b780ceded5b579736cdc08e0ccc54fb57bff8095213749a91
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: 81be60ea3284bdc3129ecda2524a99e799d0b3ec06fd0a74a1fb3922eda78382
prompt_sha256: 28abc9ae7c2a46d63213afc528700760d76ff5866e775238c90c95b3052a886f
---

クイックソート

分割処理を適用するたびに、ソートすべき2つのセグメントが残る。これらのセグメントのいずれかが空であるか、単一の項目だけから成る場合には、それを無視して、もう一方のセグメントだけで処理を続ければよい。さらに、セグメントが3個または4個未満の項目から成る場合（コンピューターの特性による）には、特定の少数の項目をソートするために特別に書かれたプログラムを用いてソートするのが有利である。最後に、両方のセグメントがかなり大きい場合には、一方が完全にソートされるまで、他方の処理を延期する必要がある。その間、延期されたセグメントの最初と最後の項目のアドレスを保存しておかなければならない。セグメントの詳細を格納するための記憶領域を節約することは非常に重要である。なぜなら、セグメントの総数はソートされる項目数に比例するからである。幸いにも、すべてのセグメントの詳細を同時に保存する必要はない。すでに完全にソートされたセグメントの詳細は、もはや必要ないからである。

推奨される格納方法では、ネスト、すなわちポインタに関連付けられた連続した記憶場所のブロックを使用する。このポインタは常に、その内容を上書きしてよいブロックの中で最も低いアドレスの場所を指す。最初は、ポインタはブロックの最初の場所を指している。
