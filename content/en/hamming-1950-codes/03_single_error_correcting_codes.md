---
paper: hamming-1950-codes
title: Error Detecting and Error Correcting Codes
authors:
  - Richard W. Hamming
year: 1950
venue: Bell System Technical Journal
field: theory
section: "3"
section_title: Single Error Correcting Codes
tag: 03DB
kind: section
lang: en
source: https://archive.org/download/bstj29-2-147/bstj29-2-147.pdf
pdf_sha256: 32f13768d0e37bcc482517d3e1f50f9309d6db65e145edc476622c435829bdad
pdf_pages: 4-7
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: e7b541a4777b94fab8a5696c6520c48ae753159e25ef817699190aa6e1d9fabb
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

To construct a single error correcting code we first assign $m$ of the $n$ available positions as information positions. We shall regard the $m$ as fixed, but the specific positions are left to a later determination. We next assign the $k$ remaining positions as check positions. The values in these $k$ positions are to be determined in the encoding process by even parity checks over selected information positions.

Let us imagine for the moment that we have received a code symbol, with or without an error. Let us apply the $k$ parity checks, in order, and for each time the parity check assigns the value observed in its check position we write a 0, while for each time the assigned and observed values disagree we write a 1. When written from right to left in a line this sequence of $k$ 0's and 1's (to be distinguished from the values assigned by the parity checks) may be regarded as a binary number and will be called the *checking number*. We shall require that this checking number give the position of any single error, with the zero value meaning no error in the symbol. Thus the check number must describe $m + k + 1$ different things, so that

$$
2^k \geq m + k + 1
$$

is a condition on $k$. Writing $n = m + k$ we find

$$
2^m \leq \frac{2^n}{n + 1}.
$$

Using this inequality we may calculate Table I, which gives the maximum $m$ for a given $n$, or, what is the same thing, the minimum $n$ for a given $m$.

We now determine the positions over which each of the various parity checks is to be applied. The checking number is obtained digit by digit, from right to left, by applying the parity checks in order and writing down the corresponding 0 or 1 as the case may be. Since the checking number is

| n | m | Corresponding k |
| --- | --- | --- |
| 1 | 0 | 1 |
| 2 | 0 | 2 |
| 3 | 1 | 2 |
| 4 | 1 | 3 |
| 5 | 2 | 3 |
| 6 | 3 | 3 |
| 7 | 4 | 3 |
| 8 | 4 | 4 |
| 9 | 5 | 4 |
| 10 | 6 | 4 |
| 11 | 7 | 4 |
| 12 | 8 | 4 |
| 13 | 9 | 4 |
| 14 | 10 | 4 |
| 15 | 11 | 4 |
| 16 | 11 | 5 |
| Etc. |  |  |

to give the position of any error in a code symbol, any position which has a 1 on the right of its binary representation must cause the first check to fail. Examining the binary form of the various integers we find

$$
\begin{align*}
1 &= 1 \\
3 &= 11 \\
5 &= 101 \\
7 &= 111 \\
9 &= 1001 \\
&\text{Etc.}
\end{align*}
$$

have a 1 on the extreme right. Thus the first parity check must use positions

$$
1, 3, 5, 7, 9, \ldots .
$$

In an exactly similar fashion we find that the second parity check must use those positions which have 1's for the second digit from the right of their binary representation,

$$
\begin{align*}
2 &= 10 \\
3 &= 11 \\
6 &= 110 \\
7 &= 111 \\
10 &= 1010 \\
11 &= 1011 \\
&\text{Etc.,}
\end{align*}
$$

the third parity check

$$
\begin{align*}
4 &= 100 \\
5 &= 101 \\
6 &= 110 \\
7 &= 111 \\
12 &= 1100 \\
13 &= 1101 \\
14 &= 1110 \\
15 &= 1111 \\
20 &= 10100 \\
\end{align*}
$$

Etc.

It remains to decide for each parity check which positions are to contain information and which the check. The choice of the positions $1, 2, 4, 8, \ldots$ for check positions, as given in the following table, has the advantage of making the setting of the check positions independent of each other. All other positions are information positions. Thus we obtain Table II.

| Check Number | Check Positions | Positions Checked |
| --- | --- | --- |
| 1 | 1 | 1, 3, 5, 7, 9, 11, 13, 15, 17, \ldots |
| 2 | 2 | 2, 3, 6, 7, 10, 11, 14, 15, 18, \ldots |
| 3 | 4 | 4, 5, 6, 7, 12, 13, 14, 15, 20, \ldots |
| 4 | 8 | 8, 9, 10, 11, 12, 13, 14, 15, 24, \ldots |
| . | . | . |
| . | . | . |
| . | . | . |

As an illustration of the above theory we apply it to the case of a seven-position code. From Table I we find for $n = 7, m = 4$ and $k = 3$. From Table II we find that the first parity check involves positions 1, 3, 5, 7 and is used to determine the value in the first position; the second parity check, positions 2, 3, 6, 7, and determines the value in the second position; and the third parity check, positions 4, 5, 6, 7, and determines the value in position four. This leaves positions 3, 5, 6, 7 as information positions. The results of writing down all possible binary numbers using positions 3, 5, 6, 7, and then calculating the values in the check positions 1, 2, 4, are shown in Table III.

Thus a seven-position single error correcting code admits of 16 code symbols. There are, of course, $2^7 - 16 = 112$ meaningless symbols. In some applications it may be desirable to drop the first symbol from the code to avoid the all zero combination as either a code symbol or a code symbol plus a single error, since this might be confused with no message. This would still leave 15 useful code symbols.

| Position |  |  |  |  |  |  | Decimal Value of Symbol |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 3 | 4 | 5 | 6 | 7 |  |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 1 | 0 | 1 | 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 1 | 0 | 1 | 0 | 2 |
| 1 | 0 | 0 | 0 | 0 | 1 | 1 | 3 |
| 1 | 0 | 0 | 1 | 1 | 0 | 0 | 4 |
| 0 | 1 | 0 | 0 | 1 | 0 | 1 | 5 |
| 1 | 1 | 0 | 0 | 1 | 1 | 0 | 6 |
| 0 | 0 | 0 | 1 | 1 | 1 | 1 | 7 |
| 1 | 1 | 1 | 0 | 0 | 0 | 0 | 8 |
| 0 | 0 | 1 | 1 | 0 | 0 | 1 | 9 |
| 1 | 0 | 1 | 1 | 0 | 1 | 0 | 10 |
| 0 | 1 | 1 | 0 | 1 | 1 | 1 | 11 |
| 0 | 1 | 1 | 1 | 1 | 0 | 0 | 12 |
| 1 | 0 | 1 | 0 | 1 | 0 | 1 | 13 |
| 0 | 0 | 1 | 0 | 1 | 1 | 0 | 14 |
| 1 | 1 | 1 | 1 | 1 | 1 | 1 | 15 |

As an illustration of how this code "works" let us take the symbol 0 1 1 1 1 0 0 corresponding to the decimal value 12 and change the 1 in the fifth position to a 0. We now examine the new symbol

$$
0\ 1\ 1\ 1\ 0\ 0\ 0
$$

by the methods of this section to see how the error is located. From Table II the first parity check is over positions 1, 3, 5, 7 and predicts a 1 for the first position while we find a 0 there; hence we write a

$$
1\ .
$$

The second parity check is over positions 2, 3, 6, 7, and predicts the second position correctly; hence we write a 0 to the left of the 1, obtaining

$$
0\ 1\ .
$$

The third parity check is over positions 4, 5, 6, 7 and predicts wrongly; hence we write a 1 to the left of the 0 1, obtaining

$$
1\ 0\ 1\ .
$$

This sequence of 0's and 1's regarded as a binary number is the number 5; hence the error is in the fifth position. The correct symbol is therefore obtained by changing the 0 in the fifth position to a 1.
