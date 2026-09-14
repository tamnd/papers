---
paper: brown-2020-gpt3
title: Language Models are Few-Shot Learners
authors:
  - Tom B. Brown
  - Benjamin Mann
  - Nick Ryder
  - Melanie Subbiah
  - Jared Kaplan
  - Prafulla Dhariwal
  - Arvind Neelakantan
  - Pranav Shyam
  - Girish Sastry
  - Amanda Askell
year: 2020
venue: NeurIPS
field: ai-ml
section: C
section_title: Details of Test Set Contamination Studies
tag: "0200"
kind: appendix
lang: en
source: arxiv:2005.14165
pdf_sha256: 97fd272f1fdfc18677462d0292f5fbf26ca86b4d1b485c2dba03269b643a0e83
pdf_pages: 43-45
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 6258f06ce09764649d32c5609a0fce9fffde636769f81323b1d549373ad0ea74
prompt_sha256: e1b070d511afab62a45db64b491e759e38eaa12f6c7943b773a942f4f2f70935
---

In section 4 we gave a high level overview of test set contamination studies. In this section we provide details on methodology and results.

Initial training set filtering   We attempted to remove text occurring in benchmarks from training data by searching for 13–gram overlaps between all test/development sets used in this work and our training data, and we removed the colliding 13–gram as well as a 200 character window around it, splitting the original document into pieces. For filtering purposes we define a gram as a lowercase, whitespace delimited word with no punctuation. Pieces less than 200 characters long were discarded. Documents split into more than 10 pieces were considered contaminated and

$^{10}$ https://spark.apache.org/docs/latest/api/python/pyspark.ml.html#pyspark.ml.feature.HashingTF removed entirely. Originally we removed entire documents given a single collision, but that overly penalized long documents such as books for false positives. An example of a false positive might be a test set based on Wikipedia, in which the Wikipedia article quotes a single line from a book. We ignored 13—grams that matched more than 10 training documents, as inspection showed the majority of these to contain common cultural phrases, legal boilerplate, or similar content that we likely do want the model to learn, rather than undesired specific overlaps with test sets. Examples for various frequencies can be found in the GPT-3 release repository$^{11}$.

Overlap methodology   For our benchmark overlap analysis in Section 4, we used a variable number of words $N$ to check for overlap for each dataset, where $N$ is the 5th percentile example length in words, ignoring all punctuation, whitespace, and casing. Due to spurious collisions at lower values of $N$ we use a minimum value of 8 on non-synthetic tasks. For performance reasons, we set a maximum value of 13 for all tasks. Values for $N$ and the amount of data marked as dirty are shown in Table C.1. Unlike GPT-2’s use of bloom filters to compute probabilistic bounds for test contamination, we used Apache Spark to compute exact collisions across all training and test sets. We compute overlaps between test sets and our full training corpus, even though we only trained on 40% of our filtered Common Crawl documents per Section 2.2.

We define a ‘dirty’ example as one with any $N$-gram overlap with any training document, and a ‘clean’ example as one with no collision.

Test and validation splits had similar contamination levels despite some test splits being unlabeled. Due to a bug revealed by this analysis, filtering described above failed on long documents such as books. Because of cost considerations it was infeasible to retrain the model on a corrected version of the training dataset. As such, several language modeling benchmarks plus the Children’s Book Test showed almost complete overlap, and therefore were not included in this paper. Overlaps are shown in Table C.1

Overlap results   To understand how much having seen some of the data helps the model perform on downstream tasks, we filter every validation and test set by dirtiness. Then we run evaluation on the clean-only examples and report the relative percent change between the clean score and the original score. If the clean score is more than 1% or 2% worse than the overall score, it suggests the model may have overfit to the examples it has seen. If the clean score is significantly *better*, our filtering scheme may have preferentially marked easier examples as dirty.

This overlap metric tends to show a high rate of false positives for datasets that contain background information (but not answers) drawn from the web (such as SQuAD, which draws from Wikipedia) or examples less than 8 words long, which we ignored in our filtering process (except for words scrambling tasks). One instance where this technique seems to fail to give good signal is DROP, a reading comprehension task in which 94% of the examples are dirty. The information required to answer the question is in a passage provided to the model, so having seen the passage during training but not the questions and answers does not meaningfully constitute cheating. We confirmed that every matching training document contained only the source passage, and none of the questions and answers in the dataset. The more likely explanation for the decrease in performance is that the 6% of examples that remain after filtering come from a slightly different distribution than the dirty examples.

Figure 4.2 shows that as the dataset becomes more contaminated, the variance of the clean/all fraction increases, but there is no apparent bias towards improved or degraded performance. This suggests that GPT-3 is relatively insensitive to contamination. See Section 4 for details on the datasets we flagged for further review. {#brown-2020-gpt3-fig-4 .figure tag=0201}

\footnotetext{11https://github.com/openai/gpt-3/blob/master/overlap_frequency.md

| Name | Split | Metric | $N$ | Acc/F1/BLEU | Total Count | Dirty Acc/F1/BLEU | Dirty Count | Clean Acc/F1/BLEU | Clean Count | Clean Percentage | Relative Difference Clean vs All |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Quac | dev | f1 | 13 | 44.3 | 7353 | 44.3 | 7315 | 54.1 | 38 | 1% | 20% |
| SQuADv2 | dev | f1 | 13 | 69.8 | 11873 | 69.9 | 11136 | 68.4 | 737 | 6% | -2% |
| DROP | dev | f1 | 13 | 36.5 | 9536 | 37.0 | 8898 | 29.5 | 638 | 7% | -21% |
| Symbol Insertion | dev | acc | 7 | 66.9 | 10000 | 66.8 | 8565 | 67.1 | 1435 | 14% | 0% |
| CoQA | dev | f1 | 13 | 86.0 | 7983 | 85.3 | 5107 | 87.1 | 2876 | 36% | 1% |
| ReCoRD | dev | acc | 13 | 89.5 | 10000 | 90.3 | 6110 | 88.2 | 3890 | 39% | -1% |
| Winograd | test | acc | 9 | 88.6 | 273 | 90.2 | 164 | 86.2 | 109 | 40% | -3% |
| BoolQ | dev | acc | 13 | 76.0 | 3270 | 75.8 | 1955 | 76.3 | 1315 | 40% | 0% |
| MultiRC | dev | acc | 13 | 74.2 | 953 | 73.4 | 558 | 75.3 | 395 | 41% | 1% |
| RACE-h | test | acc | 13 | 46.8 | 3498 | 47.0 | 1580 | 46.7 | 1918 | 55% | 0% |
| LAMBADA | test | acc | 13 | 86.4 | 5153 | 86.9 | 2209 | 86.0 | 2944 | 57% | 0% |
| LAMBADA (No Blanks) | test | acc | 13 | 77.8 | 5153 | 78.5 | 2209 | 77.2 | 2944 | 57% | -1% |
| WSC | dev | acc | 13 | 76.9 | 104 | 73.8 | 42 | 79.0 | 62 | 60% | 3% |
| PIQA | dev | acc | 8 | 82.3 | 1838 | 89.9 | 526 | 79.3 | 1312 | 71% | -4% |
| RACE-m | test | acc | 13 | 58.5 | 1436 | 53.0 | 366 | 60.4 | 1070 | 75% | 3% |
| De→En 16 | test | bleu-sb | 12 | 43.0 | 2999 | 47.4 | 739 | 40.8 | 2260 | 75% | -5% |
| En→De 16 | test | bleu-sb | 12 | 30.9 | 2999 | 32.6 | 739 | 29.9 | 2260 | 75% | -3% |
| En→Ro 16 | test | bleu-sb | 12 | 25.8 | 1999 | 24.9 | 423 | 26.1 | 1576 | 79% | 1% |
| Ro→En 16 | test | bleu-sb | 12 | 41.3 | 1999 | 40.4 | 423 | 41.6 | 1576 | 79% | 1% |
| WebQs | test | acc | 8 | 41.5 | 2032 | 41.6 | 428 | 41.5 | 1604 | 79% | 0% |
| ANLI R1 | test | acc | 13 | 36.8 | 1000 | 40.5 | 200 | 35.9 | 800 | 80% | -3% |
| ANLI R2 | test | acc | 13 | 34.0 | 1000 | 29.4 | 177 | 35.0 | 823 | 82% | 3% |
| TriviaQA | dev | acc | 10 | 71.2 | 7993 | 70.8 | 1390 | 71.3 | 6603 | 83% | 0% |
| ANLI R3 | test | acc | 13 | 40.2 | 1200 | 38.3 | 196 | 40.5 | 1004 | 84% | 1% |
| En→Fr 14 | test | bleu-sb | 13 | 39.9 | 3003 | 38.3 | 411 | 40.3 | 2592 | 86% | 1% |
| Fr→En 14 | test | bleu-sb | 13 | 41.4 | 3003 | 40.9 | 411 | 41.4 | 2592 | 86% | 0% |
| WiC | dev | acc | 13 | 51.4 | 638 | 53.1 | 49 | 51.3 | 589 | 92% | 0% |
| RTE | dev | acc | 13 | 71.5 | 277 | 71.4 | 21 | 71.5 | 256 | 92% | 0% |
| CB | dev | acc | 13 | 80.4 | 56 | 100.0 | 4 | 78.8 | 52 | 93% | -2% |
| Anagrams 2 | dev | acc | 2 | 40.2 | 10000 | 76.2 | 705 | 37.4 | 9295 | 93% | -7% |
| Reversed Words | dev | acc | 2 | 0.4 | 10000 | 1.5 | 660 | 0.3 | 9340 | 93% | -26% |
| OpenBookQA | test | acc | 8 | 65.4 | 500 | 58.1 | 31 | 65.9 | 469 | 94% | 1% |
| ARC (Easy) | test | acc | 11 | 70.1 | 2268 | 77.5 | 89 | 69.8 | 2179 | 96% | 0% |
| Anagrams 1 | dev | acc | 2 | 15.0 | 10000 | 49.8 | 327 | 13.8 | 9673 | 97% | -8% |
| COPA | dev | acc | 9 | 93.0 | 100 | 100.0 | 3 | 92.8 | 97 | 97% | 0% |
| ARC (Challenge) | test | acc | 12 | 51.6 | 1144 | 45.2 | 31 | 51.8 | 1113 | 97% | 0% |
| HellaSwag | dev | acc | 13 | 79.3 | 10042 | 86.2 | 152 | 79.2 | 9890 | 98% | 0% |
| NQs | test | acc | 11 | 29.9 | 3610 | 32.7 | 52 | 29.8 | 3558 | 99% | 0% |
| Cycled Letters | dev | acc | 2 | 38.6 | 10000 | 20.5 | 73 | 38.7 | 9927 | 99% | 0% |
| SAT Analogies | dev | acc | 9 | 65.8 | 374 | 100.0 | 2 | 65.6 | 372 | 99% | 0% |
| StoryCloze | test | acc | 13 | 87.7 | 1871 | 100.0 | 2 | 87.6 | 1869 | 100% | 0% |
| Winogrande | dev | acc | 13 | 77.7 | 1267 | - | 0 | 77.7 | 1267 | 100% | 0% |

Table C.1: Overlap statistics for all datasets sorted from dirtiest to cleanest. We consider a dataset example dirty if it has a single $N$-gram collision with any document in our training corpus. “Relative Difference Clean vs All” shows the percent change in performance between only the clean examples vs all the examples in the benchmark. “Count” shows the number of examples. “Clean percentage” is the percent of examples that are clean vs total. For “Acc/F1/BLEU” we use the metric specified in “Metric”. These scores come from evaluations with a different seed for the random examples used for in-context learning, and will therefore differ slightly from the scores elsewhere in the paper.
