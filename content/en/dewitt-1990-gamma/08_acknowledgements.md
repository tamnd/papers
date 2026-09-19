---
paper: dewitt-1990-gamma
title: The Gamma Database Machine Project
authors:
  - David J. DeWitt
  - Shahram Ghandeharizadeh
  - Donovan A. Schneider
  - Allan Bricker
  - Hui-I Hsiao
  - Rick Rasmussen
year: 1990
venue: IEEE Transactions on Knowledge and Data Engineering
field: databases
section: "8"
section_title: Acknowledgements
tag: "0281"
kind: section
lang: en
source: http://db.cs.berkeley.edu/cs286/papers/gamma-tkde1990.pdf
pdf_sha256: 420d33f44b8e050f33517cdff1299a58838b4ad826d80a6617200332ea02be5e
pdf_pages: "35"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 562f4ec6ac5a855085b582f6e20fc213b5ff376401747dd19b985a2d368fc9e9
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Like all large systems projects, a large number of people beyond those listed as authors made this paper possible. Bob Gerber deserves special recognition for his work on the design of Gamma plus his leadership on the implementation of the first prototype. The query optimizer was implemented by M. Muralikrishna. Rajiv Jauhari implemented the read-ahead mechanism to improve the performance of sequential scans. Anoop Sharma implemented both the aggregate algorithms and the embedded query interface. Goetz Graefe and Joanna Chen implemented a predicate compiler. They deserve special credit for being willing to debug the machine code produced by the compiler.

We would also like to thank Jim Gray and Susan Englert of Tandem Computers for the use of their Wisconsin benchmark relation generator. Without this generator the tests we conducted would simply not have been possible as previously we had no way of generating relations larger than 1 million tuples.
