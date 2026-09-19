---
paper: graefe-1994-volcano
title: Volcano - An Extensible and Parallel Query Evaluation System
authors:
  - Goetz Graefe
year: 1994
venue: IEEE Transactions on Knowledge and Data Engineering
field: databases
section: II
section_title: RELATED WORK
tag: 046F
kind: section
lang: en
source: http://daslab.seas.harvard.edu/reading-group/papers/volcano.pdf
pdf_sha256: 61e9ce81f84d66797c95db711fb593adcf1dbbf95fea53eba44a9b9e2239d6ca
pdf_pages: 2-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 8b90842c21390dd60eb4aa2cc07392b35bc616d83a27ad994dcd66ee6db6fb73
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Since so many different systems have been developed to process large datasets efficiently, we only survey the systems that have significantly influenced the design of Volcano. Our work has been influenced most strongly by WiSS, GAMMA, and EXODUS. The Wisconsin Storage System (WiSS) [10] is a record-oriented file system providing heap files, B-tree and hash indexes, buffering, and scans with predicates. GAMMA [11] is a software database machine running on a number of general-purpose CPU’s as a backend to a UNIX host machine. It was developed on 17 VAX 11/750’s connected with each other and the VAX 11/750 host via a 80 Mb/s token ring. Eight GAMMA processors had a local disk device, accessed using WiSS. The disks were accessible only locally, and update and selection operators used only these eight processors. The other, diskless processors were used for join processing. Recently, the GAMMA software has been ported to an Intel iPSC/2 hypercube with 32 nodes, each with a local disk drive. GAMMA uses hash-based algorithms extensively, implemented in such a way that each operator is executed on several (usually all) processors and the input stream for each operator is partitioned into disjoint sets according to a hash function.

The limited data model and extensibility of GAMMA led to the search for a more flexible but equally powerful query processing model. The operator design used in the GAMMA database machine software gives each operator control within its own process, leaving it to the networking and operating system software to synchronize multiple operators in producer-consumer relationships using flow-control mechanisms. This design, while working extremely well in GAMMA, does not lend itself to single-process query evaluation since multiple loci of control, i.e., multiple operators, cannot be realized inside a single process without special pseudo-multiprocess mechanisms such as threads. Therefore, GAMMA’s operator and data transfer concepts are not suitable for an efficient query processing engine intended for both sequential and parallel query execution.

EXODUS [7] is an extensible database system with some components following the “tool-kit” approach, e.g., the optimizer generator [13], [14] and the E database implementation language [27], [28], and other components built as powerful but fixed components, e.g., the storage manager [5]. Originally, EXODUS was conceived to be data-model-independent, i.e., it was supposed to support a wide variety of data models, but later a novel, powerful, structurally object-oriented data model called Extra was developed [6]. The concept of data model independence as first explored in EXODUS has been retained in the Volcano project and the design and implementation of its software. During the design of the EXODUS storage manager, many storage and access issues explored in WiSS and GAMMA were revisited. Lessons learned and trade-offs explored in these discussions certainly helped in forming the ideas behind Volcano. The design and development of E influenced the strong emphasis on iterators for query processing.

A number of further conventional (relational) and extensible systems have influenced our design. Ingres [32] and System R [9] have probably influenced most database systems, in particular their extensible follow-on projects Starburst [23] and Postgres [35]. It is interesting to note that independently of our work the Starburst group has also identified the demand-driven interator paradigm as a suitable basis for an extensible single-process query evaluation architecture after using it successfully in the System R relational system, but as yet has not been able to combine extensibility with parallelism. GENESIS [1] early on stressed the importance of uniform operator interfaces for extensibility and software reusability.

XPRS has been the first project aiming to combine extensibility with parallelism [34]. Its basic premise is to implement Postgres on top of RAID disk arrays and the Sprite operating system. XPRS and GAMMA basically differ in four ways. First, GAMMA supports a purely relational data model while XPRS supports an extensible relational model, Postgres. Second, GAMMA’s main form of parallelism is intra-operator parallelism based on partitioned data sets. XPRS, on the other hand, will rely on bushy parallelism, i.e., concurrent execution of different subtrees in a complex query evaluation plan. Third, GAMMA relies heavily on hashing for joins and aggregations whereas XPRS will have a mainly sort-based query processing engine [33]. Fourth, GAMMA is built on the premise that distributed memory is required to achieve scalable linear speed-up while XPRS is being implemented on a shared-memory machine.

Both XPRS and Volcano combine parallelism and extensibility, but XPRS is a far more comprehensive project than Volcano. In particular, XPRS includes a data model and a query optimizer. On the other hand, Volcano is more extensible precisely because it does not presume a data model. Therefore, Volcano could be used as the query processing engine in a parallel extensible-relational system such as XPRS. Moreover, it will eventually include a data-model-independent optimizer generator to form a complete query processing research environment.
