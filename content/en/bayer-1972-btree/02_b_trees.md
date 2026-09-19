---
paper: bayer-1972-btree
title: Organization and Maintenance of Large Ordered Indices
authors:
  - Rudolf Bayer
  - Edward M. McCreight
year: 1972
venue: Acta Informatica
field: databases
section: "2"
section_title: '**B-Trees**'
tag: 06ED
kind: section
lang: en
source: https://infolab.usc.edu/csci585/Spring2010/den_ar/indexing.pdf
pdf_sha256: 69826c036d7948fe5b02f7498620c90cc6a8de2504251a57994d13dc7b14e470
pdf_pages: "6"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 612bee79c049729fb9671931bf81a1dedfc547b855811b76bd6f424bb1e3b892
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

**Def. 2.1:** Let $h \geq 0$ be an integer, $k$ a natural number. A directed tree $T$ is in the class $\tau(k,h)$ of *B-trees* if $T$ is either empty ($h=0$) or has the following properties:

i) Each path from the root to any leaf has the same length $h$, also called the *height* of $T$, i.e., $h =$ number of nodes in path.

ii) Each node except the root and the leaves has at least $k+1$ sons. The root is a leaf or has at least two sons.

iii) Each node has at most $2k+1$ sons.

**Number of Nodes in B-Trees:** Let $N_{\min}$ and $N_{\max}$ be the minimal and maximal number of nodes in a B-tree $T \in \tau(k,h)$. Then

$$
N_{\min} = 1 + 2 \left( (k+1)^0 + (k+1)^1 + \ldots + (k+1)^{h-2} \right) = 1 + \frac{2}{k} \left( (k+1)^{h-1} - 1 \right)
$$

for $h \geq 2$. This also holds for $h = 1$. Similarly one obtains

$$
N_{\max} = \sum_{i=0}^{h-1} (2k+1)^i = \frac{1}{2k} \left( (2k+1)^h - 1 \right); \quad h \geq 1.
$$

Upper and lower bounds for the number $N(T)$ of nodes of $T \in \tau(k,h)$ are given by:

$$
N(T) = 0 \quad \text{if} \quad T \in \tau(k,0); \tag{2.1}
$$
{#bayer-1972-btree-eq-2-1 .equation tag=06EE}

$$
1 + \frac{2}{k} \left( (k+1)^{h-1} - 1 \right) \leq N(T) \leq \frac{1}{2k} \left( (2k+1)^h - 1 \right) \quad \text{otherwise}.
$$

Note that the classes $\tau(k,h)$ need not be disjoint.
