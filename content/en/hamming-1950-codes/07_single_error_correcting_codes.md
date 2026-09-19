---
paper: hamming-1950-codes
title: Error Detecting and Error Correcting Codes
authors:
  - Richard W. Hamming
year: 1950
venue: Bell System Technical Journal
field: theory
section: "7"
section_title: Single Error Correcting Codes
tag: 03DF
kind: section
lang: en
source: https://archive.org/download/bstj29-2-147/bstj29-2-147.pdf
pdf_sha256: 32f13768d0e37bcc482517d3e1f50f9309d6db65e145edc476622c435829bdad
pdf_pages: 11-12
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: d07115842ef1d96e2183ea058351c06777534fec7106ece3dec617bb80e0f5bd
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

It has probably been noted by the reader that, in the particular codes of Part I, a distinction was made between information and check positions, while, in the geometric model, there is no real distinction between the various coordinates. To bring the two treatments more in line with each other we redefine a *systematic* code as a code whose symbol lengths are all equal and
1. The positions checked are independent of the information contained in the symbol.
2. The checks are independent of each other.
3. We use parity checks.
This is equivalent to the earlier definition. To show this we form a matrix whose $i$-th row has 1's in the positions of the $i$-th parity check and 0's elsewhere. By assumption 1 the matrix is fixed and does not change from code symbol to code symbol. From 2 the rank of the matrix is $k$. This in turn means that the system can be solved for $k$ of the positions expressed in terms of the other $n - k$ positions. Assumption 3 indicates that in this solving we use the arithmetic in which $1 + 1 = 0$.

There exist non-systematic codes, but so far none have been found which for a given $n$ and minimum distance $d$ have more code symbols than a systematic code. Section 9 gives an example of a non-systematic code.

Turning to the main problem of this section we find from Table V that a single error correcting code has code points at least three units from each other. Thus each point may be surrounded by a sphere of radius 1 with no two spheres having a point in common. Each sphere has a center point and

$n$ points on its surface, a total of $n + 1$ points. Thus the space of $2^n$ points can have at most:

$$
\frac{2^n}{n + 1}
$$

spheres. This is exactly the bound we found before in section 3.

While we have shown that the special single error correcting code constructed in section 3 is of minimum redundancy, we cannot show that all optimal codes are equivalent, since the following trivial example shows that this is not so. For $n = 4$ we find from Table I that $m = 1$ and $k = 3$. Thus there are at most two code symbols in a four-position code. The following two optimal codes are clearly not equivalent:

$$
\begin{array}{cccc}
0 & 0 & 0 & 0 \\
1 & 1 & 1 & 1
\end{array}
$$

and

$$
\begin{array}{cccc}
0 & 0 & 0 & 0 \\
0 & 1 & 1 & 1
\end{array}.
$$
