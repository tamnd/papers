---
paper: cook-1971-np
title: The Complexity of Theorem-Proving Procedures
authors:
  - Stephen A. Cook
year: 1971
venue: STOC
field: theory
section: "2"
section_title: Discussion
tag: "0349"
kind: section
lang: en
source: https://www.cs.toronto.edu/~sacook/homepage/1971.pdf
pdf_sha256: aacaca0dd6db8b409317a2de282734539c3186a72cff1cb4dd601c76a4ddfb75
pdf_pages: 4-5
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 7f481a5895fa09c26adac7d195f2f950d7c752b63491b03dc1fd7a32088680d6
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Theorem 1 and its corollary give strong evidence that it is not easy to determine whether a given proposition formula is a tautology, even if the formula is in normal disjunctive form. Theorems 1 and 2 together suggest that it is fruitless to search for a polynomial decision procedure for the subgraph problem, since success would bring polynomial decision procedures to many other apparently intractible problems. Of course the same remark applies to any combinatorial problem to which {tautologies} is P-reducible. {#cook-1971-np-thm-1-2 .statement tag=034A}

Furthermore, the theorems suggest that {tautologies} is a good candidate for an interesting set not in $\mathcal{L}^*$, and I feel it is worth spending considerable effort trying to prove this conjecture. Such a proof would be a major breakthrough in complexity theory.

In view of the apparent complexity of {DNF tautologies}, it is interesting to examine the Davis-Putnam procedure [5]. This procedure was designed to determine whether a given formula in conjunctive normal form is satisfiable, but of course the "dual" procedure determines whether a given formula in disjunctive normal form is a tautology. I have not yet been able to find a series of examples showing the procedure (treated sympathetically to avoid certain pitfalls) must require more than polynomial time. Nor have I found an interesting upper bound for the time required.

If we let strings represent natural numbers, (or k-tuples of natural numbers) using m-adic or other suitable notation, then the notions in the preceding sections can be made to apply to sets of numbers (or k-place relations on numbers). It is not hard to see that the set of relations accepted in polynomial time by some nondeterministic Turing machine is precisely the set $\mathcal{L}^+$ of relations of the form

(1) $(\exists y \leq g_k(\bar{x}))\ R(\bar{x},y)$ where $g_k(\bar{x}) = 2^{(\ell(\max \bar{x}))^k}$, $\ell(z)$ is the dyadic length of z, and $R(\bar{x}, y)$ is an $\mathcal{L}^*$ relation, ($\mathcal{L}^+$ is the class of extended positive rudimentary relations of Bennett [6]). If we remove the bound on the quantifier in formula (1), the class $\mathcal{L}^+$ would become the class of recursively enumerable sets. Thus if $\mathcal{L}^+$ is the analog of the class of r.e. sets, then determining tautologyhood is the analog of the halting problem; since, according to theorem 1, {tautologies} has the complete $\mathcal{L}^+$ degree just as the halting problem has the complete r.e. degree. Unfortunately, the diagonal argument which shows the halting problem is not recursive apparently cannot be adapted to show {tautologies} is not in $\mathcal{L}^*$.
