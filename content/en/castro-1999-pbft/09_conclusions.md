---
paper: castro-1999-pbft
title: Practical Byzantine Fault Tolerance
authors:
  - Miguel Castro
  - Barbara Liskov
year: 1999
venue: OSDI
field: security
section: "9"
section_title: Conclusions
tag: "0838"
kind: section
lang: en
source: https://www.scs.stanford.edu/nyu/03sp/sched/bfs.pdf
pdf_sha256: 9b8d5842c967894eaa2d6aa71d4354d26c4f76880f859a117d96042b4a37efc1
pdf_pages: 13-14
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 222f1c18754260d5adba8fcb90741fb1eda1b005bc0c7987f4ba372be086dc64
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

This paper has described a new state-machine replication algorithm that is able to tolerate Byzantine faults and can be used in practice: it is the first to work correctly in an asynchronous system like the Internet and it improves the performance of previous algorithms by more than an order of magnitude.

The paper also described BFS, a Byzantine-fault-tolerant implementation of NFS. BFS demonstrates that it is possible to use our algorithm to implement real services with performance close to that of an unreplicated service — the performance of BFS is only 3% worse than that of the standard NFS implementation in Digital Unix. This good performance is due to a number of important optimizations, including replacing public-key signatures by vectors of message authentication codes, reducing the size and number of messages, and the incremental checkpoint-management techniques.

One reason why Byzantine-fault-tolerant algorithms will be important in the future is that they can allow systems to continue to work correctly even when there are software errors. Not all errors are survivable; our approach cannot mask a software error that occurs at all replicas. However, it can mask errors that occur independently at different replicas, including nondeterministic software errors, which are the most problematic and persistent errors since they are the hardest to detect. In fact, we encountered such a software bug while running our system, and our algorithm was able to continue running correctly in spite of it.

There is still much work to do on improving our system. One problem of special interest is reducing the amount of resources required to implement our algorithm. The number of replicas can be reduced by using $f$ replicas as witnesses that are involved in the protocol only when some full replica fails. We also believe that it is possible to reduce the number of copies of the state to $f + 1$ but the details remain to be worked out.
