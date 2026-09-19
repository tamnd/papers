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
section: I
section_title: Introduction
tag: "0944"
kind: section
lang: en
source: https://doi.org/10.21236/ada606588
pdf_sha256: f7b1f78d9a7cbeb85e32b8c563a6db60771a5cc4bdc55580645f7cb778a4966b
pdf_pages: "2"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 50868d4320ed14687b040ee05c4fb1ecf9a99c31dc9345826074d1da0fbcc515
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The era of “electronic mail” [10] may soon be upon us; we must ensure that two important properties of the current “paper mail” system are preserved: (a) messages are *private*, and (b) messages can be *signed*. We demonstrate in this paper how to build these capabilities into an electronic mail system.

At the heart of our proposal is a new encryption method. This method provides an implementation of a “public-key cryptosystem,” an elegant concept invented by Diffie and Hellman [[diffie-1976-newdirections]]. Their article motivated our research, since they presented the concept but not any practical implementation of such a system. Readers familiar with [[diffie-1976-newdirections]] may wish to skip directly to Section V for a description of our method.
