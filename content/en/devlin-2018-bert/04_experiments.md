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
section: "4"
section_title: Experiments
tag: 013C
kind: section
lang: en
source: arxiv:1810.04805
pdf_sha256: 5692a5514787a8c6727b4ff3b726a3385798bc68e12138d1d4af83947e2acf6e
pdf_pages: 5-7
extraction: vision
extraction_model: gpt-6-astra
content_sha256: b104c30c89a128ae5db4f88fe20faadcee0f6c4eee194dd1e69c3560711048e7
prompt_sha256: d53a8bfa14d5deec1eabb71e8a2ea2db8c42f516778942c09f3051aa50a9397f
---

In this section, we present BERT fine-tuning results on 11 NLP tasks.

### 4.1 GLUE {#devlin-2018-bert-s4-1 .section tag=013D}

The General Language Understanding Evaluation (GLUE) benchmark (Wang et al., 2018a) is a collection of diverse natural language understanding tasks. Detailed descriptions of GLUE datasets are included in Appendix B.1.

To fine-tune on GLUE, we represent the input sequence (for single sentence or sentence pairs) as described in Section 3, and use the final hidden vector $C \in \mathbb{R}^H$ corresponding to the first input token ([CLS]) as the aggregate representation. The only new parameters introduced during fine-tuning are classification layer weights $W \in \mathbb{R}^{K \times H}$, where $K$ is the number of labels. We compute a standard classification loss with $C$ and $W$, i.e., $\log(\operatorname{softmax}(CW^T))$.

[^1]: For example, the BERT SQuAD model can be trained in around 30 minutes on a single Cloud TPU to achieve a Dev F1 score of 91.0%.
[^2]: See (10) in https://gluebenchmark.com/faq.

| System | MNLI-(m/mm) | QQP | QNLI | SST-2 | CoLA | STS-B | MRPC | RTE | **Average** |
|---|---|---|---|---|---|---|---|---|---|
| | 392k | 363k | 108k | 67k | 8.5k | 5.7k | 3.5k | 2.5k | - |
| Pre-OpenAI SOTA | 80.6/80.1 | 66.1 | 82.3 | 93.2 | 35.0 | 81.0 | 86.0 | 61.7 | 74.0 |
| BiLSTM+ELMo+Attn | 76.4/76.1 | 64.8 | 79.8 | 90.4 | 36.0 | 73.3 | 84.9 | 56.8 | 71.0 |
| OpenAI GPT | 82.1/81.4 | 70.3 | 87.4 | 91.3 | 45.4 | 80.0 | 82.3 | 56.0 | 75.1 |
| $\mathrm{BERT}_{\mathrm{BASE}}$ | 84.6/83.4 | 71.2 | 90.5 | 93.5 | 52.1 | 85.8 | 88.9 | 66.4 | 79.6 |
| $\mathrm{BERT}_{\mathrm{LARGE}}$ | **86.7/85.9** | **72.1** | **92.7** | **94.9** | **60.5** | **86.5** | **89.3** | **70.1** | **82.1** |

Table 1: GLUE Test results, scored by the evaluation server (https://gluebenchmark.com/leaderboard). The number below each task denotes the number of training examples. The “Average” column is slightly different than the official GLUE score, since we exclude the problematic WNLI set.[^1] BERT and OpenAI GPT are single-model, single task. F1 scores are reported for QQP and MRPC, Spearman correlations are reported for STS-B, and accuracy scores are reported for the other tasks. We exclude entries that use BERT as one of their components. {#devlin-2018-bert-tab-1 .table tag=013E}

We use a batch size of 32 and fine-tune for 3 epochs over the data for all GLUE tasks. For each task, we selected the best fine-tuning learning rate (among 5e-5, 4e-5, 3e-5, and 2e-5) on the Dev set. Additionally, for $\mathrm{BERT}_{\mathrm{LARGE}}$ we found that fine-tuning was sometimes unstable on small datasets, so we ran several random restarts and selected the best model on the Dev set. With random restarts, we use the same pre-trained checkpoint but perform different fine-tuning data shuffling and classifier layer initialization.[^2]

Results are presented in Table 1. Both $\mathrm{BERT}_{\mathrm{BASE}}$ and $\mathrm{BERT}_{\mathrm{LARGE}}$ outperform all systems on all tasks by a substantial margin, obtaining 4.5% and 7.0% respective average accuracy improvement over the prior state of the art. Note that $\mathrm{BERT}_{\mathrm{BASE}}$ and OpenAI GPT are nearly identical in terms of model architecture apart from the attention masking. For the largest and most widely reported GLUE task, MNLI, BERT obtains a 4.6% absolute accuracy improvement. On the official GLUE leaderboard[^3], $\mathrm{BERT}_{\mathrm{LARGE}}$ obtains a score of 80.5, compared to OpenAI GPT, which obtains 72.8 as of the date of writing.

We find that $\mathrm{BERT}_{\mathrm{LARGE}}$ significantly outperforms $\mathrm{BERT}_{\mathrm{BASE}}$ across all tasks, especially those with very little training data. The effect of model size is explored more thoroughly in Section 5.2.

### 4.2 SQuAD v1.1 {#devlin-2018-bert-s4-2 .section tag=013F}

The Stanford Question Answering Dataset (SQuAD v1.1) is a collection of 100k crowd-sourced question/answer pairs (Rajpurkar et al., 2016). Given a question and a passage from Wikipedia containing the answer, the task is to predict the answer text span in the passage.

As shown in Figure 1, in the question answering task, we represent the input question and passage as a single packed sequence, with the question using the A embedding and the passage using the B embedding. We only introduce a start vector $S \in \mathbb{R}^H$ and an end vector $E \in \mathbb{R}^H$ during fine-tuning. The probability of word $i$ being the start of the answer span is computed as a dot product between $T_i$ and $S$ followed by a softmax over all of the words in the paragraph: $P_i = \frac{e^{S \cdot T_i}}{\sum_j e^{S \cdot T_j}}$. The analogous formula is used for the end of the answer span. The score of a candidate span from position $i$ to position $j$ is defined as $S \cdot T_i + E \cdot T_j$, and the maximum scoring span where $j \geq i$ is used as a prediction. The training objective is the sum of the log-likelihoods of the correct start and end positions. We fine-tune for 3 epochs with a learning rate of 5e-5 and a batch size of 32.

Table 2 shows top leaderboard entries as well as results from top published systems (Seo et al., 2017; Clark and Gardner, 2018; Peters et al., 2018a; Hu et al., 2018). The top results from the SQuAD leaderboard do not have up-to-date public system descriptions available,[^4] and are allowed to use any public data when training their systems. We therefore use modest data augmentation in our system by first fine-tuning on TriviaQA (Joshi et al., 2017) before fine-tuning on SQuAD.

Our best performing system outperforms the top leaderboard system by +1.5 F1 in ensembling and +1.3 F1 as a single system. In fact, our single BERT model outperforms the top ensemble system in terms of F1 score. Without TriviaQA fine-

[^2]: The GLUE data set distribution does not include the Test labels, and we only made a single GLUE evaluation server submission for each $\mathrm{BERT}_{\mathrm{BASE}}$ and $\mathrm{BERT}_{\mathrm{LARGE}}$.
[^3]: https://gluebenchmark.com/leaderboard
[^4]: QANet is described in Yu et al. (2018), but the system has improved substantially after publication.

```text
                              Dev         Test
System                     EM    F1    EM    F1
──────────────────────────────────────────────────
     Top Leaderboard Systems (Dec 10th, 2018)
Human                       -     -   82.3  91.2
#1 Ensemble - nlnet          -     -   86.0  91.7
#2 Ensemble - QANet          -     -   84.5  90.5
──────────────────────────────────────────────────
                     Published
BiDAF+ELMo (Single)          -   85.6    -   85.8
R.M. Reader (Ensemble)     81.2  87.9  82.3  88.5
──────────────────────────────────────────────────
                       Ours
BERTBASE (Single)          80.8  88.5    -     -
BERTLARGE (Single)         84.1  90.9    -     -
BERTLARGE (Ensemble)       85.8  91.8    -     -
BERTLARGE (Sgl.+TriviaQA)   84.2  91.1  85.1  91.8
BERTLARGE (Ens.+TriviaQA)   86.2  92.2  87.4  93.2
──────────────────────────────────────────────────
```

Table 2: SQuAD 1.1 results. The BERT ensemble is 7x systems which use different pre-training checkpoints and fine-tuning seeds. {#devlin-2018-bert-tab-2 .table tag=0153}

```text
                                  Dev         Test
System                         EM    F1    EM    F1
────────────────────────────────────────────────────
      Top Leaderboard Systems (Dec 10th, 2018)
Human                         86.3  89.0  86.9  89.5
#1 Single - MIR-MRC (F-Net)      -     -   74.8  78.0
#2 Single - nlnet               -     -   74.2  77.1
────────────────────────────────────────────────────
                       Published
unet (Ensemble)                -     -   71.4  74.9
SLQA+ (Single)                 -     -   71.4  74.4
────────────────────────────────────────────────────
                         Ours
BERTLARGE (Single)            78.7  81.9  80.0  83.1
────────────────────────────────────────────────────
```

Table 3: SQuAD 2.0 results. We exclude entries that use BERT as one of their components. {#devlin-2018-bert-tab-3 .table tag=0154}

tuning data, we only lose 0.1-0.4 F1, still outperforming all existing systems by a wide margin.[^1]

### 4.3 SQuAD v2.0 {#devlin-2018-bert-s4-3 .section tag=0155}

The SQuAD 2.0 task extends the SQuAD 1.1 problem definition by allowing for the possibility that no short answer exists in the provided paragraph, making the problem more realistic.

We use a simple approach to extend the SQuAD v1.1 BERT model for this task. We treat questions that do not have an answer as having an answer span with start and end at the [CLS] token. The probability space for the start and end answer span positions is extended to include the position of the [CLS] token. For prediction, we compare the score of the no-answer span: $s_{\mathrm{null}} = S \cdot C + E \cdot C$ to the score of the best non-null span

| System | Dev | Test |
|---|---|---|
| ESIM+GloVe | 51.9 | 52.7 |
| ESIM+ELMo | 59.1 | 59.2 |
| OpenAI GPT | - | 78.0 |
| BERT$_{\mathrm{BASE}}$ | 81.6 | - |
| BERT$_{\mathrm{LARGE}}$ | **86.6** | **86.3** |
| Human (expert)$^{\dagger}$ | - | 85.0 |
| Human (5 annotations)$^{\dagger}$ | - | 88.0 |

Table 4: SWAG Dev and Test accuracies. $^{\dagger}$Human performance is measured with 100 samples, as reported in the SWAG paper. {#devlin-2018-bert-tab-4 .table tag=0157}

$\hat{s}_{i,j} = \max_{j \geq i} S \cdot T_i + E \cdot T_j$. We predict a non-null answer when $\hat{s}_{i,j} > s_{\mathrm{null}} + \tau$, where the threshold $\tau$ is selected on the dev set to maximize F1. We did not use TriviaQA data for this model. We fine-tuned for 2 epochs with a learning rate of 5e-5 and a batch size of 48.

The results compared to prior leaderboard entries and top published work (Sun et al., 2018; Wang et al., 2018b) are shown in Table 3, excluding systems that use BERT as one of their components. We observe a +5.1 F1 improvement over the previous best system.

### 4.4 SWAG {#devlin-2018-bert-s4-4 .section tag=0156}

The Situations With Adversarial Generations (SWAG) dataset contains 113k sentence-pair completion examples that evaluate grounded commonsense inference (Zellers et al., 2018). Given a sentence, the task is to choose the most plausible continuation among four choices.

When fine-tuning on the SWAG dataset, we construct four input sequences, each containing the concatenation of the given sentence (sentence A) and a possible continuation (sentence B). The only task-specific parameters introduced is a vector whose dot product with the [CLS] token representation $C$ denotes a score for each choice which is normalized with a softmax layer.

We fine-tune the model for 3 epochs with a learning rate of 2e-5 and a batch size of 16. Results are presented in Table 4. BERT$_{\mathrm{LARGE}}$ outperforms the authors’ baseline ESIM+ELMo system by +27.1% and OpenAI GPT by 8.3%.
