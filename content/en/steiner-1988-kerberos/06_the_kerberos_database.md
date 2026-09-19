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
section: "5"
section_title: The Kerberos Database
tag: 080D
kind: section
lang: en
source: http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.112.9002
pdf_sha256: 2dd6604c96afde95681d25fe32df9834aad32274d1bdbb44dd5f69d6b9660f59
pdf_pages: 7-9
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 7f5ff986f6fad3013abbb303f3bbe60e06d1ccdbe8d4f6712caa0378ae2c0021
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Up to this point, we have discussed operations requiring read-only access to the Kerberos database. These operations are performed by the authentication service, which can run on both master and slave machines (see Figure 10).

### 5.1. The KDBM Server {#steiner-1988-kerberos-s5-1 .section tag=080E}

The KDBM server accepts requests to add principals to the database or change the passwords for existing principals. This service is unique in that the ticket-granting service will not issue tickets for it. Instead, the authentication service itself must be used (the same service that is used to get a ticket-granting ticket). The purpose of this is to require the user to enter a password. If this were not so, then if a user left her/his workstation unattended, a passerby could walk up and change her/his password for them, something which should be prevented. Likewise, if an administrator left her/his workstation unguarded, a passerby could change any password in the system.

When the KDBM server receives a request, it authorizes it by comparing the authenticated principal name of the requester of the change to the principal name of the target of the request. If they are the same, the request is permitted. If they are not the same, the KDBM server consults an access control list (stored in a file on the master Kerberos system). If the requester’s principal name is found in this file, the request is permitted, otherwise it is denied.

By convention, names with a NULL instance (the default instance) do not appear in the access control list file; instead, an admin instance is used. Therefore, for a user to become an administrator of Kerberos an admin instance for that username must be created, and added to the access control list. This convention allows an administrator to use a different password for Kerberos administration then s/he would use for normal login.

All requests to the KDBM program, whether permitted or denied, are logged.

### 5.2. The kadmin and kpasswd Programs {#steiner-1988-kerberos-s5-2 .section tag=080F}

Administrators of Kerberos use the kadmin program to add principals to the database, or change the passwords of existing principals. An administrator is required to enter the password for their admin instance name when they invoke the kadmin program. This password is used to fetch a ticket for the KDBM server (see Figure 12).

Figure 10. Authentication Requests. {#steiner-1988-kerberos-fig-10 .figure tag=0810}

In this section, we discuss operations that require write access to the database. These operations are performed by the administration service, called the Kerberos Database Management Service (KDBM). The current implementation stipulates that changes may only be made to the master Kerberos database; slave copies are read-only. Therefore, the KDBM server may only run on the master Kerberos machine (see Figure 11).

Figure 11. Administration Requests. {#steiner-1988-kerberos-fig-11 .figure tag=0811}

Note that, while authentication can still occur (on slaves), administration requests cannot be serviced if the master machine is down. In our experience, this has not presented a problem, as administration requests are infrequent.

The KDBM handles requests from users to change their passwords. The client side of this program, which sends requests to the KDBM over the network, is the kpasswd program. The KDBM also accepts requests from Kerberos administrators, who may add principals to the database, as well as change passwords for existing principals. The client side of the administration program, which also sends requests to the KDBM over the network, is the kadmin program.

and if it matches the checksum sent by the master, the new information is used to update the slave’s database.

Figure.

Figure 12. Kerberos Administration Protocol. {#steiner-1988-kerberos-fig-12 .figure tag=0812}

Users may change their Kerberos passwords using the kpasswd program. They are required to enter their old password when they invoke the program. This password is used to fetch a ticket for the KDBM server.

### 5.3. Database Replication {#steiner-1988-kerberos-s5-3 .section tag=0813}

Each Kerberos realm has a master Kerberos machine, which houses the master copy of the authentication database. It is possible (although not necessary) to have additional, read-only copies of the database on slave machines elsewhere in the system. The advantages of having multiple copies of the database are those usually cited for replication: higher availability and better performance. If the master machine is down, authentication can still be achieved on one of the slave machines. The ability to perform authentication on any one of several machines reduces the probability of a bottleneck at the master machine.

Keeping multiple copies of the database introduces the problem of data consistency. We have found that very simple methods suffice for dealing with inconsistency. The master database is dumped every hour. The database is sent, in its entirety, to the slave machines, which then update their own databases. A program on the master host, called kprop, sends the update to a peer program, called kpropd, running on each of the slave machines (see Figure 13). First kprop sends a checksum of the new database it is about to send. The checksum is encrypted in the Kerberos master database key, which both the master and slave Kerberos machines possess. The data is then transferred over the network to the kpropd on the slave machine. The slave propagation server calculates a checksum of the data it has received,

Figure.

Figure 13. Database Propagation. {#steiner-1988-kerberos-fig-13 .figure tag=0814}

All passwords in the Kerberos database are encrypted in the master database key Therefore, the information passed from master to slave over the network is not useful to an eavesdropper. However, it is essential that only information from the master host be accepted by the slaves, and that tampering of data be detected, thus the checksum.
