---
paper: mohan-1992-aries
title: 'ARIES: A Transaction Recovery Method Supporting Fine-Granularity Locking and Partial Rollbacks Using Write-Ahead Logging'
authors:
  - C. Mohan
  - Don Haderle
  - Bruce Lindsay
  - Hamid Pirahesh
  - Peter Schwarz
year: 1992
venue: ACM TODS
field: databases
section: "12"
section_title: ATTRIBUTES OF ARIES
tag: 074C
kind: section
lang: en
source: https://people.eecs.berkeley.edu/~brewer/cs262/Aries2.pdf
pdf_sha256: 1007fcedb6b8b465f97ee1c4e4d88420450b50b18ff5ad400a130b21e4961817
pdf_pages: 29-31
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: b9fb238ce958062191fb843b772f68e052f1df2477b5a1df1e60825deb56973b
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

ARIES makes few assumptions about the data or its model and has several advantages over other recovery methods. While ARIES is simple, it possesses several interesting and useful properties. Each of most of these properties has been demonstrated in one or more existing or proposed systems, as summarized in the last section. However, we know of no single system, proposed or real, which has all of these properties. Some of these properties of ARIES are:

(1) Support for finer than page-level concurrency control and multiple granularities of locking. ARIES supports page-level and record-level locking in a uniform fashion. Recovery is not affected by what the granularity of locking is. Depending on the expected contention for the data, the appropriate level of locking can be chosen. It also allows multiple granularities of locking (e.g., record, table, and tablespace-level) for the same object (e.g., tablespace). Concurrency control schemes other than locking (e.g., the schemes of [2]) can also be used.

(2) Flexible buffer management during restart and normal processing. As long as the write-ahead logging protocol is followed, the buffer manager is free to use any page replacement policy. In particular, dirty pages of incomplete transactions can be written to nonvolatile storage before those transactions commit (steal policy). Also, it is not required that all pages dirtied by a transaction be written back to nonvolatile storage before the transaction is allowed to commit (i.e., no-force policy). These properties lead to reduced demands for buffer storage and fewer I/Os involving frequently updated (hot-spot) pages. ARIES does not preclude the possibilities of using deferred-updating and force-at-commit policies and benefiting from them. ARIES is quite flexible in these respects.

(3) Minimal space overhead—only one LSN per page. The permanent (excluding log) space overhead of this scheme is limited to the storage required on each page to store the LSN of the last logged action performed on the page. The LSN of a page is a monotonically increasing value.

(4) No constraints on data to guarantee idempotence of redo or undo of logged actions. There are no restrictions on the data with respect to unique keys, etc. Records can be of variable length. Data can be moved around within a page for garbage collection. Idempotence of operations is ensured since the LSN on each page is used to determine whether an operation should be redone or not.

(5) Actions taken during the undo of an update need not necessarily be the exact inverses of the actions taken during the original update. Since CLRs are being written during undos, any differences between the inverses of the original actions and what actually had to be done during undo can be recorded in the former. An example of when the inverse might not be correct is the one that relates to the free space information (like at least 10% free, 20% free) about data pages that are maintained in space map pages. Because of finer than page-level granularity locking, while no free space information change takes place during the initial update of a page by a transaction, a free space information change might occur during the undo (from 20% free to 10% free) of that original change because of intervening update activities of other transactions (see Section 10.3).

Other benefits of this attribute in the context of hash-based storage methods and index management can be found in [59, 62].

(6) Support for operation logging and novel lock modes. The changes made to a page can be logged in a logical fashion. The undo information and the redo information for the entire object need not be logged. It suffices if the changed fields alone are logged. Since history is repeated, for increment or decrement kinds of operations before-and after-images of the field are not needed. Information about the type of operation and the decrement or increment amount is enough. Garbage collection actions and changes to some fields (e.g., amount of free space) of that page need not be logged. Novel lock modes based on commutativity and other properties of operations can be supported [2, 26, 88].

(7) Even redo-only and undo-only records are accommodated. While it may be efficient (single call to the log component) sometimes to include the undo and redo information about an update in the same log record, at other times it may be efficient (from the original data, the undo record can be constructed and, after the update is performed in-place in the data record, from the updated data, the redo record can be constructed) and/or necessary (because of log record size restrictions) to log the information in two different records. ARIES can handle both situations. Under these conditions, the undo record must be logged before the redo record.

(8) Support for partial and total transaction rollback. Besides allowing transactions to be rolled back totally, ARIES allows the establishment of savepoints and the partial rollback of transactions to such savepoints. Without the support for partial rollbacks, even logically recoverable errors (e.g., unique key violation, out-of-date cached catalog information in a distributed database system) will require total rollbacks and result in wasted work.

(9) Support for objects spanning multiple pages. Objects can span multiple pages (e.g., an IMS “record” which consists of multiple segments may be scattered over many pages). When an object is modified, if log records are written for every page affected by that update, ARIES works fine. ARIES itself does not treat multipage objects in any special way.

(10) Allows files to be acquired or returned, any time, from or to the operating system. ARIES provides the flexibility of being able to return files dynamically and permanently to the operating system (see [19] for the detailed description of a technique to accomplish this). Such an action is considered to be one that cannot be undone. It does not prevent the same file from being reallocated to the database system. Mappings between objects (tablespaces, etc.) and files are not required to be defined statically as in System R.

(11) Some actions of a transaction may be committed even if the transaction as a whole is rolled back. This refers to the technique of using the concept of a dummy CLR to implement nested top actions. File extension has been given as an example situation which could benefit from this. Other applications of this technique, in the context of hash-based storage methods and index management, can be found in [59, 62].

(12) Efficient checkpoints (including during restart recovery). By supporting fuzzy checkpointing, ARIES makes taking a checkpoint an efficient operation. Checkpoints can be taken even when update activities and logging are going on concurrently. Permitting checkpoints even during restart processing will help reduce the impact of failures during restart recovery. The dirty-pages information written during checkpointing helps reduce the number of pages which are read from nonvolatile storage during the redo pass.

(13) Simultaneous processing of multiple transactions in forward processing and/or in rollback accessing same page. Since many transactions could simultaneously be going forward or rolling back on a given page, the level of concurrent access supported could be quite high. Except for the short duration latching which has to be performed any time a page is being physically modified or examined, be it during forward processing or during rollback, rolling back transactions do not affect one another in any unusual fashion.

(14) No locking or deadlocks during transaction rollback. Since no locking is required during transaction rollback, no deadlocks will involve transactions that are rolling back. Avoiding locking during rollbacks simplifies not only the rollback logic, but also the deadlock detector logic. The deadlock detector need not worry about making the mistake of choosing a rolling back transaction as a victim in the event of a deadlock (cf. System R and R* [31, 49, 64]).

(15) Bounded logging during restart in spite of repeated failures or of nested rollbacks. Even if repeated failures occur during restart, the number of CLRs written is unaffected. This is also true if partial rollbacks are nested. The number of log records written will be the same as that written at the time of transaction rollback during normal processing. The latter again is a fixed number and is, usually, equal to the number of undoable records written during the forward processing of the transaction. No log records are written during the redo pass of restart.

(16) Permits exploitation of parallelism and selective/deferred processing for faster restart. Restart can be made faster by not doing all the needed I/Os synchronously one at a time while processing the corresponding log record. ARIES permits the early identification of the pages needing recovery and the initiation of asynchronous parallel I/Os for the reading in of those pages. The pages can be processed concurrently as they are brought into memory during the redo pass. Undo parallelism requires complete handling of a given transaction by a single process. Some of the restart processing can be postponed to speed up restart or to accommodate offline devices. If desired, undo of loser transactions can be performed in parallel with new transaction processing.

(17) Fuzzy image copying (archive dumping) for media recovery. Media recovery and image copying of the data are supported very efficiently. To take advantage of device geometry, the actual act of copying can even be performed outside the transaction system (i.e., without going through the buffer pool). This can happen even while the latter is accessing and modifying the information being copied. During media recovery only one forward traversal of the log is made.

(18) Continuation of loser transactions after a system restart. Since ARIES repeats history and supports the savepoint concept, we could, in the undo pass, instead of totally rolling back the loser transactions, roll back each loser only to its latest savepoint. Locks must be acquired to protect the transaction’s uncommitted, not undone updates. Later, we could resume the transaction by invoking its application at a special entry point and passing enough information about the savepoint from which execution is to be resumed.

(19) Only one backward traversal of log during restart or media recovery.

Both during media recovery and restart recovery one backward traversal of the log is sufficient. This is especially important if any portion of the log is likely to be stored in a slow medium like tape.

Repeating history exactly, which in turn implies using LSNs and writing CLRs during undos, permits the following, irrespective of whether CLRs are chained using the UndoNxtLSN field or not:

(1) Record level locking to be supported and records to be moved around within a page to avoid storage fragmentation without the moved records having to be locked and without the movements having to be logged.

(2) Use only one state variable, a log sequence number, per page.

(3) Reuse of storage released by one transaction for the same transaction’s later actions or for other transactions’ actions once the former commits, thereby leading to the preservation of clustering of records and the efficient usage of storage.

(4) The inverse of an action originally performed during forward processing of a transaction to be different from the action(s) performed during the undo of that original action (e.g., class changes in the space map pages). That is, logical undo with recovery independence is made possible.

(5) Multiple transactions may undo on the same page concurrently with transactions going forward.

(6) Recovery of each page independently of other pages or of log records relating to transaction state, especially during media recovery.

(7) If necessary, the continuation of transactions which were in progress at the time of system failure.

(8) Selective or deferred restart, and undo of losers concurrently with new transaction processing to improve data availability.

(9) Partial rollback of transactions.

(10) Operation logging and logical logging of changes within a page. For example, decrement and increment operations may be logged, rather than the before- and after-images of modified data.

(1) The avoidance of undoing CLRs’ actions, thus avoiding writing CLRs for Chaining, using the UndoNxtLSN field, CLRs to log records written during forward processing permits the following, provided the protocol of repeating history is also followed:

(2) The avoidance of the undo of the same log record written during forward processing more than once.

(3) As a transaction is being rolled back, the ability to release the lock on an object when all the updates to that object had been undone. This may be important while rolling back a long transaction or while resolving a deadlock by partially rolling back the victim.

(4) Handling partial rollbacks without any special actions like patching the log, as in System R.

(5) Making permanent, if necessary via nested top actions, some of the

Both during media recovery and restart recovery one backward traversal of the log is sufficient. This is especially important if any portion of the log is likely to be stored in a slow medium like tape.

(20) Need only redo information in compensation log records. Since compensation records are never undone they need to contain only redo information. So, on the average, the amount of log space consumed during a transaction rollback will be half the space consumed during the forward processing of that transaction.

(21) Support for distributed transactions. ARIES accommodates distributed transactions. Whether a given site is a coordinator or a subordinate site does not affect ARIES.

(22) Early release of locks during transaction rollback and deadlock resolution using partial rollbacks. Because ARIES never undoes CLRs and because it never undoes a particular non-CLR more than once, during a (partial) rollback, when the transaction’s very first update to a particular object is undone and a CLR is written for it, the system can release the lock on that object. This makes it possible to consider resolving deadlocks using partial rollbacks.

It should be noted that ARIES does not prevent the shadow page technique from being used for selected portions of the data to avoid logging of only undo information or both undo and redo information. This may be useful for dealing with long fields, as is the case in the OS/2 Extended Edition Database Manager. In such instances, for such data, the modified pages would have to be forced to nonvolatile storage before commit. Whether or not media recovery and partial rollbacks can be supported will depend on what is logged and for which updates shadowing is done.
