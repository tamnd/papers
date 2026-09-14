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
section: "1"
section_title: はじめに
tag: 00C1
kind: section
lang: ja
source: arxiv:1406.2661
pdf_sha256: ff5819e3a7b713c3bd3107b7de3d51fe0a347aa5d8444f0efdcf2345ef0a8b63
pdf_pages: 1-2
extraction: vision
extraction_model: gpt-6-astra
content_sha256: ac10dbe7345dfc788c1bf4bc3c831bcff7982f445204e3b2bc8127102b60cbdb
translated_from: content/en/goodfellow-2014-gan/01_introduction.md
source_content_sha256: 8cff2016cc5d3b4dd011b7208fdc0d32f9d8fa354a6c940d4eeb6be58318d257
translation_model: gpt-5
translation_run: 20260914T054537Z
glossary_version: 5
glossary_terms_sha256: 58c68d890f07ae3e920d6d07238da8d409da407f972fdd92b14f9e3f1e0382a4
prompt_sha256: a85b86fd402f05bc73ad3f4ad24540e4def82d38e0f105fa05c1de90e9436390
roundtrip: differs-in-wording
roundtrip_run: 20260914T070941Z
---

深層学習の有望性は、自然画像、音声を含む音響波形、自然言語コーパス中の記号といった人工知能アプリケーションで遭遇する種類のデータ上の確率分布を表現する、豊かで階層的なモデル[2]を発見することにある。これまでのところ、深層学習における最も顕著な成功は識別モデルに関するものであり、通常は高次元で豊かな感覚入力をクラスラベルへ写像するものである[14], [[krizhevsky-2012-imagenet]]。これらの顕著な成功は主として、特に扱いやすい勾配を持つ区分線形ユニット[19, 9, 10]を用いた、誤差逆伝播法とドロップアウトのアルゴリズムに基づいている。深い*生成*モデルは、最尤推定および関連する戦略において生じる多くの扱い困難な確率的計算を近似することの難しさ、および生成の文脈で区分線形ユニットの利点を活用することの難しさのために、より小さな影響しか与えてこなかった。本稿では、これらの困難を回避する新しい生成モデル推定手続きを提案する。[^4]

提案する*adversarial nets*フレームワークでは、生成モデルは敵対者と対峙する。すなわち、あるサンプルがモデル分布から来たものかデータ分布から来たものかを判定することを学習する識別モデルである。生成モデルは、偽造通貨を作り、それを発見されずに使用しようとする偽造犯の集団に類似していると考えることができる。一方、識別モデルは、その偽造通貨を検出しようとする警察に類似している。このゲームにおける競争は、偽造品が本物と区別できなくなるまで、両陣営がその手法を改善することを促す。

[^1]: Jean Pouget-AbadieはEcole PolytechniqueからUniversité de Montréalに滞在中である。
[^2]: Sherjil OzairはIndian Institute of Technology DelhiからUniversité de Montréalに滞在中である。
[^3]: Yoshua BengioはCIFAR Senior Fellowである。
[^4]: すべてのコードおよびハイパーパラメータはhttp://www.github.com/goodfeli/adversarialで利用可能である。

このフレームワークは、多くの種類のモデルおよび最適化アルゴリズムに対して具体的な学習アルゴリズムを与えることができる。本稿では、生成モデルがランダムノイズを多層パーセプトロンに通すことでサンプルを生成し、識別モデルもまた多層パーセプトロンであるという特殊な場合を検討する。この特殊な場合を*adversarial nets*と呼ぶ。この場合、非常に成功を収めている誤差逆伝播法およびドロップアウトのアルゴリズム[17]のみを用いて両方のモデルを学習でき、生成モデルからのサンプリングも順伝播のみを用いて行うことができる。近似推論やマルコフ連鎖は不要である。
