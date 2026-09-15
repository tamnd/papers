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
section: A
section_title: Details of Common Crawl Filtering
tag: 01FE
kind: appendix
lang: en
source: arxiv:2005.14165
pdf_sha256: 97fd272f1fdfc18677462d0292f5fbf26ca86b4d1b485c2dba03269b643a0e83
pdf_pages: "43"
extraction: vision
extraction_model: gpt-5
content_sha256: 2220365806ce8837806082dafbd58f450728cb126c2fa477a45b56841974c209
prompt_sha256: e1b070d511afab62a45db64b491e759e38eaa12f6c7943b773a942f4f2f70935
---

As mentioned in Section 2.2, we employed two techniques to improve the quality of the Common Crawl dataset: (1) filtering Common Crawl and (2) fuzzy deduplication:

1. In order to improve the quality of Common Crawl, we developed an automatic filtering method to remove low quality documents. Using the original WebText as a proxy for high-quality documents, we trained a classifier to distinguish these from raw Common Crawl. We then used this classifier to re-sample Common Crawl by prioritizing documents which were predicted by the classifier to be higher quality. The classifier is trained using logistic regression classifier with features from Spark’s standard tokenizer and HashingTF $^{10}$. For the positive examples, we used a collection of curated datasets such as WebText, Wikipedia, and our web books corpus as the positive examples, and for the negative examples, we used unfiltered Common Crawl. We used this classifier to score Common Crawl documents. We kept each document in our dataset iff

$$
\text{np.random.pareto}(\alpha) > 1 - \text{document\_score}
$$

We chose $\alpha = 9$ in order to take mostly documents the classifier scored highly, but still include some documents that were out of distribution. $\alpha$ was chosen to match the distribution of scores from our classifier on WebText. We found this re-weighting increased quality as measured by loss on a range of out-of-distribution generative text samples.

2. To further improve model quality and prevent overfitting (which becomes increasingly important as model capacity increases), we fuzzily deduplicated documents (i.e. removed documents with high overlap with other documents) within each dataset using Spark’s MinHashLSH implementation with 10 hashes, using the same features as were used for classification above. We also fuzzily removed WebText from Common Crawl. Overall this decreased dataset size by an average of 10%.

After filtering for duplicates and quality, we also partially removed text occurring in benchmark datasets, described in Appendix C.
