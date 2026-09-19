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
section: II
section_title: Public-Key Cryptosystems
tag: "0945"
kind: section
lang: en
source: https://doi.org/10.21236/ada606588
pdf_sha256: f7b1f78d9a7cbeb85e32b8c563a6db60771a5cc4bdc55580645f7cb778a4966b
pdf_pages: 2-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 82ff4396053dc11135f2577b819e1a9d1a5c273f69040c47df7cb2c87482dc17
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

In a “public key cryptosystem” each user places in a public file an encryption procedure $E$. That is, the public file is a directory giving the encryption procedure of each user. The user keeps secret the details of his corresponding decryption procedure $D$. These procedures have the following four properties:

(a) Deciphering the enciphered form of a message $M$ yields $M$. Formally,

$$
D(E(M)) = M.
$$

(b) Both $E$ and $D$ are easy to compute.

(c) By publicly revealing $E$ the user does not reveal an easy way to compute $D$. This means that in practice only he can decrypt messages encrypted with $E$, or compute $D$ efficiently.

(d) If a message $M$ is first deciphered and then enciphered, $M$ is the result. Formally,

$$
E(D(M)) = M.
$$

An encryption (or decryption) procedure typically consists of a *general method* and an *encryption key*. The general method, under control of the key, enciphers a message $M$ to obtain the enciphered form of the message, called the *ciphertext* $C$. Everyone can use the same general method; the security of a given procedure will rest on the security of the key. Revealing an encryption algorithm then means revealing the key.

When the user reveals $E$ he reveals a very *inefficient* method of computing $D(C)$: testing all possible messages $M$ until one such that $E(M) = C$ is found. If property (c) is satisfied the number of such messages to test will be so large that this approach is impractical.

A function $E$ satisfying (a)-(c) is a “trap-door one-way function;” if it also satisfies (d) it is a “trap-door one-way permutation.” Diffie and Hellman [[diffie-1976-newdirections]] introduced the concept of trap-door one-way functions but did not present any examples. These functions are called “one-way” because they are easy to compute in one direction but (apparently) very difficult to compute in the other direction. They are called “trap-door” functions since the inverse functions are in fact easy to compute once certain private “trap-door” information is known. A trap-door one-way function which also satisfies (d) must be a permutation: every message is the ciphertext for some other message and every ciphertext is itself a permissible message. (The mapping is “one-to-one” and “onto”). Property (d) is needed only to implement “signatures.”

The reader is encouraged to read Diffie and Hellman’s excellent article [[diffie-1976-newdirections]] for further background, for elaboration of the concept of a public-key cryptosystem, and for a discussion of other problems in the area of cryptography. The ways in which a public-key cryptosystem can ensure privacy and enable “signatures” (described in Sections III and IV below) are also due to Diffie and Hellman.

For our scenarios we suppose that $A$ and $B$ (also known as Alice and Bob) are two users of a public-key cryptosystem. We will distinguish their encryption and decryption procedures with subscripts: $E_A, D_A, E_B, D_B$.
