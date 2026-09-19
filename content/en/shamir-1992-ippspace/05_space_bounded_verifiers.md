---
paper: shamir-1992-ippspace
title: IP = PSPACE
authors:
  - Adi Shamir
year: 1992
venue: Journal of the ACM
field: theory
section: "5"
section_title: Space-Bounded Verifiers
tag: "0536"
kind: section
lang: en
source: http://crypto.cs.mcgill.ca/~crepeau/COMP647/2007/
pdf_sha256: 64e55264e8386142cd8821ddccb435579ecd13a50658047d488011145d5a405f
pdf_pages: 7-8
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 24c1e2bd348e0b1dc205f6bb4b7492eaf45b61a9fa5281b1a152b4b1bea4e633
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The interactive proofs introduced in Section 4 require polynomial time and polynomial space verifiers. In this section, we prove that the space bound can be greatly improved.

Definition. A verifier is called weak if
(1) its running time is polynomial,
(2) its workspace is logarithmic,
(3) it has a two-way read-only access to a random tape,
(4) its messages consist solely of the random bits it reads.

THEOREM 7. Any PSPACE language can be accepted by a weak verifier.

Remarks. Since the accessible portion of the random tape is polynomial, we cannot "cheat" by using the head position or the location of desirable substrings as super-logarithmic auxiliary storage. Note that without the two-way access, Fortnow and Sipser [4], proved that only languages in P can be accepted by such verifiers, and without condition 4, Condon and Rompel [private communication] have already shown that logspace verifiers can accept all of IP.

PROOF (SKETCH). To use such weak verifiers in our interactive proofs, we consider the particular PSPACE complete class of QBFs obtained by the standard reduction from deterministic polynomial space Turing machine computations. We encode each configuration of such a computation (which consists of the contents of the tape, the position of the head, and the internal state) as a polynomially long vector $X$ of Boolean variables. If $X_1$ and $X_2$ are two configurations, then we can recursively express the existence of a legal transition of length $2^k (k \geq 1)$ between them by:

$$
Q(X_1, X_2, 2^k) = \exists X_3 \forall x_4 \exists X_5 \exists X_6 \{ [x_4 \Rightarrow (X_5 = X_1) \land (X_6 = X_3)] \\
\land [\bar{x}_4 \Rightarrow (X_5 = X_3) \land (X_6 = X_2)] \land Q(X_5, X_6, 2^{k-1}) \}.
$$

The final $Q(X_i, X_{i+1}, 1)$ is the quantifier free 3CNF formula that characterizes a single move of the given Turing machine. In this expression $X_3$ represents the middle configuration of the computation, the single Boolean variable $x_4$ chooses which half of the computation we consider, $X_5$ and $X_6$ are new configuration names, and the rest of the expression states that both halves are legal transitions of length $2^{k-1}$. When $X_1$ is the initial configuration and $X_2$ is the unique accepting configuration (with tape, initial head position, and accepting state), we can express the acceptance condition by the polynomially long QBF obtained by unrolling this recursive definition.

Such QBFs are simple by definition. Their innermost 3CNF formulas can be arithmetized with de Morgan’s laws (replacing each clause such as $z_i + z_j + z_k$ by the logically equivalent $1 - (1 - z_i)(1 - z_j)(1 - z_k)$) to yield only 0/1 values. Such values are preserved by the products that result from universal quantifiers. Since the Turing machine computation is deterministic, the existentially quantified configurations $X_3, X_5,$ and $X_6$ are uniquely determined by the endpoint configurations $X_1, X_2,$ and the selector $x_4$. When such a $\exists X_i$ is arithmetized, at most one of the exponentially many summands can be non-zero. We can thus prove by induction that the arithmetized value of such QBFs is either 0 or 1 (rather than $O(2^{2^n})$), and allow the prover to use primes of logarithmic size.

The constant degree polynomials with logarithmic coefficients can be easily handled by weak verifiers. However, to evaluate the quantifier-free subexpressions by themselves, such verifiers need access to the random values assigned to the $O(n)$ variables, which require too much storage space. We overcome this difficulty by giving the verifiers a two-way read-only access to their random tapes, where these values are stored as consecutive blocks of $O(\log n)$ bits. □

ACKNOWLEDGMENTS. I am greatly indebted to Donald Beaver, Joan Feigenbaum, Dick Lipton, Noam Nisan, Carsten Lund, Lance Fortnow, Howard Karloff, and Laci Babai for making this result possible, and would like to thank Uri Feige and Oded Goldreich for simplifying some of my earlier proofs.
