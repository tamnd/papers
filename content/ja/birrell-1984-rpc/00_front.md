---
paper: birrell-1984-rpc
title: Implementing Remote Procedure Calls
authors:
  - Andrew D. Birrell
  - Bruce Jay Nelson
year: 1984
venue: ACM TOCS
field: systems
section_title: Front Matter
tag: "0051"
kind: front
lang: ja
source: https://www.cs.cmu.edu/~dga/15-712/F07/papers/birrell842.pdf
pdf_sha256: 0c5058383786e2b3e8fa9894872358e362a6f6ffc58c06f29dc08b836318f432
pdf_pages: 2-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: f6d583067c0c67fee19091ac78b662337d7203858d74d10e8567b370a9052136
translated_from: content/en/birrell-1984-rpc/00_front.md
source_content_sha256: 443c55fbdd07742a112658c60d65e70a2b25966b03a3fec4d237d8c751d86d25
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: 9c1d74873f0850941dca2606ce296d509b8f605b085ea9e17a26ed91e2333e11
prompt_sha256: 28abc9ae7c2a46d63213afc528700760d76ff5866e775238c90c95b3052a886f
---

（その環境の並行性の詳細およびRPC実装に依存して）依然として実行される。

この考えには多くの魅力的な側面がある。その一つは、明確で単純な意味論である。これにより、分散計算を構築し、正しく動作させることが容易になるはずである。もう一つは効率である。手続き呼び出しは、通信を非常に高速に行えるほど単純であると思われる。第三は一般性である。単一マシン上の計算では、手続きはしばしばアルゴリズムの各部分間の通信における最も重要な機構である。

RPCという考えは長年にわたって存在している。少なくとも1976年まで遡る以前から、公開文献で何度も議論されてきた [15]。Nelsonの博士論文 [13] は、RPCシステムの設計上の可能性を広範に検討したものであり、RPCに関する以前の研究の多くへの参照を含んでいる。しかし、RPCの本格的な実装は、論文上の設計ほど多くはなかった。注目すべき最近の取り組みとしては、Xerox NSのプロトコルファミリー [4] におけるCourier、およびMITで現在進行中の研究 [10] がある。

この論文は、CedarプロジェクトのためのRPC機能の構築から生じたものである。以前の研究（特にNelsonの論文とそれに関連する実験）に基づき、RPC機能の設計者が行わなければならない選択について理解していると考えていた。我々の課題は、我々固有の目的と環境を考慮してその選択を行うことであった。実際には、いくつかの領域について理解が不十分であることが分かり、設計にいくつかの新規な側面を持つシステムを作成した。
