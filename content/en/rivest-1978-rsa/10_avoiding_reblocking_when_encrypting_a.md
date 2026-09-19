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
section: X
section_title: Avoiding “Reblocking” When Encrypting A Signed Message
tag: 094D
kind: section
lang: en
source: https://doi.org/10.21236/ada606588
pdf_sha256: f7b1f78d9a7cbeb85e32b8c563a6db60771a5cc4bdc55580645f7cb778a4966b
pdf_pages: "13"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: a56fb6a546cc5e1c86bcbc3fd7864ffad5ea350e58837fe0d4ac7afc20ee9b59
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

A signed message may have to be “reblocked” for encryption since the signature $n$ may be larger than the encryption $n$ (every user has his own $n$). This can be avoided as follows. A threshold value $h$ is chosen (say $h = 10^{199}$) for the public-key cryptosystem. Every user maintains two public $(e, n)$ pairs, one for enciphering and one for signature-verification, where every signature $n$ is less than $h$, and every enciphering $n$ is greater than $h$. Reblocking to encipher a signed message is then unnecessary; the message is blocked according to the transmitter’s signature $n$.

Another solution uses a technique given in [4]. Each user has a single $(e, n)$ pair where $n$ is between $h$ and $2h$, where $h$ is a threshold as above. A message is encoded as a number less than $h$ and enciphered as before, except that if the ciphertext is greater than $h$, it is repeatedly re-enciphered until it is less than $h$. Similarly for decryption the ciphertext is repeatedly deciphered to obtain a value less than $h$. If $n$ is near $h$ re-enciphering will be infrequent. (Infinite looping is not possible, since at worst a message is enciphered as itself.)
