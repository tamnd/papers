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
section: "2"
section_title: 関連研究
tag: 00C2
kind: section
lang: ja
source: arxiv:1406.2661
pdf_sha256: ff5819e3a7b713c3bd3107b7de3d51fe0a347aa5d8444f0efdcf2345ef0a8b63
pdf_pages: "2"
extraction: vision
extraction_model: gpt-6-astra
content_sha256: 74b5e583713589bedbb9cd685277d12dd6d96a418d445ac1da456361e883a9cc
translated_from: content/en/goodfellow-2014-gan/02_related_work.md
source_content_sha256: 3c6ee40c3e5f0c541f155a1beac7058d33fb1fcee27693716f53a966e99ae912
translation_model: gpt-5
translation_run: 20260914T054537Z
glossary_version: 5
glossary_terms_sha256: 58c68d890f07ae3e920d6d07238da8d409da407f972fdd92b14f9e3f1e0382a4
prompt_sha256: a85b86fd402f05bc73ad3f4ad24540e4def82d38e0f105fa05c1de90e9436390
---

潜在変数を持つ有向グラフィカルモデルの代替として、restricted Boltzmann machines (RBMs) [27, 16]、deep Boltzmann machines (DBMs) [26]およびそれらの多数の変種のような、潜在変数を持つ無向グラフィカルモデルがある。そのようなモデル内の相互作用は、正規化されていないポテンシャル関数の積として表現され、確率変数のすべての状態にわたる大域的な総和／積分によって正規化される。この量（*分配関数*）とその勾配は、最も自明な場合を除いて扱いが困難であるが、Markov chain Monte Carlo (MCMC)法によって推定することは可能である。混合は、MCMCに依存する学習アルゴリズムにとって重大な問題となる[3, 5]。

Deep belief networks (DBNs) [16]は、単一の無向レイヤーと複数の有向レイヤーを含むハイブリッドモデルである。高速な近似的レイヤー単位の学習基準が存在する一方で、DBNは無向モデルと有向モデルの両方に関連する計算上の困難を抱える。

対数尤度を近似したり上界・下界を与えたりしない代替的な基準も提案されており、例えばscore matching [18]やnoise-contrastive estimation (NCE) [13]がある。これらはいずれも、学習された確率密度が正規化定数を除いて解析的に記述されることを必要とする。複数の潜在変数レイヤーを持つ多くの興味深い生成モデル（DBNやDBMなど）では、扱いやすい正規化されていない確率密度を導出することすら不可能であることに注意されたい。denoising auto-encoders [30]やcontractive autoencodersのようないくつかのモデルは、RBMに適用されたscore matchingと非常によく似た学習規則を持つ。NCEでは、本研究と同様に、生成モデルを適合させるために識別的な学習基準が用いられる。しかし、別個の識別モデルを適合させるのではなく、生成モデル自体を用いて、固定されたノイズ分布からのサンプルと生成データとを識別する。NCEは固定ノイズ分布を使用するため、モデルが観測変数の小さな部分集合に対しておおよそ正しい分布を学習した後は、学習速度が劇的に低下する。

最後に、確率分布を明示的に定義するのではなく、所望の分布からサンプルを生成する生成機械を学習させる手法も存在する。このアプローチには、そのような機械を誤差逆伝播によって学習できるように設計できるという利点がある。この分野における近年の代表的な研究として、generalized denoising auto-encoders [4]を拡張したgenerative stochastic network (GSN)フレームワーク[5]がある。両者はともに、パラメータ化されたMarkov chainを定義するものとみなすことができる。すなわち、生成Markov chainの1ステップを実行する機械のパラメータを学習するのである。GSNと比較すると、adversarial netsフレームワークはサンプリングのためにMarkov chainを必要としない。adversarial netsは生成中にフィードバックループを必要としないため、誤差逆伝播の性能を向上させる一方でフィードバックループ内で使用すると活性化が非有界になるという問題を持つpiecewise linear units [19, 9, 10]を、より効果的に活用できる。生成機械に対して誤差逆伝播を行うことによって学習するさらに最近の例として、auto-encoding variational Bayes [20]およびstochastic backpropagation [24]に関する最近の研究がある。
