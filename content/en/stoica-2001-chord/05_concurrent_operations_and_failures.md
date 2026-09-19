---
paper: stoica-2001-chord
title: 'Chord: A Scalable Peer-to-peer Lookup Service for Internet Applications'
authors:
  - Ion Stoica
  - Robert Morris
  - David Karger
  - M. Frans Kaashoek
  - Hari Balakrishnan
year: 2001
venue: SIGCOMM
field: networks
section: "5"
section_title: Concurrent Operations and Failures
tag: 06D9
kind: section
lang: en
source: https://pdos.csail.mit.edu/papers/chord:sigcomm01/chord_sigcomm.pdf
pdf_sha256: cca4ae7873ac128b7b9034b2c3fbf32f7d84541a88b5e70d0c7c1ce1d6381fe8
pdf_pages: 7-8
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 5cd339a43925efb1c2a8f5a117044e5537689434ba9bf160bb3655613094acfa
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

In practice Chord needs to deal with nodes joining the system concurrently and with nodes that fail or leave voluntarily. This section describes modifications to the basic Chord algorithms described in Section 4 to handle these situations.

### 5.1 Stabilization {#stoica-2001-chord-s5-1 .section tag=06DA}

The join algorithm in Section 4 aggressively maintains the finger tables of all nodes as the network evolves. Since this invariant is difficult to maintain in the face of concurrent joins in a large network, we separate our correctness and performance goals. A basic “stabilization” protocol is used to keep nodes’ successor pointers up to date, which is sufficient to guarantee correctness of lookups. Those successor pointers are then used to verify and correct finger table entries, which allows these lookups to be fast as well as correct.

If joining nodes have affected some region of the Chord ring, a lookup that occurs before stabilization has finished can exhibit one of three behaviors. The common case is that all the finger table entries involved in the lookup are reasonably current, and the lookup finds the correct successor in $O(\log N)$ steps. The second case is where successor pointers are correct, but fingers are inaccurate. This yields correct lookups, but they may be slower. In the final case, the nodes in the affected region have incorrect successor pointers, or keys may not yet have migrated to newly joined nodes, and the lookup may fail. The higher-layer software using Chord will notice that the desired data was not found, and has the option of retrying the lookup after a pause. This pause can be short, since stabilization fixes successor pointers quickly.

Our stabilization scheme guarantees to add nodes to a Chord ring in a way that preserves reachability of existing nodes, even in the face of concurrent joins and lost and reordered messages. Stabilization by itself won’t correct a Chord system that has split into multiple disjoint cycles, or a single cycle that loops multiple times around the identifier space. These pathological cases cannot be produced by any sequence of ordinary node joins. It is unclear whether they can be produced by network partitions and recoveries or intermittent failures. If produced, these cases could be detected and repaired by periodic sampling of the ring topology.

Figure 7 shows the pseudo-code for joins and stabilization; this code replaces Figure 6 to handle concurrent joins. When node $n$ first starts, it calls $n.join(n')$, where $n'$ is any known Chord node. The $join$ function asks $n'$ to find the immediate successor of $n$. By itself, $join$ does not make the rest of the network aware of $n$.

Every node runs stabilize periodically (this is how newly joined nodes are noticed by the network). When node $n$ runs stabilize, it asks $n$'s successor for the successor’s predecessor $p$, and decides whether $p$ should be $n$'s successor instead. This would be the case if node $p$ recently joined the system. stabilize also notifies node $n$'s successor of $n$'s existence, giving the successor the chance to change its predecessor to $n$. The successor does this only if it knows of no closer predecessor than $n$.

As a simple example, suppose node $n$ joins the system, and its ID lies between nodes $n_p$ and $n_s$. $n$ would acquire $n_s$ as its successor. Node $n_s$, when notified by $n$, would acquire $n$ as its predecessor. When $n_p$ next runs stabilize, it will ask $n_s$ for its predecessor (which is now $n$); $n_p$ would then acquire $n$ as its successor. Finally, $n_p$ will notify $n$, and $n$ will acquire $n_p$ as its predecessor. At this point, all predecessor and successor pointers are correct.

$$
n.join(n')
    predecessor = nil;
    successor = n'.find_successor(n);
$$

```text
// periodically verify n’s immediate successor,
// and tell the successor about n.
n.stabilize()
    x = successor.predecessor;
    if (x ∈ (n, successor))
        successor = x;
    successor.notify(n);
```

// $n'$ thinks it might be our predecessor.
$n$.notify($n'$)
    if ($predecessor$ is nil or $n' \in (predecessor, n)$)
        $predecessor = n';$

```text
// periodically refresh finger table entries.
n.fix_fingers()
    i = random index > 1 into finger [];
    finger[i].node = find_successor(finger[i].start);
```

Figure 7: Pseudocode for stabilization. {#stoica-2001-chord-fig-7 .figure tag=06DB}

As soon as the successor pointers are correct, calls to find_predecessor (and thus find_successor) will work. Newly joined nodes that have not yet been fingered may cause find_predecessor to initially undershoot, but the loop in the lookup algorithm will nevertheless follow successor (finger[1]) pointers through the newly joined nodes until the correct predecessor is reached. Eventually fix_fingers will adjust finger table entries, eliminating the need for these linear scans.

The following theorems (proved in the technical report [21]) show that all problems caused by concurrent joins are transient. The theorems assume that any two nodes trying to communicate will eventually succeed.

THEOREM 4. Once a node can successfully resolve a given query, it will always be able to do so in the future.

THEOREM 5. At some time after the last join all successor pointers will be correct.

The proofs of these theorems rely on an invariant and a termination argument. The invariant states that once node $n$ can reach node $r$ via successor pointers, it always can. To argue termination, we consider the case where two nodes both think they have the same successor $s$. In this case, each will attempt to notify $s$, and $s$ will eventually choose the closer of the two (or some other, closer node) as its predecessor. At this point the farther of the two will, by contacting $s$, learn of a better successor than $s$. It follows that every node progresses towards a better and better successor over time. This progress must eventually halt in a state where every node is considered the successor of exactly one other node; this defines a cycle (or set of them, but the invariant ensures that there will be at most one).

We have not discussed the adjustment of fingers when nodes join because it turns out that joins don’t substantially damage the performance of fingers. If a node has a finger into each interval, then these fingers can still be used even after joins. The distance halving argument is essentially unchanged, showing that $O(\log N)$ hops suffice to reach a node “close” to a query’s target. New joins influence the lookup only by getting in between the old predecessor and successor of a target query. These new nodes may need to be scanned linearly (if their fingers are not yet accurate). But unless a tremendous number of nodes joins the system, the number of nodes between two old nodes is likely to be very small, so the impact on lookup is negligible. Formally, we can state the following:

THEOREM 6. If we take a stable network with $N$ nodes, and another set of up to $N$ nodes joins the network with no finger pointers (but with correct successor pointers), then lookups will still take $O(\log N)$ time with high probability.

More generally, so long as the time it takes to adjust fingers is less than the time it takes the network to double in size, lookups should continue to take $O(\log N)$ hops.

### 5.2 Failures and Replication {#stoica-2001-chord-s5-2 .section tag=06DC}

When a node $n$ fails, nodes whose finger tables include $n$ must find $n$'s successor. In addition, the failure of $n$ must not be allowed to disrupt queries that are in progress as the system is re-stabilizing.

The key step in failure recovery is maintaining correct successor pointers, since in the worst case find_predecessor can make progress using only successors. To help achieve this, each Chord node maintains a “successor-list” of its $r$ nearest successors on the Chord ring. In ordinary operation, a modified version of the stabilize routine in Figure 7 maintains the successor-list. If node $n$ notices that its successor has failed, it replaces it with the first live entry in its successor list. At that point, $n$ can direct ordinary lookups for keys for which the failed node was the successor to the new successor. As time passes, stabilize will correct finger table entries and successor-list entries pointing to the failed node.

After a node failure, but before stabilization has completed, other nodes may attempt to send requests through the failed node as part of a find_successor lookup. Ideally the lookups would be able to proceed, after a timeout, by another path despite the failure. In many cases this is possible. All that is needed is a list of alternate nodes, easily found in the finger table entries preceding that of the failed node. If the failed node had a very low finger table index, nodes in the successor-list are also available as alternates.

The technical report proves the following two theorems that show that the successor-list allows lookups to succeed, and be efficient, even during stabilization [21]:

THEOREM 7. If we use a successor list of length $r = O(\log N)$ in a network that is initially stable, and then every node fails with probability 1/2, then with high probability find_successor returns the closest living successor to the query key.

THEOREM 8. If we use a successor list of length $r = O(\log N)$ in a network that is initially stable, and then every node fails with probability 1/2, then the expected time to execute find_successor in the failed network is $O(\log N)$.

The intuition behind these proofs is straightforward: a node’s $r$ successors all fail with probability $2^{-r} = 1/N$, so with high probability a node will be aware of, so able to forward messages to, its closest living successor.

The successor-list mechanism also helps higher layer software replicate data. A typical application using Chord might store replicas of the data associated with a key at the $k$ nodes succeeding the key. The fact that a Chord node keeps track of its $r$ successors means that it can inform the higher layer software when successors come and go, and thus when the software should propagate new replicas.

Figure.

Figure 9: The 1st and the 99th percentiles of the number of keys per node as a function of virtual nodes mapped to a real node. The network has $10^4$ real nodes and stores $10^6$ keys. {#stoica-2001-chord-fig-9 .figure tag=06DD}
