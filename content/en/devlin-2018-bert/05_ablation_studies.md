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
section: "5"
section_title: Ablation Studies
tag: "0158"
kind: section
lang: en
source: arxiv:1810.04805
pdf_sha256: 5692a5514787a8c6727b4ff3b726a3385798bc68e12138d1d4af83947e2acf6e
pdf_pages: 7-9
extraction: vision
extraction_model: gpt-6-astra
content_sha256: 9e2933a8f90bea8747a337586900853298d9b7ee1dd80b1aa7cd7d1f31a4839c
prompt_sha256: d53a8bfa14d5deec1eabb71e8a2ea2db8c42f516778942c09f3051aa50a9397f
---

In this section, we perform ablation experiments over a number of facets of BERT in order to better understand their relative importance. Additional

[^1]: The TriviaQA data we used consists of paragraphs from TriviaQA-Wiki formed of the first 400 tokens in documents, that contain at least one of the provided possible answers.

```text
                                      Dev Set
Tasks             MNLI-m   QNLI   MRPC   SST-2   SQuAD
                   (Acc)   (Acc)  (Acc)  (Acc)   (F1)
BERTBASE            84.4    88.4   86.7   92.7    88.5
No NSP              83.9    84.9   86.5   92.6    87.9
LTR & No NSP        82.1    84.3   77.5   92.1    77.8
  + BiLSTM          82.1    84.1   75.7   91.6    84.9
```

Table 5: Ablation over the pre-training tasks using the BERTʙᴀꜱᴇ architecture. “No NSP” is trained without the next sentence prediction task. “LTR & No NSP” is trained as a left-to-right LM without the next sentence prediction, like OpenAI GPT. “+ BiLSTM” adds a randomly initialized BiLSTM on top of the “LTR + No NSP” model during fine-tuning. {#devlin-2018-bert-tab-5 .table tag=0140}

ablation studies can be found in Appendix C.

### 5.1 Effect of Pre-training Tasks {#devlin-2018-bert-s5-1 .section tag=0159}

We demonstrate the importance of the deep bidirectionality of BERT by evaluating two pre-training objectives using exactly the same pre-training data, fine-tuning scheme, and hyperparameters as BERTʙᴀꜱᴇ:

**No NSP:** A bidirectional model which is trained using the “masked LM” (MLM) but without the “next sentence prediction” (NSP) task.

**LTR & No NSP:** A left-context-only model which is trained using a standard Left-to-Right (LTR) LM, rather than an MLM. The left-only constraint was also applied at fine-tuning, because removing it introduced a pre-train/fine-tune mismatch that degraded downstream performance. Additionally, this model was pre-trained without the NSP task. This is directly comparable to OpenAI GPT, but using our larger training dataset, our input representation, and our fine-tuning scheme.

We first examine the impact brought by the NSP task. In Table 5, we show that removing NSP hurts performance significantly on QNLI, MNLI, and SQuAD 1.1. Next, we evaluate the impact of training bidirectional representations by comparing “No NSP” to “LTR & No NSP”. The LTR model performs worse than the MLM model on all tasks, with large drops on MRPC and SQuAD.

For SQuAD it is intuitively clear that a LTR model will perform poorly at token predictions, since the token-level hidden states have no right-side context. In order to make a good faith attempt at strengthening the LTR system, we added a randomly initialized BiLSTM on top. This does significantly improve results on SQuAD, but the results are still far worse than those of the pre-trained bidirectional models. The BiLSTM hurts performance on the GLUE tasks.

We recognize that it would also be possible to train separate LTR and RTL models and represent each token as the concatenation of the two models, as ELMo does. However: (a) this is twice as expensive as a single bidirectional model; (b) this is non-intuitive for tasks like QA, since the RTL model would not be able to condition the answer on the question; (c) this is strictly less powerful than a deep bidirectional model, since it can use both left and right context at every layer.

### 5.2 Effect of Model Size {#devlin-2018-bert-s5-2 .section tag=015A}

In this section, we explore the effect of model size on fine-tuning task accuracy. We trained a number of BERT models with a differing number of layers, hidden units, and attention heads, while otherwise using the same hyperparameters and training procedure as described previously.

Results on selected GLUE tasks are shown in Table 6. In this table, we report the average Dev Set accuracy from 5 random restarts of fine-tuning. We can see that larger models lead to a strict accuracy improvement across all four datasets, even for MRPC which only has 3,600 labeled training examples, and is substantially different from the pre-training tasks. It is also perhaps surprising that we are able to achieve such significant improvements on top of models which are already quite large relative to the existing literature. For example, the largest Transformer explored in Vaswani et al. (2017) is (L=6, H=1024, A=16) with 100M parameters for the encoder, and the largest Transformer we have found in the literature is (L=64, H=512, A=2) with 235M parameters (Al-Rfou et al., 2018). By contrast, BERTʙᴀꜱᴇ contains 110M parameters and BERTʟᴀʀɢᴇ contains 340M parameters.

It has long been known that increasing the model size will lead to continual improvements on large-scale tasks such as machine translation and language modeling, which is demonstrated by the LM perplexity of held-out training data shown in Table 6. However, we believe that this is the first work to demonstrate convincingly that scaling to extreme model sizes also leads to large improvements on very small scale tasks, provided that the model has been sufficiently pre-trained. Peters et al. (2018b) presented mixed results on the downstream task impact of increasing the pre-trained bi-LM size from two to four layers and Melamud et al. (2016) mentioned in passing that increasing hidden dimension size from 200 to 600 helped, but increasing further to 1,000 did not bring further improvements. Both of these prior works used a feature-based approach — we hypothesize that when the model is fine-tuned directly on the downstream tasks and uses only a very small number of randomly initialized additional parameters, the task-specific models can benefit from the larger, more expressive pre-trained representations even when downstream task data is very small.

### 5.3 Feature-based Approach with BERT {#devlin-2018-bert-s5-3 .section tag=015B}

All of the BERT results presented so far have used the fine-tuning approach, where a simple classification layer is added to the pre-trained model, and all parameters are jointly fine-tuned on a downstream task. However, the feature-based approach, where fixed features are extracted from the pre-trained model, has certain advantages. First, not all tasks can be easily represented by a Transformer encoder architecture, and therefore require a task-specific model architecture to be added. Second, there are major computational benefits to pre-compute an expensive representation of the training data once and then run many experiments with cheaper models on top of this representation.

In this section, we compare the two approaches by applying BERT to the CoNLL-2003 Named Entity Recognition (NER) task (Tjong Kim Sang and De Meulder, 2003). In the input to BERT, we use a case-preserving WordPiece model, and we include the maximal document context provided by the data. Following standard practice, we formulate this as a tagging task but do not use a CRF

```text
Hyperparams                  Dev Set Accuracy
#L   #H    #A   LM (ppl)   MNLI-m  MRPC  SST-2
 3   768   12     5.84      77.9   79.8   88.4
 6   768    3     5.24      80.6   82.2   90.7
 6   768   12     4.68      81.9   84.8   91.3
12   768   12     3.99      84.4   86.7   92.9
12  1024   16     3.54      85.7   86.9   93.3
24  1024   16     3.23      86.6   87.8   93.7
```

Table 6: Ablation over BERT model size. #L = the number of layers; #H = hidden size; #A = number of attention heads. “LM (ppl)” is the masked LM perplexity of held-out training data. {#devlin-2018-bert-tab-6 .table tag=0141}

| System | Dev F1 | Test F1 |
| --- | --- | --- |
| ELMo (Peters et al., 2018a) | 95.7 | 92.2 |
| CVT (Clark et al., 2018) | - | 92.6 |
| CSE (Akbik et al., 2018) | - | **93.1** |
| Fine-tuning approach | | |
| $\mathrm{BERT}_{\mathrm{LARGE}}$ | 96.6 | 92.8 |
| $\mathrm{BERT}_{\mathrm{BASE}}$ | 96.4 | 92.4 |
| Feature-based approach ($\mathrm{BERT}_{\mathrm{BASE}}$) | | |
| Embeddings | 91.0 | - |
| Second-to-Last Hidden | 95.6 | - |
| Last Hidden | 94.9 | - |
| Weighted Sum Last Four Hidden | 95.9 | - |
| Concat Last Four Hidden | 96.1 | - |
| Weighted Sum All 12 Layers | 95.5 | - |

Table 7: CoNLL-2003 Named Entity Recognition results. Hyperparameters were selected using the Dev set. The reported Dev and Test scores are averaged over 5 random restarts using those hyperparameters. {#devlin-2018-bert-tab-7 .table tag=0142}

layer in the output. We use the representation of the first sub-token as the input to the token-level classifier over the NER label set.

To ablate the fine-tuning approach, we apply the feature-based approach by extracting the activations from one or more layers *without* fine-tuning any parameters of BERT. These contextual embeddings are used as input to a randomly initialized two-layer 768-dimensional BiLSTM before the classification layer.

Results are presented in Table 7. $\mathrm{BERT}_{\mathrm{LARGE}}$ performs competitively with state-of-the-art methods. The best performing method concatenates the token representations from the top four hidden layers of the pre-trained Transformer, which is only 0.3 F1 behind fine-tuning the entire model. This demonstrates that BERT is effective for both fine-tuning and feature-based approaches.
