---
paper: goldwasser-1984-probabilistic
title: Probabilistic Encryption
authors:
  - Shafi Goldwasser
  - Silvio Micali
year: 1984
venue: Journal of Computer and System Sciences
field: security
section: "6"
section_title: THE QUADRATIC RESIDUOSITY PROBLEM (QRP)
tag: 07EE
kind: section
lang: en
source: https://people.csail.mit.edu/silvio/Selected%20Scientific%20Papers/Encryption/Probabilistic_Encryption.pdf
pdf_sha256: b3d2f75d09da80c0bc3b39e3001ea3dd782b42af46df9c5bde0741f2dab7aa4a
pdf_pages: 22-28
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: f55f10071cdf78e27edd31e6f5eae690a55f5d067930af395e46a2f6e2264afb
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

We introduce a new trapdoor number theoretic predicate based on the quadratic residuosity assumption.

Let $x$ and $y$ be integers. The symbol $(x, y)$ will denote the greatest common divisor of $x$ and $n$. The symbol $\mathrm{Prob}(X)$ will denote the probability of the event $X$. Let $N$ denote the set of positive integers and $n \in N$. Let $Z_n^* = \{ x \mid 1 \leq x \leq n - 1 \text{ and } (x, n) = 1 \}$.

### 6.1. Background and Notation {#goldwasser-1984-probabilistic-s6-1 .section tag=07EF}

Given $q \in Z_n^*$, is $q \equiv x^2 \mod n$ solvable? If $n$ is prime, then the answer to this question is easily computed [16]: yes if $q^{(n-1)/2} \mod n = 1$ and no if $q^{(n-1)/2} \mod n = -1$. If a solution exists, $q$ is said to be a quadratic residue mod $n$. Otherwise $q$ is said to be a quadratic nonresidue mod $n$. In this section, $p_1$ and $p_2$ will be odd, distinct primes and $n = p_1 p_2$. Then, $q \equiv x^2 \mod n$ is solvable if and only if both $q \equiv x^2 \mod p_1$ and $q \equiv x^2 \mod p_2$ are solvable. Thus, if the factorization of $n$ is known, the solvability of $q \equiv x^2 \mod n$ is easily decidable.

Lemma 1. Given the prime factorization of a composite integer $n$, deciding whether $q \in Z_n^*$, is a quadratic residue mod $n$ can be done in $O(|n|^3)$ time. {#goldwasser-1984-probabilistic-lem-1 .statement tag=07F0}

Some information about deciding whether a number is a quadratic residue mod $n$, when the factorization of $n$ is unknown, can be obtained from the Jacobi symbol. Let $p$ be an odd prime and $q \in Z_p^*$, then the Jacobi symbol $(q/p)$ equals 1 if $q$ is a quadratic residue mod $p$ and $-1$ otherwise. The Jacobi symbol $(q/n)$, is defined as $(q/n) = (q/p_1)(q/p_2)$. Despite the fact that the Jacobi symbol $(q/n)$ is defined through the factorization of $n$, $(q/n)$ is computable in polynomial time even when the factorization of $n$ is not known!

It is easy to see, from the above definitions that if $(q/n) = -1$ then $q$ must be a quadratic nonresidue mod $n$. In fact, $q$ must be a quadratic nonresidue either mod $p_1$ or mod $p_2$. However, if $(q/n) = +1$, then either $q$ is a quadratic residue mod $n$ or $q$ is a quadratic nonresidue modulo both the prime factors of $n$.

In this paper we are interested in those elements of $Z_n^*$ whose Jacobi symbol is $+1$.
Thus we introduce the set,

$$
Z_n^1 = \{ x \mid x \in Z_n^* \text{ and } (x/n) = 1 \}.
$$

Let us count the number of elements of $Z_n^{+1}$. See [16] for proofs.

Fact 1. Let $p$ be an odd prime. Then $Z_p^*$ is a cyclic group. {#goldwasser-1984-probabilistic-fact-1 .statement tag=07F1}

Fact 2. Let $g$ be a generator for $Z_p^*$, then $g^s \mod p$ is a quadratic residue if and only if $s$ is even. {#goldwasser-1984-probabilistic-fact-2 .statement tag=07F2}

COROLLARY 3. Half of the numbers in $Z_p^*$ are quadratic residues and half are quadratic nonresidues.

FACT 4. Let $n = p_1 p_2$ ($p_1$ and $p_2$ are distinct odd primes). Then half of the numbers in $Z_n^*$ have Jacobi symbol equal to $-1$ and thus are quadratic nonresidues. The Jacobi symbol of the rest of the numbers is 1. Exactly half of these latter ones are quadratic residues mod $n$.

### 6.2. The Quadratic Residuosity Assumption {#goldwasser-1984-probabilistic-s6-2 .section tag=07F3}

Let $n$ be a composite integer, and $q$ an element of $Z_n^{+1}$. The Quadratic Residuosity Problem with parameters $q$ and $n$ is to decide whether $q$ is a quadratic residue mod $n$. If the factorization of $n$ is not known, then there is no known efficient procedure for solving the quadratic residuosity problem with parameters $n$ and $q$ in $Z_n^{+1}$. This decision problem is a well-known hard problem in Number Theory. It is one of the main four algorithmic problems discussed by Gauss [8] in his "Disquisitiones Arithmeticae" (1801). A polynomial solution for it would imply a polynomial solution to other open problems in Number Theory. One example is deciding whether a composite integer $n$, is the product of 2 or 3 primes (see open problems 9 and 15 in Adleman [2]).

In order to formally state the intractability assumption of the Quadratic Residuosity Problem, let us introduce the predicate $Q_n$ and the set of hard composite numbers $H_k$. For all $x \in Z_n^1$; the predicate $Q_n$ is defined as:

$$
Q_n(x) = 1 \quad \text{if } x \text{ is a quadratic residue mod } n,
$$

$$
= 0 \quad \text{if } x \text{ is a quadratic nonresidue mod } n.
$$

$H_k$ will denote the set of hard composite integers: Let $p_1$ and $p_2$ denote primes.

$$
H_k = \{ n \mid n = p_1 p_2, \text{where } |p_1| = |p_2| = k \}.
$$

The elements of $H_k$ constitute the hardest inputs for any known factoring algorithm.

Quadratic Residuosity Assumption (QRA)

Let $P_1$ be a fixed polynomials. For each integer $k$, let $C$ be a circuit with two $2k$-bit inputs and one Boolean output. Let $C_k$ be the minimum size of circuits $C$ such that for a fraction $1/P_1(k)$ of the $n \in H_k$, $C[n, x] = Q_n(x)$ for all $x \in Z_n^{+1}$. Then, for all polynomials $Q$, for all sufficiently large $k$: $C_k > Q(k)$.

Next, we show that under the QRA, computing $Q_n(x)$ is hard not only for some special $x \in Z_n^1$, but is hard on the average.

### 6.3. *A Number Theoretic Result* {#goldwasser-1984-probabilistic-s6-3 .section tag=07F4}

We recall that a circuit $C[\cdot]$ *ε*-approximates the predicate $B : \Omega \to \{0, 1\}$ if $C[x] = B[x]$ for at least a fraction $\frac{1}{2} + \varepsilon$ of the $x \in \Omega$.

Let us recall the weak law of large numbers:

*Weak Law of Large Numbers*

Let $y_1, y_2, ..., y_r$ be $r$ independent 0-1 variables such that $y_i = 1$ with probability $p$, and $S_r = \sum_{i=1}^r y_i$, then for real numbers $\psi, \delta > 0, r \geq 1/4\delta\psi^2$ implies that $\operatorname{Prob}(|(S_r/r) - p| > \psi) < \delta$. Notice that $r$ is bounded by a polynomial in $\psi^{-1}$ and $\delta^{-1}$.

*Remarks About Theorem* 1. Theorem 1 shows that deciding Quadratic Residuosity mod $n$ is either “everywhere hard” or “everywhere easy.” The main idea of this theorem is “how to collect a stochastic advantage,” namely, how to turn an oracle that answers most questions correctly, but you do not know which ones, into an oracle that answer *every* question correctly with arbitrarily high probability.

**Theorem** 1. *Fix polynomial* $P_1$ *and* $P_2$, *and let* $O[\cdot, \cdot] : N \times N \to \{0, 1\}$ *be an oracle. Let* $S$ *be the set of hard integers* $n$ *such that* $O[\cdot, n]$ *(1/P_1(|n|))-approximates Q_n*. *Then there is a probabilistic poly(|n|) algorithm with oracle* $O$ *that, for any* $n \in S$ *and any* $x \in Z_n^1$, *with probability greater than* $1 - (1/P_2(|n|))$ *correctly decides whether* $x$ *is a quadratic residue mod* $n$.

*Proof.* Let $n \in S$. Take $Z_n^1$ with the uniform probability distribution. For notational simplicity let $\varepsilon = 1/P_1(|n|)$ and $\delta = 1/P_2(|n|)$. Then, $\operatorname{Prob}(O[q, n] = Q_n(q) | q \in Z_n^1) > \frac{1}{2} + \varepsilon$. Let, $\alpha = \operatorname{Prob}(O[q, n] = 1 | Q_n(q) = 1)$, and $\beta = \operatorname{Prob}(O[q, n] = 1 | Q_n(q) = 0)$.

The $\operatorname{Prob}(O[q, n] = Q_n(q) | q \in Z_n^1) = \frac{1}{2}\alpha + \frac{1}{2}(1 - \beta) > \frac{1}{2} + \varepsilon$. Therefore, $\alpha - \beta \geq 2\varepsilon$, but $\alpha$ can be much less than $\frac{1}{2} + \varepsilon$. We first need to get a good estimate for $\alpha$.

Construct a sample of $r$ quadratic residues chosen at random in $Z_n^*$ (the value of $r$ will be defined later on). This can be easily done by picking $s_1, ..., s_r$ at random in $Z_n^*$ and squaring them modulo $n$. Initialize a counter $C$ to 0.

For $i = 1$ to $r$, ask the oracle for the value $O[s_i^2 \mod n, n]$. Increment $C$ each time that the oracle answers 1 (i.e., “quadratic residue”).

Let $\psi = \varepsilon/2$. If $r$ is chosen to be suitably large, $r = 1/\delta\psi^2$, the weak law of large numbers assures that $C/r$ is a good ($\varepsilon/2$)-estimate for $\alpha$:

$$
\operatorname{Prob} \left( \left| \alpha - \frac{C}{r} \right| \leq \frac{\varepsilon}{2} \right) > 1 - \frac{\delta}{2},
$$

i.e., $C/r$ is a good approximation to how well the oracle “guesses” $Q_n$ if the inputs are only quadratic residues.

We are now ready to describe a procedure for determining the quadratic residuosity of any element in $Z_n^1$. Let $q$ be an element of $Z_n^1$ that we want to test for quadratic residuosity. Randomly generate $r$ quadratic residues, $x_1, ..., x_r$, in $Z_n^1$ and compute $y_i \equiv qx_i \mod n$ for $i = 1, ..., r$. Notice that

(1) if $q$ is a quadratic residue, then the $y_i$'s are random quadratic residues,
(2) if $q$ is a quadratic nonresidue in $Z_n^1$, then the $y_i$'s are random quadratic nonresidues.

Let us postpone the proof of (1) and (2) and assume, for the time being, that they are true. Initialize a counter $\bar{C}$ to 0. For $i = 1$ to $k$ call the oracle to get the value $O[y_i, n]$. Increment $\bar{C}$ every time that the oracle answers 1. Output "q is a quadratic residue mod n" if $|(C/r) - (\bar{C}/r)| < \varepsilon$ and "q is a quadratic nonresidue mod n" otherwise.

Since the

$$
\operatorname{Prob}\left(\left|\frac{\bar{C}}{r} - \alpha\right| < \frac{\varepsilon}{2} \mid q \text{ is a quadratic residue}\right) > 1 - \frac{\delta}{2}
$$

and

$$
\operatorname{Prob}\left(\left|\frac{\bar{C}}{r} - \beta\right| < \frac{\varepsilon}{2} \mid q \text{ is a quadratic nonresidue}\right) > 1 - \frac{\delta}{2},
$$

then

$$
\operatorname{Prob}(\text{answering } q \text{ is a quadratic nonresidue} \mid q \text{ is a quadratic nonresidue})
$$

$$
= \operatorname{Prob}\left(\left|\frac{C}{r} - \frac{\bar{C}}{r}\right| < \varepsilon \mid q \text{ is a quadratic nonresidue}\right)
$$

$$
> \operatorname{Prob}\left(\left|\frac{C}{r} - \alpha\right| < \frac{\varepsilon}{2}\right) \times \operatorname{Prob}\left(\left|\frac{\bar{C}}{r} - \beta\right| < \frac{\varepsilon}{2}\right) > \left(1 - \frac{\delta}{2}\right)^2 > (1 - \delta).
$$

Thus the quadratic residuosity of any $q \in Z_n^1$ is decided correctly with probability greater than $1 - \delta$.

We still need to prove (1) and (2). To prove (1) it will suffice to prove that, given any quadratic residue $q$, any other quadratic residue $y$ in $Z_n^*$ can be uniquely written as $y = qx \mod n$, where $x$ is also a quadratic residue mod $n$. Let $g_1$ and $g_2$ be generators for, respectively, $Z_{p_1}^*$ and $Z_{p_2}^*$. Let $a$ and $b$ be such that $a \equiv g_1 \mod p_1$, $a \equiv 1 \mod p_2$, and $b \equiv 1 \mod p_1$ and $b \equiv g_2 \mod p_2$. By the Chinese Remainder Theorem such $a$ and $b$ exist. Then, any element of $Z_n^*$ can be written uniquely as $a^i b^j \mod n$, where $1 \leq i \leq p_1 - 1$ and $1 \leq j \leq p_2 - 1$. Moreover, $q$ is a quadratic residue mod $n$ if and only if it can be written as $q = a^{2i} b^{2j} \mod n$, where $1 \leq 2i \leq p_1 - 1$ and $1 \leq 2j \leq p_2 - 1$. Thus if $y = a^{2s} b^{2t} \mod n$ is any quadratic residue there exists a unique $x$ quadratic residue mod $n$, $x = a^{2(s-i)} b^{2(t-j)}$, such that $y = qx \mod n$. This proves (1); (2) is proved in a similar way.

COROLLARY 1. Fix polynomials $P_1$ and $P_2$. Let $k \in N$. Let $C_k$ be the size of the minimum size circuit $C$ that $(1/P_2(k))$-approximates $Q_n$ for a fraction $1/P_1(k)$ of the $n$'s in $H_k$. Under the QRA, for all polynomials $Q$, for all sufficiently large $k$: $C_k > Q(k)$.

Proof. Assume, for contradiction, that there exist polynomials $P_1, P_2$, and $Q$ and an infinite $\bar{N} \subseteq N$ such that for all $k \in \bar{N}$: $C_k < Q(k)$. Then, for each $k \in \bar{N}$, let $S_k$ contain an $1/P_1(k)$ fraction of the elements of $H_k$ and $\bar{C}_k$ be a circuit of size $C_k$ such that for all $n \in S_k$, $\bar{C}_k[x, n] = QR_n(x)$ for at least $\frac{1}{2} + (1/P_2(k))$ of the elements of $Z_n^{+1}$.

For every $k \in \bar{N}$, choose the oracle $O$ of Theorem 1 to be $\bar{C}_k$. That is, set $O[x, n] = \bar{C}_k[x, n]$ for all $n \in S_k$ and all $x \in Z_n^1$. Then, by Theorem 1, for all $k \in \bar{N}$, for all $n \in S_k$, for all $x \in Z_n^1$, and for all polynomials $P_j$, there is a probabilistic polynomial in $k$ time algorithm with oracle $\bar{C}_k$ that correctly decides quadratic residuosity of $x \mod n$ with probability greater than $1 - (1/P_3(k))$. As the size of $C_k$ is less than $Q(k)$, for all $k \in \bar{N}$ such an algorithm can be transformed into a polynomial in $k$ size circuit that correctly decides quadratic residuosity mod $n$ for all $n \in S_k$. As $|S_k| > (1/P_1(k))|H_k|$, this contradicts the QRA. $\blacksquare$

Let $n$ be a composite integer whose factorization is unknown. We want to investigate what happens to the difficulty of deciding Quadratic Residuosity modulo $n$ when we are given the extra knowledge that a particular $y \in Z_n^1$ is a quadratic non-residue mod $n$.

Remarks about Theorem 2. When the factorization of $n$ is secret, no efficient algorithm for selecting a quadratic nonresidue mod $n$ is known. Thus it may be that revealing, say, the smallest quadratic nonresidue in $Z_n^1$ may endanger the secrecy of the factorization of $n$ or make deciding quadratic residuosity modulo $n$ easy.

Theorem 2 shows that the complexity of the quadratic residuosity problem remains unchanged if a randomly selected quadratic nonresidue modulo $n$ is revealed. In other words: Assume that for a polynomial fraction of the quadratic nonresidues $x \in Z_n^1$, knowing that $x$ is indeed a quadratic nonresidue mod $n$ would lead to an efficient decision procedure for quadratic residuosity mod $n$. Then, quadratic residuosity mod $n$ could have been efficiently decided without such extra help. {#goldwasser-1984-probabilistic-thm-2 .statement tag=07F5}

Theorem 2. Let $P_1$ and $P_2$ be fixed polynomials. For each $k \in N$ let $E_k \subseteq H_k$ contain a fraction $1/P_1(k)$ of the integers in $H_k$. For each $n \in E_k$, let $S_n$ contain a $1/P_2(k)$ fraction of the quadratic nonresidues in $Z_n^1$. Let $C_k$ be the size of the smallest circuit $C[\cdot, \cdot, \cdot]$ such that for all $n \in E_k$, for all $s \in S_n$, and for all $x \in Z_n^1$ $C[n, s, x] = Q_n(x)$. Then, for all polynomials $Q$, for all sufficiently large $k$: $C_k > Q(k)$. {#goldwasser-1984-probabilistic-thm-2-2 .statement tag=07F6}

Proof. Let $k \in N$. Fix polynomials $P_1$ and $P_2$. Let $C[\cdot, \cdot, \cdot]$ be a circuit of size $C_k$ such that $C[n, y, q] = Q_n(q)$ for all $n \in E_k, y \in S_n, q \in Z_n^1$. The proof is divided into 3 parts:

(1) There exists a probabilistic algorithm $A_1$, with oracle $C[\cdot, \cdot, \cdot]$, that on input $n \in E_k$, outputs $x \in Z_n^1$ such that, with probability greater than $1 - (1/P_2(k))$,

C[n, x, · ] (1/P_2(k))-approximates Q_n(·). Algorithm A_1 terminates in expected time which is polynomial in k.

(2) Algorithm A_1 can be converted into a circuit C_1[·, ·] of size polynomial in k and C_k, such that for all n \in E_k, q \in Z_n^1, C_1[n, q] = Q_n(q).

(3) By the QRA, for all sufficiently large k, the size of C_1 exceeds any given polynomial in k. Therefore, again for sufficiently large k, for any given polynomial Q, C_k > Q(k).

We proceed to prove part (1). On input n \in E_k, define algorithm A_1 as follows:

repeat

(1) select x at random from Z_n^1.
(2) select k elements e_1, ..., e_k at random from Z_n^1. (comment: This can be accomplished in probabilistic poly(k) time by selecting elements r \in [1, n] with uniform probability and checking whether r \in Z_n^* and (r/n) = 1).
(Comment: with probability greater than 1 - (1/2^k), one of the e_i's is a quadratic nonresidue mod n.)
(3) Set e_0 = 1.
(4) For i = 0, ..., n, j = 1, ..., k
(5) select a sample of random quadratic residues mod n, x_1, ..., x_k, and compute y_{i,j} = e_i x_j \mod n.
(Comment: as e_0 = 1, {y_{0,1}, ..., y_{0,k}} is a sample of random quadratic residues mod n. With probability greater than 1 - (1/2^k), for some i > 0, {y_{i,1}, ..., y_{i,k}} is a sample of quadratic nonresidues in Z_n^1).
(6) For i = 0, ..., k,
(7) set f_i^x = (\sum_{j=0}^k C[n, x, y_{i,j}]/k).
(Comment: f_i^x estimates the probability that C[n, x, ·] outputs 1 on elements of Z_n^1 whose quadratic character is the same as that of e_i.)
until f_0^x = 1 and f_i^x = 0 for some i \geq 1.
output x.

We now prove that, with probability greater than 1 - (1/P_2(k)), algorithm A_1 computes x such that C[n, x, · ] (1/P_2(k))-approximates Q_n(·). Let $\alpha_x = \operatorname{Prob}(C[n, x, q] = 0 | Q_n(q) = 0)$ and $\beta_x = \operatorname{Prob}(C[n, x, q] = 0 | Q_n(q) = 1)$. Then, as $f_0^x = 1$ and $f_i^x = 0$ for some $i \geq 1$, then for all sufficiently large k, the weak law of large numbers assures us that $|\alpha_x - \beta_x| > (1/2P_2(k))$. By Theorem 1, this implies that $C[n, x, · ] P_2(k)$-approximates $Q_n(·)$.

Finally, about $A_1$'s running time. Note that, if in a given iteration of the algorithm we draw an x from $S_n$ and one of the e_i's is a quadratic nonresidue, then $f_0^x = 1$ and $f_i^x = 0$ and the algorithm terminates. Thus, the expected number of iterations performed by algorithm $A_1$ is

$$
\frac{1}{(1 - (1/2^k)) P_2(k)}.
$$

As each iteration, can be performed in probabilistic poly(k) time, $A_1$ runs in expected polynomial in $k$ time. This proves part (1).
Part (2) follows from Corollary 1, and standard transformations of probabilistic algorithms into circuits. Part (3) follows easily from part (2).

COROLLARY 2. Let $P_1, P_2,$ and $P_3$ be fixed polynomials. For each $k \in N$ let $E_k \subseteq H_k$ contain a fraction $1/P_1(k)$ of the integers in $H_k$. For each $n \in E_k$, let $S_n$ be a $1/P_2(k)$ fraction of the quadratic nonresidues in $Z_n^1$. Let $C_k$ be the size of the smallest circuit $C[\cdot, \cdot, \cdot]$ that on inputs $n \in E_k$ and $s \in S_n$, $(1/P_3(k))-approximates Q_n$. Then, for all polynomials $Q$, for all sufficiently large $k$: $C_k > Q(k)$.

What this corollary says is that, assuming the QRA, when user $B$ is presented with $(n, y)$ where $n \in H_k$ and $y$ a quadratic nonresidue in $Z_n^1$ and $x \in Z_n^1$, he cannot guess $Q_n(x)$ with probability greater than $\frac{1}{2}$.

### 6.4. *A Special Property of Quadratic Residuosity* {#goldwasser-1984-probabilistic-s6-4 .section tag=07F7}

Let $n \in H_k$ and $\alpha = (x_1, ..., x_k)$ be a probabilistic encryption of a $k$-bit message $m$ using the predicate $Q_n$. Given $\alpha$, anyone, without knowing the factorization of $n$, can reencrypt $m$. In fact he could choose, with uniform probability, another probabilistic encryption of $m$ by simply multiplying each $x_i$ by a different, randomly selected, quadratic residue mod $n$.

This property has been used by Luby, Micali, and Rackoff in [19] for fairly exchanging a secret bit.
