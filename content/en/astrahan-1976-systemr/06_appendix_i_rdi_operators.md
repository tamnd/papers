---
paper: astrahan-1976-systemr
title: 'System R: Relational Approach to Database Management'
authors:
  - M. M. Astrahan
  - M. W. Blasgen
  - D. D. Chamberlin
  - K. P. Eswaran
  - J. N. Gray
  - P. P. Griffiths
  - W. F. King
  - R. A. Lorie
  - P. R. McJones
  - J. W. Mehl
  - G. R. Putzolu
  - I. L. Traiger
  - B. W. Wade
  - V. Watson
year: 1976
venue: ACM TODS
field: databases
section_title: Appendix I. Rdi Operators
kind: appendix
lang: en
source: https://www.cs.princeton.edu/courses/archive/fall11/cos518/papers/system-R.pdf
pdf_sha256: e66b9412f77f7dc2599908c627e49e92e2949832e64a94f12652ab0915a8a1b5
pdf_pages: "34"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: fc8621c7cebce6db623a0b0ab85d72a09981c416d3a6f221f9f724e718b97d2c
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Square brackets [ ] are used below to indicate optional parameters.

Operators for data definition and manipulation:

SEQUEL ( [ <cursor name>, ] <any SEQUEL statement> )
FETCH ( <cursor name> [, <pointers to I/O locations>] )
FETCH_HOLD ( <cursor name> [, <pointers to I/O locations> ] )
OPEN ( <cursor name>, <name of relation or view> )
CLOSE ( <cursor name> )
KEEP ( <cursor name>, <new relation name>,
    <list of new field names> )
DESCRIBE ( <cursor name>, <degree>, <pointers to I/O locations> )
BIND ( <program variable name>, <program variable address> )

Operators on transactions and locks:

BEGIN_TRANS ( <transaction id>, <consistency level> )
END_TRANS
SAVE ( <save point name> )
RESTORE ( <save point name> )
RELEASE ( <cursor name> )
