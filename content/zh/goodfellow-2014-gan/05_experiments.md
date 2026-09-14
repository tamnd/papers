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
section_title: 实验
tag: 00C9
kind: section
lang: zh
source: arxiv:1406.2661
pdf_sha256: ff5819e3a7b713c3bd3107b7de3d51fe0a347aa5d8444f0efdcf2345ef0a8b63
pdf_pages: 5-7
extraction: vision
extraction_model: gpt-6-astra
content_sha256: e660abe9deababda6e8042fb1db8dd8f5a97f56422ae4b981385f6c9b869e8fa
translated_from: content/en/goodfellow-2014-gan/05_experiments.md
source_content_sha256: 6e9e71cdcb721694c83f39a82661c91c3b69837dd0335f7d11ec5fea5de12d9a
translation_model: gpt-5
translation_run: 20260914T054537Z
glossary_version: 5
glossary_terms_sha256: aa1a7666eb5aba682ebd624c3c3b22b31572ab7cb642335fce8b31a161208c7e
prompt_sha256: a85b86fd402f05bc73ad3f4ad24540e4def82d38e0f105fa05c1de90e9436390
roundtrip: differs-in-wording
roundtrip_run: 20260914T070941Z
---

我们在多个数据集上训练了对抗网络，包括MNIST[[lecun-1998-lenet]]、Toronto Face Database（TFD）[28]以及CIFAR-10 [21]。生成器网络使用了整流线性激活函数[19, 9]与sigmoid激活函数的混合，而判别器网络使用了maxout [10]激活函数。在训练判别器网络时应用了Dropout [17]。尽管我们的理论框架允许在生成器的中间层使用dropout及其他噪声，但我们仅将噪声作为生成器网络最底层的输入。

我们通过对由$G$生成的样本拟合高斯Parzen窗，并报告该分布下的对数似然，来估计测试集数据在$p_g$下的概率。$\sigma$参数

| 模型 | MNIST | TFD |
|---|---|---|
| DBN [3] | $138 \pm 2$ | $1909 \pm 66$ |
| Stacked CAE [3] | $121 \pm 1.6$ | $\mathbf{2110 \pm 50}$ |
| Deep GSN [6] | $214 \pm 1.1$ | $1890 \pm 29$ |
| 对抗网络 | $\mathbf{225 \pm 2}$ | $\mathbf{2057 \pm 26}$ |

表 1：基于Parzen窗的对数似然估计。MNIST上的报告数值是测试集样本对数似然的均值，均值标准误差在样本间计算得到。在TFD上，我们在数据集各折之间计算标准误差，并使用每一折的验证集选择不同的$\sigma$。在TFD上，$\sigma$在每一折上通过交叉验证确定，并计算每一折上的平均对数似然。对于MNIST，我们与该数据集实值版本（而非二值版本）的其他模型进行比较。 {#goodfellow-2014-gan-tab-1 .table tag=00CA}

这些高斯分布的参数通过在验证集上进行交叉验证得到。该过程由Breuleux *et al.* [8]提出，并用于多种无法计算精确似然的生成模型[25, 3, 5]。结果见表 1。这种似然估计方法具有较高方差，在高维空间中表现不佳，但据我们所知，它是当前可用的最佳方法。那些能够采样却无法直接估计似然的生成模型的发展，促使人们进一步研究如何评估此类模型。

在图 2和图 3中，我们展示了训练后从生成器网络中抽取的样本。尽管我们并不声称这些样本优于现有方法生成的样本，但我们认为这些样本至少能够与文献中较好的生成模型相竞争，并体现了对抗框架的潜力。

图 2：模型样本的可视化。最右侧一列显示相邻样本最近的训练样本，用以证明模型并未记忆训练集。样本均为公平随机抽取，而非刻意挑选。与大多数其他深度生成模型的可视化不同，这些图像展示的是模型分布中的真实样本，而不是给定隐单元样本时的条件均值。此外，这些样本彼此不相关，因为采样过程不依赖于马尔可夫链混合。a）MNIST b）TFD c）CIFAR-10（全连接模型）d）CIFAR-10（卷积判别器与“反卷积”生成器） {#goodfellow-2014-gan-fig-2 .figure tag=00CB}

图 3：通过在完整模型的$z$空间坐标之间进行线性插值得到的数字。 {#goodfellow-2014-gan-fig-3 .figure tag=00CC}

|  | 深度有向图模型 | 深度无向图模型 | 生成式自编码器 | 对抗模型 |
|---|---|---|---|---|
| 训练 | 训练期间需要推理。 | 训练期间需要推理。需要MCMC来近似配分函数梯度。 | 在混合能力与重构生成能力之间强制权衡 | 使判别器与生成器同步。Helvetica。 |
| 推理 | 学习得到的近似推理 | 变分推理 | 基于MCMC的推理 | 学习得到的近似推理 |
| 采样 | 无困难 | 需要马尔可夫链 | 需要马尔可夫链 | 无困难 |
| 评估$p(x)$ | 不可处理，可用AIS近似 | 不可处理，可用AIS近似 | 未显式表示，可用Parzen密度估计近似 | 未显式表示，可用Parzen密度估计近似 |
| 模型设计 | 几乎所有模型都会遇到极大困难 | 需要精心设计以保证多种性质 | 理论上允许任意可微函数 | 理论上允许任意可微函数 |

表 2：生成建模中的挑战：对深度生成建模不同方法在涉及模型的各项主要操作中所遇到困难的总结。 {#goodfellow-2014-gan-tab-2 .table tag=00CD}
