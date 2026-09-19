---
paper: bayer-1972-btree
title: Organization and Maintenance of Large Ordered Indices
authors:
  - Rudolf Bayer
  - Edward M. McCreight
year: 1972
venue: Acta Informatica
field: databases
section: "7"
section_title: Cost of Deletions
tag: 06F9
kind: section
lang: en
source: https://infolab.usc.edu/csci585/Spring2010/den_ar/indexing.pdf
pdf_sha256: 69826c036d7948fe5b02f7498620c90cc6a8de2504251a57994d13dc7b14e470
pdf_pages: 20-21
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: ece6ac9139a0f7f6128d3004bead708df7bb95d6171a46a67fff2dabd071d59b
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

For a successful deletion, i.e., if the key y to be deleted is in the index, the least amount of work is required if no catenations or underflows are performed and y is in a leaf. This requires:

$$
f_{\min} = h; \quad w_{\min} = l;
$$

If y is not in a leaf and no catenations or underflows occur, then

$$
f = h; \quad w = 2;
$$

A maximal amount of work must be done if all but the first two pages in the retrieval path are catenated, the son of the root in the retrieval path has an underflow, and the root is modified. This requires:

$$
f_{\max} = 2h - 1; \quad w_{\max} = h + 1;
$$

As in the case of the insertion process the bounds obtained are sharp, but very far apart and assumed rarely except in pathological examples. To obtain a more useful measure for the average amount of work necessary to delete a key, let us consider a "pure deletion process" during which all keys in an index I are deleted, but no keys are inserted.

Disregarding for the moment catenations and underflows we may get $f_1 = h$ and $w_1 = 2$ for each deletion at worst. But this is the best bound obtainable if one considers an example in which keys are always deleted from the root page.

Each deletion causes at most one underflow, requiring $f_2 = 1$ additional fetches and $w_2 = 2$ additional writes.

The total number of possible catenations is bounded by $n(I) - 1$, which is at most $\frac{I-1}{k}$. Each catenation causes 1 additional fetch and 2 additional writes, which results in an average

$$
f_3 = \frac{1}{I} \left( \frac{I-1}{k} \right) < \frac{1}{k}
$$

$$
w_3 = \frac{2}{I} \left( \frac{I-1}{k} \right) < \frac{2}{k}.
$$

Thus in the average we get:

$$
f_a = f_1 + f_2 + f_3 < h + 1 + \frac{1}{k}
$$

$$
w_a = w_1 + w_2 + w_3 < 2 + 2 + \frac{2}{k} = 4 + \frac{2}{k}.
$$
