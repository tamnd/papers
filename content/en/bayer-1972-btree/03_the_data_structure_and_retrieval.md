---
paper: bayer-1972-btree
title: Organization and Maintenance of Large Ordered Indices
authors:
  - Rudolf Bayer
  - Edward M. McCreight
year: 1972
venue: Acta Informatica
field: databases
section: "3"
section_title: The Data Structure and Retrieval Algorithm
tag: 06EF
kind: section
lang: en
source: https://infolab.usc.edu/csci585/Spring2010/den_ar/indexing.pdf
pdf_sha256: 69826c036d7948fe5b02f7498620c90cc6a8de2504251a57994d13dc7b14e470
pdf_pages: 7-11
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: f8421c330cb35f4c6e43d308ca5d9118330f5c4a8dc25a48de1c43a61fd5658a
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

To repeat, the pages on which the index is stored are the nodes of a B-tree $T \in \tau(k,h)$ and can hold up to $2k$ keys. In addition the data structure for the index has the following properties:

i) Each page holds between $k$ and $2k$ keys (index elements) except the root page which may hold between $1$ and $2k$ keys.

ii) Let the number of keys on a page $P$, which is not a leaf, be $\ell$. Then $P$ has $\ell + 1$ sons.

iii) Within each page $P$ the keys are sequential in increasing order: $x_1, x_2, ..., x_\ell$; $k \leq \ell \leq 2k$ except for the root page for which $1 \leq \ell \leq 2k$. Furthermore, $P$ contains $\ell + 1$ pointers $p_0, p_1, ..., p_\ell$ to the sons of $P$. On leaf pages these pointers are undefined. Logically a page is then organized as shown in Figure 1.

Figure 1. Organization of a Page {#bayer-1972-btree-fig-1 .figure tag=06F0}

The $\alpha_i$ are the associated information in the index element $(x_i,\alpha_i)$. The triple $(x_i,\alpha_i,p_i)$ or--omitting $\alpha_i$--the pair $(x_i,p_i)$ is also called an entry.

iv) Let $P(p_i)$ be the page to which $p_i$ points, let $K(p_i)$ be the set of keys on the pages of that maximal subtree of which $P(p_i)$ is the root. Then for the B-trees considered here the following conditions shall always hold:

$$
(\forall y \in K(p_0))(y < x_1)
$$

(3.1)

$$
(\forall y \in K(p_i))\ (x_i < y < x_{i+1});\ i = 1,2,\ldots,\ell-1
$$

(3.2)

$$
(\forall y \in K(p_\ell))(x_\ell < y)
$$

(3.3)

Figure 2 is an example of a B-tree in $\tau(2,3)$ satisfying all the above conditions. In the figure the $\alpha_i$ are not shown and the page pointers are represented graphically. The boxes represent pages and the numbers outside are page numbers to be used later.

Retrieval Algorithm: The flowchart in Figure 3 is an algorithm for retrieving a key $y$. Let $p, r, s$ be pointer variables which can also assume the value "undefined" denoted as $u$. $r$ points to the root and is $u$ if the tree is empty, $s$ does not serve any purpose for retrieval, but will be used in the insertion algorithm. Let $P(p)$ be the page to which $p$ is pointing, then $x_1, \ldots, x_\ell$ are the keys in $P(p)$ and $p_0, \ldots, p_\ell$ the page pointers in $P(p)$.

The retrieval algorithm is simple logically, but to program it for a computer one would use an efficient technique, e.g., a binary search, to scan a page.

Cost of Retrieval: Let $h$ be the height of the page tree. Then at most $h$ pages must be scanned and therefore fetched from backup store to retrieve a key $y$. We will now derive bounds for $h$ for a given index

Figure 2. A Data Structure in $\tau(2,3)$ for an Index {#bayer-1972-btree-fig-2 .figure tag=06F1}

Figure.

Figure 3. Retrieval Algorithm {#bayer-1972-btree-fig-3 .figure tag=06F2}

of size I. The minimum and maximum number $I_{\min}$ and $I_{\max}$ of keys in a B-tree of pages in $\tau(k,h)$ are:

$$
I_{\min} = 1 + k \left( 2 \frac{(k+1)^{h-1}-1}{k} \right) = 2(k+1)^{h-1} - 1
$$

$$
I_{\max} = 2k \left( \frac{(2k+1)^{h-1}}{2k} \right) = (2k+1)^h - 1
$$

This is immediate from (2.1) for $h \geq 1$. Thus we have as sharp bounds for the height $h$:

$$
\log_{2k+1}(I+1) \leq h \leq 1 + \log_{k+1}\left( \frac{I+1}{2} \right) \quad \text{for } I \geq 1,
$$

$$
h = 0 \quad \text{for } I = 0.
$$

(3.1)
