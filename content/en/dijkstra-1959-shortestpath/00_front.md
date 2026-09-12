---
paper: dijkstra-1959-shortestpath
title: A Note on Two Problems in Connexion with Graphs
authors:
  - Edsger W. Dijkstra
year: 1959
venue: Numerische Mathematik
field: algorithms
section_title: Front Matter
kind: front
lang: en
source: https://ir.cwi.nl/pub/9256/9256D.pdf
pdf_sha256: ee0938a64a327cf6d60c25115ae98990417224408d9c062f09907a044e045ac0
pdf_pages: 1-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 584ada85ee4b242ab88f6aec897b92de14d45b2b822306bde835bf4e815a61ca
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

Step 1. The shortest branch of set II is removed from this set and added to set I.
