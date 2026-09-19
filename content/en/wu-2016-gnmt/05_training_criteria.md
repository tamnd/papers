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
section: "5"
section_title: Training Criteria
tag: "0960"
kind: section
lang: en
source: arxiv:1609.08144
pdf_sha256: 285fb4323972464ba0be4f7c76a0db1a3cc196d5e44be542152f085d47fe5812
pdf_pages: 8-9
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: db69cc09e7f634f411ad445543525ded81b301b13449d41522bfcbf8bbbf516c
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Given a dataset of parallel text containing $N$ input-output sequence pairs, denoted $\mathcal{D} \equiv \{ (X^{(i)}, Y^{*(i)}) \}_{i=1}^N$, standard maximum-likelihood training aims at maximizing the sum of log probabilities of the ground-truth outputs given the corresponding inputs,

$$
\mathcal{O}_{ML}(\theta) = \sum_{i=1}^N \log P_\theta(Y^{*(i)} \mid X^{(i)}) .
$$

The main problem with this objective is that it does not reflect the task reward function as measured by the BLEU score in translation. Further, this objective does not explicitly encourage a ranking among incorrect output sequences – where outputs with higher BLEU scores should still obtain higher probabilities under the model – since incorrect outputs are never observed during training. In other words, using maximum-likelihood training only, the model will not learn to be robust to errors made during decoding since they are never observed, which is quite a mismatch between the training and testing procedure.

Several recent papers [34, 39, 32] have considered different ways of incorporating the task reward into optimization of neural sequence-to-sequence models. In this work, we also attempt to refine a model pre-trained on the maximum likelihood objective to directly optimize for the task reward. We show that, even on large datasets, refinement of state-of-the-art maximum-likelihood models using task reward improves the results considerably.

We consider model refinement using the expected reward objective (also used in [34]), which can be expressed as

$$
\mathcal{O}_{RL}(\theta) = \sum_{i=1}^N \sum_{Y \in \mathcal{Y}} P_\theta(Y \mid X^{(i)}) \ r(Y, Y^{*(i)}).
$$

Here, $r(Y, Y^{*(i)})$ denotes the per-sentence score, and we are computing an expectation over all of the output sentences $Y$, up to a certain length.

The BLEU score has some undesirable properties when used for single sentences, as it was designed to be a corpus measure. We therefore use a slightly different score for our RL experiments which we call the “GLEU score”. For the GLEU score, we record all sub-sequences of 1, 2, 3 or 4 tokens in output and target sequence (n-grams). We then compute a recall, which is the ratio of the number of matching n-grams to the number of total n-grams in the target (ground truth) sequence, and a precision, which is the ratio of the number of matching n-grams to the number of total n-grams in the generated output sequence. Then GLEU score is simply the minimum of recall and precision. This GLEU score’s range is always between 0 (no matches) and 1 (all match) and it is symmetrical when switching output and target. According to our experiments, GLEU score correlates quite well with the BLEU metric on a corpus level but does not have its drawbacks for our per sentence reward objective.

As is common practice in reinforcement learning, we subtract the mean reward from $r(Y, Y^{*(i)})$ in equation 8. The mean is estimated to be the sample mean of $m$ sequences drawn independently from distribution $P_\theta(Y | X^{(i)})$. In our implementation, $m$ is set to be 15. To further stabilize training, we optimize a linear combination of ML (equation 7) and RL (equation 8) objectives as follows:

$$
\mathcal{O}_{\text{Mixed}}(\boldsymbol{\theta}) = \alpha * \mathcal{O}_{\text{ML}}(\boldsymbol{\theta}) + \mathcal{O}_{\text{RL}}(\boldsymbol{\theta})
$$

$\alpha$ in our implementation is typically set to be 0.017.

In our setup, we first train a model using the maximum likelihood objective (equation 7) until convergence. We then refine this model using a mixed maximum likelihood and expected reward objective (equation 9), until BLEU score on a development set is no longer improving. The second step is optional.
