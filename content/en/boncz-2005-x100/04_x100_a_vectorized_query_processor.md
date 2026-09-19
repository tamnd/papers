---
paper: boncz-2005-x100
title: 'MonetDB/X100: Hyper-Pipelining Query Execution'
authors:
  - Peter Boncz
  - Marcin Zukowski
  - Niels Nes
year: 2005
venue: CIDR
field: databases
section: "4"
section_title: 'X100: A Vectorized Query Processor'
tag: "0773"
kind: section
lang: en
source: https://www.cidrdb.org/cidr2005/papers/P19.pdf
pdf_sha256: c509153c876aee8706e298d43e2fa93ade2696cc3102643b439af0f508bb52fc
pdf_pages: 7-10
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: d842626199b0276583c715cd0aea8ce884635735edf4af3ce86393597cc5dc56
edited: true
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The goal of X100 is to (i) execute high-volume queries at high CPU efficiency, (ii) be extensible to other application domains like data mining and multi-media retrieval, and achieve those same high efficiencies on extensibility code, and (iii) scale with the size of the lowest storage hierarchy (disk).

In order to achieve our goals, X100 must fight bottlenecks throughout the entire computer architecture:

Disk the ColumnBM I/O subsystem of X100 is geared towards efficient sequential data access. To reduce bandwidth requirements, it uses a vertically fragmented data layout, that in some cases is enhanced with lightweight data compression.

RAM like I/O, RAM access is carried out through explicit memory-to-cache and cache-to-memory routines (which contain platform-specific optimizations, sometimes including e.g. SSE prefetching and data movement assembly instructions). The same vertically partitioned and even compressed disk data layout is used in RAM to save space and bandwidth.

Cache we use a Volcano-like execution pipeline based on a vectorized processing model. Small (e.g. 1000 values) vertical chunks of cache-resident data items, called “vectors” are the unit of operation for X100 execution primitives. The CPU cache is the only place where bandwidth does not matter, and therefore (de)compression happens on the boundary between RAM and cache. The X100 query processing operators should be cache-conscious and fragment huge datasets efficiently into cache-chunks and perform random data access only there.

CPU vectorized primitives expose to the compiler that processing a tuple is independent of the previous and next tuples. Vectorized primitives for projections (expression calculation) do this easily, but we try to achieve the same for other query processing operators as well (e.g. aggregation). This allows compilers to produce efficient loop-pipelined code. To improve the CPU throughput further (mainly by reducing the number of load/stores in the instruction mix), X100 contains facilities to compile vectorized primitives for whole expression sub-trees rather than single functions. Currently, this compilation is statically steered, but it may eventually become a run-time activity mandated by an optimizer.

To maintain focus in this paper, we only summarily describe disk storage issues, also because the ColumnBM buffer manager is still under development. In all our experiments, X100 uses MonetDB as its storage manager (as shown in Figure 5), where it operates on in-memory BATs.

Figure.

Figure 5: X100 Software Architecture {#boncz-2005-x100-fig-5 .figure tag=0774}

### 4.1 Query Language {#boncz-2005-x100-s4-1 .section tag=0775}

X100 uses a rather standard relational algebra as query language. We departed from the column-at-a-time MIL language so that the relational operators can process (vectors of) multiple columns at the same time, allowing to use a vector produced by one expression as the input to another, while the data is in the CPU cache.

### 4.1.1 Example {#boncz-2005-x100-s4-1-1 .section tag=0776}

To demonstrate the behavior of MonetDB/X100, Figure 6 presents the execution of a simplified version of a TPC-H Query 1, with the following X100 relational algebra syntax:

Aggr(
    Project(
        Select(

Table(lineitem),
< (shipdate, date('1998-09-03'))>,
[ discountprice = *( -(flt('1.0'), discount),
extendedprice) ]),
[ returnflag ],
[ sum_disc_price = sum(discountprice) ])

Execution proceeds using Volcano-like pipelining, on the granularity of a vector (e.g. 1000 values). The Scan operator retrieves data vector-at-a-time from Monet BATs. Note that only attributes relevant to the query are actually scanned.

A second step is the Select operator, which creates a selection-vector, filled with positions of tuples that match our predicate. Then the Project operator is executed to calculate expressions needed for the final aggregation. Note that ”discount” and ”extendedprice” columns are not modified during selection. Instead, the selection-vector is taken into account by map-primitives to perform calculations only for relevant tuples, writing results at the same positions in the output vector as they were in the input one. This behavior requires propagating of the selection-vector to the final Aggr. There, for each tuple its position in the hash table is calculated, and then, using this data, aggregate results are updated. Additionally, for the new elements in the hash table, values of the grouping attribute are saved. The contents of the hash-table becomes available as the query result as soon as the underlying operators become exhausted and cannot produce more vectors.

### 4.1.2 X100 Algebra {#boncz-2005-x100-s4-1-2 .section tag=0777}

Figure 7 lists the currently supported X100 algebra operators. In X100 algebra, a Table is a materialized relation, whereas a Dataflow just consists of tuples flowing through a pipeline.

Order, TopN and Select return a Dataflow with the same shape as its input. The other operators define a Dataflow with a new shape. Some peculiarities of this algebra are that Project is just used for expression calculation; it does not eliminate duplicates. Duplicate elimination can be performed using an Aggr with only group-by columns. The Array operator generates a Dataflow representing a N-dimensional array as an N-ary relation containing all valid array index coordinates in column-major dimension order. It is used by the RAM array manipulation front-end for the MonetDB system [9].

Aggregation is supported by three physical operators: (i) direct aggregation, (ii) hash aggregation, and (iii) ordered aggregation. The latter is chosen if all group-members will arrive right after each other in the source Dataflow. Direct aggregation can be used for small datatypes where the bit-representation is limited to a known (small) domain, similar to the way aggregation was handled in the “hand-coded” solution (Section 3.3). In all other cases, hash-aggregation is used.

Figure.

Figure 6: Execution scheme of a simplified TPC-H Query 1 in MonetDB/X100 {#boncz-2005-x100-fig-6 .figure tag=0778}

X100 currently only supports left-deep joins. The default physical implementation is a CartProd operator with a Select on top (i.e. nested-loop join). If X100 detects a foreign-key condition in a join condition, and a join-index is available, it exploits it with a Fetch1Join or FetchNJoin.

The inclusion of these fetch-joins in X100 is no coincidence. In MIL, the “positional-join” of an oid into a void column has proven valuable on vertically fragmented data stored in dense columns. Positional joins allow dealing with the “extra” joins needed for vertical fragmentation in a highly efficient way [4]. Just like the void type in MonetDB, X100 gives each table a virtual #rowId column, which is just a densely ascending number from 0. The Fetch1Join allows to positionally fetch column values by #rowId.

### 4.2 Vectorized Primitives {#boncz-2005-x100-s4-2 .section tag=0779}

The primary reason for using the column-wise vector layout is not to optimize memory layout in the cache (X100 is supposed to operate on cached data anyway). Rather, vectorized execution primitives have the advantage of a low degree of freedom (as discussed in Section 3.2). In a vertically fragmented data model, the execution primitives only know about the columns they operate on without having to know about the overall table layout (e.g. record offsets). When compiling X100, the C compiler sees that the X100 *vectorized primitives* operate on restricted (independent) arrays of fixed shape. This allows it to apply aggressive loop pipelining, critical for modern CPU performance (see Section 2). As an example, we show the (generated) code for vectorized floating-point addition:

```text
Table(ID) : Table  +(double*, double*) +(double, double*) +(double*, double) +(double, double)
Scan(Table) : Dataflow
Array(List>>) : Dataflow
Select(Dataflow, Exp) : Dataflow
Join(Dataflow, Table, Exp, List) : Dataflow CartProd(Dataflow, Table, List) Fetch1Join(Dataflow, Table, Exp, List) FetchNJoin(Dataflow, Table, Exp, Exp, Column, List)
Project(Dataflow, List>) : Dataflow
Aggr(Dataflow, List>, List) : Dataflow OrdAggr(Dataflow, List>, List) DirectAggr(Dataflow, List>, List) HashAggr(Dataflow, List>, List])
TopN(Dataflow, List, List>, int):Dataflow
Order(Table, List, List) : Table
```

Figure 7: X100 Query Algebra {#boncz-2005-x100-fig-7 .figure tag=077A}

```text
map_plus_double_col_double_col(int n,
    double*__restrict__ res,
    double*__restrict__ col1, double*__restrict__ col2,
    int*__restrict__ sel)
{
    if (sel) {
        for(int j=0;j<n; j++) {
            int i = sel[j];
            res[i] = col1[i] + col2[i];
        }
    } else {
        for(int i=0;i<n; i++)
            res[i] = col1[i] + col2[i];
    }
}
```

The sel parameter may be NULL or point to an array of n selected array positions (i.e. the “selection-vector” from Figure 6). All X100 vectorized primitives allow passing such selection vectors. The rationale is that after a selection, leaving the vectors delivered by the child operator intact is often quicker than copying all selected data into new (contiguous) vectors.

X100 contains hundreds of vectorized primitives. These are not written (and maintained) by hand, but are *generated* from *primitive patterns*. The primitive pattern for addition is:

any::1 +(any::1 x,any::1 y) plus = x + y

This pattern states that an addition of two values of the same type (but without any type restriction) is implemented in C by the infix operator +. It produces a result of the same type, and the name identifier should be plus. Type-specific patterns later in the specification file may override this pattern (e.g. str +(str x,str y) concat = str_concat(x,y)).

The other part of primitive generation is a file with *map signature requests*:

This requests to generate all possible combinations of addition between single values and columns (the latter identified with an extra *). Other extensible RDBMSs often only allow UDFs with single-value parameters [19]. This inhibits loop pipelining, reducing performance (see Section 3.1).⁴

We can also request *compound primitive* signatures:

/(square(-(double*, double*)), double*)

The above signature is the Mahanalobis distance, a performance-critical operation for some multi-media retrieval tasks [9]. We found that the compound primitives often perform twice as fast as the single-function vectorized primitives. Note that this factor 2 is similar to the difference between MonetDB/X100 and the hand-coded implementation of TPC-H Query in Table 1. The reason why compound primitives are more efficient is a better instruction mix. Like in the example with addition on the MIPS processor in Section 3.1, vectorized execution often becomes load/store bound, because for simple 2-ary calculations, each vectorized instruction requires loading two parameters and storing one result (1 work instruction, 3 memory instructions). Modern CPUs can typically only perform 1 or 2 load/store operations per cycle. In compound primitives, the results from one calculation are passed via a CPU register to the next calculation, with load/stores only occurring at the edges of the expression graph.

Currently, the *primitive generator* is not much more than a macro expansion script in the make sequence of the X100 system. However, we intend to implement dynamic compilation of compound primitives as mandated by an optimizer.

A slight variation on the map primitives are the select_* primitives (see also Figure 2). These only exist for code patterns that return a boolean. Instead of producing a full result vector of booleans (as the map does), the select primitives fill a result array of selected vector positions (integers), and return the total number of selected tuples.

Similarly, there are the aggr_* primitives that calculate aggregates like count, sum, min, and max. For each, an initialization, an update, and an epilogue pattern need to be specified. The primitive generator then generates the relevant routines for the various implementations of aggregation in X100.

The X100 mechanism of allowing database extension developers to provide (source-)code patterns instead of compiled code, allows all ADTs to get first-class-citizen treatment during query execution. This was also a weak point of MIL (and most extensible DBMSs [19]), as its main algebraic operators were only optimized for the built-in types.

⁴If X100 is used in resource-restricted environments, the size of the X100 binary (less than a MB now) could be further reduced by omitting the column-versions of (certain) execution primitives. X100 will still be able to process those primitives although more slowly, with a vector size of 1.

### 4.3 Data Storage {#boncz-2005-x100-s4-3 .section tag=077B}

MonetDB/X100 stores all tables in vertically fragmented form. The storage scheme is the same whether the new ColumnBM buffer manager is used, or MonetDB BAT[void,T] storage. While MonetDB stores each BAT in a single contiguous file, ColumnBM partitions those files in large (>1MB) chunks.

A disadvantage of vertical storage is an increased update cost: a single row update or delete must perform one I/O for each column. MonetDB/X100 circumvents this by treating the vertical fragments as immutable objects. Updates go to delta structures instead. Figure 8 shows that deletes are handled by adding the tuple ID to a deletion list, and that inserts lead to appends in separate *delta columns*. ColumnBM actually stores all delta columns together in a chunk, which equates PAX [2]. Thus, both operations incur only one I/O. Updates are simply a deletion followed by an insertion. Updates make the delta columns grow, such that whenever their size exceeds a (small) percentile of the total table size, data storage should be reorganized, such that the vertical storage is up-to-date again and the delta columns are empty.

An advantage of vertical storage is that queries that access many tuples but not all columns save bandwidth (this holds both for RAM bandwidth and I/O bandwidth). We further reduce bandwidth requirements using *lightweight compression*. MonetDB/X100 supports *enumeration types*, which effectively store a column as a single-byte or two-byte integer. This integer refers to #rowId of a mapping table. MonetDB/X100 automatically adds a Fetch1Join operation to retrieve the uncompressed value using the small integer when such columns are used in a query. Notice that since the vertical fragments are immutable, updates just go to the delta columns (which are never compressed) and do not complicate the compression scheme.

MonetDB/X100 also supports simple “summary” indices, similar to [12], which are used if a column is clustered (almost sorted). These summary indices contain a #rowId, the running maximum value of the column until that point in the base table, and a reversely running minimum at a very coarse granularity (the default size is 1000 entries, with #rowids taken with fixed intervals from the base table). These summary indices can be used to quickly derive #rowId bounds for range predicates. Notice again, due to the property that vertical fragments are immutable, indices on them effectively require no maintenance. The delta columns, which are supposed to be small and in-memory, are not indexed and must always be accessed.

delete from TABLE where key=F    insert into TABLE values (K,d,m)

| shipmod |  |  | shipmod |  |  | shipmod |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| key | flag | #del | key | flag | #del | key | flag | #del |
| #0 A | a | m | #0 A | a | m | #0 A | a | m |
| #1 B | a | m | #1 B | a | m | #1 B | a | m |
| #2 C | a | m | #2 C | a | m | #2 C | a | m |
| #3 D | b | s | #3 D | b | s | #3 D | b | s |
| #4 E | d | s | #4 E | d | s | #4 E | d | s |
| #5 F | c | s | #5 F | c | s | #5 F | c | s |
| #6 G | f | s | #6 G | f | s | #6 G | f | s |
| #7 H | e | a | #7 H | e | a | #7 H | e | a |
| #8 I | e | a | #8 I | e | a | #8 I | e | a |
| #9 J | c | a | #9 J | c | a | #9 J | c | a |

leave the column storage blocks untouched on updates buffer manager blocks

#10 K d m

Figure 8: Vertical Storage and Updates {#boncz-2005-x100-fig-8 .figure tag=077C}
