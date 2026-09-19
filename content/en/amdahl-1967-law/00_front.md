---
paper: amdahl-1967-law
title: Validity of the Single Processor Approach to Achieving Large Scale Computing Capabilities
authors:
  - Gene M. Amdahl
year: 1967
venue: AFIPS Spring Joint Computer Conference
field: architecture
section_title: Front Matter
tag: "0003"
kind: front
lang: en
source: https://www3.cs.stonybrook.edu/~rezaul/Spring-2012/CSE613/reading/Amdahl-1967.pdf
pdf_sha256: 81a363deb884ca23e495280eb9229df1064b4b3f79d662f270be35b50bea5318
pdf_pages: "1"
extraction: native
extraction_model: pdftotext version 26.09.0
content_sha256: 080d937afdb838b5b3ba5e349fdd9401e761ffa730c10c526cde8d0f7b2dfa9f
---

TECHNICAL LITERATURE

Validity of the Single Processor Approach to

Achieving Large Scale Computing Capabilities

Reprinted from the AFIPS Conference Proceedings, Vol. 30 (Atlantic City, N.J., Apr. 18–20), AFIPS Press, Reston, Va., 1967, pp. 483–485, when Dr. Amdahl was at International

Business Machines Corporation, Sunnyvale, California

Dr. Gene M. Amdahl

This article was the first publication by Gene Amdahl on what became known as Amdahl's Law. Interestingly, it has no equations and only a single figure. For this issue of the SSCS News, Dr. Amdahl agreed to redraw the figure. In the available hard copy it was illegible. We print this historic paper to enable members to read the original source from some 40 years ago.

The Editors

For over a decade prophets have voiced the contention that the organization of a single computer has reached its limits and that truly significant advances can be made only by interconnection of a multiplicity of computers in such a manner as to permit cooperative solution. Variously the proper direction has been pointed out as general purpose computers with a generalized interconnection of memories, or as specialized computers with geometrically related memory interconnections and controlled by one or more instruction streams.

Demonstration is made of the continued validity of the single processor approach and of the weaknesses of the multiple processor approach in terms of application to real problems and their attendant irregularities.

The arguments presented are based on statistical characteristics of computation on computers over the last decade and upon the operational requirements within problems of physical interest. An additional reference will be one of the most thorough analyses of relative computer capabilities currently published- "Changes in Computer Performance," Datamation, September 1966, Professor Kenneth E. Knight, Stanford School of Business Administration.

Summer 2007

The first characteristic of interest is the fraction of the computational load which is associated with data management housekeeping. This fraction has been very nearly constant for about ten years, and accounts for 40% of the executed instructions in production runs. In an entirely dedicated special purpose environment this might be reduced by a factor of two, but it is highly improbably that it could be reduced by a factor of three. The nature of this overhead appears to be sequential so that it is unlikely to be amenable to parallel processing techniques. Overhead alone would then place an upper limit on throughput of five to seven times the sequential processing rate, even if the housekeeping were done in a separate processor. The non-housekeeping part of the problem could exploit at most a processor of performance three to four times the performance of the housekeeping processor. A fairly obvious conclusion which can be drawn at this point is that the effort expended on achieving high parallel processing rates is wasted unless it is accompanied by achievements in sequential processing rates of very nearly the same magnitude.

Data management housekeeping is not the only problem to plague oversimplified approaches to high speed computation. The physical problems which are of practical interest tend to have rather significant complications. Examples of these complications are as follows: Boundaries are likely to be irregular; interiors are likely to be inhomogeneous; computations required may be dependent on the states of the variables at each point; propagation rates of different physical effects may be quite different; the rate of convergence, or convergence at all, may

be strongly dependent on sweeping through the array along different axes on succeeding passes, etc. The effect of each of these complications is very severe on any computer organization based on geometrically related processors in a paralleled processing system. Even the existence of regular rectangular boundaries has the interesting property that for spatial dimension of N there are 3N different point geometries to be dealt with in a nearest neighbor computation. If the second nearest neighbor were also involved, there would be 5N different point geometries to contend with. An irregular boundary compounds this problem as does an inhomogeneous interior. Computations which are dependent on the states of variables would require the processing at each point to consume approximately the same computational time as the sum of computations of all physical effects within a large region. Differences or changes in propagation rates may affect the mesh point relationships.

Ideally the computation of the action of the neighboring points upon the point under consideration involves their values at a previous time proportional to the mesh spacing and inversely proportional to the propagation rate. Since the time step is normally kept constant, a faster propagation rate for some effects would imply interactions with more distant points. Finally, the fairly common practice of sweeping through the mesh along different axes on succeeding passes poses problems of data management which affects all processors; however, it affects geometrically related processors more severely by requiring transposing all points in storage in addition to the revised input-output scheduling. A realistic assessment of the

IEEE SSCS NEWS 19
