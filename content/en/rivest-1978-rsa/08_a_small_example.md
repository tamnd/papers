---
paper: rivest-1978-rsa
title: A Method for Obtaining Digital Signatures and Public-Key Cryptosystems
authors:
  - R. L. Rivest
  - A. Shamir
  - L. Adleman
year: 1978
venue: Communications of the ACM
field: security
section: VIII
section_title: A Small Example
tag: 094B
kind: section
lang: en
source: https://doi.org/10.21236/ada606588
pdf_sha256: f7b1f78d9a7cbeb85e32b8c563a6db60771a5cc4bdc55580645f7cb778a4966b
pdf_pages: 10-11
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 20ce0131b6c824b425e7ac3ffbcd8cfff8f709f56c9e68ba6c020daecc79fb00
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Consider the case $p = 47, q = 59, n = p \cdot q = 47 \cdot 59 = 2773$, and $d = 157$. Then $\phi(2773) = 46 \cdot 58 = 2668$, and $e$ can be computed as follows:

$$
\begin{array}{lll}
x_0 = 2668, & a_0 = 1, & b_0 = 0, \\
x_1 = 157, & a_1 = 0, & b_1 = 1, \\
x_2 = 156, & a_2 = 1, & b_2 = -16 \ (\text{since } 2668 = 157 \cdot 16 + 156) , \\
x_3 = 1, & a_3 = -1, & b_3 = 17 \ (\text{since } 157 = 1 \cdot 156 + 1) .
\end{array}
$$

Therefore $e = 17$, the multiplicative inverse $\pmod{2668}$ of $d = 157$.

With $n = 2773$ we can encode two letters per block, substituting a two-digit number for each letter: blank = 00, A = 01, B = 02, ..., Z = 26. Thus the message

ITS ALL GREEK TO ME

(Julius Caesar, I, ii, 288, paraphrased) is encoded:

0920 1900 0112 1200 0718 0505 1100 2015 0013 0500

Since $e = 10001$ in binary, the first block ($M = 920$) is enciphered:

$$
M^{17} = (((((1)^2 \cdot M)^2)^2)^2)^2 \cdot M = 948 \pmod{2773} .
$$

The whole message is enciphered as:

0948 2342 1084 1444 2663 2390 0778 0774 0219 1655 .

The reader can check that deciphering works: $948^{157} \equiv 920 \pmod{2773}$, etc.
