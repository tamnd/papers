---
paper: corbett-2012-spanner
title: 'Spanner: Google''s Globally-Distributed Database'
authors:
  - James C. Corbett
  - Jeffrey Dean
  - Michael Epstein
  - Andrew Fikes
  - Christopher Frost
  - J. J. Furman
  - Sanjay Ghemawat
  - Andrey Gubarev
  - Christopher Heiser
  - Peter Hochschild
year: 2012
venue: OSDI
field: databases
section: "4"
section_title: Concurrency Control
tag: 00A8
kind: section
lang: en
source: http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.258.9924
pdf_sha256: 61875779e75f603d21aefba6d9bd9816d4dd0c18cf41089f43707249e24bbf88
pdf_pages: 6-9
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: e78c17f9e4181cb30ec241ea6d2c3a69b4586af420515ec57048d4a5c983f0c9
prompt_sha256: 329630a0b9175a55e4af1b8e281a3e67eeab250f8d643953b7dcde99743c7628
---

This section describes how TrueTime is used to guarantee the correctness properties around concurrency control, and how those properties are used to implement features such as externally consistent transactions, lock-free read-only transactions, and non-blocking reads in the past. These features enable, for example, the guarantee that a whole-database audit read at a timestamp $t$ will see exactly the effects of every transaction that has committed as of $t$.

Going forward, it will be important to distinguish writes as seen by Paxos (which we will refer to as *Paxos writes* unless the context is clear) from Spanner client writes. For example, two-phase commit generates a Paxos write for the prepare phase that has no corresponding Spanner client write.

### 4.1 Timestamp Management {#corbett-2012-spanner-s4-1 .section tag=00A9}

Table 2 lists the types of operations that Spanner supports. The Spanner implementation supports *read-write transactions*, *read-only transactions* (predeclared snapshot-isolation transactions), and *snapshot reads*. Standalone writes are implemented as read-write transactions; non-snapshot standalone reads are implemented as read-only transactions. Both are internally retried (clients need not write their own retry loops).

A read-only transaction is a kind of transaction that has the performance benefits of snapshot isolation [6]. A read-only transaction must be predeclared as not having any writes; it is not simply a read-write transaction without any writes. Reads in a read-only transaction execute at a system-chosen timestamp without locking, so that incoming writes are not blocked. The execution of the reads in a read-only transaction can proceed on any replica that is sufficiently up-to-date (Section 4.1.3).

A snapshot read is a read in the past that executes without locking. A client can either specify a timestamp for a snapshot read, or provide an upper bound on the desired timestamp’s staleness and let Spanner choose a timestamp. In either case, the execution of a snapshot read proceeds at any replica that is sufficiently up-to-date.

For both read-only transactions and snapshot reads, commit is inevitable once a timestamp has been chosen, unless the data at that timestamp has been garbage-collected. As a result, clients can avoid buffering results inside a retry loop. When a server fails, clients can internally continue the query on a different server by repeating the timestamp and the current read position.

### 4.1.1 Paxos Leader Leases {#corbett-2012-spanner-s4-1-1 .section tag=00AA}

Spanner’s Paxos implementation uses timed leases to make leadership long-lived (10 seconds by default). A potential leader sends requests for timed *lease votes*; upon receiving a quorum of lease votes the leader knows it has a lease. A replica extends its lease vote implicitly on a successful write, and the leader requests lease-vote extensions if they are near expiration. Define a leader’s *lease interval* as starting when it discovers it has a quorum of lease votes, and as ending when it no longer has a quorum of lease votes (because some have expired). Spanner depends on the following disjointness invariant: for each Paxos group, each Paxos leader’s lease interval is disjoint from every other leader’s. Appendix A describes how this invariant is enforced.

The Spanner implementation permits a Paxos leader to abdicate by releasing its slaves from their lease votes. To preserve the disjointness invariant, Spanner constrains when abdication is permissible. Define $s_{max}$ to be the maximum timestamp used by a leader. Subsequent sections will describe when $s_{max}$ is advanced. Before abdicating, a leader must wait until *TT.after($s_{max}$) is true*.

### 4.1.2 Assigning Timestamps to RW Transactions {#corbett-2012-spanner-s4-1-2 .section tag=00AB}

Transactional reads and writes use two-phase locking. As a result, they can be assigned timestamps at any time when all locks have been acquired, but before any locks have been released. For a given transaction, Spanner assigns it the timestamp that Paxos assigns to the Paxos write that represents the transaction commit.

Spanner depends on the following monotonicity invariant: within each Paxos group, Spanner assigns timestamps to Paxos writes in monotonically increasing order, even across leaders. A single leader replica can trivially assign timestamps in monotonically increasing order. This invariant is enforced across leaders by making use of the disjointness invariant: a leader must only assign timestamps within the interval of its leader lease. Note that whenever a timestamp $s$ is assigned, $s_{max}$ is advanced to $s$ to preserve disjointness.

Spanner also enforces the following external-consistency invariant: if the start of a transaction $T_2$ occurs after the commit of a transaction $T_1$, then the commit timestamp of $T_2$ must be greater than the commit timestamp of $T_1$. Define the start and commit events for a transaction $T_i$ by $e_i^{start}$ and $e_i^{commit}$; and the commit timestamp of a transaction $T_i$ by $s_i$. The invariant becomes $t_{abs}(e_1^{commit}) < t_{abs}(e_2^{start}) \Rightarrow s_1 < s_2$.
The protocol for executing transactions and assigning timestamps obeys two rules, which together guarantee this invariant, as shown below. Define the arrival event of the commit request at the coordinator leader for a write $T_i$ to be $e_i^{server}$.

Start The coordinator leader for a write $T_i$ assigns a commit timestamp $s_i$ no less than the value of $TT.now().latest$, computed after $e_i^{server}$. Note that the participant leaders do not matter here; Section 4.2.1 describes how they are involved in the implementation of the next rule.

Commit Wait The coordinator leader ensures that clients cannot see any data committed by $T_i$ until $TT.after(s_i)$ is true. Commit wait ensures that $s_i$ is less than the absolute commit time of $T_i$, or $s_i < t_{abs}(e_i^{commit})$. The implementation of commit wait is described in Section 4.2.1. Proof:

$$
\begin{align*}
s_1 &< t_{abs}(e_1^{commit}) & \text{(commit wait)} \\
t_{abs}(e_1^{commit}) &< t_{abs}(e_2^{start}) & \text{(assumption)} \\
t_{abs}(e_2^{start}) &\leq t_{abs}(e_2^{server}) & \text{(causality)} \\
t_{abs}(e_2^{server}) &\leq s_2 & \text{(start)} \\
s_1 &< s_2 & \text{(transitivity)}
\end{align*}
$$

### 4.1.3 Serving Reads at a Timestamp {#corbett-2012-spanner-s4-1-3 .section tag=00AC}

The monotonicity invariant described in Section 4.1.2 allows Spanner to correctly determine whether a replica’s state is sufficiently up-to-date to satisfy a read. Every replica tracks a value called *safe time* $t_{safe}$ which is the maximum timestamp at which a replica is up-to-date. A replica can satisfy a read at a timestamp $t$ if $t <= t_{safe}$.

Define $t_{safe} = min(t_{safe}^{Paxos}, t_{safe}^{TM})$, where each Paxos state machine has a safe time $t_{safe}^{Paxos}$ and each transaction manager has a safe time $t_{safe}^{TM}$. $t_{safe}^{Paxos}$ is simpler: it is the timestamp of the highest-applied Paxos write. Because timestamps increase monotonically and writes are applied in order, writes will no longer occur at or below $t_{safe}^{Paxos}$ with respect to Paxos.

$t_{safe}^{TM}$ is $\infty$ at a replica if there are zero prepared (but not committed) transactions—that is, transactions in between the two phases of two-phase commit. (For a participant slave, $t_{safe}^{TM}$ actually refers to the replica’s leader’s transaction manager, whose state the slave can infer through metadata passed on Paxos writes.) If there are any such transactions, then the state affected by those transactions is indeterminate: a participant replica does not know yet whether such transactions will commit. As we discuss in Section 4.2.1, the commit protocol ensures that every participant knows a lower bound on a prepared transaction’s timestamp. Every participant leader (for a group $g$) for a transaction $T_i$ assigns a prepare timestamp $s_{i,g}^{prepare}$ to its prepare record. The coordinator leader ensures that the transaction’s commit timestamp $s_i >= s_{i,g}^{prepare}$ over all participant groups $g$. Therefore, for every replica in a group $g$, over all transactions $T_i$ prepared at $g$, $t_{safe}^{TM} = min_i(s_{i,g}^{prepare}) - 1$ over all transactions prepared at $g$.

### 4.1.4 Assigning Timestamps to RO Transactions {#corbett-2012-spanner-s4-1-4 .section tag=00AD}

A read-only transaction executes in two phases: assign a timestamp $s_{read}$ [8], and then execute the transaction’s reads as snapshot reads at $s_{read}$. The snapshot reads can execute at any replicas that are sufficiently up-to-date.

The simple assignment of $s_{read} = TT.now().latest$, at any time after a transaction starts, preserves external consistency by an argument analogous to that presented for writes in Section 4.1.2. However, such a timestamp may require the execution of the data reads at $s_{read}$ to block if $t_{safe}$ has not advanced sufficiently. (In addition, note that choosing a value of $s_{read}$ may also advance $s_{max}$ to preserve disjointness.) To reduce the chances of blocking, Spanner should assign the oldest timestamp that preserves external consistency. Section 4.2.2 explains how such a timestamp can be chosen.

### 4.2 Details {#corbett-2012-spanner-s4-2 .section tag=00AE}

This section explains some of the practical details of read-write transactions and read-only transactions elided earlier, as well as the implementation of a special transaction type used to implement atomic schema changes.

It then describes some refinements of the basic schemes as described.

### 4.2.1 Read-Write Transactions {#corbett-2012-spanner-s4-2-1 .section tag=00AF}

Like Bigtable, writes that occur in a transaction are buffered at the client until commit. As a result, reads in a transaction do not see the effects of the transaction’s writes. This design works well in Spanner because a read returns the timestamps of any data read, and uncommitted writes have not yet been assigned timestamps.

Reads within read-write transactions use wound-wait [33] to avoid deadlocks. The client issues reads to the leader replica of the appropriate group, which acquires read locks and then reads the most recent data. While a client transaction remains open, it sends keepalive messages to prevent participant leaders from timing out its transaction. When a client has completed all reads and buffered all writes, it begins two-phase commit. The client chooses a coordinator group and sends a commit message to each participant’s leader with the identity of the coordinator and any buffered writes. Having the client drive two-phase commit avoids sending data twice across wide-area links.

A non-coordinator-participant leader first acquires write locks. It then chooses a prepare timestamp that must be larger than any timestamps it has assigned to previous transactions (to preserve monotonicity), and logs a prepare record through Paxos. Each participant then notifies the coordinator of its prepare timestamp.

The coordinator leader also first acquires write locks, but skips the prepare phase. It chooses a timestamp for the entire transaction after hearing from all other participant leaders. The commit timestamp s must be greater or equal to all prepare timestamps (to satisfy the constraints discussed in Section 4.1.3), greater than TT.now().latest at the time the coordinator received its commit message, and greater than any timestamps the leader has assigned to previous transactions (again, to preserve monotonicity). The coordinator leader then logs a commit record through Paxos (or an abort if it timed out while waiting on the other participants).

Before allowing any coordinator replica to apply the commit record, the coordinator leader waits until TT.after(s), so as to obey the commit-wait rule described in Section 4.1.2. Because the coordinator leader chose s based on TT.now().latest, and now waits until that timestamp is guaranteed to be in the past, the expected wait is at least $2 * \overline{\epsilon}$. This wait is typically overlapped with Paxos communication. After commit wait, the coordinator sends the commit timestamp to the client and all other participant leaders. Each participant leader logs the transaction’s outcome through Paxos. All participants apply at the same timestamp and then release locks.

### 4.2.2 Read-Only Transactions {#corbett-2012-spanner-s4-2-2 .section tag=00B0}

Assigning a timestamp requires a negotiation phase between all of the Paxos groups that are involved in the reads. As a result, Spanner requires a scope expression for every read-only transaction, which is an expression that summarizes the keys that will be read by the entire transaction. Spanner automatically infers the scope for standalone queries.

If the scope’s values are served by a single Paxos group, then the client issues the read-only transaction to that group’s leader. (The current Spanner implementation only chooses a timestamp for a read-only transaction at a Paxos leader.) That leader assigns $s_{read}$ and executes the read. For a single-site read, Spanner generally does better than TT.now().latest. Define LastTS() to be the timestamp of the last committed write at a Paxos group. If there are no prepared transactions, the assignment $s_{read} = LastTS()$ trivially satisfies external consistency: the transaction will see the result of the last write, and therefore be ordered after it.

If the scope’s values are served by multiple Paxos groups, there are several options. The most complicated option is to do a round of communication with all of the groups’s leaders to negotiate $s_{read}$ based on LastTS(). Spanner currently implements a simpler choice. The client avoids a negotiation round, and just has its reads execute at $s_{read} = TT.now().latest$ (which may wait for safe time to advance). All reads in the transaction can be sent to replicas that are sufficiently up-to-date.

### 4.2.3 Schema-Change Transactions {#corbett-2012-spanner-s4-2-3 .section tag=00B1}

TrueTime enables Spanner to support atomic schema changes. It would be infeasible to use a standard transaction, because the number of participants (the number of groups in a database) could be in the millions. Bigtable supports atomic schema changes in one datacenter, but its schema changes block all operations.

A Spanner schema-change transaction is a generally non-blocking variant of a standard transaction. First, it is explicitly assigned a timestamp in the future, which is registered in the prepare phase. As a result, schema changes across thousands of servers can complete with minimal disruption to other concurrent activity. Second, reads and writes, which implicitly depend on the schema, synchronize with any registered schema-change timestamp at time t: they may proceed if their timestamps precede t, but they must block behind the schema-change transaction if their timestamps are after t. Without TrueTime, defining the schema change to happen at t would be meaningless.

| replicas | latency (ms) |  |  | throughput (Kops/sec) |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | write | read-only transaction | snapshot read | write | read-only transaction | snapshot read |
| 1D | 9.4±.6 | — | — | 4.0±.3 | — | — |
| 1 | 14.4±1.0 | 1.4±.1 | 1.3±.1 | 4.1±.05 | 10.9±.4 | 13.5±.1 |
| 3 | 13.9±.6 | 1.3±.1 | 1.2±.1 | 2.2±.5 | 13.8±3.2 | 38.5±.3 |
| 5 | 14.4±.4 | 1.4±.05 | 1.3±.04 | 2.8±.3 | 25.3±5.2 | 50.0±1.1 |

Table 3: Operation microbenchmarks. Mean and standard deviation over 10 runs. 1D means one replica with commit wait disabled. {#corbett-2012-spanner-tab-3 .table tag=00B2}

### 4.2.4 Refinements {#corbett-2012-spanner-s4-2-4 .section tag=00B3}

$t_{safe}^{TM}$ as defined above has a weakness, in that a single prepared transaction prevents $t_{safe}$ from advancing. As a result, no reads can occur at later timestamps, even if the reads do not conflict with the transaction. Such false conflicts can be removed by augmenting $t_{safe}^{TM}$ with a fine-grained mapping from key ranges to prepared-transaction timestamps. This information can be stored in the lock table, which already maps key ranges to lock metadata. When a read arrives, it only needs to be checked against the fine-grained safe time for key ranges with which the read conflicts.

$LastTS()$ as defined above has a similar weakness: if a transaction has just committed, a non-conflicting read-only transaction must still be assigned $s_{read}$ so as to follow that transaction. As a result, the execution of the read could be delayed. This weakness can be remedied similarly by augmenting $LastTS()$ with a fine-grained mapping from key ranges to commit timestamps in the lock table. (We have not yet implemented this optimization.) When a read-only transaction arrives, its timestamp can be assigned by taking the maximum value of $LastTS()$ for the key ranges with which the transaction conflicts, unless there is a conflicting prepared transaction (which can be determined from fine-grained safe time).

$t_{safe}^{Paxos}$ as defined above has a weakness in that it cannot advance in the absence of Paxos writes. That is, a snapshot read at $t$ cannot execute at Paxos groups whose last write happened before $t$. Spanner addresses this problem by taking advantage of the disjointness of leader-lease intervals. Each Paxos leader advances $t_{safe}^{Paxos}$ by keeping a threshold above which future writes’ timestamps will occur: it maintains a mapping $MinNextTS(n)$ from Paxos sequence number $n$ to the minimum timestamp that may be assigned to Paxos sequence number $n + 1$. A replica can advance $t_{safe}^{Paxos}$ to $MinNextTS(n) - 1$ when it has applied through $n$.

A single leader can enforce its $MinNextTS()$ promises easily. Because the timestamps promised by $MinNextTS()$ lie within a leader’s lease, the disjointness invariant enforces $MinNextTS()$ promises across leaders. If a leader wishes to advance $MinNextTS()$ beyond the end of its leader lease, it must first extend its lease. Note that $s_{max}$ is always advanced to the highest value in $MinNextTS()$ to preserve disjointness.

A leader by default advances $MinNextTS()$ values every 8 seconds. Thus, in the absence of prepared transactions, healthy slaves in an idle Paxos group can serve reads at timestamps greater than 8 seconds old in the worst case. A leader may also advance $MinNextTS()$ values on demand from slaves.
