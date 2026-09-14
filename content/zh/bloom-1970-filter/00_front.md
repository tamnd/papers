---
paper: bloom-1970-filter
title: Space/Time Trade-offs in Hash Coding with Allowable Errors
authors:
  - Burton H. Bloom
year: 1970
venue: Communications of the ACM
field: algorithms
section_title: Front Matter
tag: "0041"
kind: front
lang: zh
source: http://crystal.uta.edu/~mcguigan/cse6350/papers/Bloom.pdf
pdf_sha256: def80c7d042c39d5aab15e6ae1c2b55262ee1123ffcdf53143895089ab5c1728
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: eebbec5c64a3514a40733e527f39b796f19a4e3bf664e761a24e2daf4bc972ce
translated_from: content/en/bloom-1970-filter/00_front.md
source_content_sha256: 6e3e5001e35618a95d7390add14305bc048634f4195f7b3026a34d8a0cf633d5
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: efacc7653691a9b863e3c4cb746743abfecf7d31e7791764c13a541e1906db0f
prompt_sha256: da0c2696badfbe5d93fdc534847b1b0ca3b25ec37e0ce29843665f6e701c278e
---

带有允许误差的哈希编码中的空间／时间权衡

BURTON H. BLOOM

Computer Usage Company，Newton Upper Falls，Mass.

本文分析了哈希编码中某些计算因素之间的权衡。所考虑的典型问题是逐一测试一系列消息，以确定它们是否属于给定的消息集合。我们考察了两种新的哈希编码方法，并将其与一种特定的传统哈希编码方法进行比较。所考虑的计算因素包括哈希区域的大小（空间）、确定某消息不是给定集合成员所需的时间（拒绝时间），以及允许的错误频率。

新方法旨在减少存储哈希编码信息所需的空间，使其低于传统方法所需的空间。空间的减少是通过利用这样一种可能性实现的：在某些应用中，少量的误判错误可能是可以容忍的，尤其是在涉及大量数据、因而使用传统方法无法将哈希区域驻留于内存中的应用中。

在此类应用中，可以设想，通过结合使用新方法和较小的内存驻留哈希区域，并在必要时采用某种辅助的、可能耗时的测试来“捕获”与新方法相关的少量错误，从而提高整体性能。文中讨论了一个示例，以说明新方法可能的应用领域。
