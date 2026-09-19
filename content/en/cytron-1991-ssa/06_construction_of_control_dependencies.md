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
section: "6"
section_title: CONSTRUCTION OF CONTROL DEPENDENCIES
tag: 05A5
kind: section
lang: en
source: https://www.cs.utexas.edu/~pingali/CS380C/2010/papers/ssaCytron.pdf
pdf_sha256: 307512bb537628c2b326b23aa02109e7562bfc619509e942e015054ab58eb9ab
pdf_pages: 26-28
extraction: vision
extraction_model: gpt-5
content_sha256: 4997df8c738c095a4a05a6b201ff4dfc4c8e66ebec12681058be1696b10edbb4
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

In this section we show that control dependences [24] are essentially the dominance frontiers in the reverse graph of the control flow graph. Let X and Y be nodes in CFG. If X appears on every path from Y to Exit, then X postdominates Y.8 Like the dominator relation, the postdominator relation is reflexive and transitive. If X postdominates Y but $X \neq Y$, then X strictly postdominates Y. The immediate postdominator of Y is the closest strict postdominator of Y on any path from Y to Exit. In a postdominator tree, the children of a node X are all immediately postdominated by X.

A CFG node Y is control dependent on a CFG node X if both of the following hold:

(1) There is a nonnull path $p: X^+ \to Y$ such that Y postdominates every node after X on p.
(2) The node Y does not strictly postdominate the node X.

In other words, there is some edge from X that definitely causes Y to execute, and there is also some path from X that avoids executing Y. We associate with this control dependence from X to Y the label on the control flow edge from X that causes Y to execute. Our definition of control dependence here can easily be shown to be equivalent to the original definition [24].

Lemma 11. Let X and Y be CFG nodes. Then Y postdominates a successor of X if and only if (iff) there is a nonnull path $p: X^+ \to Y$ such that Y postdominates every node after X on p. {#cytron-1991-ssa-lem-11 .statement tag=05A6}

Proof. Suppose that Y postdominates a successor U of X. Choose any path q from U to Exit. Then Y appears on q. Let r be the initial segment of q that reaches the first appearance of Y on q. For any node V on r, we can get from U to Exit by following r to V and then by taking any path from V to Exit. Because Y postdominates U but does not appear before the end of r, Y must postdominate V as well. Let p be the path that starts with the edge $X \to U$ and then proceeds along r. Then $p: X^+ \to Y$ and Y postdominates every node after X on p.

8The postdominance relation in [24] is irreflexive, whereas the definition we use here is reflexive. The two relations are identical on pairs of distinct elements. We choose the reflexive definition here to make postdominance the dual of the dominance relation.

build $RCFG$
build dominator tree for $RCFG$
apply the algorithm in Figure 10 to find the dominance frontier mapping $RDF$ for $RCFG$

```text
for each node X do CD(X) ← ∅ end
for each node Y do
    for each X ∈ RDF(Y) do
        CD(X) ← CD(X) ∪ { Y }
    end
end
```

Fig. 14. Algorithm for computing the set $CD(X)$ of nodes that are control dependent on $X$. {#cytron-1991-ssa-fig-14 .figure tag=05A7}

| Node | $CD(Node)$ |
| --- | --- |
| Entry | 1,2,8,9,11,12 |
| 1 |  |
| 2 | 3,6,7 |
| 3 | 4,5 |
| 4 |  |
| 5 |  |
| 6 |  |
| 7 |  |
| 8 |  |
| 9 | 10 |
| 10 |  |
| 11 | 9,11 |
| 12 | 2,8,9,11,12 |

Fig. 15. Control dependences of the program in Figure 5. {#cytron-1991-ssa-fig-15 .figure tag=05A8}

Conversely, given a path $p$ with these properties, let $U$ be the first node after $X$ on $p$. Then $U$ is a successor of $X$ and $Y$ postdominates $U$. $\Box$

The reverse control flow graph $RCFG$ has the same nodes as the control flow graph $CFG$, but has an edge $Y \to X$ for each edge $X \to Y$ in $CFG$. The roles of Entry and Exit are also reversed. The postdominator relation on $CFG$ is the dominator relation on $RCFG$.

Corollary 1. Let $X$ and $Y$ be nodes in $CFG$. Then $Y$ is control dependent on $X$ in $CFG$ iff $X \in DF(Y)$ in $RCFG$. {#cytron-1991-ssa-cor-1 .statement tag=05A9}

Proof. Using Lemma 11 to simplify the first condition in the definition of control dependence, we find that $Y$ is control dependent on $X$ iff $Y$ postdominates a successor of $X$ but does not strictly postdominate $X$. In $RCFG$ this means that $Y$ dominates a predecessor of $X$ but does not strictly dominate $X$; that is, $X \in DF(Y)$. $\Box$

Figure 14 applies this result to the computation of control dependences. After building the dominator tree for $RCFG$ by the standard method [35] in time $O(E\alpha(E,N))$, we spend $O(\text{size}(RDF))$ finding dominance frontiers and then inverting them. The total time is thus $O(E + \text{size}(RDF))$ for all practical purposes. By applying the algorithm in Figure 14 to the control flow graph in Figure 5, we obtain the control dependences in Figure 15. Note that the edge from Entry to Exit was added to $CFG$ so that the control dependence relation, viewed as a graph, would be rooted at Entry.
