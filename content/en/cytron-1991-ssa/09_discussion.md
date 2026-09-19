---
paper: cytron-1991-ssa
title: Efficiently Computing Static Single Assignment Form and the Control Dependence Graph
authors:
  - Ron Cytron
  - Jeanne Ferrante
  - Barry K. Rosen
  - Mark N. Wegman
  - F. Kenneth Zadeck
year: 1991
venue: ACM TOPLAS
field: languages
section: "9"
section_title: DISCUSSION
tag: 05B4
kind: section
lang: en
source: https://www.cs.utexas.edu/~pingali/CS380C/2010/papers/ssaCytron.pdf
pdf_sha256: 307512bb537628c2b326b23aa02109e7562bfc619509e942e015054ab58eb9ab
pdf_pages: 36-38
extraction: vision
extraction_model: gpt-5
content_sha256: c2d28a86267c7875b8fe083fce5b60eb5e5e82cd7d441550985d248fe41e72a7
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

### 9.1 Summary of Algorithms and Time Bounds {#cytron-1991-ssa-s9-1 .section tag=05B5}

The conversion to SSA form is done in three steps:

(1) The dominance frontier mapping is constructed from the control flow graph $CFG$ (Section 4.2). Let $CFG$ have $N$ nodes and $E$ edges. Let $DF$ be the mapping from nodes to their dominance frontiers. The time to compute the dominator tree and then the dominance frontiers in $CFG$ is $O(E + \sum_X |DF(X)|)$.

(2) Using the dominance frontiers, the locations of the $\phi$-functions for each variable in the original program are determined (Section 5.1). Let $A_{tot}$ be the total number of assignments to variables in the resulting program, where each ordinary assignment statement $LHS \leftarrow RHS$ contributes the length of the tuple $LHS$ to $A_{tot}$, and each $\phi$-function contributes 1 to $A_{tot}$. Placing $\phi$-functions contributes $O(A_{tot} \times avrgDF)$ to the overall time, where $avrgDF$ is the weighted average (7) of the sizes $|DF(X)|$.

(3) The variables are renamed (Section 5.2). Let $M_{tot}$ be the total number of mentions of variables in the resulting program. Renaming contributes $O(M_{tot})$ to the overall time.

To state the time bounds in terms of fewer parameters, let the overall size $R$ of the original program be the maximum of the relevant numbers: $N$ nodes, $E$ edges, $A_{orig}$ original assignments to variables, and $M_{orig}$ original mentions of variables. In the worst case, $avrgDF = \Omega(N) = \Omega(R)$, and $k$ ordinary assignments can require $\Omega(kR)$ insertions of $\phi$-functions. Thus, $A_{tot} = \Omega(R^2)$ at worst. In the worst case, a $\phi$-function has $\Omega(R)$ operands. Thus, $M_{tot} = \Omega(R^3)$ at worst. The one-parameter worst-case time bounds are thus $O(R^2)$ for finding dominance frontiers and $O(R^3)$ for translation to SSA form.

However, the data in Section 8 suggest that the entire translation to SSA form will be linear in practice. The dominance frontier of each node in $CFG$ is small, as is the number of $\phi$-functions added for each variable. In effect, $avrgDF$ is constant, $A_{tot} = O(A_{orig})$, and $M_{tot} = O(M_{orig})$. The entire translation process is effectively $O(R)$.

Control dependences are read off from the dominance frontiers in the reverse graph $RCFG$ (Section 6) in time $O(E + \operatorname{size}(RDF))$. Since the size of $RDF$ is the size of the output of the control dependence calculation, this algorithm is linear in the size of the output. The only quadratic behavior is caused by the output being $\Omega(R^2)$ in the worst case. The data in Section 8 suggest that the control dependence calculation is effectively $O(R)$.

### 9.2 Related Work {#cytron-1991-ssa-s9-2 .section tag=05B6}

Minimal SSA form is a refinement of Shapiro and Saint's [45] notion of a pseudoassignment. The *pseudoassignment nodes* for $V$ are exactly the nodes that need $\phi$-functions for $V$. A closer precursor [22] of SSA form associated new names for $V$ with pseudoassignment nodes and inserted assignments from one new name to another. Without explicit $\phi$-functions, however, it was difficult to manage the new names or reason about the flow of values.

Suppose the control flow graph $CFG$ has $N$ nodes and $E$ edges for a program with $Q$ variables. One algorithm [41] requires $O(E\alpha(E, N))$ bit vector operations (where each vector is of length $Q$) to find all of the pseudoassignments. A simpler algorithm [43] for reducible programs computes SSA form in time $O(E \times Q)$. With lengths of bit vectors taken into account, both of these algorithms are essentially $O(R^2)$ on programs of size $R$, and the simpler algorithm sometimes inserts extraneous $\phi$-functions. The method presented here is $O(R^3)$ at worst, but Section 8 gives evidence that it is $O(R)$ in practice. The earlier $O(R^2)$ algorithms have no provision for running faster in typical cases; they appear to be intrinsically quadratic.

For $CFG$ with $N$ nodes and $E$ edges, previous general control dependence algorithms [24] can take quadratic time in $(N + E)$. This analysis is based on the worst-case $\Omega(N)$ depth of the (post)dominator tree [24, p. 326]. Section 6 shows that control dependences can be determined by computing dominance frontiers in the reverse graph $RCFG$. In general, our approach can also take quadratic time, but the only quadratic behavior is caused by the output being $\Omega(N^2)$ in the worst case. In particular, suppose a program is comprised only of straight-line code, **if-then-else**, and **while-do** constructs. By Corollary 2, our algorithm computes control dependences in linear time. We obtain a better time bound for such programs because our algorithm is based on dominance frontiers, whose sizes are not necessarily related to the depth of the dominator tree. For languages that offer only these constructs, control dependences can also be computed from the parse tree [28] in linear time, but our algorithm is more robust. It handles all cases in quadratic time and typical cases in linear time.

### 9.3 Conclusions {#cytron-1991-ssa-s9-3 .section tag=05B7}

Previous work has shown that SSA form and control dependences can support powerful code optimization algorithms that are highly efficient in terms of time and space bounds based on the size of the program after translation to the forms. We have shown that this translation can be performed efficiently, that it leads to only a moderate increase in program size, and that applying the early steps in the SSA translation to the reverse graph is an efficient way to compute control dependences. This is strong evidence that SSA form and control dependences form a practical basis for optimization.
