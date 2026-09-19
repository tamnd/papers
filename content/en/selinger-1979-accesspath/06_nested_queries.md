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
section: "6"
section_title: Nested Queries
tag: 071E
kind: section
lang: en
source: https://doi.org/10.1145/582095.582099
pdf_sha256: d8c02d475b49fc90b9ee2b9e15a686a320b4b537272b8a5a661642db6c800d13
pdf_pages: 11-12
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: efdd4a73994f8d71acd4b012c88774f4cce1df9b32a01cdbafba1e4ea0a160ca
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

A query may appear as an operand of a predicate of the form "expression operator query". Such a query is called a Nested Query or a Subquery. If the operator is one of the six scalar comparisons (=, !=, >, >=, <, <=), then the subquery must return a single value. The following example using the "=" operator was given in section 2:

SELECT NAME
FROM EMPLOYEE
WHERE SALARY =
    (SELECT AVG(SALARY)
        FROM EMPLOYEE)
If the operator is IN or NOT IN then the subquery may return a set of values. For example:

SELECT NAME
FROM EMPLOYEE
WHERE DEPARTMENT_NUMBER IN
    (SELECT DEPARTMENT_NUMBER
        FROM DEPARTMENT
        WHERE LOCATION='DENVER')

In both examples, the subquery needs to be evaluated only once. The OPTIMIZER will arrange for the subquery to be evaluated before the top level query is evaluated. If a single value is returned, it is incorporated into the top level query as though it had been part of the original query statement; for example, if AVG(SAL) above evaluates to 15000 at execution time, then the predicate becomes "SALARY = 15000". If the subquery can return a set of values, they are returned in a temporary list, an internal form which is more efficient than a relation but which can only be accessed sequentially. In the example above, if the subquery returns the list (17,24) then the predicate is evaluated in a manner similar to the way in which it would have been evaluated if the original predicate had been DEPARTMENT_NUMBER IN (17,24).

A subquery may also contain a predicate with a subquery, down to a (theoretically) arbitrary level of nesting. When such subqueries do not reference columns from tables in higher level query blocks, they are all evaluated before the top level query is evaluated. In this case, the most deeply nested subqueries are evaluated first, since any subquery must be evaluated before its parent query can be evaluated.

A subquery may contain a reference to a value obtained from a candidate tuple of a higher level query block (see example below). Such a query is called a correlation subquery. A correlation subquery must in principle be re-evaluated for each candidate tuple from the referenced query block. This re-evaluation must be done before the correlation subquery's parent predicate in the higher level block can be tested for acceptance or rejection of the candidate tuple. As an example, consider the query:

SELECT NAME
FROM EMPLOYEE X
WHERE SALARY > (SELECT SALARY
    FROM EMPLOYEE
    WHERE EMPLOYEE_NUMBER=
        X.MANAGER)

This selects names of EMPLOYEE's that earn more than their MANAGER. Here X identifies the query block and relation which furnishes the candidate tuple for the correlation. For each candidate tuple of the top level query block, the MANAGER value is used for evaluation of the subquery. The subquery result is then returned to the "SALARY >" predicate for testing acceptance of the candidate tuple.

If a correlation subquery is not directly below the query block it references but is separated from that block by one or more intermediate blocks, then the correlation subquery evaluation will be done before evaluation of the highest of the intermediate blocks. For example:

level 1   SELECT NAME
           FROM EMPLOYEE X
           WHERE SALARY >
level 2   (SELECT SALARY
           FROM EMPLOYEE
           WHERE EMPLOYEE-NUMBER =
level 3   (SELECT MANAGER
           FROM EMPLOYEE
           WHERE EMPLOYEE-NUMBER =
               X.MANAGER))

This selects names of EMPLOYEE's that earn more than their MANAGER's MANAGER. As before, for each candidate tuple of the level-1 query block, the EMPLOYEE.MANAGER value is used for evaluation of the level-3 query block. In this case, because the level 3 subquery references a level 1 value but does not reference level 2 values, it is evaluated once for every new level 1 candidate tuple, but not for every level 2 candidate tuple.

If the value referenced by a correlation subquery (X.MANAGER above) is not unique in the set of candidate tuples (e.g., many employees have the same manager), the procedure given above will still cause the subquery to be re-evaluated for each occurrence of a replicated value. However, if the referenced relation is ordered on the referenced column, the re-evaluation can be made conditional, depending on a test of whether or not the current referenced value is the same as the one in the previous candidate tuple. If they are the same, the previous evaluation result can be used again. In some cases, it might even pay to sort the referenced relation on the referenced column in order to avoid re-evaluating subqueries unnecessarily. In order to determine whether or not the referenced column values are unique. the OPTIMIZER can use clues like NCARD > ICARD, where NCARD is the relation cardinality and ICARD is the index cardinality of an index on the referenced column.
