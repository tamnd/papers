---
paper: karp-1972-reducibility
title: Reducibility Among Combinatorial Problems
authors:
  - Richard M. Karp
year: 1972
venue: Complexity of Computer Computations
field: theory
section: "4"
section_title: COMPLETE PROBLEMS
tag: "0509"
kind: appendix
lang: en
source: https://doi.org/10.1007/978-1-4684-2001-2_9
pdf_sha256: ae57cf641ae4f1924bdc4d7ef865edb2411c44e3040e8e546d01f1545e288e89
pdf_pages: 13-14
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 6e4a9e704a52fe0986e7807f4ce2288b27bbb5debc46282c9551b7535a3a18c4
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The main object of this paper is to establish that a large number of important computational problems can play the role of SATISFIABILITY in Cook's theorem. Such problems will be called complete.

Definition 5. The language $L$ is (polynomial) complete if {#karp-1972-reducibility-def-5 .statement tag=050A}
a) $L \in NP$
and b) SATISFIABILITY $\propto L$.

Theorem 3. Either all complete languages are in $P$, or none of them are. The former alternative holds if and only if $P = NP$. {#karp-1972-reducibility-thm-3 .statement tag=050B}

We can extend the concept of completeness to problems defined over countable domains other than $\Sigma^*$.

Definition 6. Let $D$ be a countable domain, e a "standard" one-one encoding $e : D \to \Sigma^*$ and T a subset of D. Then T is complete if and only if $e(D)$ is complete. {#karp-1972-reducibility-def-6 .statement tag=050C}

Lemma 2. Let D and D' be countable domains, with one-one encoding functions e and e'. Let $T \subseteq D$ and $T' \subseteq D'$. Then $T \propto T'$ if there is a function $F : D \to D'$ such that {#karp-1972-reducibility-lem-2 .statement tag=050D}
a) $F(x) \in T' \Leftrightarrow x \in T$
and b) there is a function $f \in \Pi$ such that $f(x) = e'(F(e^{-1}(x)))$ whenever $e'(F(e^{-1}(x)))$ is defined.

The rest of the paper is mainly devoted to the proof of the following theorem.

Main Theorem. All the problems on the following list are complete.

1. SATISFIABILITY

COMMENT: By duality, this problem is equivalent to determining whether a disjunctive normal form expression is a tautology.

2. 0-1 INTEGER PROGRAMMING

INPUT: integer matrix C and integer vector d
PROPERTY: There exists a 0-1 vector x such that Cx = d.

3. CLIQUE

INPUT: graph G, positive integer k
PROPERTY: G has a set of k mutually adjacent nodes.

4. SET PACKING

INPUT: Family of sets {S_j}, positive integer $\ell$
PROPERTY: $\{ S_j \}$ contains $\ell$ mutually disjoint sets.
