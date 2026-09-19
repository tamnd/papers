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
section: "3"
section_title: Software Architecture of Gamma
tag: "0260"
kind: section
lang: en
source: http://db.cs.berkeley.edu/cs286/papers/gamma-tkde1990.pdf
pdf_sha256: 420d33f44b8e050f33517cdff1299a58838b4ad826d80a6617200332ea02be5e
pdf_pages: 7-15
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 42ad3e7550939755b2fe6523bb141eff3908846ee891704874032edd28a06f98
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

In this section, we present an overview of Gamma’s software architecture and describe the techniques that Gamma employs for executing queries in a dataflow fashion. We begin by describing the alternative storage structures provided by the Gamma software. Next, the overall system architecture is described from the top down. After describing the overall process structure, we illustrate the operation of the system by describing the interaction of the

$^2$ Intel was forced to use such a design because the I/O system was added after the system had been completed and the only way of doing I/O was by using a empty socket on the board which did not have DMA access to memory.

processes during the execution of several different queries. A detailed presentation of the techniques used to control the execution of complex queries is presented in Section 3.4. This is followed by an example which illustrates the execution of a multioperator query. Finally, we briefly describe WiSS, the storage system used to provide low level database services, and NOSE, the underlying operating system.

### 3.1. Gamma Storage Organizations {#dewitt-1990-gamma-s3-1 .section tag=0720}

Relations in Gamma are horizontally partitioned [RIES78] across all disk drives in the system. The key idea behind horizontally partitioning each relation is to enable the database software to exploit all the I/O bandwidth provided by the hardware. By declustering$^3$ the tuples of a relation, the task of parallelizing a selection/scan operator becomes trivial as all that is required is to start a copy of the operator on each processor.

The query language of Gamma provides the user with three alternative declustering strategies: round robin, hashed, and range partitioned. With the first strategy, tuples are distributed in a round-robin fashion among the disk drives. This is the default strategy and is used for all relations created as the result of a query. If the hashed partitioning strategy is selected, a randomizing function is applied to the key attribute of each tuple (as specified in the partition command for the relation) to select a storage unit. In the third strategy the user specifies a range of key values for each site. For example, with a 4 disk system, the command partition employee on emp_id (100, 300, 1000) would result in the distribution of tuples shown in Table 2. The partitioning information for each relation is stored in the database catalog. For range and hash-partitioned relations, the name of the partitioning attribute is also kept and, in the case of range-partitioned relations, the range of values of the partitioning attribute for each site (termed a range table).

| Distribution Condition | Processor # |
| --- | --- |
| emp_$id \leq 100$ | 1 |
| 100 &lt; emp_$id \leq 300$ | 2 |
| 300 &lt; emp_$id \leq 1000$ | 3 |
| emp_id &gt; 1000 | 4 |

An Example Range Table
Table 2

Once a relation has been partitioned, Gamma provides the normal collection of relational database system access methods including both clustered and non-clustered indices. When the user requests that an index be created on a relation, the system automatically creates an index on each fragment of the relation. Unlike VSAM [WAGN73] and the Tandem file system [ENSC85], Gamma does not require the clustered index for a relation to be constructed on

$^3$ Declustering is another term for horizontal partitioning that was coined by the Bubba project [LIVN87].

the partitioning attribute.

As a query is being optimized, the partitioning information for each source relation in the query is incorporated into the query plan produced by the query optimizer. In the case of hash and range-partitioned relations, this partitioning information is used by the query scheduler (discussed below) to restrict the number of processors involved in the execution of selection queries on the partitioning attribute. For example, if relation X is hash partitioned on attribute y, it is possible to direct selection operations with predicates of the form "X.y = Constant" to a single site; avoiding the participation of any other sites in the execution of the query. In the case of range-partitioned relations, the query scheduler can restrict the execution of the query to only those processors whose ranges overlap the range of the selection predicate (which may be either an equality or range predicate).

In retrospect, we made a serious mistake in choosing to decluster all relations across all nodes with disks. A much better approach, as proposed in [COPE88], is to use the "heat" of a relation to determine the degree to which the relation is declustered. Unfortunately, to add such a capability to the Gamma software at this point in time would require a fairly major effort - one we are not likely to undertake.

### 3.2. Gamma Process Structure {#dewitt-1990-gamma-s3-2 .section tag=0261}

The overall structure of the various processes that form the Gamma software is shown in Figure 2. The role of each process is described briefly below. The operation of the distributed deadlock detection and recovery mechanism are presented in Sections 5.1 and 5.2. At system initialization time, a UNIX daemon process for the Catalog Manager (CM) is initiated along with a set of Scheduler Processes, a set of Operator Processes, the Deadlock Detection Process, and the Recovery Process.

Catalog Manager
The function of the Catalog Manager is to act as a central repository of all conceptual and internal schema information for each database. The schema information is loaded into memory when a database is first opened. Since multiple users may have the same database open at once and since each user may reside on a machine other than the one on which the Catalog Manager is executing, the Catalog Manager is responsible for insuring consistency among the copies cached by each user.

Query Manager
One query manager process is associated with each active Gamma user. The query manager is responsible for caching schema information locally, providing an interface for ad-hoc queries using gdl (our variant of Quel [STON76]), query parsing, optimization, and compilation.

Scheduler Processes
While executing, each multisite query is controlled by a scheduler process. This process is responsible for activating the Operator Processes used to execute the nodes of a compiled query tree. Scheduler processes can be run on any processor, insuring that no processor becomes a bottleneck. In practice, however, scheduler processes consume almost no resources and it is possible to run a large number of them on a single processor. A centralized dispatching process is used to assign scheduler processes to queries. Those queries that the optimizer can detect to be single-site queries are sent directly to the appropriate node for execution, by-passing the scheduling process.

Gamma Process Structure
Figure 2

Operator Process
For each operator in a query tree, at least one Operator Process is employed at each processor participating in the execution of the operator. These operators are primed at system initialization time in order to avoid the overhead of starting processes at query execution time (additional processes can be forked as needed). The structure of an operator process and the mapping of relational operators to operator processes is discussed in more detail below. When a scheduler wishes to start a new operator on a node, it sends a request to a special communications port known as the "new task" port. When a request is received on this port, an idle operator process is assigned to the request and the communications port of this operator process is returned to the requesting scheduler process.

### 3.3. An Overview of Query Execution {#dewitt-1990-gamma-s3-3 .section tag=0263}

Ad-hoc and Embedded Query Interfaces

Two interfaces to Gamma are available: an ad-hoc query language and an embedded query language interface in which queries can be embedded in a C program. When a user invokes the ad-hoc query interface, a Query Manager (QM) process is started which immediately connects itself to the CM process through the UNIX Internet socket mechanism. When the compiled query interface is used, the preprocessor translates each embedded query into a compiled query plan which is invoked at run-time by the program. A mechanism for passing parameters from the C program to the compiled query plans at run time is also provided.

Query Execution

Gamma uses traditional relational techniques for query parsing, optimization [SELI79, JARK84], and code generation. The optimization process is somewhat simplified as Gamma only employs hash-based algorithms for joins and other complex operations. Queries are compiled into a left-deep tree of operators. At execution time, each operator is executed by one or more operator processes at each participating site.

In designing the optimizer for the VAX version of Gamma, the set of possible query plans considered by the optimizer was restricted to only left-deep trees because we felt that there was not enough memory to support right-deep or bushy plans. By using a combination of left-deep query trees and hash-based join algorithms, we were able to insure that no more than two join operations were ever active simultaneously and hence were able to maximize the amount of physical memory which could be allocated to each join operator. Since this memory limitation was really only an artifact of the VAX prototype, we have recently begun to examine the performance implications of right deep and bushy query plans [SCHN89b].

As discussed in Section 3.1, in the process of optimizing a query, the query optimizer recognizes that certain queries can be directed to only a subset of the nodes in the system. In the case of a single site query, the query is sent directly by the QM to the appropriate processor for execution. In the case of a multiple site query, the optimizer establishes a connection to an idle scheduler process through a centralized dispatcher process. The dispatcher process, by controlling the number of active schedulers, implements a simple load control mechanism. Once it has established a connection with a scheduler process, the QM sends the compiled query to the scheduler process and waits for the query to complete execution. The scheduler process, in turn, activates operator processes at each query processor selected to execute the operator. Finally, the QM reads the results of the query and returns them through the ad-hoc query interface to the user or through the embedded query interface to the program from which the query was initiated.

### 3.4. Operator and Process Structure {#dewitt-1990-gamma-s3-4 .section tag=0266}

The algorithms for all the relational operators are written as if they were to be run on a single processor. As shown in Figure 3, the input to an Operator Process is a stream of tuples and the output is a stream of tuples that is demultiplexed through a structure we term a split table. Once the process begins execution, it continuously reads tuples from its input stream, operates on each tuple, and uses a split table to route the resulting tuple to the process indicated in the split table.$^4$ When the process detects the end of its input stream, it first closes the output streams and then sends a control message to its scheduler process indicating that it has completed execution. Closing the output streams has the side effect of sending "end of stream" messages to each of the destination processes.

Figure.

Figure 3

The split table defines a mapping of values to a set of destination processes. Gamma uses three different types of split tables depending on the type of operation being performed [DEWI86]. As an example of one form of split table, consider the use of the split table shown in Figure 4 in conjunction with the execution of a join operation using 4 processors. Each process producing tuples for the join will apply a hash function to the join attribute of each output tuple to produce a value between 0 and 3. This value is then used as an index into the split table to obtain the address of the destination process that should receive the tuple.

\footnotetext{4 Tuples are actually sent as 8K byte batches, except for the last batch.}

| Value | Destination Process |
| --- | --- |
| 0 | (Processor #3, Port #5) |
| 1 | (Processor #2, Port #13) |
| 2 | (Processor #7, Port #6) |
| 3 | (Processor #9, Port #15) |

An Example Split Table
Figure 4

An Example

As an example of how queries are executed, consider the query shown in Figure 5. In Figure 6, the processes used to execute the query are shown along with the flow of data between the various processes for a Gamma configuration consisting of two processors with disks and two processors without disks. Since the two input relations A and B are partitioned across the disks attached to processors P1 and P2, selection and scan operators are initiated on both processors P1 and P2. The split tables for both the select and scan operators each contain two entries since two processors are being used for the join operation. The split tables for each selection and scan are identical - routing tuples whose join attribute values hash to 0 (dashed lines) to P3 and those which hash to 1 (solid lines) to P4. The join operator executes in two phases. During the first phase, termed the Building phase, tuples from the inner relation (A in this example) are inserted into a memory-resident hash table by hashing on the join attribute value. After the first phase has completed, the probing phase of the join is initiated in which tuples from the outer relation are used to probe the hash table for matching tuples.$^5$ Since the result relation is partitioned across two disks, the split table for each join operator contains two entries and tuples of C are distributed in a round-robin fashion among P1 and P2.

Figure.

Figure 5

$^5$ This is actually a description of the simple hash join algorithm. The operation of the hybrid hash join algorithm is contained in Section 4.

Figure 6

One of the main problems with the DIRECT prototype was that every data page processed required at least one control message to a centralized scheduler. In Gamma this bottleneck is completely avoided. In fact, the number of control messages required to execute a query is approximately equal to three times the number of operators in the query times the number of processors used to execute each operator. As an example, consider Figure 7 which depicts the flow of control messages$^6$ from a scheduler process to the processes on processors P1 and P3 in Figure 6 (an identical set of messages would flow from the scheduler to P2 and P4). The scheduler begins by initiating the building phase of the join and the selection operator on relation A. When both these operators have completed, the scheduler next initiates the store operator, the probing phase of the join, and the scan of relation B. When each of these operators has completed, a result message is returned to the user.

\footnotetext{
$^6$ The "Initiate" message is sent to a "new operator" port on each processor. A dispatching processes accepts incoming messages on this port and assigns the operator to a process. The process which is assigned, replies to the scheduler with an "ID" message which indicates the private port number of the operator process. Future communications to the operator by the scheduler use this private port number.
}

Figure 7

### 3.5. Operating and Storage System {#dewitt-1990-gamma-s3-5 .section tag=0268}

Gamma is built on top of an operating system designed specifically for supporting database management systems. NOSE provides multiple, lightweight processes with shared memory. A non-preemptive scheduling policy is used to help prevent convoys [BLAS79] from occurring. NOSE provides communications between NOSE processes using the reliable message passing hardware of the Intel iPSC/2 hypercube. File services in NOSE are based on the Wisconsin Storage System (WiSS) [CHOU85]. Critical sections of WiSS are protected using the semaphore mechanism provided by NOSE.

The file services provided by WiSS include structured sequential files, byte-stream files as in UNIX, B+ indices, long data items, a sort utility, and a scan mechanism. A sequential file is a sequence of records. Records may vary in length (up to one page in length), and may be inserted and deleted at arbitrary locations within a sequential file. Optionally, each file may have one or more associated indices which map key values to the record identifiers of the records in the file that contain a matching value. One indexed attribute may be designated as a clustering attribute for the file. The scan mechanism is similar to that provided by System R’s RSS [ASTR76] except that the predicates are compiled by the query optimizer into 386 machine language to maximize performance.
