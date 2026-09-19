---
paper: cook-1971-np
title: The Complexity of Theorem-Proving Procedures
authors:
  - Stephen A. Cook
year: 1971
venue: STOC
field: theory
section: "4"
section_title: 'More Discussion:'
tag: "0414"
kind: section
lang: en
source: https://www.cs.toronto.edu/~sacook/homepage/1971.pdf
pdf_sha256: aacaca0dd6db8b409317a2de282734539c3186a72cff1cb4dd601c76a4ddfb75
pdf_pages: 6-7
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 5c67e4468d8cfa9c468ec70d6fd9b85d49cc08aadf42d1f321866bad437c2be1
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

There is a large gap between the lower bound of $\sqrt{k}/(\log k)^2$ for time functions $T_Q(k)$ given in theorem 3A and a possible

$$
T_Q(k) = k^2 k^{(\log k)^2}
$$

given in 3B. However, there are reasons for the gap. For example, if we could improve the result in 3B and find a $T_Q(k)$ bounded by a polynomial in k, then by theorem 4 we could simulate a nondeterministic $2^n$ time bounded machine deterministically in time $p(2^n)$ for some polynomial p. This is contrary to experience which indicates deterministic simulation of a nondeterministic $T(n)$ time bounded machine requires time $k^{T(n)}$ in general.

On the other hand, if we could push up the lower bound given in theorem 3A and show

$$
\frac{T_Q(k)}{2^k}
$$

is unbounded, then we could conclude {Tautologies} $\notin \mathcal{L}^*$, since otherwise the general Herbrand proof procedure would provide a $T_Q(k)$ smaller than $2^k$. Thus such an improvement in 3A would require a major breakthrough in complexity theory.

The field of mechanical theorem proving badly needs a basis for comparing and evaluating the dozens of procedures which appear in the literature. Performance of a procedure on examples by computer is a good criterion, but not sufficient (unless the procedure proves useful in some practical way). A theoretical complexity criterion is needed which will bring out fundamental limitations and suggest new goals to pursue.

The criterion suggested here (the function $T_Q(k)$) is probably too crude. For example, it might be better to make $T_Q(k)$ a function of several variables, of which one is $\phi(A)$, and another might be the minimum number of substitution instances of $fn(A)$ needed to form a contradiction (note that in general not all of $A_1, A_2, \ldots, A_{\phi(A)}$ are needed.)

$T_Q(k)$ may be a crude measure, but it does provide a basis for discussion, and, I hope, will stimulate progress toward finding better complexity measures for theorem provers.
