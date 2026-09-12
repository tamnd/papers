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
section_title: A Additional Details for BERT
kind: appendix
lang: en
source: arxiv:1810.04805
pdf_sha256: 5692a5514787a8c6727b4ff3b726a3385798bc68e12138d1d4af83947e2acf6e
pdf_pages: 12-13
extraction: vision
extraction_model: gpt-6-astra
content_sha256: 18de487aeb87fbb06e1ec57633147a4fe956b8e0c9e601f7c66bb4755ee25430
prompt_sha256: d53a8bfa14d5deec1eabb71e8a2ea2db8c42f516778942c09f3051aa50a9397f
---

### A.1 Illustration of the Pre-training Tasks {#devlin-2018-bert-s-a-1-illustration-of-the-pre-training-tasks .section tag=015E}

We provide examples of the pre-training tasks in the following.

**Masked LM and the Masking Procedure** Assuming the unlabeled sentence is

```text
my dog is hairy
```

, and during the random masking procedure we chose the 4-th token (which corresponding to

```text
hairy
```

), our masking procedure can be further illustrated by

- 80% of the time: Replace the word with the

  ```text
  [MASK]
  ```

token, e.g.,

  ```text
  my dog is hairy → my dog is [MASK]
  ```

- 10% of the time: Replace the word with a random word, e.g.,

  ```text
  my dog is hairy → my dog is apple
  ```

- 10% of the time: Keep the word unchanged, e.g.,

  ```text
  my dog is hairy → my dog is hairy
  ```

. The purpose of this is to bias the representation towards the actual observed word.

The advantage of this procedure is that the Transformer encoder does not know which words it will be asked to predict or which have been replaced by random words, so it is forced to keep a distributional contextual representation of *every* input token. Additionally, because random replacement only occurs for 1.5% of all tokens (i.e., 10% of 15%), this does not seem to harm the model’s language understanding capability. In Section C.2, we evaluate the impact this procedure.

Compared to standard language model training, the masked LM only make predictions on 15% of tokens in each batch, which suggests that more pre-training steps may be required for the model

Figure 3: Differences in pre-training model architectures. BERT uses a bidirectional Transformer. OpenAI GPT uses a left-to-right Transformer. ELMo uses the concatenation of independently trained left-to-right and right-to-left LSTMs to generate features for downstream tasks. Among the three, only BERT representations are jointly conditioned on both left and right context in all layers. In addition to the architecture differences, BERT and OpenAI GPT are fine-tuning approaches, while ELMo is a feature-based approach. {#devlin-2018-bert-fig-3 .figure tag=0144}

to converge. In Section C.1 we demonstrate that the MLM does converge marginally slower than a left-to-right model (which predicts every token), but the empirical improvements of the MLM model far outweigh the increased training cost.

**Next Sentence Prediction** The next sentence prediction task can be illustrated in the following examples.

```text
Input = [CLS] the man went to [MASK] store [SEP]
        he bought a gallon [MASK] milk [SEP]
Label = IsNext
```

```text
Input = [CLS] the man [MASK] to the store [SEP]
        penguin [MASK] are flight ##less birds [SEP]
Label = NotNext
```
