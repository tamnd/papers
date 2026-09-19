---
paper: backus-1978-vonneumann
title: Can Programming Be Liberated from the von Neumann Style? A Functional Style and Its Algebra of Programs
authors:
  - John Backus
year: 1978
venue: Communications of the ACM (Turing Award lecture)
field: languages
section: "8"
section_title: APL versus Word-at-a-Time Programming
tag: "0566"
kind: section
lang: en
source: https://www.cs.cmu.edu/~crary/819-f09/Backus78.pdf
pdf_sha256: 2e412a7986c7fd1bdd060d90d035faa9ecc8a29675f99206c243da90954ca423
pdf_pages: "6"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 690b563c3abb5381eeb52d8bdaf115c42ac2942dc7297e370d82ffa8dc46dae7
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Since I have said so much about word-at-a-time programming, I must now say something about APL [12]. We owe a great debt to Kenneth Iverson for showing us that there are programs that are neither word-at-a-time nor dependent on lambda expressions, and for introducing us to the use of new functional forms. And since APL assignment statements can store arrays, the effect of its functional forms is extended beyond a single assignment.

Unfortunately, however, APL still splits programming into a world of expressions and a world of statements. Thus the effort to write one-line programs is partly motivated by the desire to stay in the more orderly world of expressions. APL has exactly three functional forms, called inner product, outer product, and reduction. These are sometimes difficult to use, there are not enough of them, and their use is confined to the world of expressions.

Finally, APL semantics is still too closely coupled to states. Consequently, despite the greater simplicity and power of the language, its framework has the complexity and rigidity characteristic of von Neumann languages.
