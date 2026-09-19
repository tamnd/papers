---
paper: needham-1978-authentication
title: Using Encryption for Authentication in Large Networks of Computers
authors:
  - Roger M. Needham
  - Michael D. Schroeder
year: 1978
venue: Communications of the ACM
field: security
section: "1"
section_title: Encryption Algorithms
tag: "0326"
kind: section
lang: en
source: https://web.archive.org/web/20250531153030id_/https://dl.acm.org/doi/pdf/10.1145/359657.359659
pdf_sha256: 6fec623eab036ce7683fc0d35286988cb721593962c842b1360d981fff49d11e
pdf_pages: "2"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: acbb817dfb63c80c40d258d01233e45e307589f9c95d7690f4e9fcd352b64a92
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The important difference between conventional and public-key encryption algorithms is the way keys are used. With a conventional encryption algorithm, such as the NBS Data Encryption Standard [7], the same key is used for both encryption and decryption. Authentication depends upon the two participants in a conversation being the only two principals (apart possibly from trusted servers) who know the key that is being used to encrypt the transmitted material. With a public-key encryption algorithm, a concept originated by Diffie and Hellman [3], two keys are necessary: one that is used in the conversion of cleartext to ciphertext, and another that is used in the conversion of ciphertext to cleartext. Furthermore, knowledge of one key gives no help in finding the other, and the two keys will act as inverses for each other. Elegant systems may be devised in which each principal has one public key and one secret key. Anyone may encrypt a communication for $A$ using his public key, but only $A$ can decrypt the result using his secret key. Likewise, only $A$ can encrypt messages that will decrypt sensibly with $A$'s public key. The first example of a public-key encryption algorithm was devised by Rivest et al. [[rivest-1978-rsa]], and others are sure to follow.
