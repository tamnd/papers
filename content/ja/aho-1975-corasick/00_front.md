---
paper: aho-1975-corasick
title: 'Efficient String Matching: An Aid to Bibliographic Search'
authors:
  - Alfred V. Aho
  - Margaret J. Corasick
year: 1975
venue: Communications of the ACM
field: algorithms
section_title: Front Matter
tag: "0043"
kind: front
lang: ja
source: https://cr.yp.to/bib/1975/aho.pdf
pdf_sha256: f04940c07d2a12726bce4147fd4217e876cd969ddf44094ad90c866893deed34
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 0ad4871383d1d32ef91e675050f477bbf6b424e50bd14a718585c64c3292b10e
translated_from: content/en/aho-1975-corasick/00_front.md
source_content_sha256: 17d1d9c934a9c79dc1bf9969b26b2fdc40d089cc0cda4e05dff84776e249e10e
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: 81be60ea3284bdc3129ecda2524a99e799d0b3ec06fd0a74a1fb3922eda78382
prompt_sha256: 28abc9ae7c2a46d63213afc528700760d76ff5866e775238c90c95b3052a886f
---

効率的な文字列照合：書誌検索への一助

Alfred V. Aho and Margaret J. Corasick
Bell Laboratories

本論文では、テキストの文字列中から、有限個のキーワードのいずれについてもそのすべての出現箇所を特定する、単純かつ効率的なアルゴリズムについて述べる。このアルゴリズムは、キーワードから有限状態のパターン照合機械を構成し、その後、パターン照合機械を用いてテキストの文字列を一回の走査で処理するものである。パターン照合機械の構成に要する時間は、キーワードの長さの総和に比例する。テキストの文字列を処理する際にパターン照合機械が行う状態遷移の数は、キーワードの数に依存しない。このアルゴリズムは、図書館の書誌検索プログラムの速度を5倍から10倍向上させるために使用されている。

キーワードと句：キーワードと句、文字列パターン照合、書誌検索、情報検索、テキスト編集、有限状態機械、計算量。

CR分類：3.74, 3.71, 5.22, 5.25
