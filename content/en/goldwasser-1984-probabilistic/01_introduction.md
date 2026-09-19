---
paper: goldwasser-1984-probabilistic
title: Probabilistic Encryption
authors:
  - Shafi Goldwasser
  - Silvio Micali
year: 1984
venue: Journal of Computer and System Sciences
field: security
section: "1"
section_title: Introduction
tag: 048F
kind: section
lang: en
source: https://people.csail.mit.edu/silvio/Selected%20Scientific%20Papers/Encryption/Probabilistic_Encryption.pdf
pdf_sha256: b3d2f75d09da80c0bc3b39e3001ea3dd782b42af46df9c5bde0741f2dab7aa4a
pdf_pages: 1-4
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: b1969dca7ac216740e7cc85470b4bcab0f36ad725da93a7189461c209ce708d9
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

This paper proposes an encryption scheme that possesses the following property:

Whatever is efficiently computable about the cleartext given the cyphertext, is also efficiently computable without the cyphertext.

The security of our encryption scheme is based on complexity theory. Thus, when we say that it is "impossible" for an adversary to compute any information about the cleartext from the cyphertext we mean that it is not computationally feasible.

The relatively young field of complexity theory has not yet been able to prove a nonlinear lower bound for even one natural NP-complete problem. At the same time, despite the enormous mathematical effort, some problems in number theory have for centuries refused any "domestication." Thus, for concretely implementing our scheme, we assume the intractability of some problems in number theory such as factoring or deciding quadratic residuosity with respect to composite moduli. In this context, proving that a problem is hard means to prove it equivalent to one of the above mentioned problems. In other words, any threat to the security of the concrete implementation of our encryption scheme will result in an efficient algorithm for deciding quadratic residuosity modulo composite integers.

* This research was done when both authors were students at the University of California at Berkeley and supported in part by NSF Grant MCS 82-04506. The preparation of this manuscript was done when the first author was at the Laboratory of Computer Science at MIT and supported by a Bantrell fellowship and an IBM faculty development award, and the second author was at the Computer Science Department at the University of Toronto.

### 1.1. Deterministic Encryption: The Trapdoor Function Model {#goldwasser-1984-probabilistic-s1-1 .section tag=0490}

Our encryption scheme benefits from the ideas of Diffie and Hellman [9], Rivest, Shamir, and Adleman [21], and Rabin [20].

Diffie and Hellman [9] introduced the idea of a public key cryptosystem, which is based on the intractability of some underlying computational problem. Intuitively, the idea is to find an encryption function $E$ which is easy to compute but difficult to invert unless some secret information, the trapdoor, is known. Such a function is called a trapdoor function. To encrypt a message $m$, anyone simply evaluates $E(m)$, but only those who know the trapdoor information can compute $m$ from $E(m)$.

The two implementations of a trapdoor function most relevant and inspiring for this paper are the RSA function [21], due to Rivest, Shamir, and Adleman, and its particularization suggested by Rabin [20].

### 1.2. Basic Objections to the Trapdoor Function Model {#goldwasser-1984-probabilistic-s1-2 .section tag=0491}

We point out two basic weaknesses of this approach:

(1) *The fact that $f$ is a trapdoor function does not rule out the possibility of computing $x$ from $f(x)$ when $x$ is of a special form.* Usually messages do not consist of numbers chosen at random but possess more structure. Such structural information may help in decoding. For example, a function $f$, which is hard to invert on a generic input, could conceivably be easy to invert on the ASCII representations of English sentences.

(2) *The fact that $f$ is a trapdoor function does not rule out the possibility of easily computing some partial information about $x$ (even every other bit of $x$) from $f(x)$.* Encrypting messages in a way that ensures the secrecy of all partial information is an important goal in cryptography. Assume we want to use encryption to play card games over the telephone. If the suit or color of a card could be compromised the whole game should be invalid. Indeed Lipton [17] has pointed out that one bit of information about cards to remain hidden can be easily computed in the SRA implementation of Mental Poker [22].

Though no one knows how to break the RSA or the Rabin scheme, in none of these schemes is it *proved* that decoding is hard without any assumptions made on the message space. Rabin shows that, in this scheme, decoding is hard for an adversary if the set of possible messages has some density property. We discuss this further in Section 2.

### 1.3. Probabilistic Encryption: The New Model {#goldwasser-1984-probabilistic-s1-3 .section tag=0492}

In this paper we switch from a deterministic framework to a probabilistic framework. This enables us to deal with the problems that arose with the trapdoor function model, without imposing any probability structure on the messages we would like to send.

We replace the notion of a trapdoor function with the notion of an *unapproximable trapdoor predicate*. Briefly, the predicate $B$ is trapdoor and unapproximable if anyone can *select* an $x$ such that $B(x) = 0$ or $y$ such that $B(y) = 1$, but only those who know the trapdoor information can, given $z$, *compute* the value of $B(z)$. When the trapdoor information is unknown, an adversary with polynomially bounded computational resources can not decide the value of $B(z)$ better than guessing at random (see Section 3 for formal definition).

We replace deterministic block encryption by probabilistic encryption of single bits, where there are many different encodings of a “1” and many different encodings of a “0.” To encrypt each message we make use of a fair coin. Thus the encoding of each message will depend on the message plus the result of a sequence of coin tosses. More specifically, a binary message will be encrypted bit-by-bit as follows: a “0” is encoded by randomly selecting an $x$ such that $B(x) = 0$ and a “1” is encoded by randomly selecting an $x$ such that $B(x) = 1$. Consequently, there are many possible encodings for each message. However, messages are always uniquely decodable.

Two properties of the new model are:

(1) *Decoding is easy for the legal receiver of a message, who knows the trapdoor information, but provably hard for an adversary.* Therefore the spirit of a trapdoor function is maintained. In addition, in our scheme, we do not impose any restrictions on the message space. The security of the scheme is proved for messages belonging to any message space with any probability distribution.

(2) *No information about an encrypted message can be obtained by an adversary.*

Let $g : M \to V$ be a nonconstant function $m$. Assume that the message space $M$ has some probability distribution. Accordingly, let $p_v = \operatorname{prob}(g(m) = v \mid m \in M)$ for each $v \in V$, and let $\bar{v} \in V$ be such that $p_{\bar{v}} = \max_{v \in V} p_v$. Then, without any special ability, an adversary given the cyphertext, can always guess the value of $g$ over the cleartext and be correct with probability $p_{\bar{v}}$. We prove that for a probabilistic encryption scheme, an adversary, given the cyphertext, cannot guess the value of $g$ over the cleartext with probability better than $p_{\bar{v}}$. Note that $g$ needs not be polynomially computable, or even recursive. Thus, our encryption model passes a polynomially bounded version of Shannon’s *perfect secrecy* definition; see Subsection 7.3.

This property enabled Goldwasser and Micali [11] to device a scheme for Mental Poker for which, under the Quadratic Residuosity Assumption, no partial information about cards that should remain hidden can be easily computed.

### 1.4. *Concrete Implementation of the New Model* {#goldwasser-1984-probabilistic-s1-4 .section tag=0493}

We introduce Quadratic Residuosity modulo composite integers whose factorization is unknown (see Section 6 for precise definition), as the first example of an unapproximable trapdoor predicate. Thus we introduce a new probabilistic public key cryptosystem that is secure in a very strong probabilistic sense if and only if deciding quadratic residuosity with composite moduli is hard (see Section 4). The security offered by this Public Key Cryptosystems extends to *all partial information* about encrypted messages, to *all possible message spaces* and to *all possible probability distributions* for the message space (see Section 5 for formal definition of security).

Another example of such predicates, has appeared in a Goldwasser, Micali, and Tong [12] and in Goldwasser [13]. The predicate they propose is unapproximable if and only if factoring composite numbers is hard. Using the construction of Section 4, we can build a public key cryptosystem based on the predicate they propose. Again, any threat to the security of this last cryptosystem, will result in an efficient factoring algorithm.

In [26], Yao shows that unapproximable trapdoor predicates exist if one-to-one trapdoor functions exist.

### 1.5. *Related Work* {#goldwasser-1984-probabilistic-s1-5 .section tag=07DA}

Blum and Micali in [5] showed the first example of an unapproximable predicate which is not trapdoor. Their predicate is unapproximable if and only if the discrete logarithm problem is hard.

The quadratic residuosity predicate is not only an example of an unapproximable trapdoor predicate, but possesses other properties which make it particularly attractive for protocol design. It has been widely used since we first proposed it in [10]. The first protocol that uses this predicate was suggested by Goldwasser and Micali in [11]. They design a protocol for two players to play mental poker over the telephone, so that no player can obtain any partial information about cards not in his hand. Other works in which this predicate has proved useful are: Blum, Blum, and Shub’s implementation [4] of a cryptographically strong pseudo random bit generator [5], Brassard’s [7] implementation of authentication tags, Luby, Micali, and Rackoff’s [19] method for simultaneously exchanging a secret bit, and Vazirani and Vazirani’s [25] implementation of one bit disclosures.
