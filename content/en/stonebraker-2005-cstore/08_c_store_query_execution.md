---
paper: stonebraker-2005-cstore
title: 'C-Store: A Column-oriented DBMS'
authors:
  - Mike Stonebraker
  - Daniel J. Abadi
  - Adam Batkin
  - Xuedong Chen
  - Mitch Cherniack
  - Miguel Ferreira
  - Edmond Lau
  - Amerson Lin
  - Sam Madden
  - Elizabeth O'Neil
  - Pat O'Neil
  - Alex Rasin
  - Nga Tran
  - Stan Zdonik
year: 2005
venue: VLDB
field: databases
section: "8"
section_title: C-Store Query Execution
tag: "0765"
kind: section
lang: en
source: https://www.vldb.org/archives/website/2005/program/paper/thu/p553-stonebraker.pdf
pdf_sha256: c619eacc696c847e0d7697edb9193a2c35f242b12ac2835f486970a07129eecb
pdf_pages: "9"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 12aa08abd29d01dff7c0d2e0b20baa86c493d98e84d8f351e45384c1544a2d8f
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The query optimizer will accept a SQL query and construct a query plan of execution nodes. In this section, we describe the nodes that can appear in a plan and then the architecture of the optimizer itself.

### 8.1 Query Operators and Plan Format {#stonebraker-2005-cstore-s8-1 .section tag=0766}

There are 10 node types and each accepts operands or produces results of type projection (Proj), column (Col), or bitstring (Bits). A projection is simply a set of columns with the same cardinality and ordering. A bitstring is a list of zeros and ones indicating whether the associated values are present in the record subset being described. In addition, C-Store query operators accept predicates (Pred), join indexes (JI), attribute names (Att), and expressions (Exp) as arguments.

Join indexes and bitstrings are simply special types of columns. Thus, they also can be included in projections and used as inputs to operators where appropriate.

We briefly summarize each operator below.
1. Decompress converts a compressed column to an uncompressed (Type 4) representation.
2. Select is equivalent to the selection operator of the relational algebra ($\sigma$), but rather than producing a restriction of its input, instead produces a bitstring representation of the result.
3. Mask accepts a bitstring B and projection Cs, and restricts Cs by emitting only those values whose corresponding bits in B are 1.
4. Project equivalent to the projection operator of the relational algebra ($\pi$).
5. Sort sorts all columns in a projection by some subset of those columns (the sort columns).
6. Aggregation Operators compute SQL-like aggregates over a named column, and for each group identified by the values in a projection.
7. Concat combines one or more projections sorted in the same order into a single projection
8. Permute permutes a projection according to the ordering defined by a join index.
9. Join joins two projections according to a predicate that correlates them.
10. Bitstring Operators BAnd produces the bitwise AND of two bitstrings. BOr produces a bitwise OR. BNot produces the complement of a bitstring.

A C-Store query plan consists of a tree of the operators listed above, with access methods at the leaves and iterators serving as the interface between connected nodes. Each non-leaf plan node consumes the data produced by its children via a modified version of the standard iterator interface [GRAE93] via calls of “get_next.” To reduce communication overhead (i.e., number of calls of “get_next”) between plan nodes, C-Store iterators return 64K blocks from a single column. This approach preserves the benefit of using iterators (coupling data flow with control flow), while changing the granularity of data flow to better match the column-based model.

### 8.2 Query Optimization {#stonebraker-2005-cstore-s8-2 .section tag=0767}

We plan to use a Selinger-style [SELI79] optimizer that uses cost-based estimation for plan construction. We anticipate using a two-phase optimizer [HONG92] to limit the complexity of the plan search space. Note that query optimization in this setting differs from traditional query optimization in at least two respects: the need to consider compressed representations of data and the decisions about when to mask a projection using a bitstring.

C-Store operators have the capability to operate on both compressed and uncompressed input. As will be shown in Section 9, the ability to process compressed data is the key to the performance benefits of C-Store. An operator’s execution cost (both in terms of I/O and memory buffer requirements) is dependent on the compression type of the input. For example, a Select over Type 2 data (foreign order/few values, stored as a delta-encoded bitmaps, with one bitmap per value) can be performed by reading only those bitmaps from disk whose values match the predicate (despite the column itself not being sorted). However, operators that take Type 2 data as input require much larger memory buffer space (one page of memory for each possible value in the column) than any of the other three types of compression. Thus, the cost model must be sensitive to the representations of input and output columns.

The major optimizer decision is which set of projections to use for a given query. Obviously, it will be time consuming to construct a plan for each possibility, and then select the best one. Our focus will be on pruning this search space. In addition, the optimizer must decide where in the plan to mask a projection according to a bitstring. For example, in some cases it is desirable to push the Mask early in the plan (e.g., to avoid producing a bitstring while performing selection over Type 2 compressed data) while in other cases it is best to delay masking until a point where it is possible to feed a bitstring to the next operator in the plan (e.g., COUNT) that can produce results solely by processing the bitstring.
