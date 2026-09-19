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
section: "2"
section_title: Data Model
tag: "0752"
kind: section
lang: en
source: https://www.vldb.org/archives/website/2005/program/paper/thu/p553-stonebraker.pdf
pdf_sha256: c619eacc696c847e0d7697edb9193a2c35f242b12ac2835f486970a07129eecb
pdf_pages: 3-5
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 4a0a082ed707b2083094a759bfc0fda0e5b19cee0e0e72ba65322443ab3a9327
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

C-Store supports the standard relational logical data model, where a database consists of a collection of named tables, each with a named collection of attributes (columns). As in most relational systems, attributes (or collections of attributes) in C-Store tables can form a unique primary key or be a foreign key that references a primary key in another table. The C-Store query language is assumed to be SQL, with standard SQL semantics. Data in C-Store is not physically stored using this logical data model. Whereas most row stores implement physical tables directly and then add various indexes to speed access, C-Store implements only projections. Specifically, a C-Store projection is anchored on a given logical table, T, and contains one or more attributes from this table. In addition, a projection can contain any number of other attributes from other tables, as long as there is a sequence of n:1 (i.e., foreign key) relationships from the anchor table to the table containing an attribute.

To form a projection, we project the attributes of interest from T, retaining any duplicate rows, and perform the appropriate sequence of value-based foreign-key joins to obtain the attributes from the non-anchor table(s). Hence, a projection has the same number of rows as its anchor table. Of course, much more elaborate projections could be allowed, but we believe this simple scheme will meet our needs while ensuring high performance. We note that we use the term projection slightly differently than is common practice, as we do not store the base table(s) from which the projection is derived.

| Name | Age | Dept | Salary |
| --- | --- | --- | --- |
| Bob | 25 | Math | 10K |
| Bill | 27 | EECS | 50K |
| Jill | 24 | Biology | 80K |

Table 1: Sample EMP data {#stonebraker-2005-cstore-tab-1 .table tag=047B}

We denote the ith projection over table t as ti, followed by the names of the fields in the projection. Attributes from other tables are prepended with the name of the logical table they come from. In this section, we consider an example for the standard EMP(name, age, salary, dept) and DEPT(dname, floor) relations. Sample EMP data is shown in Table 1. One possible set of projections for these tables could be as shown in Example 1.

EMP1 (name, age)
EMP2 (dept, age, DEPT.floor)
EMP3 (name, salary)
DEPT1(dname, floor)

Example 1: Possible projections for EMP and DEPT {#stonebraker-2005-cstore-ex-1 .statement tag=0753}

Tuples in a projection are stored column-wise. Hence, if there are K attributes in a projection, there will be K data structures, each storing a single column, each of which is sorted on the same sort key. The sort key can be any column or columns in the projection. Tuples in a projection are sorted on the key(s) in left to right order.

We indicate the sort order of a projection by appending the sort key to the projection separated by a vertical bar. A possible ordering for the above projections would be:

EMP1(name, age| age)
EMP2(dept, age, DEPT.floor| DEPT.floor)
EMP3(name, salary| salary)
DEPT1(dname, floor| floor)

Example 2: Projections in Example 1 with sort orders {#stonebraker-2005-cstore-ex-2 .statement tag=0754}

Lastly, every projection is horizontally partitioned into 1 or more segments, which are given a segment identifier, Sid, where Sid > 0. C-Store supports only value-based partitioning on the sort key of a projection. Hence, each segment of a given projection is associated with a key range of the sort key for the projection. Moreover, the set of all key ranges partitions the key space.

Clearly, to answer any SQL query in C-Store, there must be a covering set of projections for every table in the database such that every column in every table is stored in at least one projection. However, C-Store must also be able to reconstruct complete rows of tables from the collection of stored segments. To do this, it will need to join segments from different projections, which we accomplish using storage keys and join indexes.

Storage Keys. Each segment associates every data value of every column with a storage key, SK. Values from different columns in the same segment with matching storage keys belong to the same logical row. We refer to a row of a segment using the term record or tuple. Storage keys are numbered 1, 2, 3, ... in RS and are not physically stored, but are inferred from a tuple’s physical position in the column (see Section 3 below.) Storage keys are physically present in WS and are represented as integers, larger than the largest integer storage key for any segment in RS.

Join Indices. To reconstruct all of the records in a table T from its various projections, C-Store uses join indexes. If T1 and T2 are two projections that cover a table T, a join index from the M segments in T1 to the N segments in T2 is logically a collection of M tables, one per segment, S, of T1 consisting of rows of the form:

(s: SID in T2, k: Storage Key in Segment s)

Here, an entry in the join index for a given tuple in a segment of T1 contains the segment ID and storage key of the corresponding (joining) tuple in T2. Since all join indexes are between projections anchored at the same table, this is always a one-to-one mapping. An alternative view of a join index is that it takes T1, sorted in some order O, and logically resorts it into the order, O' of T2.

In order to reconstruct T from the segments of T1, ..., Tk it must be possible to find a path through a set of join indices that maps each attribute of T into some sort order O*. A path is a collection of join indexes originating with a sort order specified by some projection, Ti , that passes through zero or more intermediate join indices and ends with a projection sorted in order O*. For example, to be able to reconstruct the EMP table from projections in Example 2, we need at least two join indices. If we choose age as a common sort order, we could build two indices that map EMP2 and EMP3 to the ordering of EMP1. Alternatively, we could create a join index that maps EMP2 to EMP3 and one that maps EMP3 to EMP1. Figure 2 shows a simple example of a join index that maps EMP3 to EMP1, assuming a single segment (SID = 1) for each projection. For example, the first entry of EMP3, (Bob, 10K), corresponds to the second entry of EMP1, and thus the first entry of the join index has storage key 2.

| EMP1 |  | Join Index |  |
| --- | --- | --- | --- |
| Name | Age | SID | Key |
| Jill | 24 | 1 | 2 |
| Bob | 25 | 1 | 3 |
| Bill | 27 | 1 | 1 |

| EMP3 |  |
| --- | --- |
| Name | Salary |
| Bob | 10K |
| Bill | 50K |
| Jill | 80K |

Figure 2: A join index from EMP3 to EMP1. {#stonebraker-2005-cstore-fig-2 .figure tag=0755}

In practice, we expect to store each column in several projections, thereby allowing us to maintain relatively few join indices. This is because join indexes are very expensive to store and maintain in the presence of updates, since each modification to a projection requires every join index that points into or out of it to be updated as well.

The segments of the projections in a database and their connecting join indexes must be allocated to the various nodes in a C-Store system. The C-Store administrator can optionally specify that the tables in a database must be K-safe. In this case, the loss of K nodes in the grid will still allow all tables in a database to be reconstructed (i.e., despite the K failed sites, there must exist a covering set of projections and a set of join indices that map to some common sort order.) When a failure occurs, C-Store simply continues with K-1 safety until the failure is repaired and the node is brought back up to speed. We are currently working on fast algorithms to accomplish this.

Thus, the C-Store physical DBMS design problem is to determine the collection of projections, segments, sort keys, and join indices to create for the collection of logical tables in a database. This physical schema must give K-safety as well as the best overall performance for a given training workload, provided by the C-Store administrator, subject to requiring no more than a given space budget, B. Additionally, C-Store can be instructed to keep a log of all queries to be used periodically as the training workload. Because there are not enough skilled DBAs to go around, we are writing an automatic schema design tool. Similar issues are addressed in [PAPA04]

We now turn to the representation of projections, segments, storage keys, and join indexes in C-Store.
