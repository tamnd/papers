---
paper: denning-1968-workingset
title: The Working Set Model for Program Behavior
authors:
  - Peter J. Denning
year: 1968
venue: Communications of the ACM
field: systems
section_title: Front Matter
tag: 004E
kind: front
lang: ja
source: https://doi.org/10.1145/800001.811670
pdf_sha256: 3585991156b07c7e878ea9dff16ef7721401adff09ee328f5ee247b016289e0f
pdf_pages: 1-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: de71a90f5e20b3336bc1681ff520159bdf44857b0eeca161e090c06228cd5131
translated_from: content/en/denning-1968-workingset/00_front.md
source_content_sha256: 1a0f412b8f796cd2bda77a1d352f7e118a00f27155e048d18edd6ba0345da370
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: 9c1d74873f0850941dca2606ce296d509b8f605b085ea9e17a26ed91e2333e11
prompt_sha256: 28abc9ae7c2a46d63213afc528700760d76ff5866e775238c90c95b3052a886f
---

プログラムの振舞いに関するワーキングセットモデル

Peter J. Denning

マサチューセッツ工科大学、マサチューセッツ州ケンブリッジ

現代のコンピューターシステムにおいてリソース割当てに関する一般的な取り扱いが存在しない最も基本的な理由は、おそらくプログラムの振舞いに関する適切なモデルがないことである。本論文では、新しいモデルである「ワーキングセットモデル」を展開する。プロセスに関連付けられたページのワーキングセットは、最近使用されたページの集合として定義され、ページングメモリの動的管理に不可欠な知識を提供する。「プロセス」と「ワーキングセット」は、同一の継続的な計算活動の現れであることを示す。次に「プロセッサ要求」と「メモリ要求」を定義し、リソース割当てを、利用可能な装置に対して要求を均衡させる問題として定式化する。

キーワードおよび句：一般的なオペレーティングシステム概念、マルチプロセッシング、マルチプログラミング、オペレーティングシステム、プログラムの振舞い、プログラムモデル、リソース割当て、スケジューリング、記憶域割当て

CR分類：4.30、4.32

1. はじめに

リソース割当ては難しい問題である。近年、プロセススケジューリングと主メモリ管理について多くの議論がなされているが、技術の開発はこれら二つの方向に沿って独立に進められてきた。統一的なアプローチが必要であることは誰も否定しないであろう。ここでは、統一的なアプローチを開発することが可能であることを示す。すべての実行中のプログラムが、特にプロセッサとメモリを含むすべてのシステムリソースに対して同時に要求を生じさせるという観察から出発し、最終的に「システム要求」を定義する。割当て問題は、利用可能なリソースに対して要求を均衡させることから成る。
