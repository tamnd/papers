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
section_title: Appendix Ii. Sequel Syntax
kind: appendix
lang: en
source: https://www.cs.princeton.edu/courses/archive/fall11/cos518/papers/system-R.pdf
pdf_sha256: e66b9412f77f7dc2599908c627e49e92e2949832e64a94f12652ab0915a8a1b5
pdf_pages: 34-38
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: d344b7b10f8cc597788ad091a8087116b2ff81a8f80e310a946bca898f5bf16c
edited: true
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The following is a shortened version of the BNF syntax for SEQUEL. It contains several minor ambiguities and generates a number of constructs with no semantic support, all of which are (hopefully) missing from our complete, production syntax. Square brackets [ ] are used to indicate optional constructs.

```sql
statement ::= query
    | dml-statement
    | ddl-statement
    | control-statement dml-statement ::= assignment
    | insertion
    | deletion
    | update query ::= query-expr [ ORDER BY ord-spec-list ] assignment ::= receiver <- query-expr receiver ::= table-name [ ( field-name-list ) ] insertion ::= INSERT INTO receiver : insert-spec insert-spec ::= query-expr
    | literal
    | constant field-name-list ::= field-name
    | field-name-list , field-name deletion ::= DELETE table-name [ var-name ] [ where-clause ] update ::= UPDATE table-name [ var-name ] set-clause-list .
    [ where-clause ] where-clause ::= WHERE boolean
    | WHERE CURRENT [ TUPLE ] OF
        [ CURSOR ] cursor-name set-clause-list ::= set-clause
    | set-clause-list , set-clause set-clause ::= SET field-name = expr
    | SET field-name = ( query-expr )

query-expr ::= query-block
    | query-expr set-op query-block
    | ( query-expr ) set-op ::= INTERSECT | UNION | MINUS

query-block ::= select-clause FROM from-list
    [ WHERE boolean ]
    [ GROUP BY field-spec-list
        [ HAVING boolean ] ] select-clause ::= SELECT [ UNIQUE ] sel-expr-list
    | SELECT [ UNIQUE ] * sel-expr-list ::= sel-expr
    | sel-expr-list , sel-expr sel-expr ::= expr [ : host-location ]
```

| var-name . * | table-name *

```text
from-list ::= table-name [ var-name ]
    | from-list , table-name [ var-name ] field-spec-list ::= field-spec
    | field-spec-list , field-spec

ord-spec-list ::= field-spec [ direction ]
    | ord-spec-list , field-spec [ direction ] direction ::= ASC | DESC

boolean ::= boolean-term
    | boolean OR boolean-term boolean-term ::= boolean-factor
    | boolean-term AND boolean-factor
```

```text
boolean-factor ::= [ NOT ] boolean-primary boolean-primary ::= predicate
    | ( boolean ) predicate ::= expr comparison expr
    | expr BETWEEN expr AND expr
    | expr comparison table-spec
    | < field-spec-list > = full-table-spec
    | < field-spec-list > [ IS ] IN full-table-spec
    | IF predicate THEN predicate
    | SET ( field-spec-list ) comparison
        full-table-spec
    | SET ( field-spec-list ) comparison
        SET ( field-spec-list )
    | table-spec comparison full-table-spec full-table-spec ::= table-spec
    | ( entry )
    | constant table-spec ::= query-block
    | ( query-expr )
    | literal expr ::= arith-term
    | expr add-op arith-term arith-term ::= arith-factor
    | arith-term mult-op arith-factor arith-factor ::= [ add-op ] primary primary ::= [ OLD | NEW ] field-spec
    | set-fn ([ UNIQUE ] expr )
    | COUNT ( * )
    | constant
    | ( expr ) field-spec ::= field-name
    | table-name . field-name
    | var-name . field-name comparison ::= comp-op
    | CONTAINS
    | DOES NOT CONTAIN
    | [ IS ] IN
    | [ IS ] NOT IN comp-op ::= = | ¬= | > | >= | < | <= add-op ::= + | -mult-op ::= * | / set-fn ::= AVG | MAX | MIN | SUM | COUNT | identifier literal ::= ( lit-tuple-list )
    | ( entry-list )
    | lit-tuple lit-tuple-list ::= lit-tuple
    | lit-tuple-list , lit-tuple lit-tuple ::= < entry >
    | < entry-list > entry-list ::= entry , entry
    | entry-list , entry entry ::= [ constant ] constant ::= quoted-string
    | number
    | host-location
    | NULL
    | USER
    | DATE
    | field-name OF CURSOR cursor-name
        [ ON table-name ] table-name ::= name image-name ::= name link-name ::= name asrt-name ::= name trig-name ::= name name ::= [ creator . ] identifier creator ::= identifier user-name ::= identifier field-name ::= identifier var-name ::= identifier cursor-name ::= identifier host-location ::= identifier integer ::= number ddl-statement ::= create-table
                | expand-table
                | keep-table
                | create-image
                | create-link
                | define-view
                | drop
                | comment create-table ::= CREATE [ perm-spec ] [ share-spec ] TABLE
                table-name : field-defn-list perm-spec ::= PERMANENT | TEMPORARY share-spec ::= SHARED | PRIVATE field-defn-list ::= field-defn
                  | field-defn-list , field-defn field-defn ::= field-name ( type [ , NONULL ] ) type ::= CHAR ( integer )
       | CHAR ( * )
       | INTEGER
       | SMALLINT
       | DECIMAL ( integer , integer )
       | FLOAT expand-table ::= EXPAND TABLE table-name ADD
                FIELD field-defn keep-table ::= KEEP TABLE table-name create-image ::= CREATE [ image-mod-list ] IMAGE image-name
                ON table-name ( ord-spec-list ) image-mod-list ::= image-mod
                 | image-mod-list image-mod image-mod ::= UNIQUE
            | CLUSTERING create-link ::= CREATE [ CLUSTERING ] LINK link-name
              FROM table-name ( field-name-list )
              TO table-name ( field-name-list )
              [ ORDER BY ord-spec-list ] define-view ::= DEFINE [ perm-spec ] VIEW table-name
              [ ( field-name-list ) ] AS query drop ::= DROP system-entity name comment ::= COMMENT ON system-entity name : quoted-string
          | COMMENT ON FIELD table-name . field-name
            : quoted-string system-entity ::= TABLE | VIEW | ASSERTION
                | TRIGGER | IMAGE | LINK control-statement ::= asrt-statement
                    | enforcement
                    | define-trigger
                    | grant
                    | revoke asrt-statement ::= ASSERT asrt-name [ IMMEDIATE ]
                  [ ON asrt-condition ] : boolean asrt-condition ::= action-list
                 | table-name [ var-name ] action-list ::= action
              | action-list , action action ::= INSERTION OF table-name [ var-name ]
         | DELETION OF table-name [ var-name ]
         | UPDATE OF table-name [ var-name ]
           [ ( field-name-list ) ] enforcement ::= ENFORCE INTEGRITY
    | ENFORCE ASSERTION asrt-name define-trigger ::= DEFINE TRIGGER trig-name
    ON trig-condition : (statement-list) trig-condition ::= action
    | READ OF table-name [ var-name ] statement-list ::= statement
    | statement-list ; statement grant ::= GRANT [ auth ] table-name TO user-list
    [ WITH GRANT OPTION ] auth ::= ALL RIGHTS ON
    | operation-list ON
    | ALL BUT operation-list ON user-list ::= user-name
    | user-list , user-name
    | PUBLIC operation-list ::= operation
    | operation-list , operation operation ::= READ
    | INSERT
    | DELETE
    | UPDATE [ (field-name-list) ]
    | DROP
    | EXPAND
    | IMAGE
    | LINK
    | CONTROL revoke ::= REVOKE [ operation-list ON ] table-name
    FROM user-list
```
