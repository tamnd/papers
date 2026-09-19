---
paper: rivest-1978-rsa
title: A Method for Obtaining Digital Signatures and Public-Key Cryptosystems
authors:
  - R. L. Rivest
  - A. Shamir
  - L. Adleman
year: 1978
venue: Communications of the ACM
field: security
section: IV
section_title: Signatures
tag: "0947"
kind: section
lang: en
source: https://doi.org/10.21236/ada606588
pdf_sha256: f7b1f78d9a7cbeb85e32b8c563a6db60771a5cc4bdc55580645f7cb778a4966b
pdf_pages: 4-6
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: a3dd78094d8dbd0c3f39df6ab870e4356d2df31ca8860cc770b36a377454f970
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

If electronic mail systems are to replace the existing paper mail system for business transactions, “signing” an electronic message must be possible. The recipient of a signed message has proof that the message originated from the sender. This quality is stronger than mere authentication (where the recipient can verify that the message came from the sender); the recipient can convince a “judge” that the signer sent the message. To do so, he must convince the judge that he did not forge the signed message himself! In an authentication problem the recipient does not worry about this possibility, since he only wants to satisfy *himself* that the message came from the sender.

An electronic signature must be *message*-dependent, as well as *signer*-dependent. Otherwise the recipient could modify the message before showing the message-signature pair to a judge. Or he could attach the signature to any message whatsoever, since it is impossible to detect electronic “cutting and pasting.”

To implement signatures the public-key cryptosystem must be implemented with trap-door one-way permutations (i.e. have property (d)), since the decryption algorithm will be applied to unenciphered messages.

How can user Bob send Alice a “signed” message $M$ in a public-key cryptosystem? He first computes his “signature” $S$ for the message $M$ using $D_B$:

$$
S = D_B(M)
$$

(Deciphering an unenciphered message “makes sense” by property (d) of a public-key cryptosystem: each message is the ciphertext for some other message.) He then encrypts $S$ using $E_A$ (for privacy), and sends the result $E_A(S)$ to Alice. He need not send $M$ as well; it can be computed from $S$.

Alice first decrypts the ciphertext with $D_A$ to obtain $S$. She knows who is the presumed sender of the signature (in this case, Bob); this can be given if necessary in plain text attached to $S$. She then extracts the message with the encryption procedure of the sender, in this case $E_B$ (available on the public file):

$$
M = E_B(S)
$$

She now possesses a message-signature pair $(M, S)$ with properties similar to those of a signed paper document.

Bob cannot later deny having sent Alice this message, since no one else could have created $S = D_B(M)$. Alice can convince a “judge” that $E_B(S) = M$, so she has proof that Bob signed the document.

Clearly Alice cannot modify $M$ to a different version $M'$, since then she would have to create the corresponding signature $S' = D_B(M')$ as well.

Therefore Alice has received a message “signed” by Bob, which she can “prove” that he sent, but which she cannot modify. (Nor can she forge his signature for any other message.)

An electronic checking system could be based on a signature system such as the above. It is easy to imagine an encryption device in your home terminal allowing you to sign checks that get sent by electronic mail to the payee. It would only be necessary to include a unique check number in each check so that even if the payee copies the check the bank will only honor the first version it sees.

Another possibility arises if encryption devices can be made fast enough: it will be possible to have a telephone conversation in which every word spoken is signed by the encryption device before transmission.

When encryption is used for signatures as above, it is important that the encryption device not be “wired in” between the terminal (or computer) and the communications channel, since a message may have to be successively enciphered with several keys. It is perhaps more natural to view the encryption device as a “hardware subroutine” that can be executed as needed.

We have assumed above that each user can always access the public file reliably. In a “computer network” this might be difficult; an “intruder” might forge messages purporting to be from the public file. The user would like to be sure that he actually obtains the encryption procedure of his desired correspondent and not, say, the encryption procedure of the intruder. This danger disappears if the public file “signs” each message it sends to a user. The user can check the signature with the public file’s encryption algorithm $E_{PF}$. The problem of “looking up” $E_{PF}$ itself in the public file is avoided by giving each user a description of $E_{PF}$ when he first shows up (in person) to join the public-key cryptosystem and to deposit his public encryption procedure. He then stores this description rather than ever looking it up again. The need for a courier between every pair of users has thus been replaced by the requirement for a single secure meeting between each user and the public file manager when the user joins the system. Another solution is to give each user, when he signs up, a book (like a telephone directory) containing all the encryption keys of users in the system.
