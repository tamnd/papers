---
paper: shamir-1992-ippspace
title: IP = PSPACE
authors:
  - Adi Shamir
year: 1992
venue: Journal of the ACM
field: theory
section: "3"
section_title: '*The Arithmetization of QBF*'
tag: "0531"
kind: section
lang: en
source: http://crypto.cs.mcgill.ca/~crepeau/COMP647/2007/
pdf_sha256: 64e55264e8386142cd8821ddccb435579ecd13a50658047d488011145d5a405f
pdf_pages: 3-4
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 68af5203b6b7001e6a145d72346d008447d62d07b00d15d90ab116e3803f5f89
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The problem of deciding whether a given closed QBF is true or false can be expressed in an arithmetic form by using the following syntactic transformations:

(1) Replace each Boolean variable $x_i$ by a new variable $z_i$, which can range over the (positive and negative) integers $\mathbb{Z}$.
(2) Replace each occurrence of $\bar{x}_i$ by $(1 - z_i)$.
(3) Replace $\land$ by integer multiplication $\cdot$, $\lor$ by integer addition $+$, the universal quantification $\forall x_i$ by the integer product $\prod_{z_i \in \{0,1\}}$, and the existential quantifier $\exists x_i$ by the integer sum $\sum_{z_i \in \{0,1\}}$.

*Example.* Consider the true QBF:

$$
B = \forall x_1 \exists x_2 [(x_1 \land x_2) \lor \exists x_3 (\bar{x}_2 \land x_3)].
$$

Its arithmetization yields:

$$
A = \prod_{z_1 \in \{0,1\}} \sum_{z_2 \in \{0,1\}} \left[ (z_1 \cdot z_2) + \sum_{z_3 \in \{0,1\}} (1 - z_2) \cdot z_3 \right],
$$

which can be evaluated to the integer 2.

**Theorem 2.** *A closed QBF B is true iff the value of its arithmetic form A is nonzero.* {#shamir-1992-ippspace-thm-2 .statement tag=0532}

*Proof.* By straightforward induction on the structure of B. □

*Remarks.*
(1) A problem may arise if we try to express a negated $\overline{B}$ directly as $(c - A)$, since the value c of the arithmetic form A of B is difficult to compute. We avoid this difficulty by allowing negated variables but no negated expressions in our definition of QBFs. This is not a real limitation, since we can always push the negations in B all the way to the variables without increasing its structural complexity.
(2) We cannot replace the boolean = by arithmetic = , since we want to interpret different non-zero integers as the same Boolean value T. We thus have to replace $x_i = x_j$ by $(x_i \land x_j) \lor (\bar{x}_i \land \bar{x}_j)$ and arithmetize the expression as $z_i z_j + (1 - z_i)(1 - z_j)$.

When B is true, the value of A can be quite large. However, we can upper bound this value as follows:

**Theorem 3.** *Let B be a closed QBF of size n. Then the value of its arithmetic form A cannot exceed $O(2^{2^n})$.* {#shamir-1992-ippspace-thm-3 .statement tag=0533}

*Proof.* For any (potentially open) subexpression $B'$ of B, define $v(B')$ as the maximal value of the arithmetic form of $B'$ under all the possible 0/1 substitutions to the free variables.

This value satisfies:

(1) If $B'$ is $x_i$ or $\bar{x}_i$, then $\nu(B') = 1$.
(2) If $B'$ is $B'' \lor B'''$, then $\nu(B') \leq \nu(B'') + \nu(B''')$.
(3) If $B'$ is $B'' \land B'''$, then $\nu(B') \leq \nu(B'') \cdot \nu(B''')$.
(4) If $B'$ is $\exists x_i B''$, then $\nu(B') \leq 2\nu(B'')$.
(5) If $B'$ is $\forall x_i B''$, then $\nu(B') \leq \nu(B'')^2$.
(6) When $B'$ is closed, $\nu(B')$ coincides with the value of its arithmetic form.

It is easy to verify that $O(2^{2^n})$ satisfies all the recursive inequalities. This bound cannot be substantially improved, since for

$$
B = \forall x_1 \forall x_2 \cdots \forall x_{n-1} \exists x_n (x_n \lor \bar{x}_n),
$$

$\nu(\exists x_n (x_n \lor \bar{x}_n)) = 2$, and each universal quantifier squares the previous value. $\Box$

Since such large numbers cannot be handled by the polynomial time verifiers in our interactive protocols, we reduce them modulo some smaller prime $p$.

Theorem 4. *Let B be a closed QBF of size n. Then there exists a prime p of length polynomial in n such that $A \neq 0 \pmod{p}$ iff B is true.* {#shamir-1992-ippspace-thm-4 .statement tag=0534}

Proof. Assume first that $A$ is a non-zero integer. If it is zero modulo all the polynomial size primes, then by the Chinese remainder theorem it is zero modulo their product as well. Since by the prime number theorem this product is $\Omega(2^{2^{nd}})$ for any desired constant $d$, this contradicts the assumption that $A$ is non-zero and at most $O(2^{2^n})$. On the other hand, if $B$ is false, then $A = 0$ modulo any prime. $\Box$
