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
section: "2"
section_title: Related Work
tag: 08DC
kind: section
lang: en
source: arxiv:1609.08144
pdf_sha256: 285fb4323972464ba0be4f7c76a0db1a3cc196d5e44be542152f085d47fe5812
pdf_pages: 2-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 874bcfd2eb6813b5f5cfc37017de7f7465da61c20dd9b77668b07d3ef3e3ede4
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Statistical Machine Translation (SMT) has been the dominant translation paradigm for decades [3, 4, 5]. Practical implementations of SMT are generally phrase-based systems (PBMT) which translate sequences of words or phrases where the lengths may differ [26].

Even prior to the advent of direct Neural Machine Translation, neural networks have been used as a component within SMT systems with some success. Perhaps one of the most notable attempts involved the use of a joint language model to learn phrase representations [13] which yielded an impressive improvement when combined with phrase-based translation. This approach, however, still makes use of phrase-based translation systems at its core, and therefore inherits their shortcomings. Other proposed approaches for learning phrase representations [7] or learning end-to-end translation with neural networks [24] offered encouraging hints, but ultimately delivered worse overall accuracy compared to standard phrase-based systems.

The concept of end-to-end learning for machine translation has been attempted in the past (e.g., [8]) with limited success. Following seminal papers in the area [[sutskever-2014-seq2seq]] [2], NMT translation quality has crept closer to the level of phrase-based translation systems for common research benchmarks. Perhaps the first successful attempt at surpassing phrase-based translation was described in [31]. On WMT’14 English-to-French, this system achieved a 0.5 BLEU improvement compared to a state-of-the-art phrase-based system.

Since then, many novel techniques have been proposed to further improve NMT: using an attention mechanism to deal with rare words [37], a mechanism to model translation coverage [42], multi-task and semi-supervised training to incorporate more data [14, 29], a character decoder [9], a character encoder [11], subword units [38] also to deal with rare word outputs, different kinds of attention mechanisms [30], and sentence-level loss minimization [39, 34]. While the translation accuracy of these systems has been encouraging, systematic comparison with large scale, production quality phrase-based translation systems has been lacking.
