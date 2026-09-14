---
paper: wegman-1991-sccp
title: Constant Propagation with Conditional Branches
authors:
  - Mark N. Wegman
  - F. Kenneth Zadeck
year: 1991
venue: ACM TOPLAS
field: languages
section_title: Front Matter
tag: 004C
kind: front
lang: ja
source: https://www.cs.utexas.edu/users/lin/cs380c/wegman.pdf
pdf_sha256: 40929436cdf1c477f2318221df5d0aa71488db4a01cc448b184e0aba8bf95ddb
pdf_pages: "2"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: b2a45f7d003ed4e91e2043efdc412a285fdcf3f353555859eca27d5ee4d36d3a
translated_from: content/en/wegman-1991-sccp/00_front.md
source_content_sha256: 94ce5b5dba477ad2c0e4754f4c994d52f8979f20334977030a8748c85db9197d
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: 07dd8f2ee4792b6dc2b4d5c388a078378107a558371bfe6613a7ad1bb7578218
prompt_sha256: 28abc9ae7c2a46d63213afc528700760d76ff5866e775238c90c95b3052a886f
---

定数伝播問題は一般には決定不能であることを容易に示すことができる（例えば Kam と Ullman [25] を参照）が、この問題の妥当なインスタンスの多くは決定可能であり、計算効率のよいアルゴリズムが存在する。本論文では、そのような4つのアルゴリズムを提示する。ここで提示する各アルゴリズムは、すべての定数が発見されるとは限らないという意味で保守的であるが、発見された各定数はプログラムのすべての可能な実行にわたって定数である。

いくつかの予備事項の後、アルゴリズムは能力が増加する順にSection 3で提示される。後続する各アルゴリズムは、少なくとも直前のアルゴリズムで発見された定数を発見する。最初の3つのアルゴリズムは他者の研究の再定式化であり、4つ目は新規で、先行する3つのそれぞれの最良の特徴を含んでいる。これらのアルゴリズムは、既知のグローバル定数伝播アルゴリズムの中でも最も単純で高速かつ強力なものの一つである。Section 4では、本アルゴリズムが正しく、かつ多項式時間の上界を持つ従来の最良のアルゴリズムと少なくとも同等の能力を持つことが証明される。Section 5では、一般的な実装上の問題について議論する。

Section 6では、単一の手続きよりも広い領域にわたって定数伝播を実行するためのいくつかの技法を検討する。Section 6.2では、定数伝播と手続き統合の関係について議論する。Section 6.3では、定数伝播と併せてエイリアシング情報を収集する、インタープロシージャ間データフロー解析の一形態を実行する新しいアルゴリズムを示す。

Section 7ではいくつかの未解決問題を概説し、Section 8では本論文を結論する。

### 1. {#wegman-1991-sccp-s-1 .section tag=012F}
