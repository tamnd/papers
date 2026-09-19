---
paper: patterson-1981-risc
title: 'RISC I: A Reduced Instruction Set VLSI Computer'
authors:
  - David A. Patterson
  - Carlo H. Sequin
year: 1981
venue: ISCA
field: architecture
section_title: Summary
kind: section
lang: en
source: https://people.eecs.berkeley.edu/~kubitron/courses/cs252-F00/handouts/papers/p216-patterson.pdf
pdf_sha256: d49afdf3db5a8374fbc757059fab0562b9a517b3ff7abec17c2e6b88c48f03e1
pdf_pages: "7"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: c04ffb67f675a2dcd1710a52656bfd886e084a595621054830567ed66c800a1c
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

From our limited experience based on the results of a few small programs, it appears that the reduced instruction set computer is a promising style of computer design. We have convinced ourselves that complicated addressing schemes are not a vital part of high-throughput machines. The register window scheme appears to make significant contributions toward the performance of our architecture and should be seriously considered in other machines.

We have taken out most of the complexity of modern computers without sacrificing much in code density while improving performance. The loss of complexity has not reduced the functionality of RISC; the chosen subset, especially when combined with the register window scheme, emulates more complex machines. It also appears we can build a single-chip computer much sooner than the traditional architectures. We are encouraged by these results and have begun the design of a single-chip RISC I as part of a multiterm class project.
