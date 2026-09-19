---
paper: karp-1972-reducibility
title: Reducibility Among Combinatorial Problems
authors:
  - Richard M. Karp
year: 1972
venue: Complexity of Computer Computations
field: theory
section: "21"
section_title: MAX CUT
tag: 051E
kind: appendix
lang: en
source: https://doi.org/10.1007/978-1-4684-2001-2_9
pdf_sha256: ae57cf641ae4f1924bdc4d7ef865edb2411c44e3040e8e546d01f1545e288e89
pdf_pages: 17-22
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 7c149b9df80d49a09e45a8391c2e6febd08da55d0032888e98d2cbd1b5ee728c
edited: true
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

INPUT: graph $G$, weighting function $w : A \to Z$, positive integer $W$
PROPERTY: There is a set $S \subseteq N$ such that

$$
\sum_{\{u, v\} \in A \\ u \in S \\ v \notin S} w(\{u, v\}) \geq W.
$$

It is clear that these problems (or, more precisely, their encodings into $\Sigma^*$), are all in $NP$. We proceed to give a series of explicit reductions, showing that SATISFIABILITY is reducible to each of the problems listed. Figure 1 shows the structure of the set of reductions. Each line in the figure indicates a reduction of the upper problem to the lower one.

To exhibit a reduction of a set $T \subseteq D$ to a set $T' \subseteq D'$, we specify a function $F : D \to D'$ which satisfies the conditions of Lemma 2. In each case, the reader should have little difficulty in verifying that $F$ does satisfy these conditions.

SATISFIABILITY $\propto$ 0-1 INTEGER PROGRAMMING

$$
c_{ij} = \begin{cases}
1 & \text{if } x_j \in C_i \\
-1 & \text{if } \overline{x}_j \in C_i \\
0 & \text{otherwise}
\end{cases} \quad i = 1, 2, \ldots, p \\
j = 1, 2, \ldots, n
$$

$$
b_i = 1 - (\text{the number of complemented variables in } C_i), \\
i = 1, 2, \ldots, p.
$$

SATISFIABILITY $\propto$ CLIQUE

$$
N = \{<\sigma, i> | \sigma \text{ is a literal and occurs in } C_i\} \\
A = \{<\sigma, i>, <\delta, j> | i \neq j \text{ and } \sigma \neq \overline{\delta}\} \\
k = p, \text{ the number of clauses.}
$$

CLIQUE $\propto$ SET PACKING

Assume $N = \{1, 2, \ldots, n\}$. The elements of the sets $S_1, S_2, \ldots, S_n$ are those two-element sets of nodes $\{i, j\}$ not in $A$.

$$
S_i = \{ \{i, j\} | \{i, j\} \notin A \}, \quad i = 1, 2, \ldots, n
$$

$$
\ell = k.
$$

CLIQUE $\propto$ NODE COVER

$G'$ is the complement of $G$.
$\ell = |N| - k$

NODE COVER $\propto$ SET COVERING

Assume $N' = \{1,2,\ldots,n\}$. The elements are the arcs of $G'$.
$S_j$ is the set of arcs incident with node $j$. $k = \ell$.

NODE COVER $\propto$ FEEDBACK NODE SET

$V = N'$
$E = \{<u,v>| \{u,v\} \in A'\}$
$k = \ell$

NODE COVER $\propto$ FEEDBACK ARC SET

$V = N' \times \{0,1\}$
$E = \{<<u,0>,<u,1>>| u \in N'\} \cup \{<<u,1>,<v,0>>| \{u,v\} \in A'\}$
$k = \ell$.

NODE COVER $\propto$ DIRECTED HAMILTON CIRCUIT

Without loss of generality assume $A' = Z_m$.
$V = \{a_1,a_2,\ldots,a_\ell\} \cup \{<u,i,\alpha>| u \in N' \text{ is incident with } i \in A' \text{ and } \alpha \in \{0,1\}\}$
$E = \{<<u,i,0>,<u;i,1>>| <u,i,0> \in V\}$
$\cup \{<<u,i,\alpha>,<v,i,\alpha>>| i \in A', u \text{ and } v \text{ are incident with } i, \alpha \in \{0,1\}\}$
$\cup \{<<u,i,1>,<u,j,0>>| u \text{ is incident with } i \text{ and } j \text{ and } \forall h, i < h < j, \text{ such that } u \text{ is incident with } h\}$
$\cup \{<<u,i,1>,a_f>| 1 \leq f \leq \ell \text{ and } \forall h > i \text{ such that } u \text{ is incident with } h\}$
$\cup \{<a_f,<u,i,0>>| 1 \leq f \leq \ell \text{ and } \forall h < i \text{ such that } u \text{ is incident with } h\}$.

DIRECTED HAMILTON CIRCUIT $\propto$ UNDIRECTED HAMILTON CIRCUIT

$N = V \times \{0,1,2\}$
$A = \{<<u,0>,<u,1>>,<<u,1>,<u,2>>| u \in V\}$
$\cup \{<<u,2>,<v,0>>| <u,v> \in E\}$

SATISFIABILITY $\propto$ SATISFIABILITY WITH AT MOST 3 LITERALS PER CLAUSE

Replace a clause $\sigma_1 \cup \sigma_2 \cup \cdots \cup \sigma_m$, where the $\sigma_i$ are literals and $m > 3$, by

$$
(\sigma_1 \cup \sigma_2 \cup u_1)(\sigma_3 \cup \cdots \cup \sigma_m \cup \overline{u}_1)(\overline{\sigma}_3 \cup u_1)\cdots(\overline{\sigma}_m \cup u_1),
$$

where $u_1$ is a new variable. Repeat this transformation until no clause has more than three literals.

SATISFIABILITY WITH AT MOST 3 LITERALS PER CLAUSE
$\propto$ CHROMATIC NUMBER

Assume without loss of generality that $m \geq 4$.

$$
N = \{u_1, u_2, \ldots, u_m\} \cup \{\bar{u}_1, \bar{u}_2, \ldots, \bar{u}_m\} \cup \{v_1, v_2, \ldots, v_m\}
$$

$$
\cup \{D_1, D_2, \ldots, D_r\}
$$

$$
A = \{\{u_i, \bar{u}_i\} | i=1,2,\ldots,n\} \cup \{\{v_i, v_j\} | i \neq j\} \cup \{\{v_i, x_j\} | i \neq j\}
$$

$$
\cup \{\{v_i, \bar{x}_j\} | i \neq j\} \cup \{\{u_i, D_f\} | u_i \notin D_f\} \cup \{\{\bar{u}_i, D_f\} | \bar{u}_i \in D_f\}
$$

k = r + 1

CHROMATIC NUMBER $\propto$ CLIQUE COVER

G' is the complement of G
$\ell = k$.

CHROMATIC NUMBER $\propto$ EXACT COVER

The set of elements is

$$
N \cup A \cup \{<u,e,f> | u \text{ is incident with } e \text{ and } 1 \leq f \leq k\}.
$$

The sets $S_j$ are the following:
for each $f, 1 < f \leq k$, and each $u \in N$,

$$
\{u\} \cup \{<u,e,f> | e \text{ is incident with } u\};
$$

for each $e \in A$ and each pair $f_1, f_2$ such that

$$
1 \leq f_1 \leq k, \quad 1 \leq f_2 \leq k \text{ and } f_1 \neq f_2
$$

$$
\{e\} \cup \{<u,e,f>, f \neq f_1\} \cup \{<v,e,g> | g \neq f_2\},
$$

where $u$ and $v$ are the two nodes incident with $e$.

EXACT COVER $\propto$ HITTING SET

The hitting set problem has sets $U_i$ and elements $s_j$, such that $s_j \in U_i \Leftrightarrow u_i \in S_j$.

EXACT COVER $\propto$ STEINER TREE

$$
N = \{n_o\} \cup \{S_j\} \cup \{u_i\}
$$

$$
R = \{n_o\} \cup \{u_i\}
$$

$$
A = \{\{n_o, S_j\}\} \cup \{\{S_j, u_i\} | u_i \in S_j\}
$$

$$
w(\{n_o, S_j\}) = |S_j|
$$

$$
w(\{S_j, u_i\}) = 0
$$

$$
k = |\{u_i\}|.
$$

EXACT COVER $\propto$ 3-DIMENSIONAL MATCHING

Without loss of generality assume $|S_j| \geq 2$ for each $j$.
Let $T = \{<i,j> | u_i \in S_j\}$. Let $\alpha$ be an arbitrary one-one function from $\{u_i\}$ into T. Let $\pi : T \to T$ be a permutation such that, for each fixed j, $\{<i,j>| u_i \in S_j\}$ is a cycle of $\pi$.

$$
U = \{<\alpha(u_i), <i,j>, <i,j>>| <i,j> \in T\}
$$

$$
\cup \{<\beta,\sigma,\pi(\sigma)>| \text{ for all } i, \beta \neq \alpha(u_i)\}
$$

EXACT COVER $\propto$ KNAPSACK

Let $d = |\{S_j\}| + 1$. Let $e_{ji} = \begin{cases} 1 & \text{if } u_i \in S_j \\ 0 & \text{if } u_i \notin S_j \end{cases}$. Let

$$
r = |\{S_j\}|, \quad a_j = \sum e_{ji} d^{i-1} \quad \text{and} \quad b = \frac{d^t - 1}{d - 1}.
$$

KNAPSACK $\propto$ SEQUENCING

$$
p = r, \quad T_i = P_i = a_i, \quad D_i = b.
$$

KNAPSACK $\propto$ PARTITION

$$
s = r + 2 \\
c_i = a_i, \quad i = 1,2,...,r \\
c_{r+1} = b + 1 \\
c_{r+2} = (\sum_{i=1}^r a_i) + 1 - b
$$

PARTITION $\propto$ MAX CUT

$$
N = \{1,2,...,s\} \\
A = \{\{i,j\}| i \in N, j \in N, i \neq j\} \\
w(\{i,j\}) = c_i \cdot c_j \\
W = \left\lceil \frac{1}{4} \sum c_i^2 \right\rceil
$$

Some of the reductions exhibited here did not originate with the present writer. Cook (1971) showed that SATISFIABILITY $\propto$ SATISFIABILITY WITH AT MOST 3 LITERALS PER CLAUSE. The reduction

SATISFIABILITY $\propto$ CLIQUE is implicit in Cook (1970), and was also known to Raymond Reiter. The reduction

NODE COVER $\propto$ FEEDBACK NODE SET was found by the Algorithms Seminar at the Cornell University Computer Science Department. The reduction

NODE COVER $\propto$ FEEDBACK ARC SET was found by Lawler and the writer, and Lawler discovered the reduction

EXACT COVER $\propto$ 3-DIMENSIONAL MATCHING

The writer discovered that the exact cover problem was reducible to the directed traveling-salesman problem on a digraph in which the arcs have weight zero or one. Using refinements of the technique used in this construction, Tarjan showed that

EXACT COVER $\propto$ DIRECTED HAMILTON CIRCUIT and, independently, Lawler showed that

NODE COVER $\propto$ DIRECTED HAMILTON CIRCUIT .

The reduction

DIRECTED HAMILTON CIRCUIT $\propto$ UNDIRECTED HAMILTON CIRCUIT was pointed out by Tarjan.

Below we list three problems in automata theory and language theory to which every complete problem is reducible. These problems are not known to be complete, since their membership in $NP$ is presently in doubt. The reader unacquainted with automata and language theory can find the necessary definitions in Hopcroft and Ullman (1969).

EQUIVALENCE OF REGULAR EXPRESSIONS
INPUT: A pair of regular expressions over the alphabet $\{0,1\}$
PROPERTY: The two expressions define the same language.

EQUIVALENCE OF NONDETERMINISTIC FINITE AUTOMATA
INPUT: A pair of nondeterministic finite automata with input alphabet $\{0,1\}$
PROPERTY: The two automata define the same language.

CONTEXT-SENSITIVE RECOGNITION
INPUT: A context-sensitive grammar $\Gamma$ and a string $x$
PROPERTY: $x$ is in the language generated by $\Gamma$.

First we show that

SATISFIABILITY WITH AT MOST 3 LITERALS PER CLAUSE
$\propto$ EQUIVALENCE OF REGULAR EXPRESSIONS .

The reduction is made in two stages. In the first stage we construct a pair of regular expressions over an alphabet $\Delta = \{u_1, u_2, \ldots, u_n, \bar{u}_1, \bar{u}_2, \ldots, \bar{u}_n\}$. We then convert these regular expressions to regular expressions over $\{0,1\}$.

The first regular expression is $\Delta^n \Delta^*$ (more exactly, $\Delta$ is written out as $(u_1 + u_2 + \cdots + u_n + \bar{u}_1 + \cdots + \bar{u}_n)$, and $\Delta^n$ represents n copies of the expression for $\Delta$ concatenated together). The second regular expression is

$$
\Delta^n \Delta^* \cup \bigcup_{i=1}^n (\Delta^* u_i \Delta^* \bar{u}_i \Delta^* \cup \Delta^* \bar{u}_i \Delta^* u_i \Delta^*) \cup \bigcup_{h=1}^r \theta(D_h)
$$

where

$$
\theta(D_h) = \begin{cases}
\Delta^*\overline{\sigma}_1\Delta^* & \text{if } D_h = \sigma_1 \\
\Delta^*\overline{\sigma}_1\Delta^*\overline{\sigma}_2\Delta^* \cup \Delta^*\overline{\sigma}_2\Delta^*\overline{\sigma}_1\Delta^* & \text{if } D_h = \sigma_1 \cup \sigma_2 \\
\Delta^*\overline{\sigma}_1\Delta^*\overline{\sigma}_2\Delta^*\overline{\sigma}_3\Delta^* \cup \Delta^*\overline{\sigma}_1\Delta^*\overline{\sigma}_3\Delta^*\overline{\sigma}_2\Delta^* \\
\cup \Delta^*\overline{\sigma}_2\Delta^*\overline{\sigma}_1\Delta^*\overline{\sigma}_3\Delta^* \cup \Delta^*\overline{\sigma}_2\Delta^*\overline{\sigma}_3\Delta^*\overline{\sigma}_1\Delta^* \\
\cup \Delta^*\overline{\sigma}_3\Delta^*\overline{\sigma}_1\Delta^*\overline{\sigma}_2\Delta^* \cup \Delta^*\overline{\sigma}_3\Delta^*\overline{\sigma}_2\Delta^*\overline{\sigma}_1\Delta^*
& \text{if } D_h = \sigma_1 \cup \sigma_2 \cup \sigma_3 .
\end{cases}
$$

Now let m be the least positive integer $\geq \log |\Delta|$, and let $\phi$ be a 1-1 function from $\Delta$ into $\{0,1\}^m$. Replace each regular expression by a regular expression over $\{0,1\}$, by making the substitution $a \rightarrow \phi(a)$ for each occurrence of each element of $\Delta$.

EQUIVALENCE OF REGULAR EXPRESSIONS $\propto$ EQUIVALENCE OF NONDETERMINISTIC FINITE AUTOMATA

There are standard polynomial-time algorithms [Salomaa (1969)] to convert a regular expression to an equivalent nondeterministic automaton. Finally, we show that, for any $L \in NP$,

$$
L \propto \text{CONTEXT-SENSITIVE RECOGNITION}.
$$

Suppose $L$ is recognized in time $p()$ by a nondeterministic Turing machine. Then the following language $\tilde{L}$ over the alphabet $\{0,1,\#\}$ is accepted by a nondeterministic linear bounded automaton which simulates the Turing machine:

$$
\tilde{L} = \{ \#^{p(\lg(x))}_{x\#^{p(\lg(x))}} | x \in L \}.
$$

Hence $\tilde{L}$ is context-sensitive and has a context-sensitive grammar $\tilde{\Gamma}$. Thus $x \in L$ iff

$$
\tilde{\Gamma}, \#^{p(\lg(x))}_{x\#^{p(\lg(x))}}
$$

is an acceptable input to CONTEXT-SENSITIVE RECOGNITION.

We conclude by listing the following important problems in $NP$ which are not known to be complete.

GRAPH ISOMORPHISM
INPUT: graphs $G$ and $G'$
PROPERTY: $G$ is isomorphic to $G'$.

NONPRIMES
INPUT: positive integer $k$
PROPERTY: $k$ is composite.

LINEAR INEQUALITIES
INPUT: integer matrix $C$, integer vector $d$
PROPERTY: $Cx \geq d$ has a rational solution.
