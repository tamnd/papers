---
paper: bayer-1972-btree
title: Organization and Maintenance of Large Ordered Indices
authors:
  - Rudolf Bayer
  - Edward M. McCreight
year: 1972
venue: Acta Informatica
field: databases
section: "4"
section_title: Key Insertion
tag: 06F3
kind: section
lang: en
source: https://infolab.usc.edu/csci585/Spring2010/den_ar/indexing.pdf
pdf_sha256: 69826c036d7948fe5b02f7498620c90cc6a8de2504251a57994d13dc7b14e470
pdf_pages: 12-14
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: f0fd3c314b6b6ca6ec78478e187f2f925bd5336de33126e9b4870afa318c0f80
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The algorithm in Figure 4 inserts a single key y into an index described in Section 3. The variable s is a page pointer set by the retrieval algorithm pointing to the last page that was scanned or having the value u if the page tree is empty.

Splitting a Page: If a page P in which an entry should be inserted is already full, it will be split into two pages. Logically first insert the entry into the sequence of entries in P--which is assumed to be in main store--resulting in a sequence

$$
p_0, (x_1, p_1), (x_2, p_2), \ldots, (x_{2k+1}, p_{2k+1})
$$

Now put the subsequence $p_0, (x_1, p_1), \ldots, (x_k, p_k)$ into P and introduce a new page P' to contain the subsequence

$$
p_{k+1}, (x_{k+2}, p_{k+2}), (x_{k+3}, p_{k+3}), \ldots, (x_{2k+1}, p_{2k+1}).
$$

Let Q be the father page of P. Insert the entry $(x_{k+1}, p')$, where p' points to P', into Q. Thus P' becomes a brother of P.

Inserting $(x_{k+1}, p')$ into Q may, of course, cause Q to split too, and so on, possibly up to the root. If the splitting page P is the root, then we introduce a new root page Q containing p, $(x_{k+1}, p')$ where p points to P and p' to P'.

Note that this insertion process maps B-trees with parameter k into B-trees with parameter k, and preserves properties (3.1), (3.2), and (3.3).

To illustrate the insertion process, insertion of key 9 into the tree in Figure 5 with parameter k = 2 results in the tree in Figure 2.

Figure.

(1) Key y is already in index, take appropriate action.

Figure 4. Insertion Algorithm {#bayer-1972-btree-fig-4 .figure tag=06F4}

Figure 5. Index structure in $\tau(2,2)$ {#bayer-1972-btree-fig-5 .figure tag=06F5}

Figure.
