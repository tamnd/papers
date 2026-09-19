---
paper: denning-1968-workingset
title: The Working Set Model for Program Behavior
authors:
  - Peter J. Denning
year: 1968
venue: Communications of the ACM
field: systems
section: "2"
section_title: Background
tag: 036C
kind: section
lang: en
source: https://doi.org/10.1145/800001.811670
pdf_sha256: 3585991156b07c7e878ea9dff16ef7721401adff09ee328f5ee247b016289e0f
pdf_pages: 2-4
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: d4a409c31b930dd918c113fbf85fc57b5554376f48e9f36401b0786b80f739ce
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

We assume that the reader is already familiar with the concepts of a computer utility [3–5], of segmentation and paging [1, 6], and of program and addressing structure [1, 7–9]; so we only mention these topics here. Briefly, each process has access to its own private, segmented name space; each segment known to the process is sliced into equal-size units, called pages, to facilitate mapping it into the paged main memory. Associated with each segment is a page table, whose entries point to the segment’s pages. An “in-core” bit in each page table entry is turned ON whenever the designated page is present in main memory²; an attempt to reference a page whose “in-core” bit is OFF causes a page fault, initiating proceedings to secure the missing page. A process has three states of existence: running, when a processor is assigned to it; ready, when it would be running if only a processor were available; or blocked, when it has no need of a processor (for example, during a page fault or during a console interaction). When talking about processes in execution, we will have to distinguish between “process-time” and “real-time.” Process-time is time as seen by a process unaware of suspensions; that is, as if it executed without interruptions.

We restrict attention to a two-level memory system, indicated by Figure 1. Only data residing in main memory is accessible to a processor; all other data resides in auxiliary memory, which we regard as having infinite capacity. There is a time $T$, the traverse time, involved in transferring a page between memories, which is measured from the moment a page fault occurs until the moment the missing page is in main memory ready for use. $T$ is actually the expectation of a random variable composed of waits in queues and mechanical positioning delays. Though it usually takes less time to store into auxiliary memory than to read from it, we shall regard the traverse time $T$ to be the same regardless of which direction a page is moved.

A basic allocation problem, “core memory management,” is that of deciding just which pages are to occupy main memory. The fundamental strategy advocated here—a compromise against a lot of expensive main memory—is to minimize *page traffic*³. There are at least three reasons for this:

(1) The more data traffic between the two levels of memory, the more the computational overhead will be deciding just what to move and where to move it.

(2) Because the traverse time $T$ is long compared to a memory cycle, too much data movement can result in congestion on the channel bridging the two memory levels.

(3) Too much data traffic can result in serious interference with processor efficiency on account of auxiliary memory devices “stealing” memory cycles.

Roughly speaking, a working set of pages is the minimum collection of pages that must be loaded in main memory for a process to operate efficiently, without “unnecessary” page faults. According to our definitions, a “process” and its “working set” are but two manifestations of the same ongoing computational activity.

Previous Work. In this section we review strategies that have been set forth in the past for memory management; the interested reader is referred to the literature for detail.

² Consistent with current usage, we will use the terms “core memory” and “main memory” interchangeably.
³ Since data is stored and transmitted by pages, we can (without ambiguity) refer to data movement between memories as “page traffic.”

Figure.

Fig. 1. Two-level memory system {#denning-1968-workingset-fig-1 .figure tag=036D}

We regard management of paged memories as operating in two stages:

(1) Paging-in: locate the required page in auxiliary memory, load it into main memory, turn the "in-core" bit of the appropriate page table entry ON.

(2) Paging-out: remove some page from main memory, turn the "in-core" bit of the appropriate page table entry OFF.

Management algorithms can be classified according to their methods of paging-in and paging-out. Nearly every strategy pages in on demand; that is, no action is taken to load a page into memory until some process attempts to reference it. There have been few proposals to date recommending look-ahead, or anticipatory page-loading, because (as we have stressed) there is no reliable advance source of allocation information, be it the programmer or the compiler. Although the working set is the desired information, it might still be futile to preload pages: there is no guarantee that a process will not block shortly after resumption, having referenced only a fraction of its working set. The operating system could devote its already precious time to activities more rewarding than loading pages which may not be used. Thus we will assume that paging-in is done on demand only, via the page fault mechanism.

The chief problem in memory management is not to decide which pages to load, but which pages to remove. For, if the page with the least likelihood of being reused in the immediate future is retired to auxiliary memory, the best choice has been made. Nearly every worker in the field has recognized this. Debate has arisen over which strategy to employ for retiring pages; that is, which page-turning or replacement algorithm to use.

A good measure of performance for a paging policy is page traffic (the number of pages per unit time being moved between memories) because erroneously removed pages add to the traffic of returning pages. In the following we use this as a basis of comparison for several strategies.

Random Selection. Whenever a fresh page of memory is needed, a page to be replaced is selected at random. Although utterly simple to implement, this method frequently removes useful pages (which must be recalled), and results therefore in high page traffic.

FIFO (First-In/First-Out) Selection. Whenever a fresh page of memory is needed, the page least recently paged in is retired and another page is brought in to fill the now vacant slot. Implementation is simple. The pages of main memory are ordered in a cyclic list; suppose the $M$ pages of memory are numbered $0, 1, \ldots, (M-1)$ and a pointer $k$ indicates that the $k$th page was most recently paged in. When a fresh page of memory is needed, $[ (k+1) \mod M ] \rightarrow k$, and page $k$ is retired. This method is based on the assumption that programs tend to follow sequences of instructions, so that references in the immediate future will most likely be close to present references. So the page which has been in memory longest is least likely to be reused: hence the cyclic list. We see two ways in which this algorithm can fail. First, we question its basic assumption. It is not at all clear that modular programs, which execute numerous intermodule calls, will indeed exhibit sequential instruction fetch patterns. The thread of control will not string pages together linearly; rather, it will entwine them intricately. Fine et al. [10] and Varian and Coffman [11] have experimental evidence to support this, namely, that references will be scattered over a large collection of pages. Second, this algorithm is subject to overloading when used in multiprogrammed memories. When core demand is too heavy, one cycle of the list completes rapidly and the pages deleted are still needed by their processes. This can create a self-intensifying crisis. Programs, deprived of still-needed pages, generate a plethora of page faults; the resulting traffic of returning pages displaces still other useful pages, leading to more page faults, and so on.

Least Recently Used (LRU) Selection. Each page-table entry contains a "use" bit, set to ON each time the page is referenced. At periodic intervals all page-table entries are searched and usage records updated. When a fresh page of memory is needed, the page unreferenced for the longest time is removed. One can see that this method is intrinsically reasonable by considering the simple case of a computer where there is exactly one process whose pages cannot all fit into main memory. In this case a very reasonable choice for a page to replace is the least recently used page. Unfortunately, this method is also susceptible to overloading when many processes compete for main memory.

ATLAS Loop Detection Method. The Ferranti ATLAS computer [12] had proposed a page-turning policy that attempted to detect loop behavior in page reference patterns and then to minimize page traffic by maximizing the time between page transfers, that is, by removing pages not expected to be needed for the longest time. It was only successful for looping programs. Performance was unimpressive for programs exhibiting random reference patterns. Implementation was costly.

Various studies concerning behavior of paging algorithms have appeared. Fine et al. [10] have investigated the effects of demand paging and have seriously questioned whether paging is worthwhile at all. We cannot agree more with their data, nor agree less with their conclusion. Their experiments, as well as those of Varian and Coffman [11], confirm that should there not be enough core memory to contain most of a program, considerable paging activity will interfere with efficiency. The remedy is not to dismiss paging; it is to provide enough core memory! Put another way, there should be enough core memory to contain a program's working set. Paging is no substitute for real core.

Belady [13] has compared some of the algorithms mathematically. His most important conclusion is that the "ideal" algorithm should possess much of the simplicity of Random or FIFO selection (for efficiency) and some, though not much, accumulation of data on past reference patterns. He has shown that too much "historical" data can have adverse effects (witness ATLAS).

In Section 3 we begin investigation of the working set concept. Even though the ideas are not entirely new [9, 14, 15], there has been no detailed documentation publicly available.
