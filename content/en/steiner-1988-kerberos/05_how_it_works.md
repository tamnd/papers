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
section: "4"
section_title: How It Works
tag: "0801"
kind: section
lang: en
source: http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.112.9002
pdf_sha256: 2dd6604c96afde95681d25fe32df9834aad32274d1bdbb44dd5f69d6b9660f59
pdf_pages: 5-7
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: e3eb060b50defde07586f7a9b0232bdbda1c4453bb980bc65d718af75df93a6f
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

This section describes the Kerberos authentication protocols. The following abbreviations are used in the figures.

| c | -> | client |
| --- | --- | --- |
| s | -> | server |
| addr | -> | client’s network address |
| life | -> | lifetime of ticket |
| tgs, TGS | -> | ticket-granting server |
| Kerberos | -> | authentication server |
| KDBM | -> | administration server |
| $K_{x}$ | -> | x’s private key |
| $K_{x,y}$ | -> | session key for x and y |
| {abc}$K_{x}$ | -> | abc encrypted in x’s key |
| $T_{x,y}$ | -> | x’s ticket to use y |
| $A_{x}$ | -> | authenticator for x |
| WS | -> | workstation |

As mentioned above, the Kerberos authentication model is based on the Needham and Schroeder key distribution protocol. When a user requests a service, her/his identity must be established. To do this, a ticket is presented to the server, along with proof that the ticket was originally issued to the user, not stolen. There are three phases to authentication through Kerberos. In the first phase, the user obtains credentials to be used to request access to other services. In the second phase, the user requests authentication for a specific service. In the final phase, the user presents those credentials to the end server.

### 4.1. Credentials {#steiner-1988-kerberos-s4-1 .section tag=0802}

There are two types of credentials used in the Kerberos authentication model: tickets and authenticators. Both are based on private key encryption, but they are encrypted using different keys. A ticket is used to securely pass the identity of the person to whom the ticket was issued between the authentication server and the end server. A ticket also passes information that can be used to make sure that the person using the ticket is the same person to which it was issued. The authenticator contains the additional information which, when compared against that in the ticket proves that the client presenting the ticket is the same one to which the ticket was issued.

A ticket is good for a single server and a single client. It contains the name of the server, the name of the client, the Internet address of the client, a timestamp, a lifetime, and a random session key. This information is encrypted using the key of the server for which the ticket will be used. Once the ticket has been issued, it may be used multiple times by the named client to gain access to the named server, until the ticket expires. Note that because the ticket is encrypted in the key of the server, it is safe to allow the user to pass the ticket on to the server without having to worry about the user modifying the ticket (see Figure 3).

$$
\{s, c, \text{addr}, \text{timestamp}, \text{life}, K_{s,c}\}K_s
$$

Figure 3. A Kerberos Ticket. {#steiner-1988-kerberos-fig-3 .figure tag=0803}

Unlike the ticket, the authenticator can only be used once. A new one must be generated each time a client wants to use a service. This does not present a problem because the client is able to build the authenticator itself. An authenticator contains the name of the client, the workstation’s IP address, and the current workstation time. The authenticator is encrypted in the session key that is part of the ticket (see Figure 4).

\{c, addr, timestamp\}K_{s,c}

Figure 4. A Kerberos Authenticator. {#steiner-1988-kerberos-fig-4 .figure tag=0804}

### 4.2. Getting the Initial Ticket {#steiner-1988-kerberos-s4-2 .section tag=0805}

When the user walks up to a workstation, only one piece of information can prove her/his identity: the user’s password. The initial exchange with the authentication server is designed to minimize the chance that the password will be compromised, while at the same time not allowing a user to properly authenticate her/himself without knowledge of that password. The process of logging in appears to the user to be the same as logging in to a timesharing system. Behind the scenes, though, it is quite different (see Figure 5).

Figure.

Figure 5. Getting the Initial Ticket. {#steiner-1988-kerberos-fig-5 .figure tag=0806}

The user is prompted for her/his username. Once it has been entered, a request is sent to the authentication server containing the user’s name and the name of a special service known as the ticket-granting service.

The authentication server checks that it knows about the client. If so, it generates a random session key which will later be used between the client and the ticket-granting server. It then creates a ticket for the ticket-granting server which contains the client’s name, the name of the ticket-granting server, the current time, a lifetime for the ticket, the client’s IP address, and the random session key just created. This is all encrypted in a key known only to the ticket-granting server and the authentication server.

The authentication server then sends the ticket, along with a copy of the random session key and some additional information, back to the client. This response is encrypted in the client’s private key, known only to Kerberos and the client, which is derived from the user’s password.

Once the response has been received by the client, the user is asked for her/his password. The password is converted to a DES key and used to decrypt the response from the authentication server. The ticket and the session key, along with some of the other information, are stored for future use, and the user’s password and DES key are erased from memory.

Once the exchange has been completed, the workstation possesses information that it can use to prove the identity of its user for the lifetime of the ticket-granting ticket. As long as the software on the workstation had not been previously tampered with, no information exists that will allow someone else to impersonate the user beyond the life of the ticket.

### 4.3. Requesting a Service {#steiner-1988-kerberos-s4-3 .section tag=0807}

For the moment, let us pretend that the user already has a ticket for the desired server. In order to gain access to the server, the application builds an authenticator containing the client’s name and IP address, and the current time. The authenticator is then encrypted in the session key that was received with the ticket for the server. The client then sends the authenticator along with the ticket to the server in a manner defined by the individual application.

Once the authenticator and ticket have been received by the server, the server decrypts the ticket, uses the session key included in the ticket to decrypt the authenticator, compares the information in the ticket with that in the authenticator, the IP address from which the request was received, and the present time. If everything matches, it allows the request to proceed (see Figure 6).

Figure.

Figure 6. Requesting a Service. {#steiner-1988-kerberos-fig-6 .figure tag=0808}

It is assumed that clocks are synchronized to within several minutes. If the time in the request is too far in the future or the past, the server treats the request as an attempt to replay a previous request. The server is also allowed to keep track of all past requests with timestamps that are still valid. In order to further foil replay attacks, a request received with the same ticket and timestamp as one already received can be discarded.

Finally, if the client specifies that it wants the server to prove its identity too, the server adds one to the timestamp the client sent in the authenticator, encrypts the result in the session key, and sends the result back to the client (see Figure 7).

Figure.

Figure 7. Mutual Authentication. {#steiner-1988-kerberos-fig-7 .figure tag=0809}

At the end of this exchange, the server is certain that, according to Kerberos, the client is who it says it is. If mutual authentication occurs, the client is also convinced that the server is authentic. Moreover, the client and server share a key which no one else knows, and can safely assume that a reasonably recent message encrypted in that key originated with the other party.

### 4.4. Getting Server Tickets {#steiner-1988-kerberos-s4-4 .section tag=080A}

Recall that a ticket is only good for a single server. As such, it is necessary to obtain a separate ticket for each service the client wants to use. Tickets for individual servers can be obtained from the ticket-granting service. Since the ticket-granting service is itself a service, it makes use of the service access protocol described in the previous section.

When a program requires a ticket that has not already been requested, it sends a request to the ticket-granting server (see Figure 8). The request contains the name of the server for which a ticket is requested, along with the ticket-granting ticket and an authenticator built as described in the previous section.

Figure.

Figure 8. Getting a Server Ticket. {#steiner-1988-kerberos-fig-8 .figure tag=080B}

The ticket-granting server then checks the authenticator and ticket-granting ticket as described above. If valid, the ticket-granting server generates a new random session key to be used between the client and the new server. It then builds a ticket for the new server containing the client’s name, the server name, the current time, the client’s IP address and the new session key it just generated. The lifetime of the new ticket is the minimum of the remaining life for the ticket-granting ticket and the default for the service.

The ticket-granting server then sends the ticket, along with the session key and other information, back to the client. This time, however, the reply is encrypted in the session key that was part of the ticket-granting ticket. This way, there is no need for the user to enter her/his password again. Figure 9 summarizes the authentication protocols.

Figure.

1. Request for TGS ticket
2. Ticket for TGS
3. Request for Server ticket
4. Ticket for Server
5. Request for service

Figure 9. Kerberos Authentication Protocols. {#steiner-1988-kerberos-fig-9 .figure tag=080C}
