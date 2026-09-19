---
paper: deutsch-1984-smalltalk
title: Efficient Implementation of the Smalltalk-80 System
authors:
  - L. Peter Deutsch
  - Allan M. Schiffman
year: 1984
venue: POPL
field: languages
section_title: Dynamic Code Translation
kind: section
lang: en
source: https://doi.org/10.1145/800017.800542
pdf_sha256: 300584e302ee0fa5a006ee363d9e3f1b0df043c3259580e32dcd409e9a09871d
pdf_pages: "5"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 954959410f7788ea5223207dc6193d7edd06b21aeef1cee4317f68aae4b5ab76
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Our implementation of the Smalltalk-80 v-machine is designed to be easily switchable between different execution strategies. We have implemented a straightforward interpreter, a simple translator with almost no optimization, and a more sophisticated translator. Both translators exist in two variants, with and without the in-line cache described above. Switching between strategies simply requires relinking the implementation with a different set of modules; the price in execution speed paid for this flexibility is negligible.

Our first experiment in code translation was a simple translator that does little peephole optimization and always generates exactly 4 n-bytes per v-byte. (The latter restriction eliminated the need for the PC mapping tables described earlier.)

Our second experiment was a translator that does significant peephole optimization. The code it generates keeps the top element of the v-machine stack in a machine register whenever possible, and implements all v-instructions in-line except sends and a few rare instructions like load current context. Even arithmetic and relational operations are implemented in-line, with a call on an out-of-line routine if the operands are not small integers. The resulting code is bulky but fast.

To estimate the space required by translated methods, we have observed that the average v-method consists of 55% pointers (literal constants, message selectors, and references to global variables) and 45% v-instructions. Since our simple translator expands each v-code byte to 4 n-code bytes, the expansion factor for the method as a whole is .55 + (.45*4) = 2.35. The version of the simple translator that uses an in-line cache simply triples the size of the pointer area, leaving room for a cached class and n-method pointer regardless of whether the pointer is a selector or something else. This expands the total size of methods by a factor of (3*.55) + (4*.45) = 3.45. The observed expansion factors for the optimizing translators appear in the table below.

We ran the standard set of Smalltalk-80 benchmarks described in [Krasner 83], section 9, using each of our five execution strategies. The normalized results are summarized in the following table:

| Strategy | Space | Time |
| --- | --- | --- |
| Interpreter | 1.00 | 1.000 |
| Simple translator, no in-line cache | 2.35 | 0.686 |
| Simple translator with in-line cache | 3.45 | 0.625 |
| Optimizing translator, no in-line cache | 5.0 | 0.564 |
| Optimizing translator with in-line cache | 5.03 | 0.515 |

The space figure for the optimizing translator without the in-line cache could be reduced at the expense of further slowing the code down.

With respect to paging behavior in a virtual memory environment, we would like to compare the following three execution strategies:

* Pure interpretation: only v-code exists; it is brought into main memory as needed.

* Static translation: n-code is generated simultaneously with v-code. Only n-code is needed at execution time. N-code is brought into memory as needed.

* Dynamic translation: n-code is kept in a cache in main memory; v-code is brought into memory for translation as needed.

Note that space taken by n-code in main memory trades off against space for data. When main memory space is needed (either for n-code or for data), we have the option of replacing data pages or discarding n-code. Unfortunately, since the work described here has been carried out in a non-virtual memory environment, we have no experimental results on this topic.
