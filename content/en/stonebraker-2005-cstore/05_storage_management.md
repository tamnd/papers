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
section: "5"
section_title: Storage Management
tag: 075A
kind: section
lang: en
source: https://www.vldb.org/archives/website/2005/program/paper/thu/p553-stonebraker.pdf
pdf_sha256: c619eacc696c847e0d7697edb9193a2c35f242b12ac2835f486970a07129eecb
pdf_pages: "6"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: dae4486147e54546462d4d49b813795114ffb1bd9aea4569be7ad61335be9165
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The storage management issue is the allocation of segments to nodes in a grid system; C-Store will perform this operation automatically using a storage allocator. It seems clear that all columns in a single segment of a projection should be co-located. As noted above, join indexes should be co-located with their “sender” segments. Also, each WS segment will be co-located with the RS segments that contain the same key range.

Using these constraints, we are working on an allocator. This system will perform initial allocation, as well as reallocation when load becomes unbalanced. The details of this software are beyond the scope of this paper.

Since everything is a column, storage is simply the persistence of a collection of columns. Our analysis shows that a raw device offers little benefit relative to today’s file systems. Hence, big columns (megabytes) are stored in individual files in the underlying operating system.
