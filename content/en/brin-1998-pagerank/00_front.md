---
paper: brin-1998-pagerank
title: The Anatomy of a Large-Scale Hypertextual Web Search Engine
authors:
  - Sergey Brin
  - Lawrence Page
year: 1998
venue: Computer Networks and ISDN Systems
field: algorithms
section_title: Front Matter
kind: front
lang: en
source: https://doi.org/10.1016/s0169-7552(98)00110-x
pdf_sha256: 3a155ade395c7789876a0bc08a1842f909486438c1b1739ae531fa5c797d93f0
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: bb9c52869a1fd932379f1b224b04320ef96bc48516321a848c2c0f71fd4093d0
prompt_sha256: 329630a0b9175a55e4af1b8e281a3e67eeab250f8d643953b7dcde99743c7628
---

The anatomy of a large-scale hypertextual Web search engine $^1$

Sergey Brin $^2$, Lawrence Page $^*,2$

Computer Science Department, Stanford University, Stanford, CA 94305, USA

Abstract

In this paper, we present Google, a prototype of a large-scale search engine which makes heavy use of the structure present in hypertext. Google is designed to crawl and index the Web efficiently and produce much more satisfying search results than existing systems. The prototype with a full text and hyperlink database of at least 24 million pages is available at http://google.stanford.edu/

To engineer a search engine is a challenging task. Search engines index tens to hundreds of millions of Web pages involving a comparable number of distinct terms. They answer tens of millions of queries every day. Despite the importance of large-scale search engines on the Web, very little academic research has been done on them. Furthermore, due to rapid advance in technology and Web proliferation, creating a Web search engine today is very different from three years ago. This paper provides an in-depth description of our large-scale Web search engine — the first such detailed public description we know of to date.

Apart from the problems of scaling traditional search techniques to data of this magnitude, there are new technical challenges involved with using the additional information present in hypertext to produce better search results. This paper addresses this question of how to build a practical large-scale system which can exploit the additional information present in hypertext.
