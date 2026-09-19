---
paper: castro-1999-pbft
title: Practical Byzantine Fault Tolerance
authors:
  - Miguel Castro
  - Barbara Liskov
year: 1999
venue: OSDI
field: security
section: "6"
section_title: Implementation
tag: 082B
kind: section
lang: en
source: https://www.scs.stanford.edu/nyu/03sp/sched/bfs.pdf
pdf_sha256: 9b8d5842c967894eaa2d6aa71d4354d26c4f76880f859a117d96042b4a37efc1
pdf_pages: 9-10
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 36a549a4a582fe2c8b20c4671d2b9161997b8d26aaa9d75d921c8f795be5183c
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

This section describes our implementation. First we discuss the replication library, which can be used as a basis for any replicated service. In Section 6.2 we describe how we implemented a replicated NFS on top of the replication library. Then we describe how we maintain checkpoints and compute checkpoint digests efficiently.

### 6.1 The Replication Library {#castro-1999-pbft-s6-1 .section tag=082C}

The client interface to the replication library consists of a single procedure, invoke, with one argument, an input buffer containing a request to invoke a state machine operation. The invoke procedure uses our protocol to execute the requested operation at the replicas and select the correct reply from among the replies of the individual replicas. It returns a pointer to a buffer containing the operation result.

On the server side, the replication code makes a number of upcalls to procedures that the server part of the application must implement. There are procedures to execute requests (execute), to maintain checkpoints of the service state (make_checkpoint, delete_checkpoint), to obtain the digest of a specified checkpoint (get_digest), and to obtain missing information (get_checkpoint, set_checkpoint). The execute procedure receives as input a buffer containing the requested operation, executes the operation, and places the result in an output buffer. The other procedures are discussed further in Sections 6.3 and 6.4.

Point-to-point communication between nodes is implemented using UDP, and multicast to the group of replicas is implemented using UDP over IP multicast [7]. There is a single IP multicast group for each service, which contains all the replicas. These communication protocols are unreliable; they may duplicate or lose messages or deliver them out of order.

The algorithm tolerates out-of-order delivery and rejects duplicates. View changes can be used to recover from lost messages, but this is expensive and therefore it is important to perform retransmissions. During normal operation recovery from lost messages is driven by the receiver: backups send negative acknowledgments to the primary when they are out of date and the primary retransmits pre-prepare messages after a long timeout. A reply to a negative acknowledgment may include both a portion of a stable checkpoint and missing messages. During view changes, replicas retransmit view-change messages until they receive a matching new-view message or they move on to a later view.

The replication library does not implement view changes or retransmissions at present. This does not compromise the accuracy of the results given in Section 7 because the rest of the algorithm is completely implemented (including the manipulation of the timers that trigger view changes) and because we have formalized the complete algorithm and proved its correctness [4].

### 6.2 BFS: A Byzantine-Fault-tolerant File System {#castro-1999-pbft-s6-2 .section tag=082D}

We implemented BFS, a Byzantine-fault-tolerant NFS service, using the replication library. Figure 2 shows the architecture of BFS. We opted not to modify the kernel NFS client and server because we did not have the sources for the Digital Unix kernel.

A file system exported by the fault-tolerant NFS service is mounted on the client machine like any regular NFS file system. Application processes run unmodified and interact with the mounted file system through the NFS client in the kernel. We rely on user level relay processes to mediate communication between the standard NFS client and the replicas. A relay receives NFS protocol requests, calls the invoke procedure of our replication library, and sends the result back to the NFS client.

Figure.

Figure 2: Replicated File System Architecture. {#castro-1999-pbft-fig-2 .figure tag=082E}

Each replica runs a user-level process with the replication library and our NFS V2 daemon, which we will refer to as snfsd (for simple nfsd). The replication library receives requests from the relay, interacts with snfsd by making upcalls, and packages NFS replies into replication protocol replies that it sends to the relay.

We implemented snfsd using a fixed-size memory-mapped file. All the file system data structures, e.g., inodes, blocks and their free lists, are in the mapped file. We rely on the operating system to manage the cache of memory-mapped file pages and to write modified pages to disk asynchronously. The current implementation uses 8KB blocks and inodes contain the NFS status information plus 256 bytes of data, which is used to store directory entries in directories, pointers to blocks in files, and text in symbolic links. Directories and files may also use indirect blocks in a way similar to Unix.

Our implementation ensures that all state machine replicas start in the same initial state and are deterministic, which are necessary conditions for the correctness of a service implemented using our protocol. The primary proposes the values for time-last-modified and time-last-accessed, and replicas select the larger of the proposed value and one greater than the maximum of all values selected for earlier requests. We do not require synchronous writes to implement NFS V2 protocol semantics because BFS achieves stability of modified data and meta-data through replication [20].

### 6.3 Maintaining Checkpoints {#castro-1999-pbft-s6-3 .section tag=082F}

This section describes how snfsd maintains checkpoints of the file system state. Recall that each replica maintains several logical copies of the state: the current state, some number of checkpoints that are not yet stable, and the last stable checkpoint.
snfsd executes file system operations directly in the memory mapped file to preserve locality, and it uses copy-on-write to reduce the space and time overhead associated with maintaining checkpoints. snfsd maintains a copy-on-write bit for every 512-byte block in the memory mapped file. When the replication code invokes the make_checkpoint upcall, snfsd sets all the copy-on-write bits and creates a (volatile) checkpoint record, containing the current sequence number, which it receives as an argument to the upcall, and a list of blocks. This list contains the copies of the blocks that were modified since the checkpoint was taken, and therefore, it is initially empty. The record also contains the digest of the current state; we discuss how the digest is computed in Section 6.4.
When a block of the memory mapped file is modified while executing a client request, snfsd checks the copy-on-write bit for the block and, if it is set, stores the block’s current contents and its identifier in the checkpoint record for the last checkpoint. Then, it overwrites the block with its new value and resets its copy-on-write bit. snfsd retains a checkpoint record until told to discard it via a delete_checkpoint upcall, which is made by the replication code when a later checkpoint becomes stable.
If the replication code requires a checkpoint to send to another replica, it calls the get_checkpoint upcall. To obtain the value for a block, snfsd first searches for the block in the checkpoint record of the stable checkpoint, and then searches the checkpoint records of any later checkpoints. If the block is not in any checkpoint record, it returns the value from the current state.
The use of the copy-on-write technique and the fact that we keep at most 2 checkpoints ensure that the space and time overheads of keeping several logical copies of the state are low. For example, in the Andrew benchmark experiments described in Section 7, the average checkpoint record size is only 182 blocks with a maximum of 500.

6.4 Computing Checkpoint Digests
snfsd computes a digest of a checkpoint state as part of a make_checkpoint upcall. Although checkpoints are only taken occasionally, it is important to compute the state digest incrementally because the state may be large. snfsd uses an incremental collision-resistant one-way hash function called AdHash [1]. This function divides the state into fixed-size blocks and uses some other hash function (e.g., MD5) to compute the digest of the string obtained by concatenating the block index with the block value for each block. The digest of the state is the sum of the digests of the blocks modulo some large integer. In our current implementation, we use the 512-byte blocks from the copy-on-write technique and compute their digest using MD5.
To compute the digest for the state incrementally, snfsd maintains a table with a hash value for each 512-byte block. This hash value is obtained by applying MD5 to the block index concatenated with the block value at the time of the last checkpoint. When make_checkpoint is called, snfsd obtains the digest $d$ for the previous checkpoint state (from the associated checkpoint record). It computes new hash values for each block whose copy-on-write bit is reset by applying MD5 to the block index concatenated with the current block value. Then, it adds the new hash value to $d$, subtracts the old hash value from $d$, and updates the table to contain the new hash value. This process is efficient provided the number of modified blocks is small; as mentioned above, on average 182 blocks are modified per checkpoint for the Andrew benchmark.
