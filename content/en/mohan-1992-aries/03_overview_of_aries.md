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
section: "3"
section_title: OVERVIEW OF ARIES
tag: "0728"
kind: section
lang: en
source: https://people.eecs.berkeley.edu/~brewer/cs262/Aries2.pdf
pdf_sha256: 1007fcedb6b8b465f97ee1c4e4d88420450b50b18ff5ad400a130b21e4961817
pdf_pages: 8-10
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 07881512548902fa7a054c223ca4415edc464d0c5e416a0f2e941f8be1256394
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The aim of this section is to provide a brief overview of the new recovery method ARIES, which satisfies quite reasonably the goals that we set forth in Section 2. Issues like deferred and selective restart, parallelism during restart recovery, and so on will be discussed in the later sections of the paper.

ARIES guarantees the atomicity and durability properties of transactions in the fact of process, transaction, system and media failures. For this purpose, ARIES keeps track of the changes made to the database by using a log and it does write-ahead logging (WAL). Besides logging, on a per-affected-page basis, update activities performed during forward processing of transactions, ARIES also logs, typically using compensation log records (CLRs), updates performed during partial or total rollbacks of transactions during both normal and restart processing. Figure 3 gives an example of a partial rollback in which a transaction, after performing three updates, rolls back two of them and then starts going forward again. Because of the undo of the two updates, two CLRs are written. In ARIES, CLRs have the property that they are redo-only log records. By appropriate chaining of the CLRs to log records written during forward processing, a bounded amount of logging is ensured during rollbacks, even in the face of repeated failures during restart or of nested rollbacks. This is to be contrasted with what happens in IMS, which may undo the same non-CLR multiple times, and in AS/400, DB2 and NonStop SQL, which, besides undoing the same non-CLR multiple times, may also undo CLRs one or more times (see Figure 4). These have caused severe problems in real-life customer situations.

In ARIES, as Figure 5 shows, when the undo of a log record causes a CLR to be written, the CLR, besides containing a description of the compensating action for redo purposes, is made to contain the UndoNxtLSN pointer which points to the predecessor of the just undone log record. The predecessor information is readily available since every log record, including a CLR, contains the PrevLSN pointer which points to the most recent preceding log record written by the same transaction. The UndoNxtLSN pointer allows us to determine precisely how much of the transaction has not been undone so far. In Figure 5, log record 3', which is the CLR for log record 3, points to log record 2, which is the predecessor of log record 3. Thus, during rollback, the UndoNxtLSN field of the most recently written CLR keeps track of the progress of rollback. It tells the system from where to continue the rollback of the transaction, if a system failure were to interrupt the completion of the rollback or if a nested rollback were to be performed. It lets the system bypass those log records that had already been undone. Since CLRs are available to describe what actions are actually performed during the undo of an original action, the undo action need not be, in terms of which page(s) is affected, the exact inverse of the original action. That is, logical undo which allows very high concurrency to be supported is made possible. For example,

ARIES: A Transaction Recovery Method

Fig. 3. Partial rollback example. {#mohan-1992-aries-fig-3 .figure tag=0729}

After performing 3 actions, the transaction performs a partial rollback by undoing actions 3 and 2, writing the compensation log records 3' and 2', and then starts going forward again and performs actions 4 and 5

Fig. 4 Problem of compensating compensations or duplicate compensations, or both.

I' is the CLR for I and r'' is the CLR for I'

Fig. 5. ARIES' technique for avoiding compensating compensations and duplicate compensations. {#mohan-1992-aries-fig-5 .figure tag=072A}

Y' is the Compensation Log Record for I
Y' points to the predecessor, if any, of I

Before Failure

| Log | 1 | 2 | 3 | 3' | 2' | 4 | 5 |
| --- | --- | --- | --- | --- | --- | --- | --- |

During Restart

| Log | 1 | 2 | 3 | 3' | 2' | 4 | 5 |
| --- | --- | --- | --- | --- | --- | --- | --- |

Before Failure

| Log | 1 | 2 | 3 | 3' | 2' | 4 | 5 |
| --- | --- | --- | --- | --- | --- | --- | --- |

During Restart

| Log | 1' | 2 | 3 | 3' | 2' | 4 | 5 |
| --- | --- | --- | --- | --- | --- | --- | --- |

a key inserted on page 10 of a B+-tree by one transaction may be moved to a page is updated and a log record is written, the LSN of the log record is placed in the page_LSN field of the updated page. This tagging of the page with the LSN allows ARIES to precisely track, for restart- and media-recovery purposes, the state of the page with respect to logged updates for that page. It allows ARIES to support novel lock modes, using which, before an update performed on a record's field by one transaction is committed, another transaction may be permitted to modify the same data for specified operations.

Periodically during normal processing, ARIES takes checkpoints. The checkpoint log records identify the transactions that are active, their states, and the LSNs of their most recently written log records, and also the modified data (dirty data) that is in the buffer pool. The latter information is needed to determine from where the redo pass of restart recovery should begin its processing.

ARIES uses a single LSN on each page to track the page's state. Whenever the database as of the time of the system failure. A log record's update is redone if the affected page's page_LSN is less than the log record's LSN. No logging is performed when updates are redone. The redo pass obtains the locks needed to protect the uncommitted updates of those distributed transactions that will remain in the in-doubt (prepared) state [63, 64] at the end of restart recovery.

The next log pass is the undo pass during which all loser transactions' updates are rolled back, in reverse chronological order, in a single sweep of the log. This is done by continually taking the maximum of the LSNs of the next log record to be processed for each of the yet-to-be-completely-undone loser transactions, until no transaction remains to be undone. Unlike during the redo pass, performing undos is not a conditional operation during the undo pass (and during normal undo). That is, ARIES does not compare the page_LSN of the affected page to the LSN of the log record to decide

Type. Indicates whether this is a compensation record ('compensation'), a regular update record ('update'), a commit protocol-related record (e.g., 'pre-pare'), or a nontransaction-related record (e.g., 'OSfile_return').

LSN. Address of the first byte of the log record in the ever-growing log address space. This is a monotonically increasing value. This is shown here as a field only to make it easier to describe ARIES. The LSN need not actually be stored in the record.

TransID. Identifier of the transaction, if any, that wrote the log record.

PageID. Present only in records of type 'update' or 'compensation'. The identifier of the page to which the updates of this record were applied. This PageID will normally consist of two parts: an objectID (e.g., tablespaceID), and a page number within that object. ARIES can deal with a log record that contains updates for multiple pages. For ease of exposition, we assume that only one page is involved.

UndoNxtLSN. Present only in CLR records. It is the LSN of the next log record of this transaction that is to be processed during rollback. That is, UndoNxtLSN is the value of PrevLSN of the log record that the current log record is compensating. If there are no more log records to be undone, then this field contains a zero.

Data. This is the redo and/or undo data that describes the update that was performed. CLRs contain only redo information since they are never undone. Updates can be logged in a logical fashion. Changes to some fields (e.g., amount of free space) of that page need not be logged since they can be easily derived. The undo information and the redo information for the entire object need not be logged. It suffices if the changed fields alone are logged. For increment or decrement types of operations, before and after-images of the field are not needed. Information about the type of operation and the decrement or increment amount is enough. The information here would also be used to determine the appropriate action routine to be used to perform the redo and/or undo of this log record.
