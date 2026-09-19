---
paper: needham-1978-authentication
title: Using Encryption for Authentication in Large Networks of Computers
authors:
  - Roger M. Needham
  - Michael D. Schroeder
year: 1978
venue: Communications of the ACM
field: security
section: "7"
section_title: One-Way Communication
tag: 032C
kind: section
lang: en
source: https://web.archive.org/web/20250531153030id_/https://dl.acm.org/doi/pdf/10.1145/359657.359659
pdf_sha256: 6fec623eab036ce7683fc0d35286988cb721593962c842b1360d981fff49d11e
pdf_pages: "5"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 8d6cda634392ccaff3769fa10483fcc0ff2b8389554973875f4c96cff68471f7
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

In a computerized mail system it is impossible to depend upon interaction between the sender and the receiver in the course of each delivery. The mail is put into the hands of a transport mechanism and may be delivered later when the sender is no longer available. On the other hand, two-way authentication of sender and receiver is as desirable for mail as it is for interactive communication. Good design of a mail system would suggest that the mail transport mechanism not be part of the security system, and the proposals here meet that goal.

With Conventional Algorithms

Consider a message used in a previous protocol:

$$
A \rightarrow B: \quad \{CK, A\}^{KB}
$$

This message has the property that if it be put at the head of mail encrypted with $CK$, then the whole is self-authenticating both as to recipient and originator even though $B$ played no part at all in the setting-up protocol.

We assume that the subsequent individual blocks of the mail are securely seriated in, for example, the manner of Kent. The very fact of delay, however, causes special steps to be needed to ensure the time integrity of mail, i.e. that it has not been recorded by an intruder from an earlier transmission and repeated. We have avoided proposing the use of time-stamps elsewhere, because it presupposes a network-wide reliable source of time. Here there seems little alternative to the use of time-stamps; but it is possible to use them here without requiring a universal clock. A suitable technique is as follows. Each message has in its body a time-stamp indicating the time of sending. (Such a time-stamp is a normal part of most mail anyway.) The resolution needs to be fine enough that no two messages from the same source will have the same stamp. Any recipient, say $B$, maintains a register in which an entry of the form $\{source, time-stamp\}$ is stored for each mail item received. A time interval $T$ is associated with $B$. $T$ is taken as an upper bound on clock asynchrony in the network and the interval between the time the mail was sent and the time of its arrival within $B$'s security control, after which time the mail cannot be diverted. A mail item is rejected if either its $\{source, time-stamp\}$ is on the register or its time-stamp predates the current time by more than $T$. The register is kept small by discarding entries older than $T$. $T$ may vary dependent on $B$'s activity if a message may only arrive in his security control when he is present.

With Public-Key Algorithms

The means of ensuring time integrity are identical in this case and will not be repeated. We have two alternative courses. With the first a header is sent that identifies $A$ to $B$ without using a handshake:

$$
A \rightarrow B: \quad \{A, I, \{B\}^{SKA}\}^{PKB}
$$

Here $A$ denotes the sender and $\{B\}^{SKA}$ enables authentication by $B$ of the identity of the sender using protocol transactions as at (2.4) and (2.5) (which may of course be short-cut by caching). $I$ is a nonce identifier that is used to connect the header with the ensuing message text sent under the protection of $PKB$, with a time-stamp as above and with a secure seriation as discussed earlier. The connection between header and message provided explicitly by $I$ in this protocol is provided implicitly by $CK$ in the case of a conventional encryption algorithm.

The other way to handle mail using the public-key system achieves the additional function of signature and is described in the next section.
