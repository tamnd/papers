---
paper: vaswani-2017-attention
title: Attention Is All You Need
authors:
  - Ashish Vaswani
  - Noam Shazeer
  - Niki Parmar
  - Jakob Uszkoreit
  - Llion Jones
  - Aidan N. Gomez
  - Lukasz Kaiser
  - Illia Polosukhin
year: 2017
venue: NIPS
field: ai-ml
section: "7"
section_title: Conclusion
tag: 002E
kind: section
lang: en
source: arxiv:1706.03762
pdf_sha256: bdfaa68d8984f0dc02beaca527b76f207d99b666d31d1da728ee0728182df697
pdf_pages: "10"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: e103bacaaf679b0b26f73970ac83cb8a25055f4e6a48b29ded835bb5c89c3647
edited: true
prompt_sha256: 329630a0b9175a55e4af1b8e281a3e67eeab250f8d643953b7dcde99743c7628
---

In this work, we presented the Transformer, the first sequence transduction model based entirely on attention, replacing the recurrent layers most commonly used in encoder-decoder architectures with multi-headed self-attention.

For translation tasks, the Transformer can be trained significantly faster than architectures based on recurrent or convolutional layers. On both WMT 2014 English-to-German and WMT 2014 English-to-French translation tasks, we achieve a new state of the art. In the former task our best model outperforms even all previously reported ensembles.

We are excited about the future of attention-based models and plan to apply them to other tasks. We plan to extend the Transformer to problems involving input and output modalities other than text and to investigate local, restricted attention mechanisms to efficiently handle large inputs and outputs such as images, audio and video. Making generation less sequential is another research goals of ours.

The code we used to train and evaluate our models is available at https://github.com/tensorflow/tensor2tensor

**Acknowledgements** We are grateful to Nal Kalchbrenner and Stephan Gouws for their fruitful comments, corrections and inspiration.
