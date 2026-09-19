---
paper: parnas-1972-modules
title: On the Criteria To Be Used in Decomposing Systems into Modules
authors:
  - D. L. Parnas
year: 1972
venue: Communications of the ACM
field: software
section_title: Conclusion
kind: section
lang: en
source: https://www.win.tue.nl/~wstomv/edu/2ip30/references/criteria_for_modularization.pdf
pdf_sha256: 7008fd6abc833ded750e52dbac4968e8eda339f66b462ca4427f1953f98df9c4
pdf_pages: "6"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: b28ad7a70884a758c2934881f87dc8f67be6f65574250a2ddad2c1f3ab1b516f
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

We have tried to demonstrate by these examples that it is almost always incorrect to begin the decomposition of a system into modules on the basis of a flowchart. We propose instead that one begins with a list of difficult design decisions or design decisions which are likely to change. Each module is then designed to hide such a decision from the others. Since, in most cases, design decisions transcend time of execution, modules will not correspond to steps in the processing. To achieve an efficient implementation we must abandon the assumption that a module is one or more subroutines, and instead allow subroutines and programs to be assembled collections of code from various modules.

Received August 1971; revised November 1971
