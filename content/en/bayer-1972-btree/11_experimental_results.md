---
paper: bayer-1972-btree
title: Organization and Maintenance of Large Ordered Indices
authors:
  - Rudolf Bayer
  - Edward M. McCreight
year: 1972
venue: Acta Informatica
field: databases
section: "11"
section_title: Experimental Results
tag: "0700"
kind: section
lang: en
source: https://infolab.usc.edu/csci585/Spring2010/den_ar/indexing.pdf
pdf_sha256: 69826c036d7948fe5b02f7498620c90cc6a8de2504251a57994d13dc7b14e470
pdf_pages: 31-35
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: c68a1a98202684c1f5e62d862afa1d570aabe9a51aabc3cfe57df246a12a6e52
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The algorithms presented here were programmed and their performance measured during various experiments. The programs were run on an IBM 360/44 computer with a 2311 disc unit as a backup store. For the index element size chosen (14 8-bit characters) and index size generally used (about 10,000 index elements), the average access mechanism delay for this unit is about 50 ms, after which information transfer takes place at the rate of about 90 $\mu s$ per index element. From these two parameters, our analysis predicts an optimal page size $(2k)$ on the order of 120 index elements.

The programming included a simple demand paging scheme to take advantage of available core storage (about 1250 index elements' worth) and thus to attempt to reduce the number of physical disc operations. In the following section by virtual disc read we mean a request to the paging scheme that a certain disc page be available in core; a virtual disc read will result in a physical disc read only if there is no copy of the requested disc page already in the paging area of core storage. A virtual disc write is defined analogously.

At the time of this writing ten experiments had been performed. These experiments were intended to give us an idea of what kind of performance to expect, what kind of storage utilization to expect, and so forth. For us the specification of an experiment consists of choosing

1) whether or not to permit overflows on insertion,
2) a number of index elements per page, and

3) a sequence of transactions to be made against an initially empty index.

At several points during the performance of an experiment certain performance variables are recorded. From these the performance of the algorithms according to various performance measures can be deduced; to wit

1) % storage utilization
2) average number of virtual disc reads/transaction
3) average number of physical disc reads/transaction
4) average number of virtual disc writes/insertion or deletion
5) average number of physical disc writes/insertion or deletion
6) average number of transactions/second.

We now summarize the experiments. Each experiment was divided into several phases, and at the end of each of these the performance variables were measured. Phases are denoted by numbers within parentheses.

E1: 25 elements/page, overflow permitted.
    (1) 10000 insertions sequential by key,
    (2) 50 insertions, 50 retrievals, and 100 deletions uniformly random in the key space.

E2: 120 elements/page; otherwise identical to E1.

E3: 250 elements/page; otherwise identical to E1.

E4: 120 elements/page, overflow permitted.
    (1) 10000 insertions sequential by key,
    (2) 1000 retrievals uniformly random in key space,

(3) 10000 sequential deletions.

E5: 120 elements/page, overflow *not* permitted.

(1) 5000 insertions uniformly random in key space,
(2) 1000 retrievals uniformly random in key space,
(3) 5000 deletions uniformly random in key space.

E6: Overflow permitted; otherwise identical to E5.

E7: 120 elements/page, overflow permitted.

(1) 5000 insertions sequential by key,
(2) 6000 each insertions, retrievals, and deletions uniformly random in key space.

E9: 250 elements/page; otherwise identical to E8.

E10: 120 elements/page, overflow permitted.

(1) 100,000 insertions sequential by key,
(2) 1000 each insertions, deletions, and retrievals uniformly random in key space,
(3) 100 group retrievals uniformly random in key space, where a group is a sequence of 100 consecutive keys (statistics on the basis of 10000 transactions),
(4) 10000 insertions sequential by key, to merge uniformly with the elements inserted in phase (1).

|  | % Storage used | VR/T* | PR/T | VW/I or D | PW/I or D | T/Sec. |
| --- | --- | --- | --- | --- | --- | --- |
| E1(1) | 99.8 | 2.2 | 0 | 2.3 | .04 | 66.1 |
| E1(2) | 91.5 | 4.4 | 1.62 | 2.7 | 1.5 | 6.6 |
| E2(1) | 99.2 | 1.0 | 0 | 1.0 | .008 | 94.5 |
| E2(2) | 87.3 | 2.5 | 1.15 | 1.3 | 1.1 | 6.7 |
| E3(1) | 97.6 | 1.0 | 0 | 1.0 | .004 | 100.0 |
| E3(2) | 84.7 | 2.4 | 1.08 | 1.3 | 1.1 | 5.2 |
| E4(1) | 99.2 | 1.0 | 0 | 1.0 | .008 | 94.5 |
| E4(2) | 99.2 | 2.0 | --- | --- | --- | 19.5 |
| E4(3) | --- | 2.0 | .01 | 2.0 | 0 | 74.1 |
| E5(1) | 67.1 | 1.0 | .55 | 1.0 | .56 | 17.0 |
| E5(2) | 67.1 | 2.0 | .83 | --- | --- | 18.2 |
| E5(3) | --- | 4.0 | .68 | 2.2 | .65 | 12.4 |
| E6(1) | 86.7 | 1.1 | .55 | 1.1 | .54 | 17.1 |
| E6(2) | 86.7 | 2.0 | .79 | --- | --- | 24.3 |
| E6(3) | --- | 4.0 | .65 | 2.2 | .62 | 13.4 |
| E7(1) | 96.9 | 1.0 | 0 | 1.0 | .008 | 111.9 |
| E7(2) | 76.8 | 2.3 | .83 | 1.3 | .88 | 13.1 |
| E8(1) | 84.5 | 1.3 | .87 | 1.3 | .85 | 10.1 |
| E8(2) | 83.9 | 3.7 | 1.00 | 3.0 | 1.00 | 9.5 |
| E9(1) | 86.4 | 1.1 | .84 | 1.0 | .82 | 8.5 |
| E9(2) | 85.2 | 2.3 | .94 | 1.1 | .96 | 8.2 |
| E10(1) | 99.8 | 1.9 | 0 | 1.9 | .008 | 91.7 |
| E10(2) | 82.1 | 4.1 | 1.94 | 1.8 | 1.54 | 4.2 |
| E10(3) | 82.1 | 4.0 | .03 | --- | --- | 75.7 |
| E10(4) | 83.8 | 2.2 | .10 | 2.2 | .11 | 38.0 |

*These numbers are somewhat misleading for deletions, due to the way the deletions were programmed into the experiments. To find the necessary number of virtual reads, for sequential deletions subtract one from the number shown, and for random deletions subtract one and multiply the result by about 0.5.

References:

Adelson-Velskii, G. M. and Landis, E. M. An Information Organization Algorithm. DANSSSR, No. 2, 1962.

Foster, C. C. Information Storage and Retrieval Using AVL Trees.
Proc. ACM 20th Nat'l. Conf. (1965), pp. 192-205.

Gladun, V. P. Storage Organization for Key Search and Recording.
Cybernetics, Vol. 1, No. 4, August 1965.

Landauer, W. I. The Balanced Tree and Its Utilization in Information Retrieval. IEEE Trans. on Electronic Computers, Vol. EC-12, No. 6, December 1963.

Sussenguth, E. H., Jr. The Use of Tree Structures for Processing Files. Comm. ACM, Vol. 6, No. 5, May 1963.
