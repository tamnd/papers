---
paper: needham-1978-authentication
title: Using Encryption for Authentication in Large Networks of Computers
authors:
  - Roger M. Needham
  - Michael D. Schroeder
year: 1978
venue: Communications of the ACM
field: security
section: "9"
section_title: Commentary
tag: 032E
kind: section
lang: en
source: https://web.archive.org/web/20250531153030id_/https://dl.acm.org/doi/pdf/10.1145/359657.359659
pdf_sha256: 6fec623eab036ce7683fc0d35286988cb721593962c842b1360d981fff49d11e
pdf_pages: 6-7
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 20604fb2235d13c6aeae32585c3b25a04e60f6b3bb0416362b7ad465a6a70266
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

We conclude from this study that protocols using public-key cryptosystems and using conventional encryption algorithms are strikingly similar. The number of protocol messages exchanged is very comparable, the public-key system having a noticeable advantage only in the case of signed communications. As in many network applications of computers, caching is important to reduce transactions with lookup servers; this is particularly so with the public-key system. In that system we noticed also that there was a requirement for encryption of public data (the authentication server's database) in order to ensure its integrity. A consequence of the similarity of protocols is that any helpful tricks for the conventional system have analogs in the public-key system, though they may not be needed. Because of this, there may be scope for hybrid systems in which a public-key method may be used to establish an authenticated connection to be used conventionally. The intrinsic security requirements of a public-key authentication server are easier to meet than those of a conventional one, but a complete evaluation of the system problems in implementing such a server in a real system, and the need to retain a secure record of old public keys to guarantee future correct arbitration of old signatures may minimize this advantage. We conclude that the choice of technique should be based on the economy and cryptographic strength of the encryption techniques themselves, rather than for their effects on protocol complexity.

Finally, protocols such as those developed here are prone to extremely subtle errors that are unlikely to be detected in normal operation. The need for techniques to verify the correctness of such protocols is great, and we encourage those interested in such problems to consider this area.

Acknowledgments. We are indebted to a number of people who have read drafts of this paper and made careful and helpful comments, notably: Peter Denning, Stockton Gaines, Jim Gray, Steve Kent, Gerry Popek, Ron Rivest, Jerry Saltzer, and Robin Walker.

Received September 1977; revised April 1978; final revision May 1978
