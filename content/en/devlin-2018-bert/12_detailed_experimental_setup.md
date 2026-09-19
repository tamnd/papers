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
section: B
section_title: Detailed Experimental Setup
tag: 01A6
kind: appendix
lang: en
source: arxiv:1810.04805
pdf_sha256: 5692a5514787a8c6727b4ff3b726a3385798bc68e12138d1d4af83947e2acf6e
pdf_pages: 14-16
extraction: vision
extraction_model: gpt-6-astra
content_sha256: 6f1f2df0d2a385ac0ca0d1e1b94b6b070823d5869766441d4d187c6e9a612541
edited: true
prompt_sha256: d53a8bfa14d5deec1eabb71e8a2ea2db8c42f516778942c09f3051aa50a9397f
---

### B.1 Detailed Descriptions for the GLUE Benchmark Experiments. {#devlin-2018-bert-s-b-1-detailed-descriptions-for-the-glue-benchmark-experiments .section tag=0164}

Our GLUE results in Table1 are obtained from https://gluebenchmark.com/leaderboard and https://blog.openai.com/language-unsupervised. The GLUE benchmark includes the following datasets, the descriptions of which were originally summarized in Wang et al. (2018a):

**MNLI** Multi-Genre Natural Language Inference is a large-scale, crowdsourced entailment classification task (Williams et al., 2018). Given a pair of sentences, the goal is to predict whether the second sentence is an *entailment*, *contradiction*, or *neutral* with respect to the first one.

**QQP** Quora Question Pairs is a binary classification task where the goal is to determine if two questions asked on Quora are semantically equivalent (Chen et al., 2018).

**QNLI** Question Natural Language Inference is a version of the Stanford Question Answering Dataset (Rajpurkar et al., 2016) which has been converted to a binary classification task (Wang et al., 2018a). The positive examples are (question, sentence) pairs which do contain the correct answer, and the negative examples are (question, sentence) from the same paragraph which do not contain the answer.

Figure 4: Illustrations of Fine-tuning BERT on Different Tasks. {#devlin-2018-bert-fig-4 .figure tag=0145}

**SST-2** The Stanford Sentiment Treebank is a binary single-sentence classification task consisting of sentences extracted from movie reviews with human annotations of their sentiment (Socher et al., 2013).

**CoLA** The Corpus of Linguistic Acceptability is a binary single-sentence classification task, where the goal is to predict whether an English sentence is linguistically “acceptable” or not (Warstadt et al., 2018).

**STS-B** The Semantic Textual Similarity Benchmark is a collection of sentence pairs drawn from news headlines and other sources (Cer et al., 2017). They were annotated with a score from 1 to 5 denoting how similar the two sentences are in terms of semantic meaning.

**MRPC** Microsoft Research Paraphrase Corpus consists of sentence pairs automatically extracted from online news sources, with human annotations for whether the sentences in the pair are semantically equivalent (Dolan and Brockett, 2005).

**RTE** Recognizing Textual Entailment is a binary entailment task similar to MNLI, but with much less training data (Bentivogli et al., 2009).[^1]

**WNLI** Winograd NLI is a small natural language inference dataset (Levesque et al., 2011). The GLUE webpage notes that there are issues with the construction of this dataset,[^2] and every trained system that’s been submitted to GLUE has performed worse than the 65.1 baseline accuracy of predicting the majority class. We therefore exclude this set to be fair to OpenAI GPT. For our GLUE submission, we always predicted the majority class.

[^1]: Note that we only report single-task fine-tuning results in this paper. A multitask fine-tuning approach could potentially push the performance even further. For example, we did observe substantial improvements on RTE from multi-task training with MNLI.
[^2]: https://gluebenchmark.com/faq
