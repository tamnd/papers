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
section: "4"
section_title: Segmentation Approaches
tag: "08E4"
kind: section
lang: en
source: arxiv:1609.08144
pdf_sha256: 285fb4323972464ba0be4f7c76a0db1a3cc196d5e44be542152f085d47fe5812
pdf_pages: 7-8
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 7e14daa4f1583cc909a5bee65b5561385b49d8b99ea7f38ce4b0b409d3f29c81
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Neural Machine Translation models often operate with fixed word vocabularies even though translation is fundamentally an open vocabulary problem (names, numbers, dates etc.). There are two broad categories of approaches to address the translation of out-of-vocabulary (OOV) words. One approach is to simply copy rare words from source to target (as most rare words are names or numbers where the correct translation is just a copy), either based on the attention model [37], using an external alignment model [31], or even using a more complicated special purpose pointing network [18]. Another broad category of approaches is to use sub-word units, e.g., chararacters [10], mixed word/characters [28], or more intelligent sub-words [38].

### 4.1 Wordpiece Model {#wu-2016-gnmt-s4-1 .section tag=08E5}

Our most successful approach falls into the second category (sub-word units), and we adopt the wordpiece model (WPM) implementation initially developed to solve a Japanese/Korean segmentation problem for the Google speech recognition system [35]. This approach is completely data-driven and guaranteed to generate a deterministic segmentation for any possible sequence of characters. It is similar to the method used in [38] to deal with rare words in Neural Machine Translation.

For processing arbitrary words, we first break words into wordpieces given a trained wordpiece model. Special word boundary symbols are added before training of the model such that the original word sequence can be recovered from the wordpiece sequence without ambiguity. At decoding time, the model first produces a wordpiece sequence, which is then converted into the corresponding word sequence.

Here is an example of a word sequence and the corresponding wordpiece sequence:

• Word: Jet makers feud over seat width with big orders at stake

• wordpieces: _J et _makers _fe ud _over _seat _width _with _big _orders _at _stake

In the above example, the word “Jet” is broken into two wordpieces “_J” and “et”, and the word “feud” is broken into two wordpieces “_fe” and “ud”. The other words remain as single wordpieces. “_” is a special character added to mark the beginning of a word.

The wordpiece model is generated using a data-driven approach to maximize the language-model likelihood of the training data, given an evolving word definition. Given a training corpus and a number of desired tokens $D$, the optimization problem is to select $D$ wordpieces such that the resulting corpus is minimal in the number of wordpieces when segmented according to the chosen wordpiece model. Our greedy algorithm to this optimization problem is similar to [38] and is described in more detail in [35]. Compared to the original implementation used in [35], we use a special symbol only at the beginning of the words and not at both ends. We also cut the number of basic characters to a manageable number depending on the data (roughly 500 for Western languages, more for Asian languages) and map the rest to a special unknown character to avoid polluting the given wordpiece vocabulary with very rare characters. We find that using a total vocabulary of between 8k and 32k wordpieces achieves both good accuracy (BLEU scores) and fast decoding speed across all pairs of language pairs we have tried.

As mentioned above, in translation it often makes sense to copy rare entity names or numbers directly from the source to the target. To facilitate this type of direct copying, we always use a shared wordpiece model for both the source language and target language. Using this approach, it is guaranteed that the same string in source and target sentence will be segmented in exactly the same way, making it easier for the system to learn to copy these tokens.

Wordpieces achieve a balance between the flexibility of characters and efficiency of words. We also find that our models get better overall BLEU scores when using wordpieces – possibly due to the fact that our models now deal efficiently with an essentially infinite vocabulary without resorting to characters only. The latter would make the average lengths of the input and output sequences much longer, and therefore would require more computation.

### 4.2 Mixed Word/Character Model {#wu-2016-gnmt-s4-2 .section tag=095F}

A second approach we use is the mixed word/character model. As in a word model, we keep a fixed-size word vocabulary. However, unlike in a conventional word model where OOV words are collapsed into a single UNK symbol, we convert OOV words into the sequence of its constituent characters. Special prefixes are prepended to the characters, to 1) show the location of the characters in a word, and 2) to distinguish them from normal in-vocabulary characters. There are three prefixes: <B>,<M>, and <E>, indicating beginning of the word, middle of the word and end of the word, respectively. For example, let’s assume the word Miki is not in the vocabulary. It will be preprocessed into a sequence of special tokens: <B>M <M>i <M>k <E>i. The process is done on both the source and the target sentences. During decoding, the output may also contain sequences of special tokens. With the prefixes, it is trivial to reverse the tokenization to the original words as part of a post-processing step.
