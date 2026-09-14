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
section_title: 优势与劣势
tag: 00CE
kind: section
lang: zh
source: arxiv:1406.2661
pdf_sha256: ff5819e3a7b713c3bd3107b7de3d51fe0a347aa5d8444f0efdcf2345ef0a8b63
pdf_pages: "7"
extraction: vision
extraction_model: gpt-6-astra
content_sha256: d8355fe9f820a6c53deb76547cbed89d288bea9f309bf952c9d2eaae0dbb0dc3
translated_from: content/en/goodfellow-2014-gan/06_advantages_and_disadvantages.md
source_content_sha256: 38ce85b3fe3c89d51c7062535a10ebc800c4286b1991da131096aa15c4f7b192
translation_model: gpt-5
translation_run: 20260914T054537Z
glossary_version: 5
glossary_terms_sha256: aa1a7666eb5aba682ebd624c3c3b22b31572ab7cb642335fce8b31a161208c7e
prompt_sha256: a85b86fd402f05bc73ad3f4ad24540e4def82d38e0f105fa05c1de90e9436390
roundtrip: same
roundtrip_run: 20260914T070941Z
---

与先前的建模框架相比，这一新框架既有优势也有劣势。其劣势主要在于不存在对$p_g(x)$的显式表示，并且在训练过程中$D$必须与$G$保持良好同步（特别是，为了避免“Helvetica 情形”，即$G$将过多的$\mathbf{z}$取值坍缩到同一个$\mathbf{x}$取值，从而缺乏足够的多样性来建模$p_{\text{data}}$，在不更新$D$的情况下不能对$G$进行过多训练）；这一点类似于玻尔兹曼机的负链必须在学习步骤之间保持最新状态。其优势在于永远不需要马尔可夫链，只需使用反向传播来获得梯度，学习过程中不需要推理，并且可以将各种各样的函数纳入模型。表 2总结了生成对抗网络与其他生成建模方法的比较。

上述优势主要体现在计算方面。由于生成器网络并非直接利用数据样例进行更新，而仅通过流经判别器的梯度进行更新，对抗模型还可能因此获得某些统计上的优势。这意味着输入的各个组成部分不会被直接复制到生成器的参数中。对抗网络的另一个优势是，它们能够表示非常尖锐甚至退化的分布；而基于马尔可夫链的方法则要求分布具有一定程度的模糊性，以便链能够在不同模态之间实现混合。
