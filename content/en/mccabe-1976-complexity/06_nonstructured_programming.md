---
paper: mccabe-1976-complexity
title: A Complexity Measure
authors:
  - Thomas J. McCabe
year: 1976
venue: IEEE Transactions on Software Engineering
field: software
section: VI
section_title: NONSTRUCTURED PROGRAMMING
tag: 03AF
kind: section
lang: en
source: http://www.literateprogramming.com/mccabe.pdf
pdf_sha256: be2ac1035940dfc7fa231e23b33bfa3c2f3e3d8ef3112e20cf92a35a7af537f6
pdf_pages: 8-11
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 36c8be47b68c4901b69c7a81fae8d462ea9f8203777d9dc0a89355bd9e3508fd
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The main thrust in the recent popularization of structured programming is to make programmers aware of a few syntactic constructs$^4$ and tell them that a structured program is one written with only these constructs. One of the difficulties with this approach is it does not define for programmers what constructs they should not use, i.e., it does not tell them what a structured program is not. If the programming population had a notion of what constructs to avoid and they could see the inherent difficulty in these constructs, perhaps the notion of structuring programming would be more psychologically palatable. A clear definition of the constructs that structured programming excludes would also sensitize programmers to their use while programs are being created, which (if we believe in structured programming) would have a desirable effect.

One of the reasons that the author thinks this is important is that as Knuth [4] points out—there is a time and a place when an unstructured goto is needed. The author has had a similar experience structuring Fortran jobs—there are a few very specific conditions when an unstructured construct works best. If it is the case that unstructured constructs should only be allowed under special circumstances, one need then to distinguish between the programmer that makes judicious use of a few unstructured goto's as compared to the programmer that is addicted to them. What would help is first the definition of the unstructured components and second a measure of the structureness of a program as well as the complexity of a program.

Rao Kasaraju [5] has a result which is related—a flow graph is reducible$^5$ to a structured program if and only if it does not contain a loop with two or more exits. This is a deep result but not, however, what we need since many programs that are reducible to structured programs are not structured programs. In order to have programmers explicitly identify and avoid unstructured code we need a theorem that is analogous to a theorem like Kuratowski's theorem in graph theory. Kuratowski's theorem states that any nonplanar graph must contain at least one of two specific nonplanar graphs that he describes. The proof of nonplanarity of a graph is then reducible to locating two specific subgraphs whereas showing nonplanarity without Kuratowski's result is, in general, much more difficult.

The following four control structures were found to generate all nonstructured programs.

Figure.

$^3$ For the CASE construct with N cases use N-1 for the number of conditions. Notice, once again, that a simulation of case with IF's will have N-1 conditions.
$^4$ The usual ones used (sometimes called D-structures) are
$^5$ Reducibility here means the same function is computed with the same actions and predicates although the control structure may differ.
$^6$ Assuming the program does not contain unconditional GOTO's.

D-structures) is that it contains as a subgraph either a), b), or c).

The reason why graph d) was slighted in Result 1 is that any 3 of the 4 graphs will generate all the unstructured programs—this will be illustrated later. It is convenient to verbalize the graphs a)–d), respectively, as follows:

a) branching out of a loop;
b) branching into a loop;
c) branching into a decision; and
d) branching out of a decision.

The following version of Result 2 may seem more intuitively appealing.

A structured program can be written by not “branching out of or into a loop, or out of or into a decision.”

The following result gives insight into why a nonstructured program’s logic often becomes convoluted and entwined.

Result 2: A nonstructured program cannot be just a little nonstructured. That is any nonstructured program must contain at least 2 of the graphs a)–d). Part of the proof of Result 2 will be shown here because it helps to illustrate how the control flow in a nonstructured program becomes entangled. We show, for an example, how graph b) cannot occur alone. Assuming we have graph b):

Figure.

the entry node E occurs either before, after, or from a node independent of the loop. Each of these three cases will be treated separately.

Case 1: E is “before” the loop E is on a path from entry to the loop so the program must have a graph as follows:

Figure.

Notice how E is a split node at the beginning of a decision that is branched into. So in this case we have a c) graph along with the original b) graph.

Case 2: E is “after” the loop. The control graph would appear as follows:

Figure.

Notice how a type a) graph must appear.

Case 3: E is independent of the loop. The control graph would look as follows:

Figure.

The graph c) must now be present with b). If there is another path that can go to a node after the loop from E then a type d) graph is also generated. Things are often this bad, and in fact much worse.

Similar arguments can be made for each of the other nonstructured graphs to show that a)–d) cannot occur alone. If one generates all the possible pairs from a)–d) it is interesting to note that they all reduce to 4 basic types:

Figure.

which leads us the following result.

Result 3: A necessary and sufficient condition for a program to be nonstructured is that it contains at least one of: (a, b), (a, d), (b, c), (c, d). Result 4 is now obvious.

Result 4: The cyclomatic complexity if a nonstructured program is at least 3. It is interesting to notice that when the orientation is taken off the edges each of the 4 basic graphs a)–d) are isomorphic to the following nondirected graph.

Also if the graphs (a, b) through (c, d) have their directions taken off they are all isomorphic to:

Figure.

By examining the graphs (a, b) through (c, d) one can formulate a more elegant nonstructured characterization:
Result 5: A structured program can be written by not branching out of loops or into decisions—a) and d) provide a basis.
Result 6: A structured program can be written by not branching into loops or out of decisions—b) and d) provide a basis.
A way to measure the lack of structure in a program or flow graph will be briefly commented upon. One of the difficulties with the nonstructured graphs mentioned above is that there is no way they can be broken down into subgraphs with one entry and one exit. This is a severe limitation since one way in which program complexity can be controlled is to recognize when the cyclomatic complexity becomes too large—and then identify and remove subgraphs with unique entry and exit nodes.
Result 7: A structured program is reducible$^7$ to a program of unit complexity.
The following example illustrates how a structured program can be reduced.

Figure.

$v = 4$ $v = 3$ $v = 2$ $v = 1$

7Reduction is the process of removing subgraphs (subroutines) with unique entry and exit nodes.

Notice in the nonstructured graphs below, however, that such a reduction process is not possible.

G1: $v = 6$
G2: $v = 6$
G3: $v = 6$

Let m be the number of proper subgraphs with unique entry and exit nodes. Notice in G1, G2, and G3 m is equal to 0, 1, and 2, respectively. The following definition of essential complexity ev is used to reflect the lack of structure.

Definition: ev = v - n.
For the above graphs we have ev(G1) = 6, ev(G2) = 5, and ev(G3) = 4. Notice how the essential complexity indicates the extent to which a graph can be reduced—G1 cannot be reduced at all since its complexity is equal to its essential complexity. G2 and G3, however, can be reduced as follows:

G2':
v(G2') = 5

G3':
v(G3') = 4

This last result is stated for completeness.

Result 8: The essential complexity of a structured program is one.
