---
paper: graefe-1994-volcano
title: Volcano - An Extensible and Parallel Query Evaluation System
authors:
  - Goetz Graefe
year: 1994
venue: IEEE Transactions on Knowledge and Data Engineering
field: databases
section: VI
section_title: MULTIPROCESSOR QUERY EVALUATION
tag: "0475"
kind: section
lang: en
source: http://daslab.seas.harvard.edu/reading-group/papers/volcano.pdf
pdf_sha256: 61e9ce81f84d66797c95db711fb593adcf1dbbf95fea53eba44a9b9e2239d6ca
pdf_pages: 10-14
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 52ca8aa8d78227ba7bb967b45d2f4aab399a3ec113175b0f316908abe0eea2f8
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

A large number of research and development projects have shown over the last decade that query processing in relational database systems can benefit significantly from parallel algorithms. The main reasons parallelism is relatively easy to exploit in relational query processing systems are 1) query processing is performed using a tree of operators that can be executed in separate processes and processors connected with pipelines (inter-operator parallelism) and 2) each operator consumes and produces sets that can be partitioned or fragmented into disjoint subsets to be processed in parallel (intra-operator parallelism).

Fortunately, the reasons parallelism is easy to exploit in relational systems does not require the relational data model per se, only that queries be processed as sets of data items in a tree of operators. These are exactly the assumptions made in the design of Volcano, and it was therefore logical to parallelize extensible query processing in Volcano.

When Volcano was ported to a multiprocessor machine, it was desirable to use all single-process query processing code existing at that point without any change. The result is very clean, self-scheduling parallel processing. We call this novel approach the operator model of parallelizing a query evaluation engine [20].2 In this model, all parallelism issues are localized in one operator that uses and provides the standard iterator interface to the operators above and below in a query tree.

The module responsible for parallel execution and synchronization is called the exchange iterator in Volcano. Notice that it is an iterator with open, next, and close procedures; therefore, it can be inserted at any one place or at multiple places in a complex query tree. Fig. 5 shows a complex query execution plan that includes data processing operators, i.e., file scans and joins, and exchange operators. The next two figures will show the processes created when this plan is executed.

This section describes how the exchange iterator implements vertical and horizontal parallelism followed by discussions of alternative modes of operation of Volcano’s exchange operator and modifications to the file system required for multiprocess query evaluation. The description goes into a fair amount of detail since the exchange operator adds significantly to the power of Volcano. In fact, it represents a new concept in parallel query execution that is likely to prove useful in parallelizing both existing commercial database products and extensible single-process systems. It is described here for shared-memory systems only; considerations for the distributed-memory version are outlined as future work in the last section of this paper.

A. Vertical Parallelism

The first function of exchange is to provide vertical parallelism or pipelining between processes. The open procedure creates a new process after creating a data structure in shared memory called a port for synchronization and data exchange. The child process is an exact duplicate of the parent process. The exchange operator then takes different paths in the parent and child processes.

The parent process serves as the consumer and the child process as the producer in Volcano. The exchange operator in the consumer process acts as a normal iterator, the only difference from other iterators is that it receives its input via inter-process communication rather than iterator (procedure) calls. After creating the child process, open_exchange in the consumer is done. Next_exchange

2Parts of this section have appeared in [20].

Print
|
Exchange
|
Join
|
Join
|
Exchange
|
Scan
|
Exchange
|
Scan
|
Exchange
|
Scan
|
Scan
|
Exchange
|
Scan
Fig. 5. Operator model of parallelization. {#graefe-1994-volcano-fig-5 .figure tag=0477}

waits for data to arrive via the port and returns them a record at a time. Close_exchange informs the producer that it can close, waits for an acknowledgment, and returns.

Fig. 6 shows the processes created for vertical parallelism or pipelining by the exchange operators in the query plan of the previous figure. The exchange operators have created the processes, and are executing on both sides of the process boundaries, hiding the existence of process boundaries from the “work” operators. The fact that the join operators are executing within the same process, i.e., the placement of the exchange operators in the query tree, was arbitrary. The exchange operator provides only the mechanisms for parallel query evaluation, and many other choices (policies) would have been possible. In fact, the mechanisms provided in the operator model tend to be more flexible and amenable to more different policies than in the alternative bracket model [20].

In the producer process, the exchange operator becomes the driver for the query tree below the exchange operator using open, next, and close on its input. The output of next is collected in packets, which are arrays of Next-Record structures. The packet size is an argument in the exchange iterator’s state record, and can be set between 1 and 32 000 records. When a packet is filled, it is inserted into a linked list originating in the port and a semaphore is used to inform the consumer about the new packet. Records in packets are fixed in the shared buffer and must be unfixed by a consuming operator.

When its input is exhausted, the exchange operator in the producer process marks the last packet with an end-of-stream tag, passes it to the consumer, and waits until the consumer allows closing all open files. This delay is necessary in Volcano because files on virtual devices must not be closed before all their records are unpinned in the buffer. In other words, it is a peculiarity due to other design decisions in Volcano rather than inherent in the exchange iterator on the operator model of parallelization.

The alert reader has noticed that the exchange module uses a different dataflow paradigm than all other operators. While all other modules are based on demand-driven dataflow (iterators, lazy evaluation), the producer-consumer relationship of exchange uses data-driven dataflow (eager evaluation). There are two reasons for this change in paradigms. First, we intend to use the exchange operator also for horizontal parallelism, to be described below, which is easier to implement with data-driven dataflow. Second, this scheme removes the need for request messages. Even though a scheme with request messages, e.g., using a semaphore, would probably perform acceptably on a shared-memory machine, it would create unnecessary control overhead and delays. Since very-high degrees of parallelism and very-high-performance query evaluation require a closely tied network, e.g., a hypercube, of shared-memory machines, we decided to use a paradigm for data exchange that has been proven to perform well in a “shared-nothing” database machine [11].

A run-time switch of exchange enables flow control or back pressure using an additional semaphore. If the producer is significantly faster than the consumer, the producer may pin a significant portion of the buffer, thus impeding overall system performance. If flow control is enabled, after a producer has inserted a new packet into the port, it must request the flow control semaphore. After a consumer has removed a packet from the port, it releases the flow control semaphore. The initial value of the flow control semaphore determines how many packets the producers may get ahead of the consumers.

Notice that flow control and demand-driven dataflow are not the same. One significant difference is that flow control allows some “slack” in the synchronization of producer and consumer and therefore truly overlapped execution, while demand-driven dataflow is a rather rigid structure of request and delivery in which the consumer waits while the producer works on its next output. The second significant difference is that data-driven dataflow is easier to combine efficiently with horizontal parallelism and partitioning.

B. Horizontal Parallelism

There are two forms of horizontal parallelism, which we call bushy parallelism and intra-operator parallelism. In bushy parallelism, different CPU’s execute different subtrees of a complex query tree. Bushy parallelism and vertical parallelism are forms of inter-operator parallelism. Intra-operator parallelism means that several CPU’s perform the same operator on different subsets of a stored dataset or an intermediate result.

Bushy parallelism can easily be implemented by inserting one or two exchange operators into a query tree. For example, in order to sort two inputs into a merge-join in parallel, the first or both inputs are separated from the merge-join by an exchange operation. The parent process turns to the second sort immediately after forking the child process that will produce the first input in sorted order. Thus, the two sort operations are working in parallel.

Intra-operator parallelism requires data partitioning. Partitioning of stored datasets is achieved by using multiple files, preferably on different devices. Partitioning of intermediate results is implemented by including multiple queues in a port. If there are multiple consumer processes, each uses its own input queue. The producers use a support function to decide into which of the queues (or actually, into which of the packets being filled by the producer) an output record must go. Using a support function allows implementing round-robin-, key-range-, or hash-partitioning.

Fig. 7 shows the processes created for horizontal parallelism or partitioning by the exchange operators in the query plan shown earlier. The join operators are executed by three processes while the file scan operators are executed by one or two processes each, typically scanning file partitions on different devices. To obtain this grouping of processes, the only difference to the query plan used for the previous figure is that the “degree of parallelism” arguments in the exchange state records have to be set to 2 or 3, respectively, and that partitioning support functions must be provided for the exchange operators that transfer file scan output to the joint processes. All file scan processes can transfer data to all join processes; however, data transfer between the join operators occurs only within each of the join processes. Unfortunately, this restriction renders this parallelization infeasible if the two joins are on different attributes and partitioning-based parallel join methods are used. For this case, a variant of exchange is supported in Volcano exchange operator called interchange, which is described in the next section.

If an operator or an operator subtree is executed in parallel by a group of processes, one of them is designated the master. When a query tree is opened, only one process is running, which is naturally the master. When a master forks a child process in a producer-consumer relationship, the child process becomes the master within its group. The first action of the master producer is to determine how many slaves are needed by calling an appropriate support function. If the producer operation is to run in parallel, the master producer forks the other producer processes.

After all producer processes are forked, they run without further synchronization among themselves, with two exceptions. First, when accessing a shared data structure, e.g., the port to the consumers or a buffer table, short-term locks must be acquired for the duration of one linked-list insertion. Second, when a producer group is also a consumer group, i.e., there are at least two exchange operators and three process groups involved in a vertical pipeline, the processes that are both consumers and producers synchronize twice. During the (very short) interval between synchronizations, the master of this group creates a port that serves all processes in its group.

When a close request is propagated down the tree and reaches the first exchange operator, the master consumer’s close_exchange procedure informs all producer processes that they are allowed to close down using the semaphore mentioned above in the discussion on vertical parallelism. If the producer processes are also consumers, the master of the process group informs its producers, etc. In this way, all operators are shut down in an orderly fashion, and the entire query evaluation is self-scheduling.

C. Variants of the Exchange Operator

There are a number of situations for which the exchange operator described so far required some modifications or extensions. In this section, we outline additional capabilities implemented in Volcano’s exchange operator. All of these variants have been implemented in the exchange operator and are controlled by arguments in the state record.

For some operations, it is desirable to replicate or broadcast a stream to all consumers. For example, one of the two partitioning methods for hash-division [16] requires that the divisor be replicated and used with each partition of the dividend. Another example are fragment-and-replicate parallel join algorithms in which one of the two input relations is not moved at all while the other relation is sent to all processors. To support these algorithms, the exchange operator can be directed to send all records to all consumers, after pinning them appropriately multiple times in the buffer pool. Notice that it is not necessary to copy the records since they reside in a shared buffer pool; it is sufficient to pin them such that each consumer can unpin them as if it were the only process using them.

During implementation and benchmarking of parallel sorting [18], [21], we added two more features to exchange. First, we wanted to implement a merge network in which some processors produce sorted streams merge concurrently by other processors. Volcano’s sort iterator can be used to generate a sorted stream. A merge iterator was easily derived from the sort module. It uses a single level merge, instead of the cascaded merge of runs used in sort. The input of a merge iterator is an exchange. Differently from other operators, the merge iterator requires to distinguish the input records by their producer. As an example, for a join operation it does not matter where the input records were created, and all inputs can be accumulated in a single input stream. For a merge operation, it is crucial to distinguish the input records by their producer in order to merge multiple sorted streams correctly.

We modified the exchange module such that it can keep the input records separated according to their producers. A third argument to next_exchange is used to communicate the required producer from the merge to the exchange iterator. Further modifications included increasing the number of input buffers used by exchange, the number of semaphores (including for flow control) used between producer and consumer part of exchange, and the logic for end-of-stream. All these modifications were implemented in such a way that they support multilevel merge trees, e.g., a parallel binary merge tree as used in [3]. The merging paths are selected automatically such that the load is distributed as evenly as possible in each level.

Second, we implemented a sort algorithm that sorts data randomly partitioned (or “striped” [29]) over multiple disks into a range-partitioned file with sorted partitions, i.e., a sorted file distributed over multiple disks. When using the same number of processors and disks, two processes per CPU were required, one to perform the file scan and partition the records and another one to sort them. Creating and running more processes than processors can inflict a significant cost since these processes compete for the CPU’s and therefore require operating system scheduling.

In order to make better use of the available processing power, we decided to reduce the number of processes by half, effectively moving to one process per CPU. This required modifications to the exchange operator. Until then, the exchange operator could “live” only at the top or the bottom of the operator tree in a process. Since the modification, the exchange operator can also be in the middle of a process' operator tree. When the exchange operator is opened, it does not fork any processes but establishes a communication port for data exchange. The next operation requests records from its input tree, possibly sending them off to other processes in the group, until a record for its own partition is found. This mode of operation was termed interchange, and was referred to earlier in the discussion of Fig. 7.

This mode of operation also makes flow control obsolete. A process runs a producer (and produces input for the other processes) only if it does not have input for the consumer. Therefore, if the producers are in danger of overrunning the consumers, none of the producer operators gets scheduled, and the consumers consume the available records.

D. File System Modifications

The file system required some modifications to serve several processes concurrently. In order to restrict the extent of such modifications, Volcano currently does not include protection of files and records other than each disk's volume table of contents. Furthermore, typically nonrepetitive actions like mounting a device must be invoked by the query root process before or after a query is evaluated by multiple processes.

The most intricate changes were required for the buffer module. In fact, making sure the buffer manager would not be a bottleneck in a shared-memory machine was an interesting subproject independent of database query processing [18]. Concurrency control in the buffer manager was designed to provide a testbed for future research with effective and efficient mechanisms, and not to destroy the separation of policies and mechanisms.

Using one exclusive lock is the simplest way to protect a buffer pool and its internal data structures. However, decreased concurrency would have removed most or all advantages of parallel query processing. Therefore, the buffer uses a two-level scheme. There is a lock for each buffer pool and one for each descriptor (page or cluster resident in the buffer). The buffer pool lock must be held while searching or updating the hash tables and bucket chains. It is never held while doing I/O; thus, it is never held for a long period of time. A descriptor or cluster lock must be held while doing I/O or while updating a descriptor in the buffer, e.g., to decrease its fix count.

If a process finds a requested cluster in the buffer, it uses an atomic test-and-lock operation to lock the descriptor. If this operation fails, the pool lock is released, the operation delayed and restarted. It is necessary to restart the buffer operation including the hash table lookup because the process that holds the lock might be replacing the requested cluster. Therefore, the requesting process must wait to determine the outcome of the prior operation. Using this restart-scheme for descriptor locks has the additional benefit of avoiding deadlocks. The four conditions for deadlock are mutual exclusion, hold-and-wait, no preemption, and circular wait; Volcano's restart scheme does not satisfy the second condition. On the other hand, starvation is theoretically possible but has become extremely unlikely after buffer modifications that basically eliminated buffer contention.

In summary, the exchange module encapsulates parallel query processing in Volcano. It provides a large set of mechanisms useful in parallel query evaluation. Only very few changes had to be made in the buffer manager and the other file system modules to accommodate parallel execution. The most important properties of the exchange module are that it implements three forms of parallel processing within a single module, that it makes parallel query processing entirely self-scheduling, supports a variety of policies, e.g., partitioning schemes or packet sizes, and that it did not require any changes in the existing query processing modules, thus leveraging significantly the time and effort spent on them and allowing easy parallel implementation of new algorithms. It entirely separates data selection, manipulation, derivation, etc. from all parallelism issues, and may therefore prove useful in parallelizing other systems, both relational commercial and extensible research systems.
