---
paper: cerf-1974-tcpip
title: A Protocol for Packet Network Intercommunication
authors:
  - Vinton G. Cerf
  - Robert E. Kahn
year: 1974
venue: IEEE Transactions on Communications
field: networks
section_title: Address Formats
kind: section
lang: en
source: https://doi.org/10.21236/ada634240
pdf_sha256: f7c614a116516e0efec906885fa3ffd9261c5101900d117b72d26d92de96d2f1
pdf_pages: "5"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 2d2bdabf0220515b7258e3d02c2c6d33b6124a1b5375e90156484e7a7e1d7cb0
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The selection of address formats is a problem between networks because the local network addresses of TCP’s may vary substantially in format and size. A uniform internetwork TCP address space, understood by each GATEWAY and TCP, is essential to routing and delivery of internetwork packets.

Similar troubles are encountered when we deal with process addressing and, more generally, port addressing. We introduce the notion of ports in order to permit a process to distinguish between multiple message streams. The port is simply a designator of one such message stream associated with a process. The means for identifying a port are generally different in different operating systems, and therefore, to obtain uniform addressing, a standard port address format is also required. A port address designates a full duplex message stream.
