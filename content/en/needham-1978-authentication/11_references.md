---
paper: needham-1978-authentication
title: Using Encryption for Authentication in Large Networks of Computers
authors:
  - Roger M. Needham
  - Michael D. Schroeder
year: 1978
venue: Communications of the ACM
field: security
section_title: References
tag: "0943"
kind: references
lang: en
source: https://web.archive.org/web/20250531153030id_/https://dl.acm.org/doi/pdf/10.1145/359657.359659
pdf_sha256: 6fec623eab036ce7683fc0d35286988cb721593962c842b1360d981fff49d11e
pdf_pages: "7"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: bdb55a442d8ed800e7c674cf0945dcbda5c27a49046f4a539a5029a6e8292222
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

1. Branstad, D. Security aspects of computer networks, Proc. AIAA Comprr. Network Syst. Conf., April 1973, paper 73-427.
2. Branstad, D. Encryption protection in computer data communications. Proc. Fourth Data Communications Symp., Oct. 1975, pp. 8.1–8.7 (available from ACM, New York).
3. Diffie, W., and Hellman, M. Multiuser Cryptographic Techniques, Proc AFIPS 1976 NCC, AFIPS Press, Montvale, N.J., pp. 109–112.
4. Feistel, H. Cryptographic coding for data bank privacy. Res. Rep. RC2827, IBM T.J. Watson Res. Ctr., Yorktown Heights, N.Y., March 1970.
5. Kent, S. Encryption-based protection protocols for interactive user-computer communication, M.S. Th., EECS Dept., M.I.T., 1976; also available as Tech. Rep. 162, Lab. for Comprr. Sci., M.I.T., Cambridge, Mass., 1976.
6. Kent, S. Encryption-based protection for interactive user/computer communication. Proc. Fifth Data Communication Symp., Sept. 1977, pp. 5–7–5–13 (available from ACM, New York).
7. National Bureau of Standards. Data Encryption Standard. Fed. Inform. Processing Standards Pub. 46, NBS, Washington, D.C., Jan. 1977.
8. Pohlig, S. Algebraic and combinatoric aspects of cryptography. Tech. Rep. No. 6602-1, Stanford Electron. Labs., Stanford, Calif., Oct. 1977.
9. Rivest, R.L., et al. A method for obtaining digital signatures and public-key cryptosystems. Comm. ACM 21, 2 (Feb. 1978), 120–126.

Programming Techniques
S. L. Graham Editor

A Linear Sieve Algorithm for Finding Prime Numbers

David Gries
Cornell University

Jayadev Misra
University of Texas at Austin

A new algorithm is presented for finding all primes between 2 and $n$. The algorithm executes in time proportional to $n$ (assuming that multiplication of integers not larger than $n$ can be performed in unit time). The method has the same arithmetic complexity as the algorithm presented by Mairson [6]; however, our version is perhaps simpler and more elegant. It is also easily extended to find the prime factorization of all integers between 2 and $n$ in time proportional to $n$.

Key Words and Phrases: primes, algorithms, data structures
CR Categories: 5.25, 5.24, 5.29

1. Introduction

An algorithm is presented for finding all primes between 2 and $n$, for $n \geq 4$, that executes in time proportional to $n$. Like the sieve of Eratosthenes, it works by removing nonprimes from the set $\{2, ..., n\}$. Unlike the sieve of Eratosthenes, no attempt is ever made to remove a nonprime that was removed earlier; this allows us to develop a linear algorithm.

The algorithm deals with sets $S$ satisfying $S \subset \{2, ..., n\}$. Two operations will be required on such sets:

Permission to copy without fee all or part of this material is granted provided that the copies are not made or distributed for direct commercial advantage, the ACM copyright notice and the title of the publication and its date appear, and notice is given that copying is by permission of the Association for Computing Machinery. To copy otherwise, or to republish, requires a fee and/or specific permission.

This research was partially supported by the National Science Foundation under Grants DCR75-09842 and MCS76-22360.

Authors’ addresses: D. Gries, Computer Science Department, Cornell University, Ithaca, NY 14853; J. Misra, Computer Science Department, University of Texas at Austin, Austin, TX 78712.
© 1978 ACM 0001-0782/78/1200–0999 \$00.75

Communications of the ACM
December 1978
Volume 21
Number 12
