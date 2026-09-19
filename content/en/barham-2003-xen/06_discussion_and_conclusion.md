---
paper: barham-2003-xen
title: Xen and the Art of Virtualization
authors:
  - Paul Barham
  - Boris Dragovic
  - Keir Fraser
  - Steven Hand
  - Tim Harris
  - Alex Ho
  - Rolf Neugebauer
  - Ian Pratt
  - Andrew Warfield
year: 2003
venue: SOSP
field: systems
section: "6"
section_title: DISCUSSION AND CONCLUSION
tag: 065D
kind: section
lang: en
source: https://doi.org/10.1145/945445.945462
pdf_sha256: 7763a4c6cca63c17c92107b4d296fe2b7600ae8f419eef9ff36ac6c58a7a2a4d
pdf_pages: "13"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 973e3e9f99891fe82b2830b6cc17c37d8d9f807224caf28685ef5bcb2aaa697f
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

We have presented the Xen hypervisor which partitions the resources of a computer between domains running guest operating systems. Our paravirtualizing design places a particular emphasis on performance and resource management. We have also described and evaluated XenoLinux, a fully-featured port of a Linux 2.4 kernel that runs over Xen.

### 6.1 Future Work {#barham-2003-xen-s6-1 .section tag=065E}

We believe that Xen and XenoLinux are sufficiently complete to be useful to a wider audience, and so intend to make a public release of our software in the very near future. A beta version is already under evaluation by selected parties; once this phase is complete, a general 1.0 release will be announced on our project page3.

After the initial release we plan a number of extensions and improvements to Xen. To increase the efficiency of virtual block devices, we intend to implement a shared universal buffer cache indexed on block contents. This will add controlled data sharing to our design without sacrificing isolation. Adding copy-on-write semantics to virtual block devices will allow them to be safely shared among domains, while still allowing divergent file systems.

To provide better physical memory performance, we plan to implement a last-chance page cache (LPC) — effectively a system-wide list of free pages, of non-zero length only when machine memory is undersubscribed. The LPC is used when the guest OS virtual memory system chooses to evict a clean page; rather than discarding this completely, it may be added to the tail of the free list. A fault occurring for that page before it has been reallocated by Xen can therefore satisfied without a disk access.

An important role for Xen is as the basis of the XenoServer project which looks beyond individual machines and is building the control systems necessary to support an Internet-scale computing infrastructure. Key to our design is the idea that resource usage be accounted precisely and paid for by the sponsor of that job — if payments are made in real cash, we can use a congestion pricing strategy [28] to handle excess demand, and use excess revenues to pay for additional machines. This necessitates accurate and timely I/O scheduling with greater resilience to hostile workloads. We also plan to incorporate accounting into our block storage architecture by creating leases for virtual block devices.

In order to provide better support for the management and administration of XenoServers, we are incorporating more thorough support for auditing and forensic logging. We are also developing additional VFR rules which we hope will allow us to detect and prevent a wide range of antisocial network behaviour. Finally, we are continuing our work on XenoXP, focusing in the first instance on writing network and block device drivers, with the aim of fully supporting enterprise servers such as IIS.

### 6.2 Conclusion {#barham-2003-xen-s6-2 .section tag=065F}

Xen provides an excellent platform for deploying a wide variety of network-centric services, such as local mirroring of dynamic web content, media stream transcoding and distribution, multiplayer game and virtual reality servers, and ‘smart proxies’ [2] to provide a less ephemeral network presence for transiently-connected devices.

Xen directly addresses the single largest barrier to the deployment of such services: the present inability to host transient servers for short periods of time and with low instantiation costs. By allowing 100 operating systems to run on a single server, we reduce the associated costs by two orders of magnitude. Furthermore, by turning the setup and configuration of each OS into a software concern, we facilitate much smaller-granularity timescales of hosting.

As our experimental results show in Section 4, the performance of XenoLinux over Xen is practically equivalent to the performance of the baseline Linux system. This fact, which comes from the careful design of the interface between the two components, means that there is no appreciable cost in having the resource management facilities available. Our ongoing work to port the BSD and Windows XP kernels to operate over Xen is confirming the generality of the interface that Xen exposes.
