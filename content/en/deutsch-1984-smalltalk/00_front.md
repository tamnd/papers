---
paper: deutsch-1984-smalltalk
title: Efficient Implementation of the Smalltalk-80 System
authors:
  - L. Peter Deutsch
  - Allan M. Schiffman
year: 1984
venue: POPL
field: languages
section_title: Front Matter
tag: 004A
kind: front
lang: en
source: https://doi.org/10.1145/800017.800542
pdf_sha256: 300584e302ee0fa5a006ee363d9e3f1b0df043c3259580e32dcd409e9a09871d
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 64032bbbb8fd182a69fb8ac6e35b65d90ee769ed62ed7b817d5f46f08accd2c1
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Efficient Implementation of the Smalltalk-80 System

L. Peter Deutsch
Xerox PARC, Software Concepts Group

Allan M. Schiffman
Fairchild Laboratory for Artificial Intelligence Research

ABSTRACT

The Smalltalk-80* programming language includes dynamic storage allocation, full upward funargs, and universally polymorphic procedures; the Smalltalk-80 programming system features interactive execution with incremental compilation, and implementation portability. These features of modern programming systems are among the most difficult to implement efficiently, even individually. A new implementation of the Smalltalk-80 system, hosted on a small microprocessor-based computer, achieves high performance while retaining complete (object code) compatibility with existing implementations. This paper discusses the most significant optimization techniques developed over the course of the project, many of which are applicable to other languages. The key idea is to represent certain runtime state (both code and data) in more than one form, and to convert between forms when needed.

*Smalltalk-80 is a trademark of the Xerox Corporation.
