---
paper: goldwasser-1984-probabilistic
title: Probabilistic Encryption
authors:
  - Shafi Goldwasser
  - Silvio Micali
year: 1984
venue: Journal of Computer and System Sciences
field: security
section: "3"
section_title: UNAPPROXIMABLE TRAPDOOR PREDICATES
tag: "07E1"
kind: section
lang: en
source: https://people.csail.mit.edu/silvio/Selected%20Scientific%20Papers/Encryption/Probabilistic_Encryption.pdf
pdf_sha256: b3d2f75d09da80c0bc3b39e3001ea3dd782b42af46df9c5bde0741f2dab7aa4a
pdf_pages: 8-10
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: adca798bb444da47d42b4013525edc19c7a60e468d88693fff1d030dc2d58386
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

In Section 4 we introduce the model of a probabilistic public key cryptosystem. We show that this model is highly secure. Our model switches from block encryption to bit-by-bit encryption. For this purpose we must abandon the notion of trapdoor functions for the new notion of unapproximable trapdoor predicates.

Definition ($\varepsilon$-approximates). A circuit $C[\cdot]$ $\varepsilon$-approximates the predicate $B : \Omega \to \{0, 1\}$ if $C[x] = B[x]$ for at least a fraction $\frac{1}{2} + \varepsilon$ of the $x \in \Omega$.

We proceed to formally define unapproximable trapdoor predicates.

Let $N$ denote the set of natural numbers and $N'$ be an infinite subset of $N$. For every $k \in N'$ let $S_k$ denote a subset of the $k$-bit integers and for every $i \in S_k$ let $\Omega_i$ be a subset of the integers with at most $k$ bits. Let

$$
B_k = \{ B_i : \Omega_i \to \{0, 1\} \mid i \in S_k \}
$$

be a collection of predicates indexed by an integer of size $k$ and

$$
B = \bigcup_{k \in N'} B_k.
$$

We say that $B$ is an unapproximable trapdoor predicate (UTP) if:

(1) ($B$ is unapproximable): Fix polynomials $P_1$ and $P_2$. Let $k \in N'$. Let $c_k$ denote the size of the minimum size circuit $C[\ , ]$ such that $C\ , i)$-approximates $B_i$ for at least a fraction $1/P_2(k)$ of the $i \in S_k$. We say that $B$ is unapproximable if $c_k$ grows faster than any polynomial in $k$.

(2) ($B$ is trapdoor): For $v \in \{0, 1\}$ set $\Omega_i^v = \{ x \in \{ \Omega_i \} \mid B_i(x) = v \}$. We say that $B$ is trapdoor if:

(a) There exists a probabilistic polynomial in $k$ time Turing machine $T_1$ that on input $(i, v)$, where $i \in S_k$ and $v \in \{0, 1\}$, selects $x \in \Omega_i^v$ with uniform probability.

(b) There exists a function $\sigma: \bigcup_{k \in V'} S_k \to N$ such that for some polynomial $Q$, for all $x, |\sigma(x)| < Q(|x|)$, and a polynomial time Turing machine $T_2$ such that $T_2[i, \sigma(i), x] = B_i(x)$ for all $i \in S_k$, and for all $x \in \Omega_i$. We call $\sigma(i)$ the secret of $i$.

(c) (constructibility condition): for all $k \in N'$ it is possible in probabilistic polynomial in $k$ time to select any pair $(i \in S_k, \sigma(i))$, with probability $1/|S_k|$.

Condition (2c), the constructibility condition, guarantees that if someone picks a pair $(i, \sigma(i))$, where $i \in S_k$ and publicizes $i$, it will be hard to compute $B_i(x)$. Otherwise, suppose the pairs $(i, \sigma(i)), i \in S_k$, that could be efficiently selected constituted a very small fraction of all possible pairs. Then, an adversary could, from the public $i$, find out $\sigma(i)$ just by repeatedly selecting pairs $(j, \sigma(j))$ until $j = i$.

Remark 3.1. Note that if $B$ is an unapproximable predicate and $P_1, P_2$ are polynomials, then for all sufficiently large $k$, for a fraction $1 - (1/P_1(k))$ of the $i \in S_k$, $|\Omega_i^0|/|\Omega_i|$ and $|\Omega_i^1|/|\Omega_i|$ are both greater than $\frac{1}{2} - (1/P_2(k))$. Otherwise either the trivial circuit $C_k$ that always outputs 0 or the trivial circuit that always outputs 1 would $(1/P_2(k))-$ approximate $B_i$ for a fraction at least $1/P_1(k)$ of the $i \in S_k$. {#goldwasser-1984-probabilistic-rem-3-1 .statement tag=0952}

### 3.1. Quadratic Residuosity as a UTP {#goldwasser-1984-probabilistic-s3-1 .section tag=0953}

We demonstrate an example of an unapproximable trapdoor set of predicates, under the intractability assumption of the Quadratic Residuosity Problem (QRP). If needed the number theoretic definitions can be found in Section 7.

Let $k \in N$. Let $p_1$ and $p_2$ denote primes. Set,

$$
H_k = \{ n \mid n = p_1 p_2, \text{ where } |p_1| = |p_2| = k \},
$$

$$
Z_n^* = \{ x \leq n \mid (x, n) = 1 \}.
$$

And let $Z_n^1$ denote the subset of $Z_n^*$ containing the elements with Jacobi symbol +1. For all $x \in Z_n^1$, $Q_n$ is defined as

$$
Q_n(x) = 1 \quad \text{if } x \text{ is a quadratic residue mod } n,
$$

$$
= 0 \quad \text{if } x \text{ is a quadratic nonresidue mod } n.
$$

Let $k \in N$. Let $x$ and $y$ be binary strings. We denote by $x \# y$ the concatenation of $x$ and $y$. Define $S_{4k} = \{ n \# y \mid n \in H_k \text{ and } y \in Z_n^1 \text{ is a quadratic nonresidue mod } n \}$. Define $\Omega_{n \# y} = Z_n^1$ and set $Q_{n \# y}(x) = Q_n(x)$ for each $x \in Z_n^1$. Then $Q^* = \{ Q_{n \# y} \mid n \# y \in S_{4k} \}$ is a set of predicates. The presence of the quadratic nonresidue $y$ will be needed to show the trapdoorness of $Q^*$.

(1) $Q^*$ is unapproximable: This is shown in Theorem 2 (Section 7), under the Quadratic Residuosity Assumption.

(2) $Q^*$ is trapdoor: Letting $\sigma_{4k}(n \# y)$ be the factorization of $n$, $Q^*$ is a trapdoor set of predicates. In fact, if the factorization of $n$ is known, $Q_n(\cdot)$ can be computed in $O(k^3)$ time. Moreover, given $y$, a quadratic nonresidue mod $n$, we can generate quadratic nonresidues mod $n$ with uniform probability in probabilistic polynomial in $k$ time by randomly selecting $x \in Z_n^*$ and computing $r = yx^2 \mod n$.

(3) $Q^*$ is constructible: Consider the following algorithm that selects one element $n \# y \in S_{4k}$, where $n \in H_k$ and $y \in Z_n^{+1}$ is a quadratic nonresidue mod $n$.

Step 1. Flip $4k$ fair coins.

Step 2. Check whether the first $k$ outcomes and the second $k$ outcomes constitute, respectively, the binary representation of a prime $p_1$ and a prime $p_2$ each of size $k$. If so, let $n = p_1 p_2$ and check if the last $2k$ bits constitute a quadratic nonresidue $y \mod n$. If so then halt: $p_1 \cdot p_2 \# y$ has been selected. Else go to Step 1.

As each element in $S_{4k}$ can be generated by exactly one $4k$-long sequence of coin tosses, the above algorithm selects elements in $S_{4k}$ with uniform probability. Due to the Prime Number Theorem and the existence of random polynomial time algorithms for primality checking, the above algorithm runs in random poly$(k)$ time.

We conclude that, under the QRA, $Q^*$ is an unapproximable trapdoor predicate.
