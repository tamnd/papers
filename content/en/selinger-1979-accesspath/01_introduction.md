---
paper: selinger-1979-accesspath
title: Access Path Selection in a Relational Database Management System
authors:
  - P. Griffiths Selinger
  - M. M. Astrahan
  - D. D. Chamberlin
  - R. A. Lorie
  - T. G. Price
year: 1979
venue: SIGMOD
field: databases
section: "1"
section_title: Introduction
tag: "0469"
kind: section
lang: en
source: https://doi.org/10.1145/582095.582099
pdf_sha256: d8c02d475b49fc90b9ee2b9e15a686a320b4b537272b8a5a661642db6c800d13
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 56c180de31d4bee82a6265ffe330d30b0e2443a468e6fc3cf8a6f6ad76440f5d
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

System R is an experimental database management system based on the relational model of data which has been under development at the IBM San Jose Research Laboratory since 1975 <1>. The software was developed as a research vehicle in relational database, and is not generally available outside the IBM Research Division.

This paper assumes familiarity with relational data model terminology as described in Codd <7> and Date <8>. The user interface in System R is the unified query, data definition, and manipulation language SQL <5>. Statements in SQL can be issued both from an on-line casual-user-oriented terminal interface and from programming languages such as PL/I and COBOL.

In System R a user need not know how the tuples are physically stored and what access paths are available (e.g. which columns have indexes). SQL statements do not require the user to specify anything about the access path to be used for tuple retrieval. Nor does a user specify in what order joins are to be performed. The System R optimizer chooses both join order and an access path for each table in the SQL statement. Of the many possible choices, the optimizer chooses the one which minimizes “total access cost” for performing the entire statement.

This paper will address the issues of access path selection for queries. Retrieval for data manipulation (UPDATE, DELETE) is treated similarly. Section 2 will describe the place of the optimizer in the processing of a SQL statement, and section 3 will describe the storage component access paths that are available on a single physically stored table. In section 4 the optimizer cost formulas are introduced for single table queries, and section 5 discusses the joining of two or more tables, and their corresponding costs. Nested queries (queries in predicates) are covered in section 6.
