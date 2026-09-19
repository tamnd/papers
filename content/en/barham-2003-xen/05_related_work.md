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
section: "5"
section_title: RELATED WORK
tag: 065C
kind: section
lang: en
source: https://doi.org/10.1145/945445.945462
pdf_sha256: 7763a4c6cca63c17c92107b4d296fe2b7600ae8f419eef9ff36ac6c58a7a2a4d
pdf_pages: 12-13
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 579e8de82ae8ce2850a3eb5bb19fa05e0601e1d52623ef2864e57b7ad871328f
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Virtualization has been applied to operating systems both commercially and in research for nearly thirty years. IBM VM/370 [19, 38] first made use of virtualization to allow binary support for legacy code. VMware [10] and Connectix [8] both virtualize commodity PC hardware, allowing multiple operating systems to run on a single host. All of these examples implement a full virtualization of (at least a subset of) the underlying hardware, rather than paravirtualizing and presenting a modified interface to the guest OS. As shown in our evaluation, the decision to present a full virtualization, although able to more easily support off-the-shelf operating systems, has detrimental consequences for performance.

The virtual machine monitor approach has also been used by Disco to allow commodity operating systems to run efficiently on ccNUMA machines [7, 18]. A small number of changes had to be made to the hosted operating systems to enable virtualized execution on the MIPS architecture. In addition, certain other changes were made for performance reasons.

At present, we are aware of two other systems which take the paravirtualization approach: IBM presently supports a paravirtualized version of Linux for their zSeries mainframes, allowing large numbers of Linux instances to run simultaneously. Denali [44], discussed previously, is a contemporary isolation kernel which attempts to provide a system capable of hosting vast numbers of virtualized OS instances.

In addition to Denali, we are aware of two other efforts to use low-level virtualization to build an infrastructure for distributed systems. The vMatrix [1] project is based on VMware and aims to build a platform for moving code between different machines. As vMatrix is developed above VMware, they are more concerned with higher-level issues of distribution that those of virtualization itself. In addition, IBM provides a “Managed Hosting” service, in which virtual Linux instances may be rented on IBM mainframes.

The PlanetLab [33] project has constructed a distributed infrastructure which is intended to serve as a testbed for the research and development of geographically distributed network services. The platform is targeted at researchers and attempts to divide individual physical hosts into slivers, providing simultaneous low-level access to users. The current deployment uses VServers [17] and SILK [4] to manage sharing within the operating system.

We share some motivation with the operating system extensibility and active networks communities. However, when running over Xen there is no need to check for “safe” code, or for guaranteed termination — the only person hurt in either case is the client in question. Consequently, Xen provides a more general solution: there is no need for hosted code to be digitally signed by a trusted compiler (as in SPIN [5]), to be accompanied by a safety proof (as with PCC [31]), to be written in a particular language (as in SafetyNet [22] or any Java-based system), or to rely on a particular middleware (as with mobile-agent systems). These other techniques can, of course, continue to be used within guest OSes running over Xen. This may be particularly useful for workloads with more transient tasks which would not provide an opportunity to amortize the cost of starting a new domain.

A similar argument can be made with regard to language-level virtual machine approaches: while a resource-managed JVM [9] should certainly be able to host untrusted applications, these applications must necessarily be compiled to Java bytecode and follow that particular system’s security model. Meanwhile, Xen can readily support language-level virtual machines as applications running over a guest OS.
