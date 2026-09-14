---
paper: mccarthy-1960-lisp
title: Recursive Functions of Symbolic Expressions and Their Computation by Machine, Part I
authors:
  - John McCarthy
year: 1960
venue: Communications of the ACM
field: languages
section_title: Front Matter
tag: "0001"
kind: front
lang: ja
source: http://www-formal.stanford.edu/jmc/recursive.pdf
pdf_sha256: 3d981849e59505eff3f14397a177b409f5d978d43d114bdd67c956e74320fc92
pdf_pages: 1-3
extraction: native
extraction_model: pdftotext version 26.09.0
content_sha256: 5a4dfccb1512a079a2b119f15eaf2588d410e30d156a3c06ecffd15f319e2e8f
translated_from: content/en/mccarthy-1960-lisp/00_front.md
source_content_sha256: 99ca45842e94baac0c4a8a87f87f893ac11b3ca331c2904346168b690e50dcd7
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: 07dd8f2ee4792b6dc2b4d5c388a078378107a558371bfe6613a7ad1bb7578218
prompt_sha256: 28abc9ae7c2a46d63213afc528700760d76ff5866e775238c90c95b3052a886f
---

記号式の再帰関数

およびその機械による計算 第I部

John McCarthy, Massachusetts Institute of Technology, Cambridge, Mass. ∗

1960年4月

1 序論

LISP（LISt Processor）と呼ばれるプログラミングシステムが、M.I.T.の人工知能グループによってIBM 704コンピューター用に開発された。このシステムは、Advice Takerと呼ばれる構想中のシステムに関する実験を容易にするために設計されたものである。Advice Takerでは、機械に宣言文だけでなく命令文も扱うよう指示でき、命令を実行する際に「常識」を発揮させることができる。Advice Takerの最初の提案 [1] は1958年11月になされた。主な要件は、形式化された宣言文および命令文を表す式を操作するためのプログラミングシステムであり、それによってAdvice Takerシステムが推論を行えるようにすることであった。

開発の過程で、LISPシステムはいくつかの簡略化の段階を経て、最終的には、あるクラスの記号式の部分再帰関数を表現するための方式に基づくものとなった。この表現はIBM 704コンピューターにも、その他のいかなる電子計算機にも依存しないものであり、現在では、S式と呼ばれる式のクラスおよびS関数と呼ばれる関数から始めてこのシステムを説明するのが適切であると思われる。

∗ Putting this paper in L A supported by ARPA (ONR) grant N00014-94-1-0775

TEXpartly 1962年以来John McCarthyが在籍しているStanford Universityへ。この論文は、若干の記法上の変更を加えてCACM, April 1960から複写したものである。正確な組版を確認したい場合は、そちらを参照されたい。
