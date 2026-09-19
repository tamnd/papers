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
section: "6"
section_title: Kerberos From the Outside Looking In
tag: "0815"
kind: section
lang: en
source: http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.112.9002
pdf_sha256: 2dd6604c96afde95681d25fe32df9834aad32274d1bdbb44dd5f69d6b9660f59
pdf_pages: 9-10
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 34d8338e62bee2d929db1393da3cdc2901366c01a7f80e6c83e4b57c7ca2b0f0
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The section will describe Kerberos from the practical point of view, first as seen by the user, then from the application programmer’s viewpoint, and finally, through the tasks of the Kerberos administrator.

### 6.1. User’s Eye View {#steiner-1988-kerberos-s6-1 .section tag=0816}

If all goes well, the user will hardly notice that Kerberos is present. In our UNIX implementation, the ticket-granting ticket is obtained from Kerberos as part of the login process. The changing of a user’s Kerberos password is part of the passwd program. And Kerberos tickets are automatically destroyed when a user logs out.

If the user’s login session lasts longer than the lifetime of the ticket-granting ticket (currently 8 hours), the user will notice Kerberos’ presence because the next time a Kerberos-authenticated application is executed, it will fail. The Kerberos ticket for it will have expired. At that point, the user can run the kinit program to obtain a new ticket for the ticket-granting server. As when logging in, a password must be provided in order to get it. A user executing the klist command out of curiosity may be surprised at all the tickets which have silently been obtained on her/his behalf for services which require Kerberos authentication.

### 6.2. From the Programmer’s Viewpoint {#steiner-1988-kerberos-s6-2 .section tag=0817}

A programmer writing a Kerberos application will often be adding authentication to an already existing network application consisting of a client and server side. We call this process “Kerberizing” a program. Kerberizing usually involves making a call to the Kerberos library in order to perform authentication at the initial request for service. It may also involve calls to the DES library to encrypt messages and data which are subsequently sent between application client and application server.

The most commonly used library functions are krb_mk_req on the client side, and krb_rd_req on the server side. The krb_mk_req routine takes as parameters the name, instance, and realm of the target server, which will be requested, and possibly a checksum of the data to be sent. The client then sends the message returned by the krb_mk_req call over the network to the server side of the application. When the server receives this message, it makes a call to the library routine krb_rd_req. The routine returns a judgement about the authenticity of the sender’s alleged identity.

If the application requires that messages sent between client and server be secret, then library calls can be made to krb_mk_priv (krb_rd_priv) to encrypt (decrypt) messages in the session key which both sides now share.7

### 6.3. The Kerberos Administrator’s Job {#steiner-1988-kerberos-s6-3 .section tag=0818}

The Kerberos administrator’s job begins with running a program to initialize the database. Another program must be run to register essential principals in the database, such as the Kerberos administrator’s name with an admin instance. The Kerberos authentication server and the administration server must be started up. If there are slave databases, the administrator must arrange that the programs to propagate database updates from master to slaves be kicked off periodically.

After these initial steps have been taken, the administrator manipulates the database over the network, using the kadmin program. Through that program, new principals can be added, and passwords can be changed.

In particular, when a new Kerberos application is added to the system, the Kerberos administrator must take a few steps to get it working. The server must be registered in the database, and assigned a private key (usually this is an automatically generated random key). Then, some data (including the server’s key) must be extracted from the database and installed in a file on the server’s machine. The default file is /etc/srvtab. The krb_rd_req library routine called by the server (see the previous section) uses the information in that file to decrypt messages sent encrypted in the server’s private key. The /etc/srvtab file authenticates the server as a password typed at a terminal authenticates the user.

The Kerberos administrator must also ensure that Kerberos machines are physically secure, and would also be wise to maintain backups of the Master database.8
