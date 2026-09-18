---
paper: codd-1970-relational
title: A Relational Model of Data for Large Shared Data Banks
authors:
  - E. F. Codd
year: 1970
venue: Communications of the ACM
field: databases
section_title: Front Matter
tag: "0034"
kind: front
lang: en
source: https://www.seas.upenn.edu/~zives/03f/cis550/codd.pdf
pdf_sha256: fa2579f427a4da68466ef159a3ae0c3c1fe4eafec60f73c9f2f40378a65d8ef9
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: e23f0c2d9064fac25f81260b415860d52e72ef7f9de29d88b36d839a352006a0
prompt_sha256: 6deed113e702745ea82772457035bb281a0a0db9eb7baaa76a842f19ad073ba5
---

A Relational Model of Data for Large Shared Data Banks

E. F. Codd
IBM Research Laboratory, San Jose, California

Future users of large data banks must be protected from having to know how the data is organized in the machine (the internal representation). A prompting service which supplies such information is not a satisfactory solution. Activities of users at terminals and most application programs should remain unaffected when the internal representation of data is changed and even when some aspects of the external representation are changed. Changes in data representation will often be needed as a result of changes in query, update, and report traffic and natural growth in the types of stored information.

Existing noninferential, formatted data systems provide users with tree-structured files or slightly more general network models of the data. In Section 1, inadequacies of these models are discussed. A model based on n-ary relations, a normal form for data base relations, and the concept of a universal data sublanguage are introduced. In Section 2, certain operations on relations (other than logical inference) are discussed and applied to the problems of redundancy and consistency in the user's model.

KEY WORDS AND PHRASES: data bank, data base, data structure, data organization, hierarchies of data, networks of data, relations, derivability, redundancy, consistency, composition, join, retrieval language, predicate calculus, security, data integrity
CR CATEGORIES: 3.70, 3.73, 3.75, 4.20, 4.22, 4.29
