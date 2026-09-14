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
section: "3"
section_title: CPU, GPU, and TPU Platforms
tag: "0185"
kind: section
lang: en
source: arxiv:1704.04760
pdf_sha256: 19793e4ae1486630ac45a12facabc0e80609dd679db8ca7a3a040f8bf0d8e0be
pdf_pages: "5"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 365bb90900e96ac87825735a028e240acc6543e598af4456151dd8dbc669b6cd
prompt_sha256: e1b070d511afab62a45db64b491e759e38eaa12f6c7943b773a942f4f2f70935
---

The six production applications in Table 1 are our workload for this paper. As mentioned above, these six are representative of 95% of TPU use in our datacenters. Ironically, deploying and measuring popular small DNNs like AlexNet or VGG is difficult on production machines. However, one of our CNNs derives from Inception V2, which is widely used.

The benchmark platforms are server-class computers that were available in 2015 when the TPUs were deployed. This restriction meant that they must include at least SECDED protection of internal SRAM as well as external DRAM memory like the TPU, which excludes some choices such as the Nvidia Maxwell GPU. For our company to purchase and deploy them, they also had to be sensibly configured machines, and not awkward artifacts assembled solely to win benchmarks.

Table 2 lists our choices. The traditional CPU server is represented by an 18-core, dual-socket Haswell processor from Intel. This platform is also the host server for GPUs or TPUs. Haswell was fabbed in an Intel 22nm process. Both the CPU and GPU are very large dies: about 600 mm²!

The 2.3 GHz CPU clock rate doesn’t include Turbo mode because it seldom occurs in our datacenters for NN apps. Haswell has different clock rates depending on whether programs use AVX instructions, which our NN apps often use. The higher clock rate of Turbo mode (for programs that avoid AVX) occurs when they don’t use all their cores. Thus, another reason Turbo mode is rare in our datacenters is that our apps typically do use all the cores, plus they can run other datacenter jobs to fill any idle cores.

The GPU accelerator is the Nvidia K80. Each K80 card contains two dies and offers SECDED on internal memory and DRAM. Nvidia states that the “K80 Accelerator dramatically lowers datacenter cost by delivering application performance with fewer, more powerful servers”[Nvi16]. NN researchers frequently used K80s in 2015, and they were chosen for new cloud-based GPU offerings as recently as September 2016 [Bar16].

Up to eight K80 dies can be installed in four cards on this server, which is the configuration we benchmark. It offers a Boost mode to increase clock rate as high as 875 MHz. Turbo mode in Haswell is controlled by hardware and so can operate in short bursts before the chip temperature rises significantly. However, Boost mode is under the control of a software driver [Nvi15], and thus lasts at least hundreds of milliseconds. Hence, power and cooling would have to be provisioned for the K80 as if it were essentially always running in Boost mode, for otherwise the chips could get too hot. For this platform, enabling Boost mode would force us to reduce the number of K80 cards, which would hurt total cost of ownership. Thus, Boost mode is disabled. This restriction reduces peak bandwidth and TOPS (see Table 2 caption); Sec. 8 examines if it were enabled.

As the number of dies per benchmarked server varies between 2 to 8, we usually show results below normalized per die (Figures 5-8, Figures 10-11, and Tables 3, 4, and 6), but we occasionally show whole systems (Figure 9). We hope this distinction is clear.
