---
paper: aho-1975-corasick
title: 'Efficient String Matching: An Aid to Bibliographic Search'
authors:
  - Alfred V. Aho
  - Margaret J. Corasick
year: 1975
venue: Communications of the ACM
field: algorithms
section_title: Front Matter
tag: "0043"
kind: front
lang: zh
source: https://cr.yp.to/bib/1975/aho.pdf
pdf_sha256: f04940c07d2a12726bce4147fd4217e876cd969ddf44094ad90c866893deed34
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: b2889fe7cab6b1969dc013cef79e9e246dff0b306d3f85c2bd10cfbc3089ba6b
translated_from: content/en/aho-1975-corasick/00_front.md
source_content_sha256: 17d1d9c934a9c79dc1bf9969b26b2fdc40d089cc0cda4e05dff84776e249e10e
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: efacc7653691a9b863e3c4cb746743abfecf7d31e7791764c13a541e1906db0f
prompt_sha256: da0c2696badfbe5d93fdc534847b1b0ca3b25ec37e0ce29843665f6e701c278e
---

高效字符串匹配：文献检索的辅助工具

Alfred V. Aho and Margaret J. Corasick
Bell Laboratories

本文介绍了一种简单而高效的算法，用于在文本字符串中定位有限数量关键字的所有出现位置。该算法首先根据关键字构造有限状态模式匹配机，然后使用该模式匹配机单遍处理文本字符串。构造模式匹配机所需的时间与关键字长度之和成正比。模式匹配机处理文本字符串时所进行的状态转移次数与关键字的数量无关。该算法已用于提高图书馆文献检索程序的速度，性能提升了5至10倍。

关键词和短语：关键词和短语，字符串模式匹配，文献检索，信息检索，文本编辑，有限状态机，计算复杂度。

CR分类：3.74，3.71，5.22，5.25
