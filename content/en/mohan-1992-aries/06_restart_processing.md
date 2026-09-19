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
section: "6"
section_title: RESTART PROCESSING
tag: "0736"
kind: section
lang: en
source: https://people.eecs.berkeley.edu/~brewer/cs262/Aries2.pdf
pdf_sha256: 1007fcedb6b8b465f97ee1c4e4d88420450b50b18ff5ad400a130b21e4961817
pdf_pages: 15-19
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: fbe29b36e05b9cc6a43752872ba07da637f05a88927ad235d0e4a022004d65fb
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

When the transaction system restarts after a failure, recovery needs to be performed to bring the data to a consistent state and ensure the atomicity and durability properties of transactions. Figure 9 describes the RESTART routine that gets invoked at the beginning of the restart of a failed system. The input to this routine is the LSN of the master record which contains the pointer to the begin_chkpt record of the last complete checkpoint taken before site failure or shutdown. This routine invokes the routines for the analysis pass, the redo pass and the undo pass, in that order. The buffer pool dirty-pages table is updated appropriately. At the end of restart recovery, a checkpoint is taken.

For high availability, the duration of restart processing must be as short as possible. One way of accomplishing this is by exploiting parallelism during the redo and undo passes. Only if parallelism is going to be employed is it necessary to latch pages before they are modified during restart recovery. Ideas for improving data availability by allowing new transaction processing during recovery are explored in [60].

### 6.1 Analysis Pass {#mohan-1992-aries-s6-1 .section tag=0737}

The first pass of the log that is made during restart recovery is the analysis pass. Figure 10 describes the RESTART_ANALYSIS routine that implements the analysis pass actions. The input to this routine is the LSN of the master record. The outputs of this routine are the transaction table, which contains the list of transactions which were in the in-doubt or unprepared state at the time of system failure or shutdown; the dirty-pages table, which contains the list of pages that were potentially dirty in the buffers when the system failed or was shut down; and, the RedoLSN, which is the location on the log from which the redo pass must start processing the log. The only log records that may be written by this routine are end records for transactions that had totally rolled back before system failure, but for whom end records are missing.

During this pass, if a log record is encountered for a page whose identity does not already appear in the dirty-pages table, then an entry is made in the table with the current log record's LSN as the page's RecLSN. The transaction table is modified to track the state changes of transactions and also to note the LSN of the most recent log record that would need to be undone if it were determined ultimately that the transaction had to be rolled back. If an OSfile_return log record is encountered, then any pages belonging to that file which are in the dirty-pages table are removed from the latter in order to make sure that no page belonging to that version of that file is accessed during the redo pass. The same file may be recreated and updated later, once the original operation causing the file erasure is committed. In that case, some pages of the recreated file will reappear in the dirty-pages table later with RecLSN values greater than the end_of_log LSN when the file was erased. The RedoLSN is the minimum RecLSN from the dirty-pages table at the end of the analysis pass. The redo pass can be skipped if there are no pages in the dirty-pages table.

It is not necessary that there be a separate analysis pass and, in fact, in the ARIES implementation in the OS/2 Extended Edition Database Manager there is no analysis pass. This is especially because, as we mentioned before (see also Section 6.2), in the redo pass, ARIES unconditionally redoes all missing updates. That is, it redoes them irrespective of whether they were logged by loser or nonloser transactions, unlike System R, SQL/DS and DB2.

Hence, redo does not need to know the loser or nonloser status of a transaction. That information is, strictly speaking, needed only for the undo pass. This would not be true for a system (like DB2) in which for in-doubt transactions their update locks are reacquired by inferring the lock names from the log records of the in-doubt transactions, as they are encountered during the redo pass. This technique for reacquiring locks forces the RedoLSN computation to consider the Begin_LSNs of in-doubt transactions which in turn requires that we know, before the start of the redo pass, the identities of the in-doubt transactions.

Without the analysis pass, the transaction table could be constructed from the checkpoint record and the log records encountered during the redo pass. The RedoLSN would have to be the minimum(minimum(RecLSN from the dirty-pages table in the end_chkpt record), LSN(begin_chkpt record)). Suppression of the analysis pass would also require that other methods be used to

```text
RESTART(Master_Addr);
Restart_Analysis(Master_Addr,Trans_Table,Dirty_Pages,RedoLSN);
Restart_Redo(RedoLSN,Trans_Table,Dirty_Pages);
buffer_pool_Dirty_Pages_table := Dirty_Pages;
remove entries for non-buffer-resident pages from the buffer pool Dirty_Pages table;
Restart_Undo(Trans_Table);
reacquire locks for prepared transactions;
RETURN;
```

Fig. 9. Pseudocode for restart. {#mohan-1992-aries-fig-9 .figure tag=0738}

```text
RESTART_REDO(RedoLSN, Dirty_Pages);
    initialize the tables Trans_Table and Dirty_Pages to empty;
    Master_Rec := Read_Disk(Master_Addr);
    Open_Log_Scan(Master_Rec.ChkptLSN);
        /* open log scan at Begin_Chkpt record */
        LogRec := Next_Log();
        /* read log record following Begin_Chkpt */
        WHILE NOT(End_of_Log) DO;
            IF trans_related record & LogRec.TransID IN Trans_Table THEN /* not chkpt/OSfile return*/
                insert (LogRec.TransID,'U',LogRec.LSN,LogRec.PrevLSN) INTO Trans_Table; /* log record */
            ELSE Trans_Table[LogRec.TransID].LastLSN := LogRec.LSN;
                IF LogRec.Type = 'update' THEN
                    IF LogRec.is undoable THEN Trans_Table[LogRec.TransID].UndoNxtLSN := LogRec.LSN;
                    ELSE Trans_Table[LogRec.TransID].UndoNxtLSN := LogRec.UndoNxtLSN;
                        /* next record to undo is the one pointed to by this CLR */
                        WHEN('Begin_Chkpt') ; /* found an incomplete checkpoint's Begin_Chkpt record. ignore it */
                            END;
                            LogRec := Next_Log();
                            RETURN;
                        WHEN('End_Chkpt') DO;
                            FOR each entry in LogRec.Trans_Table DO;
                                IF TransID NOT IN Trans_Table THEN DO;
                                    insert entry(TransID,State,LastLSN,UndoNxtLSN) in Trans_Table;
                                END;
                            END; /* FOR */
                            FOR each entry in LogRec.Dirty_PageList DO;
                                IF PageID NOT IN Dirty_Pages THEN insert entry(PageID,RecLSN) in Dirty_Pages;
                            ELSE set RecLSN of Dirty_Pages entry to RecLSN in Dirty_PageList;
                            END; /* FOR */
                            END; /* WHEN('End Chkpt') */
                            WHEN('prepare','rollback') DO;
                                IF LogRec.Type = 'prepare' THEN Trans_Table[LogRec.TransID].State := 'P';
                                ELSE Trans_Table[LogRec.TransID].LastLSN := LogRec.LSN;
                            END; /* WHEN('prepare','rollback') */
                            WHEN('end') delete Trans_Table entry for which TransID = LogRec.TransID;
                            WHEN('osfile return') delete from Dirty_Pages all pages of returned file;
                            END; /* SELECT */
                            LogRec := Next_Log();
                            END; /* WHILE */
                            FOR EACH Trans_Table entry with (State = 'U') & (UndoNxtLSN = 0) DO; /* rolled back trans */
                                /* with missing end record */
                            END; /* FOR */
                            RecLSN := minimum(Dirty_Pages.RecLSN);
                            RE-URN;
```

END; /* FOR */

Fig. 10. Pseudocode for restart analysis. {#mohan-1992-aries-fig-10 .figure tag=0739}

avoid processing updates to files which have been returned to the operating system. Another consequence is that the dirty-pages table used during the redo pass cannot be used to filter update log records which occur after the begin-chkpt record.

### 6.2 Redo Pass {#mohan-1992-aries-s6-2 .section tag=073A}

The second pass of the log that is made during restart recovery is the redo pass. Figure 11 describes the RESTART_REDO routine that implements some of that redo of loser transactions’ log records may be unnecessary. In [69] we have explored further the idea of restricting the repeating of history to possibly reduce the number of pages which get dirtied during this pass.

Since redo is page-oriented, only the pages with entries in the dirty-pages table may get modified during the redo pass. Only the pages listed in the dirty-pages table will be read and examined during this pass. Not all the pages that are read may require redo. This is because some of the pages that were dirty at the time of the last checkpoint or which became dirty later might have been written to nonvolatile storage before the system failure.

Because of reasons like reducing log volume and saving some CPU overhead, we do not expect systems to write log records that identify the dirty pages that were written to nonvolatile storage, although that option is available and such log records can be used to eliminate the corresponding pages from the dirty-pages table when those log records are encountered during the analysis pass. Even if such records were always to be written after I/Os complete, a system failure in a narrow window could prevent them from being written. The corresponding pages will not get modified during this pass.

For brevity, we do not discuss here as to how, if a failure were to occur after the logging of the end record of a transaction, but before the execution of all the pending actions of that transaction, the remaining pending actions are redone during the redo pass.

For exploiting parallelism, the availability of the information in the dirty-pages table gives us the possibility of initiating asynchronous I/Os in parallel to read all these pages so that they may be available in the buffers possibly before the corresponding log records are encountered in the redo pass. Since updates performed during the redo pass are not logged, we can also perform sophisticated things like building in-memory queues of log records which potentially need to be reapplied (as dictated by the information in the dirty-pages table) on a per page or group of pages basis and, as the processing the corresponding log record queues using multiple processes. This requires that each queue be dealt with by only one process. Updates to different pages may get applied in different orders from the order represented in the log. This does not violate any correctness properties since for a given page all its missing updates are reapplied in the same order as before. These parallelism ideas are also applicable to the context of supporting disaster recovery via remote backups [73].

### 6.3 Undo Pass {#mohan-1992-aries-s6-3 .section tag=073B}

The third pass of the log that is made during restart recovery is the undo pass. Figure 12 describes the RESTART_UNDO routine that implements the undo pass actions. The input to this routine is the restart transaction table. The dirty-pages table is not consulted during this undo pass. Also, since history is repeated before the undo pass is initiated, the LSN on the page is not consulted to determine whether an undo operation should be performed or not. Contrast this with what we describe in Section 10.1 for systems like DB2 that do not repeat history but perform selective redo.

The restart–undo routine rolls back losers transactions, in reverse chronological order, in a single sweep of the log. This is done by continually taking the maximum of the LSNs of the next log record to be processed for each of the yet-to-be-completely-undone loser transactions, until no loser transaction remains to be undone. The next record to process for each transaction to be rolled back is determined by an entry in the transaction table for each of those transactions. The processing of the encountered log records is exactly as we described before in Section 5.2. In the process of rolling back the page was written to disk after the second update. After that disk write, a partial rollback was performed (undo of log records 4 and 3) and then the transaction went forward (updates 5 and 6). During restart recovery, the missing updates (3, 4, 4', 3', 5 and 6) are first redone and then the undos (of 6, 5, 2 and 1) are performed. Each update log record will be matched with at most one CLR, regardless of how many times restart recovery is performed.

With ARIES, we have the option of allowing the continuation of loser transactions after restart recovery is completed. Since ARIES repeats history and supports the savepoint concept, we could, in the undo pass, roll back each

```text
RESTART_UNDO(Trans_Table);
WHILE EXISTS(Trans_with State = 'U' in Trans_Table) DO;
    WHILE EXISTS(UndoNxtLSN = 'U' in Trans_Table entries with State = 'U');
        UndoLSN := maximum(UndoNxtLSN) from Trans_Table entries with State = 'U';
        LogRec := Log_Read(UndoLSN);
        SELECT(LogRec.Type)
        WHEN('update') DO;
            IF LogRec is undoable THEN DO; /* record needs undoing (not redo-only record) */
                Page := fix&latch(LogRec.PageID, 'X');
                Log_Write('compensation',LogRec.TransID,Trans_Table[LogRec.TransID].LastLSN := LgLSN;
                LogWrite('end',LogRec.TransID,Trans_Table[LogRec.TransID].LastLSN := LgLSN;
                Undo_Update(Page,LogRec);
                LogWrite('compensation',LogRec.TransID,Trans_Table[LogRec.TransID].LastLSN,
                    LogRec.PageID,LogRec.PrevLSN, ...,LgLSN,Data); /* store LSN of CLR in page */
                Page.LSN := LgLSN;
                Trans_Table[LogRec.TransID].LastLSN := LgLSN;
                unfix&unlatch(Page);
                END;
            ELSE;
                IF LogRec.PrevLSN = 0 THEN DO; /* the one preceding this record in its backward chain */
                    Log_Write('end',LogRec.TransID,Trans_Table[LogRec.TransID].LastLSN,...);
                    delete Trans_Table entry where TransID = LogRec.TransID; /* delete trans from table */
                    END; /* SELECT */
                END; /* WHILE */
                RETURN;
            END; /* record cannot be undone - ignore it */
        END; /* pick up addr of next record to examine */
    END; /* pick up addr of next record to examine */
END; /* WHEN('compensation') */
WHEN('rollback'|'prepare') Trans_Table[LogRec.TransID].UndoNxtLSN := LogRec.PrevLSN;
WHEN('compensation') Trans_Table[LogRec.TransID].UndoNxtLSN := LogRec.UndoNxtLSN;
```

/* pick up addr of next record to examine */

Fig. 12. Pseudocode for estart undo. {#mohan-1992-aries-fig-12 .figure tag=073C}

recovery is performed efficiently by rolling forward using the log records in the remembered ranges. Even during normal rollbacks, CLRs may be written for offline objects.

In ARIES also, we can take similar actions, provided none of the loser transactions has modified one or more of the offline objects that may require logical undos. This is because logical undos are based on the current state of the object. Redos are not at all a problem, since they are always page-oriented.

For logical undos involving space management (see Section 10.3), generally we can take a conservative approach and generate the appropriate CLRs. For example, during the undo of an insert record operation, we can write a CLR for the space-related update stating that the page is 0% full. But for the high concurrency, index management methods of [62] this is not possible, since the effect of the logical undo (e.g., retraversing the index tree to do a key deletion), in terms of which page may be affected, is unpredictable; in fact, we cannot even predict when page-oriented undo will not work and hence logical undo is necessary.

It is not possible to handle the undos of some of the records of a transaction during restart recovery and handle the undos (possibly, logical) of the rest of the records at a later point in time, if the two sets of records are interspersed.

Remember that in all the recovery methods, undo of a transaction is done in reverse chronological order. Hence, it is enough to remember, for each transaction, the next record to be processed during the undo; from that record, the PrevLSN and/or the UndoNxtLSN chain leads us to all the other records to be processed.

Even under the circumstances where one or more of the loser transactions have to perform, potentially logical, undos on some offline objects, if deferred restart needs to be supported, then we suggest the following algorithm:

1. Perform the repeating of history for the online objects, as usual; postpone it for the offline objects and remember the log ranges.
2. Proceed with the undo pass as usual, but stop undoing a loser transaction when one of its log records is encountered for which a CLR cannot be generated for the above reasons. Call such a transaction a stopped transaction.
But continue undoing the other, unstopped transactions.
3. For the stopped transactions, acquire locks to protect their updates which have not yet been undone. This could be done as part of the undo pass by continuing to follow the pointers, as usual, even for the stopped transactions and acquiring locks based on the encountered non-CLRs that were written by the stopped transactions.
4. When restart recovery is completed and later the previously offline objects are made online, first repeat history based on the remembered log ranges and then continue with the undoing of the stopped transactions. After each of the stopped transactions is totally rolled back, release its still held locks.
5. Whenever an offline object becomes online, when the repeating of history is completed for that object, new transactions can be allowed to access that object in parallel with the further undoing of all of the stopped transactions that can make progress.

The above requires the ability to generate lock names based on the information in the update (non-CLR) log records. DB2 is doing that already for in-doubt transactions.

Fig. 13. Restart recovery example with ARIES. {#mohan-1992-aries-fig-13 .figure tag=073D}

| REDO | 3 | 4 | 4' | 3' | 5 | 6 | /6' | 5' | 2' | 1' |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| UNDO | 6 | 5 | 2 | 1 |  |  |  |  |  |  |

### 6.4 Selective or Deferred Restart {#mohan-1992-aries-s6-4 .section tag=073E}

Sometimes, after a system failure, we may wish to restart the processing of new transactions as soon as possible. Hence, we may wish to defer doing some recovery work to a later point in time. This is usually done to reduce the amount of time during which some critical data is unavailable. It is accomplished by recovering such data first and then opening the system for the processing of new transactions. In DB2, for example, it is possible to perform restart recovery even when some of the objects for which redo and/or undo work needs to be performed are offline when the system is brought up. If some undo work needs to be performed for some loser transactions on those offline objects, then DB2 is able to write the CLRs alone and finish handling the transactions. This is possible because the CLRs can be generated based solely on the information in the non-CLR records written during the forward processing of the transactions [15]. Because page (or minipage, for indexes) is the smallest granularity of locking, the undo actions will be exact inverses of the original actions. That is, there are no logical undos in DB2. DB2 remembers, in an exceptions table (called the database allocation (DBA) table) that is maintained in the log and in virtual storage, the fact that those offline objects need to be recovered when they are brought online, before they are made accessible to other transactions [14]. The LSN ranges of log records to be applied are also remembered. Unless there are some in-doubt transactions with uncommitted updates to those objects, no locks need to be acquired to protect those objects since accesses to those objects will not be permitted until recovery is completed. When those objects are brought online, then

Even if none of the objects to be recovered is offline, but it is desired that the processing of new transactions start before the rollbacks of the loser transactions are completed, then we can accommodate it by doing the following: (1) first repeat history and reacquire, based on their log records, the locks for the uncommitted updates of the loser and in-doubt transactions, and (2) then start processing new transactions even as the rollbacks of the loser transactions are performed in parallel. The locks acquired in step (1) are released as each loser transaction’s rollback completes. Performing step (1) requires that the restart RedoLSN be adjusted appropriately to ensure that all the log records of the loser transactions are encountered during the redo pass. If a loser transaction was already rolling back at the time of the system failure, then, with the information obtained during the analysis pass for such a transaction, it will be known as to which log records remain to be undone.

These are the log records whose LSNs are less than or equal to the UndoNxtLSN of the transaction’s last CLR. Locks need to be obtained during the redo pass only for those updates that have not yet been undone. If a long transaction is being rolled back and we would like to release some of its locks as soon as possible, then we can mark specially those log records which represent the first update by that transaction on the corresponding object (e.g., record, if record locking is in effect) and then release that object’s lock as soon as the corresponding log record is undone. This works only because we do not undo CLRs and because we do not undo the same non-CLR more than once; hence, it will not work in systems that undo CLRs (e.g., Encompass, AS/400, DB2) or that undo a non-CLR more than once (e.g., IMS). This early release of locks can be performed in ARIES during normal transaction undo to possibly permit resolution of deadlocks using partial rollbacks.
