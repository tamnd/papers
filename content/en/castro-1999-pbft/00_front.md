---
paper: castro-1999-pbft
title: Practical Byzantine Fault Tolerance
authors:
  - Miguel Castro
  - Barbara Liskov
year: 1999
venue: OSDI
field: security
section_title: Front Matter
tag: 019D
kind: front
lang: en
source: https://www.scs.stanford.edu/nyu/03sp/sched/bfs.pdf
pdf_sha256: 9b8d5842c967894eaa2d6aa71d4354d26c4f76880f859a117d96042b4a37efc1
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 6342591740b79386396c751cc48239551c44b7a86b764be571d5ac387a959e02
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Appears in the Proceedings of the Third Symposium on Operating Systems Design and Implementation, New Orleans, USA, February 1999

Practical Byzantine Fault Tolerance

Miguel Castro and Barbara Liskov
Laboratory for Computer Science,
Massachusetts Institute of Technology,
545 Technology Square, Cambridge, MA 02139
{castro,liskov}@lcs.mit.edu

Abstract

This paper describes a new replication algorithm that is able to tolerate Byzantine faults. We believe that Byzantine-fault-tolerant algorithms will be increasingly important in the future because malicious attacks and software errors are increasingly common and can cause faulty nodes to exhibit arbitrary behavior. Whereas previous algorithms assumed a synchronous system or were too slow to be used in practice, the algorithm described in this paper is practical: it works in asynchronous environments like the Internet and incorporates several important optimizations that improve the response time of previous algorithms by more than an order of magnitude. We implemented a Byzantine-fault-tolerant NFS service using our algorithm and measured its performance. The results show that our service is only 3% slower than a standard unreplicated NFS.
