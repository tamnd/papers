---
paper: patterson-1981-risc
title: 'RISC I: A Reduced Instruction Set VLSI Computer'
authors:
  - David A. Patterson
  - Carlo H. Sequin
year: 1981
venue: ISCA
field: architecture
section_title: Support for High-level Languages
kind: section
lang: en
source: https://people.eecs.berkeley.edu/~kubitron/courses/cs252-F00/handouts/papers/p216-patterson.pdf
pdf_sha256: d49afdf3db5a8374fbc757059fab0562b9a517b3ff7abec17c2e6b88c48f03e1
pdf_pages: "2"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 4f00f133a304ddf5888a158ae47f39585ba0a056df52aec4a856619f6359fa8b
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Clearly, new architectures should be designed with the needs of high-level language programming in mind. It should not matter whether a high-level language system is implemented mostly by hardware or mostly by software, provided the system hides any lower levels from the programmer.7 Given this framework, the role of the architect is to build a cost-effective system by deciding what pieces of the system should be in hardware and what pieces should be in software.

The selection of languages for consideration in RISC I was influenced by our environment; we chose C and Pascal languages, because there is a larger user community and considerable local expertise. Given the limited number of transistors that can be integrated into a single-chip computer, most of the pieces of a RISC high-level language system are in software, with hardware support for only the most time-consuming events.

To determine what constructs are used most frequently and, if possible, what constructs use the most time in average programs, we looked first at the frequency of classes of variables in high-level language programs. Figure 1 shows data collected by Goldwasser for Pascal language8 and by Cohen and Soiffer for C language.9

The most important observation was that integer constants appeared almost as frequently as components of arrays or structures. What is not shown is that over 80% of the scalars were local variables and over 90% of the arrays or structures were global variables.

We also looked at the relative dynamic frequency of high-level language statements for the same eight programs; the ones with averages over 1% are shown in Figure 2. This information does not tell what statements use the most time in the execution of typical programs. To answer that question, we looked at the code produced by typical versions of each of these statements. A "typical" version of each statement was supplied by W. Wulf (private communication, Nov. 1980) as part of his study on judging the quality of compilers. We used C compilers for VAX, PDP-11, and 68000 to determine the average number of instructions and memory references. By multiplying the frequency of occurrence of each statement with the corresponding number of machine instructions and memory references, we obtained the data shown in Figure 3, which is ordered by memory references.

The data in these tables suggests that the procedure CALL/return is the most time-consuming operation in typical high-level language programs. The statistics on operands emphasizes the importance of local variables and constants. RISC I attempts to make each of these constructs efficient, implementing the less-frequent operations with subroutines.
