---
paper: dewitt-1990-gamma
title: The Gamma Database Machine Project
authors:
  - David J. DeWitt
  - Shahram Ghandeharizadeh
  - Donovan A. Schneider
  - Allan Bricker
  - Hui-I Hsiao
  - Rick Rasmussen
year: 1990
venue: IEEE Transactions on Knowledge and Data Engineering
field: databases
section: "1"
section_title: Introduction
tag: 025B
kind: section
lang: en
source: http://db.cs.berkeley.edu/cs286/papers/gamma-tkde1990.pdf
pdf_sha256: 420d33f44b8e050f33517cdff1299a58838b4ad826d80a6617200332ea02be5e
pdf_pages: 3-4
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 434add00e0ae560c63acb70842242b32758e774839296c1ccb18fdaa5ee2dee4
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

For the last 5 years, the Gamma database machine project has focused on issues associated with the design and implementation of highly parallel database machines. In a number of ways, the design of Gamma is based on what we learned from our earlier database machine DIRECT [DEWI79]. While DIRECT demonstrated that parallelism could be successfully applied to processing database operations, it had a number of serious design deficiencies that made scaling of the architecture to 100s of processors impossible; primarily the use of shared memory and centralized control for the execution of its parallel algorithms [BITT83].

As a solution to the problems encountered with DIRECT, Gamma employs what appear today to be relatively straightforward solutions. Architecturally, Gamma is based on a shared-nothing [STON86] architecture consisting of a number of processors interconnected by a communications network such as a hypercube or a ring, with disks directly connected to the individual processors. It is generally accepted that such architectures can be scaled to incorporate 1000s of processors. In fact, Teradata database machines [TERA85] incorporating a shared-nothing architecture with over 200 processors are already in use. The second key idea employed by Gamma is the use of hash-based parallel algorithms. Unlike the algorithms employed by DIRECT, these algorithms require no centralized control and can thus, like the hardware architecture, be scaled almost indefinitely. Finally, to make the best of the limited I/O bandwidth provided by the current generation of disk drives, Gamma employs the concept of horizontal partitioning [RIES78] (also termed declustering [LIVN87]) to distribute the tuples of a relation among multiple disk drives. This design enables large relations to be processed by multiple processors concurrently without incurring any communications overhead.

After the design of the Gamma software was completed in the fall of 1984, work began on the first prototype which was operational by the fall of 1985. This version of Gamma was implemented on top of an existing multi-computer consisting of 20 VAX 11/750 processors [DEWI84b]. In the period of 1986-1988, the prototype was enhanced through the addition of a number of new operators (e.g. aggregate and update operators), new parallel join methods (Hybrid, Grace, and Sort-Merge [SCHN89a]), and a complete concurrency control mechanism. In addition, we also conducted a number of performance studies of the system during this period [DEWI86, DEWI88, GHAN89, GHAN90]. In the spring of 1989, Gamma was ported to a 32 processor Intel iPSC/2 hypercube and the VAX-based prototype was retired.

Gamma is similar to a number of other active parallel database machine efforts. In addition to Teradata [TERA85], Bubba [COPE88] and Tandem [TAND88] also utilize a shared-nothing architecture and employ the concept of horizontal partitioning. While Teradata and Tandem also rely on hashing to decentralize the execution of their parallel algorithms, both systems tend to rely on relatively conventional join algorithms such as sort-merge for processing the fragments of the relation at each site. Gamma, XPRS [STON88], and Volcano [GRAE89] each utilize parallel versions of the Hybrid join algorithm [DEWI84a].

The remainder of this paper is organized as follows. In Section 2 we describe the hardware used by each of the Gamma prototypes and our experiences with each. Section 3 discusses the organization of the Gamma software and describes how multioperator queries are controlled. The parallel algorithms employed by Gamma are described in Section 4 and the techniques we employ for transaction and failure management are contained in Section 5. Section 6 contains a performance study of the 32 processor Intel hypercube prototype. Our conclusions and future research directions are described in Section 7.
