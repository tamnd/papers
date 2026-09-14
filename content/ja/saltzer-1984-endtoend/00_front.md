---
paper: saltzer-1984-endtoend
title: End-To-End Arguments in System Design
authors:
  - J. H. Saltzer
  - D. P. Reed
  - D. D. Clark
year: 1984
venue: ACM TOCS
field: systems
section_title: Front Matter
tag: "0050"
kind: front
lang: ja
source: https://doi.org/10.1145/357401.357402
pdf_sha256: 3204a1a562d9d3b72ba112f20caddfd34991d6e1e39939ace6a3e7c016519768
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 409d1405e8e7f983ec4075733e862d72794e6e93987a9b449858c3021b0b4956
translated_from: content/en/saltzer-1984-endtoend/00_front.md
source_content_sha256: 5a38e3114bff08798d2d0cbd283c3deca3d00dd9fa9557b5948408e65f0e55e9
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: 9c1d74873f0850941dca2606ce296d509b8f605b085ea9e17a26ed91e2333e11
prompt_sha256: 28abc9ae7c2a46d63213afc528700760d76ff5866e775238c90c95b3052a886f
---

システム設計におけるエンドツーエンド引数

J.H. Saltzer, D.P. Reed and D.D. Clark*

M.I.T. Laboratory for Computer Science

本論文は、分散システムのモジュール間における関数の配置を導くのに役立つ設計原理を提示する。この原理はエンドツーエンド引数と呼ばれ、システムの低レベルに配置された関数は、その低レベルでそれらを提供するコストと比較すると、冗長であるか、ほとんど価値がない可能性があることを示唆する。本論文で議論する例には、ビットエラー回復、暗号化を用いたセキュリティ、重複メッセージ抑制、システムクラッシュからの回復、および配送確認が含まれる。これらの機能をサポートする低レベルのメカニズムは、性能向上としてのみ正当化される。
