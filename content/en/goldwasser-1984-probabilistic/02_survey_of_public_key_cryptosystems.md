---
paper: goldwasser-1984-probabilistic
title: Probabilistic Encryption
authors:
  - Shafi Goldwasser
  - Silvio Micali
year: 1984
venue: Journal of Computer and System Sciences
field: security
section: "2"
section_title: '*Survey of Public Key Cryptosystems Based on Trapdoor Functions*'
tag: 07DB
kind: section
lang: en
source: https://people.csail.mit.edu/silvio/Selected%20Scientific%20Papers/Encryption/Probabilistic_Encryption.pdf
pdf_sha256: b3d2f75d09da80c0bc3b39e3001ea3dd782b42af46df9c5bde0741f2dab7aa4a
pdf_pages: 4-8
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: a30fab554438970f9df9d9b6c023389a2b638bc82da124aa78401f95a4c5a900
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

All the number theoretic notation used in this section will be defined in Section 3.

### 2.1. *What Is a Public Key Cryptosystem?* {#goldwasser-1984-probabilistic-s2-1 .section tag=07DC}

The concept of a Public Key Cryptosystem was introduced by Diffie and Hellman in their ingenious paper [9]. Let $M$ be a finite message space, let $\{A, B, ...\}$ be users, and let $m \in M$ denote a message. Let $E_A : M \to M$ be $A$'s encryption function, which is ideally bijective, and $D_A$ be $A$'s decryption function such that $D_A(E_A(m)) = m$ for all $m \in M$. In a Public Key Cryptosystem $E_A$ is placed in a public file, and user $A$ keeps $D_A$ private. $D_A$ should be difficult to compute knowing only $E_A$. To send message $m$ to $A, B$ takes $E_A$ from the public file, computes $E_A(m)$ and sends this message to $A$. $A$ easily computes $D_A(E_A(m))$ to obtain $m$.

### 2.2. *The RSA Scheme and the Rabin Scheme* {#goldwasser-1984-probabilistic-s2-2 .section tag=07DD}

Two implementations of such encryption functions $E_A$ are the RSA function [21] of Rivest *et al.* and the Rabin function [20].

The key idea in both the RSA scheme and the Rabin scheme$^1$ consists in the selection of an appropriate number theoretic trapdoor function. In the RSA scheme, user $A$ selects $n$, the product of two large distinct primes $p_1$ and $p_2$, and a number $s$ such that $s$ and $\varphi(n)$ are relatively prime, where $\varphi$ is the Euler totient function. $A$ puts $n$ and $s$ in a public file and keeps the factorization of $n$ private. Let $Z_n^* = \{ x \in N : 1 \leq x \leq n-1 \text{ and } x \text{ and } n \text{ are relatively prime} \}$. For every message $m \in Z_n^*$, $E_A(m) = m^s \mod n$. Clearly, the ability to take $s$th roots mod $n$ implies the ability to decode. $A$, who knows the factorization of $n$, can easily take $s$th roots mod $n$. No efficient way to take $s$th roots mod $n$ is known when the factorization of $n$ is unknown.

Rabin suggested to modify the RSA scheme by choosing $s = 2$. Thus, for all users $A$, $E_A(x) = x^2 \mod n$. Notice that $E_A$ is a 4–1 function because our $n$ is the product of two primes. In fact, every quadratic residue mod $n$, i.e., every $q$ such that $q \equiv x^2 \mod n$ for some $x \in Z_n^*$, has four square roots mod $n$: $\pm x \mod n$ and $\pm y \mod n$. As $A$ knows the factorization of $n$, upon receiving the encrypted message $m^2 \mod n$, she could easily compute its four square roots and get the message $m$. ($A$ may compute square roots mod $n$ by first computing square roots mod $p_1$ and $p_2$, and then by combining them via the Chinese Remainder Theorem.) The following heuristics may be suggested for eliminating ambiguity in decoding: for sending a message $m$, send $m^2 \mod n$ together with the last 20 bits of $m$. Such extra information cannot effectively help in decoding: one could always guess the last 20 digits of $m$. (To avoid publicizing the last 20 digits of $m$, just select a 20-bit random integer $r$ and send $(m2^{20} + r)^2 \mod n$ together with $r$.)

The following theorem shows how hard it is to invert Rabin’s function $x^2 \mod n$.

**THEOREM** (Rabin). *If for a $1/\log n$ fraction of the quadratic residues $q \mod n$ one could find one square root of $q$, then one could factor $n$ in random polynomial time.*

The theorem follows from Lemma 1 which we state without proof.

**LEMMA** 1. *Given $x, y \in Z_n^*$ such that $x^2 \equiv y^2 \mod n$ and $x \neq \pm y \mod n$, there is a polynomial time algorithm to factor $n$. (In fact the greatest common divisor of $n$ and $x \pm y$ is a factor of $n$.)*

*Informal Proof of Rabin’s Theorem.* Assume that we have a magic box MB such

$^1$ We will state a simplified version of his method.

that given $q$, a quadratic residue mod $n$, for a fraction $1/\log n$ of the $q$'s it outputs one square root of $q \mod n$. Then we could factor $n$ by iterating the following step:

Pick $i$ at random in $Z_n^*$ and compute $q = i^2 \mod n$. Feed the magic box MB with $q$. If $M$ outputs a square root of $q$ different from $i$ or $-i \mod n$, then (by Lemma 1) factor $n$.

The expected number of iterations is low, as at each step, we have a $1/2 \log n$ chance of factoring $n$.

### 2.3. Objections to Cryptosystems Based on Trapdoor Functions {#goldwasser-1984-probabilistic-s2-3 .section tag=07DE}

The following problems may arise in the RSA and Rabin schemes and, more generally, in any other Public Key Cryptosystem based on trapdoor functions:

(1) The fact that $f$ is a trapdoor function does not rule out the possibility of computing $x$ from $f(x)$ when $x$ is of special form.

(2) The fact that $f$ is trapdoor function does not rule out the possibility of easily computing some partial information about $x$ from $f(x)$.

### 2.3.1. Discussion of Objection 1 {#goldwasser-1984-probabilistic-s2-3-1 .section tag=07DF}

One may argue that Rabin's Public Key Cryptosystem is as hard to break as factoring in the following way: whoever can get messages $m$ from their encryptions $m^2 \mod n$ for a fraction $1/\log n$ of the time, is actually realizing the magic box of Rabin's theorem and thus could efficiently factor $n$.

We would like to point out the following fact.

Claim. If $M$, the space of messages, is "sparse" in $Z_n^*$, the ability to decode for a fraction $1/\log n$ of all messages does not yield a random polynomial time algorithm for factoring.

By "sparse" we mean that for a randomly chosen $x \in Z_n^*$, the probability that $x$ is a message is virtually 0.

Let $f(x) = x^2 \mod n$. Assume that we are able to invert the function $f$ only on $f(M)$. Then, we would have a magic box MB which, on input $m^2 \mod n$, where $m \in M$, outputs $m$; and on input $q \notin \{ m^2 \mod n \mid m \in M \}$, outputs a correct answer, for a negligible portion of the $q$'s. Using such a magic box we could decode, but not factor $n$ efficiently. Let us look at the above informal proof of Rabin's theorem, using this MB. If we pick $m \in M$ and input $m^2 \mod n$ to MB, then we get $m$ back and cannot factor. If we pick $i \notin M$ and input $i^2 \mod n$ to MB, then the probability that any of the square roots of $i^2 \mod n$, which are different from $i$, belong to $M$ is practically 0 and we get no answer.

We conclude that for Rabin's function one can decode if and only if one can factor, provided the legal messages are dense in $Z_n^*$ (e.g., $M = Z_n^*$ and all messages are equally probable).

### 2.3.2. Discussion of Objection 2 {#goldwasser-1984-probabilistic-s2-3-2 .section tag=07E0}

One desirable property for an encryption algorithm is that an adversary should not be able to obtain any partial information about the cleartext from the cyphertext.

For example, let $f$ be a hashing function or a nonconstant predicate defined on the message space $M$. Let $m \in M$. If, given the encryption of $m$, an adversary can efficiently compute $f(m)$, then we say that *information* about $m$ can be obtained from the encryption of $m$.

Note that if the encryption algorithm, $E$, is a trapdoor function, then partial information about the cleartext *cannot be hidden*. In fact, the following predicate $B$, defined on the cleartext, is easy to evaluate from the cyphertext: $B(x) =$ true if and only if $E(x)$ is even. We can avoid such problems using probabilistic encryption.

Let us now discuss a crucial question, raised by Brassard [6], closely related to the security of partial information: how to send a single bit securely in a Public Key Cryptosystem.

2.3.3. Attempts to Send a Single Bit Securely in Public Key Cryptosystems Based on Trapdoor Functions

Suppose that user $B$ wants to send a single bit message to user $A$ in great secrecy. The bit is equally likely to be a 0 or a 1. $B$ wants no adversary to be able to guess correctly his message 51% of the time. $B$ knows that user's $A$'s public encryption function $E_A$ is hard to invert and tries to make use of this fact in the following way.

IDEA 1. All users in the system agree on an integer $i$. User $B$ selects $r \in M$ at random, except for the $i$th bit of $r$, which will be his message. $B$ sends $E_A(r)$ to $A$.
$A$ can decode and thus get the desired bit. But what can an adversary do?

Danger. Let $y = E_A(x)$, where $E_A$ is a one way function. Then, given $y$, it could be difficult to compute $x$ but not a specific bit of $x$.

EXAMPLE. Let $p$ be a large prime such that $p - 1$ has at least one large prime factor. Let $g$ be a generator for $Z_p^*$. Then $y \equiv g^x \mod p$ is considered to be a one-way function. But, even though it is difficult to compute $x$ from $g^x \mod p$ (the index finding problem), it is easy to get the last bit of $x$. In fact, $x$ ends in 0 if and only if $y$ is a quadratic residue mod $p$, and there are probabilistic polynomial time algorithms for testing whether numbers are quadratic residues modulo primes $p$ (see Subsection 3.1).

The following idea was suggested by Donald Johnson.

IDEA 2. $B$ constructs a 100-bit integer $x$ as follows: he selects $8 \leq i \leq 100$ at random, and sets the $i$th bit of $x$ to the bit he wants to communicate. The remaining 92 bits of $x$ are chosen at random, except for the first 7 bits of $x$, which specify location $i$. $B$ sends $E_A(x)$ to $A$.

Danger. $E_A$ can be a trapdoor function and yet one could, given $E_A(x)$, easily compute the first 7 bits of $x$ and one of the last 93 bits of $x$. If this is the case, one could correctly compute $B$'s message $x$ with probability $\frac{1}{92} + \frac{1}{2} \cdot \frac{91}{92}$.

Summarizing, there are many ways in which a single bit could be "embedded" in a binary number $x$. Taking the "exclusive or" of all the digits of $x$ is just one more example. However, given $y = E_A(x)$, being able to discover single bits embedded in $x$ does not contradict the fact that it is hard to compute $x$. Then, what is a secure way to send a single bit? Unapproximable trapdoor predicates will provide a solution to this problem.
