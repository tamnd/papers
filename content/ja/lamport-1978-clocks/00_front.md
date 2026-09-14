---
paper: lamport-1978-clocks
title: Time, Clocks, and the Ordering of Events in a Distributed System
authors:
  - Leslie Lamport
year: 1978
venue: Communications of the ACM
field: systems
section_title: Front Matter
tag: 004F
kind: front
lang: ja
source: https://lamport.azurewebsites.net/pubs/time-clocks.pdf
pdf_sha256: c55e7cab4230aa3d7126748a149b2db6f0d7a67296d5eccfdd50a210299a96b2
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 424237971e1c9ee21eddc889af18e3165a1056a1feb208d62969fe33dd668207
translated_from: content/en/lamport-1978-clocks/00_front.md
source_content_sha256: 4b7ae7f50483519411ec5d2ce1d6efe1cc22702f57cad988b4035630cf300048
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: 9c1d74873f0850941dca2606ce296d509b8f605b085ea9e17a26ed91e2333e11
prompt_sha256: 28abc9ae7c2a46d63213afc528700760d76ff5866e775238c90c95b3052a886f
---

分散システムにおける事象の時間、時計、および順序付け

Leslie Lamport
Massachusetts Computer Associates, Inc.

分散システムにおいて、ある事象が別の事象より前に発生するという概念を検討し、それが事象の半順序を定義することを示す。事象を全順序付けするために使用できる論理時計のシステムを同期させるための分散アルゴリズムを示す。全順序の利用を、同期問題を解決する方法によって例示する。次に、このアルゴリズムを物理時計の同期用に特殊化し、時計がどの程度まで同期から外れ得るかについて上界を導出する。

キーワードとフレーズ：分散システム、コンピュータネットワーク、時計同期、マルチプロセスシステム

CR分類：4.32, 5.29
