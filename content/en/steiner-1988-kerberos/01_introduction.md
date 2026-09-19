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
section_title: Introduction
kind: section
lang: en
source: http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.112.9002
pdf_sha256: 2dd6604c96afde95681d25fe32df9834aad32274d1bdbb44dd5f69d6b9660f59
pdf_pages: 1-2
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 1f56ea98dd6caf0c868759fc63ac6999859f1bf9b9b9ea872f9845f9df9dc203
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

This paper gives an overview of Kerberos, an authentication system designed by Miller and Neuman¹ for open network computing environments, and describes our experience using it at MIT’s Project Athena.² In the first section of the paper, we explain why a new authentication model is needed for open networks, and what its requirements are. The second section lists the components of the Kerberos software and describes how they interact in providing the authentication service. In Section 3, we describe the Kerberos naming scheme.

Section 4 presents the building blocks of

† Clifford Neuman was a member of the Project Athena staff during the design and initial implementation phase of Kerberos.

March 30, 1988

Kerberos authentication – the ticket and the authenticator. This leads to a discussion of the two authentication protocols: the initial authentication of a user to Kerberos (analogous to logging in), and the protocol for mutual authentication of a potential consumer and a potential producer of a network service.

Kerberos requires a database of information about its clients; Section 5 describes the database, its management, and the protocol for its modification. Section 6 describes the Kerberos interface to its users, applications programmers, and administrators. In Section 7, we describe how the Project Athena Kerberos fits into the rest of the Athena environment. We also describe the interaction of different Kerberos authentication domains, or realms; in our case, the relation between the Project Athena Kerberos and the Kerberos running at MIT’s Laboratory for Computer Science.

In Section 8, we mention open issues and problems as yet unsolved. The last section gives the current status of Kerberos at Project Athena. In the appendix, we describe in detail how Kerberos is applied to a network file service to authenticate users who wish to gain access to remote file systems.

Conventions. Throughout this paper we use terms that may be ambiguous, new to the reader, or used differently elsewhere. Below we state our use of those terms.

User, Client, Server. By user, we mean a human being who uses a program or service. A client also uses something, but is not necessarily a person; it can be a program. Often network applications consist of two parts; one program which runs on one machine and requests a remote service, and another program which runs on the remote machine and performs that service. We call those the client side and server side of the application, respectively. Often, a client will contact a server on behalf of a user.

Each entity that uses the Kerberos system, be it a user or a network server, is in one sense a client, since it uses the Kerberos service. So to distinguish Kerberos clients from clients of other services, we use the term principal to indicate such an entity. Note that a Kerberos principal can be either a user or a server. (We describe the naming of Kerberos principals in a later section.)

Service vs. Server. We use service as an abstract specification of some actions to be performed. A process which performs those actions is called a server. At a given time, there may be several servers (usually running on different machines) performing a given service. For example, at Athena there is one BSD UNIX rlogin server running on each of our timesharing machines.

Key, Private Key, Password. Kerberos uses private key encryption. Each Kerberos principal is assigned a large number, its private key, known only to that principal and Kerberos. In the case of a user, the private key is the result of a one-way function applied to the user’s password. We use key as shorthand for private key.

Credentials. Unfortunately, this word has a special meaning for both the Sun Network File System and the Kerberos system. We explicitly state whether we mean NFS credentials or Kerberos credentials, otherwise the term is used in the normal English language sense.

Master and Slave. It is possible to run Kerberos authentication software on more than one machine. However, there is always only one definitive copy of the Kerberos database. The machine which houses this database is called the master machine, or just the master. Other machines may possess read-only copies of the Kerberos database, and these are called slaves.
