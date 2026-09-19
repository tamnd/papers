---
paper: karp-1972-reducibility
title: Reducibility Among Combinatorial Problems
authors:
  - Richard M. Karp
year: 1972
venue: Complexity of Computer Computations
field: theory
section: "2"
section_title: THE CLASS $P$
tag: 04FE
kind: appendix
lang: en
source: https://doi.org/10.1007/978-1-4684-2001-2_9
pdf_sha256: ae57cf641ae4f1924bdc4d7ef865edb2411c44e3040e8e546d01f1545e288e89
pdf_pages: 6-10
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 23dd8e9a832bfaa2ac5aa9d34e0bda58cc91c89570ca5cf0a9880aee92fc6e8e
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

There is a large class of important computational problems which involve the determination of properties of graphs, digraphs, integers, finite families of finite sets, boolean formulas and elements of other countable domains. It is a reasonable working hypothesis, championed originally by Jack Edmonds (1965) in connection with problems in graph theory and integer programming, and by now widely accepted, that such a problem can be regarded as tractable if and only if there is an algorithm for its solution whose running time is bounded by a polynomial in the size of the input. In this section we introduce and begin to investigate the class of problems solvable in polynomial time.

We begin by giving an extremely general definition of "deterministic algorithm", computing a function from a countable domain D into a countable range R.

For any finite alphabet A, let $A^*$ be the set of finite strings of elements of A; for $x \in A^*$, let $\lg(x)$ denote the length of x.

A **deterministic algorithm** $A$ is specified by:
a countable set D (the **domain**)
a countable set R (the **range**)
a finite alphabet $\Delta$ such that $\Delta^* \cap R = \phi$
an **encoding function** $E : D \to \Delta^*$
a **transition function** $\tau : \Delta^* \to \Delta^* \cup R$.

The **computation** of $A$ on input $x \in D$ is the unique sequence $y_1, y_2, \ldots$ such that $y_1 = E(x),\ y_{i+1} = \tau(y_i)$ for all i and, if the sequence is finite and ends with $y_k$, then $y_k \in R$. Any string occurring as an element of a computation is called an **instantaneous description**. If the computation of $A$ on input $x$ is finite and of length $t(x)$, then $t(x)$ is the **running time** of $A$ on input $x$. $A$ is **terminating** if all its computations are finite. A terminating algorithm $A$ computes the function $f_A : D \to R$ such that $f_A(x)$ is the last element of the computation of $A$ on $x$.

If $R = \{\text{ACCEPT}, \text{REJECT}\}$ then $A$ is called a **recognition algorithm**. A recognition algorithm in which $D = \Sigma^*$ is called a **string recognition algorithm**. If $A$ is a string recognition algorithm then the **language recognized by** $A$ is $\{ x \in \Sigma^* \mid f_A(x) = \text{ACCEPT} \}$. If $D = R = \Sigma^*$ then $A$ is called a **string mapping algorithm**. A terminating algorithm $A$ with domain $D = \Sigma^*$ **operates in polynomial time** if there is a polynomial $p(\cdot)$ such that, for every $x \in \Sigma^*$, $t(x) \leq p(\lg(x))$.

To discuss algorithms in any practical context we must specialize the concept of deterministic algorithm. Various well known classes of string recognition algorithms (Markov algorithms, one-tape Turing machines, multitape and multihead Turing machines, random access machines, etc.) are delineated by restricting the functions E and T to be of certain very simple types. These definitions are standard [Hopcroft & Ullman (1969)] and will not be repeated here. It is by now commonplace to observe that many such classes are equivalent in their capability to recognize languages; for each such class of algorithms, the class of languages recognized is the class of recursive languages. This invariance under changes in definition is part of the evidence that recursiveness is the correct technical formulation of the concept of decidability.

The class of languages recognizable by string recognition algorithms which operate in polynomial time is also invariant under a wide range of changes in the class of algorithms. For example, any language recognizable in time p(·) by a multihead or multitape Turing machine is recognizable in time p^2(·) by a one-tape Turing machine. Thus the class of languages recognizable in polynomial time by one-tape Turing machines is the same as the class recognizable by the ostensibly more powerful multihead or multitape Turing machines. Similar remarks apply to random access machines.

Definition 1. P is the class of languages recognizable by one-tape Turing machines which operate in polynomial time. {#karp-1972-reducibility-def-1 .statement tag=04FF}

Definition 2. Π is the class of functions from $\Sigma^*$ into $\Sigma^*$ defined by one-tape Turing machines which operate in polynomial time. {#karp-1972-reducibility-def-2 .statement tag=0500}

The reader will not go wrong by identifying P with the class of languages recognizable by digital computers (with unbounded backup storage) which operate in polynomial time and Π with the class of string mappings performed in polynomial time by such computers.

Remark. If f: $\Sigma^* \to \Sigma^*$ is in Π then there is a polynomial p(·) such that $\lg(f(x)) \leq p(\lg(x))$.

We next introduce a concept of reducibility which is of central importance in this paper.

Definition 3. Let L and M be languages. Then L $\propto$ M (L is reducible to M) if there is a function f $\in \Pi$ such that f(x) $\in M \Leftrightarrow x \in L$. {#karp-1972-reducibility-def-3 .statement tag=0501}

Lemma 1. If L $\propto$ M and M $\in P$ then L $\in P$. {#karp-1972-reducibility-lem-1 .statement tag=0502}

Proof. The following is a polynomial-time bounded algorithm to decide if x $\in L$: compute f(x); then test in polynomial time whether f(x) $\in M$.

We will be interested in the difficulty of recognizing subsets of countable domains other than $\Sigma^*$. Given such a domain D, there is usually a natural one-one encoding $e : D \to \Sigma^*$. For example we can represent a positive integer by the string of 0's and 1's comprising its binary representation, a 1-dimensional integer array as a list of integers, a matrix as a list of 1-dimensional arrays, etc.; and there are standard techniques for encoding lists into strings over a finite alphabet, and strings over an arbitrary finite alphabet as strings of 0's and 1's. Given such an encoding $e : D \to \Sigma^*$, we say that a set $T \subseteq D$ is **recognizable in polynomial time** if $e(T) \in P$. Also, given sets $T \subseteq D$ and $U \subseteq D'$, and encoding functions $e : D \to \Sigma^*$ and $e' : D' \to \Sigma^*$ we say $T \propto U$ if $e(T) \propto e'(U)$.

As a rule several natural encodings of a given domain are possible. For instance a graph can be represented by its adjacency matrix, by its incidence matrix, or by a list of unordered pairs of nodes, corresponding to the arcs. Given one of these representations, there remain a number of arbitrary decisions as to format and punctuation. Fortunately, it is almost always obvious that any two "reasonable" encodings $e_0$ and $e_1$ of a given problem are equivalent; i.e., $e_0(S) \in P \Leftrightarrow e_1(S) \in P$. One important exception concerns the representation of positive integers; we stipulate that a positive integer is encoded in a binary, rather than unary, representation. In view of the invariance of recognizability in polynomial time and reducibility under reasonable encodings, we discuss problems in terms of their original domains, without specifying an encoding into $\Sigma^*$.

We complete this section by listing a sampling of problems which are solvable in polynomial time. In the next section we examine a number of close relatives of these problems which are not known to be solvable in polynomial time. Appendix 1 establishes our notation.

Each problem is specified by giving (under the heading "INPUT") a generic element of its domain of definition and (under the heading "PROPERTY") the property which causes an input to be accepted.

SATISFIABILITY WITH AT MOST 2 LITERALS PER CLAUSE [Cook (1971)]
INPUT: Clauses $C_1, C_2, \ldots, C_p$, each containing at most 2 literals
PROPERTY: The conjunction of the given clauses is satisfiable;
i.e., there is a set $S \subseteq \{ x_1, x_2, \ldots, x_n, x'_1, x'_2, \ldots, x'_n \}$ such that
a) $S$ does not contain a complementary pair of literals and
b) $S \cap C_k \neq \emptyset, \ k = 1, 2, \ldots, p$.

MINIMUM SPANNING TREE [Kruskal (1956)]
INPUT: $G, w, W$
PROPERTY: There exists a spanning tree of weight $\leq W$.

SHORTEST PATH [Dijkstra (1959)]
INPUT: G, w, W, s, t
PROPERTY: There is a path between s and t of weight $\leq W$.

MINIMUM CUT [Edmonds & Karp (1972)]
INPUT: G, w, W, s, t
PROPERTY: There is an s,t cut of weight $\leq W$.

ARC COVER [Edmonds (1965)]
INPUT: G, k
PROPERTY: There is a set $Y \subseteq A$ such that $|Y| \leq k$ and every node is incident with an arc in Y.

ARC DELETION
INPUT: G, k
PROPERTY: There is a set of k arcs whose deletion breaks all cycles.

BIPARTITE MATCHING [Hall (1948)]
INPUT: S $\subseteq Z_p^p \times Z_p^p$
PROPERTY: There are p elements of S, no two of which are equal in either component.

SEQUENCING WITH DEADLINES
INPUT: $(T_1, \ldots, T_n) \in Z^n$, $(D_1, \ldots, D_n) \in Z^n$, k
PROPERTY: Starting at time 0, one can execute jobs 1,2,...,n, with execution times $T_i$ and deadlines $D_i$, in some order such that not more than k jobs miss their deadlines.

SOLVABILITY OF LINEAR EQUATIONS
INPUT: $(c_{ij}), (a_i)$
PROPERTY: There exists a vector $(y_j)$ such that, for each i,
$\sum_j c_{ij} y_j = a_i$.
