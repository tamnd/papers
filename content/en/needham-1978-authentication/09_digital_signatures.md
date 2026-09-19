---
paper: needham-1978-authentication
title: Using Encryption for Authentication in Large Networks of Computers
authors:
  - Roger M. Needham
  - Michael D. Schroeder
year: 1978
venue: Communications of the ACM
field: security
section: "8"
section_title: Digital Signatures
tag: 032D
kind: section
lang: en
source: https://web.archive.org/web/20250531153030id_/https://dl.acm.org/doi/pdf/10.1145/359657.359659
pdf_sha256: 6fec623eab036ce7683fc0d35286988cb721593962c842b1360d981fff49d11e
pdf_pages: 5-6
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 170273461ccc63ed9d7a14bbb38b3d9bf79a9ab5130e32c425a2f37440833b2c
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The previous protocols are designed to authenticate each communicant to the other. It is sometimes necessary to provide evidence to a third party that a particular communication is exactly as received from a particular sender. This requirement is met by signatures on paper documents. A common example is instructions from a superior to do something; the recipient needs to retain them as evidence that his actions were proper. To produce the analog of signed documents with messages, it is necessary that the recipient could not alter a signed text undetected and that the sender cannot credibly disclaim it. The ability to provide digital signatures depends upon there being something the originator can do which the recipient cannot.

Protocol 3. Signatures with Conventional Encryption and a Little Help.

One method uses a characteristic function of the cleartext message that is to be signed. The characteristic function must have the property that, given the cleartext message, the function, and the resulting characteristic value, it is hard to find another sensible cleartext message that produces the same characteristic value. It also is useful if the characteristic value is noticeably smaller than the cleartext message. Hard-to-invert transformations of the sort used to protect passwords [8] is a class of functions with the required properties.

While sending the text, say using the interactive or mail protocols described earlier, $A$ computes the characteristic value $CS$. He then requests a signature block from the authentication server:

$$
A \rightarrow AS: \quad A, \{CS\}^{KA}
$$

which the server supplies:

$$
AS \rightarrow A: \quad \{A, CS\}^{KAS}
$$

Message 3.2 is encrypted with $AS$'s key and therefore is accessible only to $AS$. Note that $A$ cannot validate the message, but if it has been interfered with, then $B$ subsequently will be unable to validate the signature, which he likely will do anyway before acting on the message if it contains instructions worthy of signature. $A$ sends the signature block to $B$ following the text to be signed.

On receipt $B$ first decrypts the text and computes its characteristic value, $CSC$. $B$ then communicates the signature block to the authentication server for decryption:

$$
B \rightarrow AS: \quad B, \{A, CS\}^{KAS}
$$

The server decrypts the signature block and returns its contents to $B$:

$$
AS \rightarrow B: \quad \{A, CS\}^{KB}
$$

If the returned $CS$ matches $CSC$, then the principal named in (3.4) is the sender of the signed text. $CSC$ not matching $CS$ could mean that any of the steps (3.1)-(3.3), or the association of the signature block with the signed text, has been interfered with. Earlier detection of certain types of interference is possible by using nonce identifiers in transactions (3.1)-(3.2) and (3.3)-(3.4). If $B$ wishes to retain the text as evidence, all he has to do is to retain the signature block and the text itself. In response to a challenge $B$ would produce the text and the signature block for an arbiter who would go through the communication of steps (3.3) and (3.4).

The extension of protocol 3 to the case of multiple authentication servers is straightforward.

Signatures with Public-Key Encryption

It is possible to provide signed text with a public-key system using a characteristic function as above. The public key system, however, provides another, more elegant, method that was first described by Diffie and Hellman. The first steps are for $A$ to find out $B$'s public key from cache or server, as before. The successive blocks of text, seriated for time integrity, are doubly encrypted:

$$
A \rightarrow B: \quad \{\{text-block\}^{SKA}\}^{PKB}
$$

$B$ can carry out the first decryption because of knowing $SKB$, and the second because of being able to find out $PKA$ by protocol exchange or from a cache. There is a need for header information to convey securely the identity of the originator so that $PKA$ can be correctly sought. $B$ is in no position to alter the content, since $SKA$ is not available to him. When challenged, $B$ simply performs the outer decryption on the whole text and passes the result to the arbiter who can use $PKA$ to finish the job. Note that the ability of an arbiter to perform his function seems to depend on $A$ not changing his key pair. Since such changes must be allowed as the only response to a key being compromised, it is necessary for the authentication server to retain a record of the old public keys of its principals and the time of the change, and for signed texts to contain the time that they were signed. An advantage of the signature protocol for conventional encryption algorithms is that an authentication server only need retain a record of changes to its own key to guarantee correct future arbitration.
