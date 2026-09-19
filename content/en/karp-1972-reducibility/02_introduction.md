---
paper: karp-1972-reducibility
title: Reducibility Among Combinatorial Problems
authors:
  - Richard M. Karp
year: 1972
venue: Complexity of Computer Computations
field: theory
section: "1"
section_title: INTRODUCTION
tag: 04FD
kind: appendix
lang: en
source: https://doi.org/10.1007/978-1-4684-2001-2_9
pdf_sha256: ae57cf641ae4f1924bdc4d7ef865edb2411c44e3040e8e546d01f1545e288e89
pdf_pages: 5-6
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 8cebf20048171cdc8771d4a202d5a67d536e4638c5e4c4a68eee0575914b85eb
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

All the general methods presently known for computing the chromatic number of a graph, deciding whether a graph has a Hamilton circuit, or solving a system of linear inequalities in which the variables are constrained to be 0 or 1, require a combinatorial search for which the worst case time requirement grows exponentially with the length of the input. In this paper we give theorems which strongly suggest, but do not imply, that these problems, as well as many others, will remain intractable perpetually.

† This research was partially supported by National Science Foundation Grant GJ-474.

We are specifically interested in the existence of algorithms that are guaranteed to terminate in a number of steps bounded by a polynomial in the length of the input. We exhibit a class of well-known combinatorial problems, including those mentioned above, which are equivalent, in the sense that a polynomial-bounded algorithm for any one of them would effectively yield a polynomial-bounded algorithm for all. We also show that, if these problems do possess polynomial-bounded algorithms then all the problems in an unexpectedly wide class (roughly speaking, the class of problems solvable by polynomial-depth backtrack search) possess polynomial-bounded algorithms.

The following is a brief summary of the contents of the paper. For the sake of definiteness our technical development is carried out in terms of the recognition of languages by one-tape Turing machines, but any of a wide variety of other abstract models of computation would yield the same theory. Let $\Sigma^*$ be the set of all finite strings of 0's and 1's. A subset of $\Sigma^*$ is called a language. Let $P$ be the class of languages recognizable in polynomial time by one-tape deterministic Turing machines, and let $NP$ be the class of languages recognizable in polynomial time by one-tape nondeterministic Turing machines. Let $\Pi$ be the class of functions from $\Sigma^*$ into $\Sigma^*$ computable in polynomial time by one-tape Turing machines. Let L and M be languages. We say that $L \propto M$ (L is reducible to M) if there is a function $f \in \Pi$ such that $f(x) \in M \Leftrightarrow x \in L$. If $M \in P$ and $L \propto M$ then $L \in P$. We call L and M equivalent if $L \propto M$ and $M \propto L$. Call L (polynomial) complete if $L \in NP$ and every language in $NP$ is reducible to L. Either all complete languages are in $P$, or none of them are. The former alternative holds if and only if $P = NP$.

The main contribution of this paper is the demonstration that a large number of classic difficult computational problems, arising in fields such as mathematical programming, graph theory, combinatorics, computational logic and switching theory, are complete (and hence equivalent) when expressed in a natural way as language recognition problems.

This paper was stimulated by the work of Stephen Cook (1971), and rests on an important theorem which appears in his paper. The author also wishes to acknowledge the substantial contributions of Eugene Lawler and Robert Tarjan.
