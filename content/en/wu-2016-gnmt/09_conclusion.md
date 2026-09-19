---
paper: wu-2016-gnmt
title: 'Google''s Neural Machine Translation System: Bridging the Gap between Human and Machine Translation'
authors:
  - Yonghui Wu
  - Mike Schuster
  - Zhifeng Chen
  - Quoc V. Le
  - Mohammad Norouzi
  - Wolfgang Macherey
  - Maxim Krikun
  - Yuan Cao
  - Qin Gao
  - Klaus Macherey
  - Jeff Klingner
  - Apurva Shah
  - Melvin Johnson
  - Xiaobing Liu
  - Łukasz Kaiser
  - Stephan Gouws
  - Yoshikiyo Kato
  - Taku Kudo
  - Hideto Kazawa
  - Keith Stevens
  - George Kurian
  - Nishant Patil
  - Wei Wang
  - Cliff Young
  - Jason Smith
  - Jason Riesa
  - Alex Rudnick
  - Oriol Vinyals
  - Greg Corrado
  - Macduff Hughes
  - Jeffrey Dean
year: 2016
venue: arXiv
field: ai-ml
section: "9"
section_title: Conclusion
tag: 08EF
kind: section
lang: en
source: arxiv:1609.08144
pdf_sha256: 285fb4323972464ba0be4f7c76a0db1a3cc196d5e44be542152f085d47fe5812
pdf_pages: "20"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 08f2c1912a41aa407bab4da9018bc3bd93624b6d2150620027756bed7bf6d7ab
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

In this paper, we describe in detail the implementation of Google’s Neural Machine Translation (GNMT) system, including all the techniques that are critical to its accuracy, speed, and robustness. On the public WMT’14 translation benchmark, our system’s translation quality approaches or surpasses all currently published results. More importantly, we also show that our approach carries over to much larger production data sets, which have several orders of magnitude more data, to deliver high quality translations.

Our key findings are: 1) that wordpiece modeling effectively handles open vocabularies and the challenge of morphologically rich languages for translation quality and inference speed, 2) that a combination of model and data parallelism can be used to efficiently train state-of-the-art sequence-to-sequence NMT models in roughly a week, 3) that model quantization drastically accelerates translation inference, allowing the use of these large models in a deployed production environment, and 4) that many additional details like length-normalization, coverage penalties, and similar are essential to making NMT systems work well on real data.

Using human-rated side-by-side comparison as a metric, we show that our GNMT system approaches the accuracy achieved by average bilingual human translators on some of our test sets. In particular, compared to the previous phrase-based production system, this GNMT system delivers roughly a 60% reduction in translation errors on several popular language pairs.
