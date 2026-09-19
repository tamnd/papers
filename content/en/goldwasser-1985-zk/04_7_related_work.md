---
paper: goldwasser-1985-zk
title: The Knowledge Complexity of Interactive Proof-Systems
authors:
  - Shafi Goldwasser
  - Silvio Micali
  - Charles Rackoff
year: 1985
venue: STOC
field: theory
section_title: 7. Related work.
kind: section
lang: en
source: https://people.csail.mit.edu/silvio/Selected%20Scientific%20Papers/Proof%20Systems/The_Knowledge_Complexity_Of_Interactive_Proof_Systems.pdf
pdf_sha256: 17b24f25b180ba64559a089efb443337c61c916078f73be4c496bf8d27410222
pdf_pages: 20-22
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 6e629788876f4ea1ab31e4c7d53fed4d3ab0eaab95429bb1b3c1b780e7b6d468
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

### 7.1. Work related to interactive proof systems. In studying his Arthur-Merlin games, Babai [Ba] has focused on the number of rounds, i.e., the number of times the prover and the verifier alternate in sending messages. Babai denotes the set of all languages accepted by $i$ rounds in an Arthur-Merlin proof system by $AM[i]$, and $AM[f(n)]$ denotes the set of languages accepted by an Arthur-Merlin proof system with $f(n)$ rounds. Here $f$ is a nondecreasing function from natural numbers to natural numbers, and $n$ the length of the input. {#goldwasser-1985-zk-s7-1 .section tag=052B}

The elegant simplicity of Babai's definition allowed him to show that for every constant $k$, $AM[k]$ collapses to $AM[2]$. This in turn is a subset of both $\Pi_2^p$ and nonuniform NP.

We define $IP[f(n)]$ as the class of languages having an interactive proof system with $f(n)$ rounds.

Goldwasser and Sipser [GS] show that, for all $f$, $AM[f(n)]=IP[f(n)]$.

On the other hand, Aiello, Goldwasser, and Hastad [AGH] have shown that for any two nonconstant functions $g(n)$ and $f(n)$ such that $g(n)=o(f(n))$, there exists an oracle $X$ such that (if we modify the definitions so that one is computing using the oracle $X$) $IP[g(n)]$ is strictly contained in $IP[f(n)]$. This result is tight as Babai and Moran [BM] have shown that for all constants $c>0$, $IP[f(n)]=IP[cf(n)]$. Namely, $IP[O(f(n))]$ is well defined.

An interesting question is the following. Where does IP stand with respect to the polynomial time heirarchy? Boppana, Hastad, and Zachos [BHZ] have shown that if CO-NP has a constant-round interactive proof system, then the polynomial time hierarchy collapses. Thus, from the results of [GMW], [GS], and [BHZ], it follows that graph isomorphism is not NP-complete unless the polynomial time hierarchy collapses.

Other works related to the study of randomized and nondeterministic complexity classes appear in [P] and [ZF]. In Papadimitriou’s Games Against Nature, the verifier is also a probabilistic polynomial time machine that flips coins and presents them to a prover capable of optimal moves. This is different from our model in that $L$ is said to be accepted by a game against nature if $x \in L$ implies that the probability of the prover to win the game is greater than a $\frac{1}{2}$ rather than bounded away from a $\frac{1}{2}$.

Zachos and Furer [ZF], in a work investigating the robustness of probabilistic complexity classes, introduce a framework of probabilistic existential and universal quantifiers and prove several combinatorial lemmas about them. The AM and thus IP complexity classes can be formulated in terms of these special quantifiers.

7.2. Work related to knowledge complexity. Prior to our work, the theory of knowledge had received much attention in a model-theoretic framework (see [FHV] and [HM] for discussion). There are several essential differences between this framework and ours. In the latter, knowledge is defined with respect to a specific computational model with specific computational resources. In the former framework, there are no limitations on the computational power of the participants, i.e., they “know” all logical consequences of the information they possess. (For discussion of this aspect see, Belief, Awareness, and Limited Reasoning [FH].) As for another difference, in our model knowledge is defined with respect to an available public input and is gained by computing on this input. In their model-theoretic framework knowledge is gained by being told (or witnessing) that a certain event is true (e.g., the outcome of a coin flip is heads), rather than by computing.

Galil, Haber, and Yung [GHY] proposed the following extension of the concept of a zero-knowledge interactive proof systems. A language $L$ is said to have a result-indistinguishable zero-knowledge proof system if there exists an interactive protocol $(A, B)$ such that for every string $x \in \{0, 1\}^*$, $A$ can convince $B$ that $x \in L$ or $x$ is not in $L$ (whichever is the case) with high probability, such that no passive observer $C$ can get any information of which is the case. They give a result-indistinguishable proof system for QR.

As previously mentioned, Goldreich, Micali, and Wigderson [GMW] have shown, subject to the existence of secure encryption schemes, that all languages in NP have computationally zero-knowledge proof systems. Subsequently, related notions of proof systems and zero knowledge were given by Brassard and Crepeau [BC] and Chaum [Ch]. They found that for any language $L$ in NP, there is an interactive protocol that

(1) is zero-knowledge, and
(2) proves membership in $L$ correctly (i.e., with probability approaching 1) only if factoring is computationally difficult and the prover is polynomial time.

Let us explicitly contrast their protocols with the ones in [GMW]. The latter ones

(1) correctly prove membership in $L$, and
(2) are zero-knowledge only if secure encryption schemes exist (which is true if factoring is difficult).

Finally, let us mention the recent result of Fortnow.

THEOREM [Fo]. Assume a language L has an interactive proof system (A, B) that is statistically zero-knowledge with respect to B. Then L's complement has a constant-round interactive proof system.

As a corollary, if SAT had statistically zero-knowledge proof systems, the polynomial time hierarchy would collapse.

Note that the hypothesis of Fortnow's theorem is much weaker than saying that (A, B) is a statistically zero-knowledge proof system on L, which would mean that, for all verifiers B', A is zero-knowledge on L for B'. Usually, it is defeating this latter quantifier "for all" that makes it hard to find a perfect or statistically zero-knowledge proof system. Thus Fortnow's result has the potential to be widely applicable.

Acknowledgments. We thank Mike Sipser, Steve Cook, and Mike Fischer who helped us focus on this research from its beginning. Without their enthusiastic encouragement we might not have completed this work.

Oded Goldreich and Ron Rivest, as usual, have been generous with comments and ideas. Thanks also go to Leonid Levin, Zvi Galil, and Dan Simon for having helped us in various ways.

Special thanks to Josh Cohen for simplifying our original zero-knowledge protocol for proving quadratic nonresiduosity. Thanks are also due to Manuel Blum for sharing with us so many beautiful ideas about cryptographic protocols.

Finally, we thank the anonymous referees, whose comments greatly improved this paper.
