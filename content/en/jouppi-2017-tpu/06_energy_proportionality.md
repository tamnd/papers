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
section: "6"
section_title: Energy Proportionality
tag: "0191"
kind: section
lang: en
source: arxiv:1704.04760
pdf_sha256: 19793e4ae1486630ac45a12facabc0e80609dd679db8ca7a3a040f8bf0d8e0be
pdf_pages: "10"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 4048a39c09f779fe18ea5fd961414a6a4dddf28976444afbbf7dc9eb47aa9b1f
prompt_sha256: e1b070d511afab62a45db64b491e759e38eaa12f6c7943b773a942f4f2f70935
---

Thermal Design Power (TDP) affects the cost of provisioning power, as you must supply sufficient power and cooling when hardware is at full power. However, the cost of electricity is based on the average consumed as the workload varies during the day. [Bar07] found that servers are 100% busy less than 10% of the time and advocated energy proportionality: servers should consume power proportional to the amount of work performed. The estimate of power consumed in the prior section is based on the fraction of the TDP that has been seen in our datacenters.

We measured performance and power as the offered workload utilization varies from 0% to 100%, collected in buckets of 10% delta of workload [Lan09]. Figure 10 shows server power divided by the number of dies per server for the three chips by varying CNN0’s workload. We plot incremental (K80 and TPU) as well as total power (K80+Haswell/4 and TPU+Haswell/2) for the GPU and TPU. Note that all were given the same batch sizes.

We see that the TPU has the lowest power—118W per die total (TPU+Haswell/2) and 40W per die incremental (TPU in Fig. 10)—but it has poor energy proportionality: at 10% load, the TPU uses 88% of the power it uses at 100%. (The short design schedule prevented inclusion of many energy-saving features.) Not surprisingly, Haswell is the best at energy proportionality of the group: it uses 56% of the power at 10% load as it does at 100%. The K80 is closer to the CPU than the TPU, using 66% of the full load power at 10% workload. LSTM1, which is not computation bound, performs similarly: at 10% load the CPU uses 47% of full power, the GPU uses 78%, and the TPU uses 94%.

What happens to the server power usage when running CNN0 if it becomes a host to accelerators? When the GPU and TPU are at 100% load, the CPU server uses 52% of full power for the GPU and 69% for the TPU. (The CPU does more work for the TPU because it is running so much faster than the GPU.) Consequently, the Haswell server plus four TPUs use <20% additional power but run CNN0 80 times faster than the Haswell server alone (4 TPUs vs 2 CPUs).
