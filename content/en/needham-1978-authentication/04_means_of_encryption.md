---
paper: needham-1978-authentication
title: Using Encryption for Authentication in Large Networks of Computers
authors:
  - Roger M. Needham
  - Michael D. Schroeder
year: 1978
venue: Communications of the ACM
field: security
section: "3"
section_title: Means of Encryption
tag: "0328"
kind: section
lang: en
source: https://web.archive.org/web/20250531153030id_/https://dl.acm.org/doi/pdf/10.1145/359657.359659
pdf_sha256: 6fec623eab036ce7683fc0d35286988cb721593962c842b1360d981fff49d11e
pdf_pages: "2"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 1d497400c34206e5327f614fa7b6b98835fcdac60d57846e6741d6907e650ab8
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

One significant issue in this area of study is where the encryption and decryption are done. Branstad [2] suggests that these actions take place in the network interface of a computer. It is a requirement of some of our protocols that the encryption be done elsewhere, because it is necessary to prepare an encrypted message without actually sending it yet or to receive an encrypted message without knowing at the network interface what the key is. Accordingly we have assumed that any hardware encryption aid is located so one can say

$$
X := \text{encrypt}(Y, Key)
$$

and still have $X$ in hand, or say

```text
if (X := decrypt(Y, Key1)) = nonsense
then X := decrypt(Y, Key2)
```
