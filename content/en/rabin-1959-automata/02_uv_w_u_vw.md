---
paper: rabin-1959-automata
title: Finite Automata and Their Decision Problems
authors:
  - Michael O. Rabin
  - Dana Scott
year: 1959
venue: IBM Journal of Research and Development
field: theory
section_title: $$ (uv)w = U(vw). $$
kind: section
lang: en
source: https://doi.org/10.1147/rd.32.0114
pdf_sha256: 508c4c091d32b809ff5a75d91f4f313aa7f88b02e533dceb2146f34b196fdc03
pdf_pages: 8-9
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: d546ae708f5b8c72121ccefdfcaf26aa835aec42daddf4d621c4624077fb833e
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

This leads to the introduction of finite exponents where we define $U^n = UU \ldots U$ (n times) with the convention than $U^0 = \{\Lambda\}$. Finally, if $U$ is a set of tapes we can form the closure of $U$, in symbols $cl(U)$, which is the least set $V$ containing $U$, having $\Lambda$ as an element, and such that whenever $x, y$ are in $V$ then $xy$ is in $V$. Another definition is given by the equation

$$
cl(U) = U^0 \cup U^1 \cup U^2 \cup U^3 \ldots,
$$

where the infinite union extends all over finite exponents. We may prove at once about these operations that the class $\mathcal{T}$ is closed under them.

Theorem 13. *The class $\mathcal{T}$ is closed under the formation of complex products and closures of sets in $\mathcal{T}$.* {#rabin-1959-automata-thm-13 .statement tag=02E6}

*Proof:* Assume first that $U, V$ are in $\mathcal{T}$. Let $U = T(\mathfrak{A})$ and $V = T(\mathfrak{B})$ where $\mathfrak{A}$ and $\mathfrak{B}$ are ordinary automata with $\mathfrak{A} = (S, M, s_0, F)$ and $\mathfrak{B} = (T, N, t_0, G)$. We need only find a nondeterministic machine $\mathfrak{C}$ such that $UV = T(\mathfrak{C})$. We may assume that the sets $S$ and $T$ have no elements in common, and then equate $\mathfrak{C} = (S \cup T, P, \{s_0\}, G)$ where the function $P$ is defined as follows:

$$
P(s, \sigma) = \{M(s, \sigma)\}, \quad \text{if } s \text{ is in } S - F;
$$

$$
P(s, \sigma) = \{M(s, \sigma), N(T_0, \sigma)\}, \quad \text{if } s \text{ is in } F;
$$

$$
P(t, \sigma) = N(t, \sigma), \quad \text{if } t \text{ is in } T.
$$

The straightforward proof that $\mathfrak{C}$ has the desired property is left to the reader.

Next, we must show why $Hcl(U)$ is in $\mathcal{T}$. We construct a machine $\mathfrak{D}$ such that $cl(U) = T(\mathfrak{D})$, where $\mathfrak{D}$ is allowed to be nondeterministic. Simply let $\mathfrak{D} = (S, Q, s_0, F)$, where the function $Q$ is defined as follows:

$$
Q(s, \sigma) = \{M(s, \sigma)\}, \quad \text{if } s \text{ is in } S - F;
$$

$$
Q(s, \sigma) = \{M(s, \sigma), M(s_0, \sigma)\}, \quad \text{if } s \text{ is in } F.
$$

The easy completion of the proof is left to the reader.

**Theorem 14.** (Kleene-Myhill). *The class $\mathcal{T}$ is the least class of sets of tapes containing the finite sets and closed under the formation of unions, complex products, and closures of sets.* {#rabin-1959-automata-thm-14 .statement tag=02E7}

The full proof of Theorem 14 will not be given. Instead we give a brief account of the method of proof needed. Let $\mathcal{U}$ be the least class closed under the operations mentioned in the theorem. That $\mathcal{U} \subset \mathcal{T}$ is the content of Theorems 5, 5.1, and 13. To prove that $\mathcal{T} \subset \mathcal{U}$, consider each set in $\mathcal{T}$ to be of the form $T(\mathfrak{A})$, where $\mathfrak{A}$ is nondeterministic, and proceed by a kind of induction on $\mathfrak{A}$. In more precise terms, define the *weight* of $\mathfrak{A}$, in symbols $|\mathfrak{A}|$, to be the sum of all the cardinal numbers of the sets $M(s, \sigma)$ for all $s$ in $S$ and $\sigma$ in $\Sigma$. Then by assuming that $T(\mathfrak{B})$ is in $\mathcal{U}$ for all $\mathfrak{B}$ with $|\mathfrak{B}| < |\mathfrak{A}|$, one can prove that $T(\mathfrak{A})$ is also in $\mathcal{U}$. The details, however, are tiring.

This discussion completes our survey of the closure properties of the class of definable sets begun in Section 3, and the authors are not aware of any other interesting operations on sets that can be effected by constructions of automata that we have not already indicated. The remainder of this paper will be therefore devoted to generalizations of the notion of an automaton.

*7. Two-way automata*

Trying to further generalize the notion of an automaton, we consider automata which are not confined to a strict forward motion across their tapes. This leads to the following definition, which is a direct extension of Definition 1.

**Definition 13.** *Let $L = \{-1, 0, +1\}$. A two-way (finite) automation over a finite alphabet $\Sigma$ is a system $\mathfrak{A} = (S, M, s_0, F)$ where $S$ is a finite non-empty set (the set of internal states of $\mathfrak{A}$), $M$ is a function from $S \times \Sigma$ into $L \times S$ (the table of moves of $\mathfrak{A}$), $s_0$ is an element of $S$ (the initial state of $\mathfrak{A}$), and $F$ is a subset of $S$ (the set of designated final states of $\mathfrak{A}$).* {#rabin-1959-automata-def-13 .statement tag=02E9}

A two-way automaton $\mathfrak{A}$ operates as follows: When given a tape, i.e., a finite linear sequence of squares each containing a single symbol of the alphabet $\Sigma$, $\mathfrak{A}$ is set in internal state $s_0$ scanning the first (leftmost) square of the tape. At each stage of the machine's operation, if the internal state is $s$, the scanned symbol is $\sigma$, and $M(s, \sigma) = (p, s')$, where $p$ is one of $-1, 0, 1$, then $\mathfrak{A}$ will move one square to the left, stay where it is, or move one square to the right, according as $p = -1, 0, 1$; furthermore, $\mathfrak{A}$ will enter internal state $s'$. The operation described just now is called an *atomic step* of $\mathfrak{A}$. After completion of an atomic step, $\mathfrak{A}$ is again in a certain internal state scanning a certain symbol, and a new atomic step is performed, and so on.

If, when operating in this way on a given tape, $\mathfrak{A}$ will eventually *get off* the tape on the right side and at that time be in a state in $F$, then we shall say that the tape is *accepted* by $\mathfrak{A}$. The formal definition is as follows:

```text
**Definition 14.** *The set $T(\mathfrak{A})$ of tapes accepted by the two-way automaton $\mathfrak{A}$ is the set of all sequences $\sigma_0 \ldots \sigma_{n-1}$ of symbols from the alphabet $\Sigma$ for which there exist an integer $m > 0$, a sequence of integers $p_0, \ldots, p_m$, and a sequence $s_0, \ldots, s_m$ of internal states of $\mathfrak{A}$ such that*
(i) $p_0 = 0$ and $s_0$ is the initial state of $\mathfrak{A}$;
(ii) $0 \leq p_i < n$ for $i = 0, \ldots, m-1$;
(iii) $p_m = n$ and $s_m$ is in $F$;
(iv) $(p_i - p_{i-1}, s_i) = M(s_{i-1}, \sigma_{p_{i-1}})$ for $i = 1, \ldots, m$.
```

In the above definition the sequence $p_0, \ldots, p_m$ should be interpreted as the sequence of positions of the machine $\mathfrak{A}$ on the tape; thus, $p_i - p_{i-1}$ indicates the change in position of the machine from time $i-1$ to time $i$. Condition (ii), for example, means that the machine does not run off the tape before the computation has been completed.

In analogy with Definition 3 we shall say that a set $P$ of tapes is *definable by a two-way automaton* if there exists some two-way automaton $\mathfrak{A}$ such that $T(\mathfrak{A}) = P$.

To avoid confusion we shall, from now on, refer to the automata discussed in Sections 1-6 as *one-way automata*.

Let us consider an example of a two-way machine illustrating the complicated fashion in which such a machine can operate on a given tape. Let $\mathfrak{A}$, $\mathfrak{B}$, and $\mathfrak{C}$, be three one-way automata over the same alphabet $\Sigma$. We combine these automata into a single two-way automaton $\mathfrak{D}$ having the following flow diagram. Given a tape $t$ the automaton $\mathfrak{A}$ (which we imagine as being a part of $\mathfrak{D}$) starts reading it on the left end and proceeds from left to right until a designated final state of $\mathfrak{A}$ is reached; when this happens $\mathfrak{D}$ goes into the initial state of $\mathfrak{B}$ and starts reading the tape from right to left until a designated final state of $\mathfrak{B}$ is reached; when this happens $\mathfrak{D}$ switches into the initial state of $\mathfrak{A}$ and again starts moving from left to right, and so on; all this time automaton
