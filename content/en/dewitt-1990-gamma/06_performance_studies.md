---
paper: dewitt-1990-gamma
title: The Gamma Database Machine Project
authors:
  - David J. DeWitt
  - Shahram Ghandeharizadeh
  - Donovan A. Schneider
  - Allan Bricker
  - Hui-I Hsiao
  - Rick Rasmussen
year: 1990
venue: IEEE Transactions on Knowledge and Data Engineering
field: databases
section: "6"
section_title: Performance Studies
tag: "0275"
kind: section
lang: en
source: http://db.cs.berkeley.edu/cs286/papers/gamma-tkde1990.pdf
pdf_sha256: 420d33f44b8e050f33517cdff1299a58838b4ad826d80a6617200332ea02be5e
pdf_pages: 23-34
extraction: vision
extraction_model: gpt-5
content_sha256: 44b46d758a0a7f9e6df90fa280db25c00920503a6bf1ab01e6a9a5887e6100e3
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

### 6.1. Introduction and Experiment Overview {#dewitt-1990-gamma-s6-1 .section tag=0276}

To evaluate the performance of the hypercube version of Gamma three different metrics were used. First, the set of Wisconsin [BITT83] benchmark queries were run on a 30 processor configuration using three different sizes of relations: 100,000, 1 million, and 10 million tuples. While absolute performance is one measure of a database system, speedup and scaleup are also useful metrics for multiprocessor database machines [ENGL89]. Speedup is an interesting metric because it indicates whether additional processors and disks results in a corresponding decrease in the response time for a query. For a subset of the Wisconsin benchmark queries, we conducted speedup experiments by varying the number of processors from 1 to 30 while the size of the test relations was fixed at 1 million tuples. For the same set of queries, we also conducted scaleup experiments by varying the number of processors from 5 to 30 while the size of the test relations was increased from 1 to 6 million tuples, respectively. Scaleup is a valuable metric as it indicates whether a constant response time can be maintained as the workload is increased by adding a proportional number of processors and disks. [ENGL89] describes a similar set of tests on Release 2 of Tandem’s NonStop SQL system.

The benchmark relations used for the experiments were based on the standard Wisconsin Benchmark relations [BITT83]. Each relation consists of tuples that are 208 bytes wide. We constructed 100,000, 1 million, and 10 million tuple versions of the benchmark relations. Two copies of each relation were created and loaded. Except where noted otherwise, tuples were declustered by hash partitioning on the Unique1 attribute. In all cases, the results presented represent the average response time of a number of equivalent queries. Gamma was configured to use a disk page size of 8K bytes and a buffer pool of 2 megabytes.

The results of all queries were stored in the database. We avoided returning data to the host in order to avoid having the speed of the communications link between the host and the database machine or the host processor itself affect the results. By storing the result relations in the database, the impact of these factors was minimized - at the expense of incurring the cost of declustering and storing the result relations.

### 6.2. Selection Queries {#dewitt-1990-gamma-s6-2 .section tag=0277}

### Performance Relative to Relation Size {#dewitt-1990-gamma-s-performance-relative-to-relation-size .section tag=0278}

The first set of selection tests were designed to determine how Gamma would respond as the size of the source relations was increased while the machine configuration was kept at 30 processors with disks. Ideally, the response time of a query should grow as a linear function of the size of input and result relations. For these tests six different selection queries were run on three sets of relations containing, respectively, 100,000, 1 million, and 10 million tuples. The first two queries have a selectivity factor of 1% and 10% and do not employ any indices. The third and fourth queries have the same selectivity factors but use a clustered index to locate the qualifying tuples. The fifth query has a selectivity factor of 1% and employs a non-clustered index to locate the desired tuples. There is no 10% selection through a non-clustered index query as the Gamma query optimizer chooses to use a sequential scan for this query. The last query uses a clustered index to retrieve a single tuple. Except for the last query, the predicate of each query specifies a range of values and, thus, since the input relations were declustered by hashing, the query must be sent to all the nodes.

The results from these tests are tabulated in Table 3. For the most part, the execution time for each query scales as a fairly linear function of the size of the input and output relations. There are, however, several cases where the scaling is not perfectly linear. Consider, first the 1% non-indexed selection. While the increase in response time as the size of the input relation is increased from 1 to 10 million tuples is almost perfectly linear (8.16 secs. to 81.15 secs.), the increase from 100,000 tuples to 1 million tuples (0.45 sec. to 8.16 sec) is actually sublinear. The 10% selection using a clustered index is another example where increasing the size of the input relation by a factor of ten results in more than a ten-fold increase in the response time for the query. This query takes 5.02 seconds on the 1 million tuple relation and 61.86 seconds on the 10 million tuple relation. To understand why this happens one must consider the impact of seek time on the execution time of the query. Since two copies of each relation were loaded, when two one million tuple relations are declustered over 30 disk drives, the fragments occupy approximately 53 cylinders (out of 1224) on each disk drive. Two ten million tuple relations fill about 530 cylinders on each drive. As each page of the result relation is written to disk, the disk heads must be moved from their current position over the input relation to a free block on the disk. Thus, with the 10 million tuple relation, the cost of writing each output page is much higher.

As expected, the use of a clustered B-tree index always provides a significant improvement in performance. One observation to be made from Table 3 is the relative consistency of the execution time of the selection queries through a clustered index. Notice that the execution time for a 10% selection on the 1 million tuple relation is almost identical to the execution time of the 1% selection on the 10 million tuple relation. In both cases, 100,000 tuples are retrieved and stored, resulting in identical I/O and CPU costs.

The final row of Table 3 presents the time required to select a single tuple using a clustered index and return it to the host. Since the selection predicate is on the partitioning attribute, the query is directed to a single node, avoiding the overhead of starting the query on all 30 processors. The response for this query increases significantly as the

**Table 3 - Selection Queries**  
**30 Processors With Disks**  
(All Execution Times in Seconds)

```text
                                                     Number of Tuples in Source Relation
Query Description                                    100,000          1,000,000          10,000,000

1% nonindexed selection                              0.45             8.16               81.15
10% nonindexed selection                             0.82             10.82              135.61
1% selection using clustered index                   0.35             0.82               5.12
10% selection using clustered index                  0.77             5.02               61.86
1% selection using non-clustered index               0.60             8.77               113.37
single tuple select using clustered index            0.08             0.08               0.14
```

relation size is increased from 1 million to 10 million tuples because the height of the B-tree increases from two to three levels.

### Speedup Experiments {#dewitt-1990-gamma-s-speedup-experiments .section tag=0279}

In this section we examine how the response time for both the nonindexed and indexed selection queries on the 1 million tuple relation[^1] is affected by the number of processors used to execute the query. Ideally, one would like to see a linear improvement in performance as the number of processors is increased from 1 to 30. Increasing the number of processors increases both the aggregate CPU power and I/O bandwidth available, while reducing the number of tuples that must be processed by each processor.

In Figure 12, the average response times for the non-indexed 1% and 10% selection queries on the one million tuple relation are presented. As expected, the response time for each query decreases as the number of nodes is increased. The response time is higher for the 10% selection due to the cost of declustering and storing the result relation. While one could always store result tuples locally, by partitioning all result relations in a round-robin (or hashed) fashion one can ensure that the fragments of every result relation each contain approximately the same number of tuples. The speedup curves corresponding to Figure 12 are presented in Figure 13. In Figure 14, the average response time is presented as a function of the number of processors for the following three queries: a 1% selection through a clustered index, a 10% selection through a clustered index, and a 1% selection through a non-

[^1]: The 1 million tuple relation was used for these experiments because the 10 million tuple relation would not fit on 1 disk drive.

Figure 12

Figure 13 clustered index, all accessing the 1 million tuple relation. The corresponding speedup curves are presented in Figure 15.

Of the speedup curves presented in Figures 13 and 14, three queries are superlinear, one is slightly sublinear, and one is significantly sublinear. Consider first the 10% selection via a relation scan, the 1% selection through a non-clustered index, and the 10% selection through a clustered index. As discussed above, the source of the superlinear speedups exhibited by these queries is due to significant differences in the time the various configurations spend seeking. With one processor, the 1 million tuple relation occupies approximately 66% of the disk. When the same relation is declustered over 30 disk drives, it occupies about 2% of each disk. In the case of the 1% non-clustered index selection, each tuple selected requires a random seek. With one processor, the range of the each random seek is approximately 800 cylinders while with 30 processors the range of the seek is limited to about 27 cylinders. Since the seek time is proportional to the square root of the distance traveled by the disk head [GRAY88], reducing the size of the relation fragment on each disk significantly reduces the amount of time that the query spends seeking.

A similar effect also happens with the 10% clustered index selection. In this case, once the index has been used to locate the tuples satisfying the query, each input page will produce one output page and at some point the buffer pool will be filled with dirty output pages. In order to write an output page, the disk head must be moved

Figure 14

Figure 15 from its position over the input relation to the position on the disk where the output pages are to be placed. The relative cost of this seek decreases proportionally as the number of processors increases, resulting in a superlinear speedup for the query. The 10% non-indexed selection shown in Figure 13 is also superlinear for similar reasons. The reason that this query is not affected to the same degree is that, without an index, the seek time is a smaller fraction of the overall execution time of the query.

The 1% selection through a clustered index exhibits sublinear speedups because the cost of initiating a select and store operator on each processor (a total of 0.24 seconds for 30 processors) becomes a significant fraction of the total execution as the number of processors is increased.

**Scaleup Experiments**

In the final set of selection experiments the number of processors was varied from 5 to 30 while the size of the input relations was increased from 1 million to 6 million tuples, respectively. As shown in Figure 16, the response time for each of the five selection queries remains almost constant. The slight increase in response time is due to the overhead of initiating a selection and store operator at each site. Since a single process is used to initiate the execution of a query, as the number of processors employed is increased, the load on this process is increased proportionally. Switching to a tree-based, query initiation scheme [GERB87] would distribute this overhead among all the processors.

Figure 16

### 6.3. Join Queries {#dewitt-1990-gamma-s6-3 .section tag=027A}

Like the selection queries in the previous section, we conducted three sets of join experiments. First, for two different join queries, we varied the size of the input relations while the configuration of processors was kept constant. Next, for one join query a series of speedup and scaleup experiments were conducted. For each of these tests, two different partitionings of the input relations were used. In the first case, the input relations were declustered by hashing on the join attribute. In the second case, the input relations were declustered using a different attribute. The hybrid join algorithm was used for all queries.

### Performance Relative to Relation Size {#dewitt-1990-gamma-s-performance-relative-to-relation-size-2 .section tag=027B}

The first join query [BITT83], joinABprime, is a simple join of two relations: A and Bprime. The A relation contains either 100,000, 1 million, or 10 million tuples. The Bprime relation contains, respectively, 10,000, 100,000, or 1 million tuples. The result relation has the same number of tuples as the Bprime relation.[^1] The second query, joinAselB, is composed of one join and one selection. A and B have the same number of tuples and the

[^1]: For each join operation, the result relation contains all the fields of both input relations and thus the result tuples are 416 bytes wide.

selection on B reduces the size of B to the size of the Bprime relation in the corresponding joinABprime query. The result relation for this query has the same number of tuples as in the corresponding joinABprime query. As an example, if A has 10 million tuples, then joinABprime joins A with a Bprime relation that contains 1 million tuples, while in joinAselB the selection on B restricts B from 10 million tuples to 1 million tuples and then joins the result with A.

The first variation of the join queries tested involved no indices and used a non-partitioning attribute for both the join and selection attributes. Thus, before the join can be performed, the two input relations must be redistributed by hashing on the join attribute value of each tuple. The results from these tests are contained in the first 2 rows of Table 4. The second variation of the join queries also did not employ any indices but, in this case, the relations were hash partitioned on the joining attribute; enabling the redistribution phase of the join to be skipped. The results for these tests are contained in last 2 rows of Table 4.

The results in Table 4 indicate that the execution time of each join query increases in a fairly linear fashion as the size of the input relations are increased. Gamma does not exhibit linearity for the 10 million tuple queries because the size of the inner relation (208 megabytes) is twice as large as the total available space for hash tables. Hence, the Hybrid join algorithm needs two buckets to process these queries. While the tuples in the first bucket can be placed directly into memory-resident hash tables, the second bucket must be written to disk (see Section 4.2).

As expected, the version of each query in which the partitioning attribute was used as the join attribute ran faster. From these results one can estimate a lower bound on the aggregate rate at which data can be redistributed by the Intel iPSC/2 hypercube. Consider the version of the joinABprime query in which a million tuple relation is

Table 4 - Join Queries  
30 Processors With Disks  
(All Execution Times in Seconds)

| Query Description | 100,000 | 1,000,000 | 10,000,000 |
| --- | --- | --- | --- |
| JoinABprime with non-partitioning attributes of A and B used as join attributes | 3.52 | 28.69 | 438.90 |
| JoinAselB with non-partitioning attributes of A and B used as join attributes | 2.69 | 25.13 | 373.98 |
| JoinABprime with partitioning attributes of A and B used as join attributes | 3.34 | 25.95 | 426.25 |
| JoinAselB with partitioning attributes of A and B used as join attributes | 2.74 | 23.77 | 362.89 |

joined with a 100,000 tuple relation. This query requires 28.69 seconds when the join is not on the partitioning attribute. During the execution of this query, 1.1 million 208 byte tuples must be redistributed by hashing on the join attribute, yielding an aggregate total transfer rate of 7.9 megabytes/second during the processing of this query. This should not be construed, however, as an accurate estimate of the maximum obtainable interprocessor communications bandwidth as the CPUs may be the limiting factor (the disks are not likely to be the limiting factor as from Table 3 one can estimate that the aggregate bandwidth of the 30 disks to be about 25 megabytes/second).

### Speedup Experiments {#dewitt-1990-gamma-s-speedup-experiments-2 .section tag=027C}

For the join speedup experiments, we used the joinABprime query with a 1 million tuple A relation and a 100,000 tuple Bprime relation. The number of processors was varied from five to thirty. Since with fewer than five processors two or more buckets are needed, including the execution time for one processor (which needs 5 buckets) would have made the response times for five or more processors appear artificially fast; resulting in superlinear speedup curves.

The resulting response times are plotted in Figure 17 and the corresponding speedup curves are presented in Figure 18. From the shape of these graphs it is obvious that the execution time for the query is significantly reduced as additional processors are employed. Several factors prevent the system from achieving perfectly linear speedups.

Figure 17

Figure 18

First, the cost of starting four operator tasks (two scans, one join, and one store) on each processor increases as a function of the number of processors used. Second, the effect of short-circuiting local messages diminishes as the number of processors is increased. For example, consider a five processor configuration and the non-partitioning attribute version of the JoinABprime query. As each processor repartitions tuples by hashing on the join attribute, 1/5th of the input tuples it processes are destined for itself and will be short-circuited by the communications software. In addition, as the query produces tuples of the result relation (which is partitioned in a round-robin manner), they too will be short circuited. As the number of processors is increased, the number of short-circuited packets decreases to the point where, with 30 processors, only 1/30th of the packets will be short-circuited. Because these intra-node packets are less expensive than their corresponding inter-node packets, smaller configurations will benefit more from short-circuiting. In the case of a partitioning-attribute joins, all input tuples will short-circuit the network along with a fraction of the output tuples.

### Scaleup Experiments {#dewitt-1990-gamma-s-scaleup-experiments .section tag=027D}

The JoinABprime query was also used for the join scaleup experiments. For these tests, the number of processors was varied from 5 to 30 while the size of the A relation was varied from 1 million to 6 million tuples in increments of 1 million tuples and the size of the Bprime relation was varied from 100,000 to 600,000 tuples in increments of 100,000. For each configuration, only one join bucket was needed. The results of these tests are presented in Figure 19. Three factors contribute to the slight increase in response times. First, the task of initiating 4 processes at each site is performed by a single processor. Second, as the number of processors increases, the effects of short-circuiting messages during the execution of these queries diminishes - especially in the case when the join attribute is not the partitioning attribute. Finally, the response time may be being limited by the speed of the communications network.

Figure 19

### 6.4. Aggregate Queries {#dewitt-1990-gamma-s6-4 .section tag=027E}

Our aggregate tests included a mix of scalar aggregate and aggregate function queries run on the 30 processor configuration. The first query computes the minimum of a non-indexed attribute. The next two queries compute, respectively, the sum and minimum of an attribute after partitioning the relation into 20 subsets. Three sizes of input relations were used: 100,000, 1 million, and 10 million tuples. The results from these tests are contained in Table 5. Since the scalar aggregates and aggregate function operators are executed using algorithms that are similar to those used by the selection and join operators, respectively, no speedup or scaleup experiments were conducted.

**Table 5 - Aggregate Queries**  
**30 Processors with Disks**  
*(All Execution Times in Seconds)*

| Query Description | Number of Tuples in Source Relation |  |  |
| --- | --- | --- | --- |
|  | 100,000 | 1,000,000 | 10,000,000 |
| Scalar aggregate | 1.10 | 10.36 | 106.42 |
| Min aggregate function (20 Partitions) | 2.03 | 12.48 | 120.03 |
| Sum aggregate function (20 Partitions) | 2.03 | 12.39 | 120.22 |

### 6.5. Update Queries {#dewitt-1990-gamma-s6-5 .section tag=027F}

The next set of tests included a mix of append, delete, and modify queries on three different sizes of relations: 100,000, 1 million, and 10 million tuples. The results of these tests are presented in Table 6. Since Gamma’s recovery mechanism is not yet operational, these results should be viewed accordingly.

The first query appends a single tuple to a relation on which no indices exist. The second appends a tuple to a relation on which one index exists. The third query deletes a single tuple from a relation, using a clustered B-tree index to locate the tuple to be deleted. In the first query no indices exist and hence no indices need to be updated, whereas in the second and third queries, one index needs to be updated.

The fourth through sixth queries test the cost of modifying a tuple in three different ways. In all three tests, a non-clustered index exists on the unique2 attribute, and, in addition, a clustered index exists on the Unique1 attribute. In the first case, the modified attribute is the partitioning attribute, thus requiring that the modified tuple be relocated. Furthermore, since the tuple is relocated, the secondary index must also be updated. The second modify query modifies a non-partitioning, nonindexed attribute. The third modify query modifies an attribute on which a non-clustered index has been constructed, using the index to locate the tuple to be modified.

Table 6 - Update Queries  
30 Processors With Disks  
(All Execution Times in Seconds)

|  | Number of Tuples in Source Relation |  |  |
| --- | --- | --- | --- |
|  | 100,000 | 1,000,000 | 10,000,000 |
| Append 1 Tuple (No indices exist) | 0.07 | 0.08 | 0.10 |
| Append 1 Tuple (One index exists) | 0.18 | 0.21 | 0.22 |
| Delete 1 tuple | 0.34 | 0.28 | 0.49 |
| Modify 1 tuple (#1) | 0.72 | 0.73 | 0.93 |
| Modify 1 tuple (#2) | 0.18 | 0.20 | 0.24 |
| Modify 1 tuple (#3) | 0.33 | 0.38 | 0.52 |
