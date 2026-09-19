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
section: "7"
section_title: Decoder
tag: "0962"
kind: section
lang: en
source: arxiv:1609.08144
pdf_sha256: 285fb4323972464ba0be4f7c76a0db1a3cc196d5e44be542152f085d47fe5812
pdf_pages: 12-13
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: cd0ec98b8f9d66e5e7e8f5b28373ef89ede14216ebdc37be6e571e56024f92b4
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

We use beam search during decoding to find the sequence $Y$ that maximizes a score function $s(Y, X)$ given a trained model. We introduce two important refinements to the pure max-probability based beam search algorithm: a coverage penalty [42] and length normalization. With length normalization, we aim to account for the fact that we have to compare hypotheses of different length. Without some form of length-normalization regular beam search will favor shorter results over longer ones on average since a negative log-probability is added at each step, yielding lower (more negative) scores for longer sentences. We first tried to simply divide by the length to normalize. We then improved on that original heuristic by dividing by $length^\alpha$, with $0 < \alpha < 1$ where $\alpha$ is optimized on a development set ($\alpha \in [0.6 - 0.7]$ was usually found to be best). Eventually we designed the empirically-better scoring function below, which also includes a coverage penalty to favor translations that fully cover the source sentence according to the attention module.

More concretely, the scoring function $s(Y, X)$ that we employ to rank candidate translations is defined as follows:

$$
s(Y, X) = \log(P(Y|X))/lp(Y) + cp(X; Y)
$$

$$
lp(Y) = \frac{(5 + |Y|)^\alpha}{(5 + 1)^\alpha}
$$

$$
cp(X; Y) = \beta * \sum_{i=1}^{|X|} \log(\min(\sum_{j=1}^{|Y|} p_{i,j}, 1.0)),
$$

where $p_{i,j}$ is the attention probability of the $j$-th target word $y_j$ on the $i$-th source word $x_i$. By construction (equation 4), $\sum_{i=0}^{|X|} p_{i,j}$ is equal to 1. Parameters $\alpha$ and $\beta$ control the strength of the length normalization and the coverage penalty. When $\alpha = 0$ and $\beta = 0$, our decoder falls back to pure beam search by probability.

During beam search, we typically keep 8-12 hypotheses but we find that using fewer (4 or 2) has only slight negative effects on BLEU scores. Besides pruning the number of considered hypotheses, two other forms of pruning are used. Firstly, at each step, we only consider tokens that have local scores that are not more than $beamsize$ below the best token for this step. Secondly, after a normalized best score has been found according to equation 14, we prune all hypotheses that are more than $beamsize$ below the best normalized score so far. The latter type of pruning only applies to full hypotheses because it compares scores in the normalized space, which is only available when a hypothesis ends. This latter form of pruning also has the effect that very quickly no more hypotheses will be generated once a sufficiently good hypothesis has been found, so the search will end quickly. The pruning speeds up search by 30% – 40% when run on CPUs compared to not pruning (where we simply stop decoding after a predetermined maximum output length of twice the source length). Typically we use beamsize = 3.0, unless otherwise noted.

To improve throughput during decoding we can put many sentences (typically up to 35) of similar length into a batch and decode all of those in parallel to make use of available hardware optimized for parallel computations. In this case the beam search only finishes if all hypotheses for all sentences in the batch are out of beam, which is slightly less efficient theoretically, but in practice is of negligible additional computational cost.

| BLEU | α |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | 0.0 | 0.2 | 0.4 | 0.6 | 0.8 | 1.0 |
| 0.0 | 30.3 | 30.7 | 30.9 | 31.1 | 31.2 | 31.1 |
| 0.2 | 31.4 | 31.4 | 31.4 | 31.3 | 30.8 | 30.3 |
| 0.4 | 31.4 | 31.4 | 31.4 | 31.1 | 30.5 | 29.6 |
| 0.6 | 31.4 | 31.4 | 31.3 | 30.9 | 30.1 | 28.9 |
| 0.8 | 31.4 | 31.4 | 31.2 | 30.8 | 29.8 | 28.1 |
| 1.0 | 31.4 | 31.3 | 31.2 | 30.6 | 29.4 | 27.2 |

Table 2: WMT’14 En→Fr BLEU score with respect to different values of $\alpha$ and $\beta$. The model in this experiment trained using ML without RL refinement. A single WMT En→Fr model achieves a BLEU score of 30.3 on the development set when the beam search scoring function is purely based on the sequence probability (i.e., both $\alpha$ and $\beta$ are 0). Slightly larger $\alpha$ and $\beta$ values improve BLEU score by up to +1.1 ($\alpha = 0.2, \beta = 0.2$), with a wide range of $\alpha$ and $\beta$ values giving results very close to the best BLEU scores. {#wu-2016-gnmt-tab-2 .table tag=08E8}

Table 2 shows the impact of $\alpha$ and $\beta$ on the BLEU score when decoding the WMT’14 English-to-French development set. The model used here for experiments is trained using the ML objective only (without RL refinement). As can be seen from the results, having some length normalization and coverage penalty improves BLEU score considerably (from 30.3 to 31.4).

We find that length normalization ($\alpha$) and coverage penalty ($\beta$) are less effective for models with RL refinement. Table 3 summarizes our results. This is understandable, as during RL refinement, the models already learn to pay attention to the full source sentence to not under-translate or over-translate, which would result in a penalty on the BLEU (or GLEU) scores.

| BLEU | $\alpha$ |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | 0.0 | 0.2 | 0.4 | 0.6 | 0.8 | 1.0 |
| 0.0 | 0.320 | 0.321 | 0.322 | 0.322 | 0.322 | 0.322 |
| 0.2 | 0.322 | 0.322 | 0.322 | 0.322 | 0.321 | 0.321 |
| 0.4 | 0.322 | 0.322 | 0.322 | 0.321 | 0.321 | 0.316 |
| 0.6 | 0.322 | 0.322 | 0.321 | 0.321 | 0.319 | 0.309 |
| 0.8 | 0.322 | 0.322 | 0.321 | 0.321 | 0.316 | 0.302 |
| 1.0 | 0.322 | 0.321 | 0.321 | 0.320 | 0.313 | 0.295 |

Table 3: WMT En→Fr BLEU score with respect to different values of $\alpha$ and $\beta$. The model used here is trained using ML, then refined with RL. Compared to the results in Table 2, coverage penalty and length normalization appear to be less effective for models after RL-based model refinements. Results are obtained on the development set. {#wu-2016-gnmt-tab-3 .table tag=08E9}

We found that the optimal $\alpha$ and $\beta$ vary slightly for different models. Based on tuning results using internal Google datasets, we use $\alpha = 0.2$ and $\beta = 0.2$ in our experiments, unless noted otherwise.
