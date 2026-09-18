---
paper: tomasulo-1967-algorithm
title: An Efficient Algorithm for Exploiting Multiple Arithmetic Units
authors:
  - R. M. Tomasulo
year: 1967
venue: IBM Journal of Research and Development
field: architecture
section_title: Ld F0, Flb1 Ad F0, Flb2 Ae F0, Flb3
kind: section
lang: en
source: https://doi.org/10.1147/rd.111.0025
pdf_sha256: b62a6bc6a0b22d9acf08415f9f95f89d6a0b5c9ce46ee9a42563eb9228695be7
pdf_pages: 8-9
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 42ade3da2194e7ecb4f9388b4e95104aec8ac7eb88c3da0532313bd5d1406250
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Since only the last instruction, which is single-precision, will change F0, the low order result of the double-precision AD will be lost. This is handled by associating a bit with each register to indicate whether a particular register is the sink of an outstanding single- or double-precision instruction. If this bit does not match the "length" of the instruction being decoded, the decode is suspended until the busy bit goes off. While this stratagem† solves the logic problem, it does so at the expense of performance. Unfortunately, no way has been found to avoid this. Note, however, that all-single- or all-double-precision programs run at the maximum possible speed. It is only the interface between single- and double-precision to the same sink register that suffers delay.

* It does not add two cycles since storage gives one cycle prenotification of the arrival of data.
† Further complications arise from the fact that single-precision multiply produces a double-precision product. This is handled separately but with the same time penalty as above.

It might appear that the CDB adds one cycle to the execution time of each operation, but in fact it does not. In practice only 30 nsec of the 60-nsec CDB interval are required to perform all of the CDB functions. The remaining time could, in this case, be used by the execution unit to achieve a shorter effective cycle. For example, if an add requires 120 nsec, then add plus the CDB time required is 150 nsec. Therefore, as far as the add is concerned, the machine cycle could be 50 nsec. Besides, even without the CDB, a similar amount of time would be required to transmit results both to the floating-point registers and back as an input to the unit generating the result.

The following program, a typical partial differential equation inner loop, illustrates the possible performance increase.

| LOOP | MD | F0, Ai |
| --- | --- | --- |
|  | AD | F0, Bi |
|  | LD | F2, Ci |
|  | SDR | F2, F0 |
|  | MDR | F2, F6 |
|  | AD2 | F2, Ci |
|  | STD | F2, Ci |
|  | BXH | i, -1, 0, LOOP |

Without the CDB one iteration of the loop would use 17 cycles, allowing 4 per MD, 3 per AD and nothing for LD or STD. With the CDB one iteration requires 11 cycles. For this kind of code the CDB improves performance by about one-third.
