---
paper: royce-1970-lifecycle
title: Managing the Development of Large Software Systems
authors:
  - Winston W. Royce
year: 1970
venue: IEEE WESCON
field: software
section_title: 'Step 1: Program Design Comes First'
kind: section
lang: en
source: https://github.com/tpn/pdfs
pdf_sha256: 9f7db065bd1c911a8d17590eec548478f944c8b05c408f101911cde57d815a78
pdf_pages: "4"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: ef4f4a9ea66076676e7813a08c421f1e0fbcb992cfcfa3a5935e02953dbee2ae
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The first step towards a fix is illustrated in Figure 5. A preliminary program design phase has been inserted between the software requirements generation phase and the analysis phase. This procedure can be criticized on the basis that the program designer is forced to design in the relative vacuum of initial software requirements without any existing analysis. As a result, his preliminary design may be substantially in error as compared to his design if he were to wait until the analysis was complete. This criticism is correct but it misses the point. By this technique the program designer assures that the software will not fail because of storage, timing, and data flux reasons. As the analysis proceeds in the succeeding phase the program designer must impose on the analyst the storage, timing, and operational constraints in such a way that he senses the consequences. When he justifiably requires more of this kind of resource in order to implement his equations it must be simultaneously snatched from his analyst compatriots. In this way all the analysts and all the program designers will contribute to a meaningful design process which will culminate in the proper allocation of execution time and storage resources. If the total resources to be applied are insufficient or if the embryo operational design is wrong it will be recognized at this earlier stage and the iteration with requirements and preliminary design can be redone before final design, coding and test commences.

How is this procedure implemented? The following steps are required.

1) Begin the design process with program designers, not analysts or programmers.

2) Design, define and allocate the data processing modes even at the risk of being wrong. Allocate processing, functions, design the data base, define data base processing, allocate execution time, define interfaces and processing modes with the operating system, describe input and output processing, and define preliminary operating procedures.

3) Write an overview document that is understandable, informative and current. Each and every worker must have an elemental understanding of the system. At least one person must have a deep understanding of the system which comes partially from having had to write an overview document.

Figure.

Figure 5. Step 1: Insure that a preliminary program design is complete before analysis begins. {#royce-1970-lifecycle-fig-5 .figure tag=037D}
