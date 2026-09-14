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
section: "1"
section_title: 引言
tag: 00C1
kind: section
lang: zh
source: arxiv:1406.2661
pdf_sha256: ff5819e3a7b713c3bd3107b7de3d51fe0a347aa5d8444f0efdcf2345ef0a8b63
pdf_pages: 1-2
extraction: vision
extraction_model: gpt-6-astra
content_sha256: 382cac28246474e3249266a25e1ac68dcbfa53bf5fdd1787cf2ce36df79982e2
translated_from: content/en/goodfellow-2014-gan/01_introduction.md
source_content_sha256: 8cff2016cc5d3b4dd011b7208fdc0d32f9d8fa354a6c940d4eeb6be58318d257
translation_model: gpt-5
translation_run: 20260914T054537Z
glossary_version: 5
glossary_terms_sha256: aa1a7666eb5aba682ebd624c3c3b22b31572ab7cb642335fce8b31a161208c7e
prompt_sha256: a85b86fd402f05bc73ad3f4ad24540e4def82d38e0f105fa05c1de90e9436390
---

深度学习的前景在于发现丰富的、层次化的模型[2]，这些模型表示人工智能应用中遇到的各类数据上的概率分布，例如自然图像、包含语音的音频波形以及自然语言语料中的符号。到目前为止，深度学习最引人注目的成功主要来自判别模型，通常是那些将高维、丰富的感知输入映射到类别标签的模型[14]，[[krizhevsky-2012-imagenet]]。这些显著成功主要建立在反向传播和Dropout算法之上，使用分段线性单元[19, 9, 10]，其梯度具有特别良好的性质。深度*生成*模型的影响则较小，这是由于难以近似最大似然估计及相关策略中出现的许多难以处理的概率计算，也由于难以在生成场景中利用分段线性单元的优势。我们提出一种新的生成模型估计过程，绕开了这些困难。[^4]

在所提出的*对抗网络*框架中，生成模型与一个对手相对抗：一个学习判定样本来自模型分布还是数据分布的判别模型。生成模型可以被看作一群造假者，试图制造并使用假币而不被发现；而判别模型则类似于警察，试图识别假币。这场博弈中的竞争推动双方不断改进各自的方法，直到伪造品与真品无法区分。

[^1]: Jean Pouget-Abadie从Ecole Polytechnique访问蒙特利尔大学。
[^2]: Sherjil Ozair从Indian Institute of Technology Delhi访问蒙特利尔大学
[^3]: Yoshua Bengio是CIFAR高级研究员。
[^4]: 所有代码和超参数可在[http://www.github.com/goodfeli/adversarial](http://www.github.com/goodfeli/adversarial)获得

该框架能够为多种类型的模型和优化算法导出具体的训练算法。本文探索一种特殊情形：生成模型通过将随机噪声传入多层感知机来生成样本，而判别模型也是一个多层感知机。我们将这一特殊情形称为*对抗网络*。在这种情况下，我们只需使用极其成功的反向传播和Dropout算法[17]即可训练两个模型，并且只需前向传播即可从生成模型中采样。不需要近似推理或马尔可夫链。
