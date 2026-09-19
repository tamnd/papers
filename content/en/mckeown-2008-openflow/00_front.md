---
paper: mckeown-2008-openflow
title: 'OpenFlow: Enabling Innovation in Campus Networks'
authors:
  - Nick McKeown
  - Tom Anderson
  - Hari Balakrishnan
  - Guru Parulkar
  - Larry Peterson
  - Jennifer Rexford
  - Scott Shenker
  - Jonathan Turner
year: 2008
venue: ACM SIGCOMM Computer Communication Review
field: networks
section_title: Front Matter
tag: "0175"
kind: front
lang: en
source: http://ccr.sigcomm.org/online/files/p69-v38n2n-mckeown.pdf
pdf_sha256: f71746e44666eec5baf625764a347cb142fb21e60dd4b647eefe73ac262aeb60
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 7289946192e5ae324eb93c232ba2a32c8824c86e7621c3a96129899794713387
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

OpenFlow: Enabling Innovation in Campus Networks

Nick McKeown
Stanford University

Guru Parulkar
Stanford University

Tom Anderson
University of Washington

Larry Peterson
Princeton University

Hari Balakrishnan
MIT

Jennifer Rexford
Princeton University

Scott Shenker
University of California, Berkeley

Jonathan Turner
Washington University in St. Louis

This article is an editorial note submitted to CCR. It has NOT been peer reviewed.
Authors take full responsibility for this article’s technical content.
Comments can be posted through CCR Online.

ABSTRACT

This whitepaper proposes OpenFlow: a way for researchers to run experimental protocols in the networks they use every day. OpenFlow is based on an Ethernet switch, with an internal flow-table, and a standardized interface to add and remove flow entries. Our goal is to encourage networking vendors to add OpenFlow to their switch products for deployment in college campus backbones and wiring closets. We believe that OpenFlow is a pragmatic compromise: on one hand, it allows researchers to run experiments on heterogeneous switches in a uniform way at line-rate and with high port-density; while on the other hand, vendors do not need to expose the internal workings of their switches. In addition to allowing researchers to evaluate their ideas in real-world traffic settings, OpenFlow could serve as a useful campus component in proposed large-scale testbeds like GENI. Two buildings at Stanford University will soon run OpenFlow networks, using commercial Ethernet switches and routers. We will work to encourage deployment at other schools; and We encourage you to consider deploying OpenFlow in your university network too.

Categories and Subject Descriptors
C.2 [Internetworking]: Routers

General Terms
Experimentation, Design

Keywords
Ethernet switch, virtualization, flow-based
