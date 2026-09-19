---
paper: turing-1936-computable
title: On Computable Numbers, with an Application to the Entscheidungsproblem
authors:
  - A. M. Turing
year: 1936
venue: Proceedings of the London Mathematical Society
field: theory
section: "2"
section_title: Definitions
tag: 04C4
kind: section
lang: en
source: https://doi.org/10.1112/plms/s2-42.1.230
pdf_sha256: a126650c315e998ba96ea8248a60bde0afe60fec3e810acfc2b6c70d3b0e9f36
pdf_pages: 3-4
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 64faa061bcda5073d161e70cf6151c95f740a8387165a400cd5004a2afe02e1a
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Automatic machines.

If at each stage the motion of a machine (in the sense of §1) is completely determined by the configuration, we shall call the machine an "automatic machine" (or $a$-machine).

For some purposes we might use machines (choice machines or $c$-machines) whose motion is only partially determined by the configuration (hence the use of the word "possible" in §1). When such a machine reaches one of these ambiguous configurations, it cannot go on until some arbitrary choice has been made by an external operator. This would be the case if we were using machines to deal with axiomatic systems. In this paper I deal only with automatic machines, and will therefore often omit the prefix $a$.

Computing machines.

If an $a$-machine prints two kinds of symbols, of which the first kind (called figures) consists entirely of 0 and 1 (the others being called symbols of the second kind), then the machine will be called a computing machine. If the machine is supplied with a blank tape and set in motion, starting from the correct initial $m$-configuration, the subsequence of the symbols printed by it which are of the first kind will be called the *sequence computed by the machine*. The real number whose expression as a binary decimal is obtained by prefacing this sequence by a decimal point is called the *number computed by the machine*.

At any stage of the motion of the machine, the number of the scanned square, the complete sequence of all symbols on the tape, and the $m$-configuration will be said to describe the *complete configuration* at that stage. The changes of the machine and tape between successive complete configurations will be called the *moves* of the machine.

Circular and circle-free machines.

If a computing machine never writes down more than a finite number of symbols of the first kind, it will be called circular. Otherwise it is said to be circle-free.

A machine will be circular if it reaches a configuration from which there is no possible move, or if it goes on moving, and possibly printing symbols of the second kind, but cannot print any more symbols of the first kind. The significance of the term "circular" will be explained in § 8.

Computable sequences and numbers.

A sequence is said to be computable if it can be computed by a circle-free machine. A number is computable if it differs by an integer from the number computed by a circle-free machine.

We shall avoid confusion by speaking more often of computable sequences than of computable numbers.
