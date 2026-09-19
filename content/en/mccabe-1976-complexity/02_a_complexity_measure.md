---
paper: mccabe-1976-complexity
title: A Complexity Measure
authors:
  - Thomas J. McCabe
year: 1976
venue: IEEE Transactions on Software Engineering
field: software
section: II
section_title: A COMPLEXITY MEASURE
tag: 03A8
kind: section
lang: en
source: http://www.literateprogramming.com/mccabe.pdf
pdf_sha256: be2ac1035940dfc7fa231e23b33bfa3c2f3e3d8ef3112e20cf92a35a7af537f6
pdf_pages: 1-2
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: ee4c09aca1159fb862527a558ce6869be0109ceec52aea5ca55f51dd0d061d2f
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

In this section a mathematical technique for program modularization will be developed. A few definitions and theorems from graph theory will be needed, but several examples will be presented in order to illustrate the applications of the technique.

The complexity measure approach we will take is to measure and control the number of paths through a program. This approach, however, immediately raises the following nasty problem: “Any program with a backward branch potentially has an infinite number of paths.” Although it is possible to define a set of algebraic expressions that give the total number of possible paths through a (structured) program,[^1] using the total number of paths has been found to be impractical. Because of this the complexity measure developed here is defined in terms of basic paths—that when taken in combination will generate every possible path.

The following mathematical preliminaries will be needed, all of which can be found in Berge [1].

*Definition 1:* The cyclomatic number V(G) of a graph G with n vertices, e edges, and p connected components is {#mccabe-1976-complexity-def-1 .statement tag=03A9}

$$
v(G) = e - n + p.
$$

*Theorem 1:* In a strongly connected graph G, the cyclomatic number is equal to the maximum number of linearly independent circuits. {#mccabe-1976-complexity-thm-1 .statement tag=03AA}

The applications of the above theorem will be made as follows: Given a program we will associate with it a directed graph that has unique entry and exit nodes. Each node in the graph corresponds to a block of code in the program where the flow is sequential and the arcs correspond to branches taken in the program. This graph is classically known as the program control graph (see Ledgard [6]) and it is assumed that each node can be reached by the entry node and each node can reach the exit node. For example, the following is a program control graph with entry node “a” and exit node “f.”

Figure.

Manuscript received April 10, 1976.  
The author is with the Department of Defense, National Security Agency, Ft. Meade, MD 20755.

[^1]: See the Appendix.

Theorem 1 is applied to G in the following way. Imagine that the exit node (f) branches back to the entry node (a). The control graph G is now strongly connected (there is a path joining any pair of arbitrary distinct vertices) so Theorem 1 applies. Therefore, the maximum number of linearly independent circuits in G is 9-6+2. For example, one could choose the following 5 independent circuits in G: {#mccabe-1976-complexity-thm-1-2 .statement tag=03AB}

B1: (abefa), (beb), (abea), (acfa), (adcfa).

It follows that B1 forms a basis for the set of all circuits in G and any path through G can be expressed as a linear combination of circuits from B1. For instance, the path (abeabebebef) is expressable as (abea) +2(beb) + (abefa). To see how this works its necessary to number the edges on G as in

Figure.

Now for each member of the basis B1 associate a vector as follows:

| | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| (abefa) | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 1 |
| (beb) | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| (abea) | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| (acfa) | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 |
| (adcfa) | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 1 |

The path (abea(be)³fa) corresponds to the vector 2004200111 and the vector addition of (abefa), 2(beb), and (abea) yields the desired result.

In using Theorem 1 one can choose a basis set of circuits that correspond to paths through the program. The set B2 is a basis of program paths.

B2: (abef), (abeabef), (abebef), (acf), (adcf).

Linear combination of paths in B2 will also generate any path. For example,

$$
(abea(be)^3f)=2(abebef)-(abef)
$$

and

$$
(a(be)^2abef)=(a(be)^2f)+(abeabef)-(abef).
$$

The overall strategy will be to measure the complexity of a program by computing the number of linearly independent paths v(G), control the “size” of programs by setting an upper limit to v(G) (instead of using just physical size), and use the cyclomatic complexity as the basis for a testing methodology.

A few simple examples may help to illustrate. Below are the control graphs of the usual constructs used in structured programming and their respective complexities.

Figure.

Notice that the sequence of an arbitrary number of nodes always has unit complexity and that cyclomatic complexity conforms to our intuitive notion of “minimum number of paths.” Several properties of cyclomatic complexity are stated below:

1) $v(G)\geq1$.
2) $v(G)$ is the maximum number of linearly independent paths in G; it is the size of a basis set.
3) Inserting or deleting functional statements to G does not affect $v(G)$.
4) G has only one path if and only if $v(G)=1$.
5) Inserting a new edge in G increases $v(G)$ by unity.
6) $v(G)$ depends only on the decision structure of G.
