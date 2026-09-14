---
paper: dean-2004-mapreduce
title: 'MapReduce: Simplified Data Processing on Large Clusters'
authors:
  - Jeffrey Dean
  - Sanjay Ghemawat
year: 2004
venue: OSDI
field: systems
section_title: Front Matter
kind: front
lang: ja
source: https://www.usenix.org/legacy/events/osdi04/tech/full_papers/dean/dean.pdf
pdf_sha256: 9cfef3ef1b8fe1a1b66c7221f56c2eeca0b15d6608ea68b0c85a38bfbffd8ce5
pdf_pages: "1"
extraction: vision
extraction_model: gpt-5
content_sha256: b3db0fd2bde3f9e4291ca8d7b45c7e89952d31bd070d2520c67f58c3ceae0a21
translated_from: content/en/dean-2004-mapreduce/00_front.md
source_content_sha256: 50e40e1d76bad207cd63412840af8cf2e0fc4432de8ad0628778084393f54a7f
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: 9c1d74873f0850941dca2606ce296d509b8f605b085ea9e17a26ed91e2333e11
prompt_sha256: 28abc9ae7c2a46d63213afc528700760d76ff5866e775238c90c95b3052a886f
---

**MapReduce: 大規模クラスターにおける簡素化されたデータ処理**

Jeffrey Dean and Sanjay Ghemawat jeff@google.com, sanjay@google.com

*Google, Inc.*

概要

MapReduceは、大規模なデータセットを処理および生成するためのプログラミングモデルと、それに対応する実装である。ユーザーは、キー/値ペアを処理して中間キー/値ペアの集合を生成する *map* 関数と、同じ中間キーに関連付けられたすべての中間値を統合する *reduce* 関数を指定する。このモデルでは、論文で示されているように、多くの実世界のタスクを表現可能である。

この関数型スタイルで記述されたプログラムは、大規模なコモディティマシンのクラスター上で自動的に並列化され、実行される。ランタイムシステムは、入力データのパーティション化、マシン集合にまたがるプログラムの実行のスケジューリング、マシン障害の処理、および必要なマシン間通信の管理の詳細を処理する。これにより、並列および分散システムの経験を持たないプログラマーでも、大規模な分散システムのリソースを容易に利用できる。

我々のMapReduceの実装は、大規模なコモディティマシンのクラスター上で動作し、高いスケーラビリティを持つ。典型的なMapReduce計算では、数千台のマシン上で多数のテラバイトのデータを処理する。プログラマーはこのシステムを容易に使用できると感じている。数百のMapReduceプログラムが実装され、毎日1000を超えるMapReduceジョブがGoogleのクラスター上で実行されている。
