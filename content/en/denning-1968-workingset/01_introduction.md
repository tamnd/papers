---
paper: denning-1968-workingset
title: The Working Set Model for Program Behavior
authors:
  - Peter J. Denning
year: 1968
venue: Communications of the ACM
field: systems
section: "1"
section_title: Introduction
tag: 036B
kind: section
lang: en
source: https://doi.org/10.1145/800001.811670
pdf_sha256: 3585991156b07c7e878ea9dff16ef7721401adff09ee328f5ee247b016289e0f
pdf_pages: 1-2
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 423417bc9fd61641ecdd3ee9877b3e4ded2846e60bf4fe0decaeac2551b1dcc5
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Resource allocation is a tricky business. Recently there has been much dialog about process scheduling and core memory management, yet development of techniques has progressed independently along both these lines. No one will deny that a unified approach is needed. Here we show that it is possible to develop a unified approach. Starting from the observation that every running program places demands jointly on all system resources, particularly processor and memory, we eventually define "system demand"; the allocation problem will consist of balancing demands against available resources.

We regard a computation as being the fundamental activity in a computer system; in this paper, a computation consists of a single process together with the information available to it. (For a complete discussion of the meaning of "computation," see Dennis and Van Horn [1].) The usual notion "process" is one manifestation of a computation, in the form of a demand for a processor (a "processor demand"). The notion "working set of information" introduced here is another manifestation of a computation, in the form of a demand for memory (a "memory demand"). A computation's "system demand" will consist jointly of its processor and memory demands.

Probably the most basic reason for the absence of a general treatment of resource allocation is the lack of an adequate model for program behavior. In this paper we develop a new model, the working set model, which embodies certain important behavioral properties of computations operating in multiprogrammed environs, enabling us to decide which information is in use by a running program and which is not. We do not intend that the proposed model be considered "final"; rather, we hope to stimulate a new kind of thinking that may be of considerable help in solving many operating system design problems.

The working set is intended to model the behavior of programs in the general purpose computer system, or computer utility. For this reason we assume that the operating system must determine on its own the behavior of programs it runs; it cannot count on outside help. Two commonly proposed sources of externally supplied allocation information are the user and the compiler. We claim neither is adequate.

Because resources are multiplexed, each user is given the illusion that he has a complete computing system at his sole disposal: a virtual computer. For our purposes, the basic elements of a virtual computer are its virtual processor and an "infinite," one-level virtual memory. Dynamic "advice" regarding resource requirements cannot be obtained successfully from users for several reasons:

(1) A user may build his program on the work of others, frequently sharing procedures whose time and storage requirements may be either unknown or, because of data dependence, indeterminable. Therefore he cannot be expected to estimate processor-memory needs.

(2) It is not clear what sort of "advice" might be solicited. Nor is it clear how the operating system should use it, for overhead incurred by using advice could well negate any advantages attained.

(3) Any advice acquired from a user would be intended (by him) to optimize the environment for his own program. Configuring resources to suit individuals may interfere with overall good service to the community of users. Thus it seems inadvisable at the present time to permit a user, at his discretion, to advise the operating system of his needs.

Likewise, compilers cannot be expected to supply information extracted from the structure of the program regarding resource requirements:1

(1) Programs will be modular in construction; information about other modules may be unavailable at compilation time. Because of data dependence there may be no

1 There have been attempts to do this. Ramamoorthy [2], for example, has put forth a proposal for automatic segmentation of programs during compilation.

way to decide (until run time) just which modules will be included in a computation.

(2) Compilers cluttered with extra machinery to predict memory needs will be slower in operation. Many users are less interested in whether their programs operate efficiently than whether they operate at all, and are therefore concerned with rapid compilation. Furthermore the compiler is an often-used component of the operating system; if slow and bulky, it can be a serious drain on system resources.

Therefore we are recommending mechanisms that monitor the behavior of a computation, basing allocation decisions on currently observed characteristics and not on advisories from programmers or compilers. Only a mechanism that oversees the behavior of a program in operation can cope with arbitrary interconnections of arbitrary modules having arbitrary characteristics.

Our treatment proceeds as follows. As background, we define the type of computer system in which our ideas are developed and discuss previous work with problems of memory management. We define the working set model, examine its properties, and then outline a method of implementing memory management based on this model. Finally, we show how “memory demand” is defined by a working set, how “processor demand” is defined by a process, and how resource allocation is a problem of balancing demands against equipment.
