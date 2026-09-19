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
section: "4"
section_title: The Base Chord Protocol
tag: "0461"
kind: section
lang: en
source: https://pdos.csail.mit.edu/papers/chord:sigcomm01/chord_sigcomm.pdf
pdf_sha256: cca4ae7873ac128b7b9034b2c3fbf32f7d84541a88b5e70d0c7c1ce1d6381fe8
pdf_pages: 3-7
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 454d2eda7f32f247df8a7fec2e4415f192e70cf624aa1c322452749beffa732b
edited: true
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The Chord protocol specifies how to find the locations of keys, how new nodes join the system, and how to recover from the failure (or planned departure) of existing nodes. This section describes a simplified version of the protocol that does not handle concurrent joins or failures. Section 5 describes enhancements to the base protocol to handle concurrent joins and failures.

### 4.1 Overview {#stoica-2001-chord-s4-1 .section tag=0462}

At its heart, Chord provides fast distributed computation of a hash function mapping keys to nodes responsible for them. It uses consistent hashing [11, 13], which has several good properties. With high probability the hash function balances load (all nodes receive roughly the same number of keys). Also with high probability, when an $N^{th}$ node joins (or leaves) the network, only an $O(1/N)$ fraction of the keys are moved to a different location—this is clearly the minimum necessary to maintain a balanced load.

Figure 2: An identifier circle consisting of the three nodes 0, 1, and 3. In this example, key 1 is located at node 1, key 2 at node 3, and key 6 at node 0. {#stoica-2001-chord-fig-2 .figure tag=0463}

Chord improves the scalability of consistent hashing by avoiding the requirement that every node know about every other node. A Chord node needs only a small amount of “routing” information about other nodes. Because this information is distributed, a node resolves the hash function by communicating with a few other nodes. In an $N$-node network, each node maintains information only about $O(\log N)$ other nodes, and a lookup requires $O(\log N)$ messages.

Chord must update the routing information when a node joins or leaves the network; a join or leave requires $O(\log^2 N)$ messages.

### 4.2 Consistent Hashing {#stoica-2001-chord-s4-2 .section tag=0464}

The consistent hash function assigns each node and key an $m$-bit identifier using a base hash function such as SHA-1 [9]. A node’s identifier is chosen by hashing the node’s IP address, while a key identifier is produced by hashing the key. We will use the term “key” to refer to both the original key and its image under the hash function, as the meaning will be clear from context. Similarly, the term “node” will refer to both the node and its identifier under the hash function. The identifier length $m$ must be large enough to make the probability of two nodes or keys hashing to the same identifier negligible.

Consistent hashing assigns keys to nodes as follows. Identifiers are ordered in an identifier circle modulo $2^m$. Key $k$ is assigned to the first node whose identifier is equal to or follows (the identifier of) $k$ in the identifier space. This node is called the successor node of key $k$, denoted by $\operatorname{successor}(k)$. If identifiers are represented as a circle of numbers from 0 to $2^m - 1$, then $\operatorname{successor}(k)$ is the first node clockwise from $k$.

Figure 2 shows an identifier circle with $m = 3$. The circle has three nodes: 0, 1, and 3. The successor of identifier 1 is node 1, so key 1 would be located at node 1. Similarly, key 2 would be located at node 3, and key 6 at node 0.

Consistent hashing is designed to let nodes enter and leave the network with minimal disruption. To maintain the consistent hashing mapping when a node $n$ joins the network, certain keys previously assigned to $n$’s successor now become assigned to $n$. When node $n$ leaves the network, all of its assigned keys are reassigned to $n$’s successor. No other changes in assignment of keys to nodes need occur. In the example above, if a node were to join with identifier 7, it would capture the key with identifier 6 from the node with identifier 0.

The following results are proven in the papers that introduced consistent hashing [11, 13]:

THEOREM 1. For any set of $N$ nodes and $K$ keys, with high probability:

1. Each node is responsible for at most $(1 + \epsilon)K/N$ keys

2. When an $(N+1)^{st}$ node joins or leaves the network, responsibility for $O(K/N)$ keys changes hands (and only to or from the joining or leaving node).

When consistent hashing is implemented as described above, the theorem proves a bound of $\epsilon = O(\log N)$. The consistent hashing paper shows that $\epsilon$ can be reduced to an arbitrarily small constant by having each node run $O(\log N)$ “virtual nodes” each with its own identifier.

The phrase “with high probability” bears some discussion. A simple interpretation is that the nodes and keys are randomly chosen, which is plausible in a non-adversarial model of the world. The probability distribution is then over random choices of keys and nodes, and says that such a random choice is unlikely to produce an unbalanced distribution. One might worry, however, about an adversary who intentionally chooses keys to all hash to the same identifier, destroying the load balancing property. The consistent hashing paper uses “$k$-universal hash functions” to provide certain guarantees even in the case of nonrandom keys.

Rather than using a $k$-universal hash function, we chose to use the standard SHA-1 function as our base hash function. This makes our protocol deterministic, so that the claims of “high probability” no longer make sense. However, producing a set of keys that collide under SHA-1 can be seen, in some sense, as inverting, or “decrypting” the SHA-1 function. This is believed to be hard to do. Thus, instead of stating that our theorems hold with high probability, we can claim that they hold “based on standard hardness assumptions.”

For simplicity (primarily of presentation), we dispense with the use of virtual nodes. In this case, the load on a node may exceed the average by (at most) an $O(\log N)$ factor with high probability (or in our case, based on standard hardness assumptions). One reason to avoid virtual nodes is that the number needed is determined by the number of nodes in the system, which may be difficult to determine. Of course, one may choose to use an a priori upper bound on the number of nodes in the system; for example, we could postulate at most one Chord server per IPv4 address. In this case running 32 virtual nodes per physical node would provide good load balance.

### 4.3 Scalable Key Location {#stoica-2001-chord-s4-3 .section tag=06D3}

A very small amount of routing information suffices to implement consistent hashing in a distributed environment. Each node need only be aware of its successor node on the circle. Queries for a given identifier can be passed around the circle via these successor pointers until they first encounter a node that succeeds the identifier; this is the node the query maps to. A portion of the Chord protocol maintains these successor pointers, thus ensuring that all lookups are resolved correctly. However, this resolution scheme is inefficient: it may require traversing all $N$ nodes to find the appropriate mapping. To accelerate this process, Chord maintains additional routing information. This additional information is not essential for correctness, which is achieved as long as the successor information is maintained correctly.

As before, let $m$ be the number of bits in the key/node identifiers. Each node, $n$, maintains a routing table with (at most) $m$ entries, called the finger table. The $i^{th}$ entry in the table at node $n$ contains the identity of the first node, $s$, that succeeds $n$ by at least $2^{i-1}$ on the identifier circle, i.e., $s = successor(n + 2^{i-1})$, where $1 < i < m$ (and all arithmetic is modulo $2^m$). We call node $s$ the $i^{th}$ finger of node $n$, and denote it by $n.finger[i].node$ (see Table 1). A finger table entry includes both the Chord identifier and the IP address (and port number) of the relevant node. Note that the first finger of $n$ is its immediate successor on the circle; for convenience we often refer to it as the successor rather than the first finger.

In the example shown in Figure 3(b), the finger table of node 1

| Notation | Definition |
| --- | --- |
| finger[k].start | $(n + 2^{k-1}) \bmod 2^m,\ 1 \leq k \leq m$ |
| .interval | [finger[k].start, finger[k + 1].start) |
| .node | first node $\geq n.finger[k].start$ |
| successor | the next node on the identifier circle; finger[1].node |
| predecessor | the previous node on the identifier circle |

Table 1: Definition of variables for node $n$, using $m$-bit identifiers. {#stoica-2001-chord-tab-1 .table tag=06D4}

points to the successor nodes of identifiers $(1 + 2^0) \bmod 2^3 = 2$, $(1 + 2^1) \bmod 2^3 = 3$, and $(1 + 2^2) \bmod 2^3 = 5$, respectively. The successor of identifier 2 is node 3, as this is the first node that follows 2, the successor of identifier 3 is (trivially) node 3, and the successor of 5 is node 0.

This scheme has two important characteristics. First, each node stores information about only a small number of other nodes, and knows more about nodes closely following it on the identifier circle than about nodes farther away. Second, a node’s finger table generally does not contain enough information to determine the successor of an arbitrary key $k$. For example, node 3 in Figure 3 does not know the successor of 1, as 1’s successor (node 1) does not appear in node 3’s finger table.

What happens when a node $n$ does not know the successor of a key $k$? If $n$ can find a node whose ID is closer than its own to $k$, that node will know more about the identifier circle in the region of $k$ than $n$ does. Thus $n$ searches its finger table for the node $j$ whose ID most immediately precedes $k$, and asks $j$ for the node it knows whose ID is closest to $k$. By repeating this process, $n$ learns about nodes with IDs closer and closer to $k$.

The pseudocode that implements the search process is shown in Figure 4. The notation $n.foo()$ stands for the function foo() being invoked at and executed on node $n$. Remote calls and variable references are preceded by the remote node identifier, while local variable references and procedure calls omit the local node. Thus $n.foo()$ denotes a remote procedure call on node $n$, while $n.bar$, without parentheses, is an RPC to lookup a variable bar on node $n$.

find_successor works by finding the immediate predecessor node of the desired identifier; the successor of that node must be the successor of the identifier. We implement find_predecessor explicitly, because it is used later to implement the join operation (Section 4.4).

When node $n$ executes find_predecessor, it contacts a series of nodes moving forward around the Chord circle towards $id$. If node $n$ contacts a node $n'$ such that $id$ falls between $n'$ and the successor of $n'$, find_predecessor is done and returns $n'$. Otherwise node $n$ asks $n'$ for the node $n'$ knows about that most closely precedes $id$. Thus the algorithm always makes progress towards the predecessor of $id$.

As an example, consider the Chord ring in Figure 3(b). Suppose node 3 wants to find the successor of identifier 1. Since 1 belongs to the circular interval $[7,3)$, it belongs to 3.finger[3].interval; node 3 therefore checks the third entry in its finger table, which is 0. Because 0 precedes 1, node 3 will ask node 0 to find the successor of 1. In turn, node 0 will infer from its finger table that 1’s successor is the node 1 itself, and return node 1 to node 3.

The finger pointers at repeatedly doubling distances around the circle cause each iteration of the loop in find_predecessor to halve the distance to the target identifier. From this intuition follows a theorem:

Figure 3: (a) The finger intervals associated with node 1. (b) Finger tables and key locations for a net with nodes 0, 1, and 3, and keys 1, 2, and 6. {#stoica-2001-chord-fig-3 .figure tag=06D5}

THEOREM 2. With high probability (or under standard hardness assumptions), the number of nodes that must be contacted to find a successor in an $N$-node network is $O(\log N)$.

PROOF. Suppose that node $n$ wishes to resolve a query for the successor of $k$. Let $p$ be the node that immediately precedes $k$. We analyze the number of query steps to reach $p$.

Recall that if $n \neq p$, then $n$ forwards its query to the closest predecessor of $k$ in its finger table. Suppose that node $p$ is in the $i^{th}$ finger interval of node $n$. Then since this interval is not empty, node $n$ will finger some node $f$ in this interval. The distance (number of identifiers) between $n$ and $f$ is at least $2^{i-1}$. But $f$ and $p$ are both in $n$'s $i^{th}$ finger interval, which means the distance between them is at most $2^{i-1}$. This means $f$ is closer to $p$ than to $n$, or equivalently, that the distance from $f$ to $p$ is at most half the distance from $n$ to $p$.

If the distance between the node handling the query and the predecessor $p$ halves in each step, and is at most $2^m$ initially, then within $m$ steps the distance will be one, meaning we have arrived at $p$.

In fact, as discussed above, we assume that node and key identifiers are random. In this case, the number of forwardings necessary will be $O(\log N)$ with high probability. After $\log N$ forwardings, the distance between the current query node and the key $k$ will be reduced to at most $2^m / N$. The expected number of node identifiers landing in a range of this size is 1, and it is $O(\log N)$ with high probability. Thus, even if the remaining steps advance by only one node at a time, they will cross the entire remaining interval and reach key $k$ within another $O(\log N)$ steps. $\Box$

In the section reporting our experimental results (Section 6), we will observe (and justify) that the average lookup time is $\frac{1}{2} \log N$.

### 4.4 Node Joins {#stoica-2001-chord-s4-4 .section tag=06D6}

In a dynamic network, nodes can join (and leave) at any time. The main challenge in implementing these operations is preserving the ability to locate every key in the network. To achieve this goal, Chord needs to preserve two invariants:

1. Each node’s successor is correctly maintained.

2. For every key $k$, node $successor(k)$ is responsible for $k$.

In order for lookups to be fast, it is also desirable for the finger tables to be correct.

This section shows how to maintain these invariants when a single node joins. We defer the discussion of multiple nodes joining simultaneously to Section 5, which also discusses how to handle a node failure. Before describing the join operation, we summarize its performance (the proof of this theorem is in the companion technical report [21]):

THEOREM 3. With high probability, any node joining or leaving an $N$-node Chord network will use $O(\log^2 N)$ messages to re-establish the Chord routing invariants and finger tables.

To simplify the join and leave mechanisms, each node in Chord maintains a predecessor pointer. A node’s predecessor pointer contains the Chord identifier and IP address of the immediate predecessor of that node, and can be used to walk counterclockwise around the identifier circle.

To preserve the invariants stated above, Chord must perform three tasks when a node $n$ joins the network:

1. Initialize the predecessor and fingers of node $n$.

2. Update the fingers and predecessors of existing nodes to reflect the addition of $n$.

3. Notify the higher layer software so that it can transfer state (e.g. values) associated with keys that node $n$ is now responsible for.

We assume that the new node learns the identity of an existing Chord node $n'$ by some external mechanism. Node $n$ uses $n'$ to initialize its state and add itself to the existing Chord network, as follows.

Figure 5: (a) Finger tables and key locations after node 6 joins. (b) Finger tables and key locations after node 3 leaves. Changed entries are shown in black, and unchanged in gray. {#stoica-2001-chord-fig-5 .figure tag=06D7}

Initializing fingers and predecessor: Node $n$ learns its predecessor and fingers by asking $n'$ to look them up, using the init_finger_table pseudocode in Figure 6. Naively performing find_successor for each of the $m$ finger entries would give a runtime of $O(m \log N)$. To reduce this, $n$ checks whether the $i^{th}$ finger is also the correct $(i + 1)^{th}$ finger, for each $i$. This happens when finger$i$.interval does not contain any node, and thus finger$i$.node $\geq$ finger$i + 1$.start. It can be shown that the change reduces the expected (and high probability) number of finger entries that must be looked up to $O(\log N)$, which reduces the overall time to $O(\log^2 N)$.

As a practical optimization, a newly joined node $n$ can ask an immediate neighbor for a copy of its complete finger table and its predecessor. $n$ can use the contents of these tables as hints to help it find the correct values for its own tables, since $n$'s tables will be similar to its neighbors'. This can be shown to reduce the time to fill the finger table to $O(\log N)$.

Updating fingers of existing nodes: Node $n$ will need to be entered into the finger tables of some existing nodes. For example, in Figure 5(a), node 6 becomes the third finger of nodes 0 and 1, and the first and the second finger of node 3.

Figure 6 shows the pseudocode of the update_finger_table function that updates existing finger tables. Node $n$ will become the $i^{th}$ finger of node $p$ if and only if (1) $p$ precedes $n$ by at least $2^{i-1}$, and (2) the $i^{th}$ finger of node $p$ succeeds $n$. The first node, $p$, that can meet these two conditions is the immediate predecessor of $n - 2^{i-1}$. Thus, for a given $n$, the algorithm starts with the $i^{th}$ finger of node $n$, and then continues to walk in the counter-clock-wise direction on the identifier circle until it encounters a node whose $i^{th}$ finger precedes $n$.

We show in the technical report [21] that the number of nodes that need to be updated when a node joins the network is $O(\log N)$ with high probability. Finding and updating these nodes takes $O(\log^2 N)$ time. A more sophisticated scheme can reduce this time to $O(\log N)$; however, we do not present it as we expect implementations to use the algorithm of the following section.

Transferring keys: The last operation that has to be performed when a node $n$ joins the network is to move responsibility for all the keys for which node $n$ is now the successor. Exactly what this entails depends on the higher-layer software using Chord, but typically it would involve moving the data associated with each key to the new node. Node $n$ can become the successor only for keys that were previously the responsibility of the node immediately following $n$, so $n$ only needs to contact that one node to transfer responsibility for all relevant keys.

#define successor finger[1].node

```text
// node n joins the network;
// n' is an arbitrary node in the network
n.join(n')
    if (n')
        init_finger_table(n');
        update_others();
        // move keys in (predecessor, n] from successor
    else // n is the only node in the network
        for i = 1 to m
            finger[i].node = n;
        predecessor = n;

// initialize finger table of local node;
// n' is an arbitrary node already in the network
n.init_finger_table(n')
    finger[1].node = n'.find_successor(finger[1].start);
    predecessor = successor.predecessor;
    successor.predecessor = n;
    for i = 1 to m - 1
        if (finger[i + 1].start ∈ [n, finger[i].node))
            finger[i + 1].node = finger[i].node;
        else
            finger[i + 1].node =
                n'.find_successor(finger[i + 1].start);

// update all nodes whose finger
// tables should refer to n
n.update_others()
    for i = 1 to m
        // find last node p whose i^{th} finger might be n
        p = find_predecessor(n - 2^{i-1});
```

p.update_finger_table(n, i);

```text
// if s is i^{th} finger of n, update n's finger table with s
n.update_finger_table(s, i)
    if (s ∈ [n, finger[i].node])
        finger[i].node = s;
        p = predecessor; // get first node preceding n
```

p.update_finger_table(s, i);

Figure 6: Pseudocode for the node join operation. {#stoica-2001-chord-fig-6 .figure tag=06D8}
