# Back translation

67 pages checked: 44 the same, 14 differ in wording, 9 differ materially

Run 20260914T214350Z. Every abstract, every section of the first 10 papers of the canon, and a 5% sample of the rest.

2,197,912 tokens in, 22,482 out.

## Differs materially

### `content/vi/birrell-1984-rpc/00_front.md`

every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.

- material: the original says the semantics should make distributed computations easier to build and get right, the back-translation says they will help do so.
- material: the original says Nelson’s dissertation references much of the previous RPC work, the back-translation says it references most of that work.
- wording: the original says several areas were inadequately understood, the back-translation says some areas were still not fully understood.

The English as it stands:

> still execute (depending on the details of the parallelism of that environment and the RPC implementation).
>
> There are many attractive aspects to this idea. One is clean and simple semantics: these should make it easier to build distributed computations, and to get them right. Another is efficiency: procedure calls seem simple enough for the communication to be quite rapid. A third is generality: in single-machine computations, procedures are often the most important mechanism for communication between parts of the algorithm.
>
> The idea of RPC has been around for many years. It has been discussed in the public literature many times since at least as far back as 1976 [15]. Nelson’s doctoral dissertation [13] is an extensive examination of the design possibilities for an RPC system and has references to much of the previous work on RPC. However, full-scale implementations of RPC have been rarer than paper designs. Notable recent efforts include Courier in the Xerox NS family of protocols [4], and current work at MIT [10].
>
> This paper results from the construction of an RPC facility for the Cedar project. We felt, because of earlier work (particularly Nelson’s thesis and associated experiments), that we understood the choices the designer of an RPC facility must make. Our task was to make the choices in light of our particular aims and environment. In practice, we found that several areas were inadequately understood, and we produced a system whose design has several novel aspects.

What came back:

> still executes (depending on the details of concurrency in that environment and the RPC implementation).
>
> There are many attractive aspects of this idea. One is clear and simple semantics: these will help make constructing distributed computations easier, and help them be carried out correctly. Another aspect is efficiency: procedure calls seem simple enough that communication can take place very quickly. The third aspect is generality: in computations on a single machine, procedures are usually the most important mechanism for communication between parts of the algorithm.
>
> The idea of RPC has existed for many years. It has been discussed in the public literature many times since at least 1976 [15]. Nelson's doctoral dissertation [13] is an extensive survey of the design possibilities for an RPC system and has references to most of the previous work on RPC. However, full-scale RPC implementations are rarer than designs on paper. Notable recent efforts include Courier in the Xerox NS family of protocols [4], and current work at MIT [10].
>
> This paper results from building an RPC facility for the Cedar project. We felt, based on previous work (especially Nelson's dissertation and related experiments), that we understood the choices that the designer of an RPC facility must make. Our task was to make the choices based on our specific goals and environment. In practice, we found that some areas were still not fully understood, and we created a system whose design has some novel aspects.

### `content/vi/corbett-2012-spanner/07_future_work.md`

the 5% sample, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.

- material: the original plans to support direct changes of Paxos configurations, the back-translation plans to support live changes, introducing a claim about changes during operation and omitting that they are direct.

The English as it stands:

> We have spent most of the last year working with the F1 team to transition Google’s advertising backend from MySQL to Spanner. We are actively improving its monitoring and support tools, as well as tuning its performance. In addition, we have been working on improving the functionality and performance of our backup/restore system. We are currently implementing the Spanner schema language, automatic maintenance of secondary indices, and automatic load-based resharding. Longer term, there are a couple of features that we plan to investigate. Optimistically doing reads in parallel may be a valuable strategy to pursue, but initial experiments have indicated that the right implementation is non-trivial. In addition, we plan to eventually support direct changes of Paxos configurations [22, 34].
>
> Given that we expect many applications to replicate their data across datacenters that are relatively close to each other, TrueTime $\epsilon$ may noticeably affect performance. We see no insurmountable obstacle to reducing $\epsilon$ below 1ms. Time-master-query intervals can be reduced, and better clock crystals are relatively cheap. Time-master query latency could be reduced with improved networking technology, or possibly even avoided through alternate time-distribution technology.
>
> Finally, there are obvious areas for improvement. Although Spanner is scalable in the number of nodes, the node-local data structures have relatively poor performance on complex SQL queries, because they were designed for simple key-value accesses. Algorithms and data structures from DB literature could improve single-node performance a great deal. Second, moving data automatically between datacenters in response to changes in client load has long been a goal of ours, but to make that goal effective, we would also need the ability to move client-application processes between datacenters in an automated, coordinated fashion. Moving processes raises the even more difficult problem of managing resource acquisition and allocation between datacenters.

What came back:

> We have spent most of the past year working with the F1 team to move Google's advertising backend from MySQL to Spanner. We are actively improving its monitoring and support tools, as well as tuning its performance. In addition, we have worked to improve the functionality and performance of our backup/restore system. We are currently implementing the Spanner schema language, automatic maintenance of secondary indexes, and automatic load-based resharding. In the long term, there are a few features that we plan to investigate. Performing parallel reads optimistically may be a valuable strategy to pursue, but initial experiments have shown that implementing it correctly is not trivial. In addition, we plan eventually to support live changes to Paxos configurations [22, 34].
>
> Because we expect many applications to replicate their data across relatively nearby data centers, TrueTime $\epsilon$ may significantly affect performance. We see no insurmountable obstacle to reducing $\epsilon$ below 1ms. Time-master query intervals can be reduced, and better clock crystals are relatively inexpensive. Time-master query latency can be reduced with improved networking technology, or may even be avoided through alternative time-distribution technology.
>
> Finally, there are clear areas that need improvement. Although Spanner scales with the number of nodes, node-local data structures perform relatively poorly on complex SQL queries, because they were designed for simple key-value accesses. Algorithms and data structures from the DB literature could significantly improve the performance of a single node. Second, automatic movement of data between data centers in response to changes in client load has long been a goal of ours, but for that goal to be effective, we also need the ability to move client application processes between data centers in an automatic, coordinated way. Moving processes raises the even more difficult problem of managing resource acquisition and allocation between data centers.

### `content/vi/dageville-2016-snowflake/00_front.md`

every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.

- material: the original says the data and workloads require freshness, the back-translation says they require novelty.

The English as it stands:

> The Snowflake Elastic Data Warehouse
>
> Benoit Dageville, Thierry Cruanes, Marcin Zukowski, Vadim Antonov, Artin Avanes,
>
> Jon Bock, Jonathan Claybaugh, Daniel Engovatov, Martin Hentschel,
>
> Jiansheng Huang, Allison W. Lee, Ashish Motivala, Abdul Q. Munir, Steven Pelley,
>
> Peter Povinec, Greg Rahn, Spyridon Triantafyllis, Philipp Unterbrunner
>
> Snowflake Computing
>
> ABSTRACT
>
> We live in the golden age of distributed computing. Public cloud platforms now offer virtually unlimited compute and storage resources on demand. At the same time, the Software-as-a-Service (SaaS) model brings enterprise-class systems to users who previously could not afford such systems due to their cost and complexity. Alas, traditional data warehousing systems are struggling to fit into this new environment. For one thing, they have been designed for fixed resources and are thus unable to leverage the cloud’s elasticity. For another thing, their dependence on complex ETL pipelines and physical tuning is at odds with the flexibility and freshness requirements of the cloud’s new types of semi-structured data and rapidly evolving workloads.
>
> We decided a fundamental redesign was in order. Our mission was to build an enterprise-ready data warehousing solution for the cloud. The result is the Snowflake Elastic Data Warehouse, or “Snowflake” for short. Snowflake is a multi-tenant, transactional, secure, highly scalable and elastic system with full SQL support and built-in extensions for semi-structured and schema-less data. The system is offered as a pay-as-you-go service in the Amazon cloud. Users upload their data to the cloud and can immediately manage and query it using familiar tools and interfaces.

What came back:

> The Snowflake Elastic Data Warehouse
>
> Benoit Dageville, Thierry Cruanes, Marcin Zukowski, Vadim Antonov, Artin Avanes,
>
> Jon Bock, Jonathan Claybaugh, Daniel Engovatov, Martin Hentschel,
>
> Jiansheng Huang, Allison W. Lee, Ashish Motivala, Abdul Q. Munir, Steven Pelley,
>
> Peter Povinec, Greg Rahn, Spyridon Triantafyllis, Philipp Unterbrunner
>
> Snowflake Computing
>
> ABSTRACT
>
> We are living in the golden age of distributed computing. Public cloud platforms now provide nearly unlimited computing and storage resources on demand. At the same time, the Software-as-a-Service (SaaS) model brings enterprise-grade systems to users who previously could not afford such systems because of their cost and complexity. However, traditional data warehouse systems are struggling to adapt to this new environment. On the one hand, they were designed for fixed resources and therefore cannot take advantage of the elasticity of the cloud. On the other hand, their dependence on complex ETL pipelines and physical tuning goes against the requirements for flexibility and novelty of the cloud’s new semi-structured data types as well as rapidly evolving workloads.
>
> We decided that a fundamental redesign was needed. Our mission was to build an enterprise-ready data warehouse solution for the cloud. The result is the Snowflake Elastic Data Warehouse, or “Snowflake” for short. Snowflake is a multi-tenant, transactional, secure, highly scalable and elastic system with full SQL support and built-in extensions for semi-structured data and schemaless data. The system is provided as a pay-per-use service in the Amazon cloud. Users upload their data to the cloud and can immediately manage and query that data using familiar tools and interfaces.

### `content/vi/jacobson-1988-congestion/00_front.md`

every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.

- material: the original says much of the cause lies in transport protocol implementations, the back-translation says most of the cause lies in those implementations.

The English as it stands:

> Congestion Avoidance and Control*
>
> Van Jacobson†
> Lawrence Berkeley Laboratory
>
> Michael J. Karels‡
> University of California at Berkeley
>
> November, 1988
>
> Computer networks have experienced an explosive growth over the past few years and with that growth have come severe congestion problems. For example, it is now common to see internet gateways drop 10% of the incoming packets because of local buffer overflows. Our investigation of some of these problems has shown that much of the cause lies in transport protocol implementations (not in the protocols themselves): The ‘obvious’ ways to implement a window-based transport protocol can result in exactly the wrong behavior in response to network congestion. We give examples of ‘wrong’ behavior and describe some simple algorithms that can be used to make right things happen. The algorithms are rooted in the idea of achieving network stability by forcing the transport connection to obey a ‘packet conservation’ principle. We show how the algorithms derive from this principle and what effect they have on traffic over congested networks.

What came back:

> Congestion Avoidance and Control*
>
> Van Jacobson†
> Lawrence Berkeley Laboratory
>
> Michael J. Karels‡
> University of California at Berkeley
>
> November, 1988
>
> Computer networks have grown explosively over the past few years, and along with that growth have come serious congestion problems. For example, it is now common to see Internet gateways discard 10% of incoming packets due to local buffer overflow. Our research into some of these problems shows that most of the cause lies in transport protocol implementations (not the protocols themselves): The ‘obvious’ ways to implement a window-based transport protocol can lead to exactly the wrong behavior in response to network congestion. We give examples of ‘wrong’ behavior and describe some simple algorithms that can be used to make things go right. These algorithms are based on the idea of achieving network stability by forcing the transport connection to obey a ‘packet conservation’ principle. We show how the algorithms are derived from this principle and their impact on traffic through congested networks.

### `content/vi/lattner-2004-llvm/00_front.md`

every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.

- material: the original says the evaluation examines the effectiveness of the representation, the back-translation says it examines the efficiency of the representation.

The English as it stands:

> LLVM: A Compilation Framework for Lifelong Program Analysis & Transformation
>
> Chris Lattner
>
> Vikram Adve
> University of Illinois at Urbana-Champaign
> {lattner,vadve}@cs.uiuc.edu
> http://llvm.cs.uiuc.edu/
>
> ABSTRACT
> This paper describes LLVM (Low Level Virtual Machine), a compiler framework designed to support transparent, lifelong program analysis and transformation for arbitrary programs, by providing high-level information to compiler transformations at compile-time, link-time, run-time, and in idle time between runs. LLVM defines a common, low-level code representation in Static Single Assignment (SSA) form, with several novel features: a simple, language-independent type-system that exposes the primitives commonly used to implement high-level language features; an instruction for typed address arithmetic; and a simple mechanism that can be used to implement the exception handling features of high-level languages (and setjmp/longjmp in C) uniformly and efficiently. The LLVM compiler framework and code representation together provide a combination of key capabilities that are important for practical, lifelong analysis and transformation of programs. To our knowledge, no existing compilation approach provides all these capabilities. We describe the design of the LLVM representation and compiler framework, and evaluate the design in three ways: (a) the size and effectiveness of the representation, including the type information it provides; (b) compiler performance for several interprocedural problems; and (c) illustrative examples of the benefits LLVM provides for several challenging compiler problems.

What came back:

> LLVM: A Compilation Framework for Lifelong Program Analysis & Transformation
>
> Chris Lattner
>
> Vikram Adve
> University of Illinois at Urbana-Champaign
> {lattner,vadve}@cs.uiuc.edu
> http://llvm.cs.uiuc.edu/
>
> ABSTRACT
> This paper describes LLVM (Low Level Virtual Machine), a compiler framework designed to support transparent, lifelong program analysis and transformation for arbitrary programs, by providing high-level information for compiler transformations at compile time, link time, runtime, and idle time between runs. LLVM defines a common, low-level code representation in Static Single Assignment (SSA) form, with several new features: a simple, language-independent type system that exposes the primitives commonly used to implement high-level language features; an instruction for typed address computation; and a simple mechanism that can be used to implement the exception-handling features of high-level languages (and setjmp/longjmp in C) uniformly and efficiently. The LLVM compiler framework and code representation together provide a combination of key capabilities important for lifelong program analysis and transformation in practice. To our knowledge, no existing compilation approach provides all of these capabilities. We describe the design of the LLVM representation and compiler framework, and evaluate the design in three respects: (a) the size and efficiency of the representation, including the type information it provides; (b) the performance of the compiler on several interprocedural problems; and (c) illustrative examples of the benefits that LLVM brings to several challenging compiler problems.

### `content/vi/patterson-1981-risc/00_front.md`

every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.

- material: the original says such a machine should have a much shorter design time, the back-translation says it will have a much shorter design time.

The English as it stands:

> RISC I: A REDUCED INSTRUCTION SET VLSI COMPUTER
>
> DAVID A. PATTERSON and CARLO H. SEQUIN
>
> Computer Science Division
> University of California
> Berkeley, California
>
> ABSTRACT
>
> The Reduced Instruction Set Computer (RISC) Project investigates an alternative to the general trend toward computers with increasingly complex instruction sets: With a proper set of instructions and a corresponding architectural design, a machine with a high effective throughput can be achieved. The simplicity of the instruction set and addressing modes allows most instructions to execute in a single machine cycle, and the simplicity of each instruction guarantees a short cycle time. In addition, such a machine should have a much shorter design time.
>
> This paper presents the architecture of RISC I and its novel hardware support scheme for procedure call/return. Overlapping sets of register banks that can pass parameters directly to subroutines are largely responsible for the excellent performance of RISC I. Static and dynamic comparisons between this new architecture and more traditional machines are given. Although instructions are simpler, the average length of programs was found not to exceed programs for DEC VAX 11 by more than a factor of 2. Preliminary benchmarks demonstrate the performance advantages of RISC. It appears possible to build a single chip computer faster than VAX 11/780.

What came back:

> RISC I: VLSI COMPUTER WITH A REDUCED INSTRUCTION SET
>
> DAVID A. PATTERSON and CARLO H. SEQUIN
>
> Computer Science Division
> University of California
> Berkeley, California
>
> ABSTRACT
>
> The Reduced Instruction Set Computer (RISC) project investigates an alternative to the general trend toward computers with increasingly complex instruction sets: With an appropriate instruction set and a corresponding architectural design, a machine with high effective throughput can be achieved. The simplicity of the instruction set and addressing modes allows most instructions to execute in a single machine cycle, and the simplicity of each instruction ensures a short cycle time. In addition, such a machine will have a much shorter design time.
>
> This paper presents the architecture of RISC I and the new hardware support scheme for procedure call/return. Overlapping sets of register banks that can pass parameters directly to subroutines are the principal factor creating the excellent performance of RISC I. Static and dynamic comparisons between this new architecture and more traditional machines are given. Although the instructions are simpler, the average length of programs was found not to exceed programs for the DEC VAX 11 by more than a factor of 2. Preliminary benchmarks demonstrate the performance advantages of RISC. It appears feasible to build a single-chip computer faster than the VAX 11/780.

### `content/vi/rabin-1959-automata/00_front.md`

every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.

- material: the original says some decision problems are solvable by effective algorithms, the back-translation says they are solvable by efficient algorithms.

The English as it stands:

> Finite Automata and Their Decision Problems†
>
> Abstract: Finite automata are considered in this paper as instruments for classifying finite tapes. Each one-tape automaton defines a set of tapes, a two-tape automaton defines a set of pairs of tapes, et cetera. The structure of the defined sets is studied. Various generalizations of the notion of an automaton are introduced and their relation to the classical automata is determined. Some decision problems concerning automata are shown to be solvable by effective algorithms; others turn out to be unsolvable by algorithms.

What came back:

> Finite Automata and Their Decision Problems†
>
> Abstract: In this paper, finite automata are viewed as tools for classifying finite tapes. Each one-tape automaton defines a set of tapes, a two-tape automaton defines a set of pairs of tapes, etc. The structure of the defined sets is studied. Various generalizations of the concept of an automaton are introduced and their relationships with classical automata are determined. Some decision problems concerning automata are proved to be solvable by efficient algorithms; others turn out to be unsolvable by algorithms.

### `content/vi/selinger-1979-accesspath/00_front.md`

every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.

- material: the original names the authors’ affiliation as IBM Research Division, San Jose, the back-translation names it as IBM Research Laboratory, San Jose.

The English as it stands:

> Access Path Selection
> in a Relational Database Management System
>
> P. Griffiths Selinger
> M. M. Astrahan
> D. D. Chamberlin
> R. A. Lorie
> T. G. Price
>
> IBM Research Division, San Jose, California 95193
>
> ABSTRACT: In a high level query and data manipulation language such as SQL, requests are stated non-procedurally, without reference to access paths. This paper describes how System R chooses access paths for both simple (single relation) and complex queries (such as joins), given a user specification of desired data as a boolean expression of predicates. System R is an experimental database management system developed to carry out research on the relational model of data. System R was designed and built by members of the IBM San Jose Research Laboratory.

What came back:

> Access Path Selection
> in a Relational Database Management System
>
> P. Griffiths Selinger
> M. M. Astrahan
> D. D. Chamberlin
> R. A. Lorie
> T. G. Price
>
> IBM Research Laboratory, San Jose, California 95193
>
> ABSTRACT: In a high-level query and data manipulation language such as SQL, requests are expressed nonprocedurally, without reference to access paths. This paper describes how System R selects access paths for both simple queries (a single relation) and complex queries (such as joins), with a user specification of the desired data in the form of a boolean expression of predicates. System R is an experimental database management system developed to conduct research on the relational data model. System R was designed and built by members of the IBM San Jose Research Laboratory.

### `content/vi/yeh-1991-branchprediction/00_front.md`

every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.

- material: the original says prediction misses cause serious performance degradation because much speculative work must be discarded, the back-translation says the discarded speculative work causes the mispredictions.

The English as it stands:

> There is serious performance degradation in deep-pipelined and/or superscalar machines caused by prediction misses due to the large amount of speculative work that has to be discarded [1, 8]. This is the motivation for proposing a new, higher-accuracy dynamic branch prediction scheme. The new scheme uses two levels of branch history information to make predictions. The first level is the history of the last $n$ branches. The second is the branch behavior for the last $s$ occurrences of that unique pattern of the last $n$ branches. The history information is collected on the fly without executing the program beforehand, eliminating the major disadvantage of Static Training Prediction. The scheme proposed here is called Two-Level Adaptive Training Branch Prediction, because predictions are based not only on the record of the last $n$ branches, but moreover on the record of the last $s$ occurrences of the particular record of the last $n$ branches.
>
> Trace-driven simulations were used in this study. The Two-Level Adaptive Training branch prediction scheme as well as the other dynamic and static branch prediction schemes were simulated on the SPEC benchmark suite. By using Two-Level Adaptive Training Branch Prediction, the average prediction accuracy for the benchmarks reaches 97 percent, while most of the other schemes achieve under 93 percent. This represents more than 100 percent reduction in mispredictions by using the Two-Level Adaptive Training scheme. This reduction can lead directly to a large performance gain on a high-performance processor.

What came back:

> There is serious performance degradation in deeply pipelined and/or superscalar machines due to mispredictions caused by the large amount of speculative work that must be discarded [1, 8]. This is the motivation for proposing a new dynamic branch prediction scheme with higher accuracy. The new scheme uses two levels of branch history information to make predictions. The first level is the history of the $n$ most recent branches. The second level is the behavior of the branch in the $s$ most recent occurrences of that unique pattern of the $n$ most recent branches. History information is collected directly during execution without requiring prior execution of the program, eliminating the main disadvantage of Static Training Prediction. The scheme proposed here is called Two-Level Adaptive Training Branch Prediction, because the predictions are based not only on the record of the $n$ most recent branches, but also on the record of the $s$ most recent occurrences of the specific record of the $n$ most recent branches.
>
> Trace-driven simulations were used in this study. The Two-Level Adaptive Training branch prediction scheme as well as other dynamic and static branch prediction schemes were simulated on the SPEC benchmark suite. By using Two-Level Adaptive Training Branch Prediction, the average prediction accuracy for the benchmarks reached 97 percent, while most other schemes achieved less than 93 percent. This represents a reduction of more than 100 percent in the number of mispredictions when using the Two-Level Adaptive Training scheme. This reduction can directly lead to a large performance increase on a high-performance processor.

## Differs in wording

### `content/vi/barham-2003-xen/00_front.md`

every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.

- wording: the original says “commodity operating systems,” the back-translation says “popular operating systems.”

The English as it stands:

> Xen and the Art of Virtualization
>
> Paul Barham*, Boris Dragovic, Keir Fraser, Steven Hand, Tim Harris,
>
> Alex Ho, Rolf Neugebauer†, Ian Pratt, Andrew Warfield
>
> University of Cambridge Computer Laboratory
>
> 15 JJ Thomson Avenue, Cambridge, UK, CB3 0FD
>
> {firstname.lastname}@cl.cam.ac.uk
>
> ABSTRACT
>
> Numerous systems have been designed which use virtualization to subdivide the ample resources of a modern computer. Some require specialized hardware, or cannot support commodity operating systems. Some target 100% binary compatibility at the expense of performance. Others sacrifice security or functionality for speed. Few offer resource isolation or performance guarantees; most provide only best-effort provisioning, risking denial of service.
>
> This paper presents Xen, an x86 virtual machine monitor which allows multiple commodity operating systems to share conventional hardware in a safe and resource managed fashion, but without sacrificing either performance or functionality. This is achieved by providing an idealized virtual machine abstraction to which operating systems such as Linux, BSD and Windows XP, can be ported with minimal effort.
>
> Our design is targeted at hosting up to 100 virtual machine instances simultaneously on a modern server. The virtualization approach taken by Xen is extremely efficient: we allow operating systems such as Linux and Windows XP to be hosted simultaneously for a negligible performance overhead — at most a few percent compared with the unvirtualized case. We considerably outperform competing commercial and freely available solutions in a range of microbenchmarks and system-wide tests.
>
> Categories and Subject Descriptors
>
> D.4.1 [Operating Systems]: Process Management; D.4.2 [Operating Systems]: Storage Management; D.4.8 [Operating Systems]: Performance

What came back:

> Xen and the Art of Virtualization
>
> Paul Barham*, Boris Dragovic, Keir Fraser, Steven Hand, Tim Harris,
>
> Alex Ho, Rolf Neugebauer†, Ian Pratt, Andrew Warfield
>
> University of Cambridge Computer Laboratory
>
> 15 JJ Thomson Avenue, Cambridge, UK, CB3 0FD
>
> {firstname.lastname}@cl.cam.ac.uk
>
> ABSTRACT
>
> Many systems have been designed using virtualization to partition the abundant resources of a modern computer. Some require specialized hardware, or cannot support popular operating systems. Some aim for 100% binary compatibility at the cost of performance. Other systems sacrifice security or functionality in exchange for speed. Very few systems provide resource isolation or performance guarantees; most only provide best-effort allocation, leading to the risk of denial of service.
>
> This paper presents Xen, an x86 virtual machine monitor that allows multiple popular operating systems to share conventional hardware in a secure and resource-managed manner, but without sacrificing either performance or functionality. This is achieved by providing an ideal virtual machine abstraction to which operating systems such as Linux, BSD and Windows XP can be ported with minimal effort.
>
> Our design aims to host up to 100 virtual machine instances simultaneously on a modern server. The virtualization approach used by Xen is extremely efficient: we allow operating systems such as Linux and Windows XP to be hosted simultaneously with negligible performance overhead — at most only a few percent compared with the non-virtualized case. We significantly outperform competing commercial solutions and freely available solutions across a range of microbenchmarks and system-wide tests.
>
> Categories and Subject Descriptors
>
> D.4.1 [Operating Systems]: Process Management; D.4.2 [Operating Systems]: Storage Management; D.4.8 [Operating Systems]: Performance

### `content/vi/brin-1998-pagerank/00_front.md`

every abstract is checked, translated by gpt-6-astra, put back by gpt-6-astra, judged by gpt-6-astra. The fleet had nothing else free, so this is a model marking its own work.

- wording: the original says Google makes heavy use of hypertext structure, the back-translation says it makes full use of that structure.
- wording: the original says a comparable number of distinct terms, the back-translation says a comparable number of distinct words.

The English as it stands:

> The anatomy of a large-scale hypertextual Web search engine $^1$
>
> Sergey Brin $^2$, Lawrence Page $^*,2$
>
> Computer Science Department, Stanford University, Stanford, CA 94305, USA
>
> Abstract
>
> In this paper, we present Google, a prototype of a large-scale search engine which makes heavy use of the structure present in hypertext. Google is designed to crawl and index the Web efficiently and produce much more satisfying search results than existing systems. The prototype with a full text and hyperlink database of at least 24 million pages is available at http://google.stanford.edu/
>
> To engineer a search engine is a challenging task. Search engines index tens to hundreds of millions of Web pages involving a comparable number of distinct terms. They answer tens of millions of queries every day. Despite the importance of large-scale search engines on the Web, very little academic research has been done on them. Furthermore, due to rapid advance in technology and Web proliferation, creating a Web search engine today is very different from three years ago. This paper provides an in-depth description of our large-scale Web search engine — the first such detailed public description we know of to date.
>
> Apart from the problems of scaling traditional search techniques to data of this magnitude, there are new technical challenges involved with using the additional information present in hypertext to produce better search results. This paper addresses this question of how to build a practical large-scale system which can exploit the additional information present in hypertext.

What came back:

> The structure of a large-scale hypertext web search engine $^1$
>
> Sergey Brin $^2$, Lawrence Page $^*,2$
>
> Department of Computer Science, Stanford University, Stanford, CA 94305, USA
>
> Abstract
>
> In this paper, we introduce Google, a prototype large-scale search engine that makes full use of the structure present in hypertext (hypertext). Google is designed to crawl and index (indexing) the web efficiently, while producing search results that are much more satisfactory than existing systems. The prototype with a full-text and hyperlink database of at least 24 million pages is available at http://google.stanford.edu/
>
> Building a search engine is a challenging task. Search engines index tens to hundreds of millions of web pages with a comparable number of distinct words. They answer tens of millions of queries every day. Although large-scale search engines play an important role on the web, there is still very little academic research about them. Furthermore, due to the rapid advancement of technology and the strong growth of the web, building a web search engine today is very different from three years ago. This paper describes our large-scale web search engine in depth — the first such detailed public description that we know of to date.
>
> In addition to the problems of scaling traditional search techniques to handle data at this scale, there are new technical challenges in using the additional information present in hypertext to produce better search results. This paper addresses the question of how to build a practical large-scale system that can exploit the additional information present in hypertext.

### `content/vi/cerf-1974-tcpip/00_front.md`

every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.

- wording: the original says the protocol accommodates variation in individual network packet sizes, the back-translation says it allows changes to the packet size of each network.

The English as it stands:

> A Protocol for Packet Network Intercommunication
>
> Abstract — A protocol that supports the sharing of resources that exist in different packet switching networks is presented. The protocol provides for variation in individual network packet sizes, transmission failures, sequencing, flow control, end-to-end error checking, and the creation and destruction of logical process-to-process connections. Some implementation issues are considered, and problems such as internetwork routing, accounting, and timeouts are exposed.

What came back:

> A protocol for the interconnection of packet networks
>
> Abstract — A protocol is presented that supports the sharing of resources existing in different packet-switched networks. This protocol allows changes to the packet size of each network, handles transmission failures, sequencing, flow control, end-to-end error checking, as well as the creation and destruction of logical connections between processes. Some implementation issues are considered, while issues such as internetwork routing, accounting, and timeouts are raised.

### `content/vi/codd-1970-relational/00_front.md`

every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.

- wording: the original says a prompting service supplying such information is not satisfactory, the back-translation says a reminder service providing such information is not satisfactory.

The English as it stands:

> A Relational Model of Data for Large Shared Data Banks
>
> E. F. Codd
> IBM Research Laboratory, San Jose, California
>
> Future users of large data banks must be protected from having to know how the data is organized in the machine (the internal representation). A prompting service which supplies such information is not a satisfactory solution. Activities of users at terminals and most application programs should remain unaffected when the internal representation of data is changed and even when some aspects of the external representation are changed. Changes in data representation will often be needed as a result of changes in query, update, and report traffic and natural growth in the types of stored information.
>
> Existing noninferential, formatted data systems provide users with tree-structured files or slightly more general network models of the data. In Section 1, inadequacies of these models are discussed. A model based on n-ary relations, a normal form for data base relations, and the concept of a universal data sublanguage are introduced. In Section 2, certain operations on relations (other than logical inference) are discussed and applied to the problems of redundancy and consistency in the user's model.
>
> KEY WORDS AND PHRASES: data bank, data base, data structure, data organization, hierarchies of data, networks of data, relations, derivability, redundancy, consistency, composition, join, retrieval language, predicate calculus, security, data integrity
> CR CATEGORIES: 3.70, 3.73, 3.75, 4.20, 4.22, 4.29

What came back:

> The relational model of data for large shared data banks
>
> E. F. Codd
> IBM Research Laboratory, San Jose, California
>
> Future users of large data banks must be protected from having to know how the data is organized in the machine (internal representation). A reminder service providing such information is not a satisfactory solution. Users' activities at terminals and most application programs should be unaffected when the internal representation of data is changed and even when some aspects of the external representation are changed. Changes in data representation will often be necessary due to changes in the traffic of queries, updates, and reports, as well as natural growth in the types of information stored.
>
> Existing formatted, noninferential data systems provide users with tree-structured files or slightly more general network models of data. In Section 1, the inadequacies of these models are discussed. A model based on n-ary relations, a normal form for database relations, and the concept of a universal data sublanguage are introduced. In Section 2, some operations on relations (other than logical inference) are discussed and applied to the problems of redundancy and consistency in the user's model.
>
> KEY WORDS AND PHRASES: data banks, databases, data structures, data organization, hierarchies of data, networks of data, relations, derivability, redundancy, consistency, composition, join, retrieval language, predicate calculus, security, data integrity
> CR CLASSIFICATION: 3.70, 3.73, 3.75, 4.20, 4.22, 4.29

### `content/vi/corbett-2012-spanner/08_conclusions.md`

the 5% sample, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.

- wording: the original says “reifying clock uncertainty in the time API,” the back-translation says “realizing clock uncertainty in the time API.”

The English as it stands:

> To summarize, Spanner combines and extends on ideas from two research communities: from the database community, a familiar, easy-to-use, semi-relational interface, transactions, and an SQL-based query language; from the systems community, scalability, automatic sharding, fault tolerance, consistent replication, external consistency, and wide-area distribution. Since Spanner’s inception, we have taken more than 5 years to iterate to the current design and implementation. Part of this long iteration phase was due to a slow realization that Spanner should do more than tackle the problem of a globally-replicated namespace, and should also focus on database features that Bigtable was missing.
>
> One aspect of our design stands out: the linchpin of Spanner’s feature set is TrueTime. We have shown that reifying clock uncertainty in the time API makes it possible to build distributed systems with much stronger time semantics. In addition, as the underlying system enforces tighter bounds on clock uncertainty, the overhead of the stronger semantics decreases. As a community, we should no longer depend on loosely synchronized clocks and weak time APIs in designing distributed algorithms.

What came back:

> In summary, Spanner combines and extends ideas from two research communities: from the database community, a familiar, easy-to-use semi-relational interface, transactions, and an SQL-based query language; from the systems community, scalability, automatic sharding, fault tolerance, consistent replication, external consistency, and wide-area distribution. Since Spanner came into being, we have spent more than 5 years iterating through versions to reach the current design and implementation. Part of this long iteration period is due to the slow realization that Spanner should do more than solve the problem of a globally replicated namespace, and should also focus on the database features that Bigtable lacks.
>
> One aspect of our design stands out: the key element in Spanner's feature set is TrueTime. We have shown that realizing clock uncertainty in the time API makes it possible to build distributed systems with much stronger time semantics. In addition, when the underlying system imposes tighter bounds on clock uncertainty, the overhead of stronger semantics will decrease. As a community, we should no longer depend on loosely synchronized clocks and weak time APIs in designing distributed algorithms.

### `content/vi/decandia-2007-dynamo/00_front.md`

every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.

- wording: the original says “persistent state,” the back-translation says “long-term state.”

The English as it stands:

> Dynamo: Amazon’s Highly Available Key-value Store
>
> Giuseppe DeCandia, Deniz Hastorun, Madan Jampani, Gunavardhan Kakulapati, Avinash Lakshman, Alex Pilchin, Swaminathan Sivasubramanian, Peter Vosshall and Werner Vogels
> Amazon.com
>
> ABSTRACT
> Reliability at massive scale is one of the biggest challenges we face at Amazon.com, one of the largest e-commerce operations in the world; even the slightest outage has significant financial consequences and impacts customer trust. The Amazon.com platform, which provides services for many web sites worldwide, is implemented on top of an infrastructure of tens of thousands of servers and network components located in many datacenters around the world. At this scale, small and large components fail continuously and the way persistent state is managed in the face of these failures drives the reliability and scalability of the software systems.
>
> This paper presents the design and implementation of Dynamo, a highly available key-value storage system that some of Amazon’s core services use to provide an “always-on” experience. To achieve this level of availability, Dynamo sacrifices consistency under certain failure scenarios. It makes extensive use of object versioning and application-assisted conflict resolution in a manner that provides a novel interface for developers to use.
>
> Categories and Subject Descriptors
> D.4.2 [Operating Systems]: Storage Management; D.4.5 [Operating Systems]: Reliability; D.4.2 [Operating Systems]: Performance;
>
> General Terms
> Algorithms, Management, Measurement, Performance, Design, Reliability.

What came back:

> Dynamo: Amazon’s Highly Available Key-Value Store
>
> Giuseppe DeCandia, Deniz Hastorun, Madan Jampani, Gunavardhan Kakulapati, Avinash Lakshman, Alex Pilchin, Swaminathan Sivasubramanian, Peter Vosshall and Werner Vogels
> Amazon.com
>
> ABSTRACT
> Reliability at extremely large scale is one of the greatest challenges we face at Amazon.com, one of the world’s largest e-commerce operations; even the smallest disruption causes significant financial consequences and affects customer trust. The Amazon.com platform, which provides services to many websites worldwide, is deployed on an infrastructure consisting of tens of thousands of servers and network components located in multiple data centers around the world. At this scale, large and small components continually fail, and the way long-term state is managed in the face of these failures determines the reliability and scalability of software systems.
>
> This paper presents the design and implementation of Dynamo, a highly available key-value storage system that some of Amazon’s core services use to provide an “always-on” experience. To achieve this level of availability, Dynamo sacrifices consistency in certain failure scenarios. The system makes extensive use of object versioning and application-assisted conflict resolution, in a manner that provides a new interface for developers to use.
>
> Categories and Subject Descriptors
> D.4.2 [Operating Systems]: Storage Management; D.4.5 [Operating Systems]: Reliability; D.4.2 [Operating Systems]: Performance;
>
> General Terms
> Algorithms, Management, Measurement, Performance, Design, Reliability.

### `content/vi/deutsch-1984-smalltalk/00_front.md`

every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.

- wording: the original says “universally polymorphic procedures,” the back-translation says “fully polymorphic procedures.”

The English as it stands:

> Efficient Implementation of the Smalltalk-80 System
>
> L. Peter Deutsch
> Xerox PARC, Software Concepts Group
>
> Allan M. Schiffman
> Fairchild Laboratory for Artificial Intelligence Research
>
> ABSTRACT
>
> The Smalltalk-80* programming language includes dynamic storage allocation, full upward funargs, and universally polymorphic procedures; the Smalltalk-80 programming system features interactive execution with incremental compilation, and implementation portability. These features of modern programming systems are among the most difficult to implement efficiently, even individually. A new implementation of the Smalltalk-80 system, hosted on a small microprocessor-based computer, achieves high performance while retaining complete (object code) compatibility with existing implementations. This paper discusses the most significant optimization techniques developed over the course of the project, many of which are applicable to other languages. The key idea is to represent certain runtime state (both code and data) in more than one form, and to convert between forms when needed.
>
> *Smalltalk-80 is a trademark of the Xerox Corporation.

What came back:

> Efficient Implementation of the Smalltalk-80 System
>
> L. Peter Deutsch  
> Xerox PARC, Software Concepts Group
>
> Allan M. Schiffman  
> Fairchild Laboratory for Artificial Intelligence Research
>
> ABSTRACT
>
> The Smalltalk-80* programming language includes dynamic memory allocation, full upward funargs, and fully polymorphic procedures; the Smalltalk-80 programming system features interactive execution with incremental compilation, and portability in implementation. These features of modern programming systems are among the most difficult features to implement efficiently, even when considered individually. A new implementation of the Smalltalk-80 system, hosted on a microprocessor-based small computer, achieves high performance while maintaining complete (object code) compatibility with existing implementations. This paper discusses the most important optimization techniques developed in the course of carrying out the project, many of which can be applied to other languages. The key idea is to represent some runtime state (both code and data) in multiple different forms, and convert between the forms as needed.
>
> *Smalltalk-80 is a trademark of Xerox Corporation.

### `content/vi/gal-2009-tracejit/00_front.md`

every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.

- wording: the original says machine code is generated “on the fly,” the back-translation says it is generated “immediately.”

The English as it stands:

> Trace-based Just-in-Time Type Specialization for Dynamic Languages
>
> Andreas Gal*+, Brendan Eich*, Mike Shaver*, David Anderson*, David Mandelin*, Mohammad R. Haghighat\$, Blake Kaplan*, Graydon Hoare*, Boris Zbarsky*, Jason Orendorff*, Jesse Ruderman*, Edwin Smith#, Rick Reitmaier#, Michael Bebenita+, Mason Chang+#, Michael Franz+
>
> Mozilla Corporation*
>
> {gal,brendan,shaver,danderson,dmandelin,mrbkap,graydon,bz,jorendorff,jruderman}@mozilla.com
>
> Adobe Corporation#
>
> {edwsmith,rreitmai}@adobe.com
>
> Intel Corporation\$
>
> {mohammad.r.haghighat}@intel.com
>
> University of California, Irvine+
>
> {mbebenit,changm,franz}@uci.edu
>
> Abstract
>
> Dynamic languages such as JavaScript are more difficult to compile than statically typed ones. Since no concrete type information is available, traditional compilers need to emit generic code that can handle all possible type combinations at runtime. We present an alternative compilation technique for dynamically-typed languages that identifies frequently executed loop traces at run-time and then generates machine code on the fly that is specialized for the actual dynamic types occurring on each path through the loop. Our method provides cheap inter-procedural type specialization, and an elegant and efficient way of incrementally compiling lazily discovered alternative paths through nested loops. We have implemented a dynamic compiler for JavaScript based on our technique and we have measured speedups of 10x and more for certain benchmark programs.
>
> Categories and Subject Descriptors D.3.4 [Programming Languages]: Processors — Incremental compilers, code generation.
>
> General Terms Design, Experimentation, Measurement, Performance.
>
> Keywords JavaScript, just-in-time compilation, trace trees.
>
> 1. Introduction
>
> Dynamic languages such as JavaScript, Python, and Ruby, are popular since they are expressive, accessible to non-experts, and make deployment as easy as distributing a source file. They are used for small scripts as well as for complex applications.

What came back:

> Trace-based Just-in-Time Type Specialization for Dynamic Languages
>
> Andreas Gal*+, Brendan Eich*, Mike Shaver*, David Anderson*, David Mandelin*, Mohammad R. Haghighat\$, Blake Kaplan*, Graydon Hoare*, Boris Zbarsky*, Jason Orendorff*, Jesse Ruderman*, Edwin Smith#, Rick Reitmaier#, Michael Bebenita+, Mason Chang+#, Michael Franz+
>
> Mozilla Corporation*
>
> {gal,brendan,shaver,danderson,dmandelin,mrbkap,graydon,bz,jorendorff,jruderman}@mozilla.com
>
> Adobe Corporation#
>
> {edwsmith,rreitmai}@adobe.com
>
> Intel Corporation\$
>
> {mohammad.r.haghighat}@intel.com
>
> University of California, Irvine+
>
> {mbebenit,changm,franz}@uci.edu
>
> Abstract
>
> Dynamic languages such as JavaScript are harder to compile than statically typed languages. Because there is no concrete type information, traditional compilers need to generate general code that can handle every possible combination of types at runtime. We present an alternative compilation technique for dynamically typed languages, which identifies frequently executed loop traces at runtime and then immediately generates machine code specialized for the actual dynamic types that appear on each path through the loop. Our method provides low-cost interprocedural type specialization, along with an elegant and efficient way to incrementally compile lazily discovered alternative paths through nested loops. We have implemented a dynamic compiler for JavaScript based on our technique and have measured speedups of 10x or more for some benchmark programs.
>
> Categories and Subject Descriptors D.3.4 [Programming Languages]: Processors — Incremental compilers, code generation.
>
> General Terms Design, Experimentation, Measurement, Performance.
>
> Keywords JavaScript, just-in-time compilation, trace trees.
>
> 1. Introduction
>
> Dynamic languages such as JavaScript, Python, and Ruby are popular because they are expressive, accessible to non-experts, and make deployment as easy as distributing a source code file. They are used for small scripts as well as complex applications.

### `content/vi/graefe-1994-volcano/00_front.md`

every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.

- wording: the original says support-function semantics are not prescribed, the back-translation says they are not specified in advance.
- wording: the original says Volcano effectively combines extensibility and parallelism, the back-translation says Volcano is capable of effectively combining them.

The English as it stands:

> Volcano—An Extensible and Parallel Query Evaluation System
>
> Goetz Graefe
>
> Abstract—To investigate the interactions of extensibility and parallelism in database query processing, we have developed a new dataflow query execution system called Volcano. The Volcano effort provides a rich environment for research and education in database systems design, heuristics for query optimization, parallel query execution, and resource allocation.
>
> Volcano uses a standard interface between algebra operators, allowing easy addition of new operators and operator implementations. Operations on individual items, e.g., predicates, are imported into the query processing operators using support functions. The semantics of support functions is not prescribed; any data type including complex objects and any operation can be realized. Thus, Volcano is extensible with new operators, algorithms, data types, and type-specific methods.
>
> Volcano includes two novel meta-operators. The choose-plan meta-operator supports dynamic query evaluation plans that allow delaying selected optimization decisions until run-time, e.g., for embedded queries with free variables. The exchange meta-operator supports intra-operator parallelism on partitioned datasets and both vertical and horizontal inter-operator parallelism, translating between demand-driven dataflow within processes and data-driven dataflow between processes.
>
> All operators, with the exception of the exchange operator, have been designed and implemented in a single-process environment, and parallelized using the exchange operator. Even operators not yet designed can be parallelized using this new operator if they use and provide the interator interface. Thus, the issues of data manipulation and parallelism have become orthogonal, making Volcano the first implemented query execution engine that effectively combines extensibility and parallelism.

What came back:

> Volcano—An Extensible and Parallel Query Evaluation System
>
> Goetz Graefe
>
> Abstract—To study the interactions between extensibility and parallelism in database query processing, we have developed a new dataflow query execution system called Volcano. The Volcano effort provides a rich environment for research and education on database system design, heuristics for query optimization, parallel query execution, and resource allocation.
>
> Volcano uses a standard interface between algebraic operators, allowing easy addition of new operators and operator implementations. Operations on individual items, for example predicates, are imported into query processing operators using support functions. The semantics of the support functions are not specified in advance; any data type including complex objects and any operation can be implemented. Therefore, Volcano is extensible with new operators, algorithms, data types, and type-specific methods.
>
> Volcano includes two new meta-operators. The choose-plan meta-operator supports dynamic query evaluation plans, allowing selected optimization decisions to be delayed until runtime, for example for embedded queries with free variables. The exchange meta-operator supports intra-operator parallelism on partitioned datasets and both vertical and horizontal inter-operator parallelism, converting between demand-driven dataflow within processes and data-driven dataflow between processes.
>
> All operators, except the exchange operator, have been designed and implemented in a single-process environment, and parallelized using the exchange operator. Even operators that have not yet been designed can be parallelized using this new operator if they use and provide the interator interface. Therefore, the issues of data manipulation and parallelism have become orthogonal, making Volcano the first implemented query execution engine capable of effectively combining extensibility and parallelism.

### `content/vi/hamming-1950-codes/00_front.md`

every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.

- wording: the original says the failure escapes routine checking, the back-translation says it escapes periodic checking.

The English as it stands:

> Error Detecting and Error Correcting Codes
>
> By R. W. HAMMING
>
> 1. Introduction
>
> The author was led to the study given in this paper from a consideration of large scale computing machines in which a large number of operations must be performed without a single error in the end result. This problem of "doing things right" on a large scale is not essentially new; in a telephone central office, for example, a very large number of operations are performed while the errors leading to wrong numbers are kept well under control, though they have not been completely eliminated. This has been achieved, in part, through the use of self-checking circuits. The occasional failure that escapes routine checking is still detected by the customer and will, if it persists, result in customer complaint, while if it is transient it will produce only occasional wrong numbers. At the same time the rest of the central office functions satisfactorily. In a digital computer, on the other hand, a single failure usually means the complete failure, in the sense that if it is detected no more computing can be done until the failure is located and corrected, while if it escapes detection then it invalidates all subsequent operations of the machine.

What came back:

> Error-detecting codes and error-correcting codes
>
> By R. W. HAMMING
>
> 1. Introduction
>
> The author was led to the research presented in this paper from considering large-scale computers, in which a large number of operations must be performed without a single error in the final result. The problem of "doing everything right" on this large scale is fundamentally not new; for example, in a telephone exchange, a very large number of operations are performed while errors leading to wrong numbers are very tightly controlled, although they have not been completely eliminated. This has been achieved in part through the use of self-checking circuits. The occasional failure that escapes periodic checking is still detected by the customer and will, if prolonged, lead to a customer complaint, while if it is temporary it only produces occasional wrong numbers. At the same time, the remaining functions of the exchange still operate satisfactorily. On the other hand, in a digital computer, a single failure usually means complete breakdown, in the sense that if it is detected then no further computation can be performed until the failure is identified and repaired, while if it escapes detection then it invalidates all subsequent operations of the machine.

### `content/vi/jouppi-2017-tpu/08_discussion.md`

the 5% sample, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.

- wording: the original says CPU and GPU results would be “comparable to” the TPU under the stated conditions, the back-translation says they would be “equivalent to” the TPU.

The English as it stands:

> This section follows the fallacy and pitfall with rebuttal style of [Hen18].
> • *Fallacy*: *NN inference applications in datacenters value throughput as much as response time.*
> We were surprised that our developers had strong response-time demands, as some suggested in 2014 that batch sizes would be large enough for the TPU to reach peak performance or that latency requirements wouldn’t be as tight. One driving application was off-line image processing, and the intuition was that if interactive services also wanted TPUs, most of them would just accumulate larger batches. Even the developers of one application in 2014 that cared about response time (LSTM1) said the limit was 10 ms in 2014, but shrank it to 7 ms when they actually ported it to the TPU. The unexpected desire for TPUs by many such services combined with the impact on and preference for low response time changed the equation, with application writers often opting for reduced latency over waiting for bigger batches to accumulate. Fortunately, the TPU has a simple and repeatable execution model to help meet the response-time targets of interactive services and such high peak throughput that even small batch sizes result in higher performance than contemporary CPUs and GPUs.
> • *Fallacy*: *The K80 GPU architecture is a good match to NN inference.*
> GPUs have traditionally been seen as high-throughput architectures that rely on high-bandwidth DRAM and thousands of threads to achieve their goals. This perspective helps explain why the K80 is only a little faster at inference than Haswell and much slower than the TPU. Successors to the K80 will surely include optimizations to improve peak inference performance, but given their throughput-oriented architectural approach, it may be more challenging for GPUs to meet the strict latency limits. And as Section 7 shows, there is plenty of headroom to improve the TPU, so it’s not an easy target.
>
> • *Pitfall: Architects have neglected important NN tasks.*
> We are pleased by the attention that the architecture community is paying to NN: 15% of the papers at ISCA 2016 were on hardware accelerators for NN [Alb16] [Che16a][Chi16][Han16][Kim16][LiK16][Liu16][Rea16] [Sha16]! Alas, all nine papers looked at CNNs, and only two mentioned other NNs. CNNs are more complex than MLPs and prominent in NN competitions [Rus15], which might explain their allure, but they are only about 5% of our datacenter NN workload. While CNNs may be common in edge devices, the volume of convolutional models hasn’t yet caught up with MLPs and LSTMs in the datacenter. We hope that architects try to accelerate MLPs and LSTMs with at least as much gusto.
> • *Pitfall: For NN hardware, Inferences Per Second (IPS) is an inaccurate summary performance metric.*
> Our results show that IPS is a poor overall performance summary for NN hardware, as it’s simply the inverse of the complexity of the typical inference in the application (e.g., the number, size, and type of NN layers). For example, the TPU runs the 4-layer MLP1 at 360,000 IPS but the 89-layer CNN1 at only 4,700 IPS, so TPU IPS vary by 75X! Thus, using IPS as the single-speed summary is *even more misleading* for NN accelerators than MIPS or FLOPS are for regular processors [Hen18], so IPS should be even more disparaged. To compare NN machines better, we need a benchmark suite written at a high-level to port it to the wide variety of NN architectures. Fathom is a promising new attempt at such a benchmark suite [Ado16].
> • *Fallacy: The K80 GPU results would be much better if Boost mode were enabled.*
> Setting aside the negative impact of K80 Boost mode on TCO (Section 3), we measured it on LSTM1. Boost mode increased the clock rate by a factor of up to 1.6—from 560 to 875 MHz—which increased performance by 1.4X, but it also raised power by 1.3X. The net gain in performance/Watt is 1.1X, and thus for LSTM1, boost mode would have a minor impact on our energy-speed analysis.
> • *Fallacy: CPU and GPU results would be comparable to the TPU if we used them more efficiently or compared to newer versions.*
> We originally had 8-bit results for just one DNN on the CPU, due to the significant work to use AVX2 integer support efficiently. The benefit was ~3.5X. It was less confusing (and less space) to present all CPU results in floating point, rather than having one exception, with its own roofline. If all DNNs had similar speedup, performance/Watt ratio would drop from 41-83X to 12-24X. The new 16-nm, 1.5GHz, 250W P40 datacenter GPU can perform 47 Tera 8-bit ops/sec, but was unavailable in early 2015, so isn’t contemporary with our three platforms. We also can’t know the fraction of P40 peak delivered within our rigid time bounds. If we compared newer chips, Section 7 shows that we could triple performance of the 28-nm, 0.7GHz, 40W TPU just by using the K80’s GDDR5 memory (at a cost of an additional 10W).
> • *Pitfall: Performance counters added as an afterthought for NN hardware.*
> The TPU has 106 performance counters, and if anything we would like a few more (see Table 3). The raison d'etre for NN accelerators is performance, and it is way too early in their evolution to have good intuition about what is going on.
> • *Fallacy: After two years of software tuning, the only path left to increase TPU performance is hardware upgrades.*
> The performance of CNN1 on the TPU could improve if developers and compiler writers did more work to match CNN1 to the TPU hardware. For example, developers could reorganize the applications to aggregate multiple short batches out of the convolution layers into a single, deeper batch (from 32 to 128) for the four fully connected layers. Such a single layer would improve utilization of the matrix unit (Table 3). As CNN1 currently runs more than 70 times faster on the TPU than the CPU, the CNN1 developers are already very happy, so it’s not clear whether or when such optimizations would be performed.

What came back:

> This section follows the rebuttal style of [Hen18] for fallacies and pitfalls.
> • *Fallacy*: *NN inference applications in datacenters value throughput as much as response time.*
> We were very surprised that our developers had strong requirements for response time, because some people had proposed in 2014 that batch sizes would be large enough for the TPU to reach peak performance or that latency requirements would not be too tight. One motivating application was offline image processing, and the intuition was that if interactive services also wanted to use the TPU, most of them would just accumulate larger batches. Even the developers of an application in 2014 that cared about response time (LSTM1) said that the limit was 10 ms in 2014, but it had dropped to 7 ms when they actually moved it to the TPU. The unexpected desire for the TPU from many such services combined with the impact and priority given to low response time changed the equation, with application writers often choosing to reduce latency instead of waiting to accumulate larger batches. Fortunately, the TPU has a simple and repeatable execution model to help meet the response time targets of interactive services and has such high peak throughput that even small batch sizes produce higher performance than contemporary CPUs and GPUs.
> • *Fallacy*: *The K80 GPU architecture is a good fit for NN inference.*
> GPUs have traditionally been viewed as high-throughput architectures that rely on high-bandwidth DRAM and thousands of threads to achieve their goals. This perspective helps explain why the K80 is only slightly faster at inference than Haswell and much slower than the TPU. Successors to the K80 will certainly include optimizations to improve peak inference performance, but due to their throughput-oriented architectural approach, it may be more difficult for GPUs to meet strict latency limits. And as Section 7 points out, there is still much room to improve the TPU, so this is not an easy target.
>
> • *Pitfall: Architects have overlooked important NN tasks.*
> We are pleased with the attention that the architecture community is giving to NNs: 15% of the papers at ISCA 2016 were about hardware accelerators for NNs [Alb16] [Che16a][Chi16][Han16][Kim16][LiK16][Liu16][Rea16] [Sha16]! However, all nine papers considered CNNs, and only two mentioned other NNs. CNNs are more complex than MLPs and prominent in NN competitions [Rus15], which may explain their appeal, but they account for only about 5% of the NN workload in our datacenters. Although CNNs may be popular in edge devices, the volume of convolutional models has not yet caught up with MLPs and LSTMs in datacenters. We hope architects will try to accelerate MLPs and LSTMs with at least equal enthusiasm.
> • *Pitfall: For NN hardware, Inferences Per Second (IPS) is an inaccurate aggregate performance metric.*
> Our results show that IPS is a poor summary of overall performance for NN hardware, because it is simply the inverse of the complexity of typical inference in the application (for example: the number, size, and type of NN layers). For example, the TPU runs the 4-layer MLP1 at 360,000 IPS but the 89-layer CNN1 at only 4,700 IPS, so the TPU's IPS varies by 75X! Thus, using IPS as the sole speed metric is *even more misleading* for NN accelerators than MIPS or FLOPS are for conventional processors [Hen18], so IPS should be taken even less seriously. To compare NN machines better, we need a benchmark suite written at a high level to port it to many different NN architectures. Fathom is a promising new effort for such a benchmark suite [Ado16].
> • *Fallacy: The K80 GPU results would be much better if Boost mode were enabled.*
> Ignoring the negative impact of the K80's Boost mode on TCO (Section 3), we measured it on LSTM1. Boost mode increases the clock speed by a maximum factor of 1.6—from 560 to 875 MHz—increasing performance by 1.4X, but it also increases power by 1.3X. The net gain in performance/Watt is 1.1X, and thus for LSTM1, boost mode would have a small impact on our energy-speed analysis.
> • *Fallacy: The CPU and GPU results would be equivalent to the TPU if we used them more efficiently or compared with newer versions.*
> Initially we had 8-bit results for only one DNN on the CPU, due to the substantial amount of work needed to use AVX2 integer support effectively. The benefit was ~3.5X. Presenting all CPU results in floating point was less confusing (and took less space), instead of having one exception with its own roofline. If all DNNs had a similar speedup, the performance/Watt ratio would decrease from 41-83X to 12-24X. The new 16-nm, 1.5GHz, 250W P40 datacenter GPU can perform 47 Tera 8-bit ops/sec, but was not available in early 2015, so it is not contemporary with our three platforms. We also cannot know the fraction of the P40's peak delivered within our rigid time limits. If we compared newer chips, Section 7 shows that we could triple the performance of the 28-nm, 0.7GHz, 40W TPU just by using the K80's GDDR5 memory (at an additional cost of 10W).
> • *Pitfall: Performance counters are added as an afterthought for NN hardware.*
> The TPU has 106 performance counters, and if anything we would like a few more (see Table 3). The reason for existence of NN accelerators is performance, and it is too early in their development to have good intuition about what is happening.
> • *Fallacy: After two years of software tuning, the only remaining path to increasing TPU performance is to upgrade the hardware.*
> The performance of CNN1 on the TPU could be improved if developers and compiler writers did more work to match CNN1 to the TPU hardware. For example, developers could reorganize applications to aggregate many short batches from the convolutional layers into a single, deeper batch (from 32 to 128) for the four fully connected layers. Such a single layer would improve the utilization of the matrix unit (Table 3). Because CNN1 currently runs more than 70 times faster on the TPU than on the CPU, the CNN1 developers were very satisfied, so it is unclear whether or when such optimizations will be performed.

### `content/vi/lamport-1998-paxos/00_front.md`

every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.

- wording: the original labels category C2.4 “Computer-Communications Networks,” the back-translation labels it “Computer Networks.”

The English as it stands:

> The Part-Time Parliament
>
> Leslie Lamport
>
> This article appeared in ACM Transactions on Computer Systems 16, 2 (May 1998), 133-169. Minor corrections were made on 29 August 2000.
>
> The Part-Time Parliament
>
> LESLIE LAMPORT Digital Equipment Corporation
>
> Recent archaeological discoveries on the island of Paxos reveal that the parliament functioned despite the peripatetic propensity of its part-time legislators. The legislators maintained consistent copies of the parliamentary record, despite their frequent forays from the chamber and the forgetfulness of their messengers. The Paxon parliament’s protocol provides a new way of implementing the state-machine approach to the design of distributed systems. Categories and Subject Descriptors: C2.4 [Computer-Communications Networks]: Distributed Systems—Network operating systems; D4.5 [Operating Systems]: Reliability—Fault-tolerance; J.1 [Administrative Data Processing]: Government General Terms: Design, Reliability Additional Key Words and Phrases: State machines, three-phase commit, voting
>
> This submission was recently discovered behind a filing cabinet in the TOCS editorial office. Despite its age, the editor-in-chief felt that it was worth publishing. Because the author is currently doing field work in the Greek isles and cannot be reached, I was asked to prepare it for publication.
>
> The author appears to be an archeologist with only a passing interest in computer science. This is unfortunate; even though the obscure ancient Paxon civilization he describes is of little interest to most computer scientists, its legislative system is an excellent model for how to implement a distributed computer system in an asynchronous environment.

What came back:

> The Part-Time Parliament
>
> Leslie Lamport
>
> This paper appeared in ACM Transactions on Computer Systems 16, 2 (May 1998), 133-169. Minor corrections were made on August 29, 2000.
>
> The Part-Time Parliament
>
> LESLIE LAMPORT Digital Equipment Corporation
>
> Recent archaeological discoveries on the island of Paxos show that the parliament continued to operate despite the wandering tendencies of its part-time legislators. The legislators maintained consistent copies of the parliamentary records, despite frequently leaving the chamber and the absent-mindedness of the messengers. The protocol of the Paxon parliament provides a new method for implementing the state machine approach to designing distributed systems. Categories and Subject Descriptions: C2.4 [Computer Networks]: Distributed systems—Network operating systems; D4.5 [Operating Systems]: Reliability—Fault tolerance; J.1 [Administrative Data Processing]: Government General Terms: Design, Reliability Additional Keywords and Phrases: State machine, three-phase commit, voting
>
> This manuscript was recently discovered behind a filing cabinet in the TOCS editorial office. Although it is old, the editor-in-chief thought it was worth publishing. Because the author is currently conducting fieldwork on the Greek islands and cannot be contacted, I was asked to prepare the manuscript for publication.
>
> The author appears to be an archaeologist with only a passing interest in computer science. This is unfortunate; although the little-known ancient Paxon civilization that he describes is of little interest to most computer scientists, its legislative system is an excellent model for how to implement a distributed computer system in an asynchronous environment.

### `content/vi/savitch-1970-tape/00_front.md`

every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.

- wording: the original says computations correspond to “threadings” of mazes and refers to “threadable mazes,” the back-translation says “paths through” mazes and “mazes that can be traversed.”

The English as it stands:

> Relationships Between Nondeterministic and Deterministic Tape Complexities*
>
> Walter J. Savitch
>
> Department of Applied Physics and Information Science,
> University of California, San Diego, La Jolla, California 92037
>
> Received August 29, 1969
>
> The amount of storage needed to simulate a nondeterministic tape bounded Turing machine on a deterministic Turing machine is investigated. Results include the following: Theorem. A nondeterministic $L(n)$-tape bounded Turing machine can be simulated by a deterministic $[L(n)]^2$-tape bounded Turing machine, provided $L(n) \geq \log_2 n$. Computations of nondeterministic machines are shown to correspond to threadings of certain mazes. This correspondence is used to produce a specific set, namely the set of all codings of threadable mazes, such that, if there is any set which distinguishes nondeterministic tape complexity classes from deterministic tape complexity classes, then this is one such set.

What came back:

> The relationship between the tape complexity of nondeterministic and deterministic Turing machines*
>
> Walter J. Savitch
>
> Department of Applied Physics and Information Science,
> University of California, San Diego, La Jolla, California 92037
>
> Received August 29, 1969
>
> The amount of memory needed to simulate a tape-bounded nondeterministic Turing machine on a deterministic Turing machine is studied. The results include the following: Theorem. An $L(n)$ tape-bounded nondeterministic Turing machine can be simulated by an $[L(n)]^2$ tape-bounded deterministic Turing machine, provided that $L(n) \geq \log_2 n$. The computations of nondeterministic machines are shown to correspond to paths through certain mazes. This correspondence is used to produce a specific set, namely the set of all encodings of mazes that can be traversed, such that, if there exists a set distinguishing nondeterministic tape complexity classes from deterministic tape complexity classes, then this set is also such a set.

### `content/vi/stonebraker-2005-cstore/00_front.md`

every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.

- wording: the original title says “A Column-oriented DBMS,” the back-translation title says “A Column-Oriented Relational DBMS.”

The English as it stands:

> C-Store: A Column-oriented DBMS
>
> Mike Stonebraker*, Daniel J. Abadi*, Adam Batkin†, Xuedong Chen†, Mitch Cherniack†,  
> Miguel Ferreira*, Edmond Lau*, Amerson Lin*, Sam Madden*, Elizabeth O’Neil†,  
> Pat O’Neil†, Alex Rasin‡, Nga Tran†, Stan Zdonik‡
>
> *MIT CSAIL  
> Cambridge, MA
>
> †Brandeis University  
> Waltham, MA
>
> †UMass Boston  
> Boston, MA
>
> ‡Brown University  
> Providence, RI
>
> Abstract
>
> This paper presents the design of a read-optimized relational DBMS that contrasts sharply with most current systems, which are write-optimized. Among the many differences in its design are: storage of data by column rather than by row, careful coding and packing of objects into storage including main memory during query processing, storing an overlapping collection of column-oriented projections, rather than the current fare of tables and indexes, a non-traditional implementation of transactions which includes high availability and snapshot isolation for read-only transactions, and the extensive use of bitmap indexes to complement B-tree structures.
>
> We present preliminary performance data on a subset of TPC-H and show that the system we are building, C-Store, is substantially faster than popular commercial products. Hence, the architecture looks very encouraging.

What came back:

> C-Store: A Column-Oriented Relational DBMS
>
> Mike Stonebraker*, Daniel J. Abadi*, Adam Batkin†, Xuedong Chen†, Mitch Cherniack†,  
> Miguel Ferreira*, Edmond Lau*, Amerson Lin*, Sam Madden*, Elizabeth O’Neil†,  
> Pat O’Neil†, Alex Rasin‡, Nga Tran†, Stan Zdonik‡
>
> *MIT CSAIL  
> Cambridge, MA
>
> †Brandeis University  
> Waltham, MA
>
> †UMass Boston  
> Boston, MA
>
> ‡Brown University  
> Providence, RI
>
> Abstract
>
> This paper presents the design of a read-optimized relational DBMS, in sharp contrast to most current systems, which are write-optimized. Among the many differences in its design are: storing data by column instead of by row, carefully encoding and packing objects into storage including main memory during query processing, storing an overlapping set of column-oriented projections instead of the current approach with tables and indexes, an unconventional implementation of transactions including high availability and snapshot isolation for read-only transactions, along with extensive use of bitmap indexes to supplement B-tree structures.
>
> We present preliminary performance data on a subset of TPC-H and show that the system we are building, C-Store, is significantly faster than popular commercial products. Therefore, this architecture appears very promising.

## The same

- `content/vi/aho-1975-corasick/00_front.md` every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.
- `content/vi/amdahl-1967-law/00_front.md` every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.
- `content/vi/astrahan-1976-systemr/00_front.md` every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.
- `content/vi/backus-1978-vonneumann/00_front.md` every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.
- `content/vi/bayer-1972-btree/00_front.md` every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.
- `content/vi/bloom-1970-filter/00_front.md` every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.
- `content/vi/cook-1971-np/00_front.md` every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.
- `content/vi/cooley-1965-fft/00_front.md` every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.
- `content/vi/corbett-2012-spanner/00_front.md` every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.
- `content/vi/cytron-1991-ssa/00_front.md` every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.
- `content/vi/dean-2004-mapreduce/00_front.md` every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.
- `content/vi/dennard-1974-scaling/00_front.md` every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.
- `content/vi/denning-1968-workingset/00_front.md` every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.
- `content/vi/dewitt-1990-gamma/00_front.md` every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.
- `content/vi/dijkstra-1959-shortestpath/00_front.md` every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.
- `content/vi/dijkstra-1968-the/00_front.md` every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.
- `content/vi/floyd-1962-shortestpath/00_front.md` every abstract is checked, translated by gpt-6-astra, put back by gpt-6-astra, judged by gpt-6-astra. The fleet had nothing else free, so this is a model marking its own work.
- `content/vi/ford-1956-maxflow/00_front.md` every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.
- `content/vi/ghemawat-2003-gfs/00_front.md` every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.
- `content/vi/goldwasser-1985-zk/00_front.md` every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.
- `content/vi/goodfellow-2014-gan/00_front.md` every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.
- `content/vi/hoare-1962-quicksort/00_front.md` every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.
- `content/vi/hoare-1969-axiomatic/00_front.md` every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.
- `content/vi/jouppi-1990-victimcache/00_front.md` every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.
- `content/vi/jouppi-2017-tpu/00_front.md` every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.
- `content/vi/karp-1972-reducibility/00_front.md` every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.
- `content/vi/knuth-1977-kmp/00_front.md` every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.
- `content/vi/lamport-1978-clocks/00_front.md` every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.
- `content/vi/mccarthy-1960-lisp/00_front.md` every abstract is checked, translated by gpt-6-astra, put back by gpt-6-astra, judged by gpt-6-astra. The fleet had nothing else free, so this is a model marking its own work.
- `content/vi/mckeown-2008-openflow/00_front.md` every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.
- `content/vi/metcalfe-1976-ethernet/00_front.md` every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.
- `content/vi/mohan-1992-aries/00_front.md` every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.
- `content/vi/nagle-1984-congestion/00_front.md` every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.
- `content/vi/ongaro-2014-raft/00_front.md` every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.
- `content/vi/razborov-1997-naturalproofs/00_front.md` every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.
- `content/vi/ritchie-1974-unix/00_front.md` every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.
- `content/vi/saltzer-1984-endtoend/00_front.md` every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.
- `content/vi/shannon-1948-communication/00_front.md` every abstract is checked, translated by gpt-6-astra, put back by gpt-6-astra, judged by gpt-6-astra. The fleet had nothing else free, so this is a model marking its own work.
- `content/vi/stoica-2001-chord/00_front.md` every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.
- `content/vi/sussman-1975-scheme/00_front.md` every abstract is checked, translated by gpt-6-astra, put back by gpt-6-astra, judged by gpt-6-astra. The fleet had nothing else free, so this is a model marking its own work.
- `content/vi/tarjan-1972-dfs/00_front.md` every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.
- `content/vi/tomasulo-1967-algorithm/00_front.md` every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.
- `content/vi/turing-1936-computable/00_front.md` every abstract is checked, translated by gpt-6-astra, put back by gpt-6-astra, judged by gpt-6-astra. The fleet had nothing else free, so this is a model marking its own work.
- `content/vi/verma-2015-borg/00_front.md` every abstract is checked, translated by gpt-5, put back by gpt-6-astra, judged by gpt-6-astra.

