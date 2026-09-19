---
paper: sutherland-1963-sketchpad
title: 'Sketchpad: A Man-Machine Graphical Communication System'
authors:
  - Ivan E. Sutherland
year: 1963
venue: MIT PhD thesis / AFIPS Spring Joint Computer Conference
field: graphics
section_title: Appendix F
kind: appendix
lang: en
source: https://www.cl.cam.ac.uk/techreports/UCAM-CL-TR-574.pdf
pdf_sha256: e052281b553622badc8dd308003c127617aa5723e4ec3dbfa79b781d8e712742
pdf_pages: 135-136
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: aa9034738f54589ba88fd7870f2815e7390e442d70365c79deb53e729b3546be
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

MATHEMATICS OF LEAST MEAN SQUARE FIT

The result quoted in this appendix is well known and is repeated here only for reference.
Suppose we have $P$ equations in $N$ unknowns:

$$
\sum_{j=1}^{N} a_{ij} x_j = c_i \quad 1 \leq i \leq P; \quad \text{or} \quad AX = C.
$$

If $P$ is larger than $N$ there would in general be no exact solution. We wish to find the values for the unknowns which minimize the sum of the squared errors of the equations. The error in the $i^{th}$ equality is given by:

$$
E_i = \sum_{j=1}^{N} (a_{ij} x_j - c_i),
$$

and the total squared error,

$$
E_t = \sum_{i=1}^{P} \left[ \sum_{j=1}^{N} (a_{ij} x_j) - c_i \right]^2.
$$

We wish to minimize $E_t$, and so we take partials with respect to each $x_j$ and set all these equal to zero. For a particular $x_j$ called $x_k$,

$$
\frac{\delta E_t}{\delta x_k} = \frac{\delta}{\delta x_k} \sum_{i=1}^{P} \left[ \sum_{j=1}^{N} (a_{ij} x_j) - c_i \right]^2.
$$

Since the partial of a sum is equal to the sum of the partials,

$$
\frac{\delta E_t}{\delta x_k} = \sum_{i=1}^{P} \frac{\delta}{\delta x_k} \left[ \sum_{j=1}^{N} (a_{ij} x_j) - c_i \right]^2,
$$

or since $\frac{\delta}{\delta x}(Q)^2 = 2Q \frac{\delta}{\delta x} Q$,

$$
\frac{\delta E^2}{\delta x_k} = \sum_{i=1}^{P} 2 \left[ \sum_{j=1}^{N} (a_{ij} x_j) - c_i \right] \frac{\delta}{\delta x_k} \left[ \sum_{j=1}^{N} (a_{ij} x_j) - c_i \right].
$$

Now the last part of (F-6) is a sum of terms like $a_{12}x_2 \ldots$ only one of which involves $x_k$ at all, namely $a_{ik}x_k$. Therefore,

$$
\frac{\delta E^2}{\delta x_k} = \sum_{i=1}^P 2 \left[ \sum_{j=1}^N (a_{ij} x_j) - c_i \right] (a_{ik}),
$$

which, when set equal to zero gives

$$
0 = \sum_{i=1}^P \left[ \sum_{j=1}^N (a_{ik} a_{ij} x_j) - a_{ik} c_i \right],
$$

or

$$
\sum_{i=1}^P \sum_{j=1}^N a_{ik} a_{ij} x_j = \sum_{i=1}^P a_{ik} c_i.
$$

Changing the order os summation,

$$
\sum_{j=1}^N \left( \sum_{i=1}^P a_{ik} a_{ij} \right) x_j = \left( \sum_{i=1}^P a_{ik} c_i \right),
$$

which in matrix notation becomes:

$$
A^T A X = A^T C.
$$

$A^T A$ is a square matrix of order $N$. Thus a system of any number of linear equations can be reduced to a simpler system whose solution is the value of the variables for least square fit to the original set of equations.

If the original equations are equations in two unknowns, a plot of (F-2) with error squared in the upward direction is a parabolic valley. Since any vertical section of a parabolic valley will be a parabola, and the sum of any two parabolas in likewise a parabola, a plot of (F-3) can at most be an eliptic paraboloid. The Equations (F-10) and (F-11) resulting from the method described here represent the locus of locations where contour lines of the eliptic paraboloid are parallel to the axes. The intersection of these loci, the solution of (F-11), is the lowest point in the eliptic paraboloid, the least mean squares fit to (F-1).
