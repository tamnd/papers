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
section: "4"
section_title: DATA STRUCTURES
tag: 072B
kind: section
lang: en
source: https://people.eecs.berkeley.edu/~brewer/cs262/Aries2.pdf
pdf_sha256: 1007fcedb6b8b465f97ee1c4e4d88420450b50b18ff5ad400a130b21e4961817
pdf_pages: 10-11
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 0d71fba27e9bd837accdcf7653f5ffe9c4634bcba70b9e0eab10024713011cbf
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

This section describes the major data structures that are used by ARIES.

### 4.1 Log Records {#mohan-1992-aries-s4-1 .section tag=072C}

Below, we describe the important fields that may be present in different types of log records.

### 4.2 Page Structure {#mohan-1992-aries-s4-2 .section tag=072D}

One of the fields in every page of the database is the page_LSN field. It contains the LSN of the log record that describes the latest update to the page. This record may be a regular update record or a CLR. ARIES expects the buffer manager to enforce the WAL protocol. Except for this, ARIES does not place any restrictions on the buffer page replacement policy. The steal buffer management policy may be used. In-place updating is performed on nonvolatile storage. Updates are applied immediately and directly to the

### 4.3 Transaction Table {#mohan-1992-aries-s4-3 .section tag=072E}

A table called the transaction table is used during restart recovery to track the state of active transactions. The table is initialized during the analysis pass from the most recent checkpoint’s record(s) and is modified during the analysis of the log records written after the beginning of that checkpoint.

During the undo pass, the entries of the table are also modified. If a checkpoint is taken during restart recovery, then the contents of the table will be included in the checkpoint record(s). The same table is also used during normal processing by the transaction manager. A description of the important fields of the transaction table follows:

TransID. Transaction ID.

State. Commit state of the transaction: prepared (‘P’—also called in-doubt) or unprepared (‘U’).

LastLSN. The LSN of the latest log record written by the transaction.

UndoNxtLSN. The LSN of the next record to be processed during rollback. If the most recent log record written or seen for this transaction is an undoable non-CLR log record, then this field’s value will be set to LastLSN. If that most recent log record is a CLR, then this field’s value is set to the UndoNxtLSN value from that CLR.

### 4.4 Dirty–Pages Table {#mohan-1992-aries-s4-4 .section tag=072F}

A table called the dirty-pages table is used to represent information about dirty buffer pages during normal processing. This table is also used during restart recovery. The actual implementation of this table may be done using hashing or via the deferred-writes queue mechanism of [96]. Each entry in the table consists of two fields: PageID and RecLSN (recovery LSN). During normal processing, when a nondirty page is being fixed in the buffers with the intention to modify, the buffer manager records in the buffer pool (BP) dirty-pages table, as RecLSN, the current end-of-log LSN, which will be the LSN of the next log record to be written. The value of RecLSN indicates from what point in the log there may be updates which are, possibly, not yet in the nonvolatile storage version of the page. Whenever pages are written back to nonvolatile storage, the corresponding entries in the BP dirty-pages table are removed. The contents of this table are included in the checkpoint record(s) that is written during normal processing. The restart dirty-pages table is initialized from the latest checkpoint’s record(s) and is modified during the analysis of the other records during the analysis pass. The minimum RecLSN value in the table gives the starting point for the redo buffer version of the page containing the object. That is, no deferred updating as in INGRES [86] is performed. If it is found desirable, deferred updating and, consequently, deferred logging can be implemented. ARIES is flexible enough not to preclude those policies from being implemented.
