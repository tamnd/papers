---
paper: backus-1978-vonneumann
title: Can Programming Be Liberated from the von Neumann Style? A Functional Style and Its Algebra of Programs
authors:
  - John Backus
year: 1978
venue: Communications of the ACM (Turing Award lecture)
field: languages
section_title: Front Matter
tag: "0049"
kind: front
lang: ja
source: https://www.cs.cmu.edu/~crary/819-f09/Backus78.pdf
pdf_sha256: 2e412a7986c7fd1bdd060d90d035faa9ecc8a29675f99206c243da90954ca423
pdf_pages: 1-2
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 036e411aa3c6e6f9c4bc6e5940fd580bab68ca6df1b7ee4ec0da8cfe08829e07
translated_from: content/en/backus-1978-vonneumann/00_front.md
source_content_sha256: 752feced1622b510f0705492c1cbfb9e3b6bd628b154c0b11f2d80acdd041ccc
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: 07dd8f2ee4792b6dc2b4d5c388a078378107a558371bfe6613a7ad1bb7578218
prompt_sha256: 28abc9ae7c2a46d63213afc528700760d76ff5866e775238c90c95b3052a886f
---

フォン・ノイマン・スタイルからプログラミングを解放できるか？ 関数型スタイルとそのプログラム代数

John Backus

IBM Research Laboratory, San Jose

従来のプログラミング言語はますます巨大になっているが、より強力にはなっていない。最も基本的なレベルに内在する欠陥によって、それらは肥大化すると同時に弱体化している。その欠陥とは、共通の祖先であるフォン・ノイマン・コンピューターから受け継いだ、単語を一つずつ処理する原始的なプログラミング・スタイル、意味論と状態遷移との密接な結合、プログラミングを式の世界と文の世界に分割すること、既存のプログラムから新しいプログラムを構築するための強力な結合形式を効果的に利用できないこと、そしてプログラムについて推論するために有用な数学的性質を欠いていることである。

これに代わる関数型のプログラミング・スタイルは、プログラムを作成するための結合形式の利用を基盤とする。関数型プログラムは構造化データを扱い、多くの場合、反復的でも再帰的でもなく、階層的に構成され、引数に名前を付けず、手続き宣言の複雑な機構を必要とせずに一般的に適用可能となる。結合形式は高水準のプログラムを用いて、従来の言語では不可能なスタイルで、さらに高水準のプログラムを構築できる。

関数型のプログラミング・スタイルには、変数がプログラムの範囲を取り、演算が結合形式であるプログラムの代数が伴う。この代数は、プログラムを変形したり、「未知数」がプログラムである方程式を、高校の代数で方程式を変形するのとほぼ同じ方法で解いたりするために使用できる。
