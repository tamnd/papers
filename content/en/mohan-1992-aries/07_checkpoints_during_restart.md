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
section: "7"
section_title: CHECKPOINTS DURING RESTART
tag: 073F
kind: section
lang: en
source: https://people.eecs.berkeley.edu/~brewer/cs262/Aries2.pdf
pdf_sha256: 1007fcedb6b8b465f97ee1c4e4d88420450b50b18ff5ad400a130b21e4961817
pdf_pages: "19"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 0a03aa779272ece1db43e67ca6742dc126e55496dd13e7855043238388f5694e
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

In this section, we describe how the impact of failures on CPU processing and I/O can be reduced by, optionally, taking checkpoints during different stages of restart recovery processing.

Analysis pass. By taking a checkpoint at the end of the analysis pass, we can save some work if a failure were to occur during recovery. The entries of the transaction table of this checkpoint will be the same as the entries of the transaction table at the end of the analysis pass. The entries of the dirty-pages list of this checkpoint will be the same as the entries that the restart dirty-pages table contains at the end of the analysis pass. This is different from what happens during a normal checkpoint. For the latter, the dirty-pages list is obtained from the buffer pool (BP) dirty-pages table.

Redo pass. At the beginning of the redo pass, the buffer manager (BM) is notified so that, whenever it writes out a modified page to nonvolatile storage during the redo pass, it will change the restart dirty-pages table entry for that page by making the RecLSN be equal to the LSN of that log record such that all log records up to that log record had been processed. It is enough if BM manipulates the restart dirty-pages table in this fashion. BM does not have to maintain its own dirty-pages table as it does during normal processing. Of course, it should still be keeping track of what pages are currently in the buffers. The above allow checkpoints to be taken any time during the redo pass to reduce the amount of the log that would need to be redone if a failure were to occur before the end of the redo pass. The entries of the restart dirty-pages table at the time of the checkpoint. The entries of the transaction table of this checkpoint will be the same as the entries of the transaction table at the end of the analysis pass. This checkpointing is not affected by whether or not parallelism is employed in the redo pass.

Undo pass. At the beginning of the undo pass, the restart dirty-pages table becomes the BP dirty-pages table. At this point, the table is cleaned up by removing those entries for which the corresponding pages are no longer in the buffers. From then onward, the BP manager manipulates this table as it does during normal processing—removing entries when pages are written to nonvolatile storage, adding entries when pages are about to become dirty, etc. During the undo pass, the entries of the transaction table are modified as during normal undo. If a checkpoint is taken any time during the undo pass, then the entries of the dirty-pages list of that checkpoint are the same as the entries of the BP dirty-pages table at the time of the checkpoint. The entries of the transaction table of this checkpoint will be the same as the entries of the transaction table at that time.

In System R, during restart recovery, sometimes it may be required that a checkpoint be taken to free up some physical pages (the shadow pages) for more undo or redo work to be performed. This is another consequence of the fact that history cannot be repeated in System R. This complicates the restart logic since the view depicted in Figure 17 would no longer be true after a restart checkpoint completes. The restart checkpoint logic and its effect on a restart following a system failure during an earlier restart were considered too complex to be describable in [31]. ARIES is able to easily accommodate date checkpoints during restart. While these checkpoints are optional in our case, they may be forced to take place in System R.
