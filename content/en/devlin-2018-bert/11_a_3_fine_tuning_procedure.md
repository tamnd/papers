---
paper: devlin-2018-bert
title: 'BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding'
authors:
  - Jacob Devlin
  - Ming-Wei Chang
  - Kenton Lee
  - Kristina Toutanova
year: 2018
venue: NAACL
field: ai-ml
section_title: A.3 Fine-tuning Procedure
kind: appendix
lang: en
source: arxiv:1810.04805
pdf_sha256: 5692a5514787a8c6727b4ff3b726a3385798bc68e12138d1d4af83947e2acf6e
pdf_pages: 13-14
extraction: vision
extraction_model: gpt-6-astra
content_sha256: 1280f6ec37caafc4ae3897c22b869fe58ece332ceb8ceddaf9104c2170302947
prompt_sha256: d53a8bfa14d5deec1eabb71e8a2ea2db8c42f516778942c09f3051aa50a9397f
---

For fine-tuning, most model hyperparameters are the same as in pre-training, with the exception of the batch size, learning rate, and number of training epochs. The dropout probability was always kept at 0.1. The optimal hyperparameter values are task-specific, but we found the following range of possible values to work well across all tasks:

- **Batch size:** 16, 32

[^1]: https://cloudplatform.googleblog.com/2018/06/Cloud-TPU-now-offers-preemptible-pricing-and-global-availability.html

- **Learning rate (Adam):** 5e-5, 3e-5, 2e-5
- **Number of epochs:** 2, 3, 4

We also observed that large data sets (e.g., 100k+ labeled training examples) were far less sensitive to hyperparameter choice than small data sets. Fine-tuning is typically very fast, so it is reasonable to simply run an exhaustive search over the above parameters and choose the model that performs best on the development set.

### A.4 Comparison of BERT, ELMo ,and OpenAI GPT {#devlin-2018-bert-s-a-4-comparison-of-bert-elmo-and-openai-gpt .section tag=0161}

Here we studies the differences in recent popular representation learning models including ELMo, OpenAI GPT and BERT. The comparisons between the model architectures are shown visually in Figure 3. Note that in addition to the architecture differences, BERT and OpenAI GPT are fine-tuning approaches, while ELMo is a feature-based approach.

The most comparable existing pre-training method to BERT is OpenAI GPT, which trains a left-to-right Transformer LM on a large text corpus. In fact, many of the design decisions in BERT were intentionally made to make it as close to GPT as possible so that the two methods could be minimally compared. The core argument of this work is that the bi-directionality and the two pre-training tasks presented in Section 3.1 account for the majority of the empirical improvements, but we do note that there are several other differences between how BERT and GPT were trained:

- GPT is trained on the BooksCorpus (800M words); BERT is trained on the BooksCorpus (800M words) and Wikipedia (2,500M words).
- GPT uses a sentence separator ([SEP]) and classifier token ([CLS]) which are only introduced at fine-tuning time; BERT learns [SEP], [CLS] and sentence A/B embeddings during pre-training.
- GPT was trained for 1M steps with a batch size of 32,000 words; BERT was trained for 1M steps with a batch size of 128,000 words.
- GPT used the same learning rate of 5e-5 for all fine-tuning experiments; BERT chooses a task-specific fine-tuning learning rate which performs the best on the development set.

To isolate the effect of these differences, we perform ablation experiments in Section 5.1 which demonstrate that the majority of the improvements are in fact coming from the two pre-training tasks and the bidirectionality they enable.

### A.5 Illustrations of Fine-tuning on Different Tasks {#devlin-2018-bert-s-a-5-illustrations-of-fine-tuning-on-different-tasks .section tag=0162}

The illustration of fine-tuning BERT on different tasks can be seen in Figure 4. Our task-specific models are formed by incorporating BERT with one additional output layer, so a minimal number of parameters need to be learned from scratch. Among the tasks, (a) and (b) are sequence-level tasks while (c) and (d) are token-level tasks. In the figure, $E$ represents the input embedding, $T_i$ represents the contextual representation of token $i$, [CLS] is the special symbol for classification output, and [SEP] is the special symbol to separate non-consecutive token sequences.
