---
paper: needham-1978-authentication
title: Using Encryption for Authentication in Large Networks of Computers
authors:
  - Roger M. Needham
  - Michael D. Schroeder
year: 1978
venue: Communications of the ACM
field: security
section_title: Introduction
kind: section
lang: en
source: https://web.archive.org/web/20250531153030id_/https://dl.acm.org/doi/pdf/10.1145/359657.359659
pdf_sha256: 6fec623eab036ce7683fc0d35286988cb721593962c842b1360d981fff49d11e
pdf_pages: 1-2
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 5764e42d9fe921138154dfa3a831103e92e9665dbe3619fd36bcb06407e758ad
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

In the context of secure computer communications, authentication means verifying the identity of the communicating principals to one another. A network in which a large number of computers communicate may have no central machine or system that contains authoritative descriptions of the connected computers, of the purposes for which they are used, or of the individuals who use them. We present protocols for decentralized authentication in such a network that are integrated with the allied subject of naming. There is minimal reliance on network-wide services; in particular there is no reliance on a single network clock or a single network name management authority.

Three functions are discussed:

(1) Establishment of authenticated interactive communication between two principals on different machines. By interactive communication we mean a series of messages in either direction, typically each in response to a previous one.

(2) Authenticated one-way communication, such as is found in mail systems, where it is impossible to require protocol exchanges between the sender and the recipient while sending an item, since there can be no guarantee that sender and recipient are simultaneously available.

(3) Signed communication, in which the origin of a communication and the integrity of the content can be authenticated to a third party.

Secure communication in physically vulnerable networks depends upon encryption of material passed between machines. We assume that it is feasible for each computer in the network to encrypt and decrypt material efficiently with arbitrary keys, and that these keys are not readily discoverable by exhaustive search or cryptanalysis. We consider both conventional encryption algorithms and public-key encryption algorithms as a basis for the protocols presented.

We assume that an intruder can interpose a computer in all communication paths, and thus can alter or copy parts of messages, replay messages, or emit false material. While this may seem an extreme view, it is the only safe one when designing authentication protocols.

We also assume that each principal has a secure environment in which to compute, such as is provided by a personal computer or would be by a secure shared operating system. Our viewpoint throughout is to provide authentication services to principals that choose to communicate securely. We have not considered the extra problems encountered when trying to force all communication to be performed in a secure fashion or when trying to prevent communication between particular principals in order to enforce restrictions on information flow.

Our protocols should be regarded as examples that expose the authentication issues in large networks rather than as fully engineered solutions to the overall security problems of a particular application. While providing an adequate solution to the authentication problems specified and meeting most common security objectives, our protocols would need elaboration to meet other security goals such as preventing traffic analysis, withholding all matching cleartext-ciphertext pairs from an eavesdropper, and ensuring instantaneous detection of tampering, and also to maximize efficiency in particular networks. It is possible to devise other protocols similar to those presented that also meet the stated objectives.

There is a modest amount of literature on our subject, and methods have been proposed for several of the individual functions we describe [1, 3, 5, 6], although no work is reported that integrates these techniques and applies them in a decentralized environment, or that provides functionally equivalent protocols based on both conventional and public-key encryption.
