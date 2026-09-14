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
section: C
section_title: Additional Ablation Studies
tag: 01A7
kind: appendix
lang: en
source: arxiv:1810.04805
pdf_sha256: 5692a5514787a8c6727b4ff3b726a3385798bc68e12138d1d4af83947e2acf6e
pdf_pages: "16"
extraction: vision
extraction_model: gpt-6-astra
content_sha256: 82f25362e31025dbd6c2ed6cad12aa9180210c7cb807b845d915f9d2e0f628ac
prompt_sha256: d53a8bfa14d5deec1eabb71e8a2ea2db8c42f516778942c09f3051aa50a9397f
---

### C.1 Effect of Number of Training Steps {#devlin-2018-bert-s-c-1-effect-of-number-of-training-steps .section tag=0166}

Figure 5 presents MNLI Dev accuracy after fine-tuning from a checkpoint that has been pre-trained for $k$ steps. This allows us to answer the following questions:

1. Question: Does BERT really need such a large amount of pre-training (128,000 words/batch * 1,000,000 steps) to achieve high fine-tuning accuracy?

Answer: Yes, $\mathrm{BERT}_{\mathrm{BASE}}$ achieves almost 1.0% additional accuracy on MNLI when trained on 1M steps compared to 500k steps.

2. Question: Does MLM pre-training converge slower than LTR pre-training, since only 15% of words are predicted in each batch rather than every word?

Answer: The MLM model does converge slightly slower than the LTR model. However, in terms of absolute accuracy the MLM model begins to outperform the LTR model almost immediately.

### C.2 Ablation for Different Masking Procedures {#devlin-2018-bert-s-c-2-ablation-for-different-masking-procedures .section tag=0167}

In Section 3.1, we mention that BERT uses a mixed strategy for masking the target tokens when pre-training with the masked language model (MLM) objective. The following is an ablation study to evaluate the effect of different masking strategies.

Figure 5: Ablation over number of training steps. This shows the MNLI accuracy after fine-tuning, starting from model parameters that have been pre-trained for $k$ steps. The x-axis is the value of $k$. {#devlin-2018-bert-fig-5 .figure tag=0146}

Note that the purpose of the masking strategies is to reduce the mismatch between pre-training and fine-tuning, as the [MASK] symbol never appears during the fine-tuning stage. We report the Dev results for both MNLI and NER. For NER, we report both fine-tuning and feature-based approaches, as we expect the mismatch will be amplified for the feature-based approach as the model will not have the chance to adjust the representations.

```text
    Masking Rates                 Dev Set Results
─────────────────────   ─────────────────────────────────
MASK   SAME   RND        MNLI               NER
                       Fine-tune   Fine-tune Feature-based
─────────────────────  ─────────   ──────────────────────
 80%    10%    10%        84.2        95.4        94.9
100%     0%     0%        84.3        94.9        94.0
 80%     0%    20%        84.1        95.2        94.6
 80%    20%     0%        84.4        95.2        94.7
  0%    20%    80%        83.7        94.8        94.6
  0%     0%   100%        83.6        94.9        94.6
```

Table 8: Ablation over different masking strategies. {#devlin-2018-bert-tab-8 .table tag=0147}

The results are presented in Table 8. In the table, MASK means that we replace the target token with the [MASK] symbol for MLM; SAME means that we keep the target token as is; RND means that we replace the target token with another random token.

The numbers in the left part of the table represent the probabilities of the specific strategies used during MLM pre-training (BERT uses 80%, 10%, 10%). The right part of the paper represents the Dev set results. For the feature-based approach, we concatenate the last 4 layers of BERT as the features, which was shown to be the best approach in Section 5.3.

From the table it can be seen that fine-tuning is surprisingly robust to different masking strategies. However, as expected, using only the MASK strategy was problematic when applying the feature-based approach to NER. Interestingly, using only the RND strategy performs much worse than our strategy as well.
