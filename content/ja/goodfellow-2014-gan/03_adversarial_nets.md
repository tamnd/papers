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
section: "3"
section_title: 敵対的ネット
tag: 00C3
kind: section
lang: ja
source: arxiv:1406.2661
pdf_sha256: ff5819e3a7b713c3bd3107b7de3d51fe0a347aa5d8444f0efdcf2345ef0a8b63
pdf_pages: 2-3
extraction: vision
extraction_model: gpt-6-astra
content_sha256: 51e636a55971e86f6fc0d73fd95213a16e1e4ae54c04a3150ffca284c7298394
translated_from: content/en/goodfellow-2014-gan/03_adversarial_nets.md
source_content_sha256: ff7821dc77a57394deb3070ec820aedcf565d4263a8f0633cecb1bd742a41264
translation_model: gpt-5
translation_run: 20260914T054537Z
glossary_version: 5
glossary_terms_sha256: 58c68d890f07ae3e920d6d07238da8d409da407f972fdd92b14f9e3f1e0382a4
prompt_sha256: a85b86fd402f05bc73ad3f4ad24540e4def82d38e0f105fa05c1de90e9436390
---

敵対的モデリングのフレームワークは、両方のモデルが多層パーセプトロンである場合に最も直接的に適用できる。データ$\boldsymbol{x}$上の生成器の分布$p_g$を学習するために、入力ノイズ変数$p_z(\boldsymbol{z})$上の事前分布を定義し、次にデータ空間への写像を$G(\boldsymbol{z}; \theta_g)$として表現する。ここで$G$は、パラメータ$\theta_g$を持つ多層パーセプトロンによって表現される微分可能な関数である。また、単一のスカラーを出力する第2の多層パーセプトロン$D(\boldsymbol{x}; \theta_d)$も定義する。$D(\boldsymbol{x})$は、$\boldsymbol{x}$が$p_g$ではなくデータから来た確率を表す。$D$は、学習例と$G$からのサンプルの両方に正しいラベルを割り当てる確率を最大化するように学習する。同時に、$G$は$\log(1 - D(G(\boldsymbol{z})))$を最小化するように学習する。

言い換えると、$D$と$G$は、値関数$V(G,D)$を持つ以下の二者ミニマックスゲームを行う。

$$\min_G \max_D V(D,G) = \mathbb{E}_{x\sim p_{\mathrm{data}}(x)}[\log D(x)] + \mathbb{E}_{z\sim p_z(z)}[\log(1-D(G(z)))]. \tag{1}$$
{#goodfellow-2014-gan-eq-1 .equation tag=00C4}

次節では、敵対的ネットの理論的解析を示す。基本的には、この学習基準によって、$G$と$D$に十分な容量が与えられたとき、すなわち非パラメトリック極限において、データ生成分布を回復できることを示す。より形式性を抑えた教育的な説明については図 1を参照されたい。実際には、このゲームを反復的な数値的手法を用いて実装しなければならない。学習の内側ループで$D$を完全に最適化することは計算上法外に高価であり、有限のデータセットでは過学習を引き起こす。その代わりに、$D$の最適化を$k$ステップ行い、その後$G$の最適化を1ステップ行うことを交互に繰り返す。これにより、$G$が十分ゆっくり変化する限り、$D$はその最適解の近傍に維持される。この戦略は、SML/PCD [31, 29]学習が、学習の内側ループの一部としてマルコフ連鎖をバーンインすることを避けるために、ある学習ステップから次の学習ステップへとマルコフ連鎖からのサンプルを維持する方法と類似している。この手続きはアルゴリズム 1で形式的に示される。

実際には、式 1は$G$が十分に学習するための十分な勾配を与えない可能性がある。学習の初期段階では、$G$の性能が低いとき、$D$はサンプルが学習データと明らかに異なるため、高い確信度でそれらを棄却できる。この場合、$\log(1-D(G(z)))$は飽和する。$G$を$\log(1-D(G(z)))$の最小化に向けて学習する代わりに、$\log D(G(z))$を最大化するように$G$を学習できる。この目的関数は、$G$と$D$の力学系において同じ不動点をもたらすが、学習初期においてはるかに強い勾配を提供する。

図 1: Generative adversarial netsは、識別分布($D$、青色、破線)を同時に更新することによって学習される。これにより、データ生成分布（黒色、点線）$p_x$からのサンプルと、生成分布$p_g$（$G$）（緑色、実線）からのサンプルとを識別する。下側の水平線は$z$がサンプリングされる定義域であり、この場合は一様である。上側の水平線は$x$の定義域の一部である。上向きの矢印は、写像$x=G(z)$がどのようにして変換されたサンプル上に非一様分布$p_g$を課すかを示している。$G$は高密度領域では収縮し、$p_g$の低密度領域では拡張する。(a) 収束近傍の敵対的な組を考える。$p_g$は$p_{\mathrm{data}}$に類似しており、$D$は部分的に正確な分類器である。(b) アルゴリズムの内側ループでは、$D$はデータからのサンプルを識別するように学習され、$D^*(x)=\frac{p_{\mathrm{data}}(x)}{p_{\mathrm{data}}(x)+p_g(x)}$へ収束する。(c) $G$の更新後、$D$の勾配が$G(z)$を、データとして分類される可能性がより高い領域へ流れるよう導いている。(d) 数ステップの学習後、$G$と$D$が十分な容量を持つならば、$p_g=p_{\mathrm{data}}$であるため両者とも改善できない点に到達する。識別器は2つの分布を区別できず、すなわち$D(x)=\frac{1}{2}$である。 {#goodfellow-2014-gan-fig-1 .figure tag=00C5}
