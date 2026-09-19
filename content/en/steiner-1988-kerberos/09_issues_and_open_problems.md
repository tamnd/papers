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
section: "8"
section_title: Issues and Open Problems
tag: 081C
kind: section
lang: en
source: http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.112.9002
pdf_sha256: 2dd6604c96afde95681d25fe32df9834aad32274d1bdbb44dd5f69d6b9660f59
pdf_pages: 11-12
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: ffe41f82eeed7791e46caafaa99c5ce320ad4528fb5c72052fdb7c9912192189
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

There are a number of issues and open problems associated with the Kerberos authentication mechanism. Among the issues are how to decide the correct lifetime for a ticket, how to allow proxies, and how to guarantee workstation integrity.

The ticket lifetime problem is a matter of choosing the proper tradeoff between security and convenience. If the life of a ticket is long, then if a ticket and its associated session key are stolen or misplaced, they can be used for a longer period of time. Such information can be stolen if a user forgets to log out of a public workstation. Alternatively, if a user has been authenticated on a system that allows multiple users, another user with access to root might be able to find the information needed to use stolen tickets. The problem with giving a ticket a short lifetime, however, is that when it expires, the user will have to obtain a new one which requires the user to enter the password again.

An open problem is the proxy problem. How can an authenticated user allow a server to acquire other network services on her/his behalf? An example where this would be important is the use of a service that will gain access to protected files directly from a fileserver. Another example of this problem is what we call authentication forwarding. If a user is logged into a workstation and logs in to a remote host, it would be nice if the user had access to the same services available locally, while running a program on the remote host. What makes this difficult is that the user might not trust the remote host, thus authentication forwarding is not desirable in all cases. We do not presently have a solution to this problem.

Another problem, and one that is important in the Athena environment, is how to guarantee the integrity of the software running on a workstation. This is not so much of a problem on private workstations since the user that will be using it has control over it. On public workstations, however, someone might have come along and modified the login program to save the user’s password. The only solution presently available in our environment is to make it difficult for people to modify software running on the public workstations. A better solution would require that the user’s key never leave a system that the user knows can be trusted. One way this could be done would be if the user possessed a smartcard capable of doing the encryptions required in the authentication protocol.
