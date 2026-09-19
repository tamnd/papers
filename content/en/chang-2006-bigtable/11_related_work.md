---
paper: chang-2006-bigtable
title: 'Bigtable: A Distributed Storage System for Structured Data'
authors:
  - Fay Chang
  - Jeffrey Dean
  - Sanjay Ghemawat
  - Wilson C. Hsieh
  - Deborah A. Wallach
  - Mike Burrows
  - Tushar Chandra
  - Andrew Fikes
  - Robert E. Gruber
year: 2006
venue: OSDI
field: databases
section: "10"
section_title: Related Work
tag: "0797"
kind: section
lang: en
source: http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.101.9822
pdf_sha256: 9126cf3b930fd7be2de6248f82565c9b970482eb063bdc30be8c1b29c86b2167
pdf_pages: 12-14
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 24df75b0de364b00aabdb0b89e380763472e626817b8698254a2f9209838e397
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The Boxwood project [24] has components that overlap in some ways with Chubby, GFS, and Bigtable, since it provides for distributed agreement, locking, distributed chunk storage, and distributed B-tree storage. In each case where there is overlap, it appears that the Boxwood’s component is targeted at a somewhat lower level than the corresponding Google service. The Boxwood project’s goal is to provide infrastructure for building higher-level services such as file systems or databases, while the goal of Bigtable is to directly support client applications that wish to store data.

Many recent projects have tackled the problem of providing distributed storage or higher-level services over wide area networks, often at “Internet scale.” This includes work on distributed hash tables that began with projects such as CAN [29], Chord [32], Tapestry [37], and Pastry [30]. These systems address concerns that do not arise for Bigtable, such as highly variable bandwidth, untrusted participants, or frequent reconfiguration; decentralized control and Byzantine fault tolerance are not Bigtable goals.

In terms of the distributed data storage model that one might provide to application developers, we believe the key-value pair model provided by distributed B-trees or distributed hash tables is too limiting. Key-value pairs are a useful building block, but they should not be the only building block one provides to developers. The model we chose is richer than simple key-value pairs, and supports sparse semi-structured data. Nonetheless, it is still simple enough that it lends itself to a very efficient flat-file representation, and it is transparent enough (via locality groups) to allow our users to tune important behaviors of the system.

Several database vendors have developed parallel databases that can store large volumes of data. Oracle’s Real Application Cluster database [27] uses shared disks to store data (Bigtable uses GFS) and a distributed lock manager (Bigtable uses Chubby). IBM’s DB2 Parallel Edition [4] is based on a shared-nothing [33] architecture similar to Bigtable. Each DB2 server is responsible for a subset of the rows in a table which it stores in a local relational database. Both products provide a complete relational model with transactions.

G. P., AND WILSON, W. G. DB2 parallel edition. *IBM Systems Journal* 34, 2 (1995), 292–322.
