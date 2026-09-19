---
paper: bosshart-2014-p4
title: 'P4: Programming Protocol-Independent Packet Processors'
authors:
  - Pat Bosshart
  - Dan Daly
  - Glen Gibb
  - Martin Izzard
  - Nick McKeown
  - Jennifer Rexford
  - Cole Schlesinger
  - Dan Talayco
  - Amin Vahdat
  - George Varghese
  - David Walker
year: 2014
venue: ACM SIGCOMM Computer Communication Review
field: networks
section_title: Front Matter
tag: 008C
kind: front
lang: en
source: arxiv:1312.1719
pdf_sha256: 2bb0ccb7b5410868efdecc9ef5208d235c6f3aa75dee84aa992751aed117a42f
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: da1eae2f3ec530d41618e1756af33a46e44daeb9a5f6969424ba7f2b5d124f69
prompt_sha256: 329630a0b9175a55e4af1b8e281a3e67eeab250f8d643953b7dcde99743c7628
---

P4: Programming Protocol-Independent Packet Processors

Pat Bosshart†, Dan Daly*, Glen Gibb†, Martin Izzard†, Nick McKeown‡, Jennifer Rexford**, Cole Schlesinger**, Dan Talayco†, Amin Vahdat†, George Varghese§, David Walker**
†Barefoot Networks   *Intel   ‡Stanford University   **Princeton University   †Google   §Microsoft Research

ABSTRACT

P4 is a high-level language for programming protocol-independent packet processors. P4 works in conjunction with SDN control protocols like OpenFlow. In its current form, OpenFlow explicitly specifies protocol headers on which it operates. This set has grown from 12 to 41 fields in a few years, increasing the complexity of the specification while still not providing the flexibility to add new headers. In this paper we propose P4 as a strawman proposal for how OpenFlow should evolve in the future. We have three goals: (1) Reconfigurability in the field: Programmers should be able to change the way switches process packets once they are deployed. (2) Protocol independence: Switches should not be tied to any specific network protocols. (3) Target independence: Programmers should be able to describe packet-processing functionality independently of the specifics of the underlying hardware. As an example, we describe how to use P4 to configure a switch to add a new hierarchical label.
