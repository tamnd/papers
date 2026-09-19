---
paper: stonebraker-2005-cstore
title: 'C-Store: A Column-oriented DBMS'
authors:
  - Mike Stonebraker
  - Daniel J. Abadi
  - Adam Batkin
  - Xuedong Chen
  - Mitch Cherniack
  - Miguel Ferreira
  - Edmond Lau
  - Amerson Lin
  - Sam Madden
  - Elizabeth O'Neil
  - Pat O'Neil
  - Alex Rasin
  - Nga Tran
  - Stan Zdonik
year: 2005
venue: VLDB
field: databases
section: "6"
section_title: Updates and Transactions
tag: 075B
kind: section
lang: en
source: https://www.vldb.org/archives/website/2005/program/paper/thu/p553-stonebraker.pdf
pdf_sha256: c619eacc696c847e0d7697edb9193a2c35f242b12ac2835f486970a07129eecb
pdf_pages: 6-8
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 46fa96f06dc2448678dca39f273c97e616d385244a78df7297f2d034cf864d5f
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

An insert is represented as a collection of new objects in WS, one per column per projection, plus the sort key data structure. All inserts corresponding to a single logical record have the same storage key. The storage key is allocated at the site where the update is received. To prevent C-Store nodes from needing to synchronize with each other to assign storage keys, each node maintains a locally unique counter to which it appends its local site id to generate a globally unique storage key. Keys in the WS will be consistent with RS storage keys because we set the initial value of this counter to be one larger than the largest key in RS.

We are building WS on top of BerkeleyDB [SLEE04]; we use the B-tree structures in that package to support our data structures. Hence, every insert to a projection results in a collection of physical inserts on different disk pages, one per column per projection. To avoid poor performance, we plan to utilize a very large main memory buffer pool, made affordable by the plummeting cost per byte of primary storage. As such, we expect “hot” WS data structures to be largely main memory resident.

C-Store’s processing of deletes is influenced by our locking strategy. Specifically, C-Store expects large numbers of ad-hoc queries with large read sets interspersed with a smaller number of OLTP transactions covering few records. If C-Store used conventional locking, then substantial lock contention would likely be observed, leading to very poor performance.

Instead, in C-Store, we isolate read-only transactions using snapshot isolation. Snapshot isolation works by allowing read-only transactions to access the database as of some time in the recent past, before which we can guarantee that there are no uncommitted transactions. For this reason, when using snapshot isolation, we do not need to set any locks. We call the most recent time in the past at which snapshot isolation can run the high water mark (HWM) and introduce a low-overhead mechanism for keeping track of its value in our multi-site environment. If we let read-only transactions set their effective time arbitrarily, then we would have to support general time travel, an onerously expensive task. Hence, there is also a low water mark (LWM) which is the earliest effective time at which a read-only transaction can run. Update transactions continue to set read and write locks and obey strict two-phase locking, as described in Section 6.2.

### 6.1 Providing Snapshot Isolation {#stonebraker-2005-cstore-s6-1 .section tag=075C}

The key problem in snapshot isolation is determining which of the records in WS and RS should be visible to a read-only transaction running at effective time ET. To provide snapshot isolation, we cannot perform updates in place. Instead, an update is turned into an insert and a delete. Hence, a record is visible if it was inserted before ET and deleted after ET. To make this determination without requiring a large space budget, we use coarse granularity “epochs,” to be described in Section 6.1.1, as the unit for timestamps. Hence, we maintain an insertion vector (IV) for each projection segment in WS, which contains for each record the epoch in which the record was inserted. We program the tuple mover (described in Section 7) to ensure that no records in RS were inserted after the LWM. Hence, RS need not maintain an insertion vector. In addition, we maintain a deleted record vector (DRV) for each projection, which has one entry per projection record, containing a 0 if the tuple has not been deleted; otherwise, the entry contains the epoch in which the tuple was deleted. Since the DRV is very sparse (mostly zeros), it can be compactly coded using the type 2 algorithm described earlier. We store the DRV in the WS, since it must be updatable. The runtime system can now consult IV and DRV to make the visibility calculation for each query on a record-by-record basis.

### 6.1.1 Maintaining the High Water Mark {#stonebraker-2005-cstore-s6-1-1 .section tag=075D}

To maintain the HWM, we designate one site the timestamp authority (TA) with the responsibility of allocating timestamps to other sites. The idea is to divide time into a number of epochs; we define the epoch number to be the number of epochs that have elapsed since the beginning of time. We anticipate epochs being relatively long – e.g., many seconds each, but the exact duration may vary from deployment to deployment. We define the initial HWM to be epoch 0 and start current epoch at 1. Periodically, the TA decides to move the system to the next epoch; it sends a end of epoch message to each site, each of which increments current epoch from e to e+1, thus causing new transactions that arrive to be run with a timestamp e+1. Each site waits for all the transactions that began in epoch e (or an earlier epoch) to complete and then sends an epoch complete message to the TA. Once the TA has received epoch complete messages from all sites for epoch e, it sets the HWM to be e, and sends this value to each site. Figure 3 illustrates this process.

After the TA has broadcast the new HWM with value e, read-only transactions can begin reading data from epoch e or earlier and be assured that this data has been committed. To allow users to refer to a particular real-world time when their query should start, we maintain a table mapping epoch numbers to times, and start the query as of the epoch nearest to the user-specified time.

To avoid epoch numbers from growing without bound and consuming extra space, we plan to “reclaim” epochs that are no longer needed. We will do this by “wrapping” timestamps, allowing us to reuse old epoch numbers as in other protocols, e.g., TCP. In most warehouse applications, records are kept for a specific amount of time, say 2 years. Hence, we merely keep track of the oldest epoch in any DRV, and ensure that wrapping epochs through zero does not overrun.

To deal with environments for which epochs cannot effectively wrap, we have little choice but to enlarge the “wrap length” of epochs or the size of an epoch.

### 6.2 Locking-based Concurrency Control {#stonebraker-2005-cstore-s6-2 .section tag=075E}

Read-write transactions use strict two-phase locking for concurrency control [GRAY92]. Each site sets locks on data objects that the runtime system reads or writes, thereby implementing a distributed lock table as in most distributed databases. Standard write-ahead logging is employed for recovery purposes; we use a NO-FORCE, STEAL policy [GRAY92] but differ from the traditional implementation of logging and locking in that we only log UNDO records, performing REDO as described in Section 6.3, and we do not use strict two-phase commit, avoiding the PREPARE phase as described in Section 6.2.1 below.

Locking can, of course, result in deadlock. We resolve deadlock via timeouts through the standard technique of aborting one of the deadlocked transactions.

### 6.2.1 Distributed COMMIT Processing {#stonebraker-2005-cstore-s6-2-1 .section tag=075F}

In C-Store, each transaction has a master that is responsible for assigning units of work corresponding to a transaction to the appropriate sites and determining the ultimate commit state of each transaction. The protocol differs from two-phase commit (2PC) in that no PREPARE messages are sent. When the master receives a COMMIT statement for the transaction, it waits until all workers have completed all outstanding actions and then issues a commit (or abort) message to each site. Once a site has received a commit message, it can release all locks related to the transaction and delete the UNDO log for the transaction. This protocol differs from 2PC because the master does not PREPARE the worker sites. This means it is possible for a site the master has told to commit to crash before writing any updates or log records related to a transaction to stable storage. In such cases, the failed site will recover its state, which will reflect updates from the committed transaction, from other projections on other sites in the system during recovery.

### 6.2.2 Transaction Rollback {#stonebraker-2005-cstore-s6-2-2 .section tag=0760}

When a transaction is aborted by the user or the C-

Figure.

Figure 3. Illustration showing how the HWM selection algorithm works. Gray arrows indicate messages from the TA to the sites or vice versa. We can begin reading tuples with timestamp e when all transactions from epoch e have committed. Note that although T4 is still executing when the HWM is incremented, read-only transactions will not see its updates because it is running in epoch e+1. {#stonebraker-2005-cstore-fig-3 .figure tag=0761}

Store system, it is undone by scanning backwards in the UNDO log, which contains one entry for each logical update to a segment. We use logical logging (as in ARIES [MOHA92]), since physical logging would result in many log records, due to the nature of the data structures in WS.

### 6.3 Recovery {#stonebraker-2005-cstore-s6-3 .section tag=0762}

As mentioned above, a crashed site recovers by running a query (copying state) from other projections. Recall that C-Store maintains K-safety; i.e. sufficient projections and join indexes are maintained, so that K sites can fail within t, the time to recover, and the system will be able to maintain transactional consistency. There are three cases to consider. If the failed site suffered no data loss, then we can bring it up to date by executing updates that will be queued for it elsewhere in the network. Since we anticipate read-mostly environments, this roll forward operation should not be onerous. Hence, recovery from the most common type of crash is straightforward. The second case to consider is a catastrophic failure which destroys both the RS and WS. In this case, we have no choice but to reconstruct both segments from other projections and join indexes in the system. The only needed functionality is the ability to retrieve auxiliary data structures (IV, DRV) from remote sites. After restoration, the queued updates must be run as above. The third case occurs if WS is damaged but RS is intact. Since RS is written only by the tuple mover, we expect it will typically escape damage. Hence, we discuss this common case in detail below.

### 6.3.1 Efficiently Recovering the WS {#stonebraker-2005-cstore-s6-3-1 .section tag=0763}

Consider a WS segment, Sr, of a projection with a sort key K and a key range R on a recovering site r along with a collection C of other projections, M1, ..., Mb which contain the sort key of Sr. The tuple mover guarantees that each WS segment, S, contains all tuples with an insertion timestamp later than some time t_lastmove(S), which represents the most recent insertion time of any record in S’s corresponding RS segment.

To recover, the recovering site first inspects every projection in C for a collection of columns that covers the key range K with each segment having t_lastmove(S) ≤ t_lastmove(Sr). If it succeeds, it can run a collection of queries of the form:

SELECT desired_fields,
    insertion_epoch,
    deletion_epoch
FROM recovery_segment
WHERE insertion_epoch > t_lastmove(Sr)
    AND insertion_epoch <= HWM
    AND deletion_epoch = 0
        OR deletion_epoch >= LWM
    AND sort_key in K

As long as the above queries return a storage key, other fields in the segment can be found by following appropriate join indexes. As long as there is a collection of segments that cover the key range of Sr, this technique will restore Sr to the current HWM. Executing queued updates will then complete the task.

On the other hand, if there is no cover with the desired property, then some of the tuples in Sr have already been moved to RS on the remote site. Although we can still query the remote site, it is challenging to identify the desired tuples without retrieving everything in RS and differencing against the local RS segment, which is obviously an expensive operation.

To efficiently handle this case, if it becomes common, we can force the tuple mover to log, for each tuple it moves, the storage key in RS that corresponds to the storage key and epoch number of the tuple before it was moved from WS. This log can be truncated to the timestamp of the oldest tuple still in the WS on any site, since no tuples before that will ever need to be recovered. In this case, the recovering site can use a remote WS segment, S, plus the tuple mover log to solve the query above, even though t_lastmove(S) comes after t_lastmove(Sr).

At r, we must also reconstruct the WS portion of any join indexes that are stored locally, i.e. for which Sr is a “sender.” This merely entails querying remote “receivers,” which can then compute the join index as they generate tuples, transferring the WS partition of the join index along with the recovered columns.
