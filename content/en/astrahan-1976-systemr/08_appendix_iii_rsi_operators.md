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
section_title: Appendix Iii. Rsi Operators
kind: appendix
lang: en
source: https://www.cs.princeton.edu/courses/archive/fall11/cos518/papers/system-R.pdf
pdf_sha256: e66b9412f77f7dc2599908c627e49e92e2949832e64a94f12652ab0915a8a1b5
pdf_pages: 38-39
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 50276f8fdc6fd0f3e77572873b4d97060f6f83afa347b41a3d6512c6f55c9b4c
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The RSI operators are oriented toward the use of formatted control blocks. Rather than explain the detailed conventions of these control blocks, we list below an approximate but hopefully readable form for the operators. Square brackets [ ] are used to indicate optional parameters.

Operators on segments:

OPEN_SEGMENT ( <segid> )
CLOSE_SEGMENT ( <segid> )
SAVE_SEGMENT ( <segid> )
RESTORE_SEGMENT ( <segid> )

Operators on transactions and locks:

START_TRANS ( <consistency level> )
END_TRANS
SAVE_TRANS, RETURNS ( <saveid> )
RESTORE_TRANS ( <saveid> )
LOCK_SEGMENT ( <segid>, <mode: SHARE or EXCLUSIVE or SIX> )
LOCK_RELATION ( <segid>, <relid>, <mode, as above> )
RELEASE_TUPLE ( <segid>, <tid> )

Operators on tuples and scans:

FETCH ( <segid>, <relid>, <identifier: tid or scanid or imageid,
    key values>, <field list>, <pointers to I/O locations>
    [, HOLD] )

INSERT ( <segid>, <relid>, <pointers to I/O locations>
    [, <nearby tid> ] ), RETURNS ( <tid> )

DELETE ( <segid>, <relid>, <identifier, as above> )
UPDATE ( <segid>, <relid>, <identifier, as above>,
    <field list>, <pointers to I/O locations> )
OPEN_SCAN ( <segid>, <path: relid or imageid or linkid>,
    <start-point: key values for image, or tid for link,
    or scanid for link> ),
    RETURNS ( <scanid> )
NEXT ( <segid>, <scanid>, <field list>, <pointers to I/O locations>
    [, <search argument>] [, HOLD] )
CLOSE ( <segid>, <scanid> )
PARENT ( <child segid>, <linkid>, <identifier for new tuple, as
    above>, <field list>, <pointers to I/O locations>
    [, HOLD] )
CONNECT ( <child segid>, <linkid>, <identifier for new tuple, as
    above>, <neighbor relid>, <neighbor tid>,
    <location: BEFORE or AFTER> )
DISCONNECT ( <child segid>, <linkid>, <identifier for child, as
    above> )

Operators for data definition:

CREATE ( <segid>, <object type: REL or IMAGE or LINK >, <specs> ),
    RETURNS ( <object identifier: relid or imageid or linkid> )
DESTROY ( <segid>, <object identifier, as above> )
CHANGE ( <segid>, <object identifier, as above>,
    <new specs> )
READSPEC ( <segid>, <object identifier, as above>,
    <pointer to I/O location> )
