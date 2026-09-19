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
section: VII
section_title: Algorithms
tag: 094A
kind: section
lang: en
source: https://doi.org/10.21236/ada606588
pdf_sha256: f7b1f78d9a7cbeb85e32b8c563a6db60771a5cc4bdc55580645f7cb778a4966b
pdf_pages: 8-10
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: d8d3198b3085faf2f25e6ac179cc15bf663457e914eb50a5b9dcf7680835bfb2
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

To show that our method is practical, we describe an efficient algorithm for each required operation.

A  How to Encrypt and Decrypt Efficiently

Computing $M^e \pmod{n}$ requires at most $2 \cdot \log_2(e)$ multiplications and $2 \cdot \log_2(e)$ divisions using the following procedure (decryption can be performed similarly using $d$ instead of $e$):

Step 1. Let $e_k e_{k-1} \ldots e_1 e_0$ be the binary representation of $e$.
Step 2. Set the variable $C$ to 1.
Step 3. Repeat steps 3a and 3b for $i = k, k-1, \ldots, 0$:
    Step 3a. Set $C$ to the remainder of $C^2$ when divided by $n$.
    Step 3b. If $e_i = 1$, then set $C$ to the remainder of $C \cdot M$ when divided by $n$.
Step 4. Halt. Now $C$ is the encrypted form of $M$.

This procedure is called “exponentiation by repeated squaring and multiplication.” This procedure is half as good as the best; more efficient procedures are known. Knuth [3] studies this problem in detail.

The fact that the enciphering and deciphering are identical leads to a simple implementation. (The whole operation can be implemented on a few special-purpose integrated circuit chips.)

A high-speed computer can encrypt a 200-digit message $M$ in a few seconds; special-purpose hardware would be much faster. The encryption time per block increases no faster than the cube of the number of digits in $n$.

B  How to Find Large Prime Numbers

Each user must (privately) choose two large random numbers $p$ and $q$ to create his own encryption and decryption keys. These numbers must be large so that it is not computationally feasible for anyone to factor $n = p \cdot q$. (Remember that $n$, but not $p$ or $q$, will be in the public file.) We recommend using 100-digit (decimal) prime numbers $p$ and $q$, so that $n$ has 200 digits.

To find a 100-digit “random” prime number, generate (odd) 100-digit random numbers until a prime number is found. By the prime number theorem [7], about $(\ln 10^{100})/2 = 115$ numbers will be tested before a prime is found.

To test a large number $b$ for primality we recommend the elegant “probabilistic” algorithm due to Solovay and Strassen [12]. It picks a random number $a$ from a uniform distribution on $\{1, \ldots, b-1\}$, and tests whether

$$
\gcd(a, b) = 1 \text{ and } J(a, b) = a^{(b-1)/2} \pmod{b},
$$

where $J(a, b)$ is the Jacobi symbol [7]. If $b$ is prime (6) is always true. If $b$ is composite (6) will be false with probability at least 1/2. If (6) holds for 100 randomly chosen values of $a$ then $b$ is almost certainly prime; there is a (negligible) chance of one in $2^{100}$ that $b$ is composite. Even if a composite were accidentally used in our system, the receiver would probably detect this by noticing that decryption didn’t work correctly. When $b$ is odd, $a \leq b$, and $\gcd(a, b) = 1$, the Jacobi symbol $J(a, b)$ has a value in $\{-1, 1\}$ and can be efficiently computed by the program:

$$
J(a, b) = \text{if } a = 1 \text{ then } 1 \text{ else} \\
\quad \text{if } a \text{ is even then } J(a/2, b) \cdot (-1)^{(b^2-1)/8} \\
\quad \text{else } J(b \pmod{a}, a) \cdot (-1)^{(a-1)\cdot(b-1)/4}
$$

(The computations of $J(a, b)$ and $\gcd(a, b)$ can be nicely combined, too.) Note that this algorithm does *not* test a number for primality by trying to factor it. Other efficient procedures for testing a large number for primality are given in [6,9,11].

To gain additional protection against sophisticated factoring algorithms, $p$ and $q$ should differ in length by a few digits, both $(p-1)$ and $(q-1)$ should contain large prime factors, and $\gcd(p-1, q-1)$ should be small. The latter condition is easily checked.

To find a prime number $p$ such that $(p-1)$ has a large prime factor, generate a large random prime number $u$, then let $p$ be the first prime in the sequence $i \cdot u + 1$, for $i = 2, 4, 6, \ldots$. (This shouldn’t take too long.) Additional security is provided by ensuring that $(u-1)$ also has a large prime factor.

A high-speed computer can determine in several seconds whether a 100-digit number is prime, and can find the first prime after a given point in a minute or two.

Another approach to finding large prime numbers is to take a number of known factorization, add one to it, and test the result for primality. If a prime $p$ is found it is possible to *prove* that it really is prime by using the factorization of $p - 1$. We omit a discussion of this since the probabilistic method is adequate.

C  How to Choose $d$

It is very easy to choose a number $d$ which is relatively prime to $\phi(n)$. For example, any prime number greater than $\max(p, q)$ will do. It is important that $d$ should be chosen from a large enough set so that a cryptanalyst cannot find it by direct search.

D  How to Compute $e$ from $d$ and $\phi(n)$

To compute $e$, use the following variation of Euclid’s algorithm for computing the greatest common divisor of $\phi(n)$ and $d$. (See exercise 4.5.2.15 in [3].) Calculate $\gcd(\phi(n), d)$ by computing a series $x_0, x_1, x_2, \ldots$, where $x_0 \equiv \phi(n), x_1 = d$, and $x_{i+1} \equiv x_{i-1} \pmod{x_i}$, until an $x_k$ equal to 0 is found. Then $\gcd(x_0, x_1) = x_{k-1}$. Compute for each $x_i$ numbers $a_i$ and $b_i$ such that $x_i = a_i \cdot x_0 + b_i \cdot x_1$. If $x_{k-1} = 1$ then $b_{k-1}$ is the multiplicative inverse of $x_1 \pmod{x_0}$. Since $k$ will be less than $2 \log_2(n)$, this computation is very rapid.

If $e$ turns out to be less than $\log_2(n)$, start over by choosing another value of $d$. This guarantees that every encrypted message (except $M = 0$ or $M = 1$) undergoes some “wrap-around” (reduction modulo $n$).
