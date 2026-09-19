---
paper: patterson-1981-risc
title: 'RISC I: A Reduced Instruction Set VLSI Computer'
authors:
  - David A. Patterson
  - Carlo H. Sequin
year: 1981
venue: ISCA
field: architecture
section_title: Introduction
kind: section
lang: en
source: https://people.eecs.berkeley.edu/~kubitron/courses/cs252-F00/handouts/papers/p216-patterson.pdf
pdf_sha256: d49afdf3db5a8374fbc757059fab0562b9a517b3ff7abec17c2e6b88c48f03e1
pdf_pages: 1-2
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: ef6c732ee921c3be6291da009859ddd003caf8da557b04f503f4f9b236e3eec4
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

A general trend in computers today is to increase the complexity of architectures commensurate with the increasing potential of implementation technologies, as exemplified by the complex successors of simpler machines. Compare, for example, VAX 11$^1$ to PDP-11, IBM System/38$^2$ to IBM System/3, and Intel iAPX-432$^3$ to 8086. The consequences of this complexity are increased design time, increased design errors, and inconsistent implementations.$^4$ We call this class of computers, complex instruction set computers (CISC).

Investigations of VLSI architectures$^5$ indicated that one of the major design limitations is the delay-power penalty of data transfers across chip boundaries and the still-limited amount of resources (devices) available on a single chip. Even a million transistors does not go far if a whole computer has to be built from it.$^6$ This raises the question as to whether the extra hardware needed to implement CISC is the best way to use this "scarce" resource.

The above findings led to the Reduced Instruction Set Computer (RISC) Project. The purpose of the project is to explore alternatives to the general trend toward architectural complexity. The hypothesis is that by reducing the instruction set, VLSI architecture can be designed that uses the scarce resources more effectively than CISC. We also expect this approach to reduce design time, the number of design errors, and the execution time of individual instructions.

Our initial version of such a computer is called RISC I. To meet our goals of simplicity and effective single-chip implementation, we placed the following "constraints" on the architecture:

1. Execute one instruction per cycle. RISC I instructions should be about as fast as, and no more complicated than, micro instructions in current machines such as PDP-11 or VAX. Furthermore, this simplicity makes microcode control unnecessary. Skipping this extra level of interpretation appears to enhance performance while reducing chip size.

2. All instructions are the same size. This again simplifies implementation. We intentionally postponed attempts to reduce program size.

3. Only load and store instructions access memory; the rest operate between registers. This restriction simplifies the design. The lack of complex addressing modes also makes it easier to restart instructions.

4. Support high-level languages (HLL). An explanation of the degree of support follows. Our intention is always to use high-level languages with RISC I.

RISC I supports 32-bit addresses, 8-, 16-, and 32-bit data, and several 32-bit registers. We intend to examine support for operating systems and floating-point calculations in successors to RISC I.

It would appear that such constraints would result in a machine with substantially poorer code density or poorer performance or both. In spite of these constraints, the resulting architecture competes favorably with other state-of-the-art machines such as VAX 11/780. This is largely because of an innovative new scheme of register organization we call overlapped register windows.
