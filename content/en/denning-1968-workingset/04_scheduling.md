---
paper: denning-1968-workingset
title: The Working Set Model for Program Behavior
authors:
  - Peter J. Denning
year: 1968
venue: Communications of the ACM
field: systems
section: "4"
section_title: Scheduling
tag: "0606"
kind: section
lang: en
source: https://doi.org/10.1145/800001.811670
pdf_sha256: 3585991156b07c7e878ea9dff16ef7721401adff09ee328f5ee247b016289e0f
pdf_pages: 7-8
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 42c739a5b526a31c8d3454a21aea12802a136ab855f21576b5e7f72abe8422a7
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The previous discussion has indicated a skeleton for implementing memory management using working sets. Now we fill in the flesh.

If the working set ideas are to contribute to good service, an implementation should at least have these properties:
(1) Since there is such an intimate relation between a process and its working set, memory management and process scheduling must be closely related activities. One cannot take place independently of the other.
(2) Efficiency should be of prime importance. When sampling of page tables is done, it should be only on pages in currently changing working sets, and it should be done as infrequently as possible.
(3) The mechanism ought to be capable of providing measurements of current working set sizes and processor time consumptions for each process.

Figure 7 displays an implementation having these properties. Each solid box represents a delay. The solid arrows indicate the paths that may be followed by a process identifier while it traverses the network of queues. The dashed boxes and arrows show when operations are to be performed on the time-used variable $t_i$ associated with process $i$; processor time used by process $i$ since it was last blocked (page faults excluded) is recorded in $t_i$. Let us trace a single process through this system:
(1) When process $i$ is created, an identifier for it is placed in the ready list, which lists all the processes in the ready state. Processes are selected from the ready list according to the prevailing priority rule.
(2) Once selected from the ready list, process $i$ is assigned a quantum $q_i$, which upper-bounds its time in the running list. This list is a cyclic queue; process $i$ cycles through repeatedly, receiving bursts $\sigma$ of processor time until it blocks or exceeds its quantum $q_i$. Note that the processor burst $\sigma$ is also the sampling interval.
(3) If process $i$ blocks, its identifier is placed in the blocked list, where it remains until the process unblocks; it is then re-entered in the ready list.

Perennially present in the running list is a special process, the checker. The checker performs core management functions. It samples the page tables of each process that has received service since the last time it (the checker) was run, removing pages according to the algorithm discussed at eqs. (15) and (16). It should be clear that if the length of the running list is $l$ and there are $N$ processors, sampling of page tables occurs about every $l \sigma / N$ seconds, not every $\sigma$ seconds.

Associated with process $i$ is a counter $w_i$ giving the current size of its working set. Each time a page fault occurs a new page enters $W_i(t, \tau)$, and so $w_i$ must be increased by one. Each time a page is removed from $W_i(t, \tau)$ by the checker, $w_i$ must be decreased by one.

Having completed its management duties, the checker replenishes vacancies in the running list by selecting jobs from the ready list according to the prevailing priority rule. This is discussed in more detail below.
