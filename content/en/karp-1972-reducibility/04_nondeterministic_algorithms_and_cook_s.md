---
paper: karp-1972-reducibility
title: Reducibility Among Combinatorial Problems
authors:
  - Richard M. Karp
year: 1972
venue: Complexity of Computer Computations
field: theory
section: "3"
section_title: NONDETERMINISTIC ALGORITHMS AND COOK'S THEOREM
tag: "0503"
kind: appendix
lang: en
source: https://doi.org/10.1007/978-1-4684-2001-2_9
pdf_sha256: ae57cf641ae4f1924bdc4d7ef865edb2411c44e3040e8e546d01f1545e288e89
pdf_pages: 10-13
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: f765d1846c36f8d5da0efd2a05243049d4ea96ccd1a97cb93c8363f7e896bc63
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

In this section we state an important theorem due to Cook (1971) which asserts that any language in a certain wide class $NP$ is reducible to a specific set S, which corresponds to the problem of deciding whether a boolean formula in conjunctive normal form is satisfiable.

Let $p^{(2)}$ denote the class of subsets of $\Sigma^* \times \Sigma^*$ which are recognizable in polynomial time. Given $L^{(2)} \in p^{(2)}$ and a polynomial p, we define a language L as follows:

$L = \{ x | \text{there exists } y \text{ such that } <x,y> \in L^{(2)} \text{ and } lg(y) \leq p(lg(x)) \}$.

We refer to L as the language derived from $L^{(2)}$ by p-bounded existential quantification.

Definition 4. NP is the set of languages derived from elements of $P^{(2)}$ by polynomial-bounded existential quantification. {#karp-1972-reducibility-def-4 .statement tag=0504}

There is an alternative characterization of NP in terms of nondeterministic Turing machines. A nondeterministic recognition algorithm A is specified by:

a countable set D (the domain)
a finite alphabet $\Delta$ such that $\Delta^* \cap \{\text{ACCEPT}, \text{REJECT}\} = \phi$
an encoding function E: $D \to \Delta^*$
a transition relation $\tau \subseteq \Delta^* \times (\Delta^* \cup \{\text{ACCEPT}, \text{REJECT}\})$ such that, for every $y_0 \in \Delta^*$, the set $\{<y_0, y> | <y_0, y> \in \tau\}$ has fewer than $k_A$ elements, where $k_A$ is a constant. A computation of A on input $x \in D$ is a sequence $y_1, y_2, \ldots$ such that $y_1 = E(x)$, $<y_i, y_{i+1}> \in \tau$ for all i, and, if the sequence is finite and ends with $y_k$, then $y_k \in \{\text{ACCEPT}, \text{REJECT}\}$. A string $y \in \Delta^*$ which occurs in some computation is an instantaneous description. A finite computation ending in ACCEPT is an accepting computation. Input x is accepted if there is an accepting computation for x. If $D = \Sigma^*$ then A is a nondeterministic string recognition algorithm and we say that A operates in polynomial time if there is a polynomial $p(\cdot)$ such that, whenever A accepts x, there is an accepting computation for x of length $\leq p(\lg(x))$.

A nondeterministic algorithm can be regarded as a process which, when confronted with a choice between (say) two alternatives, can create two copies of itself, and follow up the consequences of both courses of action. Repeated splitting may lead to an exponentially growing number of copies; the input is accepted if any sequence of choices leads to acceptance.

The nondeterministic 1-tape Turing machines, multitape Turing machines, random-access machines, etc. define classes of nondeterministic string recognition algorithms by restricting the encoding function E and transition relation $\tau$ to particularly simple forms. All these classes of algorithms, restricted to operate in polynomial time, define the same class of languages. Moreover, this class is NP.

Theorem 1. $L \in NP$ if and only if L is accepted by a nondeterministic Turing machine which operates in polynomial time. {#karp-1972-reducibility-thm-1 .statement tag=0505}

Proof. $\Rightarrow$ Suppose $L \in NP$. Then, for some $L^{(2)} \in P^{(2)}$ and some polynomial p, L is obtained from $L^{(2)}$ by p-bounded existential quantification. We can construct a nondeterministic machine which first guesses the successive digits of a string y of length $\leq p(\lg(y))$ and then tests whether $<x,y> \in L^{(2)}$. Such a machine clearly recognizes L in polynomial time.

$\Leftarrow$ Suppose L is accepted by a nondeterministic Turing machine T which operates in time p. Assume without loss of generality that, for any instantaneous description Z, there are at most two instantaneous descriptions that may follow Z (i.e., at most two primitive transitions are applicable). Then the sequence of choices of instantaneous descriptions made by T in a given computation can be encoded as a string y of 0's and 1's, such that $\lg(y) \leq p(\lg(x))$.

Thus we can construct a deterministic Turing machine T', with $\Sigma^* \times \Sigma^*$ as its domain of inputs, which, on input $<x,y>$, simulates the action of T on input x with the sequence of choices y. Clearly T' operates in polynomial time, and L is obtained by polynomial bounded existential quantification from the set of pairs of strings accepted by T'.

The class NP is very extensive. Loosely, a recognition problem is in NP if and only if it can be solved by a backtrack search of polynomial bounded depth. A wide range of important computational problems which are not known to be in P are obviously in NP. For example, consider the problem of determining whether the nodes of a graph G can be colored with k colors so that no two adjacent nodes have the same color. A nondeterministic algorithm can simply guess an assignment of colors to the nodes and then check (in polynomial time) whether all pairs of adjacent nodes have distinct colors.

In view of the wide extent of NP, the following theorem due to Cook is remarkable. We define the satisfiability problem as follows:

SATISFIABILITY
INPUT: Clauses $C_1, C_2, \ldots, C_p$
PROPERTY: The conjunction of the given clauses is satisfiable; i.e., there is a set $S \subseteq \{x_1, x_2, \ldots, x_n; \overline{x}_1, \overline{x}_2, \ldots, \overline{x}_n\}$ such that
a) S does not contain a complementary pair of literals
and b) $S \cap C_k \neq \emptyset, \ k = 1, 2, \ldots, p.$

Theorem 2 (Cook). If $L \in NP$ then $L \propto SATISFIABILITY.$ {#karp-1972-reducibility-thm-2 .statement tag=0506}

The theorem stated by Cook (1971) uses a weaker notion of reducibility than the one used here, but Cook's proof supports the present statement.

Corollary 1. $P = NP \Leftrightarrow SATISFIABILITY \in P.$ {#karp-1972-reducibility-cor-1 .statement tag=0507}

Proof. If SATISFIABILITY $\in P$ then, for each $L \in NP, \ L \in P$, since $L \propto SATISFIABILITY$. If SATISFIABILITY $\notin P$, then, since clearly SATISFIABILITY $\in NP, \ P \neq NP$.

Remark. If $P = NP$ then $NP$ is closed under complementation and polynomial-bounded existential quantification. Hence it is also closed under polynomial-bounded universal quantification. It follows that a polynomial-bounded analogue of Kleene's Arithmetic Hierarchy [Rogers (1967)] becomes trivial if $P = NP$.

Theorem 2 shows that, if there were a polynomial-time algorithm to decide membership in SATISFIABILITY then every problem solvable by a polynomial-depth backtrack search would also be solvable by a polynomial-time algorithm. This is strong circumstantial evidence that SATISFIABILITY $\notin P$. {#karp-1972-reducibility-thm-2-2 .statement tag=0508}
