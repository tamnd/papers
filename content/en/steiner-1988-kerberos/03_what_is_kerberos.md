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
section: "2"
section_title: What is Kerberos?
tag: "0495"
kind: section
lang: en
source: http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.112.9002
pdf_sha256: 2dd6604c96afde95681d25fe32df9834aad32274d1bdbb44dd5f69d6b9660f59
pdf_pages: 3-4
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 52666252097d027ee4b845a8cb3f731106b80f35f274ad18b133d06a577f6a02
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Kerberos is a trusted third-party authentication service based on the model presented by Needham and Schroeder.3 It is trusted in the sense that each of its clients believes Kerberos’ judgement as to the identity of each of its other clients to be accurate. Timestamps (large numbers representing the current date and time) have been added to the original model to aid in the detection of replay. Replay occurs when a message is stolen off the network and resent later. For a more complete description of replay, and other issues of authentication, see Voydock and Kent.4

### 2.1. What Does It Do? {#steiner-1988-kerberos-s2-1 .section tag=0496}

Kerberos keeps a database of its clients and their private keys. The private key is a large number known only to Kerberos and the client it belongs to. In the case that the client is a user, it is an encrypted password. Network services requiring authentication register with Kerberos, as do clients wishing to use those services. The private keys are negotiated at registration.

Because Kerberos knows these private keys, it can create messages which convince one client that another is really who it claims to be. Kerberos also generates temporary private keys, called session keys, which are given to two clients and no one else. A session key can be used to encrypt messages between two parties.

Kerberos provides three distinct levels of protection. The application programmer determines which is appropriate, according to the requirements of the application. For example, some applications require only that authenticity be established at the initiation of a network connection, and can assume that further messages from a given network address originate from the authenticated party. Our authenticated network file system uses this level of security.

Other applications require authentication of each message, but do not care whether the content of the message is disclosed or not. For these,

Kerberos provides safe messages. Yet a higher level of security is provided by private messages, where each message is not only authenticated, but also encrypted. Private messages are used, for example, by the Kerberos server itself for sending passwords over the network.

### 2.2. Software Components {#steiner-1988-kerberos-s2-2 .section tag=07FD}

The Athena implementation comprises several modules (see Figure 1). The Kerberos applications library provides an interface for application clients and application servers. It contains, among others, routines for creating or reading authentication requests, and the routines for creating safe or private messages.

• Kerberos applications library
• encryption library
• database library
• database administration programs
• administration server
• authentication server
• db propagation software
• user programs
• applications

Figure 1. Kerberos Software Components. {#steiner-1988-kerberos-fig-1 .figure tag=07FE}

Encryption in Kerberos is based on DES, the Data Encryption Standard.5 The encryption library implements those routines. Several methods of encryption are provided, with trade-offs between speed and security. An extension to the DES Cypher Block Chaining (CBC) mode, called the Propagating CBC mode, is also provided. In CBC, an error is propagated only through the current block of the cipher, whereas in PCBC, the error is propagated throughout the message. This renders the entire message useless if an error occurs, rather than just a portion of it. The encryption library is an independent module, and may be replaced with other DES implementations or a different encryption library.

Another replaceable module is the database management system. The current Athena implementation of the database library uses ndbm, although Ingres was originally used. Other database management libraries could be used as well.

The Kerberos database needs are straightforward; a record is held for each principal, containing the name, private key, and expiration date of the principal, along with some administrative information. (The expiration date is the date after which an entry is no longer valid. It is usually set to a few years into the future at registration.)

Other user information, such as real name, phone number, and so forth, is kept by another server, the Hesiod nameserver.6 This way, sensitive information, namely passwords, can be handled by Kerberos, using fairly high security measures; while the non-sensitive information kept by Hesiod is dealt with differently; it can, for example, be sent unencrypted over the network.

The Kerberos servers use the database library, as do the tools for administering the database.

The administration server (or KDBM server) provides a read-write network interface to the database. The client side of the program may be run on any machine on the network. The server side, however, must run on the machine housing the Kerberos database in order to make changes to the database.

The authentication server (or Kerberos server), on the other hand, performs read-only operations on the Kerberos database, namely, the authentication of principals, and generation of session keys. Since this server does not modify the Kerberos database, it may run on a machine housing a read-only copy of the master Kerberos database.

Database propagation software manages replication of the Kerberos database. It is possible to have copies of the database on several different machines, with a copy of the authentication server running on each machine. Each of these slave machines receives an update of the Kerberos database from the master machine at given intervals.

Finally, there are end-user programs for logging in to Kerberos, changing a Kerberos password, and displaying or destroying Kerberos tickets (tickets are explained later on).
