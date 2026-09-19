---
paper: denning-1968-workingset
title: The Working Set Model for Program Behavior
authors:
  - Peter J. Denning
year: 1968
venue: Communications of the ACM
field: systems
section: "5"
section_title: Sharing
tag: "0607"
kind: section
lang: en
source: https://doi.org/10.1145/800001.811670
pdf_sha256: 3585991156b07c7e878ea9dff16ef7721401adff09ee328f5ee247b016289e0f
pdf_pages: "8"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: f25157379d469ea339e438d27721d56cbea1d5dc09465eb493ca15e7272e651f
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Sharing finds its place naturally.

When pages are shared, working sets will overlap. If Arden's [7] suggestion concerning program structure$^4$ is followed, sharing of data can be accomplished without modification of the regime of Figure 7. If a page is in at least one working set, the "use bits" in the page table entry will be ON and the page will not be removed. To prevent anomalies, the checker must not be permitted to examine the same page table more than once during one of its samples. Allocation policies should tend to run two processes together in time whenever they are sharing information (symptomized by overlap of their working sets), in order to avoid unnecessary reloading of the same information. How processes should be charged for memory usage when their working sets overlap is still an open question, and is under investigation.
