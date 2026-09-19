---
paper: diffie-1976-newdirections
title: New Directions in Cryptography
authors:
  - Whitfield Diffie
  - Martin E. Hellman
year: 1976
venue: IEEE Transactions on Information Theory
field: security
section: III
section_title: Public Key Cryptography
tag: "0373"
kind: section
lang: en
source: https://doi.org/10.1109/tit.1976.1055638
pdf_sha256: 03fa2f493a1448a309586b9cf9e5c3a4dfd14735e0786cc94674519570b890ff
pdf_pages: 4-6
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 764a3022188e498d562cbe8fe0ec806bb9e01397bf8ddff9dbca5313687ca0da
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

As shown in Fig. 1, cryptography has been a derivative security measure. Once a secure channel exists along which keys can be transmitted, the security can be extended to other channels of higher bandwidth or smaller delay by encrypting the messages sent on them. The effect has been to limit the use of cryptography to communications among people who have made prior preparation for cryptographic security.

In order to develop large, secure, telecommunications systems, this must be changed. A large number of users $n$ results in an even larger number, $(n^2 - n)/2$ potential pairs who may wish to communicate privately from all others. It is unrealistic to assume either that a pair of users with no prior acquaintance will be able to wait for a key to be sent by some secure physical means, or that keys for all $(n^2 - n)/2$ pairs can be arranged in advance. In another paper [5], the authors have considered a conservative approach requiring no new development in cryptography itself, but this involves diminished security, inconvenience, and restriction of the network to a starlike configuration with respect to initial connection protocol.

We propose that it is possible to develop systems of the type shown in Fig. 2, in which two parties communicating solely over a public channel and using only publicly known techniques can create a secure connection. We examine two approaches to this problem, called public key cryptosys-

Figure.

Fig. 2. Flow of information in public key system. {#diffie-1976-newdirections-fig-2 .figure tag=0374}

tems and public key distribution systems, respectively. The first are more powerful, lending themselves to the solution of the authentication problems treated in the next section, while the second are much closer to realization.

A *public key cryptosystem* is a pair of families $\{E_K\}_{K \in \{K\}}$ and $\{D_K\}_{K \in \{K\}}$ of algorithms representing invertible transformations,

$$
E_K : \{M\} \to \{M\}
$$

(2)

$$
D_K : \{M\} \to \{M\}
$$

(3) on a finite message space $\{M\}$, such that

1) for every $K \in \{K\}$, $E_K$ is the inverse of $D_K$,
2) for every $K \in \{K\}$ and $M \in \{M\}$, the algorithms $E_K$ and $D_K$ are easy to compute,
3) for almost every $K \in \{K\}$, each easily computed algorithm equivalent to $D_K$ is computationally infeasible to derive from $E_K$,
4) for every $K \in \{K\}$, it is feasible to compute inverse pairs $E_K$ and $D_K$ from $K$.

Because of the third property, a user's enciphering key $E_K$ can be made public without compromising the security of his secret deciphering key $D_K$. The cryptographic system is therefore split into two parts, a family of enciphering transformations and a family of deciphering transformations in such a way that, given a member of one family, it is infeasible to find the corresponding member of the other.

The fourth property guarantees that there is a feasible way of computing corresponding pairs of inverse transformations when no constraint is placed on what either the enciphering or deciphering transformation is to be. In practice, the cryptoequipment must contain a true random number generator (e.g., a noisy diode) for generating $K$, together with an algorithm for generating the $E_K - D_K$ pair from its outputs.

Given a system of this kind, the problem of key distribution is vastly simplified. Each user generates a pair of inverse transformations, $E$ and $D$, at his terminal. The deciphering transformation $D$ must be kept secret, but need never be communicated on any channel. The enciphering key $E$ can be made public by placing it in a public directory along with the user's name and address. Anyone can then encrypt messages and send them to the user, but no one else can decipher messages intended for him. Public key cryptosystems can thus be regarded as *multiple access ciphers*.

It is crucial that the public file of enciphering keys be protected from unauthorized modification. This task is made easier by the public nature of the file. Read protection is unnecessary and, since the file is modified infrequently, elaborate write protection mechanisms can be economically employed.

A suggestive, although unfortunately useless, example of a public key cryptosystem is to encipher the plaintext, represented as a binary $n$-vector $m$, by multiplying it by an invertible binary $n \times n$ matrix $E$. The cryptogram thus equals $Em$. Letting $D = E^{-1}$ we have $m = Dc$. Thus, both enciphering and deciphering require about $n^2$ operations. Calculation of $D$ from $E$, however, involves a matrix inversion which is a harder problem. And it is at least conceptually simpler to obtain an arbitrary pair of inverse matrices than it is to invert a given matrix. Start with the identity matrix $I$ and do elementary row and column operations to obtain an arbitrary invertible matrix $E$. Then starting with $I$ do the inverses of these same elementary operations in reverse order to obtain $D = E^{-1}$. The sequence of elementary operations could be easily determined from a random bit string.

Unfortunately, matrix inversion takes only about $n^3$ operations. The ratio of "cryptanalytic" time (i.e., computing $D$ from $E$) to enciphering or deciphering time is thus at most $n$, and enormous block sizes would be required to obtain ratios of $10^6$ or greater. Also, it does not appear that knowledge of the elementary operations used to obtain $E$ from $I$ greatly reduces the time for computing $D$. And, since there is no round-off error in binary arithmetic, numerical stability is unimportant in the matrix inversion. In spite of its lack of practical utility, this matrix example is still useful for clarifying the relationships necessary in a public key cryptosystem.

A more practical approach to finding a pair of easily computed inverse algorithms $E$ and $D$; such that $D$ is hard to infer from $E$, makes use of the difficulty of analyzing programs in low level languages. Anyone who has tried to determine what operation is accomplished by someone else's machine language program knows that $E$ itself (i.e., what $E$ does) can be hard to infer from an algorithm for $E$. If the program were to be made purposefully confusing through addition of unneeded variables and statements, then determining an inverse algorithm could be made very difficult. Of course, $E$ must be complicated enough to prevent its identification from input-output pairs.

Essentially what is required is a one-way compiler: one which takes an easily understood program written in a high level language and translates it into an incomprehensible program in some machine language. The compiler is one-way because it must be feasible to do the compilation, but infeasible to reverse the process. Since efficiency in size of program and run time are not crucial in this application, such compilers may be possible if the structure of the machine language can be optimized to assist in the confusion.

Merkle [1] has independently studied the problem of distributing keys over an insecure channel. His approach is different from that of the public key cryptosystems suggested above, and will be termed a *public key distribution system*. The goal is for two users, $A$ and $B$, to securely exchange a key over an insecure channel. This key is then used by both users in a normal cryptosystem for both enciphering and deciphering. Merkle has a solution whose cryptanalytic cost grows as $n^2$ where $n$ is the cost to the legitimate users. Unfortunately the cost to the legitimate users of the system is as much in transmission time as in computation, because Merkle's protocol requires $n$ potential keys to be transmitted before one key can be decided on. Merkle notes that this high transmission overhead prevents the system from being very useful in practice. If a one megabit limit is placed on the setup protocol’s overhead, his technique can achieve cost ratios of approximately 10 000 to 1, which are too small for most applications. If inexpensive, high bandwidth data links become available, ratios of a million to one or greater could be achieved and the system would be of substantial practical value.

We now suggest a new public key distribution system which has several advantages. First, it requires only one “key” to be exchanged. Second, the cryptanalytic effort appears to grow exponentially in the effort of the legitimate users. And, third, its use can be tied to a public file of user information which serves to authenticate user $A$ to user $B$ and vice versa. By making the public file essentially a read only memory, one personal appearance allows a user to authenticate his identity many times to many users. Merkle’s technique requires $A$ and $B$ to verify each other’s identities through other means.

The new technique makes use of the apparent difficulty of computing logarithms over a finite field $GF(q)$ with a prime number $q$ of elements. Let

$$
Y = \alpha^X \mod q, \quad \text{for } 1 \leq X \leq q - 1,
$$

where $\alpha$ is a fixed primitive element of $GF(q)$, then $X$ is referred to as the logarithm of $Y$ to the base $\alpha$, mod $q$:

$$
X = \log_\alpha Y \mod q, \quad \text{for } 1 \leq Y \leq q - 1.
$$

Calculation of $Y$ from $X$ is easy, taking at most $2 \times \log_2 q$ multiplications [6, pp. 398–422]. For example, for $X = 18$,

$$
Y = \alpha^{18} = (((\alpha^2)^2)^2)^2 \times \alpha^2.
$$

Computing $X$ from $Y$, on the other hand can be much more difficult and, for certain carefully chosen values of $q$, requires on the order of $q^{1/2}$ operations, using the best known algorithm [7, pp. 9, 575–576], [8].

The security of our technique depends crucially on the difficulty of computing logarithms mod $q$, and if an algorithm whose complexity grew as $\log_2 q$ were to be found, our system would be broken. While the simplicity of the problem statement might allow such simple algorithms, it might instead allow a proof of the problem’s difficulty. For now we assume that the best known algorithm for computing logs mod $q$ is in fact close to optimal and hence that $q^{1/2}$ is a good measure of the problem’s complexity, for a properly chosen $q$.

Each user generates an independent random number $X_i$ chosen uniformly from the set of integers $\{1, 2, \cdots, q - 1\}$. Each keeps $X_i$ secret, but places

$$
Y_i = \alpha^{X_i} \mod q
$$

in a public file with his name and address. When users $i$ and $j$ wish to communicate privately, they use

$$
K_{ij} = \alpha^{X_i X_j} \mod q
$$

as their key. User $i$ obtains $K_{ij}$ by obtaining $Y_j$ from the public file and letting

$$
K_{ij} = Y_j^{X_i} \mod q \\
= (\alpha^{X_j})^{X_i} \mod q \\
= \alpha^{X_j X_i} = \alpha^{X_i X_j} \mod q.
$$

User $j$ obtains $K_{ij}$ in the similar fashion

$$
K_{ij} = Y_i^{X_j} \mod q.
$$

Another user must compute $K_{ij}$ from $Y_i$ and $Y_j$, for example, by computing

$$
K_{ij} = Y_i^{(\log_\alpha Y_j)} \mod q.
$$

We thus see that if logs mod $q$ are easily computed the system can be broken. While we do not currently have a proof of the converse (i.e., that the system is secure if logs mod $q$ are difficult to compute), neither do we see any way to compute $K_{ij}$ from $Y_i$ and $Y_j$ without first obtaining either $X_i$ or $X_j$.

If $q$ is a prime slightly less than $2^b$, then all quantities are representable as $b$ bit numbers. Exponentiation then takes at most $2b$ multiplications mod $q$, while by hypothesis taking logs requires $q^{1/2} = 2^{b/2}$ operations. The cryptanalytic effort therefore grows exponentially relative to legitimate efforts. If $b = 200$, then at most 400 multiplications are required to compute $Y_i$ from $X_i$, or $K_{ij}$ from $Y_i$ and $X_j$, yet taking logs mod $q$ requires $2^{100}$ or approximately $10^{30}$ operations.
