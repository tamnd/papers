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
section: "4"
section_title: Costs for single relation access paths
tag: 046C
kind: section
lang: en
source: https://doi.org/10.1145/582095.582099
pdf_sha256: d8c02d475b49fc90b9ee2b9e15a686a320b4b537272b8a5a661642db6c800d13
pdf_pages: 3-5
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: fb7181557ba50689307648a0cdc200fca5873f22c77448a64a9fab844246a6b7
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

In the next several sections we will describe the process of choosing a plan for evaluating a query. We will first describe the simplest case, accessing a single relation, and show how it extends and generalizes to 2-way joins of relations, n-way joins, and finally multiple query blocks (nested queries).

The OPTIMIZER examines both the predicates in the query and the access paths available on the relations referenced by the query, and formulates a cost prediction for each access plan, using the following cost formula:

$$
COST = PAGE\ FETCHES + W * (RSI\ CALLS).
$$

This cost is a weighted measure of I/O (pages fetched) and CPU utilization (instructions executed). $W$ is an adjustable weighting factor between I/O and CPU. $RSI\ CALLS$ is the predicted number of tuples returned from the RSS. Since most of System R's CPU time is spent in the RSS, the number of RSI calls is a good approximation for CPU utilization. Thus the choice of a minimum cost path to process a query attempts to minimize total resources required.

During execution of the type-compatibility and semantic checking portion of the OPTIMIZER, each query block's WHERE tree of predicates is examined. The WHERE tree is considered to be in conjunctive normal form, and every conjunct is called a boolean factor. Boolean factors are notable because every tuple returned to the user must satisfy every boolean factor. An index is said to match a boolean factor if the boolean factor is a sargable predicate whose referenced column is the index key; e.g., an index on SALARY matches the predicate 'SALARY = 20000'. More precisely, we say that a predicate or set of predicates matches an index access path when the predicates are sargable and the columns mentioned in the predicate(s) are an initial substring of the set of columns of the index key. For example, a NAME, LOCATION index matches NAME = 'SMITH' AND LOCATION = 'SAN JOSE'. If an index matches a boolean factor, an access using that index is an efficient way to satisfy the boolean factor. Sargable boolean factors can also be efficiently satisfied if they are expressed as search arguments. Note that a boolean factor may be an entire tree of predicates headed by an OR.

During catalog lookup, the OPTIMIZER retrieves statistics on the relations in the query and on the access paths available on each relation. The statistics kept are the following:

For each relation T,
- NCARD(T), the cardinality of relation T.
- TCARD(T), the number of pages in the segment that hold tuples of relation T.
- P(T), the fraction of data pages in the segment that hold tuples of relation T. $P(T) = TCARD(T) /$ (no. of non-empty pages in the segment).

For each index I on relation T,
- ICARD(I), number of distinct keys in index I.
- NINDX(I), the number of pages in index I.

These statistics are maintained in the System R catalogs, and come from several sources. Initial relation loading and index creation initialize these statistics. They are then updated periodically by an UPDATE STATISTICS command, which can be run by any user. System R does not update these statistics at every INSERT, DELETE, or UPDATE because of the extra database operations and the locking bottleneck this would create at the system catalogs. Dynamic updating of statistics would tend to serialize accesses that modify the relation contents.

Using these statistics, the OPTIMIZER assigns a selectivity factor 'F' for each boolean factor in the predicate list. This selectivity factor very roughly corresponds to the expected fraction of tuples which will satisfy the predicate. TABLE 1 gives the selectivity factors for different kinds of predicates. We assume that a lack of statistics implies that the relation is small, so an arbitrary factor is chosen.

Query cardinality (QCARD) is the product of the cardinalities of every relation in the query block's FROM list times the product of all the selectivity factors of that

| TABLE 1 |  | SELECTIVITY FACTORS |
| --- | --- | --- |
| column = value F = 1 / ICARD(column index) if there is an index on column This assumes an even distribution of tuples among the index key values. F = 1/10 otherwise |  |  |
| column1 = column2 F = 1/MAX(ICARD(column1 index), ICARD(column2 index)) if there are indexes on both column1 and column2 This assumes that each key value in the index with the smaller cardinality has a matching value in the other index. F = 1/ICARD(column-i index) if there is only an index on column-i F = 1/10 otherwise |  |  |
| column > value (or any other open-ended comparison) F = (high key value - value) / (high key value - low key value) Linear interpolation of the value within the range of key values yields F if the column is an arithmetic type and value is known at access path selection time. F = 1/3 otherwise (i.e. column not arithmetic) There is no significance to this number, other than the fact that it is less selective than the guesses for equal predicates for which there are no indexes, and that it is less than 1/2. We hypothesize that few queries use predicates that are satisfied by more than half the tuples. |  |  |
| column BETWEEN value1 AND value2 F = (value2 - value1) / (high key value - low key value) A ratio of the BETWEEN value range to the entire key value range is used as the selectivity factor if column is arithmetic and both value1 and value2 are known at access path selection. F = 1/4 otherwise Again there is no significance to this choice except that it is between the default selectivity factors for an equal predicate and a range predicate. |  |  |
| column IN (list of values) F = (number of items in list) * (selectivity factor for column = value) This is allowed to be no more than 1/2. |  |  |
| columnA IN subquery F = (expected cardinality of the subquery result) / (product of the cardinalities of all the relations in the subquery’s FROM-list). The computation of query cardinality will be discussed below. This formula is derived by the following argument: Consider the simplest case, where subquery is of the form “SELECT columnB FROM relationC ...”. Assume that the set of all columnB values in relationC contains the set of all columnA values. If all the tuples of relationC are selected by the subquery, then the predicate is always TRUE and F = 1. If the tuples of the subquery are restricted by a selectivity factor F’, then assume that the set of unique values in the subquery result that match columnA values is proportionately restricted, i.e. the selectivity factor for the predicate should be F’. F’ is the product of all the subquery’s selectivity factors, namely (subquery cardinality) / (cardinality of all possible subquery answers). With a little optimism, we can extend this reasoning to include subqueries which are joins and subqueries in which columnB is replaced by an arithmetic expression involving column names. This leads to the formula given above. |  |  |
| (pred expression1) OR (pred expression2) F = F(pred1) + F(pred2) - F(pred1) * F(pred2) |  |  |
| (pred1) AND (pred2) F = F(pred1) * F(pred2) Note that this assumes that column values are independent. |  |  |
| NOT pred F = 1 - F(pred) |  |  |

query block’s boolean factors. The number of expected RSI calls (RSICARD) is the product of the relation cardinalities times the selectivity factors of the sargable boolean factors, since the sargable boolean factors will be put into search arguments which will filter out tuples without returning across the RSS interface.

Choosing an optimal access path for a single relation consists of using these selectivity factors in formulas together with the statistics on available access paths. Before this process is described, a definition is needed. Using an index access path or sorting tuples produces tuples in the index value or sort key order. We say that a tuple order is an interesting order if that order is one specified by the query block’s GROUP BY or ORDER BY clauses.

For single relations, the cheapest access path is obtained by evaluating the cost for each available access path (each index on the relation, plus a segment scan). The costs will be described below. For each such access path, a predicted cost is computed along with the ordering of the tuples it will produce. Scanning along the SALARY index in ascending order, for example, will produce some cost C and a tuple order of SALARY (ascending). To find the cheapest access plan for a single relation query, we need only to examine the cheapest access path which produces tuples in each “interesting” order and the cheapest “unordered” access path. Note that an “unordered” access path may in fact produce tuples in some order, but the order is not “interesting”. If there are no GROUP BY or ORDER BY clauses on the query, then there will be no interesting orderings, and the cheapest access path is the one chosen. If there are GROUP BY or ORDER BY clauses, then the cost for producing that interesting ordering must be compared to the cost of the cheapest unordered path plus the cost of sorting QCARD tuples into the proper order. The cheapest of these alternatives is chosen as the plan for the query block.

The cost formulas for single relation access paths are given in TABLE 2. These formulas give index pages fetched plus data pages fetched plus the weighting factor times RSI tuple retrieval calls. W is the weighting factor between page fetches and RSI calls. Some situations give several alternative formulas depending on whether the set of tuples retrieved will fit entirely in the RSS buffer pool (or effective buffer pool per user). We assume for clustered indexes that a page remains in the buffer long enough for every tuple to be retrieved from it. For non-clustered indexes, it is assumed that for those relations not fitting in the buffer, the relation is sufficiently large with respect to the buffer size that a page fetch is required for every tuple retrieval.
