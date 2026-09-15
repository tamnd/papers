---
paper: amdahl-1967-law
title: Validity of the Single Processor Approach to Achieving Large Scale Computing Capabilities
authors:
  - Gene M. Amdahl
year: 1967
venue: AFIPS Spring Joint Computer Conference
field: architecture
section_title: Front Matter
tag: "0003"
kind: front
lang: ja
source: https://www3.cs.stonybrook.edu/~rezaul/Spring-2012/CSE613/reading/Amdahl-1967.pdf
pdf_sha256: 81a363deb884ca23e495280eb9229df1064b4b3f79d662f270be35b50bea5318
pdf_pages: "1"
extraction: native
extraction_model: pdftotext version 26.09.0
content_sha256: 2082fe921e422c410761c29b2afedad56a0eebbc6b9cdb8348c3be60012788ca
translated_from: content/en/amdahl-1967-law/00_front.md
source_content_sha256: 171773ab6985277014edc3cd9c8194b6f319c68c97b5f19c7035fd7df73aebc8
translation_model: gpt-5
translation_run: 20260915T021455Z
glossary_version: 6
glossary_terms_sha256: d6a44d6b0bbfd9cf9eaea95e1ac210d23c97ce7b6624d89dfa9ab8e54555b149
prompt_sha256: 28abc9ae7c2a46d63213afc528700760d76ff5866e775238c90c95b3052a886f
---

単一プロセッサアプローチによる

大規模計算能力の達成の妥当性

AFIPS Conference Proceedings, Vol. 30（Atlantic City, N.J., Apr. 18–20）より再掲載、AFIPS Press, Reston, Va., 1967年, pp. 483–485。Amdahl博士がInternational

Business Machines Corporation, Sunnyvale, Californiaに在籍していた時のものである。

Dr. Gene M. Amdahl

この記事は、後にアムダールの法則として知られるようになったものについてGene Amdahlが発表した最初の出版物である。興味深いことに、これは方程式を含まず、単一の図のみを含んでいる。SSCS Newsのこの号のために、Amdahl博士は図の描き直しに同意した。利用可能なハードコピーでは、それは判読不能であった。我々は、会員が約40年前の原典を読むことができるように、この歴史的な論文を掲載する。

編集者

10年以上にわたり、予言者たちは、単一コンピューターの構成が限界に達しており、真に重要な進歩は、協調的な解決を可能にするような方法で多数のコンピューターを相互接続することによってのみ達成できる、という主張を表明してきた。適切な方向性としては、メモリの一般化された相互接続を備えた汎用コンピューター、または幾何学的に関連付けられたメモリ相互接続を備え、1つ以上の命令ストリームによって制御される専用コンピューターが、それぞれ指摘されてきた。

単一プロセッサアプローチが引き続き妥当であること、および複数プロセッサアプローチが現実の問題とそれらに伴う不規則性に適用される場合の弱点が示される。
