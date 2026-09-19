---
paper: mccabe-1976-complexity
title: A Complexity Measure
authors:
  - Thomas J. McCabe
year: 1976
venue: IEEE Transactions on Software Engineering
field: software
section: V
section_title: SIMPLIFICATION
tag: 03AE
kind: section
lang: en
source: http://www.literateprogramming.com/mccabe.pdf
pdf_sha256: be2ac1035940dfc7fa231e23b33bfa3c2f3e3d8ef3112e20cf92a35a7af537f6
pdf_pages: 7-8
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 7794539d733ec90103c6cf3fdfd0ab7843a75a62fcdea20571dde85c3c956afe
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Since the calculation $v = e - n + 2p$ can be quite tedious for a programmer an effort has been made to simplify the complexity calculations (for single-component graphs). There are two results presented in this section—the first allows the complexity calculations to be done in terms of program syntactic constructs, the second permits an easier calculation from the graph form.

In [7] Mills proves the following: if the number of function, predicate, and collecting nodes in a structured program is $\theta, \pi,$ and $\gamma$, respectively, and e is the number of edges, then

$$
e = 1 + \theta + 3\pi.
$$

Since for every predicate node there is exactly one collecting node and there are unique entry and exit nodes it follows that

$$
n = \theta + 2\pi + 2.
$$

Assuming $p = 1$ and substituting in $v = e - n + 2$ we get

$$
v = (1 + \theta + 3\pi) - (\theta + 2\pi + 2) + 2 = \pi + 1.
$$

This proves that the cyclomatic complexity of a structured program equals the number of predicates plus one, for example in

Figure.

$^2$ A graph is connected if for every pair of vertices there is a chain going from one to the other. Given a vertex a, the set of vertices that can be connected to a, together with a itself is a connected component.

complexity $v(G) = \pi + 1 = 3 + 1 = 4$. Notice how in this case complexity can be computed by simply counting the number of predicates in the code and not having to deal with the control graph.

In practice compound predicates such as IF "C1 AND C2" THEN are treated as contributing two to complexity since without the connective AND we would have

IF C1 THEN IF C2 THEN which has two predicates. For this reason and for testing purposes it has been found to be more convenient to count conditions instead of predicates when calculating complexity.$^3$

It has been proved that in general the complexity of any (unstructured) program is $\pi + 1$.

The second simplification of the calculation of e - n + 2p reduces the calculation of visual inspection of the control graph. We need Euler's formula which is as follows. If G is a connected plane graph with n vertices, e edges, and r regions, then

$$
n - e + r = 2.
$$

Just changing the order of the terms we get $r = e - n + 2$ so the number of regions is equal to the cyclomatic complexity. Given a program with a plane control graph one can therefore calculate v by counting regions, as in

Figure.
