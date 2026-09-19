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
section: "2"
section_title: How CPUs Work
tag: 047E
kind: section
lang: en
source: https://www.cidrdb.org/cidr2005/papers/P19.pdf
pdf_sha256: c509153c876aee8706e298d43e2fa93ade2696cc3102643b439af0f508bb52fc
pdf_pages: 2-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: d24c12429e368de9b81271a11bd560b8dc91e036fbc7c945a163ccfaaa487296
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Figure 1 displays for each year in the past decade the fastest CPU available in terms of MHz, as well as highest performance (one thing does not necessarily equate the other), as well as the most advanced chip manufacturing technology in production that year.

The root cause for CPU MHz improvements is progress in chip manufacturing process scales, that typically shrink by a factor 1.4 every 18 months (a.k.a. Moore’s law [13]). Every smaller manufacturing scale means twice (the square of 1.4) as many, and twice smaller transistors, as well as 1.4 times smaller wire distances and signal latencies. Thus one would expect CPU MHz to increase with inverted signal latencies, but Figure 1 shows that clock speed has increased even further. This is mainly done by *pipelining*: dividing the work of a CPU instruction in ever more stages. Less work per stage means that the CPU frequency can be increased. While the 1988 Intel 80386 CPU executed one instruction in one (or more) cycles, the 1993 Pentium already had a 5-stage pipeline, to be increased in the 1999 PentiumIII to 14 while the 2004 Pentium4 has 31 pipeline stages.

Pipelines introduce two dangers: (*i*) if one instruction needs the result of a previous instruction, it cannot be pushed into the pipeline right after it, but must wait until the first instruction has passed through the pipeline (or a significant fraction thereof), and (*ii*) in case of IF-*a*-THEN-*b*-ELSE-*c* branches, the CPU must

Figure.

Figure 1: A Decade of CPU Performance {#boncz-2005-x100-fig-1 .figure tag=047F}

*predict* whether *a* will evaluate to true or false. It might guess the latter and put *c* into the pipeline, just after *a*. Many stages further, when the evaluation of *a* finishes, it may determine that it guessed wrongly (i.e. *mispredicted* the branch), and then must *flush* the pipeline (discard all instructions in it) and start over with *b*. Obviously, the longer the pipeline, the more instructions are flushed away and the higher the performance penalty. Translated to database systems, branches that are data-dependent, such as those found in a selection operator on data with a selectivity that is neither very high nor very low, are impossible to predict and can significantly slow down query execution [17].

In addition, *super-scalar* CPUs² offer the possibility to take multiple instructions into execution in parallel if they are independent. That is, the CPU has not one, but multiple pipelines. Each cycle, a new instruction can be pushed into each pipeline, provided again they are independent of all instructions already in execution. A super-scalar CPU can get to an IPC (Instructions Per Cycle) of > 1. Figure 1 shows that this has allowed real-world CPU performance to increase faster than CPU frequency.

Modern CPUs are balanced in different ways. The Intel Itanium2 processor is a VLIW (Very Large Instruction Word) processor with many parallel pipelines (it can execute up to 6 instructions per cycle) with only few (7) stages, and therefore a relatively low clock speed of 1.5GHz. In contrast, the Pentium4 has its very long 31-stage pipeline allowing for a 3.6GHz clock speed, but can only execute 3 instructions per cycle. Either way, to get to its theoretical maximum throughput, an Itanium2 needs 7×6 = 42 independent instructions *at any time*, while the Pentium4 needs 31×3 = 93. Such parallelism cannot always be found, and therefore many programs use the resources of the Itanium2 much better than the Pentium4, which explains why in benchmarks the performance of both CPUs is similar, despite the big clock speed difference.

²Intel introduced the term *hyper-pipelined* as a synonym for “super-scalar”, to market its Pentium4 CPU.

```c
int sel_lt_int_col_int_val(int n, int* res, int* in, int V) {
    for(int i=0,j=0; i<n; i++){
        /* branch version */
        if (src[i] < v)
            out[j++] = i;
        /* predicated version */
        bool b = (src[i] < v);
        out[j] = i;
        j += b;
    }
    return j;
}
```

Figure.

Figure 2: Itanium Hardware Predication Eliminates Branch Mispredictions {#boncz-2005-x100-fig-2 .figure tag=0480}

Most programming languages do not require programmers to explicitly specify in their programs which instructions (or expressions) are independent. Therefore, compiler optimizations have become critical to achieving good CPU utilization. The most important technique is loop pipelining, in which an operation consisting of multiple dependent operations F(), G() on all n independent elements of an array A is transformed from:
F(A[0]),G(A[0]), F(A[1]),G(A[1]),.. F(A[n]),G(A[n])
into:
F(A[0]),F(A[1]),F(A[2]), G(A[0]),G(A[1]),G(A[2]), F(A[3]),..

Supposing the pipeline dependency latency of F() is 2 cycles, when G(A[0]) is taken into execution, the result of F(A[0]) has just become available.

In the case of the Itanium2 processor, the importance of the compiler is even stronger, as it is the compiler which has to find instructions that can go into different pipelines (other CPUs do that at runtime, using out-of-order execution). As the Itanium2 chip does not need any complex logic dedicated to finding out-of-order execution opportunities, it can contain more pipelines that do real work. The Itanium2 also has a feature called branch predication for eliminating branch mispredictions, by allowing to execute both the THEN and ELSE blocks in parallel and discard one of the results as soon as the result of the condition becomes known. It is also the task of the compiler to detect opportunities for branch predication.

Figure 2 shows a micro-benchmark of the selection query SELECT oid FROM table WHERE col < X, where X is uniformly and randomly distributed over [0:100] and we vary the selectivity X between 0 and 100. Normal CPUs like the AthlonMP show worst-case behavior around 50%, due to branch mispredictions. As suggested in [17], by rewriting the code cleverly, we can transform the branch into a boolean calculation (the “predicated” variant). Performance of this rewritten variant is independent of the selectivity, but incurs a higher average cost. Interestingly, the “branch” variant on Itanium2 is highly efficient and independent of selectivity as well, because the compiler transforms the branch into hardware-predicated code.

Finally, we should mention the importance of on-chip caches to CPU throughput. About 30% of all instructions executed by a CPU are memory loads and stores, that access data on DRAM chips, located inches away from the CPU on a motherboard. This imposes a physical lower bound on memory latency of around 50 ns. This (ideal) minimum latency of 50ns already translates into 180 wait cycles for a 3.6GHz CPU. Thus, only if the overwhelming majority of the memory accessed by a program can be found in an on-chip *cache*, a modern CPU has a chance to operate at its maximum throughput. Recent database research has shown that DBMS performance is strongly impaired by memory access cost (“cache misses”) [3], and can significantly improve if *cache-conscious* data structures are used, such as cache-aligned B-trees [16, 7] or column-wise data layouts such as PAX [2] and DSM [8] (as in MonetDB). Also, query processing algorithms that restrict their random memory access patterns to regions that fit a CPU cache, such as radix-partitioned hash-join [18, 11], strongly improve performance.

All in all, CPUs have become highly complex devices, where the instruction throughput of a processor can vary by orders of magnitude (!) depending on the cache hit-ratio of the memory loads and stores, the number of branches and whether they can be predicted/predicated, as well as the amount of independent instructions a compiler and the CPU can detect on average. It has been shown that query execution in commercial DBMS systems get an IPC of only 0.7 [6], thus executing *less* than one instruction per cycle. In contrast, scientific computation (e.g. matrix multiplication) or multimedia processing does extract average IPCs of up to 2 out of modern CPUs. We argue that database systems do not need to perform so badly, especially not on large-scale analysis tasks, where millions of tuples need to be examined and expressions to be calculated. This abundance of work contains plenty of independence that should be able to fill all the pipelines a CPU can offer. Hence, our quest is to adapt database architecture to expose this to the compiler and CPU where possible, and thus significantly improve query processing throughput.
