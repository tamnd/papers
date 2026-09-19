---
paper: wegman-1991-sccp
title: Constant Propagation with Conditional Branches
authors:
  - Mark N. Wegman
  - F. Kenneth Zadeck
year: 1991
venue: ACM TOPLAS
field: languages
section: "5"
section_title: OBSERVATIONS ON THE CONSTANT PROPAGATION ALGORITHMS
tag: 05C7
kind: section
lang: en
source: https://www.cs.utexas.edu/users/lin/cs380c/wegman.pdf
pdf_sha256: 40929436cdf1c477f2318221df5d0aa71488db4a01cc448b184e0aba8bf95ddb
pdf_pages: 15-19
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 09e148ebca70a9e32a1cced6078d96afe6f70314cfca744a4d31598dcb205ffd
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Several problems can arise in implementations of constant propagation algorithms that affect the quality of the solution (the number of constants found) as well as the asymptotic complexity.

### 5.1 Finding the Maximal Fixed Point {#wegman-1991-sccp-s5-1 .section tag=05C8}

SSC was not the first algorithm to use a sparse representation for propagation; it was, however, the first to use such a representation and to find all simple constants. Many global constant propagation algorithms in common use resemble SSC but do not achieve the same results. In these weaker algorithms, propagation at a use is deferred until all edges that reach that use have been visited. If they all have the same value, the join node is given that value. These algorithms start with the assumption that all expressions have $\bot$ and attempt to raise the lattice value to $\mathcal{C}$ when it can be proven that all values reaching that location are constant. Each SSA edge is visited only once. The weaker algorithms are *pessimistic* in their propagation: They never propagate any value unless they are certain that the value will never be invalidated.

Fig. 10. A simple program loop. {#wegman-1991-sccp-fig-10 .figure tag=05C9}

$$
\begin{aligned}
& l \leftarrow 1 \\
& \text{while}(\ldots) \text{do} \\
& \quad j \leftarrow i \\
& \quad i \leftarrow f(\ldots) \\
& \quad \ldots \{\text{no stores are done into } j \text{ here}\} \\
& \quad i \leftarrow j \\
& \text{end}
\end{aligned}
$$

All of the algorithms presented in this paper, on the other hand, are optimistic. They start with the possibly incorrect assumption that everything may be constant and determine the values that may not be constant. If an optimistic algorithm is stopped before it terminates naturally, the information gathered may be wrong. Pessimistic algorithms may be stopped at any time and still produce correct (though poor) results.

The major drawback of the pessimistic approach is that propagation cannot proceed around cycles in the SSA graph. These cycles are typically the result of simple loops in the program. SSC finds more constants than the weaker algorithms, since SSC can propagate through loops. In Figure 10, the variable $i$ always has the value 1 at the bottom of the loop. The weaker algorithms get stuck on the loop and fail to discover this constant.

In practice, the difference between the optimistic and pessimistic versions of SC or SSC would be quite small. When conditional branches are considered, however, as in CC or SCC, the differences could be significant, particularly when these algorithms are used for procedure integration or type determination, as discussed in Section 6.2.

More precisely, these weaker algorithms find a fixed point that is not maximal. A fixed point is defined by saying that:

(1) The lattice element at each node represents what is provably true at a node.
(2) We have functions whose domain and range is the lattice and these functions represent what changes in state take place when we go from node to node.
(3) If $f$ is a function associated with the transition from node $u$ to node $v$, then the lattice element at $v$ is less than or equal to (in the lattice-theoretic sense) $f$ applied to the lattice element at $u$.

The maximal fixed point is the fixed point with the largest lattice elements at the nodes and has been used as a minimal acceptable criterion of the quality of flow analysis (see Kam and Ullman [25] and Graham and Wegman [21]). Several pessimistic versions of SSC have been published and implemented. These include an algorithm described by Kennedy in chapter 6 of [14], an algorithm in chapter 4 of [30], and an algorithm by Kennedy in chapter 1 of [28]. Two optimistic versions of SSC have been published, the first by Reif and Lewis [32, 33] and the second by Ferrante and Ottenstein [19].

Several versions of SC have also been published. The first, by Kildall [26], also appears in [1]; a generalization of this was published by Kam and

```text
(a) i ← 1
    j ← 2
    if j = 2
(b) then i ← 3
(c) ... ← i
```

Fig. 11. Constant not found with def-use chains. {#wegman-1991-sccp-fig-11 .figure tag=05CA}

Ullman [25]. Each of these is optimistic, although none has made the observations made here to reduce the worst case complexity from cubic to quadratic.

### 5.2 Def-Use Chains {#wegman-1991-sccp-s5-2 .section tag=05CB}

Many constant propagation algorithms work on a graph of *def-use chains*. This data structure is common in optimizing compilers and is described in many textbooks on compilers, such as the one by Aho, Sethi, and Ullman [1]. Def-use chains can cause two problems with the algorithms presented here.

A def-use chain is a connection from a *definition site* for a variable to a *use site* for that variable. A definition site for a variable is a statement that assigns to the variable. A use site is normally an operand of an expression. There is a def-use chain between a definition site and a use site if the use site can be reached from a definition site along the program flow graph without passing through another definition site for that variable.

If SCC is performed using def-use chains rather than the SSA graph, some constants are missed, because def-use chains exist along paths that are not executable. Consider the program shown in Figure 11. Statement (b) provides the only possible value for statement (c), because the path through (b) is the only path to (c) (we know this because the condition must always be true). A def-use chain version of SCC does not find this because it applies the def-use chain that starts from (a) and the algorithm does not know that the value is really killed by (b).

Another shortcoming of def-use chains is related to the size of the graph. In def-use chains, many definitions can reach a use. The number of def-use chains for a single variable can be $N^2$, and thus the worst case complexity of an algorithm that uses def-use chains is $N^2 \times V$. In the SSA graph, however, only one definition reaches each use, and only $N \phi$-functions can be inserted for each variable. This means that the worst case complexity of a constant propagation algorithm that uses the SSA graph is only $N \times V$.

Figure 12 shows a program in which the def-use chain graph grows as $N^2$. Here each of several definition sites for each variable reaches each use site for each variable. This does not occur in the SSA graph, since a $\phi$-function is inserted at the join node.

### 5.3 Nodes versus Edges {#wegman-1991-sccp-s5-3 .section tag=05CC}

In the algorithms presented here, the ExecutableFlag is associated with the program flow graph edges rather than the nodes. Two nodes may be executable and there may be an edge between them, but that edge may not be traversable. In Figure 13, if p can be determined always to be false, then i

```text
select j
    when x {1 ← 1}
    when y {1 ← 2}
    when z {1 ← 3}
end
select k
    when x {a ← i}
    when y {b ← i}
    when z {c ← i}
end
```

Original Program

Def-Use Chains for Previous Program

SSA Graph for Previous Program will be 10 after execution of the loop. If the ExecutableFlag is associated with the nodes rather than the edges in the graph, then i will have the value $\perp$ at the end of the loop.

Fig. 12. Worst-case behavior of def-use chains. {#wegman-1991-sccp-fig-12 .figure tag=05CD}

An alternative way of implementing this would be to add nodes to the graph and then associate an ExecutableFlag with each node. An additional node must be inserted between any node that has more than one immediate i ← 1
while (true) do
    if p
        then exit
    i ← i + 1
    if i = 10
        then exit
end
print i successor and any successor node that has more than one immediate predecessor. Such a transformation has the effect of changing if - then statements to if - then - else statements and also adds nodes at the destinations of gotos and loop-exits. Since this transformation also improves redundancy elimination algorithms [27, 13, 38], it may be the method of choice.

### 5.4 Expression Evaluation {#wegman-1991-sccp-s5-4 .section tag=05CE}

An expression may be evaluated twice for each of its operands, since the LatticeCell associated with each operand may be lowered twice. If the expression is large, this can be expensive. Reif and Lewis [32] store expressions as trees and evaluate the leaves and internal nodes of the tree only as their values change, and we suggest doing the same. As most expressions in most programs are small, however, this improvement may be of only theoretical interest.
