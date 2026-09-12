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
section: "5"
section_title: Training
tag: "0022"
kind: section
lang: en
source: arxiv:1706.03762
pdf_sha256: bdfaa68d8984f0dc02beaca527b76f207d99b666d31d1da728ee0728182df697
pdf_pages: 7-8
extraction: native
extraction_model: pdftotext version 26.09.0
content_sha256: 1d91f43bf9fb0e70d49a73ae397f830aa8413939da2459fed12320715caa56cf
---

This section describes the training regime for our models.

### 5.1 Training Data and Batching {#vaswani-2017-attention-s5-1 .section tag=0023}

We trained on the standard WMT 2014 English-German dataset consisting of about 4.5 million sentence pairs. Sentences were encoded using byte-pair encoding [3], which has a shared sourcetarget vocabulary of about 37000 tokens. For English-French, we used the significantly larger WMT 2014 English-French dataset consisting of 36M sentences and split tokens into a 32000 word-piece vocabulary [38]. Sentence pairs were batched together by approximate sequence length. Each training batch contained a set of sentence pairs containing approximately 25000 source tokens and 25000 target tokens.

### 5.2 Hardware and Schedule {#vaswani-2017-attention-s5-2 .section tag=0024}

We trained our models on one machine with 8 NVIDIA P100 GPUs. For our base models using the hyperparameters described throughout the paper, each training step took about 0.4 seconds. We trained the base models for a total of 100,000 steps or 12 hours. For our big models,(described on the bottom line of table 3), step time was 1.0 seconds. The big models were trained for 300,000 steps (3.5 days).

### 5.3 Optimizer {#vaswani-2017-attention-s5-3 .section tag=0025}

We used the Adam optimizer [20] with β = 0.9, β = 0.98 and ϵ = 10 −9 . We varied the learning

1 2 rate over the course of training, according to the formula:

−0.5 −0.5 −1.5 lrate = d model · min(step_num , step_num · warmup_steps ) (3)

This corresponds to increasing the learning rate linearly for the first warmup_steps training steps, and decreasing it thereafter proportionally to the inverse square root of the step number. We used warmup_steps = 4000.

### 5.4 Regularization {#vaswani-2017-attention-s5-4 .section tag=0026}

We employ three types of regularization during training:

Table 2: The Transformer achieves better BLEU scores than previous state-of-the-art models on the English-to-German and English-to-French newstest2014 tests at a fraction of the training cost. {#vaswani-2017-attention-tab-2 .table tag=0027}

BLEU Training Cost (FLOPs) Model

EN-DE EN-FR EN-DE EN-FR ByteNet [18] 23.75 Deep-Att + PosUnk [39] 39.2 1.0 · 10 20 GNMT + RL [38] 24.6 39.92 2.3 · 10 19 1.4 · 10 20 ConvS2S [9] 25.16 40.46 9.6 · 10 18 1.5 · 10 20 MoE [32] 26.03 40.56 2.0 · 10 19 1.2 · 10 20 Deep-Att + PosUnk Ensemble [39] 40.4 8.0 · 10 20 GNMT + RL Ensemble [38] 26.30 41.16 1.8 · 10 20 1.1 · 10 21 ConvS2S Ensemble [9] 26.36 41.29 7.7 · 10 19 1.2 · 10 21 Transformer (base model) 27.3 38.1 3.3 · 10 18 Transformer (big) 28.4 41.8 2.3 · 10 19

Residual Dropout We apply dropout [33] to the output of each sub-layer, before it is added to the sub-layer input and normalized. In addition, we apply dropout to the sums of the embeddings and the positional encodings in both the encoder and decoder stacks. For the base model, we use a rate of P drop = 0.1.

Label Smoothing During training, we employed label smoothing of value ϵ ls = 0.1 [36]. This hurts perplexity, as the model learns to be more unsure, but improves accuracy and BLEU score.
