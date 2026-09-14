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
section: "6"
section_title: 利点と欠点
tag: 00CE
kind: section
lang: ja
source: arxiv:1406.2661
pdf_sha256: ff5819e3a7b713c3bd3107b7de3d51fe0a347aa5d8444f0efdcf2345ef0a8b63
pdf_pages: "7"
extraction: vision
extraction_model: gpt-6-astra
content_sha256: 3fc878f2dec6b08c7c01e22096957d565aa89249b1e49ec3740ceb6209f3a217
translated_from: content/en/goodfellow-2014-gan/06_advantages_and_disadvantages.md
source_content_sha256: 38ce85b3fe3c89d51c7062535a10ebc800c4286b1991da131096aa15c4f7b192
translation_model: gpt-5
translation_run: 20260914T054537Z
glossary_version: 5
glossary_terms_sha256: 58c68d890f07ae3e920d6d07238da8d409da407f972fdd92b14f9e3f1e0382a4
prompt_sha256: a85b86fd402f05bc73ad3f4ad24540e4def82d38e0f105fa05c1de90e9436390
roundtrip: differs-in-wording
roundtrip_run: 20260914T070941Z
---

この新しいフレームワークには、従来のモデリングフレームワークと比較して利点と欠点がある。欠点は主として、$p_g(x)$の明示的な表現が存在しないこと、そして学習中に$D$が$G$とうまく同期されなければならないことである（特に、$p_{\text{data}}$をモデル化するのに十分な多様性を持たせるために、$G$が$\mathbf{z}$のあまりにも多くの値を同じ$\mathbf{x}$の値へと崩壊させてしまう「Helveticaシナリオ」を避けるため、$D$を更新せずに$G$を過度に学習させてはならない）。これは、Boltzmannマシンの負のチェーンが学習ステップ間で常に最新に保たれなければならないのと同様である。利点は、Markovチェーンがまったく不要であり、勾配を得るためにはバックプロパゲーションのみが用いられ、学習中に推論 (inference) が不要であり、さらに多種多様な関数をモデルに組み込めることである。表 2は、生成的敵対ネットワークと他の生成モデリング手法との比較を要約している。

前述の利点は主として計算上のものである。敵対的モデルはまた、生成器ネットワークがデータ例によって直接更新されるのではなく、識別器を通って流れる勾配によってのみ更新されることから、何らかの統計的利点も得られる可能性がある。これは、入力の構成要素が生成器のパラメータへ直接コピーされないことを意味する。敵対的ネットワークのもう一つの利点は、非常に鋭い、さらには退化した分布さえ表現できることである。一方、Markovチェーンに基づく手法では、チェーンがモード間を混合できるようにするため、分布がある程度ぼやけている必要がある。
