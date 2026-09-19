---
paper: karp-1972-reducibility
title: Reducibility Among Combinatorial Problems
authors:
  - Richard M. Karp
year: 1972
venue: Complexity of Computer Computations
field: theory
section_title: Appendix I
kind: appendix
lang: en
source: https://doi.org/10.1007/978-1-4684-2001-2_9
pdf_sha256: ae57cf641ae4f1924bdc4d7ef865edb2411c44e3040e8e546d01f1545e288e89
pdf_pages: "23"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 8a323e90caf95ebc65bbdb2a874d6bcd382005836cad2a12ce66583727e3c068
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Notation and Terminology Used in Problem Specification

PROPOSITIONAL CALCULUS

$$
\begin{array}{ll}
x_1, x_2, \ldots, x_n & u_1, u_2, \ldots, u_m \\
\overline{x}_1, \overline{x}_2, \ldots, \overline{x}_n & \overline{u}_1, \overline{u}_2, \ldots, \overline{u}_m \\
\sigma, \sigma_i \\
C_1, C_2, \ldots, C_p & D_1, D_2, \ldots, D_r \\
C_k \subseteq \{x_1, x_2, \ldots, x_n, \overline{x}_1, \overline{x}_2, \ldots, \overline{x}_n\} \\
D_\ell \subseteq \{u_1, u_2, \ldots, u_m, \overline{u}_1, \overline{u}_2, \ldots, \overline{u}_m\}
\end{array}
$$

propositional variables
complements of propositional variables
literals
clauses

A clause contains no complementary pair of literals.

SCALARS, VECTORS, MATRICES

$$
\begin{array}{ll}
Z & \text{the positive integers} \\
Z^p & \text{the set of } p\text{-tuples of positive integers} \\
Z_p & \text{the set } \{0, 1, \ldots, p-1\} \\
k, W & \text{elements of } Z \\
<x, y> & \text{the ordered pair } <x, y> \\
(a_i)_j & \text{vectors with nonnegative integer components} \\
(c_{ij})_C & \text{matrices with integer components}
\end{array}
$$

GRAPHS AND DIGRAPHS

$$
\begin{array}{ll}
G = (N, A) & G' = (N', A') \\
N, N' & \text{sets of nodes} \\
s, t, u, v & \text{nodes} \\
(X, \overline{X}) = \{\{u, v\} | u \in X \text{ and } v \in \overline{X}\} & \text{cut} \\
\text{If } s \in X \text{ and } t \in \overline{X}, & (X, \overline{X}) \text{ is a s-t cut.} \\
w: A \to Z & w': A' \to Z \\
\text{weight functions}
\end{array}
$$

The weight of a subgraph is the sum of the weights of its arcs.

$$
\begin{array}{ll}
H = (V, E) & \text{digraph} \\
e, <u, v> & \text{arcs} \\
V & \text{set of nodes, } E \text{ set of arcs}
\end{array}
$$

SETS

$$
\begin{array}{ll}
\emptyset & \text{the empty set} \\
|S| & \text{the number of elements in the finite set } S \\
\{S_j\}, \{T_h\}, \{U_i\} & \text{finite families of finite sets}
\end{array}
$$
