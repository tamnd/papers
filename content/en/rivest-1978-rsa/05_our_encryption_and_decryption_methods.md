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
section: V
section_title: Our Encryption and Decryption Methods
tag: "0948"
kind: section
lang: en
source: https://doi.org/10.21236/ada606588
pdf_sha256: f7b1f78d9a7cbeb85e32b8c563a6db60771a5cc4bdc55580645f7cb778a4966b
pdf_pages: 6-7
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 12a1fe38961a14c6a0e1faa75eecf7dc6163ec20d221d9eb03d7a07933b41867
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

To encrypt a message $M$ with our method, using a public encryption key $(e, n)$, proceed as follows. (Here $e$ and $n$ are a pair of positive integers.)

First, represent the message as an integer between 0 and $n - 1$. (Break a long message into a series of blocks, and represent each block as such an integer.) Use any standard representation. The purpose here is not to encrypt the message but only to get it into the numeric form necessary for encryption.

Then, encrypt the message by raising it to the eth power modulo $n$. That is, the result (the ciphertext $C$) is the remainder when $M^e$ is divided by $n$.

To decrypt the ciphertext, raise it to another power $d$, again modulo $n$. The encryption and decryption algorithms $E$ and $D$ are thus:

$$
C \equiv E(M) \equiv M^e \pmod{n}, \text{ for a message } M .
$$

$$
D(C) \equiv C^d \pmod{n}, \text{ for a ciphertext } C .
$$

Note that encryption does not increase the size of a message; both the message and the ciphertext are integers in the range 0 to $n - 1$.

The encryption key is thus the pair of positive integers $(e, n)$. Similarly, the decryption key is the pair of positive integers $(d, n)$. Each user makes his encryption key public, and keeps the corresponding decryption key private. (These integers should properly be subscripted as in $n_A, e_A,$ and $d_A$, since each user has his own set. However, we will only consider a typical set, and will omit the subscripts.)

How should you choose your encryption and decryption keys, if you want to use our method?

You first compute $n$ as the product of two primes $p$ and $q$:

$$
n = p \cdot q .
$$

These primes are very large, “random” primes. Although you will make $n$ public, the factors $p$ and $q$ will be effectively hidden from everyone else due to the enormous difficulty of factoring $n$. This also hides the way $d$ can be derived from $e$.

You then pick the integer $d$ to be a large, random integer which is relatively prime to $(p - 1) \cdot (q - 1)$. That is, check that $d$ satisfies:

$$
\gcd(d, (p - 1) \cdot (q - 1)) = 1
$$

(“gcd” means “greatest common divisor”).

The integer e is finally computed from p, q, and d to be the “multiplicative inverse” of d, modulo $(p - 1) \cdot (q - 1)$. Thus we have

$$
e \cdot d \equiv 1 \pmod{(p - 1) \cdot (q - 1)}.
$$

We prove in the next section that this guarantees that (1) and (2) hold, i.e. that $E$ and $D$ are inverse permutations. Section VII shows how each of the above operations can be done efficiently.

The aforementioned method should not be confused with the “exponentiation” technique presented by Diffie and Hellman [[diffie-1976-newdirections]] to solve the key distribution problem. Their technique permits two users to determine a key in common to be used in a normal cryptographic system. It is not based on a trap-door one-way permutation. Pohlig and Hellman [8] study a scheme related to ours, where exponentiation is done modulo a prime number.
