---
paper: mccabe-1976-complexity
title: A Complexity Measure
authors:
  - Thomas J. McCabe
year: 1976
venue: IEEE Transactions on Software Engineering
field: software
section: IV
section_title: DECOMPOSITION
tag: 03AD
kind: section
lang: en
source: http://www.literateprogramming.com/mccabe.pdf
pdf_sha256: be2ac1035940dfc7fa231e23b33bfa3c2f3e3d8ef3112e20cf92a35a7af537f6
pdf_pages: "7"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: f7717482da99c83803ed6939e2d408aae4fe54fb1f315ea6cc52907aa4cfa37a
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The role of p in the complexity calculation v = e - n + 2p will now be explained. Recall in Definition 1 that p is the number of connected components. The way we defined a program control graph (unique entry and exit nodes, all nodes reachable from the entry, and the exit reachable from all nodes) would result in all control graphs having only one connected component. One could, however, imagine a main program M and two called subroutines A and B having a control structure shown below:

M:
A:
B:

Let us denote the total graph above with 3 connected components$^2$ as M \cup A \cup B. Now, since p = 3 we calculate complexity as

$$
v(M \cup A \cup B) = e - n + 2p = 13 - 13 + 2 \times 3 = 6.
$$

This method with p \neq 1 can be used to calculate the complexity of a collection of programs, particularly a hierarchical nest of subroutines as shown above.

Notice that $v(M \cup A \cup B) = v(M) + v(A) + v(B) = 6$. In general, the complexity of a collection C of control graphs with k connected components is equal to the summation of their complexities. To see this let $C_i, 1 \leq i \leq k$ denote the k distinct connected components, and let $e_i$ and $n_i$ be the number of edges and nodes in the ith connected component. Then

$$
v(C) = e - n + 2p = \sum_{i=1}^k e_i - \sum_{i=1}^k n_i + 2k
$$

$$
= \sum_{i=1}^k (e_i - n_i + 2) = \sum_{i=1}^k v(C_i).
$$
