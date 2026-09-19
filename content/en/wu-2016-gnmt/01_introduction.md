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
section: "1"
section_title: Introduction
tag: 08DB
kind: section
lang: en
source: arxiv:1609.08144
pdf_sha256: 285fb4323972464ba0be4f7c76a0db1a3cc196d5e44be542152f085d47fe5812
pdf_pages: 1-2
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 1864152040582c984ea22d5e94e62d192ae1f774454f0dad57ac1e81363db03c
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Neural Machine Translation (NMT) [[sutskever-2014-seq2seq]], [2] has recently been introduced as a promising approach with the potential of addressing many shortcomings of traditional machine translation systems. The strength of NMT lies in its ability to learn directly, in an end-to-end fashion, the mapping from input text to associated output text. Its architecture typically consists of two recurrent neural networks (RNNs), one to consume the input text sequence and one to generate translated output text. NMT is often accompanied by an attention mechanism [2] which helps it cope effectively with long input sequences.

An advantage of Neural Machine Translation is that it sidesteps many brittle design choices in traditional phrase-based machine translation [26]. In practice, however, NMT systems used to be worse in accuracy than phrase-based translation systems, especially when training on very large-scale datasets as used for the very best publicly available translation systems. Three inherent weaknesses of Neural Machine Translation are responsible for this gap: its slower training and inference speed, ineffectiveness in dealing with rare words, and sometimes failure to translate all words in the source sentence. Firstly, it generally takes a considerable amount of time and computational resources to train an NMT system on a large-scale translation dataset, thus slowing the rate of experimental turnaround time and innovation. For inference they are generally much slower than phrase-based systems due to the large number of parameters used. Secondly, NMT lacks robustness in translating rare words. Though this can be addressed in principle by training a “copy model” to mimic a traditional alignment model [31], or by using the attention mechanism to copy rare words [37], these approaches are both unreliable at scale, since the quality of the alignments varies across languages, and the latent alignments produced by the attention mechanism are unstable when the network is deep. Also, simple copying may not always be the best strategy to cope with rare words, for example when a transliteration is more appropriate. Finally, NMT systems sometimes produce output sentences that do not translate all parts of the input sentence – in other words, they fail to completely “cover” the input, which can result in surprising translations.

This work presents the design and implementation of GNMT, a production NMT system at Google, that aims to provide solutions to the above problems. In our implementation, the recurrent networks are Long Short-Term Memory (LSTM) RNNs [23, 17]. Our LSTM RNNs have 8 layers, with residual connections between layers to encourage gradient flow [[he-2016-resnet]]. For parallelism, we connect the attention from the bottom layer of the decoder network to the top layer of the encoder network. To improve inference time, we employ low-precision arithmetic for inference, which is further accelerated by special hardware (Google’s Tensor Processing Unit, or TPU). To effectively deal with rare words, we use sub-word units (also known as “wordpieces”) [35] for inputs and outputs in our system. Using wordpieces gives a good balance between the flexibility of single characters and the efficiency of full words for decoding, and also sidesteps the need for special treatment of unknown words. Our beam search technique includes a length normalization procedure to deal efficiently with the problem of comparing hypotheses of different lengths during decoding, and a coverage penalty to encourage the model to translate all of the provided input.

Our implementation is robust, and performs well on a range of datasets across many pairs of languages without the need for language-specific adjustments. Using the same implementation, we are able to achieve results comparable to or better than previous state-of-the-art systems on standard benchmarks, while delivering great improvements over Google’s phrase-based production translation system. Specifically, on WMT’14 English-to-French, our single model scores 38.95 BLEU, an improvement of 7.5 BLEU from a single model without an external alignment model reported in [31] and an improvement of 1.2 BLEU from a single model without an external alignment model reported in [45]. Our single model is also comparable to a single model in [45], while not making use of any alignment model as being used in [45]. Likewise on WMT’14 English-to-German, our single model scores 24.17 BLEU, which is 3.4 BLEU better than a previous competitive baseline [6]. On production data, our implementation is even more effective. Human evaluations show that GNMT has reduced translation errors by 60% compared to our previous phrase-based system on many pairs of languages: English ↔ French, English ↔ Spanish, and English ↔ Chinese. Additional experiments suggest the quality of the resulting translation system gets closer to that of average human translators.
