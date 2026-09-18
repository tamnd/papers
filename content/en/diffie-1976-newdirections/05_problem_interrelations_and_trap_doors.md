---
paper: diffie-1976-newdirections
title: New Directions in Cryptography
authors:
  - Whitfield Diffie
  - Martin E. Hellman
year: 1976
venue: IEEE Transactions on Information Theory
field: security
section: V
section_title: PROBLEM INTERRELATIONS AND TRAP DOORS
tag: "0376"
kind: section
lang: en
source: https://doi.org/10.1109/tit.1976.1055638
pdf_sha256: 03fa2f493a1448a309586b9cf9e5c3a4dfd14735e0786cc94674519570b890ff
pdf_pages: 8-9
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 96ce9fac939555dbfe43abadcf6890ef6bd2724419ed13678db5cc8f63a9327e
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

In this section, we will show that some of the cryptographic problems presented thus far can be reduced to others, thereby defining a loose ordering according to difficulty. We also introduce the more difficult problem of trap doors.

In Section II we showed that a cryptographic system intended for privacy can also be used to provide authentication against third party forgeries. Such a system can be used to create other cryptographic objects, as well.

A cryptosystem which is secure against a known plaintext attack can be used to produce a one-way function.

As indicated in Fig. 3, take the cryptosystem $\{S_K : \{P\} \to \{C\}\}_{K \in \{K\}}$ which is secure against a known plaintext attack, fix $P = P_0$ and consider the map

$$
f : \{K\} \to \{C\}
$$

defined by

$$
f(X) = S_X(P_0).
$$

This function is one-way because solving for $X$ given $f(X)$ is equivalent to the cryptanalytic problem of finding the key from a single known plaintext–cryptogram pair. Public knowledge of $f$ is now equivalent to public knowledge of $\{S_K\}$ and $P_0$.

While the converse of this result is not necessarily true, it is possible for a function originally found in the search for one-way functions to yield a good cryptosystem. This actually happened with the discrete exponential function discussed in Section III [8].

One-way functions are basic to both block ciphers and key generators. A key generator is a pseudorandom bit generator whose output, the keystream, is added modulo 2 to a message represented in binary form, in imitation of a one-time pad. The key is used as a “seed” which determines the pseudorandom keystream sequence. A known plaintext attack thus reduces to the problem of determining the key from the keystream. For the system to be secure, computation of the key from the keystream must be computationally infeasible. While, for the system to be usable, calculation of the keystream from the key must be computationally simple. Thus a good key generator is, almost by definition, a one-way function.

Use of either type of cryptosystem as a one way function suffers from a minor problem. As noted earlier, if the function $f$ is not uniquely invertible, it is not necessary (or possible) to find the actual value of $X$ used. Rather any $X$ with the same image will suffice. And, while each mapping $S_K$ in a cryptosystem must be bijective, there is no such restriction on the function $f$ from key to cryptogram defined above. Indeed, guaranteeing that a cryptosystem has this property appears quite difficult. In a good cryptosystem the mapping $f$ can be expected to have the characteristics of a randomly chosen mapping (i.e., $f(X_i)$ is chosen uniformly from all possible $Y$, and successive choices are independent). In this case, if $X$ is chosen uniformly and there are an equal number of keys and messages ($X$ and $Y$), then the probability that the resultant $Y$ has $k + 1$ inverses is approximately $e^{-1}/k!$ for $k = 0,1,2,3,\ldots$. This is a Poisson distribution with mean $\lambda = 1$, shifted by 1 unit. The expected number of inverses is thus only 2. While it is possible for $f$ to be more degenerate, a good cryptosystem will not be too degenerate since then the key is not being well used. In the worst case, if $f(X) \equiv Y_0$ for some $Y_0$, we have $S_K(P_0) \equiv C_0$, and encipherment of $P_0$ would not depend on the key at all!

Figure.

Fig. 3. Secure cryptosystem used as one-way function. {#diffie-1976-newdirections-fig-3 .figure tag=0377}

While we are usually interested in functions whose domain and range are of comparable size, there are exceptions. In the previous section we required a one-way function mapping long strings onto much shorter ones. By using a block cipher whose key length is larger than the blocksize, such functions can be obtained using the above technique.

Evans *et al.* [10] have a different approach to the problem of constructing a one-way function from a block cipher. Rather than selecting a fixed $P_0$ as the input, they use the function

$$
f(X) = S_X(X).
$$

This is an attractive approach because equations of this form are generally difficult to solve, even when the family $S$ is comparatively simple. This added complexity, however, destroys the equivalence between the security of the system $S$ under a known plaintext attack and the one-wayness of $f$.

Another relationship has already been shown in Section IV.

*A public key cryptosystem can be used to generate a one-way authentication system.*

The converse does not appear to hold, making the construction of a public key cryptosystem a strictly more difficult problem than one-way authentication. Similarly, a public key cryptosystem can be used as a public key distribution system, but not conversely.

Since in a public key cryptosystem the general system in which $E$ and $D$ are used must be public, specifying $E$ specifies a complete algorithm for transforming input messages into output cryptograms. As such a public key system is really a set of *trap-door one-way functions*. These are functions which are not really one-way in that simply computed inverses exist. But given an algorithm for the forward function it is computationally infeasible to find a simply computed inverse. Only through knowledge of certain *trap-door information* (e.g., the random bit string which produced the $E-D$ pair) can one easily find the easily computed inverse.

*Trap doors* have already been seen in the previous paragraph in the form of *trap-door one-way functions*, but other variations exist. A *trap-door cipher* is one which strongly resists cryptanalysis by anyone not in possession of *trap-door information* used in the design of the cipher. This allows the designer to break the system after he has sold it to a client and yet falsely to maintain his reputation as a builder of secure systems. It is important to note that it is not greater cleverness or knowledge of cryptography which allows the designer to do what others cannot. If he were to lose the trap-door information he would be no better off than anyone else. The situation is precisely analogous to a combination lock. Anyone who knows the combination can do in seconds what even a skilled locksmith would require hours to accomplish. And yet, if he forgets the combination, he has no advantage.

*A trap-door cryptosystem can be used to produce a public key distribution system.*

For $A$ and $B$ to establish a common private key, $A$ chooses a key at random and sends an arbitrary plaintext–cryptogram pair to $B$. $B$, who made the trap-door cipher public, but kept the trap-door information secret, uses the plaintext-cryptogram pair to solve for the key. $A$ and $B$ now have a key in common.

There is currently little evidence for the existence of trap-door ciphers. However they are a distinct possibility and should be remembered when accepting a cryptosystem from a possible opponent [12].

By definition, we will require that a trap-door problem be one in which it is computationally feasible to devise the trap door. This leaves room for yet a third type of entity for which we shall use the prefix “quasi.” For example a *quasi one-way function* is not one-way in that an easily computed inverse exists. However, it is computationally infeasible even for the designer, to find the easily computed inverse. Therefore a quasi one-way function can be used in place of a one-way function with essentially no loss in security.

Losing the trap-door information to a trap-door one-way function makes it into a quasi one-way function, but there may also be one-way functions not obtainable in this manner.

It is entirely a matter of definition that quasi one-way functions are excluded from the class of one-way functions. One could instead talk of one-way functions in the wide sense or in the strict sense.

Similarly, a quasi secure cipher is a cipher which will successfully resist cryptanalysis, even by its designer, and yet for which there exists a computationally efficient cryptanalytic algorithm (which is of course computationally infeasible to find). Again, from a practical point of view, there is essentially no difference between a secure cipher and a quasi secure one.

We have already seen that public key cryptosystems imply the existence of trap-door one-way functions. However the converse is not true. For a trap-door one-way function to be usable as a public key cryptosystem, it must be invertible (i.e., have a unique inverse.)
