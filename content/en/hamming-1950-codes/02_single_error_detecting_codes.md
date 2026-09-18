---
paper: hamming-1950-codes
title: Error Detecting and Error Correcting Codes
authors:
  - Richard W. Hamming
year: 1950
venue: Bell System Technical Journal
field: theory
section: "2"
section_title: SINGLE ERROR DETECTING CODES
tag: 03DA
kind: section
lang: en
source: https://archive.org/download/bstj29-2-147/bstj29-2-147.pdf
pdf_sha256: 32f13768d0e37bcc482517d3e1f50f9309d6db65e145edc476622c435829bdad
pdf_pages: 3-4
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 3e0333ef07dbbf7878838c2d6ed35a0dc1e8c3a75fcbe560f6124191752fa4a4
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

We may construct a single error detecting code having $n$ binary digits in the following manner: In the first $n - 1$ positions we put $n - 1$ digits of information. In the $n$-th position we place either 0 or 1, so that the entire $n$ positions have an even number of 1's. This is clearly a single error detecting code since any single error in transmission would leave an odd number of 1's in a code symbol.

The redundancy of these codes is, since $m = n - 1$,

$$
R = \frac{n}{n - 1} = 1 + \frac{1}{n - 1}.
$$

It might appear that to gain a low redundancy we should let $n$ become very large. However, by increasing $n$, the probability of at least one error in a symbol increases; and the risk of a double error, which would pass undetected, also increases. For example, if $p \ll 1$ is the probability of any error, then for $n$ so large as $1/p$, the probability of a correct symbol is approximately $1/e = 0.3679 \ldots$, while a double error has probability $1/2e = 0.1839 \ldots$.

The type of check used above to determine whether or not the symbol has any single error will be used throughout the paper and will be called a *parity check*. The above was an *even* parity check; had we used an odd number of 1's to determine the setting of the check position it would have been an odd parity check. Furthermore, a parity check need not always involve all the positions of the symbol but may be a check over selected positions only.
