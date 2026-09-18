---
paper: needham-1978-authentication
title: Using Encryption for Authentication in Large Networks of Computers
authors:
  - Roger M. Needham
  - Michael D. Schroeder
year: 1978
venue: Communications of the ACM
field: security
section: "4"
section_title: Protocols for Establishing Interactive Connections
tag: "0329"
kind: section
lang: en
source: https://web.archive.org/web/20250531153030id_/https://dl.acm.org/doi/pdf/10.1145/359657.359659
pdf_sha256: 6fec623eab036ce7683fc0d35286988cb721593962c842b1360d981fff49d11e
pdf_pages: 2-4
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 1dfe42a209fc42d58dcf629669aab79ad6e07cc6a9463291ff0be5fdb244162a
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Protocol 1. With Conventional Algorithms

If a conventional algorithm is used then each principal has a secret key that is known only to itself and to its authentication server, the contents of which are accordingly secret. The essential step in setting up secure communication between $A$ and $B$ is for the initiator, say $A$, to generate a message with two properties:
(a) It must be comprehensible only to $B$, i.e. allow only $B$ to use its contents to identify himself to $A$.
(b) It must be evident to $B$ that it originated with $A$.
The use of encryption to achieve these properties was first described by Feistel [4] and applied to a network context by Branstad [1].

Assuming for the moment that $A$ and $B$ are in the purview of the same authentication server $AS$, we now outline a protocol. The notation used will be followed throughout: encryption is indicated by braces that are superscripted with the key used.

The protocol opens with $A$ communicating in clear to $AS$ his own claimed identity and the identity of the desired correspondent, $B$, together with $A$'s nonce identifier for this transaction, $I_{A1}$. ("Nonce" means "used only once.") Here the nonce identifier must be different than others used by $A$ in previous messages of the same type. The first message of the protocol is:

$$
A \rightarrow AS: \quad A, B, I_{A1}
$$

Upon receiving message (1.1), $AS$ looks up the secret, identifying keys of both parties and also computes a new key $CK$ that will be the key for the conversation if all goes well.$^2$ The next transaction is a rather complicated message from $AS$ to $A$:

$$
AS \rightarrow A: \quad \{I_{A1}, B, CK, \{CK, A\}^{KB}\}^{KA}
$$

where $KA$ and $KB$ are $A$'s and $B$'s secret, identifying keys. Because (1.2) is encrypted with $A$'s secret key, only $A$ can decrypt it and discover the conversation key $CK$. Following decryption, $A$ checks for the presence of the intended recipient's name, $B$, and the correct identifier, $I_{A1}$, in order to verify that the message really is a reply by $AS$ to the current enquiry. Both the name of the intended recipient and the transaction identifier must appear in message (1.2). If the recipient's name is left out, then an intruder could change that name in message (1.1), say to $X$, before $AS$ receives it, with the subsequent result that $A$ would unknowingly communicate with $X$ instead of $B$. If the identifier is left out, then an intruder could substitute a previously recorded message (1.2) (from $AS$ to $A$ about $B$) and force $A$ to reuse a previous conversation key.$^3$ $A$ remembers $CK$ and sends the part encrypted with $KB$ to $B$:

$$
A \rightarrow B: \quad \{CK, A\}^{KB}
$$

The real $B$, but no other, will be able to decrypt message (1.3) and emerge with the conversation key $CK$, the same as $A$ has. $B$ also knows the identity of the intending correspondent, as authenticated by $AS$.

It is worth reviewing at this point the state of knowledge of the two parties. $A$ now knows that any communication he receives encrypted with $CK$ must have originated with $B$, and also that any communication he emits with $CK$ encryption will be understood only by $B$. Both are known because the only messages containing $CK$ that have ever been sent are tied to $A$'s and $B$'s secret keys. $B$ is in a similar state, mutatis mutandis. It is important, however, to be sure that no part of the protocol exchange or ensuing conversation is being replayed by an intruder from a recording of a previous conversation between $A$ and $B$. In relationship to this question the positions of $A$ and $B$ differ. $A$ is aware that he has not used the key $CK$ before and therefore has no reason to fear that material encrypted with it is other than the legitimate responses from $B$. $B$'s position is not so good; unless he remembers indefinitely keys previously used by $A$ in order to check that $CK$ is new, he is unclear that the message (1.3) and the subsequent messages supposedly from $A$ are not being replayed. To guard against this possibility, $B$ generates a nonce identifier for the transaction, $I_B$, and sends it to $A$ under $CK$:

$$
B \rightarrow A: \quad \{I_B\}^{CK}
$$

expecting a related reply, say one less:

$$
A \rightarrow B: \quad \{I_B - 1\}^{CK}
$$

If this reply is satisfactorily received, then the mutual confidence is sufficient to enable substantive communication, encrypted with $CK$, to begin.

There are five messages in protocol 1. The number may be reduced to three by $A$'s keeping, for regular interaction partners, a cache of items of the form $B: CK, \{CK, A\}^{KB}$ derived from message (1.2), thus eliminating messages (1.1) and (1.2). Note however that, if such authenticators are cached, changes are needed to the protocol. With caching, the same $CK$ is being used again and again, so the conversation identifier handshakes need to be two-way, for example, by replacing steps (1.3) and (1.4) with:

$$
A \rightarrow B: \quad \{CK, A\}^{KB}, \{I_{A2}\}^{CK}
$$

$$
B \rightarrow A: \quad \{I_{A2} - 1, I_B\}^{CK}
$$

The change does not increase the number of protocol messages but does alter the content slightly. In practice, messages (1.3)-(1.5) would be used to start a two-way seriation in order to ensure the integrity of the subsequent conversation. Methods for ensuring integrity following initial contact have been studied by Kent [5].

Protocol 2. With Public-Key Algorithms

We use key labels such as $PKA$ for $A$'s public key and $SKA$ for his secret one. The exchange opens with $A$ consulting the authentication server in the clear to find $B$'s public key.

$$
A \rightarrow AS: \quad A, B
$$

$AS$ responds with:

$$
AS \rightarrow A: \quad \{PKB, B\}^{SKAS}
$$

where $SKAS$ is the authentication server's secret key. $A$ is presumed to know the $AS$'s public key, $PKAS$, which is used to decrypt the message. $A$ must obtain and store $PKAS$ in a reliable way, so he is sure it is correct. If an

\footnotetext{
2 The new key must be unpredictable and should never have been used before.
3 Also note that messages (1.1) and (1.2) together, and others in our protocols, make available known plaintext encrypted with a principal's identifying key. If there is concern about cryptanalytic attack based on known plaintext being used to expose an identifying key, then an additional temporary key $TK$ may be used where appropriate throughout, so that $\{X\}^{KA}$ becomes $\{TK\}^{KA}\{X\}^{TK}$.
} intruder somehow could provide an arbitrary value that $A$ thinks is $PKAS$, then that intruder could impersonate $AS$.

The importance of the reciprocity between the public and secret keys is shown here. Encryption of message (2.2) is required not to ensure the *privacy* of the information but to ensure its *integrity*. It is important that $A$ should be sure that he is getting $PKB$ rather than the public key of some miscreant. $A$ knows that the name of the intended recipient, $B$, was correctly communicated to $AS$ because that name is returned in message (2.2).

The next step is for the communication with $B$ to be initiated:

$$
A \rightarrow B: \quad \{I_A, A\}^{PKB}
$$

This message, which can only be understood by $B$, indicates that someone purporting to be $A$ wishes to establish communication, and secretly communicates a nonce identifier, $I_A$, generated by $A$. $B$ decrypts the message with his secret key and then finds $PKA$ with steps similar to (2.1) and (2.2):

$$
B \rightarrow AS: \quad B, A
$$

$$
AS \rightarrow B: \quad \{PKA, A\}^{SKAS}
$$

Message (2.5) is encrypted for integrity, as was (2.2), not for secrecy. At this point a double handshake is needed to authenticate $A$ and $B$ to one another and to establish the time integrity of the conversation. The handshake is completed as steps (2.6) and (2.7):

$$
B \rightarrow A: \quad \{I_A, I_B\}^{PKA}
$$

$$
A \rightarrow B: \quad \{I_B\}^{PKB}
$$

There are thus seven steps in this protocol as against five with protocol 1, but four of them (2.1, 2.2, 2.4, and 2.5) can be done away with by $A$ and $B$ both having local caches of commonly used public keys. The resulting three protocol steps have very similar purposes to the three remaining after caching in protocol 1.

Observe that, because public keys are not secret, double encryption, i.e. $\{\{message\}^{SKA}\}^{PKB}$, or some equivalent is required during the course of the ensuing interaction. If the data were simply encrypted with the public key of the recipient, then anyone else could inject material into the stream. An equivalent safeguard is to use an arbitrary number from a large space as the base for seriation of encryption blocks. This number may be initialized as $I_A$ or $I_B$ according to direction. An intruder would have no way of knowing what was the correct serial to insert in a forged packet, even if he had counted previous packets, since he could not know the correct base. The more bits that are devoted to this redundant seriation the fewer good data bits we get per unit decryption effort.
