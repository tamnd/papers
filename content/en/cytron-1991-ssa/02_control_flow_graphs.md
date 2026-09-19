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
section: "2"
section_title: CONTROL FLOW GRAPHS
tag: "0586"
kind: section
lang: en
source: https://www.cs.utexas.edu/~pingali/CS380C/2010/papers/ssaCytron.pdf
pdf_sha256: 307512bb537628c2b326b23aa02109e7562bfc619509e942e015054ab58eb9ab
pdf_pages: 5-7
extraction: vision
extraction_model: gpt-5
content_sha256: 050d2aa2b106d9ececbd60aca8bd125e93644166872b15219fc653ed6efef84e
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The statements of a program are organized into (not necessarily maximal) basic blocks, where program flow enters a basic block at its first statement and leaves the basic block at its last statement [1, 36]. Basic blocks are indicated by the column of numbers in parentheses in Figure 5. A control flow graph is a directed graph whose nodes are the basic blocks of a program and two additional nodes, Entry and Exit. There is an edge from Entry to

```text
I ← 1	(1)
J ← 1	(1)
K ← 1	(1)
L ← 1	(1)
repeat	(2)
    if (P)	(2)
        then do	(3)
            J ← I	(3)
            if (Q)	(3)
                then L ← 2	(4)
                else L ← 3	(5)
            K ← K + 1	(6)
        end	(6)
    else K ← K + 2	(7)
print(I,J,K,L)	(8)
repeat	(9)
    if (R)	(9)
        then L ← L + 4	(10)
until (S)	(11)
I ← I + 6	(12)
until (T)	(12)
```

Fig 5  Simple program and its control flow graph.

any basic block at which the program can be entered, and there is an edge to Exit from any basic block that can exit the program. For reasons related to the representation of control dependences and explained in Section 6, there is also an edge from Entry to Exit. The other edges of the graph represent transfers of control (jumps) between the basic blocks. We assume that each node is on a path from Entry and on a path to Exit. For each node X, a successor of X is any node Y with an edge X → Y in the graph, and Succ(X) is the set of all successors of X; similarly for predecessors. A node with more than one successor is a branch node; a node with more than one predecessor is a join node. Finally, each variable is considered to have an assignment in Entry to represent whatever value the variable may have when the program is entered. This assignment is treated just like the ones that appear explicitly in the code. Throughout this paper, CFG denotes the control flow graph of the program under discussion.

For any nonnegative integer J, a path of length J in CFG consists of a sequence of J + 1 nodes (denoted X₀, ..., X_J) and a sequence of J edges (denoted e₁, ..., e_J) such that e_j runs from X_{j-1} to X_j for all j with 1 ≤ j ≤ J. (We write e_j: X_{j-1} → X_j.) As is usual with sequences, one item (node or edge) may occur several times. The null path, with J = 0, is allowed. We write $p: X_0 \to^* X_J$ for an unrestricted path $p$, but $p: X_0 \to^+ X_J$ if $p$ is known to be nonnull.

Nonnull paths $p: X_0 \to^+ X_J$ and $q: Y_0 \to^+ Y_K$ are said to converge at a node $Z$ if

$$
X_0 \neq Y_0;
$$

$$
X_J = Z = Y_K;
$$

$$
(X_J = Y_k) \Rightarrow (j = J \text{ or } k = K).
$$

Intuitively, the paths $p$ and $q$ start at different nodes and are almost node-disjoint, but they come together at the end. The use of *or* rather than *and* in (3) is deliberate. One of the paths may happen to be a cycle $Z \to^+ Z$, but we still need to consider the possibility of convergence.
