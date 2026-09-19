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
section_title: Shafi Goldwasser†, Silvio Micali†, and Charles Rackoff‡
kind: section
lang: en
source: https://people.csail.mit.edu/silvio/Selected%20Scientific%20Papers/Proof%20Systems/The_Knowledge_Complexity_Of_Interactive_Proof_Systems.pdf
pdf_sha256: 17b24f25b180ba64559a089efb443337c61c916078f73be4c496bf8d27410222
pdf_pages: 1-14
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 456afbb2b6479d0ecfdf1fe702d337dc4ac2d7b0a553e287cf1fa553a2a30b65
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Abstract. Usually, a proof of a theorem contains more knowledge than the mere fact that the theorem is true. For instance, to prove that a graph is Hamiltonian it suffices to exhibit a Hamiltonian tour in it; however, this seems to contain more knowledge than the single bit Hamiltonian/non-Hamiltonian.

In this paper a computational complexity theory of the "knowledge" contained in a proof is developed. Zero-knowledge proofs are defined as those proofs that convey no additional knowledge other than the correctness of the proposition in question. Examples of zero-knowledge proof systems are given for the languages of quadratic residuosity and quadratic nonresiduosity. These are the first examples of zero-knowledge proofs for languages not known to be efficiently recognizable.

Key words. cryptography, zero knowledge, interactive proofs, quadratic residues

AMS(MOS) subject classifications. 68Q15, 94A60

1. Introduction. It is often regarded that saying a language $L$ is in NP (that is, acceptable in nondeterministic polynomial time) is equivalent to saying that there is a polynomial time "proof system" for $L$. The proof system we have in mind is one where on input $x$, a "prover" creates a string $\alpha$, and the "verifier" then computes on $x$ and $\alpha$ in time polynomial in the length of the binary representation of $x$ to check that $x$ is indeed in $L$. It is reasonable to ask if there is a more general, and perhaps more natural, notion of a polynomial time proof system. This paper proposes one such notion.

We will still allow the verifier only polynomial time and the prover arbitrary computing power, but will now allow both parties to flip unbiased coins. The result is a probabilistic version of NP, where a small probability of error is allowed. However, to obtain what appears to be the full generality of this idea, we must also allow the prover and verifier to interact (i.e., to talk back and forth) and to keep secret their coin tosses. We call these proof systems "interactive proof systems." This notion is formally defined in § 2, where we also define what it means for a language to have an interactive proof system.

It is far from clear how to use this power of interaction. Languages with nondeterministic polynomial time algorithms or with probabilistic polynomial time algorithms have proof systems with little or no interaction. We would therefore like examples of languages that appear to have neither nondeterministic nor probabilistic polynomial time algorithms, and yet have interactive proof systems. Although we do not present any such examples here, there are now examples in the literature. Using ideas from an initial version of this paper [GMR] Goldreich, Micali, and Wigderson [GMW] have shown that the "graph nonisomorphism" language has an interactive

* Received by the editors August 26, 1985; accepted for publication (in revised form) April 18, 1988.
A preliminary version of this paper appeared in the Proceedings of the 27th Annual IEEE Symposium on Foundations of Computer Science, 1986, pp. 174-187.
Editor's Note. This paper was originally scheduled to appear in the February 1988 Special Issue on Cryptography (SIAM J. Comput., 17 (1988)).
† Laboratory for Computer Science, Massachusetts Institute of Technology, Cambridge, Massachusetts 02139. The work of these authors was supported by National Science Foundation grants DCR-84-13577 and DCR-85-09905.
‡ Computer Science Department, University of Toronto, Toronto, QNT M5S 1A4 Canada. The work of this author was supported by the Natural Sciences and Engineering Research Council of Canada under grant A3611.

proof system. Independently of this paper, Babai and Szemeredi [BS] show that certain matrix group problems have what they call “Arthur–Merlin” proof systems, which immediately implies that they have interactive proof systems. In fact, the notion of an Arthur–Merlin proof system consists of a restricted interactive proof system in which the prover sees the coin flips of the verifier. Nevertheless, Goldwasser and Sipser [GS] have shown that a language has an interactive proof system if and only if it has an Arthur–Merlin proof system.

It appears, however, that our notion of interactive proof systems generalizes in the right way to attack a novel problem. The main purpose of this current paper, in fact, is to use interactive proof systems to investigate a natural question; how much knowledge is transmitted to the verifier in an interactive proof system for $L$? For example, consider SAT, the NP-complete language of satisfiable sentences of the propositional calculus. In the obvious proof system, to prove $F \in \mathrm{SAT}$, the prover gives a satisfying assignment $I$ for the formula $F$, which the verifier then checks in polynomial time. This assignment gives the verifier much more knowledge than merely the fact that $F \in \mathrm{SAT}$; it also gives a satisfying assignment. At the other extreme, every language that can be accepted in probabilistic polynomial time has a proof system in which the prover does nothing, and hence gives no knowledge to the verifier.

We say an interactive proof system for $L$ is zero-knowledge if for each $x \in L$, the prover tells the verifier essentially nothing, other than that $x \in L$; this should be the case even if the verifier chooses not to follow the proof system but instead tries (in polynomial time) to trick the prover into revealing something. The notion of zero-knowledge is formally defined in § 3. This definition is an important contribution of this paper.

The main technical contributions of this paper are the proofs in §§ 5 and 6 that the languages QR and QNR (defined below) both have zero-knowledge interactive proof systems. These are the first zero-knowledge protocols demonstrated for languages not known to be recognizable in probabilistic polynomial time. To understand the languages QR and QNR, it helps to read the (brief) number theory background given in § 4. However, for now, let $x, y$ be integers, $0 < y < x$, such that $\gcd(x, y) = 1$; we say that $y$ is a quadratic residue mod $x$ if $y = z^2 \mod x$ for some $z$; if not, we say that $y$ is a quadratic nonresidue mod $x$. We define

$$
\begin{align*}
\mathrm{QR} &= \{(x, y) | y \text{ is a quadratic residue mod } x\}, \quad \text{and} \\
\mathrm{QNR} &= \{(x, y) | y \text{ is a quadratic nonresidue mod } x\}.
\end{align*}
$$

(Actually, QNR will be defined slightly differently in § 4.) Both QR and QNR are in NP, and thus possess an elementary proof system. For instance, to prove membership in QNR, the prover just sends $x$'s factorization. But looking ahead to zero-knowledge proof systems, let us discuss a more interesting example of a proof system for QNR.

Example 1. Let us call the prover $A$ and the verifier $B$. Say that the input is $(x, y)$. Let $n = |x|$, where $|x|$ is the length of the binary representation of $x$. We will now describe (omitting some details) an interactive proof system for QNR. $B$ begins by flipping coins to obtain random bits $b_1, b_2, \ldots, b_n$. $B$ then flips additional coins to obtain a string $\alpha$, from which $B$ computes $z_1, z_2, \ldots, z_n$ such that each $z_i$ is a random $z, 0 < z < x, \gcd(x, z) = 1$. $B$ then computes $w_1, w_2, \ldots, w_n$ as follows: for each $i$, if $b_i = 0$ then $w_i = z_i^2 \mod x$; if $b_i = 1$ then $w_i = (z_i^2 y) \mod x$. $B$ then sends $w_1, w_2, \ldots, w_n$ to $A$. For each $i$, $A$ computes (somehow) whether or not $w_i$ is a quadratic residue mod $x$, and sends $B$ a sequence of bits $c_1, c_2, \ldots, c_n$, where $c_i = 0$ if and only if $w_i$ is a quadratic residue mod $x$. $B$ checks if $b_i = c_i$ for every $i$, and if so is “convinced” that $(x, y) \in \mathrm{QNR}$. {#goldwasser-1985-zk-ex-1 .statement tag=0417}

It is not hard to see that if $(x, y) \in \mathrm{QNR}$ and both parties follow the protocol, then $B$ will become "convinced." On the other hand, if $y$ is a quadratic residue mod $x$, then so is each $w_i$, and every value for $w_i$ is equally likely; since $A$ does not see the sequence $\{b_i\}$, the probability that every $c_i = b_i$ (and hence that $B$ will be convinced) is $2^{-n}$. So this is an interactive proof system for QNR. Let us now address the question of how much knowledge $A$ may release.

It is an interesting question how zero-knowledge should be defined. If the prover is trying to prove to the verifier that $y$ is a quadratic residue mod $x$, then certainly the verifier should not be able to trick the prover into revealing a square root of $y$ mod $x$, or the factorization of $x$, or any information which would help the verifier to compute these things much faster than before. In fact, the prover should not reveal anything which would help the verifier compute *anything* much faster than before. The way to state this formally seems to be that what the verifier sees in the protocol (even if he cheats) should be something which the verifier could have computed for himself, merely from the fact that $(x, y) \in \mathrm{QNR}$. Of course, what the verifier sees in the protocol is really a probability distribution. Thus, zero-knowledge means that one can compute in polynomial time, from $(x, y) \in \mathrm{QNR}$, without a prover, the same (or almost the same) probability distribution that the verifier would see with the prover. This is defined formally in § 3. Here, let us informally discuss whether the above interactive proof system for QNR is zero-knowledge.

Consider a pair $(x, y) \in \mathrm{QNR}$, and say that $A$ follows the protocol. Can $B$ obtain any additional knowledge? For the moment, assume that $B$ follows the protocol. $B$ "sees" $[\{b_i\}, \alpha, \{w_i\}, \{c_i\}]$ distributed according to a particular distribution. Without any help from a prover, we can quickly generate a random string according to this distribution: just choose $\{b_i\}$ and $\alpha$ randomly, and then compute $\{w_i\}$ from them; then compute $c_i = b_i$ for each $i$.

Now what if $B$ were to cheat? $B$ could begin by setting $w_1 = 42$, and then behave correctly. Consider now the induced distribution on $[\{b_i\}, \alpha, \{w_i\}, \{c_i\}]$; in order to compute a random member of it (without help from a prover), we must compute whether or not 42 is a quadratic residue $x$, given $x$ and a quadratic nonresidue $y$. At this time it is not known how to compute this in polynomial time, so this proof system may not be zero-knowledge.

A zero-knowledge proof system for QNR is given in § 6. The ideas of this proof system partially come from the secret exchanging protocol of Luby, Micali, and Rackoff [LMR] and are useful there as well. They have also proved useful in the oblivious transfer protocol of Fischer, Micali, Rackoff, and Witenberg [FMRW] and for the identification scheme of Feige, Fiat, and Shamir [FFS]. These ideas have also helped Goldreich, Micali, and Wigderson [GMW] to show that the languages of "graph isomorphism" and "graph nonisomorphism" have zero-knowledge interactive proof systems.

Although we find the idea of a zero-knowledge interactive proof system fascinating in itself, the main motivation for it and the main applications of it are in the area of cryptographic protocols. For example, in the secret exchanging protocol in [LMR], one person wishes to exchange a secret with another without giving away any additional knowledge. Ideas similar to those here must be used to even define this concept.

More generally, however, it often arises at some point in a protocol that $A$ wishes to convince $B$ of some fact. Say that we know that the protocol would be secure if at this point an angel or someone $B$ trusted were to tell $B$ (truthfully) if $A$ is telling the truth. We want the notion of zero-knowledge to be such that an appropriate zero-knowledge interactive proof system could be inserted at this point instead of the trusted party, and the whole protocol would remain secure. (Of course, $A$ would have to possess some additional information enabling her to implement the part of the prover efficiently.) In particular instances, we can prove that such substitution works, but a general framework for discussing protocols must exist before the general theorem can even be stated. However, based on intuition and experience, the authors (and many others who have studied these ideas since their initial appearance) believe that the definition of zero-knowledge proposed here has the required properties.

The most important development since these results first appeared is the proof by Goldreich, Micali, and Wigderson [GMW] that, subject to a common complexity theory assumption, every language in NP has a zero-knowledge interactive proof system. These proof systems for NP languages appear to have applications in just about every protocol problem. It is almost certain that these results will vastly simplify distributed cryptographic protocol design in the future, as demonstrated by the powerful results of [GMW2].

2. Interactive proof systems. Intuitively, what should we require from an efficient theorem-proving procedure?
(1) That it should be possible to "prove" a true theorem.
(2) That it should not be possible to "prove" a false theorem.
(3) That communicating the "proof" should be efficient. Namely, regardless of how much time it takes to come up with the proof, its correctness should be efficiently verified.

The NP formalization of the concept of an efficient proof system captures one way of communicating a proof. In this section, we will generalize the NP proof system to capture a more general way of communicating a proof. The verifier will be a probabilistic polynomial time (in the length of the common input) machine that is able to exchange messages (strings) with the prover.

At the same time that we introduce probability into the proof system, we relax the classical notion of a "proof." Our verifier may erroneously be convinced of the truth of a proposition with a very small probability of error (less than $n^{-k}$ for each positive constant $k$ and all sufficiently large input-sizes $n$).

We proceed to formally define the new system.

2.1. Interactive Turing machines and protocols.

Definition. An interactive Turing machine (ITM) is a Turing machine equipped with a read-only input tape, a work tape, a random tape, one read-only communication tape, and one write-only communication tape. The random tape contains an infinite sequence of random bits, and can be scanned only from left to right. We say that an interactive machine flips a coin, meaning that it reads the next bit in its own random tape.

Figure.

Fig. 1. An interactive protocol. — denotes a read/write head, $R$ a read-only head, $W$ a write-only head. {#goldwasser-1985-zk-fig-1 .figure tag=051F}

Definition. An interactive protocol is an ordered pair of ITM's $A$ and $B$ such that $A$ and $B$ share the same input tape, $B$'s write-only communication tape is $A$'s read-only communication tape and vice versa. Machine $A$ is not computationally bounded, while machine $B$'s computation time is bounded by a polynomial in the length of the common input. The two machines take turns in being active, with $B$ being active first. During an active stage machine $A(B)$ first performs some internal computation using its input tape, work tapes, communication tape and random tape; and, second, it writes a string (for $B(A)$) on its write-only communication tape. The $i$th message of $A(B)$ is the entire string that $A(B)$ writes on its communication tape during its $i$th active stage. As soon as machine $A(B)$ writes its message, it is deactivated and machine $B(A)$ becomes active, unless the protocol has been terminated. Either machine can terminate the computation of the protocol by not sending any message in an active stage. Machine $B$ accepts (or rejects) the input by outputting accept (or reject) and terminating the protocol. The computation time of machine $B$ is the sum of the $B$'s computation time during its active stages, and it is this time that is bounded by a polynomial in the length of the input, denoted $|x|$.

2.2. Interactive proof systems.

Definition. Let $L$ be a language over $\{0, 1\}^*$. Let $(A, B)$ be an interactive protocol. We say that $(A, B)$ is an interactive proof system for $L$ if we have the following:

(1) For each $k$, for sufficiently large $x$ in $L$ given as input to $(A, B)$, $B$ halts and accepts with probability at least $1 - |x|^{-k}$. (The probabilities here are taken over the coin tosses of $A$ and $B$.)

(2) For each $k$, for sufficiently large $x$ not in $L$, for any ITM $A'$, on input $x$ to $(A', B)$, $B$ accepts with probability at most $|x|^{-k}$. (The probabilities here are taken over the coin tosses of $A'$ and $B$.)

Remark 1. The above probability of error can be decreased, say to smaller than $2^{-|x|}$, by the standard technique of repeating the protocol many times and choosing to accept by majority vote. {#goldwasser-1985-zk-rem-1 .statement tag=0520}

We now argue that this definition captures what we intuitively want from an efficient proof system. Condition (1) essentially says that, if $x \in L$, $B$ will accept with overwhelming probability. Condition (2) says that, if $x$ is not in $L$, there exists no strategy that succeeds with nonnegligible probability for convincing $B$ to accept. In fact, $B$ needs not to trust (or know the program of) the machine with which it is interacting. It is enough for $B$ to trust the randomness of its own coin tosses.

Similar to the NP proof system, note that the definition of an interactive proof system for a language emphasizes the "yes-instances": when a string is in the language, $B$ must be led to acceptance with high probability, but when a string is not in the language $A$ is not required to convince $B$ of the contrary.

A more general version of the above definition is where $A$ is not a Turing machine, but an infinite state machine. However it has been shown by Feldman in [F] that this adds no extra power to the model. In fact, he shows that with respect to language recognition it is sufficient for $A$ to be a deterministic PSPACE machine. The fact that $A$ is probabilistic is of importance to the more subtle definition of zero-knowledge, which is given in the next section.

We define IP, *Interactive Polynomial time*, to be the class of languages for which there exists interactive proof systems.

The first examples of a language in IP but not known to be in NP have been exhibited by Babai and Szemeredi [BS]. Their examples are "matrix group nonmembership" and "matrix group order," where the matrix groups over finite fields are represented by a list of generator matrices. The other, more well-known example of “graph nonisomorphism” is due to Goldreich, Micali, and Wigderson [GMW]. They have shown that the language of pairs of graphs that are nonisomorphic to each other is in IP.

2.3. Arthur–Merlin games. Babai independently conceived the notion of an “Arthur–Merlin Game,” an interactive proof system in which Merlin plays the role of $A$ and Arthur that of $B$. The interaction, though, is less “liberal” than in our model since Merlin sees all the coin tosses of Arthur. A message from Arthur to Merlin can only consist of a randomly selected string. In an interactive proof system, instead, the verifier is allowed, given a polynomial time computable function $f$, to secretly select a random string $R$ and transmit only $f(R)$ to the prover (as in the interactive proof system for QNR of Example 1).

This restriction immediately implies that the languages recognized by an Arthur–Merlin game are a subset of those having an interactive proof system. Interestingly, Goldwasser and Sipser [GS] show that they are not a proper subset. However, there is value in having both definitions around. It is easier to design protocols using the interactive proof systems definition, and it is easier to prove complexity results using the Arthur–Merlin definition.

Though the ability to make secret random choices does not help us to recognize more languages, we believe that it is crucial for recognizing languages in zero-knowledge. We make precise this belief in the conjecture of § 3.7.

An Arthur–Merlin type of interactive proof system was already implicitly used in a paper by Blum [B1]. He showed an interactive protocol for recognizing the language of the Blum integers:

$$
\mathrm{BL} = \{ n \mid p^{\alpha} \text{ divides } n \text{ and } p^{\alpha+1} \text{ does not, where } p \equiv 3 \bmod 4 \text{ is prime and } \alpha \text{ is odd} \}.
$$

The prover’s goal was to demonstrate membership in BL without having to send $n$'s prime factorization. In this proof system, the verifier talks only once and his message consists of sending the sequence of his coin tosses. Protocols of this type were also found by Goldwasser and Micali [GM1] to prove, without releasing the prime factorization membership in the languages:

$$
\mathrm{GM1} = \{ n \mid n \text{ has exactly two distinct prime divisors} \} \text{ and }
$$

$$
\mathrm{GM2} = \{ (x, n) \mid \gcd(x, \phi(n)) = 1 \} \quad \text{where } \phi(n) \text{ is the number of positive integers smaller and relatively prime to } n.
$$

3. Zero-knowledge. Rather than giving the definition of zero-knowledge only for interactive proof systems, we will give a more general definition. We will define what it means for any interactive protocol $(A, B)$ to be *zero-knowledge* for a language $L$, whether or not $(A, B)$ is a proof system for $L$. Actually the definition will not depend on $B$ at all; as we shall see, it says that for every polynomial time $B'$, the distribution that $B'$ “sees” on all its tapes, when interacting with $A$ on input $x \in L$, is “indistinguishable” from a distribution that can be computed from $x$ in polynomial time. We thus first focus on the notion of indistinguishability for random variables.

3.1. Indistinguishability of random variables. Throughout this paper, we will only consider families of random variables $U = \{ U(x) \}$ where the parameter $x$ is from a language $L$, a particular subset of $\{0, 1\}^*$, and all random variables take values in $\{0, 1\}^*$. Let $U = \{ U(x) \}$ and $V = \{ V(x) \}$ be two families of random variables. We want to express the fact that, when the length of $x$ increases, $U(x)$ essentially becomes “replaceable” by $V(x)$. To do this, we consider the following framework.

A random sample is selected either from $U(x)$ or from $V(x)$ and it is handed to a “judge.” After studying the sample, the judge will proclaim his verdict: 0 or 1. (We may interpret 0 as the judge’s decision that the sample came from $U(x)$; 1 as the decision that the sample came from $V(x)$.) It is then natural to say that $U(x)$ becomes “replaceable” by $V(x)$ for $x$ long enough if, when $x$ increases, the verdict of any judge becomes “meaningless,” that is, essentially uncorrelated to the distribution from which the sample came.

There are two relevant parameters in this framework: the size of the sample and the amount of *time* the judge is given to produce his verdict. By bounding these two parameters in different ways we obtain different notions of indistinguishability for random variables. We focus on the three notions we believe to be the most important: equality, statistical indistinguishability, and computational indistinguishability. Roughly speaking, these notions correspond to the following restrictions on the relevant parameters. If the two families of random variables $\{U(x)\}$ and $\{V(x)\}$ are equal, then the judge’s verdict will be meaningless even if he is given samples of arbitrary size and he can study them for an arbitrary amount of time. We will define the two families to be statistically indistinguishable if the judge’s verdict becomes meaningless when he is given an infinite amount of time but only random, polynomial (in $|x|$) size samples to work on. We will define the two families to be computationally indistinguishable if the judge’s verdict becomes meaningless when he is only given polynomial ($|x|$)-size samples and polynomial ($|x|$) time. Let us now proceed to formalize these notions.

**Definition** (Statistical indistinguishability). Let $L \subset \{0, 1\}^*$ be a language. Two families of random variables $\{U(x)\}$ and $\{V(x)\}$ are *statistically indistinguishable on* $L$ if

$$
\sum_{\alpha \in \{0, 1\}^*} |\operatorname{prob}(U(x) = \alpha) - \operatorname{prob}(V(x) = \alpha)| < |x|^{-c}
$$

for all constants $c > 0$ and all sufficiently long $x \in L$.

Notice that, for $U$ and $V$ as above, if a “judge” is handed a polynomial (in $|x|$) size sample, having infinite computing power will not help him to decide whether it came from $U(x)$ or $V(x)$. His answer will be essentially useless, as he will say “1” with essentially the same probability in both cases.

*Example 2.* Let $U(x)$ assign equal probability to all strings of length $|x|$, and let $V(x)$ assign probability $2^{-|x|}$ to all strings of length $|x|$, except for $0^{x|}$, which is given probability 0 and for $1^{-|x|}$, which is given probability $2^{-|x|+1}$. Then $\{U(x)\}$ and $\{V(x)\}$ are two families of random variables statistically indistinguishable on $\{0, 1\}^*$. {#goldwasser-1985-zk-ex-2 .statement tag=0521}

To formalize the notion of computational indistinguishability we make use of nonuniformity (the reasons for this choice can be found in § 3.4). Thus, our “judge,” rather than being a polynomial time Turing machine, will be a *poly-size family of circuits*. That is a family $C = \{C_x\}$ of Boolean circuits $C_x$ with one Boolean output such that, for some constant $e > 0$, all $C_x \in C$ have at most $|x|^e$ gates. In order to feed samples from our probability distributions to such circuits, we will consider only *poly-bounded* families of random variables, that is, families $U = \{U(x)\}$ such that, for some constant $d > 0$, all random variable $U(x) \in U$ assigns positive probability only to strings whose lengths are exactly $|x|^d$. If $U = \{U(x)\}$ is a poly-bounded family of random variables and $C = \{C_x\}$ a poly-size family of circuits, we denote by $P(U, C, x)$ the probability that $C_x$ outputs 1 on input a random string distributed according to $U(x)$. (Here we assume that strings assigned positive probability by $U(x)$ have lengths equal to the number of Boolean inputs of $C_x$.)

**Definition** (Computational indistinguishability). Let $L \subset \{0, 1\}^*$ be a language. Two poly-bounded families of random variables $U$ and $V$ are *computationally indistinguishable on* $L$ if for all poly-size family of circuits $C$, for all constants $c > 0$ and all sufficiently long strings $x \in L$,

$$
|P(U, C, x) - P(V, C, x)| < |x|^{-c}.
$$

This notion of computational indistinguishability was already used by Goldwasser and Micali [GM] in the context of encryption and by Yao [Y] in the context of pseudorandom generation. It is trivial that if $U$ and $V$ are identical, then they are statistically indistinguishable. It is also not hard to see that if $U$ and $V$ are statistically indistinguishable, then they are computationally indistinguishable, as follows. Let $C_x$ be a circuit and let $S$ be the set of inputs on which $C_x$ outputs 1. Since $U$ and $V$ are statistically indistinguishable, the value of $U(x)$ will be in $S$ with almost exactly the same probability that the value of $V(x)$ will be. Hence $P(U, C, x)$ will be very close to $P(V, C, x)$.

Example 3. Consider a probabilistic encryption algorithm that is secure in the sense of Goldwasser and Micali [GM]; for $n$ integer, let $U(1^n)$ and $V(1^n)$ be the random variables taking as values the possible encryptions of 0 and 1, respectively, on security parameter $n$. Then $U$ and $V$ are computationally indistinguishable on $L = \{1\}^*$. {#goldwasser-1985-zk-ex-3 .statement tag=0522}

We believe that the notion of computational indistinguishability for random variables achieves the right level of generality. Thus we will call indistinguishable any two families of random variables that are computationally indistinguishable.

Remark 2. Let us point out the robustness of the last definition. In this definition, we are handing our computationally bounded "judge" only samples of size 1. This, however, is not restrictive. We note that two families of random variables $\{U_x\}$ and $\{V_x\}$ are computationally indistinguishable (with respect to samples of size 1) if and only if when $C_x$ is given a polynomial in $|x|$ number of input strings, each independently generated according to the distribution $U_x$, then the probability of accepting is close to the probability of accepting when $V_x$ is used. {#goldwasser-1985-zk-rem-2 .statement tag=0523}

3.2. Approximability of random variables. We now formalize the notion that a random variable $U$ is essentially easy to generate. That is, there exists an efficient algorithm that randomly outputs strings in a way that is indistinguishable from $U$.

Definition. Let $M$ be a probabilistic Turing machine that on input $x$ halts with probability 1. We denote by $M(x)$ the random variable that, for each string $\alpha$, takes on $\alpha$ with exactly the same probability that $M$ on input $x$ outputs $\alpha$.

Definition. Let $L \subset \{0, 1\}^*$ be a language and $U = \{U(x)\}$ a family of random variables. We say that $U$ is perfectly approximable on $L$ if there exists a probabilistic Turing machine $M$, running in expected polynomial time, such that for all $x \in L$, $M(x)$ is equal to $U(x)$. We say that $U$ is statistically (computationally) approximable on $L$ if there exists a probabilistic Turing machine $M$, running in expected polynomial time, such that the families of random variables $\{M(x)\}$ and $\{U(x)\}$ are statistically (computationally) indistinguishable on $L$.

In what follows, we will use approximability to mean computational approximability. We are now ready to define the notion of zero-knowledge.

3.3. Zero-knowledge protocols and proof systems. We first address the issue of a "cheating verifier," $B'$, who is allowed not to follow the protocol.

Definition. Let $(A, B)$ be an interactive protocol. Let $B'$ be an interactive Turing machine that has as input $x$ and on an extra input tape $H$, where the length of $H$ is bounded above by a polynomial in the length of $x$. (Figure 1 must be emended to allow $B'$ this extra tape.) When $B'$ interacts with $A$, $A$ sees only $x$ on its input tape, whereas $B'$ sees $(x, H)$. A good way to think of $H$ is as some knowledge about $x$ that the cheating $B'$ already possesses. Alternatively, $H$ can be considered as the history of previous interactions that the cheating $B'$ is trying to use to get knowledge from $A$; this is discussed in more detail in the next section. We assume that the total computation time of $B'$ when interacting with $A$ will be bounded above by a polynomial in the length of $x$.

For a run of the protocol on common input $x$ and extra input $H$, we define the view of $B'$ to be everything that $B'$ sees. Namely, let $\sigma$ (and $\rho$) be the strings contained in the random tapes of $A$ (and $B'$). Say the computation of $A$ and $B'$, with these random choices, consist of $n$ turns with $B'$ going first, where $a_i$ (and $b_i$) are the $i$th messages of $A$ (and $B'$), respectively. Then, we say that $(\rho, b_1, a_1, \ldots, b_n, a_n)$ is the view of $B'$ on inputs $x$ and $H$, and let $\mathrm{View}_{A,B'}(x, H)$ be the random variable whose value is this view. (Note that it would make no difference if we included in the view the material written by $B'$ on its private tape, or excluded the strings that $B'$ sends to $A$, since these bits can be efficiently computed from the other bits of the view.) For convenience, we consider each view to be a string from $\{0, 1\}^*$ of length exactly $|x|^c$ for some fixed $c > 0$.

Definition. Let $L \subset \{0, 1\}^*$ be a language and $(A, B)$ a protocol. Let $B'$ be as above. We say that $(A, B)$ is perfectly (statistically) (computationally) zero-knowledge on $L$ for $B'$ if the family of random variables $\mathrm{View}_{A,B'}$ is perfectly (statistically) (computationally) approximable on

$$
L' = \{(x, H) \mid x \in L \text{ and } |H| = |x|^c\}.
$$

We say that $(A, B)$ is perfectly (statistically) (computationally) zero-knowledge on $L$ if it is perfectly (statistically) (computationally) zero-knowledge on $L$ for all probabilistic polynomial time ITM $B'$.

Note that the definition of $(A, B)$ being zero-knowledge (in some manner) for $B'$ only depends on $A$ and not at all on $B$. It might be less misleading to think of $A$ as being zero-knowledge for $B'$. A similar issue arises in the definition of an interactive proof system in § 2.2. Part (2) of this definition depends only on $B$, and not at all on $A$.

Computational zero-knowledge is certainly the most general of the above notions, and we will refer to it simply as zero-knowledge. Zero-knowledge really captures any information, which could not have been obtained efficiently in polynomial time, about members of $L$. That is, if $(A, B)$ is zero-knowledge, it is not possible, in probabilistic polynomial time, to extract any information about members of $L$ by interacting with $A$, not even by "cheating."

Definition. Let $L \subset \{0, 1\}^*$ be a language. We say that $(A, B)$ is a perfectly (statistically) (computationally) zero-knowledge proof system for $L$ if it is an interactive proof system for $L$ and a perfectly (statistically) (computationally) zero-knowledge protocol on $L$.

We will refer to computationally zero-knowledge proof systems (the most general notion of the three) simply as zero-knowledge proof systems. This notion is totally adequate in the real world. That is, if $(A, B)$ is a zero-knowledge proof system for $L$, it is not possible in polynomial time (not even for a "cheating" $B'$) to interact with $A$ and extract anything else besides proofs of membership in $L$.

3.4. Some remarks about the above definitions. First, let us stress that the coin tosses of $B$ are an essential part of the notion of a view in the definition of zero-knowledge for $B$. Consider the language $L$ of all composite integers and the following protocol $(A, B)$. On input an integer $n$, $B$ randomly selects an integer $x$ between 1 and $n$ and relatively prime with $n$. It then sends $A$ the number $a = x^2 \mod n$. $A$ responds by sending $y$, a randomly chosen square root of $a \mod n$. Should the view consist only of the text of the interaction between $A$ and $B$, then the above-mentioned protocol would be perfectly zero-knowledge on $L$. However, we define the view so as to contain also the coin tosses of $B$. Thus, if $(x, a, y)$ is randomly selected in View$_{(A,B)}(n)$, then $\gcd(x + y, n)$ is not 1 or $n$ with probability at least $\frac{1}{2}$. Thus, if factoring is not in probabilistic polynomial time, the above protocol is not zero-knowledge for $B$. (It should be noted, however, that in the definition of zero-knowledge (for *all* $B'$), it is *not* necessary to include the random bits of $B'$ in the view; this is because we have included in the view the messages sent by $B'$, and for every $B'$ there is a $B''$, which is like $B'$ except that it sends its random bits as part of its last message.)

Second, it should be explained why $B'$ sees an additional string $H$. (The need for this was independently discovered by the authors of this paper, by Oren [O], and by Tompa and Woll [TW].) $H$ may be thought about in a number of different ways; $H$ may be some extra information that the verifier (cheating or not) happens to know. For example, a zero-knowledge protocol for graph isomorphism should remain zero-knowledge even if the verifier happens to know colorings for the graphs. It is also possible that the protocol will be inserted in the middle of another protocol, where the verifier has seen some history $H$. There is the fear that this $H$ was generated perhaps by interacting with a machine of unlimited power; we want to rule out the possibility of the verifier then obtaining knowledge by using $H$ when interacting with $A$. It is for a similar reason that the distinguishing circuits in the definition of computational indistinguishability are allowed to be nonuniform. We want to say that two families of random variables can be computationally distinguished if there are circuits that tell them apart, where the circuits may have wired in some information about $x$ or some information obtained from the history of some protocol in which the protocol of interest is immersed. In other words, the view $B'$ obtains on inputs $(x, H)$ should look like the simulated distribution $M(x, H)$.

One test of a definition is that we should be able to prove those facts that intuition dictates *must* be true. One such fact is that the repetition of a zero-knowledge protocol a polynomial number of times is still zero-knowledge. We can prove this with our current definitions, but we cannot prove it if, for example, we do not give $B'$ the extra string $H$. We can also prove that if $B'$ wants to decide a special predicate $P(x)$ for $x \in L$, it does not help $B'$ to engage in a zero-knowledge proof system for $L$. We can prove all the intuitively obvious "facts" we have tried to prove, but only time will tell if these definitions are the right ones, or if they need some further modifications. We feel (and hope) that these definitions capture exactly the intuitive ideas we have tried to capture.

Last, there is the peculiar fact that the machine $M$ simulating the view is allowed to operate in *expected* polynomial time. This appears to be necessary for the zero-knowledge proof system for QNR given in §6. To see why this is necessary in general, consider a pair $(A, B)$, where $B$ (on input of length $n$) sends $n$ random bits $\alpha$ to $A$; if the predicate $P(\alpha)$ holds, then $A$ sends a random $\beta$ of length $n$ such that $P(\beta)$ holds. Imagine that the predicate $P$ is easily computable, but the number of strings of length $n$ for which $P$ holds is small—maybe a fraction $n^{-10}$ or maybe $n^{-20}$—but we do not know exactly which; imagine that the only way we know to find a string for which $P$ holds is to select random strings until one satisfying $P$ is found. The only way we know how to simulate the view of $B$ statistically closely (or even computationally indistinguishably) is to choose a random $\alpha$; if $P(\alpha)$ holds, look through random $n$-bit strings until a $\beta$ is found such that $P(\beta)$ holds. This process is only expected polynomial time.

3.5. Examples of zero-knowledge languages. Trivially, all languages in BPP have perfect zero-knowledge proof systems. (A language is in BPP if there is a probabilistic, polynomial time machine which on each input computes membership in the language with small probability of error.)

The first nontrivial zero-knowledge proof systems (i.e., for recognizing languages not known to be in BPP) are the perfect zero-knowledge proof systems for the quadratic residuosity language QR given in § 5, and the statistically zero-knowledge proof system for QNR given in § 6.

Recently, Goldreich, Micali, and Wigderson have shown in [GMW] that the graph isomorphism language has a perfect zero-knowledge proof system, that the graph nonisomorphism language (though not known to belong to NP) has a statistically zero-knowledge proof system, and that all languages in NP possess computationally zero-knowledge proof systems if secure encryption schemes exist. In [BGGHKMR] it is proved that all languages in IP possess zero-knowledge proof systems.

Results by Boppana, Hastad, and Zachos [BHZ] and Fortnow [Fo] show that if an NP-complete language had a perfect or statistically zero-knowledge proof system, the polynomial time hierarchy would collapse. Thus it may not be surprising that the interactive proof systems in [GMW] for graph coloring were zero-knowledge only in a computational sense. A more immediate reason for their being computationally zero-knowledge is that they make use of probabilistic encryption [GM] (see Example 3). This may tempt us to interpret Fortnow’s result as saying that encryption is crucial in any zero-knowledge proof system for NP-complete languages. (Further discussion on Fortnow’s result can be found in § 7.)

3.6. A study of earlier proposals. Having reached the notion of a zero-knowledge proof system, let us now have a second look at the earlier, Arthur–Merlin type, proof systems of Blum [Bl] and Goldwasser and Micali [GM1] that we have already mentioned in § 2.3.

The Proof System for BL (defined in § 2.3). In his beautiful paper, assuming that integer factorization is computationally hard, Blum proposes a protocol for flipping a coin over the telephone. For “fairly” flipping a coin, Alice and Bob need an integer $n$ whose prime factorization is known to Alice but not to Bob, and has a special property, namely, $n \in \mathrm{BL}$. Alice is sure that the coin flip is fair because she computes $n$ by multiplying two randomly selected primes both congruent to 3 mod 4, and because she trusts that factoring is hard. Bob, after the coin has come up Head or Tail, checks that the flipping was fair by requesting $n$’s factorization from Alice. Thus a different $n$ should be selected for each coin flip. To make coin flipping more efficient, Blum proposed to test that $n \in \mathrm{BL}$, by means of a protocol that does not give away $n$’s factorization in any obvious way. After slightly modifying it, Blum’s protocol can be proved to be perfect zero-knowledge on BL. However, without this modification, it is not clear how much knowledge about $n$’s factorization it releases.

The Proof Systems for GM1 and GM2 (defined in § 2.3). The cryptographic protocols of Goldwasser and Micali use the inefficient version of Blum’s coin-flipping protocols, and thus assume that factoring integers is computationally difficult. Based on this assumption, they showed that their proof systems do not give away the prime factorization of an input $n$. That is, no cheating polynomial time verifier can, after participating in the protocol, compute $n$’s factorization much faster than it could before.

More generally, their same protocols can actually be proved to be computationally zero-knowledge on, respectively, the languages GM1 and GM2. Thus, in particular, their protocols do not even give away whether or not, say, 3 is a quadratic residue mod n.

3.7. Interactive proof systems versus Arthur–Merlin games for zero-knowledge. We are now ready to formally express our belief that interactive proof systems are more appropriate than Arthur–Merlin games for recognizing languages in zero-knowledge.

Conjecture. There exist languages L that have perfect or statistical zero-knowledge proof systems, but do not have any Arthur–Merlin proof system that is perfect or zero-knowledge on L.

4. The quadratic residuosity problem. In this section we describe the necessary number-theoretic background and notation needed for the proofs in §§ 5 and 6.

Let N denote the natural numbers, $x \in \mathbb{N}$ and $\mathbb{Z}_x^* = \{ y \mid 1 \leq y < x, \gcd(x, y) = 1 \}$. We can determine in time polynomial in $|x|$ and $|y|$ whether or not $y \in \mathbb{Z}_x^*$.

We say that $y$ in $\mathbb{Z}_x^*$ is a quadratic residue mod $x$ if there exists a $w$ in $\mathbb{Z}_x^*$ such that $w^2 \equiv y \mod x$. Otherwise, we call $y$ in $\mathbb{Z}_x^*$ a quadratic nonresidue mod $x$.

Fact 1. Let $x \in \mathbb{N}$ and $y \in \mathbb{Z}_x^*$. Then, $y$ is a quadratic residue mod $x$ if and only if it is a quadratic residue mod all of the prime factors of $x$. {#goldwasser-1985-zk-fact-1 .statement tag=0524}

Define the quadratic residuosity predicate to be

$$
Q_x(y) = \begin{cases}
0 & \text{if } y \text{ is a quadratic residue mod } x, \\
1 & \text{otherwise}.
\end{cases}
$$

Then we have the following fact.

Fact 2. Let $x \in \mathbb{N}$ and $y \in \mathbb{Z}_x^*$. Given $y$ and the prime factorization of $x$, $Q_x(y)$ can be computed in time polynomial in $|x|$. {#goldwasser-1985-zk-fact-2 .statement tag=0525}

Let $y \in \mathbb{Z}_x^*$ and the prime factorization of $x$ be $\prod_{i=1}^k p_i^{\alpha_i}$. Then, the Jacobi symbol of $y \mod x$ is defined as

$$
(y/x) = \prod_{i=1}^k (y/p_i)^{\alpha_i},
$$

where $(y/p_i) = 1$ if $y$ is a quadratic residue mod $p_i$, and $-1$ otherwise.

Fact 3. Given $x \in \mathbb{N}$ and $y \in \mathbb{Z}_x^*$, $(y/x)$ can be computed in time polynomial in $|x|$. {#goldwasser-1985-zk-fact-3 .statement tag=0526}

The Jacobi symbol of $y \mod x$ gives some information about whether $y$ is quadratic residue mod $x$ or not. If $(y/x) = -1$, then $y$ is a quadratic nonresidue mod $x$ and $Q_x(y) = 1$. However, when $(y/x) = 1$, no efficient (probabilistic or deterministic polynomial time) solution is known for computing $Q_x(y)$ correctly with probability significantly better than $\frac{1}{2}$. This leads to the formulation of the quadratic residuosity problem.

Definition. We define the quadratic residuosity problem as that of computing $Q_x(y)$ on inputs $x$ and $y$, where $y$ in $Z_x^*$ and $(y/x) = 1$,

The current best algorithm for computing $Q_x(y)$, is to first factor $x$ and then compute $Q_x(y)$. In fact, factoring integers and computing $Q_x$ have been conjectured to be of the same time complexity. The difficulty of the quadratic residuosity problem has been used as a basis for the design of several cryptographic protocols [GM], [LMR], [Bl].

Define the following two languages:

$$
\mathrm{QR} = \{ (x, y) \mid x \in \mathbb{N}, y \in \mathbb{Z}_x^*, \text{and } Q_x(y) = 0 \},
$$

$$
\mathrm{QNR} = \{ (x, y) \mid x \in \mathbb{N}, y \in \mathbb{Z}_x^*, (y/x) = 1, \text{and } Q_x(y) = 1 \},
$$

where $x$ and $y$ are presented in binary.

Clearly, by Facts 1 and 2, both QR and QNR are in the intersection of CO-NP and NP. However, no probabilistic polynomial time algorithm is known that accepts these languages, and thus they are not trivially zero-knowledge. In §5 we show a perfectly zero-knowledge proof system for QR, and in §6 we show a statistically zero-knowledge proof system for QNR. The following facts will be useful in the zero-knowledge proofs of §§ 5 and 6.

Fact 4. Let $x \in \mathbb{N}$. Then, for all $y$ such that $Q_x(y) = 0$, the number of solutions $w \in \mathbb{Z}_x^*$ to $w^2 \equiv y \mod x$ is the same (independent of $y$). {#goldwasser-1985-zk-fact-4 .statement tag=0527}

Fact 5. Let $x \in \mathbb{N}$, $y, z \in \mathbb{Z}_x^*$. Then we have the following: {#goldwasser-1985-zk-fact-5 .statement tag=0528}
(a) If $Q_x(y) = Q_x(z) = 0$, then $Q_x(yz) = 0$.
(b) If $Q_x(y) \neq Q_x(z)$, then $Q_x(yz) = 1$.

Fact 6. Given $x, y$, the Euclidean gcd algorithm allows us to compute in polynomial time whether or not $y \in \mathbb{Z}_x^*$. {#goldwasser-1985-zk-fact-6 .statement tag=0529}

5. Zero-knowledge proofs of quadratic residuosity. Recall that $\mathrm{QR} = \{ (x, y) | y \text{ is a quadratic residue mod } x \}$, where $x$ and $y$ are presented in binary.

We will first informally describe our zero-knowledge interactive proof system for QR, and then describe it with more rigor. Say that $A$ and $B$ are given $(x, y), |x| = m$; then the following is done $m$ times:

• $A$ sends $B$ a random quadratic residue mod $x, u$.
• $B$ sends $A$ a random bit, $bit$.
• If $bit = 0$ then $A$ sends $B$ a random square root of $u \mod x, w$; if $bit = 1$ then $A$ sends $B$ a random square root of $(uy) \mod x, w$.
• $B$ checks that either [bit = 0 and $w^2 \mod x = u$] or [bit = 1 and $w^2 \mod x = (uy) \mod x$].

More formally, we assume, for convenience, that $A$ starts the protocol.

A’s PROTOCOL ON INPUT $(x, y) \in \mathrm{QR}$.
FOR $i = 1$ to $m$
Use random bits to generate $u_i$, a random quadratic residue mod $x$.
SEND $u_i$ to $B$
GET a string $\beta_i$ from $B$; let $bit_i =$ the first bit of $\beta_i$ (or 0 if $\beta_i$ is empty). If $bit_i = 0$, use random bits and generate $w_i$, a random square root of $u_i \mod x$; if $bit_i = 1$, use random bits and generate $w_i$, a random square root of $(u_iy) \mod x$.
SEND $w_i$ to $B$
GET a string from $B$ (this will merely indicate that $B$ wishes to continue the protocol).
END FOR
SEND “terminate” (just a string to finish off the protocol) to $B$.

B’s PROTOCOL ON INPUT $(x, y)$.
See if $x \geq 1$ and $y \in \mathbb{Z}_x^*$; if not, halt.
FOR $i = 1$ to $m$
GET $u_i$ from $A$. See if $u_i \in \mathbb{Z}_x^*$; if not, halt.
Generate a random $bit_i$.
SEND $bit_i$ to $A$.
GET $w_i$ from $A$. See if $w_i \in \mathbb{Z}_x^*$ and either [$bit_i = 0$ and $w_i^2 \mod x = u_i$] or [$bit_i = 1$ and $w_i^2 \mod x = (u_iy) \mod x$]; if not, halt.
SEND “okay” (just a string to continue the protocol) to $A$.
END FOR
GET any string from $A$, and halt accepting.

This is clearly an interactive protocol.

CLAIM 1. *The above* $(A, B)$ *protocol is an interactive proof system for QR*.

*Proof.* Say that $B$ is interacting with an arbitrary $A'$. Say that $x \geq 1$, $y \in Z_x^*$, and $y$ is *not* a quadratic residue mod $x$. For each $u_i$ that $B$ receives from $A'$ it cannot be the case that *both* $u_i$ and $(u_i y)$ have square roots mod $x$. Since $A'$ does not see any *bit* in advance, there is at most a $\frac{1}{2}$ probability that $B$ will "okay" the $i$th pass. Hence, the probability that $B$ will say "convinced" is at most $1/2^m$.

We will now show that the protocol is zero-knowledge for QR.

THEOREM 1. *The above* $(A, B)$ *protocol is a perfectly zero-knowledge proof system for* QR.

*Proof.* Let $B'$ be an arbitrary polynomial time ITM that interacts with $A$. Let $(x, y) \in \mathrm{QR}$ be the common input to the pair $(A, B')$, $|x| = m$, and let $H$ be the extra input to $B'$. For convenience we consider the view $\mathrm{View}_{A,B'}((x, y), H)$ to consist of the random variables

$$
R, U_1, \mathrm{BIT}_1, W_1, U_2, \mathrm{BIT}_2, W_2, \cdots, U_m, \mathrm{BIT}_m, W_m,
$$

where $R$ is the string of random bits generated by $B'$, $U_i$ takes on the value $u_i$, $\mathrm{BIT}_i$ takes on the $i$th message of $B'$, etc.

One way to describe the distribution of the view is as follows: $R$ is assigned a random bit string $r$ (of the appropriate length). Say that $R, U_1, \mathrm{BIT}_1, W_1, \cdots, U_i, \mathrm{BIT}_i, W_i$ is the random variable $V_i$. Assume that for some $i, 1 \leq i < m$, $V_i$ has been given the value $v_i$; we will describe the experiment for giving values to $U_{i+1}, \mathrm{BIT}_{i+1}, W_{i+1}$.
