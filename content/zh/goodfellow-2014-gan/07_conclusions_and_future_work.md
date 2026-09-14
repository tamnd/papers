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
section: "7"
section_title: 结论与未来工作
tag: 00CF
kind: section
lang: zh
source: arxiv:1406.2661
pdf_sha256: ff5819e3a7b713c3bd3107b7de3d51fe0a347aa5d8444f0efdcf2345ef0a8b63
pdf_pages: 7-8
extraction: vision
extraction_model: gpt-6-astra
content_sha256: 7086ff45d2aa6fec690b5c8acaec3fb2b3ab2912bbb9d4b89d7b108a742524a5
translated_from: content/en/goodfellow-2014-gan/07_conclusions_and_future_work.md
source_content_sha256: 6597befe412644971c55ff96746aa0a8f4a0851488f0444c194e2a434ef4b7a1
translation_model: gpt-5
translation_run: 20260914T054537Z
glossary_version: 5
glossary_terms_sha256: aa1a7666eb5aba682ebd624c3c3b22b31572ab7cb642335fce8b31a161208c7e
prompt_sha256: a85b86fd402f05bc73ad3f4ad24540e4def82d38e0f105fa05c1de90e9436390
roundtrip: differs-in-wording
roundtrip_run: 20260914T070941Z
---

该框架允许许多直接的扩展：

1. 通过将$\mathbf{c}$作为输入同时加入$G$和$D$，可以得到一个*条件*生成模型$p(\mathbf{x}\mid\mathbf{c})$。
2. 通过训练一个辅助网络来根据$\mathbf{x}$预测$\mathbf{z}$，可以实现*学习得到的近似推理*。这与由wake-sleep算法[15]训练的推理网络类似，但其优点在于，在生成器网络完成训练之后，可以针对一个固定的生成器网络来训练推理网络。

3. 通过训练一族共享参数的条件模型，可以近似地对所有条件分布$p(x_S \mid x_{\not S})$进行建模，其中$S$是$x$的索引集合的一个子集。从本质上讲，可以利用对抗网络来实现确定性MP-DBM [11]的随机扩展。
4. *半监督学习：*来自判别器或推理网络的特征，能够在可用标注数据有限时提高分类器的性能。
5. *效率改进：*通过设计更好的方法来协调$G$和$D$，或者在训练期间确定更优的$z$采样分布，可以大幅加速训练。

本文已经证明了对抗建模框架的可行性，表明这些研究方向可能是有价值的。
