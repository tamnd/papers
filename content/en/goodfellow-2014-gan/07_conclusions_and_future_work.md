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
section_title: Conclusions and future work
tag: 00CF
kind: section
lang: en
source: arxiv:1406.2661
pdf_sha256: ff5819e3a7b713c3bd3107b7de3d51fe0a347aa5d8444f0efdcf2345ef0a8b63
pdf_pages: 7-8
extraction: vision
extraction_model: gpt-6-astra
content_sha256: 6597befe412644971c55ff96746aa0a8f4a0851488f0444c194e2a434ef4b7a1
prompt_sha256: d53a8bfa14d5deec1eabb71e8a2ea2db8c42f516778942c09f3051aa50a9397f
---

This framework admits many straightforward extensions:

1. A *conditional* generative model $p(\mathbf{x}\mid\mathbf{c})$ can be obtained by adding $\mathbf{c}$ as input to both $G$ and $D$.
2. *Learned approximate inference* can be performed by training an auxiliary network to predict $\mathbf{z}$ given $\mathbf{x}$. This is similar to the inference net trained by the wake-sleep algorithm [15] but with the advantage that the inference net may be trained for a fixed generator net after the generator net has finished training.

3. One can approximately model all conditionals $p(x_S \mid x_{\not S})$ where $S$ is a subset of the indices of $x$ by training a family of conditional models that share parameters. Essentially, one can use adversarial nets to implement a stochastic extension of the deterministic MP-DBM [11].
4. *Semi-supervised learning:* features from the discriminator or inference net could improve performance of classifiers when limited labeled data is available.
5. *Efficiency improvements:* training could be accelerated greatly by divising better methods for coordinating $G$ and $D$ or determining better distributions to sample $z$ from during training.

This paper has demonstrated the viability of the adversarial modeling framework, suggesting that these research directions could prove useful.
