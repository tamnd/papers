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
pdf_pages: "5"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 8d17fdd66c91c64643edd8ff9b33a9bf04897c955de569276b8fdb0d03d45d01
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
