---
paper: cook-1971-np
title: The Complexity of Theorem-Proving Procedures
authors:
  - Stephen A. Cook
year: 1971
venue: STOC
field: theory
section: "1"
section_title: Tautologies and Polynomial Reducibility
tag: "0346"
kind: section
lang: en
source: https://www.cs.toronto.edu/~sacook/homepage/1971.pdf
pdf_sha256: aacaca0dd6db8b409317a2de282734539c3186a72cff1cb4dd601c76a4ddfb75
pdf_pages: 1-4
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 98c024913226c1199a9236761f09076aa78e25f9618dfdc5d745f5bee5f1ceaf
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Let us fix a formalism for the propositional calculus in which formulas are written as strings on $\Sigma$. Since we will require infinitely many proposition symbols (atoms), each such symbol will consist of a member of $\Sigma$ followed by a number in binary notation to distinguish that symbol. Thus a formula of length n can only have about $n/\log n$ distinct function and predicate symbols. The logical connectives are $\&$ (and), $\vee$ (or), and $\neg$ (not).

The set of tautologies (denoted by {tautologies}) is a certain recursive set of strings on this alphabet, and we are interested in the problem of finding a good lower bound on its possible recognition times. We provide no such lower bound here, but theorem 1 will give evidence that {tautologies} is a difficult set to recognize, since many apparently difficult problems can be reduced to determining tautologyhood. By reduced we mean, roughly speaking, that if tautologyhood could be decided instantly (by an "oracle") then these problems could be decided in polynomial time. In order to make this notion precise, we introduce query machines, which are like Turing machines with oracles in [1].

A query machine is a multitape Turing machine with a distinguished tape called the query tape, and three distinguished states called the query state, yes state, and no state, respectively. If M is a query machine and T is a set of strings, then a T-computation of M is a computation of M in which initially M is in the initial state and has an input string w on its input tape, and each time M assumes the query state there is a string u on the query tape, and the next state M assumes is the yes state if $u \in T$ and the no state if $u \notin T$. We think of an "oracle", which knows T, placing M in the yes state or no state.

Definition

A set S of strings is P-reducible (P for polynomial) to a set T of strings iff there is some query machine M and a polynomial Q(n) such that for each input string w, the T-computation of M with input w halts within $Q(|w|)$ steps ($|w|$ is the length of w), and ends in an accepting state iff $w \in S$.

It is not hard to see that P-reducibility is a transitive relation. Thus the relation E on sets of strings, given by $(S,T)\in E$ iff each of $S$ and $T$ is P-reducible to the other, is an equivalence relation. The equivalence class containing a set $S$ will be denoted by $\deg(S)$ (the polynomial degree of difficulty of $S$).

Definition: We will denote $\deg(\{0\})$ by $\mathcal{L}_*$, where $0$ denotes the zero function.

Thus $\mathcal{L}_*$ is the class of sets recognizable in polynomial time. $\mathcal{L}_*$ was discussed in [2], p. 5, and is the string analog of Cabham's class $\mathcal{L}$ of functions [3].

We now define the following special sets of strings.

1) The subgraph problem is the problem given two finite undirected graphs, determine whether the first is isomorphic to a subgraph of the second. A graph $G$ can be represented by a string $\bar{G}$ on the alphabet $\{0,1,*\}$ by listing the successive rows of its adjacency matrix, separated by *'s. We let {subgraph pairs} denote the set of strings $\bar{G}_1**\bar{G}_2$ such that $G_1$ is isomorphic to a subgraph of $G_2$.

2) The graph isomorphism problem will be represented by the set, denoted by {isomorphic graphpairs}, of all strings $\bar{G}_1**\bar{G}_2$ such that $G_1$ is isomorphic to $G_2$.

3) The set {Primes} is the set of all binary notations for prime numbers.

4) The set {DNF tautologies} is the set of strings representing tautologies in disjunctive normal form.

5) The set $D_3$ consists of those tautologies in disjunctive normal form in which each disjunct has at most three conjuncts (each of which is an atom or negation of an atom).

Theorem 1: If a set $S$ of strings is accepted by some nondeterministic Turing machine within polynomial time, then $S$ is P-reducible to {DNF tautologies}. {#cook-1971-np-thm-1 .statement tag=0347}

Corollary: Each of the sets in definitions 1)-5) is P-reducible to {DNF tautologies}.

This is because each set, or its complement, is accepted in polynomial time by some nondeterministic Turing machine.

Proof of the theorem: Suppose a nondeterministic Turing machine $M$ accepts a set $S$ of strings within time $Q(n)$, where $Q(n)$ is a polynomial. Given an input $w$ for $M$, we will construct a proposition formula $A(w)$ in conjunctive normal form such that $A(w)$ is satisfiable iff $M$ accepts $w$. Thus $\neg\neg A(w)$ is easily put in disjunctive normal form (using De Morgan's laws), and $\neg A(w)$ is a tautology if and only if $w\not\in S$. Since the whole construction can be carried out in time bounded by a polynomial in $|w|$ (the length of $w$), the theorem will be proved.

We may as well assume the Turing machine $M$ has only one tape, which is infinite to the right but has a left-most square. Let us number the squares from left to right $1, 2, \ldots$. Let us fix an input $w$ to $M$ of length $n$, and suppose $w\in S$. Then there is a computation of $M$ with input $w$ that ends in an accepting state within $T = Q(n)$ steps. The formula $A(w)$ will be built from many different proposition symbols, whose intended meanings, listed below, refer to such a computation.

Suppose the tape alphabet for $M$ is $\{\sigma_1, \ldots, \sigma_\ell\}$, and the set of states is $\{q_1, \ldots, q_s\}$. Notice that since the computation has at most $T = Q(n)$ steps, no tape square beyond number $T$ is scanned.

Proposition symbols:

$$
p_{s,t}^i \quad \text{for } 1 \leq i \leq \ell, \ 1 \leq s, t \leq T.
$$

$p_{s,t}^i$ is true iff tape square number $s$ at step $t$ contains the symbol $\sigma_i$.

$$
Q_t^i \quad \text{for } 1 \leq i \leq r, \ 1 \leq t \leq T. \quad Q_t^i \text{ is true iff at step } t \text{ the machine is in state } q_i.
$$

$$
S_{s,t} \quad \text{for } 1 \leq s, t \leq T \text{ is true iff at time } t \text{ square number } s \text{ is scanned by the tape head.}
$$

The formula $A(w)$ is a conjunctive B\&C\&D\&E\&F\&G\&H\&I formed as follows. Notice $A(w)$ is in conjunctive normal form.

B will assert that at each step t, one and only one square is scanned. B is a conjunction $B_1 \land B_2 \land \ldots \land B_T$, where $B_t$ asserts that at time t one and only one square is scanned:

$$
B_t = (S_{1,t} \lor S_{2,t} \lor \ldots \lor S_{T,t}) \land 
[\land_{1 \leq i < j \leq T} (\neg S_{i,t} \lor \neg S_{j,t})]
$$

For $1 \leq s \leq T$ and $1 \leq t \leq T_j$, $C_{s,t}$ asserts that at square s and time t there is one and only one symbol. C is the conjunction of all the $C_{s,t}$.

D asserts that for each t there is one and only one state.

E asserts the initial conditions are satisfied:

$$
E = Q_1^o \land S_{1,1} \land P_{1,1}^{i_1} \land P_{2,1}^{i_2} \land \ldots \land P_{n,1}^{i_n} \land P_{n+1,1}^1 \land \ldots \land P_{T,1}^1
$$

where $w = \sigma_{i_1} \cdots \sigma_{i_n}$, $q_0$ is the initial state and $\sigma_1$ is the blank symbol.

F, G, and H assert that for each time t the values of the P's, Q's and S's are updated properly. For example, G is the conjunction over all t, i, j of $G_{i,j}^t$, where $G_{i,j}^t$ asserts that if at time t the machine is in state $q_i$ scanning symbol $\sigma_j$, then at time $t + 1$ the machine is in state $q_k$, where $q_k$ is the state given by the transition function for M.

$$
G_{i,j}^t = \land_{s=1}^T (\neg Q_s^i \lor \neg S_{s,t} \lor \neg P_{s,t}^j \lor Q_{t+1}^k)
$$

Finally, the formula I asserts that the machine reaches an accepting state at some time. The machine M should be modified so that it continues to compute in some trivial fashion after reaching an accepting state, so that $A(w)$ will be satisfied.

It is now straightforward to verify that $A(w)$ has all the properties asserted in the first paragraph of the proof.

Theorem 2: The following sets are P-reducible to each other in pairs (and hence each has the same polynomial degree of difficulty): {tautologies}, {DNF tautologies}, $D_3$, {subgraph pairs}. {#cook-1971-np-thm-2 .statement tag=0348}

Remark: We have not been able to add either {primes} or {isomorphic graph pairs} to the above list. To show {tautologies} is P-reducible to {primes} would seem to require some deep results in number theory, while showing {tautologies} is P-reducible to {isomorphic graph pairs} would probably upset a conjecture of Corneil's [4] from which he deduces that the graph isomorphism problem can be solved in polynomial time.

Incidently, it not hard to see from the Davis-Putnam procedure [5] that the set $D_2$, consisting of all DNF tautologies with at most two conjuncts per disjunct, is in $\mathcal{L}^*$. Hence $D_2$ cannot be added to the list in theorem 2 (unless all sets in the list are in $\mathcal{L}^*$).

Proof of theorem 2: By the corollary to theorem 1, each of the sets is P-reducible to {DNF tautologies}. Since obviously {DNF tautologies} is P-reducible to {tautologies}, it remains to show {DNF tautologies} is P-reducible to $D_3$ and $D_3$ is P-reducible to {subgraph pairs}.

To show {DNF tautologies} is P-reducible to $D_3$, let A be a proposition formula in disjunctive normal form. Say $A = B_1 \lor B_2 \lor \ldots \lor B_k$, where $B_1 = R_1 \land \ldots \land R_s$, and each $R_i$ is an atom or negation of an atom, and $s > 3$. Then A is a tautology if and only if $A'$ is a tautology where

$$
A' = P \land R_3 \land \ldots \land R_s \land \neg P \land R_1 \land R_2 \land \ldots \land R_k,
$$

where P is a new atom. Since we have reduced the number of conjuncts in $B_1$, this process may be repeated until eventually a formula is found with at most three conjuncts per disjunct. Clearly the entire process is bounded in time by a polynomial in the length of A.

It remains to show $D_3$ is P-reducible to {subgraph pairs}. Suppose A is a formula in disjunctive normal form with three conjuncts per disjunct. Thus $A = C_1 \lor \ldots \lor C_k$, where

C_i = R_{i1} \& R_{i2} \& R_{i3}, and each R_{ij} is an atom or a negation of an atom. Now let G_1 be the complete graph with vertices {v_1, v_2, ..., v_k}, and let G_2 be the graph with vertices {u_{ij}}, 1 \leq i \leq k, 1 \leq j \leq 3, such that u_{ij} is connected by an edge to u_{rs} if and only if i \neq r and the two literals (R_{ij}, R_{rs}) do not form an opposite pair (that is they are neither of the form (P, \neg P) nor of the form (\neg P, P)). Thus there is a falsifying truth assignment to the formula A iff there is a graph homomorphism $\phi : G_1 \to G_2$ such that for each i, $\phi(v_i) = u_{ij}$ for some j. (The homomorphism tells for each i which of R_{i1}, R_{i2}, R_{i3} should be falsified, and the selective lack of edges in G_2 guarantees that the resulting truth assignment is consistently specified).

In order to guarantee that a one-one homomorphism $\phi : G_1 \to G_2$ has the property that for each i, $\phi(v_i) = u_{ij}$ for some j, we modify G_1 and G_2 as follows. We select graphs H_1, H_2, ..., H_k which are sufficiently distinct from each other that if G'_1 is formed from G_1 by attaching H_i to v_i, 1 \leq i \leq k, and G'_2 is formed from G_2 by attaching H_i to each of u_{i1} and u_{i2} and u_{i3}, 1 \leq i \leq k, then every one-one homomorphism $\phi : G'_1 \to G'_2$ has the property just stated. It is not hard to see such a construction can be carried out in polynomial time. Then G'_1 can be embedded in G'_2 if and only if A \notin D_3. This completes the proof of theorem 2.
