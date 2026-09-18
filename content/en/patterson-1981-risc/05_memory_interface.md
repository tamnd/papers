---
paper: patterson-1981-risc
title: 'RISC I: A Reduced Instruction Set VLSI Computer'
authors:
  - David A. Patterson
  - Carlo H. Sequin
year: 1981
venue: ISCA
field: architecture
section_title: Memory Interface
kind: section
lang: en
source: https://people.eecs.berkeley.edu/~kubitron/courses/cs252-F00/handouts/papers/p216-patterson.pdf
pdf_sha256: d49afdf3db5a8374fbc757059fab0562b9a517b3ff7abec17c2e6b88c48f03e1
pdf_pages: 6-7
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 637e62a8e3887b7e32383945f914a61d32712a7ffd24e5eb77ed0db471f0d1c4
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

In most computers, the interface to memory is a main performance bottleneck, so this point must be given special consideration. In our discussions and simulations, we assumed that we can access main memory in a single RISC CPU cycle. Depending on the assumptions that we make for our CPU cycle time, and the size of the main memory, this assumption may be too optimistic. We thus reworked our benchmarks also under the assumption that two CPU cycles are required to access data memory. Performance degraded only 10%, because the register window scheme reduces the number of off-chip data references. Data references do not constitute a problem, but allowing two cycles to fetch instructions out of memory would reduce performance by almost a factor of 2.

Clearly, this memory interface will be an increasingly critical point as the intrinsic speed of CPU increases with technologic advances. Accesses to memory can be forced to come mainly from on-chip, either with a large register file or with an on-chip cache and associated memory hierarchy.6

An on-chip cache would be beneficial for RISC. It is sometimes forgotten that a cache is ineffective if it is too small. In our opinion, an effective data cache would have to be quite a bit larger than our planned register file, especially if it was to provide the same number of ports as the register file. More-complicated translation and decoding might even stretch the basic CPU cycle time. Given the limited amount of circuitry we can place onto a chip at this point, and given the university environment and our student designers, a register file is clearly the safer way to go.

Although the problem of data accesses has been alleviated by the large number of registers and the effective window scheme, the number of instruction fetches has actually increased because of the simplicity of individual instructions. Instruction fetches from main memory are indeed a major speed-limiting factor. An instruction cache is a desirable commodity. Because there is no need for CPU to write into this cache, its controller can be simpler than that of a data cache. We decided that RISC I should not be burdened with the design of a full-blown on-chip cache, but an instruction cache would definitely be a good idea for the next-generation RISC.
