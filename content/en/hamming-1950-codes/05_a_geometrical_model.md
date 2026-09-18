---
paper: hamming-1950-codes
title: Error Detecting and Error Correcting Codes
authors:
  - Richard W. Hamming
year: 1950
venue: Bell System Technical Journal
field: theory
section: "5"
section_title: A GEOMETRICAL MODEL
tag: 03DD
kind: section
lang: en
source: https://archive.org/download/bstj29-2-147/bstj29-2-147.pdf
pdf_sha256: 32f13768d0e37bcc482517d3e1f50f9309d6db65e145edc476622c435829bdad
pdf_pages: 8-10
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: b68d78b6c3f3a071c1a174b6ab2ae602dfba310dbbf884b401edb451cfb730aa
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

When examining various problems connected with error detecting and correcting codes it is often convenient to introduce a geometric model. The model used here consists in identifying the various sequences of 0's and 1's which are the symbols of a code with vertices of a unit $n$-dimensional cube. The code points, labelled $x, y, z, \cdots$, form a subset of the set of all vertices of the cube.

Into this space of $2^n$ points we introduce a *distance*, or, as it is usually called, a *metric*, $D(x, y)$. The definition of the metric is based on the observation that a single error in a code point changes one coordinate, two errors, two coordinates, and in general $d$ errors produce a difference in $d$ coordinates.

Thus we define the distance $D(x, y)$ between two points $x$ and $y$ as the number of coordinates for which $x$ and $y$ are different. This is the same as the least number of edges which must be traversed in going from $x$ to $y$. This distance function satisfies the usual three conditions for a metric, namely,

$$
D(x, y) = 0 \quad \text{if and only if } x = y
$$

$$
D(x, y) = D(y, x) > 0 \quad \text{if } x \neq y
$$

$$
D(z, y) + D(y, z) \geq D(x, z) \text{ (triangle inequality)}.
$$

As an example we note that each of the following code points in the three-dimensional cube is two units away from the others,

$$
\begin{array}{ccc}
0 & 0 & 1 \\
0 & 1 & 0 \\
1 & 0 & 0 \\
1 & 1 & 1 .
\end{array}
$$

To continue the geometric language, a sphere of radius $r$ about a point $x$ is defined as all points which are at a distance $r$ from the point $x$. Thus, in the above example, the first three code points are on a sphere of radius 2 about the point $(1, 1, 1)$. In fact, in this example any one code point may be chosen as the center and the other three will lie on the surface of a sphere of radius 2.

If all the code points are at a distance of at least 2 from each other, then it follows that any single error will carry a code point over to a point that is *not* a code point, and hence is a meaningless symbol. This in turn means that any single error is detectable. If the minimum distance between code points is at least three units then any single error will leave the point nearer to the correct code point than to any other code point, and this means that any single error will be correctable. This type of information is summarized in the following table:

| Minimum Distance | Meaning |
| --- | --- |
| 1 | uniqueness |
| 2 | single error detection |
| 3 | single error correction |
| 4 | single error correction plus double error detection |
| 5 | double error correction Etc. |

Conversely, it is evident that, if we are to effect the detection and correction listed, then all the distances between code points must equal or exceed the minimum distance listed. Thus the problem of finding suitable codes is the same as that of finding subsets of points in the space which maintain at least the minimum distance condition. The special codes in sections 2, 3, and 4 were merely descriptions of how to choose a particular subset of points for minimum distances 2, 3, and 4 respectively.

It should perhaps be noted that, at a given minimum distance, some of the correctability may be exchanged for more detectability. For example, a subset with minimum distance 5 may be used for:
a. double error correction, (with, of course, double error detection).
b. single error correction plus triple error detection.
c. quadruple error detection.

Returning for the moment to the particular codes constructed in Part I we note that any interchanges of positions in a code do not change the code in any essential way. Neither does interchanging the 0's and 1's in any position, a process usually called complementing. This idea is made more precise in the following definition:

Definition. Two codes are said to be equivalent to each other if, by a finite number of the following operations, one can be transformed into the other:
1. The interchange of any two positions in the code symbols.
2. The complementing of the values in any position in the code symbols.
This is a formal equivalence relation ($\sim$) since $A \sim A$; $A \sim B$ implies $B \sim A$; and $A \sim B, B \sim C$ implies $A \sim C$. Thus we can reduce the study of a class of codes to the study of typical members of each equivalence class.

In terms of the geometric model, equivalence transformations amount to rotations and reflections of the unit cube.
