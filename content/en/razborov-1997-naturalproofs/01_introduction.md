---
paper: razborov-1997-naturalproofs
title: Natural Proofs
authors:
  - Alexander A. Razborov
  - Steven Rudich
year: 1997
venue: Journal of Computer and System Sciences
field: theory
section: "1"
section_title: Introduction
tag: 020B
kind: section
lang: en
source: https://doi.org/10.1006/jcss.1997.1494
pdf_sha256: 6cf137cf878d01654aeff5dbf031e97a624cd72367b87415ff61080447de7682
pdf_pages: 2-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: c8da0b2b3fc647f0cff07dd1e91f363d16945826401d3cc0c3844cd7f259a3e6
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

It is natural to ask what makes lower bound questions such as P = ? PSPACE , P = ? NP , and P = ? NC so dicult to solve. A non-technical reason for thinking they are dicult might be that some very bright people have tried and failed { but this is hardly satisfactory. A technical reason along the same lines would be provided by a reduction to these questions from another problem known to be really hard such as the Riemann Hypothesis. Perhaps the ultimate demonstration that P = ? NP is a hard problem would be to show it to be independent of set theory (ZFC).

Another way to answer this question is to demonstrate that known methods are inherently too weak to solve problems such as P = ? NP . This approach was taken in Baker, Gill, and Solovay [7], who used oracle separation results for many major complexity classes to argue that relativizing proof techniques could not solve these problems. Since relativizing proof techniques involving diagonalization and simulation were the only available tools at the time of their work, progress along known lines was ruled out.

Because of this, people began to study these problems from the vantage of Boolean circuit complexity, rather than machines. The new goal is to prove a stronger, non-uniform version of P 6 = NP , namely that SAT (or some other problem in NP ) does not have polynomial-size circuits. Many new proof techniques have been discovered and successfully applied to prove lower bounds in circuit complexity, as exempli ed by [11, 1, 40, 14, 27, 28, 3, 2, 37, 4, 29, 36, 8, 5, 23, 24, 15, 13, 17, 26, 6] among others, although the lower bounds have not come up near the level of P or even NC . These techniques are highly combinatorial, and in principle they are not subject to relativization. They exist in a much larger variety than their recursion-theoretic predecessors. Even so, in this paper we give evidence of a general limitation on their ability to resolve P = ? NP and other hard problems.

Section 2 introduces and formalizes the notion of a natural proof . We argue that all lower bound proofs known to date against non-monotone Boolean circuits are natural, or can be represented as natural . In Section 3 we present diverse examples of circuit lower bound proofs and show why they are natural in our sense. While Section 5 gives some general theoretical reasons why proofs against circuits tend to be natural. Section 4 gives evidence that \naturalizable" proof techniques cannot prove strong lower bounds on circuit size . In particular, we show modulo a widely believed cryptographic assumption that no natural proof can prove super-polynomial lower bounds for general circuits , and show unconditionally that no natural proof can prove exponential lower bounds on the circuit size of the discrete logarithm problem .

Natural proofs form a hierarchy according to the complexity of the combinatorial property involved in the proof. We show without using any cryptographic assumption that AC 0 -natural proofs, which are sucient to prove the parity lower bounds of [11, 40, 14], are inherently incapable of proving the bounds for AC 0 [ q ]-circuits of [29, 36, 8].

One application of natural proofs was given in [33]. It was shown there that in certain fragments of Bounded Arithmetic any proof of super-polynomial lower bounds for general circuits would naturalize, i.e., could be recast as a natural proof. Combined with the material contained in Section 4 of this paper, this leads to the independence of such lower bounds from these theories (assuming our cryptographic hardness assumption). See also [19, 34] for interpretations of this approach in terms of the propositional calculus, [10, 25] for further results in this direction, and [35] for an informal survey.

### 1.1. Notation and de nitions {#razborov-1997-naturalproofs-s1-1 .section tag=020C}

We denote by F n the set of all Boolean functions in n variables. Most of the time, it will be convenient to think of f 2 F as a binary string of length 2 n , called the truth-table of n n f n . f n is a randomly chosen function from F n , and in general we reserve the bold face in our formulae for random objects.

The notation AC k , NC k is used in the standard sense to denote non-uniform classes. AC 0 [ m ], TC 0 and P=poly are the classes of functions computable by polynomial-size bounded-depth circuits allowing MOD - m gates, bounded-depth circuits allowing threshold gates and unbounded-depth circuits over a complete basis, respectively.
