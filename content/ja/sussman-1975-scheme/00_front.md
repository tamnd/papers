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
content_sha256: 3b988a62e6948ce1143ad06653af6fa8a4eb35d192adb95af35fb0e5a33e3ccc
translated_from: content/en/sussman-1975-scheme/00_front.md
source_content_sha256: 326c3043a5d2c15ce603ddfd07ea950af19f0f9587bb0f8c53dce7b8a3d04f66
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: 07dd8f2ee4792b6dc2b4d5c388a078378107a558371bfe6613a7ad1bb7578218
prompt_sha256: 28abc9ae7c2a46d63213afc528700760d76ff5866e775238c90c95b3052a886f
---

マサチューセッツ工科大学

人工知能研究所

AI Memo No. 349

1975年12月

SCHEME

拡張ラムダ計算のインタプリタ

著者

Gerald Jay Sussman and Guy Lewis Steele Jr.

概要：

ACTORS [Greif and Hewitt] [Smith and Hewitt] に触発され、ラムダ計算 [Church] に基づくLISP風言語SCHEMEのインタプリタを実装した。ただし、側作用、マルチプロセス処理、およびプロセス同期のために拡張されている。本実装の目的は教育的なものである。目的は次のとおりである。

(1) Micro-PLANNER、CONNIVERなどによって引き起こされた混乱を、LISPのような再帰的ホスト言語における非再帰的制御構造の埋め込みを明確にすることによって軽減する。

(2) パターンマッチングやデータベース操作などの問題とは独立して、これらの制御構造の使用方法を説明する。

(3) プログラミングの意味論およびスタイルに関する特定の問題を扱うための、単純で具体的な実験領域を持つ。

本論文は、複数の節から構成されている。第1節は、SCHEMEのすべての特異な機能についての仕様を含む短い「リファレンスマニュアル」である。次に、さまざまなプログラミングスタイルとその使用方法を例示する一連のプログラミング例を提示する。これにより、意味論に関するいくつかの問題が生じるが、第3節でラムダ計算を用いてそれらを明確にしようとする。第4節では、ラムダ計算に基づく言語のインタプリタの実装者が直面する問題について、一般的な議論を行う。
