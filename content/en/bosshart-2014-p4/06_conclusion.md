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
section: "6"
section_title: CONCLUSION
tag: 009D
kind: section
lang: en
source: arxiv:1312.1719
pdf_sha256: 2bb0ccb7b5410868efdecc9ef5208d235c6f3aa75dee84aa992751aed117a42f
pdf_pages: "7"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 80a6aa96195a65f9aa76e0574e7f3fe1cbb89f4966ef2b4c7287e9cec28edb9b
prompt_sha256: 329630a0b9175a55e4af1b8e281a3e67eeab250f8d643953b7dcde99743c7628
---

The promise of SDN is that a single control plane can directly control a whole network of switches. OpenFlow supports this goal by providing a single, vendor-agnostic API. However, today’s OpenFlow targets fixed-function switches that recognize a pre-determined set of header fields and that process packets using a small set of predefined actions. The control plane cannot express how packets should be processed to best meet the needs of control applications.

We propose a step towards more flexible switches whose functionality is specified—and may be changed—in the field. The programmer decides how the forwarding plane processes packets without worrying about implementation details. A compiler transforms an imperative program into a table dependency graph that can be mapped to many specific target switches, including optimized hardware implementations.

We emphasize that this is only a first step, designed as a straw-man proposal for OpenFlow 2.0 to contribute to the debate. In this proposal, several aspects of a switch remain undefined (e.g., congestion-control primitives, queuing disciplines, traffic monitoring). However, we believe the approach of having a configuration language—and compilers that generate low-level configurations for specific targets—will lead to future switches that provide greater flexibility, and unlock the potential of software defined networks.
