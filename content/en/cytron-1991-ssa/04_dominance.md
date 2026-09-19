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
section: "4"
section_title: DOMINANCE
tag: 058C
kind: section
lang: en
source: https://www.cs.utexas.edu/~pingali/CS380C/2010/papers/ssaCytron.pdf
pdf_sha256: 307512bb537628c2b326b23aa02109e7562bfc619509e942e015054ab58eb9ab
pdf_pages: 13-19
extraction: vision
extraction_model: gpt-5
content_sha256: ebf4835acb67f502804c2c0a789d7efe741f1ca2fcab5e6493924ae7f4ddfacf
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Section 4.1 reviews the dominance relation [47] between nodes in the control flow graph and how to summarize this relation in a dominator tree. Section 4.2 introduces the *dominance frontier* mapping and gives an algorithm for its computation.

### 4.1 Dominator Trees {#cytron-1991-ssa-s4-1 .section tag=058D}

Let $X$ and $Y$ be nodes in the control flow graph $CFG$ of a program. If -$X$ appears on every path from **Entry** to $Y$, then $X$ *dominates* $Y$. Domination is both reflexive and transitive. If $X$ dominates $Y$ and $X \neq Y$, then $X$ *strictly*

Fig. 9  Control flow graph and dominator tree of the simple program  The sets of nodes listed in () and [ ] brackets summarize the dominance frontier calculation from Section 4.2. Each node $X$ is annotated with two sets $[DF_{local}(X)|DF(X)]$ and a third set $(DF_{up}(X))$.

dominates $Y$. In formulas, we write $X \gg Y$ for strict domination and $X \geq Y$ for domination. If $X$ does *not* strictly dominate $Y$, we write $X \not\gg Y$. The *immediate dominator* of $Y$ (denoted $idom(Y)$) is the closest strict dominator of $Y$ on any path from Entry to $Y$. In a *dominator tree*, the children of a node $X$ are all immediately dominated by $X$. The root of a dominator tree is Entry, and any node $Y$ other than Entry has $idom(Y)$ as its parent in the tree. The dominator tree for $CFG$ from Figure 5 is shown in Figure 9. Let $N$ and $E$ be the numbers of nodes and edges in $CFG$. The dominator tree can be constructed in $O(E \alpha(E, N))$ time [35] or (by a more difficult algorithm) in $O(E)$ time [26]. For all practical purposes, $\alpha(E, N)$ is a small constant,$^4$ so this paper will consider the dominator tree to have been found in linear time.

The dominator tree of $CFG$ has exactly the same set of nodes as $CFG$ but a very different set of edges. Here, the words *predecessor*, *successor*, and *path* always refer to $CFG$. The words *parent*, *child*, *ancestor*, and *descendant* always refer to the dominator tree.

$^4$Under the definition of $\alpha$ used in analyzing the dominator tree algorithm [35, p. 123], $N \leq E$ implies that $\alpha(E, N) = 1$ when $\log_2 N < 16$ and $\alpha(E, N) = 2$ when $16 \leq \log_2 N < 2^{16}$.

### 4.2 Dominance Frontiers {#cytron-1991-ssa-s4-2 .section tag=058E}

The dominance frontier $DF(X)$ of a $CFG$ node $X$ is the set of all $CFG$ nodes $Y$ such that $X$ dominates a predecessor of $Y$ but does not strictly dominate $Y$:

$$
DF(X) = \{ Y \mid (\exists P \in Pred(Y)) (X \gg P \text{ and } X \not\gg Y) \}.
$$

Computing $DF(X)$ directly from the definition would require searching much of the dominator-tree. The total time to compute $DF(X)$ for all nodes $X$ would be quadratic, even when the sets themselves are small. To compute the dominance frontier mapping in time linear in the size $\sum_X |DF(X)|$ of the mapping, we define two intermediate sets $DF_{local}$ and $DF_{up}$ for each node such that the following equation holds:

$$
DF(X) = DF_{local}(X) \cup \bigcup_{Z \in Children(X)} DF_{up}(Z).
$$

Given any node $X$, some of the successors of $X$ may contribute to $DF(X)$. This local contribution $DF_{local}(X)$ is defined by

$$
DF_{local}(X) \overset{\text{def}}{=} \{ Y \in Succ(X) \mid X \not\gg Y \}.
$$

Given any node $Z$ that is not the root Entry of the dominator tree, some of the nodes in $DF(Z)$ may contribute to $DF(idom(Z))$. The contribution $DF_{up}(Z)$ that $Z$ passes up to $idom(Z)$ is defined by

$$
DF_{up}(Z) \overset{\text{def}}{=} \{ Y \in DF(Z) \mid idom(Z) \not\gg Y \}.
$$

Lemma 1. *The dominance frontier equation (4) is correct.* {#cytron-1991-ssa-lem-1 .statement tag=058F}

Proof. Because dominance is reflexive, $DF_{local}(X) \subseteq DF(X)$. Because dominance is transitive, each child $Z$ of $X$ has $DF_{up}(Z) \subseteq DF(X)$. We must still show that everything in $DF(X)$ has been accounted for. Suppose $Y \in DF(X)$, and let $U \to Y$ be an edge such that $X$ dominates $U$ but does not strictly dominate $Y$. If $U = X$, then $Y \in DF_{local}(X)$, and we are done. If $U \neq X$, on the other hand, then there is a child $Z$ of $X$ that dominates $U$ but cannot strictly dominate $Y$ because $X$ does not strictly dominate $Y$. This implies that $Y \in DF_{up}(Z)$.

The intermediate sets can be computed with simple equality tests as follows:

Lemma 2. *For any node $X$,* {#cytron-1991-ssa-lem-2 .statement tag=0590}

$$
DF_{local}(X) = \{ Y \in Succ(X) \mid idom(Y) \neq X \}.
$$

Proof. We assume that $Y \in Succ(X)$ and show that

$$
(X \gg Y) \Leftrightarrow (idom(Y) = X).
$$

The $\Leftarrow$ part is true because the immediate dominator is defined to be a *strict* dominator. For the $\Rightarrow$ part, suppose that $X$ strictly dominates $Y$ and, hence,

```text
for each X in a bottom-up traversal of the dominator tree do
DF(X) ← ∅
for each Y ∈ Succ(X) do
/*local*/ if idom(Y) ≠ X then DF(X) ← DF(X) ∪ {Y}
end
for each Z ∈ Children(X) do
for each Y ∈ DF(Z) do
/*up*/ if idom(Y) ≠ X then DF(X) ← DF(X) ∪ {Y}
end
end
end
```

Fig. 10. Calculation of $DF(X)$ for each $CFG$ node $X$. {#cytron-1991-ssa-fig-10 .figure tag=0591}

that some child $V$ of $X$ dominates $Y$. Then $V$ appears on any path from Entry to $Y$ that goes to $X$ and then follows the edge $X \rightarrow Y$, so either $V$ dominates $X$ or $V = Y$. But $V$ cannot dominate $X$, so $V = Y$ and $idom(Y) = idom(V) = X$. $\Box$

Lemma 3. For any node $X$ and any child $Z$ of $X$ in the dominator tree, {#cytron-1991-ssa-lem-3 .statement tag=0592}

$$
DF_{up}(Z) = \{ Y \in DF(Z) \mid idom(Y) \neq X \}.
$$

Proof. We assume that $Y \in DF(Z)$ and show that

$$
(X \gg Y) \Leftrightarrow (idom(Y) = X).
$$

The $\Leftarrow$ part is true because strict dominance is the transitive closure of immediate dominance. For the $\Rightarrow$ part, suppose that $X$ strictly dominates $Y$ and, hence, that some child $V$ of $X$ dominates $Y$. Choose a predecessor $U$ of $Y$ such that $Z$ dominates $U$. Then $V$ appears on any path from Entry to $Y$ that goes to $U$ and then follows the edge $U \rightarrow Y$, so either $V$ dominates $U$ or $V = Y$. If $V = Y$, then $idom(Y) = idom(V) = X$, and we are done. Suppose that $V \neq Y$ (and, hence, that $V$ dominates $U$) and derive a contradiction. Only one child of $X$ can dominate $U$, so $V = Z$ and $Z$ dominates $Y$. This contradicts the hypothesis that $Y \in DF(Z)$. $\Box$

These results imply the correctness of the algorithm for computing the dominance frontiers given in Figure 10. The /*local*/ line effectively computes $DF_{local}(X)$ on the fly and uses it in (4) without needing to devote storage to it. The /*up*/ line is similar for $DF_{up}(Z)$. We traverse the dominator tree bottom-up, visiting each node $X$ only after visiting each of its children. To illustrate the working of this algorithm, we have annotated the dominator tree in Figure 9 with the information [ ] and () brackets.

Theorem 1. The algorithm in Figure 10 is correct. {#cytron-1991-ssa-thm-1 .statement tag=0593}

Proof. Direct from the preceding lemmas. $\Box$

Let $CFG$ have $N$ nodes and $E$ edges. The loop over $Succ(X)$ in Figure 10 examines each edge just once, so all executions of the /*local*/ line are complete in time $O(E)$. Similarly, all executions of the /*up*/ line are complete in time $O(\mathrm{size}(DF))$. The overall time is thus $O(E + \mathrm{size}(DF))$, which amounts to a worst-case complexity of $O(E + N^2)$. However, Section 8 shows that, in practice, the size of the mapping $DF$ is usually linear. We have implemented this algorithm and have observed that it is faster than the standard data-flow computations in the PTRAN compiler [2].

### 4.3 Relating Dominance Frontiers to Joins {#cytron-1991-ssa-s4-3 .section tag=0594}

We start by stating more formally the nonrecursive characterization of where the $\phi$-functions should be located. Given a set $\mathcal{S}$ of $CFG$ nodes, the set $J(\mathcal{S})$ of *join* nodes is defined to be the set of all nodes $Z$ such that there are two nonnull $CFG$ paths that start at two distinct nodes in $\mathcal{S}$ and converge at $Z$. The *iterated* join $J^+(\mathcal{S})$ is the limit of the increasing sequence of sets of nodes

$$
J_1 = J(\mathcal{S});
$$

$$
J_{i+1} = J(\mathcal{S} \cup J_i).
$$

In particular, if $\mathcal{S}$ happens to be the set of assignment nodes for a variable $V$, then $J^+(\mathcal{S})$ is the set of $\phi$-function nodes for $V$.

The join and iterated join operations map sets of nodes to sets of nodes. We extend the dominance frontier mapping from nodes to sets of nodes in the natural way:

$$
DF(\mathcal{S}) = \bigcup_{X \in \mathcal{S}} DF(X).
$$

As with join, the *iterated* dominance frontier $DF^+(\mathcal{S})$ is the limit of the increasing sequence of sets of nodes

$$
DF_1 = DF(\mathcal{S});
$$

$$
DF_{i+1} = DF(\mathcal{S} \cup DF_i).
$$

The actual computation of $DF^+(\mathcal{S})$ is performed by the efficient worklist algorithm in Section 5.1; the formulation here is convenient for relating iterated dominance frontiers to iterated joins. If the set $\mathcal{S}$ is the set of assignment nodes for a variable $V$, then we will show that

$$
J^+(\mathcal{S}) = DF^+(\mathcal{S})
$$

(this equation depends on the fact that **Entry** is in $\mathcal{S}$) and, hence, that the location of the $\phi$-functions for $V$ can be computed by the worklist algorithm for computing $DF^+(\mathcal{S})$ that is given in Section 5.1.

The following lemmas do most of the work by relating dominance frontiers to joins:

**Lemma 4.** *For any nonnull path p: $X \rightarrow^+ Z$ in $CFG$, there is a node $X' \in \{ X \} \cup DF^+(\{ X \})$ on p that dominates $Z$. Moreover, unless $X$ dominates every node on p, the node $X'$ can be chosen in $DF^+(\{ X \})$.* {#cytron-1991-ssa-lem-4 .statement tag=0595}

**Proof.** If $X$ dominates every node on $p$, then we just choose $X' = X$ to get all the claimed properties of $X'$. We may assume that some of the nodes on $p$ are *not* dominated by $X$. Let the sequence of nodes on $p$ be $X = X_0, \ldots, X_J = Z$. For the smallest $i$ such that $X$ does not dominate $X_i$, the predecessor $X_{i-1}$ is dominated by $X$ and so puts $X_i$ into $DF(X)$. Thus, there are choices of $j$ with $X_j \in DF^+(\{X\})$. Consider $X' = X_j$ for the largest $j$ with $X_j \in DF^+(\{X\})$. We will show that $X' \gg Z$. Suppose not. Then $j < J$, and there is a first $k$ with $j < k \leq J$ such that $X'$ does not dominate $X_k$. The predecessor $X_{k-1}$ is dominated by $X'$ and so puts $X_k$ into $DF(X')$. Thus, $X_k \in DF(DF^+(\{X\})) = DF^+(\{X\})$, contradicting the choice of $j$.

**Lemma 5.** *Let $X \neq Y$ be two nodes in CFG, and suppose that nonnull paths $p: X \to^+ Z$ and $q: Y \to^+ Z$ in CFG converge at $Z$. Then $Z \in DF^+(\{X\}) \cup DF^+(\{Y\})$.* {#cytron-1991-ssa-lem-5 .statement tag=0596}

**Proof.** We consider three cases that are obviously exhaustive. In the first two cases, we prove that $Z \in DF^+(\{X\}) \cup DF^+(\{Y\})$. Then we show that the first two cases are (unobviously) exhaustive because the third case leads to a contradiction. Let $X'$ be from Lemma 4 for the path $p$, with the sequence of nodes $X = X_0, \ldots, X_J = Z$. Let $Y'$ be from Lemma 4 for the path $q$, with the sequence of nodes $Y = Y_0, \ldots, Y_K = Z$.

*Case 1.* We suppose that $X'$ is on $q$ and show that $Z \in DF^+(\{X\})$. By the definition of convergence (specifically, (3) in Section 2), $X' = Z$. We may now assume that $Z = X$ and $X$ dominates every node on $p$. (Otherwise, Lemma 4 already asserts $Z \in DF^+(\{X\})$.) Because $X$ dominates the predecessor $X_{J-1}$ of $Z$ but does not *strictly* dominate $Z$, we have $Z \in DF(X) \subseteq DF^+(\{X\})$.

*Case 2.* We suppose that $Y'$ is on $p$, and show that $Z \in DF^+(\{Y\})$, reasoning just as in Case 1.

*Case 3.* We derive a contradiction from the suppositions that $X'$ is *not* on $q$ and $Y'$ is *not* on $p$. Because $X' \gg Z$ but $X'$ is not on $q$, $X' \gg Y_K = Z$ and, therefore, dominates all predecessors of $Y_K$. In particular, $X' \gg Y_{K-1}$. But $X' \neq Y_{K-1}$, so $X' \gg Y_{K-1}$, and we continue inductively to show that $X' \gg Y_k$ for all $k$. In particular, $X' \gg Y'$. On the other hand, by similar reasoning from the supposition that $Y' \gg Z$ but $Y'$ is not on $p$, we can show that $Y' \gg X'$. Two nodes cannot strictly dominate each other, so Case 3 is impossible.

**Lemma 6.** *For any set $\mathcal{S}$ of CFG nodes, $J(\mathcal{S}) \subseteq DF^+(\mathcal{S})$.* {#cytron-1991-ssa-lem-6 .statement tag=0597}

**Proof.** We apply Lemma 5.

**Lemma 7.** *For any set $\mathcal{S}$ of CFG nodes such that **Entry** $\in \mathcal{S}$, $DF(\mathcal{S}) \subseteq J(\mathcal{S})$.* {#cytron-1991-ssa-lem-7 .statement tag=0598}

**Proof.** Consider any $X \in \mathcal{S}$ and any $Y \in DF(X)$. There is a path from $X$ to $Y$ where all nodes before $Y$ are dominated by $X$. There is also a path from **Entry** to $Y$ where *none* of the nodes are dominated by $X$. The paths therefore converge at $Y$.

**Theorem 2.** *The set of nodes that need $\phi$-functions for any variable V is the iterated dominance frontier $DF^+(\mathcal{S})$, where $\mathcal{S}$ is the set of nodes with assignments to V.* {#cytron-1991-ssa-thm-2 .statement tag=0599}

Proof. By Lemma 6 and induction on $i$ in the definition of $J^+$, we can show that

$$
J^+(\mathcal{S}) \subseteq DF^+(\mathcal{S}).
$$

The induction step is as follows:

$$
J_{i+1} = J(\mathcal{S} \cup J_i) \subseteq J(\mathcal{S} \cup DF^+(\mathcal{S}))
$$

$$
\subseteq DF^+(\mathcal{S} \cup DF^+(\mathcal{S})) = DF^+(\mathcal{S}).
$$

The node Entry is in $\mathcal{S}$, so Lemma 7 and another induction yield

$$
DF^+(\mathcal{S}) \subseteq J^+(\mathcal{S}).
$$

The induction step is as follows:

$$
DF_{i+1} = DF(\mathcal{S} \cup DF_i) \subseteq DF(\mathcal{S} \cup J^+(\mathcal{S}))
$$

$$
\subseteq J(\mathcal{S} \cup J^+(\mathcal{S})) = J^+(\mathcal{S}).
$$

The set of nodes that need $\phi$-functions for $V$ is precisely $J^+(\mathcal{S})$, so (5) and (6) prove the theorem. □
