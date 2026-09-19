---
paper: rivest-1978-rsa
title: A Method for Obtaining Digital Signatures and Public-Key Cryptosystems
authors:
  - R. L. Rivest
  - A. Shamir
  - L. Adleman
year: 1978
venue: Communications of the ACM
field: security
section: VI
section_title: The Underlying Mathematics
tag: "0949"
kind: section
lang: en
source: https://doi.org/10.21236/ada606588
pdf_sha256: f7b1f78d9a7cbeb85e32b8c563a6db60771a5cc4bdc55580645f7cb778a4966b
pdf_pages: 7-8
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 95cb9b6da4899c5e01b846804ddbd50a3badc1b7f9806af3b2f6e9a45b7ff6ef
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

We demonstrate the correctness of the deciphering algorithm using an identity due to Euler and Fermat [7]: for any integer (message) $M$ which is relatively prime to $n$,

$$
M^{\phi(n)} \equiv 1 \pmod{n}.
$$

(3)

Here $\phi(n)$ is the Euler totient function giving number of positive integers less than $n$ which are relatively prime to $n$. For prime numbers $p$,

$$
\phi(p) = p - 1.
$$

In our case, we have by elementary properties of the totient function [7]:

$$
\begin{align*}
\phi(n) &= \phi(p) \cdot \phi(q) \\
&= (p - 1) \cdot (q - 1) \\
&= n - (p + q) + 1.
\end{align*}
$$

(4)

Since $d$ is relatively prime to $\phi(n)$, it has a multiplicative inverse $e$ in the ring of integers modulo $\phi(n)$:

$$
e \cdot d \equiv 1 \pmod{\phi(n)}.
$$

(5)

We now prove that equations (1) and (2) hold (that is, that deciphering works correctly if $e$ and $d$ are chosen as above). Now

$$
\begin{align*}
D(E(M)) &\equiv (E(M))^d \equiv (M^e)^d \pmod{n} = M^{e \cdot d} \pmod{n} \\
E(D(M)) &\equiv (D(M))^e \equiv (M^d)^e \pmod{n} = M^{e \cdot d} \pmod{n}
\end{align*}
$$

and

$$
M^{e \cdot d} \equiv M^{k \cdot \phi(n) + 1} \pmod{n} \quad \text{(for some integer } k).
$$

From (3) we see that for all $M$ such that $p$ does not divide $M$

$$
M^{p-1} \equiv 1 \pmod{p}
$$

and since $(p-1)$ divides $\phi(n)$

$$
M^{k \cdot \phi(n)+1} \equiv M \pmod{p}.
$$

This is trivially true when $M \equiv 0 \pmod{p}$, so that this equality actually holds for all $M$. Arguing similarly for $q$ yields

$$
M^{k \cdot \phi(n)+1} \equiv M \pmod{q}.
$$

Together these last two equations imply that for all $M$,

$$
M^{e \cdot d} \equiv M^{k \cdot \phi(n)+1} \equiv M \pmod{n}.
$$

This implies (1) and (2) for all $M, 0 \leq M < n$. Therefore $E$ and $D$ are inverse permutations. (We thank Rich Schroeppe1 for suggesting the above improved version of the authors’ previous proof.)
