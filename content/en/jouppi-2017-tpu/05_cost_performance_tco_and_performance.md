---
paper: jouppi-2017-tpu
title: In-Datacenter Performance Analysis of a Tensor Processing Unit
authors:
  - Norman P. Jouppi
  - Cliff Young
  - Nishant Patil
  - David Patterson
  - Gaurav Agrawal
  - Raminder Bajwa
  - Sarah Bates
  - Suresh Bhatia
  - Nan Boden
  - Al Borchers
year: 2017
venue: ISCA
field: architecture
section: "5"
section_title: Cost-Performance, TCO, and Performance/Watt
tag: "0190"
kind: section
lang: en
source: arxiv:1704.04760
pdf_sha256: 19793e4ae1486630ac45a12facabc0e80609dd679db8ca7a3a040f8bf0d8e0be
pdf_pages: "10"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 483e14ed4b9e74bdce60f3c235ba492aed4b4b67c4b4e9ad846af3c16b121053
prompt_sha256: e1b070d511afab62a45db64b491e759e38eaa12f6c7943b773a942f4f2f70935
---

When buying computers by the thousands, cost-performance trumps performance. The best cost metric in a datacenter is total cost of ownership (TCO). The actual price we pay for thousands of chips depends on negotiations between the companies involved. For business reasons, we can’t publish such price information or data that might let them be deduced. However, power is correlated with TCO, and we can publish Watts per server, so we use performance/Watt as our proxy for performance/TCO in this paper. In this section, we compare whole servers rather than single dies, which Table 2 lists in the “Benchmarked Server” columns.

Figure 9 shows the geometric and weighted mean performance/Watt for the K80 GPU and TPU relative to the Haswell CPU. We present two different calculations of performance/Watt. The first (“total”) includes the power consumed by the host CPU server when calculating performance/Watt for the GPU and TPU. The second (“incremental”) subtracts the host CPU server power from the GPU and TPU beforehand.

For total-performance/Watt, the K80 server is 1.2 - 2.1X Haswell. For incremental-performance/Watt, when Haswell server power is omitted, the K80 server is 1.7- 2.9X.

The TPU server has 17 to 34 times better total-performance/Watt than Haswell, which makes the TPU server 14 to 16 times the performance/Watt of the K80 server. The relative incremental-performance/Watt—which was our company’s justification for a custom ASIC—is 41 to 83 for the TPU, which lifts the TPU to 25 to 29 times the performance/Watt of the GPU.
