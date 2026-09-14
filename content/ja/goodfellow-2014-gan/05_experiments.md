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
section: "5"
section_title: 実験
tag: 00C9
kind: section
lang: ja
source: arxiv:1406.2661
pdf_sha256: ff5819e3a7b713c3bd3107b7de3d51fe0a347aa5d8444f0efdcf2345ef0a8b63
pdf_pages: 5-7
extraction: vision
extraction_model: gpt-6-astra
content_sha256: 90945eeb26cab636f6bbeabab17d1f9b9f6043612e495d603d493fd0fbd7b499
translated_from: content/en/goodfellow-2014-gan/05_experiments.md
source_content_sha256: 6e9e71cdcb721694c83f39a82661c91c3b69837dd0335f7d11ec5fea5de12d9a
translation_model: gpt-5
translation_run: 20260914T054537Z
glossary_version: 5
glossary_terms_sha256: 58c68d890f07ae3e920d6d07238da8d409da407f972fdd92b14f9e3f1e0382a4
prompt_sha256: a85b86fd402f05bc73ad3f4ad24540e4def82d38e0f105fa05c1de90e9436390
roundtrip: differs-materially
roundtrip_run: 20260914T070941Z
---

MNIST[[lecun-1998-lenet]]、Toronto Face Database (TFD) [28]、および CIFAR-10 [21]を含むさまざまなデータセット上で敵対的ネットを学習した。生成器ネットは rectifier linear activation [19, 9]と sigmoid activation の混合を用い、一方で識別器ネットは maxout [10] activation を用いた。識別器ネットの学習にはドロップアウト [17]を適用した。理論的フレームワークでは生成器の中間レイヤーにドロップアウトやその他のノイズを用いることが可能であるが、本研究では生成器ネットワークの最下層への入力としてのみノイズを用いた。

$G$によって生成されたサンプルに Gaussian Parzen window を当てはめ、この分布の下での対数尤度を報告することにより、$p_g$の下でのテストセットデータの確率を推定する。$\sigma$パラメータ

| モデル | MNIST | TFD |
|---|---|---|
| DBN [3] | $138 \pm 2$ | $1909 \pm 66$ |
| Stacked CAE [3] | $121 \pm 1.6$ | $\mathbf{2110 \pm 50}$ |
| Deep GSN [6] | $214 \pm 1.1$ | $1890 \pm 29$ |
| 敵対的ネット | $\mathbf{225 \pm 2}$ | $\mathbf{2057 \pm 26}$ |

表 1: Parzen window に基づく対数尤度推定値。MNIST で報告した数値はテストセット上のサンプルの平均対数尤度であり、平均の標準誤差はサンプル間で計算した。TFD では、データセットの各 fold 間で標準誤差を計算し、各 fold の検証セットを用いて異なる$\sigma$を選択した。TFD では、各 fold ごとに$\sigma$の交差検証を行い、各 fold の平均対数尤度を計算した。MNIST については、データセットの二値版ではなく実数値版に対する他のモデルと比較している。 {#goodfellow-2014-gan-tab-1 .table tag=00CA}

の Gaussian は検証セット上での交差検証によって求めた。この手法は Breuleux *et al.* [8]によって導入され、厳密な尤度の計算が実行不可能なさまざまな生成モデルに対して用いられている [25, 3, 5]。結果を表 1 に示す。この尤度推定法は分散がやや大きく、高次元空間では良好に機能しないが、我々の知る限り利用可能な最良の手法である。サンプリングはできるが尤度を直接推定できない生成モデルの進歩は、そのようなモデルの評価方法に関するさらなる研究を促している。

図 2 および図 3 では、学習後の生成器ネットから得られたサンプルを示す。これらのサンプルが既存手法によって生成されたサンプルより優れていると主張するものではないが、少なくとも文献中の優れた生成モデルと競争力があり、敵対的フレームワークの可能性を示していると考える。

図 2: モデルからのサンプルの可視化。最右列には隣接するサンプルに最も近い学習サンプルを示しており、モデルが学習セットを記憶していないことを示すためのものである。サンプルは恣意的に選んだものではなく、公平なランダム抽出である。深層生成モデルの他の多くの可視化とは異なり、これらの画像は隠れユニットのサンプルに条件付けられた条件付き平均ではなく、モデル分布からの実際のサンプルを示している。さらに、サンプリング過程は Markov chain の混合に依存しないため、これらのサンプルは無相関である。a) MNIST b) TFD c) CIFAR-10 (全結合モデル) d) CIFAR-10 (畳み込み識別器および「deconvolutional」生成器) {#goodfellow-2014-gan-fig-2 .figure tag=00CB}

図 3: 完全モデルの$z$空間内の座標間を線形補間することによって得られた数字。 {#goodfellow-2014-gan-fig-3 .figure tag=00CC}

|  | 深層有向グラフィカルモデル | 深層無向グラフィカルモデル | 生成オートエンコーダ | 敵対的モデル |
|---|---|---|---|---|
| 学習 | 学習中に推論が必要。 | 学習中に推論が必要。分配関数の勾配を近似するために MCMC が必要。 | 混合と再構成生成能力の間のトレードオフを強制。 | 識別器と生成器の同期。Helvetica。 |
| 推論 | 学習された近似推論 | 変分推論 | MCMC ベースの推論 | 学習された近似推論 |
| サンプリング | 困難なし | Markov chain が必要 | Markov chain が必要 | 困難なし |
| $p(x)$の評価 | 実行不可能だが AIS により近似可能 | 実行不可能だが AIS により近似可能 | 明示的には表現されないが、Parzen density estimation により近似可能 | 明示的には表現されないが、Parzen density estimation により近似可能 |
| モデル設計 | ほぼすべてのモデルで極端な困難が生じる | 複数の性質を保証するために慎重な設計が必要 | 任意の微分可能な関数が理論上許容される | 任意の微分可能な関数が理論上許容される |

表 2: 生成モデリングにおける課題。モデルに関わる主要な操作ごとに、深層生成モデリングへの異なるアプローチが遭遇する困難を要約したものである。 {#goodfellow-2014-gan-tab-2 .table tag=00CD}
