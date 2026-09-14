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
content_sha256: 1f2bf2601b86ac2d3063820074d6ea1d6525944427047564169991e8ea59dc5f
translated_from: content/en/goodfellow-2014-gan/00_front.md
source_content_sha256: c265cba67355836c7114c3970907c02f98e48871dec6b14aad433176ef193cb2
translation_model: gpt-5
translation_run: 20260914T092812Z
glossary_version: 6
glossary_terms_sha256: a54b44c66f813573817631b2e13509458c4c984fece046c19f0e2b8008e83eba
prompt_sha256: da0c2696badfbe5d93fdc534847b1b0ca3b25ec37e0ce29843665f6e701c278e
---

生成对抗网络

Ian J. Goodfellow, Jean Pouget-Abadie[^1], Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair[^2], Aaron Courville, Yoshua Bengio[^3]

Département d’informatique et de recherche opérationnelle  
Université de Montréal  
Montréal, QC H3C 3J7

arXiv:1406.2661v1 [stat.ML] 10 Jun 2014

摘要

我们提出了一种通过对抗过程估计生成模型的新框架，在该过程中，我们同时训练两个模型：一个捕获数据分布的生成模型$G$，以及一个判别模型$D$，用于估计样本来自训练数据而非$G$的概率。$G$的训练过程是最大化$D$出错的概率。该框架对应于一个极小极大双人博弈。在任意函数$G$和$D$的空间中，存在唯一解，其中$G$恢复训练数据分布，而$D$处处等于$\frac12$。当$G$和$D$由多层感知机定义时，整个系统可以通过反向传播进行训练。在训练或生成样本的过程中，都不需要任何马尔可夫链或展开的近似推理网络。实验通过对生成样本进行定性和定量评估，展示了该框架的潜力。
