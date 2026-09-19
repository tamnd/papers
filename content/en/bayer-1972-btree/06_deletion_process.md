---
paper: bayer-1972-btree
title: Organization and Maintenance of Large Ordered Indices
authors:
  - Rudolf Bayer
  - Edward M. McCreight
year: 1972
venue: Acta Informatica
field: databases
section: "6"
section_title: Deletion Process
tag: 06F7
kind: section
lang: en
source: https://infolab.usc.edu/csci585/Spring2010/den_ar/indexing.pdf
pdf_sha256: 69826c036d7948fe5b02f7498620c90cc6a8de2504251a57994d13dc7b14e470
pdf_pages: 17-19
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 2d5162ada7e53588fb1af5b3c6c9223512c3ce947c43a7ef8317ae892462652c
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

In a dynamically changing index it must be necessary to delete keys. The algorithm of Figure 6 deletes one key y from an index and maintains our data structure properly. It first locates the key, say $y_i$. To maintain the data structure properly, $y_i$ is deleted if it is on a leaf, otherwise it must be replaced by the smallest key in the subtree whose root is $P(p_i)$. This smallest key is found by going from $P(p_i)$ along the $p_0$ pointers to the leaf page, say L, and taking the first key in L. Then this key, say $x_1$, is deleted from L. As a consequence L may contain fewer than k keys and a catenation or underflow between L and an adjacent brother is performed.

Catenation: Two pages P and P' are called adjacent brothers if they have the same father Q and are pointed to by adjacent pointers in Q. P and P' can be catenated, if together they have no more than 2k keys, as follows: The three pages of the form

$$
\begin{array}{|c|}
\hline
\ldots, (y_{j-1}, p), (y_j, p'), (y_{j+1}, p_{j+1}) \ldots \\
\hline
\end{array}
$$

can be replaced by two pages of the form:

$$
\begin{array}{|c|}
\hline
\ldots, (y_{j-1}, p), (y_{j+1}, p_{j+1}), \ldots \\
\hline
\end{array}
$$

$$
\begin{array}{|c|}
\hline
p_0, (x_1, p_1), \ldots, (x_\ell, p_\ell) \\
\hline
\end{array}
$$

$$
\begin{array}{|c|}
\hline
p'_0, (x_{\ell+1}, p_{\ell+1}), \ldots \\
\hline
\end{array}
$$

As a consequence of deleting the entry $(y_j, p')$ from Q it is now possible that Q contains fewer than k keys and special action must be taken for Q. This process may propagate up to the root of the tree.

Underflow: If the sum of the number of keys in P and P' is greater than $2k$, then the keys in P and P' can be equally distributed, the process being called an underflow, as follows:

Perform the catenation between P and P' resulting in too large a P. This is possible since P is in main store. Now split P "in the middle" as described in Section 4 with some obvious minor modifications.

Note that underflows do not propagate. Q is modified, but the number of keys in it is not changed.

To illustrate the deletion process consider the index in Figure 2. Deleting key 9 results in the index in Figure 5.

(1) The key to be deleted is not in index, take appropriate action.

Figure 6. Deletion Algorithm {#bayer-1972-btree-fig-6 .figure tag=06F8}
