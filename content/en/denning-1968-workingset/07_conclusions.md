---
paper: denning-1968-workingset
title: The Working Set Model for Program Behavior
authors:
  - Peter J. Denning
year: 1968
venue: Communications of the ACM
field: systems
section: "7"
section_title: Conclusions
tag: 060B
kind: section
lang: en
source: https://doi.org/10.1145/800001.811670
pdf_sha256: 3585991156b07c7e878ea9dff16ef7721401adff09ee328f5ee247b016289e0f
pdf_pages: 10-11
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: f4b095249c7d5ffc29e3642d346bc5aaaf6f6feab78f3b5bc9499b6a087dfaea
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Starting from the observation that "process" and "working set" are two manifestations of a computation, we have shown that it is possible to define precise notions of "processor demand," of "memory demand," and of "system demand." Resource allocation is then the problem of "balancing" memory and processor demands against equipment. A "balance policy" strives to maintain balance by judiciously selecting jobs to run. The notions "demand" and "balance" can play important roles in understanding the complex interactions among computer system components. It is quite clear that even with these intuitively simple notions, interactions are exceedingly complex.

In order to arrive at notions of memory demand, we had to define a model for program behavior. The working set model affords a convenient way to determine which information is in use by a computation and which is not; it enables simple determination of memory demands.

It is interesting that Oppenheimer and Weizer [17] have used notions related to "working set" and "memory balance" in their simulations of the RCA Spectra 70/46 Time-Sharing Operating System; their evidence indicates that system performance can be improved markedly through these techniques.

Regarding this paper from a slightly different point of view, we have seen four major contenders for page-turning policies for use in memory management: random, first-in/first-out (FIFO), least recently used (LRU), and working set. Each of these policies pages in on demand, believing that paging out is the heart of the problem, for if pages least likely to be reused in the near future are removed from main memory, the traffic of returning pages is minimized. Random brings on the highest page traffic, working set the lowest. Although Random and FIFO are the easiest to implement, the added cost of working set is more than offset by its accuracy and compatibility with generalized allocation strategies.

Acknowledgment. I thank Jack B. Dennis and Donald R. Slutz for many helpful criticisms.

APPENDIX. Hardware Implementation of Memory Management

Just as hardware is used to streamline the address-mapping mechanism, so hardware can be used to streamline memory management. The hardware described here associates a timer with each physical page of main storage to measure multiples of the working set parameter $\tau$.

Each process, upon creation, is assigned an identification number, $i$, which is used to index the process table. The $i$th entry in the process table contains information about the $i$th process, including its current demand $(p_i, m_i)$. Because this demand information is stored in a commonplace, the memory hardware can update the memory demand $m_i$ without calling the supervisor. Whenever a page fault occurs, the new page is located in auxiliary memory and transferred to main memory; then a signal is sent to the management hardware to free a page of main memory in readiness for the next page fault. The hardware selects a page not in any working set and dispatches it directly to auxiliary memory, without troubling the supervisor. This hardware modifies the page table entry pointing to the newly deleted page, turning the “in-core” bit OFF, and leaving a pointer to help locate the page in auxiliary memory.

Figure A indicates that with each page of memory there is associated a page register, having three fields:

(1) $\pi$-field. $\pi$ is a pointer to the memory location of the page table entry pointing to this page. A page table cannot be moved or removed without modifying $\pi$.

(2) $t$-field. $t$ is a timer to measure off the interval $\tau$. The value to be used for $\tau$ is found in the $t$-register. The supervisor modifies the contents of the $t$-register as discussed below.

(3) $A$-field. $A$ is an “alarm” bit, set to 1 if the timer $t$ runs out. Operation proceeds as follows:

(1) When a page is loaded into main memory, $\pi$ is set to point to the memory location of the correct page table entry. The “in-core” bit of that entry is turned ON.

(2) Each time a reference to some location within a page occurs, its page register is modified: $\tau \rightarrow t$ and $0 \rightarrow A$. The timer $t$ begins to run down (in real-time), taking $\tau$ seconds to do so.

(3) If $t$ runs down, $1 \rightarrow A$. Whenever a fresh page of memory is needed, the supervisor sends a signal to additional memory hardware (not shown) which scans pages looking for a page with $A = 1$. Such a page is dispatched directly to auxiliary memory. $\pi$ is used to find the page table entry, turn the “in-core” bit OFF, and leave information there to permit future retrieval of the page from auxiliary memory. Note that a page need not be removed when $A = 1$; it is only subject to removal. This means a page may leave and later reenter a working set without actually leaving main memory.

The timers $t$ are running down in real time. The value in

Figure.

Fig. A. Memory management hardware

the $t$-register must be modifiable by the supervisor for the following reason. As in Figure 7, the running list is cyclic, except now we suppose that each process is given a burst $\beta$ of processor time ($\beta$ need not be related to the sampling interval $\sigma$), and continues to receive bursts $\beta$ until its running-list quantum is exhausted. If on a particular cycle there are $n$ entries in the list and $N$ processors in service, a given process will be unable to reference any of its pages for about $n\beta/N$ seconds, the time to complete a cycle through the queue. That is, one unit of process time elapses for a program about each $n$ units of real-time. So the supervisor should be able to set the contents of the $t$-register to some multiple of $n\tau$, for otherwise management hardware will begin removing pages of working sets of running processes. However the $t$-register contents should never be less than some multiple of the traverse time $T$, for otherwise when a process interrupts for a page fault its working set may disappear from core memory.
