---
paper: patterson-1981-risc
title: 'RISC I: A Reduced Instruction Set VLSI Computer'
authors:
  - David A. Patterson
  - Carlo H. Sequin
year: 1981
venue: ISCA
field: architecture
section_title: Front Matter
kind: front
lang: en
source: https://people.eecs.berkeley.edu/~kubitron/courses/cs252-F00/handouts/papers/p216-patterson.pdf
pdf_sha256: d49afdf3db5a8374fbc757059fab0562b9a517b3ff7abec17c2e6b88c48f03e1
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: a686fd9175b03d68a4a6bedd90c2299a0601e73a0a0d60e2e5b89ec8a4121cc4
prompt_sha256: 329630a0b9175a55e4af1b8e281a3e67eeab250f8d643953b7dcde99743c7628
---

RISC I: A REDUCED INSTRUCTION SET VLSI COMPUTER

DAVID A. PATTERSON and CARLO H. SEQUIN

Computer Science Division
University of California
Berkeley, California

ABSTRACT

The Reduced Instruction Set Computer (RISC) Project investigates an alternative to the general trend toward computers with increasingly complex instruction sets: With a proper set of instructions and a corresponding architectural design, a machine with a high effective throughput can be achieved. The simplicity of the instruction set and addressing modes allows most instructions to execute in a single machine cycle, and the simplicity of each instruction guarantees a short cycle time. In addition, such a machine should have a much shorter design time.

This paper presents the architecture of RISC I and its novel hardware support scheme for procedure call/return. Overlapping sets of register banks that can pass parameters directly to subroutines are largely responsible for the excellent performance of RISC I. Static and dynamic comparisons between this new architecture and more traditional machines are given. Although instructions are simpler, the average length of programs was found not to exceed programs for DEC VAX 11 by more than a factor of 2. Preliminary benchmarks demonstrate the performance advantages of RISC. It appears possible to build a single chip computer faster than VAX 11/780.
