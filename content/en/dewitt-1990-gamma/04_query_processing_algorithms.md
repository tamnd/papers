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
section: "4"
section_title: Query Processing Algorithms
tag: "0269"
kind: section
lang: en
source: http://db.cs.berkeley.edu/cs286/papers/gamma-tkde1990.pdf
pdf_sha256: 420d33f44b8e050f33517cdff1299a58838b4ad826d80a6617200332ea02be5e
pdf_pages: 16-17
extraction: vision
extraction_model: gpt-5
content_sha256: d22e48238c755bbcc929c10e234ae51aec60286784490475c9054648fe7655c5
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

### 4.1. Selection Operator {#dewitt-1990-gamma-s4-1 .section tag=026A}

Since all relations are declustered over multiple disk drives, parallelizing the selection operation involves simply initiating a selection operator on the set of relevant nodes with disks. When the predicate in the selection clause is on the partitioning attribute of the relation and the relation is hash or range partitioned, the scheduler can direct the selection operator to a subset of the nodes. If either the relation is round-robin partitioned or the selection predicate is not on the partitioning attribute, a selection operator must be initiated on all nodes over which the relation is declustered. To enhance performance, Gamma employs a one page read-ahead mechanism when scanning the pages of a file sequentially or through a clustered index. This mechanism enables the processing of one page to be overlapped with the I/O for the subsequent page.

### 4.2. Join Operator {#dewitt-1990-gamma-s4-2 .section tag=026B}

The multiprocessor join algorithms provided by Gamma are based on concept of partitioning the two relations to be joined into disjoint subsets called **buckets** [GOOD81, KITS83, BRAT84]. by applying a hash function to the join attribute of each tuple. The partitioned buckets represent disjoint subsets of the original relations and have the important characteristic that all tuples with the same join attribute value are in the same bucket. We have implemented parallel versions of four join algorithms on the Gamma prototype: sort-merge, Grace [KITS83], Simple [DEWI84], and Hybrid [DEWI84]. While all four algorithms employ this concept of hash-based partitioning, the actual join computation depends on the algorithm. The parallel hybrid join algorithm is described in the following section. Additional information on all four parallel algorithms and their relative performance can be found in [SCHN89a]. Since this study found that the Hybrid hash join almost always provides the best performance, it is now the default algorithm in Gamma and is described in more detail in the following section. Since these hash-based join algorithms cannot be used to execute non-equijoin operations, such operations are not currently supported. To remedy this situation, we are in the process of designing a parallel non-equijoin algorithm for Gamma.

**Hybrid Hash-Join**

A **centralized** Hybrid hash-join algorithm [DEWI84] operates in three phases. In the first phase, the algorithm uses a hash function to partition the inner (smaller) relation, R, into N buckets. The tuples of the first bucket are used to build an in-memory hash table while the remaining N-1 buckets are stored in temporary files. A good hash function produces just enough buckets to ensure that each bucket of tuples will be small enough to fit entirely in main memory. During the second phase, relation S is partitioned using the hash function from step 1. Again, the last N-1 buckets are stored in temporary files while the tuples in the first bucket are used to immediately probe the in-memory hash table built during the first phase. During the third phase, the algorithm joins the remaining $N-1$ buckets from relation $R$ with their respective buckets from relation $S$. The join is thus broken up into a series of smaller joins; each of which hopefully can be computed without experiencing join overflow. The size of the smaller relation determines the number of buckets; this calculation is independent of the size of the larger relation.

Our parallel version of the Hybrid hash join algorithm is similar to the centralized algorithm described above. A **partitioning split table** first separates the joining relations into $N$ logical buckets. The number of buckets is chosen such that the tuples corresponding to each logical bucket will fit in the **aggregate memory** of the joining processors. The $N-1$ buckets intended for temporary storage on disk are each partitioned across all available disk sites. Likewise, a **joining split table** will be used to route tuples to their respective joining processor (these processors do not necessarily have attached disks), thus parallelizing the joining phase. Furthermore, the partitioning of the inner relation, $R$, into buckets is overlapped with the insertion of tuples from the first bucket of $R$ into memory-resident hash tables at each of the join nodes. In addition, the partitioning of the outer relation, $S$, into buckets is overlapped with the joining of the first bucket of $S$ with the first bucket of $R$. This requires that the partitioning split table for $R$ and $S$ be enhanced with the joining split table as tuples in the first bucket must be sent to those processors being used to effect the join. Of course, when the remaining $N-1$ buckets are joined, only the joining split table will be needed. Figure 8 depicts relation $R$ being partitioned into $N$ buckets across $k$ disk sites where the first bucket is to be joined on $m$ processors ($m$ may be less than, equal to, or greater than $k$).

### 4.3. Aggregate Operations {#dewitt-1990-gamma-s4-3 .section tag=026C}

Gamma implements scalar aggregates by having each processor compute its piece of the result in parallel. The partial results are then sent to a single process which combines these partial results into the final answer. Aggregate functions are computed in two steps. First, each processor computes a piece of the result by calculating a value for each of the partitions. Next, the processors redistribute the partial results by hashing on the "group by" attribute. The result of this step is to collect the partial results for each partition at a single site so that the final result for each partition can be computed.

### 4.4. Update Operators {#dewitt-1990-gamma-s4-4 .section tag=026D}

For the most part, the update operators (replace, delete, and append) are implemented using standard techniques. The only exception occurs when a replace operator modifies the partitioning attribute of a tuple. In this case, rather than writing the modified tuple back into the local fragment of the relation, the modified tuple is passed through a split table to determine which site should contain the tuple.
