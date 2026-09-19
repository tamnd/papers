---
paper: needham-1978-authentication
title: Using Encryption for Authentication in Large Networks of Computers
authors:
  - Roger M. Needham
  - Michael D. Schroeder
year: 1978
venue: Communications of the ACM
field: security
section: "5"
section_title: Multiple Authentication Servers
tag: 032A
kind: section
lang: en
source: https://web.archive.org/web/20250531153030id_/https://dl.acm.org/doi/pdf/10.1145/359657.359659
pdf_sha256: 6fec623eab036ce7683fc0d35286988cb721593962c842b1360d981fff49d11e
pdf_pages: "4"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 8476a2a40ab85777f52588f616a84b952bc91aec39b37e5d69f03508e8cdb896
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

In the protocols just given we assumed that $A$ and $B$ were clients of the same authentication server. This restriction is not necessary, and we now remove it. When extending the protocols we must bear in mind that, while an authentication server must be regarded as the final authority for its clients, it must be able to have no effect for good or ill on communication between clients of other authentication servers. Then our system will not be upset completely by the conduct of a shoddy authenticator. Of course, outsiders will show circumspection on a human level in their dealings with a shoddy authenticator’s clients.

The effects on the protocols of multiple authentication servers differ somewhat between the two encryption techniques. Consider first the case of conventional encryption. The requirement is still to produce an item of the form $\{CK, A\}^{KB}$ for $A$ to use when making his first approach to $B$ (see step (1.3)). To produce this quantity both authentication servers (which will be called $AS_A$ and $AS_B$) are involved, since only $AS_B$ can produce items encrypted with $KB$ and only $AS_A$ can produce items encrypted with $KA$. We find two more steps between (1.1) and (1.2), which constitute an interchange between the two servers. We suppose that separate measures have been taken to ensure secure communication between the servers—for example, their secret keys are held by a master server, and the regular servers establish secure links (by protocol 1 already given) whenever they come into operation. We also presume that names are, where necessary, always full “NamingAuthority SimpleName” names, so that the correct authentication server can be located. As explained above, the knowledge of a naming authority’s name leads to the network address of the associated authentication server.

$$
AS_A \rightarrow AS_B: \quad CK, B, A, I_{A1}
$$

$$
AS_B \rightarrow AS_A: \quad \{CK, A\}^{KB}, I_{A1}, A
$$

($I_{A1}$ is transmitted to avoid retention of state in $AS_A$ between messages (1.11) and (1.12).) Following (1.12) $AS_A$ is in a position to complete the protocol.

In the public-key case, since no secret keys are moved around, it is possible for $A$ to approach $AS_B$ directly if $A$ knows that server’s public key. We assume that $A$ already has this knowledge, though in a strict case of total ignorance there would be key lookup steps, for example, correspondence with a master authentication server, before (2.1). With the knowledge of $PKAS_B$, $A$ corresponds directly with $AS_B$ in steps (2.1) and (2.2). Likewise, with knowledge of $PKAS_A$, $B$ corresponds directly with $AS_A$ in (2.4) and (2.5).

In both cases caching can be expected to reduce the number of protocol messages to three.
