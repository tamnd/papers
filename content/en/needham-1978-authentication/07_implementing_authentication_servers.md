---
paper: needham-1978-authentication
title: Using Encryption for Authentication in Large Networks of Computers
authors:
  - Roger M. Needham
  - Michael D. Schroeder
year: 1978
venue: Communications of the ACM
field: security
section: "6"
section_title: Implementing Authentication Servers
tag: 032B
kind: section
lang: en
source: https://web.archive.org/web/20250531153030id_/https://dl.acm.org/doi/pdf/10.1145/359657.359659
pdf_sha256: 6fec623eab036ce7683fc0d35286988cb721593962c842b1360d981fff49d11e
pdf_pages: 4-5
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 5cd17dc88d56f604096b6437ded40e506e0dd8182e8d6b26d71ff6f0fd56871d
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

There are differences in the implementation of authentication servers for the two varieties of encryption. In the conventional case the content of the database, items of the form $A:KA$, must be kept secret (which could be done by encrypting it with the secret, identifying key of the server). A secure transaction takes place every time the server is used: at step (1.2) the keys of both customers must be extracted in order to construct the message contents. By contrast, in the public-key case the content of the database need not be secret, and no secure transaction need take place when the server is used if the server’s database is set up to contain items of the form $A: \{PKA, A\}^{SKAS}$ as required at step (2.2). (If the server contained the public keys directly, there would still be a secure operation at each use, for the reasons mentioned in the discussion of step (2.2).) With the public-key authentication server there still is a requirement for a secure computation, creating $\{PKA, A\}^{SKAS}$, but only when a new public key is registered, and this operation may be done outside the authentication server and the result added to the database in a nonsecure way. In practice, however, we suspect that the implementation of authentication servers would not differ as much as we have indicated, for reasons such as the need to prevent corruption of the public-key authentication server’s data, which could prevent communication even though it will not lead to faulty authentication.

Note that with both encryption techniques the communications with servers can be done without the formalities of establishing what is usually called a “connection.” The servers need never retain information about an ongoing transaction from one message to the next, so that repetition or loss of protocol packets does not matter. Only at step (1.11) does anything special have to be done to ensure lack of connection state. If this simplicity were lost, then the total cost of protocol exchanges would become higher.
