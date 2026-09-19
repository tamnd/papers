---
paper: verma-2015-borg
title: Large-scale cluster management at Google with Borg
authors:
  - Abhishek Verma
  - Luis Pedrosa
  - Madhukar Korupolu
  - David Oppenheimer
  - Eric Tune
  - John Wilkes
year: 2015
venue: EuroSys
field: systems
section: "1"
section_title: Introduction
tag: "0453"
kind: section
lang: en
source: https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/43438.pdf
pdf_sha256: 2fdacd3b69f8af91477412fc91d1d858a43e764929a4edb646bd517ededdad94
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 5c6a26306f291eac2765257ee88cc7538367f38fea2e788af86e2e22d3fe4308
edited: true
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The cluster management system we internally call Borg admits, schedules, starts, restarts, and monitors the full range of applications that Google runs. This paper explains how.

Borg provides three main benefits: it (1) hides the details of resource management and failure handling so its users can focus on application development instead; (2) operates with very high reliability and availability, and supports applications that do the same; and (3) lets us run workloads across tens of thousands of machines effectively. Borg is not the first system to address these issues, but it’s one of the few operating at this scale, with this degree of resiliency and completeness. This paper is organized around these topics, concluding with a set of qualitative observations we have made from operating Borg in production for more than a decade.

† Work done while author was at Google.
‡ Currently at University of Southern California.

Permission to make digital or hard copies of part or all of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for third-party components of this work must be honored. For all other uses, contact the owner/author(s).
EuroSys’15, April 21–24, 2015, Bordeaux, France.
Copyright is held by the owner/author(s).
ACM 978-1-4503-3238-5/15/04.
http://dx.doi.org/10.1145/2741948.2741964

Figure.

Figure 1: The high-level architecture of Borg. Only a tiny fraction of the thousands of worker nodes are shown. {#verma-2015-borg-fig-1 .figure tag=0454}
