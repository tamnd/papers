---
paper: steiner-1988-kerberos
title: 'Kerberos: An Authentication Service for Open Network Systems'
authors:
  - Jennifer G. Steiner
  - Clifford Neuman
  - Jeffrey I. Schiller
year: 1988
venue: USENIX Winter Conference
field: security
section: "3"
section_title: Kerberos Names
tag: 07FF
kind: section
lang: en
source: http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.112.9002
pdf_sha256: 2dd6604c96afde95681d25fe32df9834aad32274d1bdbb44dd5f69d6b9660f59
pdf_pages: 4-5
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 309135bb200ea22d9938e9c646fc46cf9d31eababcc1a0e9d7093ef90a415258
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Part of authenticating an entity is naming it. The process of authentication is the verification that the client is the one named in a request. What does a name consist of? In Kerberos, both users and servers are named. As far as the authentication server is concerned, they are equivalent. A name consists of a primary name, an instance, and a realm, expressed as name.instance@realm (see Figure 2).

bcn
treese.root
jis@LCS.MIT.EDU
rlogin.priam@ATHENA.MIT.EDU

Figure 2. Kerberos Names. {#steiner-1988-kerberos-fig-2 .figure tag=0800}

The primary name is the name of the user or the service. The instance is used to distinguish among variations on the primary name. For users, an instance may entail special privileges, such as the “root” or “admin” instances. For services in the Athena environment, the instance is usually the name of the machine on which the server runs. For example, the rlogin service has different instances on different hosts: rlogin.priam is the rlogin server on the host named priam. A Kerberos ticket is only good for a single named server. As such, a separate ticket is required to gain access to different instances of the same service. The realm is the name of an administrative entity that maintains authentication data. For example, different institutions may each have their own Kerberos machine, housing a different database. They have different Kerberos realms. (Realms are discussed further in section 8.2.)
