---
paper: birrell-1984-rpc
title: Implementing Remote Procedure Calls
authors:
  - Andrew D. Birrell
  - Bruce Jay Nelson
year: 1984
venue: ACM TOCS
field: systems
section_title: Front Matter
kind: front
lang: en
source: https://www.cs.cmu.edu/~dga/15-712/F07/papers/birrell842.pdf
pdf_sha256: 0c5058383786e2b3e8fa9894872358e362a6f6ffc58c06f29dc08b836318f432
pdf_pages: 2-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 443c55fbdd07742a112658c60d65e70a2b25966b03a3fec4d237d8c751d86d25
prompt_sha256: 329630a0b9175a55e4af1b8e281a3e67eeab250f8d643953b7dcde99743c7628
---

still execute (depending on the details of the parallelism of that environment and the RPC implementation).

There are many attractive aspects to this idea. One is clean and simple semantics: these should make it easier to build distributed computations, and to get them right. Another is efficiency: procedure calls seem simple enough for the communication to be quite rapid. A third is generality: in single-machine computations, procedures are often the most important mechanism for communication between parts of the algorithm.

The idea of RPC has been around for many years. It has been discussed in the public literature many times since at least as far back as 1976 [15]. Nelson’s doctoral dissertation [13] is an extensive examination of the design possibilities for an RPC system and has references to much of the previous work on RPC. However, full-scale implementations of RPC have been rarer than paper designs. Notable recent efforts include Courier in the Xerox NS family of protocols [4], and current work at MIT [10].

This paper results from the construction of an RPC facility for the Cedar project. We felt, because of earlier work (particularly Nelson’s thesis and associated experiments), that we understood the choices the designer of an RPC facility must make. Our task was to make the choices in light of our particular aims and environment. In practice, we found that several areas were inadequately understood, and we produced a system whose design has several novel aspects.
