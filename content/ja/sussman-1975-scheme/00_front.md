---
paper: sussman-1975-scheme
title: 'Scheme: An Interpreter for Extended Lambda Calculus'
authors:
  - Gerald Jay Sussman
  - Guy L. Steele Jr.
year: 1975
venue: MIT AI Memo 349
field: languages
section_title: Front Matter
tag: "0047"
kind: front
lang: ja
source: https://dspace.mit.edu/server/api/core/bitstreams/70ab0fe6-0e7a-41ef-99fb-ac2c9481a05e/content
pdf_sha256: c2961e078943a26ae1f752b202290f561578b7ecf8b24b8929e3c1f99e6b2c52
pdf_pages: 1-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 465fa5e2a4a1b400bde68cc2e3408be23c348bdfda76de2773d76349ddbe7f8b
translated_from: content/en/sussman-1975-scheme/00_front.md
source_content_sha256: 3d6c1645013adada5ed8396c103bb95dcd22e4e3723d8c5352a4ba786fc9c140
translation_model: gpt-5
translation_run: 20260915T020405Z
glossary_version: 6
glossary_terms_sha256: 07dd8f2ee4792b6dc2b4d5c388a078378107a558371bfe6613a7ad1bb7578218
prompt_sha256: 28abc9ae7c2a46d63213afc528700760d76ff5866e775238c90c95b3052a886f
---

SCHEME

拡張ラムダ計算のためのインタープリタ

Gerald Jay Sussman and Guy Lewis Steele Jr.

要旨：

ACTORS [Greif and Hewitt] [Smith and Hewitt] に触発され、ラムダ計算 [Church] に基づき、副作用、マルチプロセシング、プロセス同期のために拡張されたLISP風言語SCHEMEのインタープリタを実装した。この実装の目的はチュートリアル的なものである。目的は次のとおりである：

(1) Micro-PLANNER、CONNIVERなどによって引き起こされた混乱を、LISPのような再帰的ホスト言語における非再帰的制御構造の埋め込みを明確にすることによって軽減する。

(2) パターンマッチングやデータベース操作などの問題とは独立して、これらの制御構造をどのように使用するかを説明する。

(3) プログラミングの意味論とスタイルに関する特定の問題のための、単純で具体的な実験領域を提供する。

本論文はセクションに分けて構成されている。最初のセクションは短い「リファレンスマニュアル」であり、SCHEMEのすべての特殊な機能についての仕様を含んでいる。次に、さまざまなプログラミングスタイルと、それらの使用方法を示す一連のプログラミング例を提示する。これによって意味論に関するいくつかの問題が生じるが、第3セクションではラムダ計算を用いてそれらを明らかにする。第4セクションでは、ラムダ計算に基づく言語のインタープリタを実装する者が直面する問題について一般的に論じる。最後に、LISPのような再帰的言語において非再帰的制御構造を実装するための実践的な技法をプログラマに理解してもらうため、MacLISP [Moon] で記述した、完全に注釈を付したSCHEMEのインタープリタを提示する。
