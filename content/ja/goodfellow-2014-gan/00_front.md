---
paper: goodfellow-2014-gan
title: Generative Adversarial Nets
authors:
  - Ian J. Goodfellow
  - Jean Pouget-Abadie
  - Mehdi Mirza
  - Bing Xu
  - David Warde-Farley
  - Sherjil Ozair
  - Aaron Courville
  - Yoshua Bengio
year: 2014
venue: NIPS
field: ai-ml
section_title: Front Matter
tag: 00C0
kind: front
lang: ja
source: arxiv:1406.2661
pdf_sha256: ff5819e3a7b713c3bd3107b7de3d51fe0a347aa5d8444f0efdcf2345ef0a8b63
pdf_pages: "1"
extraction: vision
extraction_model: gpt-6-astra
content_sha256: 940ec590b4d28f0894e999788b9f4fc7b4b0cc2f126b7ef6c74772a4da4406ae
translated_from: content/en/goodfellow-2014-gan/00_front.md
source_content_sha256: c265cba67355836c7114c3970907c02f98e48871dec6b14aad433176ef193cb2
translation_model: gpt-5
translation_run: 20260914T092812Z
glossary_version: 6
glossary_terms_sha256: b54b51f3654b8fb3a38fdda707a4eab5eac703c3fbfea813e544de2709bff5b9
prompt_sha256: 28abc9ae7c2a46d63213afc528700760d76ff5866e775238c90c95b3052a886f
---

生成的敵対ネットワーク

Ian J. Goodfellow, Jean Pouget-Abadie[^1], Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair[^2], Aaron Courville, Yoshua Bengio[^3]

Département d’informatique et de recherche opérationnelle  
Université de Montréal  
Montréal, QC H3C 3J7

arXiv:1406.2661v1 [stat.ML] 10 Jun 2014

概要

敵対的プロセスを通じて生成モデルを推定するための新しいフレームワークを提案する。このプロセスでは、2つのモデルを同時に学習する。一方はデータ分布を捉える生成モデル$G$であり、もう一方は、あるサンプルが$G$ではなく学習データから得られたものである確率を推定する識別モデル$D$である。$G$の学習手続きは、$D$が誤りを犯す確率を最大化することである。このフレームワークは、ミニマックス2人ゲームに対応する。任意の関数$G$および$D$の空間において、$G$が学習データの分布を復元し、$D$があらゆる場所で$\frac12$に等しくなる一意の解が存在する。$G$および$D$が多層パーセプトロンによって定義される場合、システム全体をバックプロパゲーションによって学習できる。学習中にもサンプルの生成中にも、マルコフ連鎖や展開された近似推論ネットワークは必要ない。実験により、生成されたサンプルの定性的および定量的な評価を通じて、このフレームワークの可能性を示す。
