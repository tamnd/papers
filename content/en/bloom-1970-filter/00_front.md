---
paper: bloom-1970-filter
title: Space/Time Trade-offs in Hash Coding with Allowable Errors
authors:
  - Burton H. Bloom
year: 1970
venue: Communications of the ACM
field: algorithms
section_title: Front Matter
kind: front
lang: en
source: http://crystal.uta.edu/~mcguigan/cse6350/papers/Bloom.pdf
pdf_sha256: def80c7d042c39d5aab15e6ae1c2b55262ee1123ffcdf53143895089ab5c1728
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 6e3e5001e35618a95d7390add14305bc048634f4195f7b3026a34d8a0cf633d5
prompt_sha256: 329630a0b9175a55e4af1b8e281a3e67eeab250f8d643953b7dcde99743c7628
---

Space/Time Trade-offs in Hash Coding with Allowable Errors

BURTON H. BLOOM

Computer Usage Company, Newton Upper Falls, Mass.

In this paper trade-offs among certain computational factors in hash coding are analyzed. The paradigm problem considered is that of testing a series of messages one-by-one for membership in a given set of messages. Two new hash-coding methods are examined and compared with a particular conventional hash-coding method. The computational factors considered are the size of the hash area (space), the time required to identify a message as a nonmember of the given set (reject time), and an allowable error frequency.

The new methods are intended to reduce the amount of space required to contain the hash-coded information from that associated with conventional methods. The reduction in space is accomplished by exploiting the possibility that a small fraction of errors of commission may be tolerable in some applications, in particular, applications in which a large amount of data is involved and a core resident hash area is consequently not feasible using conventional methods.

In such applications, it is envisaged that overall performance could be improved by using a smaller core resident hash area in conjunction with the new methods and, when necessary, by using some secondary and perhaps time-consuming test to "catch" the small fraction of errors associated with the new methods. An example is discussed which illustrates possible areas of application for the new methods.
