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
section: "7"
section_title: The Bigger Picture
tag: "0819"
kind: section
lang: en
source: http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.112.9002
pdf_sha256: 2dd6604c96afde95681d25fe32df9834aad32274d1bdbb44dd5f69d6b9660f59
pdf_pages: 10-11
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: c9c0def3841f15c3be18ea9abce7b82cfbc4ff080751038e4f95392ea30bc1b0
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

In this section, we describe how Kerberos fits into the Athena environment, including its use by other network services and applications, and how it interacts with remote Kerberos realms. For a more complete description of the Athena environment, please see G. W. Treese.9

### 7.1. Other Network Services’ Use of Kerberos {#steiner-1988-kerberos-s7-1 .section tag=081A}

Several network applications have been modified to use Kerberos. The rlogin and rsh commands first try to authenticate using Kerberos. A user with valid Kerberos tickets can rlogin to another Athena machine without having to set up .rhosts files. If the Kerberos authentication fails, the programs fall back on their usual methods of authorization, in this case, the .rhosts files.

We have modified the Post Office Protocol to use Kerberos for authenticating users who wish to retrieve their electronic mail from the “post office”. A message delivery program, called Zephyr, has been recently developed at Athena, and it uses Kerberos for authentication as well.10

The program for signing up new users, called register, uses both the Service Management System (SMS)11 and Kerberos. From SMS, it determines whether the information entered by the would-be new Athena user, such as name and MIT identification number, is valid. It then checks with Kerberos to see if the requested username is unique. If all goes well, a new entry is made to the Kerberos database, containing the username and password.

For a detailed discussion of the use of Kerberos to secure Sun’s Network File System, please refer to the appendix.

### 7.2. Interaction with Other Kerberi {#steiner-1988-kerberos-s7-2 .section tag=081B}

It is expected that different administrative organizations will want to use Kerberos for user authentication. It is also expected that in many cases, users in one organization will want to use services in another. Kerberos supports multiple administrative domains. The specification of names in Kerberos includes a field called the realm. This field contains the name of the administrative domain within which the user is to be authenticated.

Services are usually registered in a single realm and will only accept credentials issued by an authentication server for that realm. A user is usually registered in a single realm (the local realm), but it is possible for her/him to obtain credentials issued by another realm (the remote realm), on the strength of the authentication provided by the local realm. Credentials valid in a remote realm indicate the realm in which the user was originally authenticated. Services in the remote realm can choose whether to honor those credentials, depending on the degree of security required and the level of trust in the realm that initially authenticated the user.

In order to perform cross-realm authentication, it is necessary that the administrators of each pair of realms select a key to be shared between their realms. A user in the local realm can then request a ticket-granting ticket from the local authentication server for the ticket-granting server in the remote realm. When that ticket is used, the remote ticket-granting server recognizes that the request is not from its own realm, and it uses the previously exchanged key to decrypt the ticket-granting ticket. It then issues a ticket as it normally would, except that the realm field for the client contains the name of the realm in which the client was originally authenticated.

This approach could be extended to allow one to authenticate oneself through a series of realms until reaching the realm with the desired service. In order to do this, though, it would be necessary to record the entire path that was taken, and not just the name of the initial realm in which the user was authenticated. In such a situation, all that is known by the server is that A says that B says that C says that the user is so-and-so. This statement can only be trusted if everyone along the path is also trusted.
