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
section: "3"
section_title: 'Microbenchmark: TPC-H Query 1'
tag: "0481"
kind: section
lang: en
source: https://www.cidrdb.org/cidr2005/papers/P19.pdf
pdf_sha256: c509153c876aee8706e298d43e2fa93ade2696cc3102643b439af0f508bb52fc
pdf_pages: 3-7
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 254991e92110e0719a80b003635f8e0528e0fa07020499564e9cb25c44fae4ce
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

While we target CPU efficiency of query processing in general, we first focus on *expression calculation*, discarding more complex relational operations (like join) to simplify our analysis. We choose Query 1 of the TPC-H benchmark, shown in Figure 3, this query is CPU-bound because on all RDBMSs we tested. Also, this query requires virtually no optimization or fancy join implementations as its plan is so simple. Thus, all database systems operate on a level playing field and mainly expose their expression evaluation efficiency.

The TPC-H benchmark operates on a data warehouse of 1GB, the size of which can be increased with a Scaling Factor (SF). Query 1 is a scan on the lineitem table of SF*6M tuples, that selects almost all tuples (SF*5.9M), and computes a number of fixed-point decimal expressions: two column-to-constant subtractions, one column-to-constant addition, three column-to-column multiplications, and eight aggregates (four SUM()s, three AVG()s and a COUNT()). The aggregate grouping is on two single-character columns, and yields only 4 unique combinations, such that it can be done efficiently with a small hash-table, requiring no additional I/O nor even CPU cache misses (for accessing the hash-table).

In the following, we analyze the performance of Query 1 first on relational database systems, then on MonetDB/MIL and finally in a hand-coded program.

| TPC-H Query 1 Experiments |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| DBMS “X” | (sec*#CPU)/SF | SF | #CPU, | SPECcpu int/fp |  |  |
| MySQL 4.1 | 28.1 | 1 | 1 AthlonMP 1533MHz, | 609/547 |  |  |
| MonetDB/MIL | 26.6 | 1 | 1 AthlonMP 1533MHz, | 609/547 |  |  |
| hand-coded | 0.22 | 1 | 1 AthlonMP 1533MHz, | 609/547 |  |  |
| hand-coded | 0.14 | 1 | 1 Itanium2 1.3GHz, | 1132/1891 |  |  |
| MonetDB/X100 | 0.50 | 1 | 1 AthlonMP 1533MHz, | 609/547 |  |  |
| MonetDB/X100 | 0.31 | 1 | 1 Itanium2 1.3GHz, | 1132/1891 |  |  |
| MonetDB/X100 | 0.30 | 100 | 1 Itanium2 1.3GHz, | 1132/1891 |  |  |
| Oracle10g | 18.1 | 100 | 16 Itanium2 1.3GHz, | 1132/1891 |  |  |
| Oracle10g | 13.2 | 1000 | 64 Itanium2 1.5GHz, | 1408/2161 |  |  |
| SQLserver2000 | 18.0 | 100 | 2 Xeon P4 3.0GHz, | 1294/1208 |  |  |
| SQLserver2000 | 21.8 | 1000 | 8 Xeon P4 2.8GHz, | 1270/1094 |  |  |
| DB2 UDB 8.1 | 9.0 | 100 | 4 Itanium2 1.5GHz, | 1408/2161 |  |  |
| DB2 UDB 8.1 | 7.4 | 100 | 2 Opteron 2.0GHz, | 1409/1514 |  |  |
| Sybase IQ 12.5 | 15.6 | 100 | 2 USIII 1.28GHz, | 704/1054 |  |  |
| Sybase IQ 12.5 | 15.8 | 1000 | 2 USIII 1.28GHz, | 704/1054 |  |  |
| TPC-H Query 1 Reference Results (www.tpc.org) |  |  |  |  |  |  |

Table 1: TPC-H Query 1 Performance {#boncz-2005-x100-tab-1 .table tag=076B}

### 3.1 Query 1 on Relational Database Systems {#boncz-2005-x100-s3-1 .section tag=076C}

Since the early days of RDBMSs, query execution functionality is provided by implementing a physical

SELECT l_returnflag, l_linestatus,
sum(l_quantity) AS sum_qty,
sum(l_extendedprice) AS sum_base_price,
sum(l_extendedprice * (1 - l_discount))
    AS sum_disc_price,
sum(l_extendedprice * (1 - l_discount) *
    (1 + l_tax)) AS sum_charge,
avg(l_quantity) AS avg_qty,
avg(l_extendedprice) AS avg_price,
avg(l_discount) AS avg_disc,
count(*) AS count_order

FROM lineitem
WHERE l_shipdate <= date '1998-09-02'
GROUP BY l_returnflag, l_linestatus relational algebra, typically following the Volcano [[graefe-1994-volcano]] model of pipelined processing. Relational algebra, however, has a high degree of freedom in its parameters. For instance, even a simple ScanSelect(R, b, P) only at query-time receives full knowledge of the format of the input relation R (number of columns, their types, and record offsets), the boolean selection expression b (which may be of any form), and a list of projection expressions P (each of arbitrary complexity) that define the output relation. In order to deal with all possible R, b, and P, DBMS implementors must in fact implement an expression interpreter that can handle expressions of arbitrary complexity.

Figure 3: TPC-H Query 1 {#boncz-2005-x100-fig-3 .figure tag=076D}

One of the dangers of such an interpreter, especially if the granularity of interpretation is a tuple, is that the cost of the “real work” (i.e. executing the expressions found in the query) is only a tiny fraction of total query execution cost. We can see this happening in Table 2 that shows a gprof trace of a MySQL 4.1 of TPC-H Query 1 on a database of SF=1. The second column shows the percentage of total execution time spent in the routine, excluding time spent in routines it called (excl.). The first column is a cumulative sum of the second (cum.). The third column lists how many times the routine was called, while the fourth and fifth columns show the average number of instructions executed on each call, as well as the IPC achieved.

The first observation to make is that the five operations that do all the “work” (displayed in boldface), correspond to only 10% of total execution time. Closer inspection shows that 28% of execution time is taken up by creation and lookup in the hash-table used for aggregation. The remaining 62% of execution time is spread over functions like rec_get_nth_field, that navigate through MySQL’s record representation and copy data in and out of it. Other factors, such as locking overhead (pthread_mutex_unlock, mutex_test_and_set) or buffer page allocation (buf_frame_align) seem to play only a minor role in this decision support query.

The second observation is the cost of the Item operations that correspond to the computational “work” of the query. For example, Item_func_plus::val has a cost of 38 instructions per addition. This performance trace was made on an SGI machine with MIPS R12000 CPU$^3$, which can execute three integer or floating-point instructions and one load/store per cycle, with an average operation latency of about 5 cycles. A simple arithmetic operation +(double src1, double src2) : double in RISC instructions would look like:

LOAD src1,reg1
LOAD src2,reg2
ADD reg1,reg2,reg3
STOR dst,reg3

The limiting factor in this code are the three

\footnotetext{3On our Linux test platforms, no multi-threaded profiling tools seem to be available.}

| cum. | excl. | calls | ins. | IPC | function |
| --- | --- | --- | --- | --- | --- |
| 11.9 | 11.9 | 846M | 6 | 0.64 | ut_fold_ulong_pair |
| 20.4 | 8.5 | 0.15M | 27K | 0.71 | ut_fold_binary |
| 26.2 | 5.8 | 77M | 37 | 0.85 | memcpy |
| 29.3 | 3.1 | 23M | 64 | 0.88 | Item_sum_sum::update_field |
| 32.3 | 3.0 | 6M | 247 | 0.83 | row_search_for_mysql |
| 35.2 | 2.9 | 17M | 79 | 0.70 | Item_sum_avg::update_field |
| 37.8 | 2.6 | 108M | 11 | 0.60 | rec_get_bit_field_1 |
| 40.3 | 2.5 | 6M | 213 | 0.61 | row_sel_store_mysql_rec |
| 42.7 | 2.4 | 48M | 25 | 0.52 | rec_get_nth_field |
| 45.1 | 2.4 | 60 | 19M | 0.69 | ha_print_info |
| 47.5 | 2.4 | 5.9M | 195 | 1.08 | end_update |
| 49.6 | 2.1 | 11M | 89 | 0.98 | field_conv |
| 51.6 | 2.0 | 5.9M | 16 | 0.77 | Field_float::val_real |
| 53.4 | 1.8 | 5.9M | 14 | 1.07 | Item_field::val |
| 54.9 | 1.5 | 42M | 17 | 0.51 | row_sel_field_store_in_mysql.. |
| 56.3 | 1.4 | 36M | 18 | 0.76 | buf_frame_align |
| 57.6 | 1.3 | 17M | 38 | 0.80 | Item_func_mul::val |
| 59.0 | 1.4 | 25M | 25 | 0.62 | pthread_mutex_unlock |
| 60.2 | 1.2 | 206M | 2 | 0.75 | hash_get_nth_cell |
| 61.4 | 1.2 | 25M | 21 | 0.65 | mutex_test_and_set |
| 62.4 | 1.0 | 102M | 4 | 0.62 | rec_get_1byte_offs_flag |
| 63.4 | 1.0 | 53M | 9 | 0.58 | rec_1_get_field_start_offs |
| 64.3 | 0.9 | 42M | 11 | 0.65 | rec_get_nth_field_extern_bit |
| 65.3 | 1.0 | 11M | 38 | 0.80 | Item_func_minus::val |
| 65.8 | 0.5 | 5.9M | 38 | 0.80 | Item_func_plus::val |

Table 2: MySQL gprof trace of TPC-H Q1: +,-,*,SUM,Avg takes <10%, low IPC of 0.7 {#boncz-2005-x100-tab-2 .table tag=076E}

load/store instructions, thus a MIPS processor can do one *(double,double) per 3 cycles. This is in sharp contrast to the MySQL cost of #ins/Instruction-Cycle (IPC) = 38/0.8 = 49 cycles! One explanation for this high cost is the absence of loop pipelining. As the routine called by MySQL only computes one addition per call, instead of an array of additions, the compiler cannot perform loop pipelining. Thus, the addition consists of four dependent instructions that have to wait for each other. With a mean instruction latency of 5 cycles, this explains a cost of about 20 cycles. The rest of the 49 cycles are spent on jumping into the routine, and pushing and popping the stack.

The consequence of the MySQL policy to execute expressions tuple-at-a-time, is twofold:

• Item_func_plus::val only performs one addition, preventing the compiler from creating a pipelined loop. As the instructions for one operation are highly dependent, empty pipeline slots must be generated (stalls) to wait for the instruction latencies, such that the cost of the loop becomes 20 instead of 3 cycles.

• the cost of the routine call (in the ballpark of 20 cycles) must be amortized over only one operation, which effectively doubles the operation cost.

We also tested the same query on a well-known commercial RDBMS (see the first row of Table 1). As we obviously lack the source code of this product, we cannot produce a gprof trace. However, the query evaluation cost on this DBMS is very similar to MySQL.

The lower part of Table 1 includes some official TPC-H Query 1 results taken from the TPC website.

```text
SF=1 ms  BW  SF=0.001 us  BW  tot MB  res size  (BW = MB/s)  MIL statement
127  352  150  305  45  5.9M  s0 := select(l_shipdate).mark
134  505  113  608  68  5.9M  s1 := join(s0,l_returnflag)
134  506  113  608  68  5.9M  s2 := join(s0,l_linestatus)
235  483  129  887  114  5.9M  s3 := join(s0,l_extprice)
233  488  130  881  114  5.9M  s4 := join(s0,l_discount)
232  489  127  901  114  5.9M  s5 := join(s0,l_tax)
134  507  104  660  68  5.9M  s6 := join(s0,l_quantity)
290  155  324  141  45  5.9M  s7 := group(s1)
329  136  368  124  45  5.9M  s8 := group(s7,s2)
0  0  0  0  0  4  s9 := unique(s8.mirror)
206  440  60  1527  91  5.9M  r0 := [+] (1.0,s5)
210  432  51  1796  91  5.9M  r1 := [-] (1.0,s4)
274  498  83  1655  137  5.9M  r2 := [*] (s3,r1)
274  499  84  1653  137  5.9M  r3 := [*] (s12,r0)
165  271  121  378  45  4  r4 := {sum} (r3,s8,s9)
165  271  125  366  45  4  r5 := {sum} (r2,s8,s9)
163  275  128  357  45  4  r6 := {sum} (s3,s8,s9)
163  275  128  357  45  4  r7 := {sum} (s4,s8,s9)
144  151  107  214  22  4  r8 := {sum} (s6,s8,s9)
112  196  145  157  22  4  r9 := {count} (s7,s8,s9)
3724  2327  TOTAL
```

Table 3: MonetDB/MIL trace of TPC-H Query 1 {#boncz-2005-x100-tab-3 .table tag=076F}

Query 1 is dominated by computations in a full scan and this scales linearly with table size. The query is also “embarrassingly parallel” using horizontal parallelism, such that TPC-H results on parallel systems most likely achieved linear speedup. Thus, we can compare throughput for different systems, by normalizing all times towards SF=1 and a single CPU. We also provide the SPECcpu int/float scores of the various hardware platforms used. We mainly do this in order to check that the relational DBMS results we obtained are roughly in the same ballpark as what is published by TPC. This leads us to believe that what we see in the MySQL trace is likely representative of what happens in commercial RDBMS implementations.

### 3.2 Query 1 on MonetDB/MIL {#boncz-2005-x100-s3-2 .section tag=0770}

The MonetDB system [4] developed by our group, is mostly known for its use of vertical fragmentation, storing tables column-wise, each column in a Binary Association Table (BAT) that contains [oid,value] combinations. A BAT is a 2-column table where the left column is called head and the right column tail. The algebraic query language of MonetDB is a column-algebra called MIL [5].

In contrast to the relational algebra, the MIL algebra does not have any degree of freedom. Its algebraic operators have a fixed number of parameters of a fixed format (all two-column tables or constants). The expression calculated by an operator is fixed, as well as the shape of the result. For example, the MIL join(BAT[t_l,t_e] A, BAT[t_e,t_r] B) : BAT[t_l,t_r] is an equi-join between the tail column of A and head column of B, that for each matching combination of tuples returns the head value from A and tail value from B. The mechanism in MIL to join on the other column (i.e. the head, instead of the tail) of A, is to use the MIL reverse(A) operator that returns a view on A with its columns swapped: BAT[t_e,t_l]. This reverse is a zero-cost operation in MonetDB that just swaps some pointers in the internal representation of a BAT. Complex expressions must be executed using multiple statements in MIL. For example, extprice * (1 - tax) becomes tmp1 := -; tmp2 := *, where * and - are multiplex operators that “map” a function onto an entire BAT (column). MIL executes in column-wise fashion in the sense that its operators always consume a number of materialized input BATs and materialize a single output BAT.

We used the MonetDB/MIL SQL front-end to translate TPC-H Query 1 into MIL and run it. Table 3 shows all 20 MIL invocations that together span more than 99% of elapsed query time. On TPC-H Query 1, MonetDB/MIL is clearly faster than MySQL and the commercial DBMS on the same machine, and is also competitive with the published TPC-H scores (see Table 1). However, closer inspection of Table 3 shows that almost all MIL operators are memory-bound instead of CPU-bound! This was established by running the same query plan on the TPC-H dataset with SF=0.001, such that all used columns of the lineitem table as well as all intermediate results fit inside the CPU cache, eliminating any memory traffic. MonetDB/MIL then becomes almost twice as fast. Columns 2 and 4 list the bandwidth (BW) in MB/s achieved by the individual MIL operations, counting both the size of the input BATs and the produced output BAT. On SF=1, MonetDB gets stuck at 500MB/s, which is the maximum bandwidth sustainable on this hardware [1]. When running purely in the CPU cache at SF=0.001, bandwidths can get above 1.5GB/s. For the multiplexed multiplication *, a bandwidth of only 500MB/s means 20M tuples per second (16 bytes in, 8 bytes out), thus 75 cycles per multiplication on our 1533MHz CPU, which is even worse than MySQL.

Thus, the column-at-a-time policy in MIL turns out to be a two-edged sword. To its advantage is the fact that MonetDB is not prone to the MySQL problem of spending 90% of its query execution time in tuple-at-a-time interpretation “overhead”. As the multiplex operations that perform expression calculations work on entire BATs (basically arrays of which the layout is known at compile-time), the compiler is able to employ loop-pipelining such that these operators achieve high CPU efficiencies, embodied by the SF=0.001 results.

However, we identify the following problems with full materialization. First, queries that contain complex calculation expressions over many tuples will materialize an entire result column for each function in the expression. Often, such function results are not required in the query result, but just serve as inputs to other functions in the expression. For instance, if an aggregation is the top-most operator in the query plan, the eventual result size might even be negligible (such as in Query 1). In such cases, MIL materializes much more data than strictly necessary, causing its high bandwidth consumption.

Also, Query 1 starts with a 98% selection of the 6M tuple table, and performs the aggregations on the remaining 5.9M million tuples. Again, MonetDB materializes the relevant result columns of the select() using six positional join()s. These joins are not required in a Volcano-like pipelined execution model. It can do the selection, computations and aggregation all in a single pass, not materializing any data.

While in this paper we concentrate on CPU efficiency in main-memory scenarios, we point out that the “artificially” high bandwidths generated by MonetDB/MIL make it harder to scale the system to disk-based problems efficiently, simply because memory bandwidth tends to be much larger (and cheaper) than I/O bandwidth. Sustaining a data transfer of e.g. 1.5GB/s would require a truly high-end RAID system with a very large number of disks.

```c
static void tpch_query1(int n, int hi_date,
    unsigned char*__restrict__ p_returnflag,
    unsigned char*__restrict__ p_linestatus,
    double*__restrict__ p_quantity,
    double*__restrict__ p_extendedprice,
    double*__restrict__ p_discount,
    double*__restrict__ p_tax,
    int*__restrict__ p_shipdate,
    aggr_t1*__restrict__ hashtab)
{
    for(int i=0; i<n; i++) {
        if (p_shipdate[i] <= hi_date) {
            aggr_t1 *entry = hashtab +
                (p_returnflag[i]<<8) + p_linestatus[i];
            double discount = p_discount[i];
            double extprice = p_extendedprice[i];
            entry->count++;
            entry->sum_qty += p_quantity[i];
            entry->sum_disc += discount;
            entry->sum_base_price += extprice;
            entry->sum_disc_price += (extprice *= (1-discount));
            entry->sum_charge += extprice*(1-p_tax[i]);
        }
    }
}
```

Figure 4: Hard-Coded UDF for Query 1 in C {#boncz-2005-x100-fig-4 .figure tag=0771}

### 3.3 Query 1: Baseline Performance {#boncz-2005-x100-s3-3 .section tag=0772}

To get a baseline of what modern hardware can do on a problem like Query 1, we implemented it as a single User Defined Function (UDF) in MonetDB, as shown in Figure 4. The UDF gets passed in only those columns touched by the query. In MonetDB, these columns are stored as arrays in BAT[void,T]s. That is, the oid values in the head column are densely ascending from 0 upwards. In such cases, MonetDB uses voids (“virtual-oids”) that are not stored. The BAT then takes the form of an array. We pass these arrays as __restrict__ pointers, such that the C compiler knows that they are non-overlapping. Only then can it apply loop-pipelining!

This implementation exploits the fact that a GROUP BY on two single-byte characters can never yield more than 65536 combinations, such that their combined bit-representation can be used directly as an array index to the table with aggregation results. Like in MonetDB/MIL, we performed some common subexpression elimination such that one minus and three AVG aggregates can be omitted.

Table 1 shows that this UDF implementation (labeled “hand-coded”) reduces query evaluation cost to a stunning 0.22 seconds. From the same table, you will notice that our new X100 query processor, that is the topic of the remainder of this paper, is able to get within a factor 2 of this hand-coded implementation.
