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
section_title: 理论结果
tag: 00C6
kind: section
lang: zh
source: arxiv:1406.2661
pdf_sha256: ff5819e3a7b713c3bd3107b7de3d51fe0a347aa5d8444f0efdcf2345ef0a8b63
pdf_pages: 3-5
extraction: vision
extraction_model: gpt-6-astra
content_sha256: d3264cb1b7ddbb2cff4563cff5f2650e9a9e7beb3fdb38df449065c31eebe5bb
translated_from: content/en/goodfellow-2014-gan/04_theoretical_results.md
source_content_sha256: 1d15ad3c47f4ca03cc21c1352f04d4732982e16fb3695b4b962e91ca04507c05
translation_model: gpt-5
translation_run: 20260914T054537Z
glossary_version: 5
glossary_terms_sha256: aa1a7666eb5aba682ebd624c3c3b22b31572ab7cb642335fce8b31a161208c7e
prompt_sha256: a85b86fd402f05bc73ad3f4ad24540e4def82d38e0f105fa05c1de90e9436390
roundtrip: differs-materially
roundtrip_run: 20260914T070941Z
---

生成器$G$将当$z\sim p_z$时得到的样本$G(z)$的分布隐式定义为概率分布$p_g$。因此，如果给定足够的容量和训练时间，我们希望算法1能够收敛到$p_{\mathrm{data}}$的一个良好估计器。本节的结果是在非参数设定下得到的，例如，我们通过研究概率密度函数空间中的收敛性来表示具有无限容量的模型。

我们将在4.1节中证明，当$p_g=p_{\mathrm{data}}$时，该极小极大博弈具有全局最优解。随后我们将在4.2节中证明算法1优化式1，从而得到期望的结果。

**算法 1** 生成对抗网络的小批量随机梯度下降训练。应用于判别器的步数$k$是一个超参数。在我们的实验中使用了$k = 1$，这是代价最低的选择。

**for** 训练迭代次数 **do**

**for** $k$步 **do**

- 从噪声先验$p_g(z)$中采样包含$m$个噪声样本的小批量$\{z^{(1)}, \ldots, z^{(m)}\}$。
- 从数据生成分布$p_{\text{data}}(x)$中采样包含$m$个样本的小批量$\{x^{(1)}, \ldots, x^{(m)}\}$。
- 通过沿其随机梯度上升来更新判别器：

$$\nabla_{\theta_d}\frac{1}{m}\sum_{i=1}^{m}\left[\log D\left(x^{(i)}\right)+\log\left(1-D\left(G\left(z^{(i)}\right)\right)\right)\right].$$

**end for**

- 从噪声先验$p_g(z)$中采样包含$m$个噪声样本的小批量$\{z^{(1)}, \ldots, z^{(m)}\}$。
- 通过沿其随机梯度下降来更新生成器：

$$\nabla_{\theta_g}\frac{1}{m}\sum_{i=1}^{m}\log\left(1-D\left(G\left(z^{(i)}\right)\right)\right).$$

**end for**

基于梯度的更新可以使用任何标准的基于梯度的学习规则。在我们的实验中使用了动量法。

### 4.1 $p_g = p_{\text{data}}$的全局最优性 {#goodfellow-2014-gan-s4-1 .section tag=00C7}

我们首先考虑任意给定生成器$G$对应的最优判别器$D$。

**命题 1.** *对于固定的$G$，最优判别器$D$为* {#goodfellow-2014-gan-prop-1 .statement tag=00C8}

$$D_G^*(x)=\frac{p_{\text{data}}(x)}{p_{\text{data}}(x)+p_g(x)}\tag{2}$$
{#goodfellow-2014-gan-eq-2 .equation tag=014B}

*证明。* 给定任意生成器G，判别器D的训练准则是最大化量$V(G,D)$

$$\begin{aligned}
V(G,D)&=\int_x p_{\text{data}}(x)\log(D(x))dx+\int_z p_z(z)\log(1-D(g(z)))dz\\
&=\int_x p_{\text{data}}(x)\log(D(x))+p_g(x)\log(1-D(x))dx
\end{aligned}\tag{3}$$
{#goodfellow-2014-gan-eq-3 .equation tag=014C}

对于任意$(a,b)\in\mathbb{R}^2\setminus\{0,0\}$，函数$y\rightarrow a\log(y)+b\log(1-y)$在区间$[0,1]$上的最大值于$\frac{a}{a+b}$处取得。判别器无需在$Supp(p_{\text{data}})\cup Supp(p_g)$之外定义，证明完成。$\square$

注意，$D$的训练目标可以解释为最大化用于估计条件概率$P(Y=y|x)$的对数似然，其中$Y$表示$x$是来自$p_{\text{data}}$（此时$y=1$）还是来自$p_g$（此时$y=0$）。式1中的极小极大博弈现在可以重写为：

$$\begin{aligned}
C(G)&=\max_D V(G,D)\\
&=\mathbb{E}_{x\sim p_{\text{data}}}\left[\log D_G^*(x)\right]+\mathbb{E}_{z\sim p_z}\left[\log(1-D_G^*(G(z)))\right]\\
&=\mathbb{E}_{x\sim p_{\text{data}}}\left[\log D_G^*(x)\right]+\mathbb{E}_{x\sim p_g}\left[\log(1-D_G^*(x))\right]\\
&=\mathbb{E}_{x\sim p_{\text{data}}}\left[\log\frac{p_{\text{data}}(x)}{p_{\text{data}}(x)+p_g(x)}\right]+\mathbb{E}_{x\sim p_g}\left[\log\frac{p_g(x)}{p_{\text{data}}(x)+p_g(x)}\right]
\end{aligned}\tag{4}$$
{#goodfellow-2014-gan-eq-4 .equation tag=014D}

**定理 1.** *虚拟训练准则$C(G)$的全局最小值当且仅当$p_g = p_{\mathrm{data}}$时达到。此时，$C(G)$取得值$-\log 4$。* {#goodfellow-2014-gan-thm-1 .statement tag=0111}

*证明。* 当$p_g = p_{\mathrm{data}}$时，$D_G^*(x) = \frac{1}{2}$（见式2）。因此，考察$D_G^*(x) = \frac{1}{2}$时的式4，可得$C(G) = \log \frac{1}{2} + \log \frac{1}{2} = -\log 4$。为了说明这是$C(G)$所能达到的最佳值，并且仅在$p_g = p_{\mathrm{data}}$时达到，注意到

$$\mathbb{E}_{x\sim p_{\mathrm{data}}}[-\log 2] + \mathbb{E}_{x\sim p_g}[-\log 2] = -\log 4$$

并且从$C(G) = V(D_G^*, G)$中减去该表达式，我们得到：

$$C(G) = -\log(4) + KL\left(p_{\mathrm{data}} \left\| \frac{p_{\mathrm{data}} + p_g}{2}\right.\right) + KL\left(p_g \left\| \frac{p_{\mathrm{data}} + p_g}{2}\right.\right) \tag{5}$$
{#goodfellow-2014-gan-eq-5 .equation tag=014E}

其中 KL 是 Kullback–Leibler 散度。我们可以在前面的表达式中识别出模型分布与数据生成过程之间的 Jensen–Shannon 散度：

$$C(G) = -\log(4) + 2 \cdot JSD(p_{\mathrm{data}} \| p_g) \tag{6}$$
{#goodfellow-2014-gan-eq-6 .equation tag=014F}

由于两个分布之间的 Jensen–Shannon 散度总是非负的，并且仅当它们相等时才为零，我们已经证明$C^* = -\log(4)$是$C(G)$的全局最小值，并且唯一解为$p_g = p_{\mathrm{data}}$，即生成模型完美复制了数据生成过程。$\square$

### 4.2 算法 1 的收敛性 {#goodfellow-2014-gan-s4-2 .section tag=0112}

**命题 2.** *如果$G$和$D$具有足够的容量，并且在算法 1 的每一步中，判别器在给定$G$的条件下都被允许达到其最优值，同时更新$p_g$以改进准则* {#goodfellow-2014-gan-prop-2 .statement tag=0113}

$$\mathbb{E}_{x\sim p_{\mathrm{data}}}[\log D_G^*(x)] + \mathbb{E}_{x\sim p_g}[\log(1 - D_G^*(x))]$$

*则$p_g$收敛到$p_{\mathrm{data}}$*

*证明。*按照上述准则中的做法，将$V(G, D) = U(p_g, D)$视为$p_g$的函数。注意，$U(p_g, D)$关于$p_g$是凸的。凸函数上确界的次导数包含达到最大值点处该函数的导数。换言之，如果$f(x) = \sup_{\alpha\in\mathcal{A}} f_\alpha(x)$，并且对每个$\alpha$都有$f_\alpha(x)$关于$x$凸，那么当$\beta = \arg \sup_{\alpha\in\mathcal{A}} f_\alpha(x)$时，$\partial f_\beta(x) \in \partial f$。这等价于在对应$G$给定时的最优$D$处，对$p_g$计算一次梯度下降更新。根据定理 1 已证明的结果，$\sup_D U(p_g, D)$关于$p_g$是凸的，并且具有唯一的全局最优解，因此当$p_g$的更新足够小时，$p_g$收敛到$p_x$，从而完成证明。$\square$

在实践中，对抗网络通过函数$G(z; \theta_g)$表示$p_g$分布的一个受限族，而我们优化的是$\theta_g$而非$p_g$本身。使用多层感知机来定义$G$会在参数空间中引入多个临界点。然而，多层感知机在实践中的优异性能表明，尽管缺乏理论保证，它们仍然是合理可用的模型。
