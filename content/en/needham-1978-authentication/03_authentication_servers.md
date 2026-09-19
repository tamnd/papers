---
paper: needham-1978-authentication
title: Using Encryption for Authentication in Large Networks of Computers
authors:
  - Roger M. Needham
  - Michael D. Schroeder
year: 1978
venue: Communications of the ACM
field: security
section: "2"
section_title: Authentication Servers
tag: "0327"
kind: section
lang: en
source: https://web.archive.org/web/20250531153030id_/https://dl.acm.org/doi/pdf/10.1145/359657.359659
pdf_sha256: 6fec623eab036ce7683fc0d35286988cb721593962c842b1360d981fff49d11e
pdf_pages: "2"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 77052d8a17c45b6f75065133b55233f4832eab9bf6bc4c57e1bc425392eaada6
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

With both kinds of encryption the basis of authenticated communication is a secret key belonging to each principal using the network, and there is need for an authoritative source of information about these keys. We use the term *authentication server* for a server that can deliver identifying information computed from a requested principal's secret key.

Since the main database of an authentication server is indexed by name, the management of authentication servers is related to the management of names. In an extended network it is inexpedient to have a single central name registration authority, so we suppose that there are multiple naming authorities, each of which assigns and cancels names as it wishes. With this organization, principals have names of the form "NamingAuthority.SimpleName." Associated with each naming authority are one or more name lookup servers and one or more authentication servers.\footnote{Naming authorities are independent of network topology; they need have nothing to do with subnetworks or with particular computers on the network. Multiple identical name lookup servers and authentication servers for a single naming authority may be used to make sure that these services are topologically "close" to those needing to use them, and to enhance reliability. Our multiple authentication servers must be carefully distinguished from those proposed by Diffie and Hellman [3], which perform the quite different function of checking one another. In that case every user is registered with every authenticator, the aim being to defend against corruption of particular authenticators.}

A name lookup server is prepared to provide various network addresses associated with a given SimpleName, for example, the address of that principal's mail system buffer. One or more instances of a master name lookup server will provide the network addresses of appropriate name lookup and authentication servers when given a naming authority's name. Authentication servers perform strikingly similar functions for the two classes of encryption algorithms; the differences will be brought out as they arise.
