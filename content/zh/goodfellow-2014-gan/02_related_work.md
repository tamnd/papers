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
section_title: 相关工作
tag: 00C2
kind: section
lang: zh
source: arxiv:1406.2661
pdf_sha256: ff5819e3a7b713c3bd3107b7de3d51fe0a347aa5d8444f0efdcf2345ef0a8b63
pdf_pages: "2"
extraction: vision
extraction_model: gpt-6-astra
content_sha256: 192d0676b7611697090e74c11f26fa3e5cc2e6050271882c5dc3cce3fca4804d
translated_from: content/en/goodfellow-2014-gan/02_related_work.md
source_content_sha256: 3c6ee40c3e5f0c541f155a1beac7058d33fb1fcee27693716f53a966e99ae912
translation_model: gpt-5
translation_run: 20260914T054537Z
glossary_version: 5
glossary_terms_sha256: aa1a7666eb5aba682ebd624c3c3b22b31572ab7cb642335fce8b31a161208c7e
prompt_sha256: a85b86fd402f05bc73ad3f4ad24540e4def82d38e0f105fa05c1de90e9436390
---

有潜变量的有向图模型的一种替代方案是有潜变量的无向图模型，例如受限玻尔兹曼机（RBM）[27, 16]、深度玻尔兹曼机（DBM）[26]及其众多变体。这类模型中的相互作用被表示为未归一化势函数乘积的形式，并通过对随机变量所有状态进行全局求和／积分来归一化。这一量（即*配分函数*）及其梯度除最平凡的情形外都难以处理，不过可以通过马尔可夫链蒙特卡罗（MCMC）方法进行估计。混合问题给依赖MCMC的学习算法带来了显著困难[3, 5]。

深度信念网络（DBN）[16]是包含一个无向层和若干有向层的混合模型。尽管存在一种快速的近似逐层训练准则，但DBN同时承担了无向模型和有向模型相关的计算困难。

也有人提出了不对对数似然进行近似或求界的替代准则，例如分数匹配（score matching）[18]和噪声对比估计（NCE）[13]。这两种方法都要求所学习的概率密度在解析形式上可表示到一个归一化常数为止。需要指出的是，在许多包含多层潜变量的有趣生成模型中（例如DBN和DBM），甚至无法导出一个可处理的未归一化概率密度。一些模型，如去噪自编码器[30]和收缩自编码器，其学习规则与应用于RBM的分数匹配非常相似。在NCE中，与本文一样，采用判别式训练准则来拟合生成模型。然而，它不是拟合一个独立的判别模型，而是利用生成模型本身来区分生成数据与来自固定噪声分布的样本。由于NCE使用固定的噪声分布，当模型已经在观测变量的一个小子集上学到哪怕近似正确的分布之后，学习速度也会显著下降。

最后，一些技术并不显式定义概率分布，而是训练一个生成机器从目标分布中抽取样本。这种方法的优点在于，此类机器可以被设计为通过反向传播进行训练。该方向近期的重要工作包括生成随机网络（GSN）框架[5]，它扩展了广义去噪自编码器[4]：两者都可以看作定义了一个参数化的马尔可夫链，即学习一个机器的参数，使其执行生成马尔可夫链中的一步。与GSN相比，对抗网络框架在采样时不需要马尔可夫链。由于对抗网络在生成过程中不需要反馈环路，因此能够更好地利用分段线性单元[19, 9, 10]；这类单元能够提升反向传播的性能，但在反馈环路中使用时会面临激活值无界的问题。通过向生成机器内部反向传播来训练生成机器的更近期例子，包括关于自编码变分贝叶斯（auto-encoding variational Bayes）[20]和随机反向传播（stochastic backpropagation）[24]的最新工作。
