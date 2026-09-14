---
paper: cooley-1965-fft
title: An Algorithm for the Machine Calculation of Complex Fourier Series
authors:
  - James W. Cooley
  - John W. Tukey
year: 1965
venue: Mathematics of Computation
field: algorithms
section_title: Front Matter
tag: "0040"
kind: front
lang: ja
source: https://doi.org/10.1090/s0025-5718-1965-0178586-1
pdf_sha256: b4fa04410bcbf324eca035ab9d94818f075cee2f2ae38e99ebb0e2348e64654a
pdf_pages: 1-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: c38b1e10864015b14472ae75751dd9921b4059b0c42f91d62b25d73e91cca58b
translated_from: content/en/cooley-1965-fft/00_front.md
source_content_sha256: 75f827c0ac01a12a53f6f7d8ac49df10329caa98952de96c18f1d44bf14b5a54
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: 81be60ea3284bdc3129ecda2524a99e799d0b3ec06fd0a74a1fb3922eda78382
prompt_sha256: 28abc9ae7c2a46d63213afc528700760d76ff5866e775238c90c95b3052a886f
---

複素フーリエ級数の機械計算のためのアルゴリズム

James W. Cooley and John W. Tukey による

$2^m$要因実験の交互作用を計算する効率的な方法はYatesによって導入され、広く彼の名で知られている。$3^m$への一般化はBox et al. [1]によって与えられた。Good [2]はこれらの方法を一般化し、その応用の一分野としてフーリエ級数の計算に用いることのできる優れたアルゴリズムを与えた。Goodの方法はその最も一般的な形では、$N$-ベクトルに、$m$個の疎行列に因数分解できる$N \times N$行列を乗算しなければならないある種の問題に適用できる。ただし、$m$は$\log N$に比例する。この結果、$N^2$ではなく$N \log N$に比例する数の演算を必要とする手続きが得られる。ここではこれらの方法を複素フーリエ級数の計算に適用する。これはデータ点の数が非常に合成数である場合、またはそのように選択できる場合に有用である。ここではアルゴリズムをかなり異なる形で導出し、提示する。$N$の選択についても考察する。また、$N = 2^m$とした二進コンピューターを使用することで特別な利点が得られること、および与えられたフーリエ係数に用いる$N$個のデータ記憶場所からなる配列内だけで計算全体を実行できることを示す。

複素フーリエ級数を計算する問題を考える。
