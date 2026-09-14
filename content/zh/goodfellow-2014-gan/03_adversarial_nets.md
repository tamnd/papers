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
section_title: 对抗网络
tag: 00C3
kind: section
lang: zh
source: arxiv:1406.2661
pdf_sha256: ff5819e3a7b713c3bd3107b7de3d51fe0a347aa5d8444f0efdcf2345ef0a8b63
pdf_pages: 2-3
extraction: vision
extraction_model: gpt-6-astra
content_sha256: 7b8a9840b42752351164835b0f3e902a1b06dc4992944d1aebc3c2c00e71183d
translated_from: content/en/goodfellow-2014-gan/03_adversarial_nets.md
source_content_sha256: ff7821dc77a57394deb3070ec820aedcf565d4263a8f0633cecb1bd742a41264
translation_model: gpt-5
translation_run: 20260914T063738Z
glossary_version: 5
glossary_terms_sha256: aa1a7666eb5aba682ebd624c3c3b22b31572ab7cb642335fce8b31a161208c7e
prompt_sha256: a85b86fd402f05bc73ad3f4ad24540e4def82d38e0f105fa05c1de90e9436390
roundtrip: differs-in-wording
roundtrip_run: 20260914T070941Z
---

当两个模型都是多层感知机时，对抗建模框架最容易应用。为了学习生成器在数据$\boldsymbol{x}$上的分布$p_g$，我们定义输入噪声变量的先验分布$p_z(\boldsymbol{z})$，然后将到数据空间的映射表示为$G(\boldsymbol{z}; \theta_g)$，其中$G$是一个由参数$\theta_g$的多层感知机表示的可微函数。我们还定义第二个多层感知机$D(\boldsymbol{x}; \theta_d)$，其输出为单个标量。$D(\boldsymbol{x})$表示$\boldsymbol{x}$来自数据而非$p_g$的概率。我们训练$D$以最大化对训练样本和来自$G$的样本都赋予正确标签的概率。同时，我们训练$G$以最小化$\log(1 - D(G(\boldsymbol{z})))$：

换句话说，$D$和$G$进行如下以$V(G,D)$为价值函数的双人极小极大博弈：

$$\min_G \max_D V(D,G) = \mathbb{E}_{x\sim p_{\mathrm{data}}(x)}[\log D(x)] + \mathbb{E}_{z\sim p_z(z)}[\log(1-D(G(z)))]. \tag{1}$$
{#goodfellow-2014-gan-eq-1 .equation tag=00C4}

在下一节中，我们将给出对抗网络的理论分析，其本质是说明：当赋予$G$和$D$足够的容量时，即在非参数极限下，该训练准则能够恢复数据生成分布。关于该方法一种不那么正式、更具教学性的解释，请参见图 1。在实践中，我们必须采用迭代的数值方法来实现这一博弈。在训练的内层循环中将$D$优化至完成在计算上代价过高，而且在有限数据集上会导致过拟合。相反，我们交替执行$k$步对$D$的优化和一步对$G$的优化。只要$G$变化得足够缓慢，这就能使$D$始终维持在其最优解附近。这一策略类似于SML/PCD [31, 29]训练中的做法，即从一个学习步骤到下一个学习步骤持续维护来自马尔可夫链的样本，从而避免在学习的内层循环中对马尔可夫链进行预热。该过程在算法 1中进行了正式描述。

在实践中，公式 1可能无法为$G$提供足够的梯度以实现良好学习。在学习初期，当$G$表现较差时，$D$能够以很高的置信度拒绝样本，因为它们与训练数据明显不同。在这种情况下，$\log(1-D(G(z)))$会饱和。与其训练$G$去最小化$\log(1-D(G(z)))$，我们可以训练$G$去最大化$\log D(G(z))$。这一目标函数会产生与$G$和$D$动力学相同的不动点，但在学习初期能够提供强得多的梯度。

图 1：生成对抗网络通过同时更新判别分布（$D$，蓝色虚线），使其能够区分来自数据生成分布（黑色点线）$p_x$的样本与来自生成分布$p_g$（$G$）（绿色实线）的样本来进行训练。下方的水平线是对$z$进行采样的定义域，在此情形下为均匀采样。上方的水平线是$x$定义域的一部分。向上的箭头展示了映射$x=G(z)$如何在变换后的样本上施加非均匀分布$p_g$。$G$在高密度区域收缩，在$p_g$的低密度区域扩张。(a) 考虑一个接近收敛的对抗博弈对：$p_g$与$p_{\mathrm{data}}$相似，而$D$是一个部分准确的分类器。(b) 在算法的内层循环中，训练$D$以区分来自数据的样本，并收敛到$D^*(x)=\frac{p_{\mathrm{data}}(x)}{p_{\mathrm{data}}(x)+p_g(x)}$。(c) 在对$G$进行一次更新后，$D$的梯度引导$G(z)$流向更有可能被分类为数据的区域。(d) 经过若干步训练后，如果$G$和$D$具有足够的容量，它们将达到一个双方都无法进一步改进的点，因为$p_g=p_{\mathrm{data}}$。判别器无法区分这两个分布，即$D(x)=\frac{1}{2}$。 {#goodfellow-2014-gan-fig-1 .figure tag=00C5}
