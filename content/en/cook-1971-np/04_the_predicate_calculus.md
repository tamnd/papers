---
paper: cook-1971-np
title: The Complexity of Theorem-Proving Procedures
authors:
  - Stephen A. Cook
year: 1971
venue: STOC
field: theory
section: "3"
section_title: The Predicate Calculus
tag: 034B
kind: section
lang: en
source: https://www.cs.toronto.edu/~sacook/homepage/1971.pdf
pdf_sha256: aacaca0dd6db8b409317a2de282734539c3186a72cff1cb4dd601c76a4ddfb75
pdf_pages: 5-6
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: fe5bccbd2bed45cd7cf5b217bb425687084c90b44a55d123fa9611d32f55cf5d
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Formulas in the predicate calculus are represented by strings in a manner similar to the propositional calculus. In addition to the symbols for the latter, we need the quantifier symbols $\forall$ and $\exists$, and symbols for forming an infinite list of individual variables, and infinite lists of function and predicate symbols of each order (of course the underlying alphabet $\Sigma$ is still finite).

Suppose Q is a procedure which operates on the above formulas and which terminates on a given input formula A iff A is unsatisfiable. Since there is no decision procedure for satisfiability in the predicate calculus, it follows that there is no recursive function T such that if A is unsatisfiable, then Q will terminate within T(n) steps, where n is the length of A. How then does one appraise the efficiency of the procedure?

We will take the following approach. Most automatic theorem provers depend on the Herbrand theorem, which states briefly that a formula A is unsatisfiable if and only if some conjunction of substitution instances of the functional form fn(A) of A is truth functionally inconsistent. Suppose we order the terms in the Herbrand universe of fn(A) according to rank, and then order in a natural way the substitution instances of fn(A) from the Herbrand universe. The ordering should be such that in general substitution instances which use terms with greater rank follow substitution instances which use terms of lesser rank. Let $A_1, A_2, ...$ be these substitution instances in order.

Definition: If A is unsatisfiable, then $\phi(A)$ is the least k such that $A_1 \land A_2 \land ... \land A_k$ is truth-functionally inconsistent. If A is satisfiable, then $\phi(A)$ is undefined.

Now let Q be the procedure which, given A, computes the sequence $A_1, A_2, ...$ and for each i, tests whether $A_1 \land ... \land A_i$ is truth-functionally consistent. If the answer is ever no, the procedure terminates successfully. Then clearly there is a recursive T(k) such that for all k and all formulas A, if the length of $A \leq k$ and $\phi(A) \leq k$, then Q will terminate within T(k) steps. We suggest that the function T(k) is a measure of the efficiency of Q.

For convenience, all procedures in this section will be realized on single tape Turing machines, which we shall call simply machines.

Definition: Given a machine $M_Q$ and recursive function $T_Q(k)$, we will say $M_Q$ is of type Q and runs within time $T_Q(k)$ provided that when $M_Q$ starts with a predicate formula A written on its tape, then $M_Q$ halts if and only if A is unsatisfiable, and for all k, if $\phi(A) \leq k$ and $|A| \leq \log_2 k$, then $M_Q$ halts within $T_Q(k)$ steps. In this case we will also say that $T_Q(k)$ is of type Q. Here $|A|$ is the length of A.

The reason for the condition $|A| \leq \log_2 k$ instead of $|A| \leq k$, is that with the latter condition, finding a lower bound for $T_Q(k)$ would be nearly equivalent to finding a lower bound for the decision problem for the propositional calculus. In particular, theorem 3A would become obvious and trivial.

Theorem 3: A) For any $T_Q(k)$ of type Q, {#cook-1971-np-thm-3 .statement tag=0412}

$$
\frac{T_Q(k)}{\sqrt{k}/(\log k)^2}
$$

is unbounded.

B) There is a $T_Q(k)$ of type Q such that

$$
T_Q(k) \leq k^2 (\log k)^2
$$

Outline of proof: A). Given any machine M, one can construct a predicate formula $A(M)$ which is satisfiable if and only if M never halts when starting on a blank tape. This is done along the lines described in Wang [7] in the proof which reduces the halting problem to the decision problem for the predicate calculus. Further, if M halts in s steps, then

$$
\phi(A(M)) \leq s^2
$$

Thus, if, contrary to (2), $T_Q(k) = O(\sqrt{k}/\log^2 k)$, then a modification of $M_Q$ could verify in only

$$
O(\sqrt{s^2}/\log^2 s^2) = O(s/\log^2 s)
$$

steps that M halted in s steps (provided $m \leq \log s^2$, where m is the length of $A(M)$). A diagonal argument (see [8] p. 153) shows that this is impossible in general.

B) The machine $M_Q$ operates in time $T_Q$ by following the procedure outlined at the beginning of this section. Note that the formula $A_1 \& A_2 \& \ldots \& A_k$ has length $O(k \log^2 k)$, since we can assume $|A| \leq \log k$.

Theorem 4: If the set S of strings is accepted by a nondeterministic machine within time $T(n) = 2^n$, and if $T_Q(k)$ is an honest (i.e. real-time countable) function of type Q, then there is a constant K so S can be recognized by a deterministic machine within time $T_Q(K8^n)$. {#cook-1971-np-thm-4 .statement tag=0413}

Proof: Suppose $M_1$ is a nondeterministic machine which accepts S in time $2^n$. Let $M_2$ be a nondeterministic machine which simulates $M_1$ for exactly $2^n$ steps and then halts, unless $M_1$ accepts the input, in which case $M_2$ computes forever. Thus for all strings w, if $w \in S$ then there is a computation for which $M_2$ with input w fails to halt, and if $w \notin S$, then $M_2$ with input w halts within $4^n$ steps for all computations. Now given w of length n, we may construct a formula $A(w)$ of length $O(n)$ such that $A(w)$ is satisfiable if and only if $M_1$ accepts w. ($A(w)$ is constructed in a way similar to $A(M)$ in the proof of 1A). Further, if $M_2$ halts within $4^n$ steps for all possible computations, then

$$
\phi(A(w)) \leq K(4^n)^2 = K8^n
$$

Thus, a deterministic machine M can be constructed to determine whether $w \in S$ by presenting $M_Q$ with input $A(w)$. If no result appears within $T_Q(K8^n)$ steps, then $w \in S$, and otherwise $w \notin S$.
