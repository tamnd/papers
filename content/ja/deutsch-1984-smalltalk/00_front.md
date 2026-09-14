---
paper: deutsch-1984-smalltalk
title: Efficient Implementation of the Smalltalk-80 System
authors:
  - L. Peter Deutsch
  - Allan M. Schiffman
year: 1984
venue: POPL
field: languages
section_title: Front Matter
tag: 004A
kind: front
lang: ja
source: https://doi.org/10.1145/800017.800542
pdf_sha256: 300584e302ee0fa5a006ee363d9e3f1b0df043c3259580e32dcd409e9a09871d
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 44bfe7929e9aec2bdb837157d8b06c46a5ddcac56a214ec60a45371c291dd300
translated_from: content/en/deutsch-1984-smalltalk/00_front.md
source_content_sha256: 64032bbbb8fd182a69fb8ac6e35b65d90ee769ed62ed7b817d5f46f08accd2c1
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: 07dd8f2ee4792b6dc2b4d5c388a078378107a558371bfe6613a7ad1bb7578218
prompt_sha256: 28abc9ae7c2a46d63213afc528700760d76ff5866e775238c90c95b3052a886f
---

Smalltalk-80システムの効率的な実装

L. Peter Deutsch
Xerox PARC, Software Concepts Group

Allan M. Schiffman
Fairchild Laboratory for Artificial Intelligence Research

概要

Smalltalk-80*プログラミング言語は動的記憶域割り当て、完全な上向き funarg、および普遍的多相性を持つ手続きを含む。Smalltalk-80プログラミングシステムは、対話的実行、増分コンパイル、および実装の移植性を特徴とする。現代のプログラミングシステムにおけるこれらの機能は、それぞれ単独であっても効率的に実装することが最も困難なものの一つである。小規模なマイクロプロセッサベースのコンピューター上でホストされるSmalltalk-80システムの新しい実装は、既存の実装との完全な（オブジェクトコード）互換性を維持しながら、高い性能を達成している。本論文では、プロジェクトの過程で開発された最も重要な最適化技術について論じる。その多くは他の言語にも適用可能である。中心となる考え方は、特定のランタイム状態（コードとデータの両方）を複数の形式で表現し、必要に応じて形式間で変換することである。

*Smalltalk-80はXerox Corporationの商標である。
