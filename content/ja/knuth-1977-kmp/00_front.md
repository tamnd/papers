---
paper: knuth-1977-kmp
title: Fast Pattern Matching in Strings
authors:
  - Donald E. Knuth
  - James H. Morris Jr.
  - Vaughan R. Pratt
year: 1977
venue: SIAM Journal on Computing
field: algorithms
section_title: Front Matter
tag: "0044"
kind: front
lang: ja
source: https://www.cs.jhu.edu/~misha/ReadingSeminar/Papers/Knuth77.pdf
pdf_sha256: cf3391d85e2456f8242a3dc4a88e7cdead9a419b52890bb4b8a31433e9659dcb
pdf_pages: 1-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 081c6026e3c0bf65634bf7689e350483e61136bf48173c6579873c56ee235b01
translated_from: content/en/knuth-1977-kmp/00_front.md
source_content_sha256: 60ce63ba3d84477d570209bf28278eaed833668a8bc0ad505f60de5046d621c3
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: 81be60ea3284bdc3129ecda2524a99e799d0b3ec06fd0a74a1fb3922eda78382
prompt_sha256: 28abc9ae7c2a46d63213afc528700760d76ff5866e775238c90c95b3052a886f
---

高速文字列パターン照合*

DONALD E. KNUTH†, JAMES H. MORRIS, JR.‡ AND VAUGHAN R. PRATT¶

要約。ある文字列内に別の与えられた文字列が出現するすべての位置を、その文字列の長さの和に比例する実行時間で発見するアルゴリズムを提示する。比例定数は、このアルゴリズムを実用に供するのに十分小さく、またこの手続きは、より一般的ないくつかのパターン照合問題を扱うよう拡張することもできる。このアルゴリズムの理論的応用により、偶数回文の連結の集合、すなわち言語$\{\alpha\alpha^R\}^*$が線形時間で認識可能であることを示す。平均的にはさらに高速に実行される他のアルゴリズムについても考察する。

キーワード。パターン、文字列、テキスト編集、パターン照合、トライメモリ、探索、文字列の周期、回文、最適アルゴリズム、フィボナッチ文字列、正規表現

テキスト編集プログラムでは、与えられた「パターン」文字列の出現を探すために、しばしば文字列を検索する必要がある。我々は、パターンがテキストの連続した部分文字列として現れるすべての位置、あるいは左端の位置だけを発見したい。例えば、$c a t e n a r y$はパターン$t e n$を含むが、$c a n a r y$を部分文字列とはみなさない。

一致するパターンを探索する明白な方法は、テキストの各開始位置で探索を試み、誤った文字が見つかった時点で探索を打ち切ることである。
