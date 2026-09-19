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
section: IX
section_title: 'Security of the Method: Cryptanalytic Approaches'
tag: 094C
kind: section
lang: en
source: https://doi.org/10.21236/ada606588
pdf_sha256: f7b1f78d9a7cbeb85e32b8c563a6db60771a5cc4bdc55580645f7cb778a4966b
pdf_pages: 11-13
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 05bfa8a78ff58205b1e89df1995817cc4d85f14eee68abe100681b419461fced
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Since no techniques exist to prove that an encryption scheme is secure, the only test available is to see whether anyone can think of a way to break it. The NBS standard was “certified” this way; seventeen man-years at IBM were spent fruitlessly trying to break that scheme. Once a method has successfully resisted such a concerted attack it may for practical purposes be considered secure. (Actually there is some controversy concerning the security of the NBS method [2].)

We show in the next sections that all the obvious approaches for breaking our system are at least as difficult as factoring $n$. While factoring large numbers is not provably difficult, it is a well-known problem that has been worked on for the last three hundred years by many famous mathematicians. Fermat (1601?-1665) and Legendre (1752-1833) developed factoring algorithms; some of today’s more efficient algorithms are based on the work of Legendre. As we shall see in the next section, however, no one has yet found an algorithm which can factor a 200-digit number in a reasonable amount of time. We conclude that our system has already been partially “certified” by these previous efforts to find efficient factoring algorithms.

In the following sections we consider ways a cryptanalyst might try to determine the secret decryption key from the publicly revealed encryption key. We do not consider ways of protecting the decryption key from theft; the usual physical security methods should suffice. (For example, the encryption device could be a separate device which could also be used to generate the encryption and decryption keys, such that the decryption key is never printed out (even for its owner) but only used to decrypt messages. The device could erase the decryption key if it was tampered with.)

A  Factoring $n$

Factoring $n$ would enable an enemy cryptanalyst to “break” our method. The factors of $n$ enable him to compute $\phi(n)$ and thus $d$. Fortunately, factoring a number seems to be much more difficult than determining whether it is prime or composite.

A large number of factoring algorithms exist. Knuth [3, Section 4.5.4] gives an excellent presentation of many of them. Pollard [9] presents an algorithm which factors a number $n$ in time $O(n^{1/4})$.

The fastest factoring algorithm known to the authors is due to Richard SchroeppeI (unpublished); it can factor $n$ in approximately

$$
\exp \sqrt{\ln(n) \cdot \ln(\ln(n))} = n^{\sqrt{\ln \ln(n)/\ln(n)}}
$$

$$
= (\ln(n)) \sqrt{\ln(n)/\ln(\ln(n))}
$$

steps (here ln denotes the natural logarithm function). Table 1 gives the number of operations needed to factor $n$ with Schroepel’s method, and the time required if each operation uses one microsecond, for various lengths of the number $n$ (in decimal digits).

Table 1

| Digits | Number of operations | Time |
| --- | --- | --- |
| 50 | $1.4 \times 10^{10}$ | 3.9 hours |
| 75 | $9.0 \times 10^{12}$ | 104 days |
| 100 | $2.3 \times 10^{15}$ | 74 years |
| 200 | $1.2 \times 10^{23}$ | $3.8 \times 10^9$ years |
| 300 | $1.5 \times 10^{29}$ | $4.9 \times 10^{15}$ years |
| 500 | $1.3 \times 10^{39}$ | $4.2 \times 10^{25}$ years |

We recommend that $n$ be about 200 digits long. Longer or shorter lengths can be used depending on the relative importance of encryption speed and security in the application at hand. An 80-digit $n$ provides moderate security against an attack using current technology; using 200 digits provides a margin of safety against future developments. This flexibility to choose a key-length (and thus a level of security) to suit a particular application is a feature not found in many of the previous encryption schemes (such as the NBS scheme).

B Computing $\phi(n)$ Without Factoring $n$

If a cryptanalyst could compute $\phi(n)$ then he could break the system by computing $d$ as the multiplicative inverse of $e$ modulo $\phi(n)$ (using the procedure of Section VII D).

We argue that this approach is no easier than factoring $n$ since it enables the cryptanalyst to easily factor $n$ using $\phi(n)$. This approach to factoring $n$ has not turned out to be practical.

How can $n$ be factored using $\phi(n)$? First, $(p + q)$ is obtained from $n$ and $\phi(n) = n - (p + q) + 1$. Then $(p - q)$ is the square root of $(p + q)^2 - 4n$. Finally, $q$ is half the difference of $(p + q)$ and $(p - q)$.

Therefore breaking our system by computing $\phi(n)$ is no easier than breaking our system by factoring $n$. (This is why $n$ must be composite; $\phi(n)$ is trivial to compute if $n$ is prime.)

C Determining $d$ Without Factoring $n$ or Computing $\phi(n)$.

Of course, $d$ should be chosen from a large enough set so that a direct search for it is unfeasible.

We argue that computing $d$ is no easier for a cryptanalyst than factoring $n$, since once $d$ is known $n$ could be factored easily. This approach to factoring has also not turned out to be fruitful.

A knowledge of $d$ enables $n$ to be factored as follows. Once a cryptanalyst knows $d$ he can calculate $e \cdot d - 1$, which is a multiple of $\phi(n)$. Miller [6] has shown that $n$ can be factored using any multiple of $\phi(n)$. Therefore if $n$ is large a cryptanalyst should not be able to determine $d$ any easier than he can factor $n$.

A cryptanalyst may hope to find a $d'$ which is equivalent to the $d$ secretly held by a user of the public-key cryptosystem. If such values $d'$ were common then a brute-force search could break the system. However, all such $d'$ differ by the least common multiple of $(p-1)$ and $(q-1)$, and finding one enables $n$ to be factored. (In (3) and (5), $\phi(n)$ can be replaced by $\operatorname{lcm}(p-1, q-1)$.) Finding any such $d'$ is therefore as difficult as factoring $n$.

D Computing $D$ in Some Other Way

Although this problem of “computing $e$-th roots modulo $n$ without factoring $n$” is not a well-known difficult problem like factoring, we feel reasonably confident that it is computationally intractable. It may be possible to prove that any general method of breaking our scheme yields an efficient factoring algorithm. This would establish that any way of breaking our scheme must be as difficult as factoring. We have not been able to prove this conjecture, however.

Our method should be certified by having the above conjecture of intractability withstand a concerted attempt to disprove it. The reader is challenged to find a way to “break” our method.
