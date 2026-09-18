---
paper: hamming-1950-codes
title: Error Detecting and Error Correcting Codes
authors:
  - Richard W. Hamming
year: 1950
venue: Bell System Technical Journal
field: theory
section: "9"
section_title: Miscellaneous Observations
tag: "03E1"
kind: section
lang: en
source: https://archive.org/download/bstj29-2-147/bstj29-2-147.pdf
pdf_sha256: 32f13768d0e37bcc482517d3e1f50f9309d6db65e145edc476622c435829bdad
pdf_pages: 13-14
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 12e0e9bb1c0ac1d822503ab7c4fb8162ae3f44b59c03028f2cef2b8aa0495084
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

For the next case, minimum distance of five units, one can surround each code point by a sphere of radius 2. Each sphere will contain

$$
1 + C(n, 1) + C(n, 2)
$$

points, where $C(n, k)$ is the binomial coefficient, so that an upper bound on the number of code points in a systematic code is

$$
\frac{2^n}{1 + C(n, 1) + C(n, 2)} = \frac{2^{n+1}}{n^2 + n + 2} \geq 2^m.
$$

This bound is too high. For example, in the case of $n = 7$, we find that $m = 2$ so that there should be a code with four code points. The maximum possible, as can be easily found by trial and error, is two.

In a similar fashion a bound on the number of code points may be found whenever the minimum distance between code points is an odd number. A bound on the even cases can then be found by use of the general theorem of the preceding section. These bounds are, in general, too high, as the above example shows.

If we write the bound on the number of code points in a unit cube of dimension $n$ and with minimum distance $d$ between them as $B(n, d)$, then the information of this type in the present paper may be summarized as follows:

$$
B(n, 1) = 2^n \\
B(n, 2) = 2^{n-1} \\
B(n, 3) = 2^m \leq \frac{2^n}{n + 1} \\
B(n, 4) = 2^m \leq \frac{2^{n-1}}{n} \\
B(n - 1, 2k - 1) = B(n, 2k) \\
B(n, 2k - 1) = 2^m \leq \frac{2^n}{1 + C(n, 1) + \cdots + C(n, k - 1)}.
$$

While these bounds have been attained for certain cases, no general methods have yet been found for contructing optimal codes when the minimum distance between code points exceeds four units, nor is it known whether the bound is or is not attainable by systematic codes.

We have dealt mainly with systematic codes. The existence of non-systematic codes is proved by the following example of a single error correcting code with $n = 6$.

$$
\begin{array}{cccccc}
0 & 0 & 0 & 0 & 0 & 0 \\
0 & 1 & 0 & 1 & 0 & 1 \\
1 & 0 & 0 & 1 & 1 & 0 \\
1 & 1 & 1 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 1 & 1 \\
1 & 1 & 1 & 1 & 1 & 1 .
\end{array}
$$

The all 0 symbol indicates that any parity check must be an even one. The all 1 symbol indicates that each parity check must involve an even number of positions. A direct comparison indicates that since no two columns are the same the even parity checks must involve four or six positions. An examination of the second symbol, which has three 1's in it, indicates that no six-position parity check can exist. Trying now the four-position parity checks we find that

$$
\begin{array}{cccccc}
1 & 2 & & & 5 & 6 \\
2 & 3 & 4 & 5 &
\end{array}
$$

are two independent parity checks and that no third one is independent of these two. Two parity checks can at most locate four positions, and, since there are six positions in the code, these two parity checks are not enough to locate any single error. The code is, however, single error correcting since it satisfies the minimum distance condition of three units.

The only previous work in the field of error correction that has appeared in print, so far as the author is aware, is that of M. J. E. Golay.$^4$

$^4$ M. J. E. Golay, Correspondence, Notes on Digital Coding, Proceedings of the I.R.E., Vol. 37, p. 657, June 1949.
