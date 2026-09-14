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
section: "4"
section_title: 理論的結果
tag: 00C6
kind: section
lang: ja
source: arxiv:1406.2661
pdf_sha256: ff5819e3a7b713c3bd3107b7de3d51fe0a347aa5d8444f0efdcf2345ef0a8b63
pdf_pages: 3-5
extraction: vision
extraction_model: gpt-6-astra
content_sha256: 04ab7940708a7962d1d67fcac611389694819e7e3eb79296923c75d4fa5874ef
translated_from: content/en/goodfellow-2014-gan/04_theoretical_results.md
source_content_sha256: 1d15ad3c47f4ca03cc21c1352f04d4732982e16fb3695b4b962e91ca04507c05
translation_model: gpt-5
translation_run: 20260914T054537Z
glossary_version: 5
glossary_terms_sha256: 58c68d890f07ae3e920d6d07238da8d409da407f972fdd92b14f9e3f1e0382a4
prompt_sha256: a85b86fd402f05bc73ad3f4ad24540e4def82d38e0f105fa05c1de90e9436390
---

生成器$G$は、$z\sim p_z$のときに得られるサンプル$G(z)$の分布として、確率分布$p_g$を暗黙的に定義する。したがって、十分な容量と学習時間が与えられれば、アルゴリズム 1が$p_{\mathrm{data}}$の良い推定量へ収束することを望む。本節の結果は非パラメトリックな設定で行われる。例えば、確率密度関数の空間における収束を調べることによって、無限の容量を持つモデルを表現する。

4.1節で、このミニマックスゲームが$p_g=p_{\mathrm{data}}$に対して大域的最適解を持つことを示す。続いて4.2節で、アルゴリズム 1が式 1を最適化することを示し、これによって望ましい結果が得られることを示す。

**アルゴリズム 1** 生成的敵対的ネットワークのミニバッチ確率的勾配降下法による学習。識別器に適用するステップ数$k$はハイパーパラメータである。我々の実験では、最も計算コストの低い選択肢である$k = 1$を用いた。

**for** 学習反復回数 **do**

**for** $k$ ステップ **do**

- ノイズ事前分布$p_g(z)$から、$m$個のノイズサンプル$\{z^{(1)}, \ldots, z^{(m)}\}$のミニバッチをサンプリングする。
- データ生成分布$p_{\text{data}}(x)$から、$m$個の例$\{x^{(1)}, \ldots, x^{(m)}\}$のミニバッチをサンプリングする。
- 確率的勾配に沿って上昇することにより識別器を更新する。

$$\nabla_{\theta_d}\frac{1}{m}\sum_{i=1}^{m}\left[\log D\left(x^{(i)}\right)+\log\left(1-D\left(G\left(z^{(i)}\right)\right)\right)\right].$$

**end for**

- ノイズ事前分布$p_g(z)$から、$m$個のノイズサンプル$\{z^{(1)}, \ldots, z^{(m)}\}$のミニバッチをサンプリングする。
- 確率的勾配に沿って下降することにより生成器を更新する。

$$\nabla_{\theta_g}\frac{1}{m}\sum_{i=1}^{m}\log\left(1-D\left(G\left(z^{(i)}\right)\right)\right).$$

**end for**

勾配ベースの更新には、任意の標準的な勾配ベース学習則を用いることができる。我々の実験ではモメンタムを用いた。

### 4.1 $p_g = p_{\text{data}}$の大域的最適性 {#goodfellow-2014-gan-s4-1 .section tag=00C7}

まず、任意の与えられた生成器$G$に対する最適な識別器$D$を考える。

**命題 1.** *$G$を固定したとき、最適な識別器$D$は次式である* {#goodfellow-2014-gan-prop-1 .statement tag=00C8}

$$D_G^*(x)=\frac{p_{\text{data}}(x)}{p_{\text{data}}(x)+p_g(x)}\tag{2}$$
{#goodfellow-2014-gan-eq-2 .equation tag=014B}

*証明.* 任意の生成器Gが与えられたとき、識別器Dの学習基準は量$V(G,D)$を最大化することである。

$$\begin{aligned}
V(G,D)&=\int_x p_{\text{data}}(x)\log(D(x))dx+\int_z p_z(z)\log(1-D(g(z)))dz\\
&=\int_x p_{\text{data}}(x)\log(D(x))+p_g(x)\log(1-D(x))dx
\end{aligned}\tag{3}$$
{#goodfellow-2014-gan-eq-3 .equation tag=014C}

任意の$(a,b)\in\mathbb{R}^2\setminus\{0,0\}$について、関数$y\rightarrow a\log(y)+b\log(1-y)$は、$[0,1]$において$\frac{a}{a+b}$で最大値を達成する。識別器は$Supp(p_{\text{data}})\cup Supp(p_g)$の外側で定義される必要がないため、証明が完了する。$\square$

$D$の学習目的関数は、条件付き確率$P(Y=y|x)$を推定するための対数尤度を最大化するものとして解釈できることに注意されたい。ここで$Y$は、$x$が$p_{\text{data}}$（$y=1$）から来たか、あるいは$p_g$（$y=0$）から来たかを示す。式 1のミニマックスゲームは次のように再定式化できる。

$$\begin{aligned}
C(G)&=\max_D V(G,D)\\
&=\mathbb{E}_{x\sim p_{\text{data}}}\left[\log D_G^*(x)\right]+\mathbb{E}_{z\sim p_z}\left[\log(1-D_G^*(G(z)))\right]\\
&=\mathbb{E}_{x\sim p_{\text{data}}}\left[\log D_G^*(x)\right]+\mathbb{E}_{x\sim p_g}\left[\log(1-D_G^*(x))\right]\\
&=\mathbb{E}_{x\sim p_{\text{data}}}\left[\log\frac{p_{\text{data}}(x)}{p_{\text{data}}(x)+p_g(x)}\right]+\mathbb{E}_{x\sim p_g}\left[\log\frac{p_g(x)}{p_{\text{data}}(x)+p_g(x)}\right]
\end{aligned}\tag{4}$$
{#goodfellow-2014-gan-eq-4 .equation tag=014D}

**定理 1.** *仮想的な学習基準$C(G)$の大域的最小値は、$p_g = p_{\mathrm{data}}$である場合に限り達成される。そのとき、$C(G)$は値$-\log 4$を達成する。* {#goodfellow-2014-gan-thm-1 .statement tag=0111}

*証明.* $p_g = p_{\mathrm{data}}$のとき、$D_G^*(x) = \frac{1}{2}$である（式 2を参照）。したがって、$D_G^*(x) = \frac{1}{2}$における式 4を調べることで、$C(G) = \log \frac{1}{2} + \log \frac{1}{2} = -\log 4$を得る。これが$C(G)$の取り得る最良の値であり、かつ$p_g = p_{\mathrm{data}}$のときにのみ達成されることを示すために、次を観察する。

$$\mathbb{E}_{x\sim p_{\mathrm{data}}}[-\log 2] + \mathbb{E}_{x\sim p_g}[-\log 2] = -\log 4$$

そして、この式を$C(G) = V(D_G^*, G)$から差し引くことにより、次を得る。

$$C(G) = -\log(4) + KL\left(p_{\mathrm{data}} \left\| \frac{p_{\mathrm{data}} + p_g}{2}\right.\right) + KL\left(p_g \left\| \frac{p_{\mathrm{data}} + p_g}{2}\right.\right) \tag{5}$$
{#goodfellow-2014-gan-eq-5 .equation tag=014E}

ここで、KLはKullback–Leiblerダイバージェンスである。前式の中に、モデルの分布とデータ生成過程との間のJensen–Shannonダイバージェンスを認めることができる。

$$C(G) = -\log(4) + 2 \cdot JSD(p_{\mathrm{data}} \| p_g) \tag{6}$$
{#goodfellow-2014-gan-eq-6 .equation tag=014F}

二つの分布間のJensen–Shannonダイバージェンスは常に非負であり、それらが等しい場合にのみゼロとなるので、$C^* = -\log(4)$が$C(G)$の大域的最小値であり、唯一の解が$p_g = p_{\mathrm{data}}$、すなわち生成モデルがデータ生成過程を完全に再現することであることを示した。$\square$

### 4.2 アルゴリズム 1 の収束 {#goodfellow-2014-gan-s4-2 .section tag=0112}

**命題 2.** *$G$と$D$が十分な容量を持ち、アルゴリズム 1 の各ステップにおいて、識別器が与えられた$G$に対する最適値に到達することを許され、さらに$p_g$が次の基準を改善するように更新されるならば* {#goodfellow-2014-gan-prop-2 .statement tag=0113}

$$\mathbb{E}_{x\sim p_{\mathrm{data}}}[\log D_G^*(x)] + \mathbb{E}_{x\sim p_g}[\log(1 - D_G^*(x))]$$

*$p_g$は$p_{\mathrm{data}}$に収束する*

*証明.* 上記の基準で行ったように、$V(G, D) = U(p_g, D)$を$p_g$の関数として考える。$U(p_g, D)$は$p_g$について凸であることに注意せよ。凸関数族の上限の劣微分には、最大値が達成される点での関数の導関数が含まれる。言い換えると、$f(x) = \sup_{\alpha\in\mathcal{A}} f_\alpha(x)$であり、すべての$\alpha$について$f_\alpha(x)$が$x$に関して凸であるならば、$\beta = \arg \sup_{\alpha\in\mathcal{A}} f_\alpha(x)$のとき$\partial f_\beta(x) \in \partial f$である。これは、対応する$G$が与えられたときの最適な$D$において、$p_g$に対する勾配降下更新を計算することと等価である。定理 1 で証明したように、$\sup_D U(p_g, D)$は$p_g$について凸であり、かつ一意な大域的最適値を持つ。したがって、$p_g$の更新が十分に小さければ、$p_g$は$p_x$に収束し、これで証明は完了する。$\square$

実際には、敵対的ネットワークは関数$G(z; \theta_g)$を介して$p_g$分布の限定された族を表現し、$p_g$そのものではなく$\theta_g$を最適化する。$G$を定義するために多層パーセプトロンを用いると、パラメータ空間に複数の臨界点が導入される。しかし、多層パーセプトロンが実際には優れた性能を示すことは、理論的保証が欠如しているにもかかわらず、それらが使用するのに妥当なモデルであることを示唆している。
