---
paper: dean-2004-mapreduce
title: 'MapReduce: Simplified Data Processing on Large Clusters'
authors:
  - Jeffrey Dean
  - Sanjay Ghemawat
year: 2004
venue: OSDI
field: systems
section: "2"
section_title: プログラミングモデル
kind: section
lang: ja
source: https://www.usenix.org/legacy/events/osdi04/tech/full_papers/dean/dean.pdf
pdf_sha256: 9cfef3ef1b8fe1a1b66c7221f56c2eeca0b15d6608ea68b0c85a38bfbffd8ce5
pdf_pages: 2-3
extraction: vision
extraction_model: gpt-5
content_sha256: a253efef94522bf7d6f141d664d21fdef97905846f4fa96fa49e04b905e797be
translated_from: content/en/dean-2004-mapreduce/02_programming_model.md
source_content_sha256: aaf581737cd4d87ef514b916c1ce15d8ee969caef455403515366f71228c9af2
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: 9c1d74873f0850941dca2606ce296d509b8f605b085ea9e17a26ed91e2333e11
prompt_sha256: 28abc9ae7c2a46d63213afc528700760d76ff5866e775238c90c95b3052a886f
---

計算は入力キー/値ペアの集合を受け取り、出力キー/値ペアの集合を生成する。MapReduceライブラリのユーザーは、計算を2つの関数: MapとReduceとして表現する。

ユーザーによって記述されるMapは、入力ペアを受け取り、中間キー/値ペアの集合を生成する。MapReduceライブラリは、同じ中間キー $I$ に関連付けられたすべての中間値をグループ化し、それらをReduce関数に渡す。

ユーザーによって記述されるReduce関数も、中間キー $I$ とそのキーに対する値の集合を受け取る。これらの値を統合して、場合によってはより小さい値の集合を形成する。通常、1回のReduce呼び出しごとに生成される出力値は0個または1個だけである。中間値はイテレータを介してユーザーのreduce関数に供給される。これにより、メモリに収まらないほど大きな値のリストを扱うことが可能になる。

### 2.1 例

大規模な文書コレクション内の各単語の出現回数を数える問題を考える。ユーザーは次の擬似コードに類似したコードを記述する。

```text
map(String key, String value):
    // key: document name
    // value: document contents
    for each word w in value:
        EmitIntermediate(w, "1");

reduce(String key, Iterator values):
    // key: a word
    // values: a list of counts
    int result = 0;
    for each v in values:
        result += ParseInt(v);
    Emit(AsString(result));
```

map関数は、各単語と関連する出現回数（この単純な例では単に‘1’）を出力する。reduce関数は、特定の単語について出力されたすべてのカウントを合計する。

さらに、ユーザーは入力ファイルと出力ファイルの名前、およびオプションのチューニングパラメータをmapreduce仕様オブジェクトに格納するコードを記述する。その後、ユーザーは仕様オブジェクトを渡してMapReduce関数を呼び出す。ユーザーのコードはMapReduceライブラリ（C++で実装されている）とリンクされる。付録Aには、この例の完全なプログラムテキストが含まれている。

### 2.2 型

前述の擬似コードは文字列の入力と出力という観点で記述されているが、概念的にはユーザーが提供するmapおよびreduce関数には対応する型が存在する。

```text
map     (k1,v1)          → list(k2,v2)
reduce  (k2,list(v2))    → list(v2)
```

すなわち、入力キーと値は出力キーと値とは異なるドメインから取り出される。さらに、中間キーと値は出力キーと値と同じドメインに属する。

我々のC++実装はユーザー定義関数との間で文字列を渡し、適切な型への文字列間の変換はユーザーコードに任せている。

### 2.3 その他の例

ここでは、MapReduce計算として容易に表現できる興味深いプログラムのいくつかの単純な例を示す。

Distributed Grep: map関数は、与えられたパターンに一致する場合に行を出力する。reduce関数は、与えられた中間データを単に出力へコピーする恒等関数である。

Count of URL Access Frequency: map関数はWebページ要求のログを処理し、$\langle URL,1\rangle$を出力する。reduce関数は、同じURLに対するすべての値を加算し、$\langle URL,total\ count\rangle$ペアを出力する。

Reverse Web-Link Graph: map関数は、sourceという名前のページ内で見つかったtarget URLへの各リンクについて、$\langle target,source\rangle$ペアを出力する。reduce関数は、与えられたtarget URLに関連付けられたすべてのsource URLのリストを連結し、ペア: $\langle target,list(source)\rangle$を出力する。

Term-Vector per Host: 用語ベクトルは、文書または文書集合内に出現する最も重要な単語を、$\langle word,frequency\rangle$ペアのリストとして要約する。map関数は、各入力文書について$\langle hostname,term\ vector\rangle$ペアを出力する（ここでhostnameは文書のURLから抽出される）。reduce関数には、あるホストについての文書ごとのすべての用語ベクトルが渡される。これらの用語ベクトルを加算し、頻度の低い用語を破棄した後、最終的な$\langle hostname,term\ vector\rangle$ペアを出力する。

図 1: 実行概要

Inverted Index: map関数は各文書を解析し、$\langle word, document\ ID\rangle$ペアのシーケンスを出力する。reduce関数は、ある単語に対するすべてのペアを受け取り、対応する文書IDをソートして、$\langle word, list(document\ ID)\rangle$ペアを出力する。すべての出力ペアの集合は単純な転置インデックスを形成する。この計算を拡張して単語の位置を追跡することは容易である。

Distributed Sort: map関数は各レコードからキーを抽出し、$\langle key, record\rangle$ペアを出力する。reduce関数はすべてのペアを変更せずに出力する。この計算は、Section 4.1で説明されているパーティション分割機能と、Section 4.2で説明されている順序付けの性質に依存する。
