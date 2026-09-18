---
paper: mccabe-1976-complexity
title: A Complexity Measure
authors:
  - Thomas J. McCabe
year: 1976
venue: IEEE Transactions on Software Engineering
field: software
section: VII
section_title: A TESTING METHODOLOGY
tag: 03B0
kind: section
lang: en
source: http://www.literateprogramming.com/mccabe.pdf
pdf_sha256: be2ac1035940dfc7fa231e23b33bfa3c2f3e3d8ef3112e20cf92a35a7af537f6
pdf_pages: 11-12
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: fe26af936cef5986070108e9f811cbb9dd419671cd542ffe3746335104f62fc4
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The complexity measure v is designed to conform to our intuitive notion of complexity and since we often spend as much as 50 percent of our time in test and debug mode the measure should correlate closely with the amount of work required to test a program. In this section the relationship between testing and cyclomatic complexity will be defined and a testing methodology will be developed.

Let us assume that a program P has been written, its complexity v has been calculated, and the number of paths tested is ac (actual complexity). If ac is less than v then one of the following conditions must be true:
1) there is more testing to be done (more paths to be tested);
2) the program flow graph can be reduced in complexity by v-ac (v-ac decisions can be taken out); and
3) portions of the program can be reduced to in line code (complexity has increased to conserve space).

Up to this point the complexity issue has been considered purely in terms of the structure of the control flow. This testing issue, however, is closely related to the data flow because it is the data behavior that either precludes or makes realizable the execution of any particular control path. A few simple examples may help to illustrate. Assume we start with the following flow graph:

G:

Figure.

Suppose that ac = 2 and the two tested paths are [E, a₁, b, c₂, x] and [E, a₂, b, c₁, x]. Then given that paths [E, a₁, b, c₁, x] and [E, a₂, b, c₂, x] cannot be executed we have ac < v so case 2 holds and G can be reduced by removing decision b as in

G1:

Figure.

Notice how in G v = ac and the complexity of G1 is less than the complexity of G.

In experience this approach is most helpful when programmers are required to document their flow graph and complexity and show explicitly the different paths tested. It is often the case when the actual number of paths tested is compared with the cyclomatic complexity that several additional paths are discovered that would normally be overlooked. It should be noted that v is only the minimal number of independent paths that should be tested. There are often additional paths to test. It should also be noted that this procedure (like any other testing method) will by no means guarantee or prove the software—all it can do is surface more bugs and improve the quality of the software.

Two more examples are presented without comment.

G1:

Figure.

TESTS:
a1b1
a2b2
c1b1
c2b2
c3b1 v=6
ac=5 v=5
ac=5

G2:
v=5
ac=2

TESTS:
acdfghik
acefgijabk v=3
ac=2
