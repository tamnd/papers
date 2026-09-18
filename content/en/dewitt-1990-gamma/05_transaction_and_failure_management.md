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
section: "5"
section_title: Transaction and Failure Management
tag: 026E
kind: section
lang: en
source: http://db.cs.berkeley.edu/cs286/papers/gamma-tkde1990.pdf
pdf_sha256: 420d33f44b8e050f33517cdff1299a58838b4ad826d80a6617200332ea02be5e
pdf_pages: 17-22
extraction: vision
extraction_model: gpt-5
content_sha256: 85cd2673868e364d06ad62fcc93e3e1adfb1ee3d1a498e985c7f98b29aeac7d0
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

In this section we describe the mechanisms that Gamma uses for transaction and failure management. While the locking mechanisms are fully operational, the recovery system is currently being implemented. We expect to begin the implementation of the failure management mechanism in early 1990.

### 5.1. Concurrency Control in Gamma {#dewitt-1990-gamma-s5-1 .section tag=026F}

Concurrency control in Gamma is based on two-phase locking [GRAY78]. Currently, two lock granularities, file, and page, and five lock modes, S, X, IS, IX, and SIX are provided. Each site in Gamma has its own local lock manager and deadlock detector. The lock manager maintains a lock table and a transaction wait-for-graph. The cost of setting a lock varies from approximately 100 instructions, if there is no conflict, to 250 instructions if the lock request conflicts with the granted group. In this case, the wait-for-graph must be checked for deadlock and the transaction that requested the lock must be suspended via a semaphore mechanism.

In order to detect multisite deadlocks, Gamma uses a centralized deadlock detection algorithm. Periodically, the centralized deadlock detector sends a message to each node in the configuration, requesting the local transaction wait-for-graph of that node. Initially, the period for running the centralized deadlock detector is set at one second. Each time the deadlock detector fails to find a global deadlock, this interval is doubled and each time a deadlock is found the current value of the interval is halved. The upper bound of the interval is limited to 60 seconds and the lower bound is 1 second. After collecting the wait-for-graph from each site, the centralized deadlock detector creates a global transaction wait-for-graph. Whenever a cycle is detected in the global wait-for-graph, the centralized deadlock manager chooses to abort the transaction holding the fewest number of locks.

### 5.2. Recovery Architecture and Log Manager {#dewitt-1990-gamma-s5-2 .section tag=0270}

The algorithms currently being implemented for coordinating transaction commit, abort, and rollback operate as follows. When an operator process updates a record, it also generates a log record which records the change of the database state. Associated with every log record is a log sequence number (LSN) which is composed of a node number and a local sequence number. The node number is statically determined at the system configuration time whereas the local sequence number, termed **current LSN**, is a monotonically increasing value.

Log records are sent by the query processors to one or more Log Managers (each running on a separate processor) which merges the log records it receives to form a single log stream. If M is the number of log processors being used, query processor i will direct its log records to the (i mod M) log processor [AGRA85]. Because this algorithm selects the log processor statically and a query processor always sends its log records to the same log processor, the recovery process at a query processing node can easily determine where to request the log records for processing a transaction abort.

When a page of log records is filled, it is written to disk. The Log Manager maintains a table, called the **Flushed Log Table**, which contains, for each node, the LSN of the last log record from that node that has been flushed to disk. These values are returned to the nodes either upon request or when they can be piggybacked on another message. Query processing nodes save this information in a local variable, termed the **Flushed LSN**.

The buffer managers at the query processing nodes observe the WAL protocol [GRAY78]. When a dirty page needs to be forced to disk, the buffer manager first compares the page’s LSN with the local value of Flushed LSN. If the page LSN of a page is smaller or equal to the Flushed LSN, that page can be safely written to disk. Otherwise, either a different dirty page must be selected, or a message must be sent to the Log Manager to flush the corresponding log record(s) of the dirty page. Only after the Log Manager acknowledges that the log record has been written to the log disk will the dirty data page be written back to disk. In order to reduce the time spent waiting for a reply from the Log Manager, the buffer manager always keeps T (a pre-selected threshold) clean and unfixed buffer pages available. When buffer manager notices that the number of clean, unfixed buffer pages has fallen below T, a process, termed **local log manager**, is activated. This process sends a message to the Log Manager to flush one or more log records so that the number of clean and unfixed pages plus the number of dirty pages that can be safely written to disk is greater than T.

The scheduler process for a query is responsible for sending commit or abort records to the appropriate Log Managers. If a transaction completes successfully, a commit record for the transaction is generated by its scheduler and sent to each relevant Log Manager which employs a group commit protocol. On the other hand, if a transaction is aborted by either the system or the user, its scheduler will send an abort message to all query processors that participated in its execution. The recovery process at each of the participating nodes responds by requesting the log records generated by the node from its Log Manager (the LSN of each log record contains the originating node number). As the log records are received, the recovery process undoes the log records in reverse chronological order using the ARIES undo algorithm [MOHA89]. The ARIES algorithms are also used as the basis for checkpointing and restart recovery.

### 5.3. Failure Management {#dewitt-1990-gamma-s5-3 .section tag=0271}

To help insure availability of the system in the event of processor and/or disk failures, Gamma employs a new availability technique termed **chained declustering** [HSIA90]. Like Tandem’s mirrored disk mechanism [BORR81] and Teradata’s interleaved declustering mechanism [TERA85, COPE89], chained declustering employs both a primary and backup copy of each relation. All three systems can sustain the failure of a single processor or disk without suffering any loss in data availability. In [HSIA90], we show that chained declustering provides a higher degree of availability than interleaved declustering and, in the event of a processor or disk failure, does a better job of distributing the workload of the broken node. The mirrored disk mechanism, while providing the highest level of availability, does a very poor job of distributing the load of a failed processor.

### Data Placement with Chained Declustering {#dewitt-1990-gamma-s-data-placement-with-chained-declustering .section tag=0272}

With chained declustering, nodes (a processor with one or more disks) are divided into disjoint groups called relation-clusters and tuples of each relation are declustered among the drives that form one of the relation clusters. Two physical copies of each relation, termed the **primary copy** and the **backup copy**, are maintained. As an example, consider Figure 9 where M, the number of disks in the relation cluster, is equal to 8. The tuples in the primary copy of relation R are declustered using one of Gamma’s three partitioning strategies with tuples in the i-th primary fragment (designated Ri) stored on the {i mod M}-th disk drive. The backup copy is declustered using the same partitioning strategy but the i-th backup fragment (designated ri) is stored on {(i + 1) mod M}-th disk. We term this data replication method **chained declustering** because the disks are linked together, by the fragments of a relation, like a chain.

Figure 9. Chained Declustering (Relation Cluster Size = 8) {#dewitt-1990-gamma-fig-9 .figure tag=0273}

The difference between the chained and interleaved declustering mechanisms [TERA85, COPE89] is illustrated by Figure 10. In Figure 10, the fragments from the primary copy of R are declustered across all 8 disk drives by hashing on a "key" attribute. With the interleaved declustering mechanism the set of disks are divided into units of size N called **clusters**. As illustrated by Figure 10, where N=4, each backup fragment is subdivided into N-1 sub-fragments and each subfragment is placed on a different disk within the same cluster other than the disk containing the primary fragment.

Figure 10. Interleaved Declustering (Cluster Size = 4) {#dewitt-1990-gamma-fig-10 .figure tag=0274}

Since interleaved and chained declustering can both sustain the failure of a single disk or processor, what then is the difference between the two mechanisms? In the case of a single node (processor or disk) failure both the chained and interleaved declustering strategies are able to uniformly distribute the workload of the cluster among the remaining operational nodes. For example, with a cluster size of 8, when a processor or disk fails, the load on each remaining node will increase by 1/7th. One might conclude then that the cluster size should be made as large as possible; until, of course, the overhead of the parallelism starts to overshadow the benefits obtained. While this is true for chained declustering, the availability of the interleaved strategy is inversely proportional to the cluster size, since the failure of any two processors or disk will render data unavailable. Thus, doubling the cluster size in order to halve (approximately) the increase in the load on the remaining nodes when a failure occurs has the (quite negative) side effect of doubling the probability that data will actually be unavailable. For this reason, Teradata recommends a cluster size of 4 or 8 processors.

Figure 11 illustrates how the workload is balanced in the event of a node failure (node 1 in this example) with the chained declustering mechanism. During the normal mode of operation, read requests are directed to the fragments of the primary copy and write operations update both copies. When a failure occurs, pieces of both the primary and backup fragments are used for read operations. For example, with the failure of node 1, primary fragment R1 can no longer be accessed and thus its backup fragment r1 on node 2 must be used for processing queries that would normally have been directed to R1. However, instead of requiring node 2 to process all accesses to both R2 and r1, chained declustering offloads 6/7-ths of the accesses to R2 by redirecting them to r2 at node 3. In turn, 5/7-ths of access to R3 at node 3 are sent to R4 instead. This dynamic reassignment of the workload results in an increase of 1/7-th in the workload of each remaining node in the cluster. Since the relation cluster size can be increased without penalty, it is possible to make this load increase as small as is desired.

|  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| **Primary Copy** | R0 | --- | $\frac{1}{7}$R2 | $\frac{2}{7}$R3 | $\frac{3}{7}$R4 | $\frac{4}{7}$R5 | $\frac{5}{7}$R6 | $\frac{6}{7}$R7 |
| **Backup Copy** | $\frac{1}{7}$r7 | --- | r1 | $\frac{6}{7}$r2 | $\frac{5}{7}$r3 | $\frac{4}{7}$r4 | $\frac{3}{7}$r5 | $\frac{2}{7}$r6 |

Fragment Utilization with Chained Declustering  
After the Failure of Node 1 (Relation Cluster Size = 8)  
Figure 11

What makes this scheme even more attractive is that the reassignment of active fragments incurs neither disk I/O nor data movement. Only some of the bound values and pointers/indices in a memory resident control table must be changed and these modifications can be done very quickly and efficiently.

The example shown in Figure 11 provides a very simplified view of how the chained declustering mechanism actually balances the workload in the event of a node failure. In reality, queries cannot simply access an arbitrary fraction of a data fragment, especially given the variety of partitioning and index mechanisms provided by the Gamma software. In [HSIA90], we describe how all combinations of query types, access methods, and partitioning
