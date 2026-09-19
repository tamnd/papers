---
paper: dijkstra-1959-shortestpath
title: A Note on Two Problems in Connexion with Graphs
authors:
  - Edsger W. Dijkstra
year: 1959
venue: Numerische Mathematik
field: algorithms
section_title: Front Matter
tag: 003D
kind: front
lang: en
source: https://ir.cwi.nl/pub/9256/9256D.pdf
pdf_sha256: ee0938a64a327cf6d60c25115ae98990417224408d9c062f09907a044e045ac0
pdf_pages: 1-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: a31154142bc70b6cc2902b02475a56116828fb179aef58c75e01773274da4b43
prompt_sha256: 329630a0b9175a55e4af1b8e281a3e67eeab250f8d643953b7dcde99743c7628
---

A Note on Two Problems in Connexion with Graphs

By
E. W. DIJKSTRA

We consider $n$ points (nodes), some or all pairs of which are connected by a branch; the length of each branch is given. We restrict ourselves to the case where at least one path exists between any two nodes. We now consider two problems.

Problem 1. Construct the tree of minimum total length between the $n$ nodes. (A tree is a graph with one and only one path between every two nodes.)

In the course of the construction that we present here, the branches are subdivided into three sets:
I. the branches definitely assigned to the tree under construction (they will form a subtree);
II. the branches from which the next branch to be added to set I, will be selected;
III. the remaining branches (rejected or not yet considered).

The nodes are subdivided into two sets:
A. the nodes connected by the branches of set I,
B. the remaining nodes (one and only one branch of set II will lead to each of these nodes).

We start the construction by choosing an arbitrary node as the only member of set A, and by placing all branches that end in this node in set II. To start with, set I is empty. From then onwards we perform the following two steps repeatedly.

Step 1. The shortest branch of set II is removed from this set and added to set I. As a result one node is transferred from set $B$ to set $A$.

Step 2. Consider the branches leading from the node, that has just been transferred to set A, to the nodes that are still in set B. If the branch under consideration is longer than the corresponding branch in set II, it is rejected; if it is shorter, it replaces the corresponding branch in set II, and the latter is rejected.

We then return to step 1 and repeat the process until sets II and B are empty. The branches in set I form the tree required.

The solution given here is to be preferred to the solution given by J. B. KRUSKAL [1] and those given by H. LOBERMAN and A. WEINBERGER [2]. In their solutions all the — possibly $\frac{1}{2} n(n-1)$ — branches are first of all sorted according to length. Even if the length of the branches is a computable function of the node coordinates, their methods demand that data for all branches are stored simultaneously. Our method only requires the simultaneous storing of the data for at most $n$ branches, viz. the branches in sets I and II and the branch under consideration in step 2.

Problem 2. Find the path of minimum total length between two given nodes $P$ and $Q$.

We use the fact that, if $R$ is a node on the minimal path from $P$ to $Q$, knowledge of the latter implies the knowledge of the minimal path from $P$ to $R$. In the solution presented, the minimal paths from $P$ to the other nodes are constructed in order of increasing length until $Q$ is reached.

In the course of the solution the nodes are subdivided into three sets:
A. the nodes for which the path of minimum length from $P$ is known; nodes will be added to this set in order of increasing minimum path length from node $P$;
B. the nodes from which the next node to be added to set A will be selected; this set comprises all those nodes that are connected to at least one node of set A but do not yet belong to A themselves;
C. the remaining nodes.

The branches are also subdivided into three sets:
I. the branches occurring in the minimal paths from node $P$ to the nodes in set A;
II. the branches from which the next branch to be placed in set I will be selected; one and only one branch of this set will lead to each node in set B;
III. the remaining branches (rejected or not yet considered).

To start with, all nodes are in set C and all branches are in set III. We now transfer node $P$ to set A and from then onwards repeatedly perform the following steps.

Step 1. Consider all branches $r$ connecting the node just transferred to set A with nodes $R$ in sets B or C. If node $R$ belongs to set B, we investigate whether the use of branch $r$ gives rise to a shorter path from $P$ to $R$ than the known path that uses the corresponding branch in set II. If this is not so, branch $r$ is rejected; if, however, use of branch $r$ results in a shorter connexion between $P$ and $R$ than hitherto obtained, it replaces the corresponding branch in set II and the latter is rejected. If the node $R$ belongs to set C, it is added to set B and branch $r$ is added to set II.

Step 2. Every node in set B can be connected to node $P$ in only one way if we restrict ourselves to branches from set I and one from set II. In this sense each node in set B has a distance from node $P$: the node with minimum distance from $P$ is transferred from set B to set A, and the corresponding branch is transferred from set II to set I. We then return to step 1 and repeat the process until node $Q$ is transferred to set A. Then the solution has been found.

Remark 1. The above process can also be applied in the case where the length of a branch depends on the direction in which it is traversed. {#dijkstra-1959-shortestpath-rem-1 .statement tag=0418}

Remark 2. For each branch in sets I and II it is advisable to record its two nodes (in order of increasing distance from $P$), and the distance between $P$ and that node of the branch that is furthest from $P$. For the branches of set I this is the actual minimum distance, for the branches of set II it is only the minimum thus far obtained. {#dijkstra-1959-shortestpath-rem-2 .statement tag=0419}

The solution given above is to be preferred to the solution by L. R. Ford [3] as described by C. Berge [4], for, irrespective of the number of branches, we need not store the data for all branches simultaneously but only those for the branches in sets I and II, and this number is always less than $n$. Furthermore, the amount of work to be done seems to be considerably less.
