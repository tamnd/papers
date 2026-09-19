---
paper: milner-1978-polymorphism
title: A Theory of Type Polymorphism in Programming
authors:
  - Robin Milner
year: 1978
venue: Journal of Computer and System Sciences
field: languages
section_title: Front Matter
tag: "0048"
kind: front
lang: en
source: https://doi.org/10.1016/0022-0000(78)90014-4
pdf_sha256: a55f1fb81848085165c55a73c33f28b5d25f3b7bdcfa782c462af7997faad6bc
pdf_pages: 1-2
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 4b2981f5e24d5cd0557d452c5d6d147cc645f5fcb6995cc1b2bfedb5ef3a2b09
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Edinburgh Research Explorer

A theory of type polymorphism in programming

Citation for published version:
Milner, R 1978, 'A theory of type polymorphism in programming', Journal of Computer and System Sciences, vol. 17, no. 3, pp. 348-375. https://doi.org/10.1016/0022-0000(78)90014-4

Digital Object Identifier (DOI):
10.1016/0022-0000(78)90014-4

Link:
Link to publication record in Edinburgh Research Explorer

Document Version:
Publisher's PDF, also known as Version of record

Published In:
Journal of Computer and System Sciences

General rights
Copyright for the publications made accessible via the Edinburgh Research Explorer is retained by the author(s) and / or other copyright owners and it is a condition of accessing these publications that users recognise and abide by the legal requirements associated with these rights.

Take down policy
The University of Edinburgh has made every reasonable effort to ensure that Edinburgh Research Explorer content complies with UK legislation. If you believe that the public display of this file breaches copyright please contact openaccess@ed.ac.uk providing details, and we will remove access to the work immediately and investigate your claim.

A Theory of Type Polymorphism in Programming

ROBIN MILNER

Computer Science Department, University of Edinburgh, Edinburgh, Scotland

Received October 10, 1977; revised April 19, 1978

The aim of this work is largely a practical one. A widely employed style of programming, particularly in structure-processing languages which impose no discipline of types, entails defining procedures which work well on objects of a wide variety. We present a formal type discipline for such polymorphic procedures in the context of a simple programming language, and a compile time type-checking algorithm $\mathcal{W}$ which enforces the discipline. A Semantic Soundness Theorem (based on a formal semantics for the language) states that well-type programs cannot "go wrong" and a Syntactic Soundness Theorem states that if $\mathcal{W}$ accepts a program then it is well typed. We also discuss extending these results to richer languages; a type-checking algorithm based on $\mathcal{W}$ is in fact already implemented and working, for the metalanguage ML in the Edinburgh LCF system.
