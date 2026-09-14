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
content_sha256: 59e9bd126805aa7cfea88a6cfef098bcc7015c959c92e9f6fd910a6661d00eab
translated_from: content/en/goodfellow-2014-gan/00_front.md
source_content_sha256: c265cba67355836c7114c3970907c02f98e48871dec6b14aad433176ef193cb2
translation_model: gpt-5
translation_run: 20260914T054537Z
glossary_version: 5
glossary_terms_sha256: 58c68d890f07ae3e920d6d07238da8d409da407f972fdd92b14f9e3f1e0382a4
prompt_sha256: a85b86fd402f05bc73ad3f4ad24540e4def82d38e0f105fa05c1de90e9436390
---

敵対的生成ネットワーク

**Ian J. Goodfellow, Jean Pouget-Abadie[^1], Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair[^2], Aaron Courville, Yoshua Bengio[^3]**

Département d’informatique et de recherche opérationnelle  
Université de Montréal  
Montréal, QC H3C 3J7

arXiv:1406.2661v1 [stat.ML] 10 Jun 2014

要約

本論文では、敵対的過程を通じて生成モデルを推定するための新しいフレームワークを提案する。このフレームワークでは、二つのモデルを同時に学習する。すなわち、データ分布を捉える生成モデル$G$と、サンプルが$G$ではなく学習データから来た確率を推定する識別モデル$D$である。$G$の学習手続きは、$D$が誤りを犯す確率を最大化することである。このフレームワークはミニマックス二人ゲームに対応する。任意の関数$G$および$D$の空間において、一意な解が存在し、そのとき$G$は学習データ分布を復元し、$D$はあらゆる点で$\frac{1}{2}$に等しい。$G$および$D$が多層パーセプトロンによって定義される場合、システム全体は誤差逆伝播法によって学習可能である。学習時にもサンプル生成時にも、マルコフ連鎖や展開された近似推論ネットワークは必要ない。実験により、生成されたサンプルの定性的および定量的評価を通じて、このフレームワークの可能性を示す。
