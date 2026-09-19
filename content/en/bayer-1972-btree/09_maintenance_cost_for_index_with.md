---
paper: bayer-1972-btree
title: Organization and Maintenance of Large Ordered Indices
authors:
  - Rudolf Bayer
  - Edward M. McCreight
year: 1972
venue: Acta Informatica
field: databases
section: "9"
section_title: Maintenance Cost for Index with Insertions and Deletions
tag: 06FB
kind: section
lang: en
source: https://infolab.usc.edu/csci585/Spring2010/den_ar/indexing.pdf
pdf_sha256: 69826c036d7948fe5b02f7498620c90cc6a8de2504251a57994d13dc7b14e470
pdf_pages: 24-27
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 1fe7831bf46c574f373b03886e40d055a2aeb7b1c760a2901e6a4bf3bf604da7
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The main purpose of this paper is to develop a data structure which allows economical maintenance of an index in which retrievals, insertions, and deletions must be done in any order. We will now derive bounds on the processing cost in such an environment.

The derivation of bounds for retrieval cost did not make any assumptions about the order of insertions or deletions, so they are still valid. Also, the minimal and maximal bounds for the cost of insertions and deletions were derived without any such assumptions and are still valid. The bounds derived for the average cost, however, are no longer valid if insertions and deletions are mixed.

The following example shows that the upper bounds for the average cost cannot be improved appreciably over the upper bounds of the cost derived for a single retrieval or deletion.

Example: Consider the trees $T_2$ in Figure 2 and $T_5$ in Figure 5. Deleting key 9 from $T_2$ leads to $T_5$, and inserting key 9 in $T_5$ leads back to $T_2$. Consider a sequence of alternating deletions and insertions of key 9 being applied starting with $T_2$.

Case 1: No page overflows, but only page splits occur:

i) Each deletion of key 9 from $T_2$ requires:
   3 retrievals to locate key 9, namely pages 1, 2, 6.
   1 retrieval of brother 5 of page 6 to find out that pages 5 and 6 can be catenated.

2 pages, namely 5 and 2 are modified and must be written.

Pages 6 and 3 are deleted from the tree $T_2$.

Thus $f = 5$ and $w = 2$. But $f = 5 = 2h - 1 = f_{\max}$ and $w = 2 = h - 1 = w_{\max} - 2$.

ii) Each insertion of key 9 into $T_5$ requires:

2 retrievals to locate slot for 9 in page 5.

5 pages must be written, namely 1, 2, 3, 5, 6.

Thus

$$
f = 2 = h = f_{\max}
$$

$$
w = 5 = 2h + 1 = w_{\max}
$$

Case 2: Consider a scheme with page overflows.

i) Deletion of key 9 leads to the same results as in Case 1.

ii) Insertion of key 9 requires:

2 retrievals to locate slot for 9 on page 5.

2 retrievals of brothers 4 and 7 of 5 to find out that 5 must be split.

5 pages must be written as in Case 1.

Thus:

$$
f = 4 = 3h - 2 = f_{\max}
$$

$$
w = 5 = 2h + 1 = w_{\max}
$$

Analogous examples can be constructed for arbitrary $h$ and $k$.

From the analysis it is clear that the performance of our scheme depends on the actual sequence of insertions and deletions. The interference between insertions and deletions may degrade the performance of the scheme as opposed to doing insertions or deletions only. But even in the worst cases this interference degrades the performance at most by a factor of 3.

It is an open question how important this interference is in any actual applications and how relevant our worst case analysis is. Although the derivable cost bounds are worse, the scheme with overflows performed better in our experiments than the scheme without overflows.

| min | insertion in index with-out deletions and without overflows retrieval |  | deletion in index without insertions, but with overflow |  | insertion in index with deletions, without overflow |  | insertion in index with deletions, with overflow |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | f = 1 | w = 0 | f = h | w = 1 | f = h | w = 1 | f = h | w = 1 |
| average as derived in paper | f ≤ h | w = 0 | f < h + 1 + $\frac{1}{k}$ | w < 1 + $\frac{2}{k}$ | f ≤ h + 2 + $\frac{2}{k}$ | w ≤ 3 + $\frac{2}{k}$ | f ≤ 2h - 1 | w ≤ 2h + 1 |
|  | f = h | w = 0 | f = h | w = 2h + 1 | f = h | w = h + 1 | f = 2h - 1 | w = 2h + 1 |
| max | f = h | w = 0 | f = h | w = 2h + 1 | f = 3h - 2 | w = 2h + 1 | f = 3h - 2 | w = 2h + 1 |
|  |  |  |  |  |  |  |  |  |

f : number of pages fetched
w : number of pages written
I : size of index set
h : height of B-tree
k : parameter of B-tree of pages
u : best upper bound obtainable for w

Figure 7. Table of Costs for a Single Retrieval, Insertion, or Deletion of a Key {#bayer-1972-btree-fig-7 .figure tag=06FC}
