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
section: "7"
section_title: Tuple Mover
tag: "0764"
kind: section
lang: en
source: https://www.vldb.org/archives/website/2005/program/paper/thu/p553-stonebraker.pdf
pdf_sha256: c619eacc696c847e0d7697edb9193a2c35f242b12ac2835f486970a07129eecb
pdf_pages: 8-9
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 95aa6d1459c2271f05e92f6c90fe9b6e3709568fa10c023bafc44320bf573bef
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The job of the tuple mover is to move blocks of tuples in a WS segment to the corresponding RS segment, updating any join indexes in the process. It operates as a background task looking for worthy segment pairs. When it finds one, it performs a merge-out process, MOP on this (RS, WS) segment pair.

MOP will find all records in the chosen WS segment with an insertion time at or before the LWM, and then divides them into two groups:
• Ones deleted at or before LWM. These are discarded, because the user cannot run queries as of a time when they existed.
• Ones that were not deleted, or deleted after LWM. These are moved to RS.
MOP will create a new RS segment that we name RS'. Then, it reads in blocks from columns of the RS segment, deletes any RS items with a value in the DRV less than or equal to the LWM, and merges in column values from WS. The merged data is then written out to the new RS' segment, which grows as the merge progresses. The most recent insertion time of a record in RS’ becomes the segment’s new t_lastmove and is always less than or equal to the LWM. This old-master/new-master approach will be more efficient than an update-in-place strategy, since essentially all data objects will move. Also, notice that records receive new storage keys in RS', thereby requiring join index maintenance. Since RS items may also be deleted, maintenance of the DRV is also mandatory. Once RS' contains all the WS data and join indexes are modified on RS', the system cuts over from RS to RS'. The disk space used by the old RS can now be freed.

Periodically the timestamp authority sends out to each site a new LWM epoch number. Hence, LWM “chases” HWM, and the delta between them is chosen to mediate between the needs of users who want historical access and the WS space constraints.
