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
section_title: Front Matter
tag: 00C0
kind: front
lang: zh
source: arxiv:1406.2661
pdf_sha256: ff5819e3a7b713c3bd3107b7de3d51fe0a347aa5d8444f0efdcf2345ef0a8b63
pdf_pages: "1"
extraction: vision
extraction_model: gpt-6-astra
content_sha256: b1c208c8091c94335038956ca99c7664e87ca47f2448bff44b88114ef2b7c72a
translated_from: content/en/goodfellow-2014-gan/00_front.md
source_content_sha256: c265cba67355836c7114c3970907c02f98e48871dec6b14aad433176ef193cb2
translation_model: gpt-5
translation_run: 20260914T054537Z
glossary_version: 5
glossary_terms_sha256: aa1a7666eb5aba682ebd624c3c3b22b31572ab7cb642335fce8b31a161208c7e
prompt_sha256: a85b86fd402f05bc73ad3f4ad24540e4def82d38e0f105fa05c1de90e9436390
---

生成对抗网络

**Ian J. Goodfellow，Jean Pouget-Abadie[^1]，Mehdi Mirza，Bing Xu，David Warde-Farley，Sherjil Ozair[^2]，Aaron Courville，Yoshua Bengio[^3]**

Département d’informatique et de recherche opérationnelle  
Université de Montréal  
Montréal, QC H3C 3J7

arXiv:1406.2661v1 [stat.ML] 10 Jun 2014

摘要

我们提出了一种通过对抗过程估计生成模型的新框架，其中同时训练两个模型：一个捕获数据分布的生成模型$G$，以及一个估计某个样本来自训练数据而非$G$的概率的判别模型$D$。$G$的训练过程是最大化$D$犯错的概率。该框架对应于一个极小极大双人博弈。在任意函数$G$和$D$构成的空间中，存在唯一解，其中$G$恢复训练数据分布，而$D$在所有位置都等于$\frac{1}{2}$。当$G$和$D$由多层感知机定义时，整个系统都可以通过反向传播进行训练。在训练过程中或生成样本过程中，都不需要任何马尔可夫链或展开的近似推理网络。实验通过对生成样本的定性和定量评估，展示了该框架的潜力。
