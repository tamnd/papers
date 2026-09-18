---
paper: jouppi-1990-victimcache
title: Improving Direct-Mapped Cache Performance by the Addition of a Small Fully-Associative Cache and Prefetch Buffers
authors:
  - Norman P. Jouppi
year: 1990
venue: ISCA
field: architecture
section: "5"
section_title: Conclusions
tag: "0292"
kind: section
lang: en
source: https://doi.org/10.1145/325164.325162
pdf_sha256: 0077ca65ae80ad9d11024aea044515225281980a2dd542f6c04cdece03ed3f86
pdf_pages: 9-10
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 649401c7c6466156c6e9473de72f4ee0fc0c4974c436a8c5e0ae6860cf740c6d
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Small miss caches (e.g., 2 to 5 entries) have been shown to be effective in reducing data cache conflict misses for direct-mapped caches in range of 1K to 8K bytes. They effectively remove tight conflicts where misses alternate between several addresses that map to the same line in the cache. Miss caches are increasingly beneficial as line sizes increase and the percentage of conflict misses increases. In general it appears that as the percentage of conflict misses increases, the percent of these misses removable by a miss cache also increases, resulting in an even steeper slope for the performance improvement possible by using miss caches.

Victim caches are an improvement to miss caching that saves the victim of the cache miss instead of the target in a small associative cache. Victim caches are even more effective at removing conflict misses than miss caches.

Stream buffers prefetch cache lines after a missed cache line. They store the line until it is requested by a cache miss (if ever) to avoid unnecessary pollution of the cache. They are particularly useful at reducing the number of capacity and compulsory misses. They can take full advantage of the memory bandwidth available in pipelined memory systems for sequential references, unlike previously discussed prefetch techniques such as tagged prefetch or prefetch on miss. Stream buffers can also tolerate longer memory system latencies since they prefetch data much in advance of other prefetch techniques (even prefetch always). Stream buffers can also compensate for instruction conflict misses, since these tend to be relatively sequential in nature as well.

Multi-way stream buffers are a set of stream buffers that can prefetch down several streams concurrently. Multi-way stream buffers are useful for data references that contain interleaved accesses to several different large data structures, such as in array operations. However, since the prefetching is of sequential lines, only unit stride or near unit stride (2 or 3) access patterns benefit.

The performance improvements due to victim caches and due to stream buffers are relatively orthogonal for data references. Victim caches work well where references alternate between two locations that map to the same line in the cache. They do not prefetch data but only do a better job of keeping data fetched available for use. Stream buffers, however, achieve performance improvements by prefetching data. They do not remove conflict misses unless the conflicts are widely spaced in time, and the cache miss reference stream consists of many sequential accesses. These are precisely the conflict misses not handled well by a victim cache due to its relatively small capacity. Over the set of six benchmarks, on average only 2.5% of 4KB direct-mapped data cache misses that hit in a four-entry victim cache also hit in a four-way stream buffer for ccom, met, yacc, grr, and liver. In contrast, linpack, due to its sequential data access patterns, has 50% of the hits in the victim cache also hit in a four-way stream buffer. However only 4% of linpack’s cache misses hit in the victim cache (it benefits least from victim caching among the six benchmarks), so this is still not a significant amount of overlap between stream buffers and victim caching.

Figure 5-1 shows the performance of the base system with the addition of a four entry data victim cache, a instruction stream buffer, and a four-way data stream buffer. (The base system has on-chip 4KB instruction and 4KB data caches with 24 cycle miss penalties and 16B lines to a three-stage pipelined second-level 1MB cache with 128B lines and 320 cycle miss penalty.) The lower solid line in Figure 5-1 gives the performance of the original base system without the victim caches or buffers while the upper solid line gives the performance with buffers and victim caches. The combination of these techniques reduces the first-level miss rate to less than half of that of the baseline system, resulting in an average of 143% improvement in system performance for the six benchmarks. These results show that the addition of a small amount of hardware can dramatically reduce cache miss rates and improve system performance.

Figure.

Figure 5-1: Improved system performance

This study has concentrated on applying victim caches and stream buffers to first-level caches. An interesting area for future work is the application of these techniques to second-level caches. Also, the numeric programs used in this study used unit stride access patterns. Numeric programs with non-unit stride and mixed stride access patterns also need to be simulated. Finally, the performance of victim caching and stream buffers needs to be investigated for operating system execution and for multiprogramming workloads.

Acknowledgements
Mary Jo Doherty, John Ousterhout, Jeremy Dion, Anita Borg, Richard Swan, and the anonymous referees provided many helpful comments on an early draft of this paper. Alan Eustace suggested victim caching as an improvement to miss caching.

References
1. Baer, Jean-Loup, and Wang, Wenn-Hann. On the Inclusion Properties for Multi-Level Cache Hierarchies. The 15th Annual Symposium on Computer Architecture, IEEE Computer Society Press, June, 1988, pp. 73-80.

2. Borg, Anita, Kessler, Rick E., Lazana, Georgia, and Wall, David W. Long Address Traces from RISC Machines: Generation and Analysis. Tech. Rept. 89/14, Digital Equipment Corporation Western Research Laboratory, September, 1989.

3. Digital Equipment Corporation, Inc. VAX Hardware Handbook, volume 1 - 1984. Maynard, Massachusetts, 1984.

4. Emer, Joel S., and Clark, Douglas W. A Characterization of Processor Performance in the VAX-11/780. The 11th Annual Symposium on Computer Architecture, IEEE Computer Society Press, June, 1984, pp. 301-310.

5. Eustace, Alan. Private communication.

6. Farrens, Matthew K., and Pleszkun, Andrew R. Improving Performance of Small On-Chip Instruction Caches . The 16th Annual Symposium on Computer Architecture, IEEE Computer Society Press, May, 1989, pp. 234-241.

7. Hill, Mark D. Aspects of Cache Memory and Instruction Buffer Performance. Ph.D. Th., University of California, Berkeley, 1987.

8. Jouppi, Norman P., and Wall, David W. Available Instruction-Level Parallelism For Superpipelined and Superscalar Machines. Third International Conference on Architectural Support for Programming Languages and Operating Systems, IEEE Computer Society Press, April, 1989, pp. 272-282.

9. Jouppi, Norman P. Architectural and Organizational Tradeoffs in the Design of the MultiTitan CPU. The 16th Annual Symposium on Computer Architecture, IEEE Computer Society Press, May, 1989, pp. 281-289.

10. Nielsen, Michael J. K. Titan System Manual. Tech. Rept. 86/1, Digital Equipment Corporation Western Research Laboratory, September, 1986.

11. Ousterhout, John. Why Aren’t Operating Systems Getting Faster As Fast As Hardware? Tech. Rept. Technote 11, Digital Equipment Corporation Western Research Laboratory, October, 1989.

12. Smith, Alan J. “Sequential program prefetching in memory hierarchies.” IEEE Computer 11, 12 (December 1978), 7-21.

13. Smith, Alan J. “Cache Memories.” Computing Surveys (September 1982), 473-530.
