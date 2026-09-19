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
section_title: Front Matter
tag: 019C
kind: front
lang: en
source: http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.112.9002
pdf_sha256: 2dd6604c96afde95681d25fe32df9834aad32274d1bdbb44dd5f69d6b9660f59
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 9e474d18dcc9446a1011c0bf72b3a6a42cb6d6041611756a306268973021818e
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Kerberos: An Authentication Service for Open Network Systems

Jennifer G. Steiner
Project Athena
Massachusetts Institute of Technology
Cambridge, MA 02139
steiner@ATHENA.MIT.EDU

Clifford Neuman†
Department of Computer Science, FR-35
University of Washington
Seattle, WA 98195
bcn@CS.WASHINGTON.EDU

Jeffrey I. Schiller
Project Athena
Massachusetts Institute of Technology
Cambridge, MA 02139
jis@ATHENA.MIT.EDU

ABSTRACT

In an open network computing environment, a workstation cannot be trusted to identify its users correctly to network services. Kerberos provides an alternative approach whereby a trusted third-party authentication service is used to verify users’ identities. This paper gives an overview of the Kerberos authentication model as implemented for MIT’s Project Athena. It describes the protocols used by clients, servers, and Kerberos to achieve authentication. It also describes the management and replication of the database required. The views of Kerberos as seen by the user, programmer, and administrator are described. Finally, the role of Kerberos in the larger Athena picture is given, along with a list of applications that presently use Kerberos for user authentication. We describe the addition of Kerberos authentication to the Sun Network File System as a case study for integrating Kerberos with an existing application.
