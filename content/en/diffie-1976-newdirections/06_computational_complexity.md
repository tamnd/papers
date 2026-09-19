---
paper: diffie-1976-newdirections
title: New Directions in Cryptography
authors:
  - Whitfield Diffie
  - Martin E. Hellman
year: 1976
venue: IEEE Transactions on Information Theory
field: security
section: VI
section_title: COMPUTATIONAL COMPLEXITY
tag: "0378"
kind: section
lang: en
source: https://doi.org/10.1109/tit.1976.1055638
pdf_sha256: 03fa2f493a1448a309586b9cf9e5c3a4dfd14735e0786cc94674519570b890ff
pdf_pages: 9-11
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 1d944145d2e79ef2b24404f2fce81d8659c6767d6ae37eed00002bb3a052ca22
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Cryptography differs from all other fields of endeavor in the ease with which its requirements may appear to be satisfied. Simple transformations will convert a legible text into an apparently meaningless jumble. The critic, who wishes to claim that meaning might yet be recovered by cryptanalysis, is then faced with an arduous demonstration if he is to prove his point of view correct. Experience has shown, however, that few systems can resist the concerted attack of skillful cryptanalysts, and many supposedly secure systems have subsequently been broken.

In consequence of this, judging the worth of new systems has always been a central concern of cryptographers. During the sixteenth and seventeenth centuries, mathematical arguments were often invoked to argue the strength of cryptographic methods, usually relying on counting methods which showed the astronomical number of possible keys. Though the problem is far too difficult to be laid to rest by such simple methods, even the noted algebraist Cardano fell into this trap [2, p. 145]. As systems whose strength had been so argued were repeatedly broken, the notion of giving mathematical proofs for the security of systems fell into disrepute and was replaced by certification via crypanalytic assault.

During this century, however, the pendulum has begun to swing back in the other direction. In a paper intimately connected with the birth of information theory, Shannon [3] showed that the one time pad system, which had been in use since the late twenties offered “perfect secrecy” (a form of unconditional security). The provably secure systems investigated by Shannon rely on the use of either a key whose length grows linearly with the length of the message or on perfect source coding and are therefore too unwieldy for most purposes. We note that neither public key cryptosystems nor one-way authentication systems can be unconditionally secure because the public information always determines the secret information uniquely among the members of a finite set. With unlimited computation, the problem could therefore be solved by a straightforward search.

The past decade has seen the rise of two closely related disciplines devoted to the study of the costs of computation: computational complexity theory and the analysis of algorithms. The former has classified known problems in computing into broad classes by difficulty, while the latter has concentrated on finding better algorithms and studying the resources they consume. After a brief digression into complexity theory, we will examine its application to cryptography, particularly the analysis of one-way functions.

A function is said to belong to the complexity class $P$ (for polynomial) if it can be computed by a deterministic Turing Machine in a time which is bounded above by some polynomial function of the length of its input. One might think of this as the class of easily computed functions, but it is more accurate to say that a function not in this class must be hard to compute for at least some inputs. There are problems which are known not to be in the class $P$ [13, pp. 405–425].

There are many problems which arise in engineering which cannot be solved in polynomial time by any known techniques, unless they are run on a computer with an unlimited degree of parallelism. These problems may or may not belong to the class $P$, but belong to the class $NP$ (for nondeterministic, polynomial) of problems solvable in polynomial time on a “nondeterministic” computer (i.e., one with an unlimited degree of parallelism). Clearly the class $NP$ includes the class $P$, and one of the great open questions in complexity theory is whether the class $NP$ is strictly larger.

Among the problems known to be solvable in $NP$ time, but not known to be solvable in $P$ time, are versions of the traveling salesman problem, the satisfiability problem for propositional calculus, the knapsack problem, the graph coloring problem, and many scheduling and minimization problems [13, pp. 363–404], [[karp-1972-reducibility]]. We see that it is not lack of interest or effort which has prevented people from finding solutions in $P$ time for these problems. It is thus strongly believed that at least one of these problems must not be in the class $P$, and that therefore the class $NP$ is strictly larger.

Karp has identified a subclass of the $NP$ problems, called $NP$ complete, with the property that if any one of them is in $P$, then all $NP$ problems are in $P$. Karp lists 21 problems which are $NP$ complete, including all of the problems mentioned above [[karp-1972-reducibility]].

While the $NP$ complete problems show promise for cryptographic use, current understanding of their difficulty includes only worst case analysis. For cryptographic purposes, typical computational costs must be considered. If, however, we replace worst case computation time with average or typical computation time as our complexity measure, the current proofs of the equivalences among the $NP$ complete problems are no longer valid. This suggests several interesting topics for research. The ensemble and typicality concepts familiar to information theorists have an obvious role to play.

We can now identify the position of the general cryptanalytic problem among all computational problems.

*The cryptanalytic difficulty of a system whose encryption and decryption operations can be done in $P$ time cannot be greater than $NP$.*

To see this, observe that any cryptanalytic problem can be solved by finding a key, inverse image, etc., chosen from a finite set. Choose the key nondeterministically and verify in $P$ time that it is the correct one. If there are $M$ possible keys to choose from, an $M$-fold parallelism must be employed. For example in a known plaintext attack, the plaintext is encrypted simultaneously under each of the keys and compared with the cryptogram. Since, by assumption, encryption takes only $P$ time, the cryptanalysis takes only $NP$ time.

We also observe that the general cryptanalytic problem is $NP$ complete. This follows from the breadth of our definition of cryptographic problems. A one-way function with an $NP$ complete inverse will be discussed next.

Cryptography can draw directly from the theory of $NP$ complexity by examining the way in which $NP$ complete problems can be adapted to cryptographic use. In particular, there is an $NP$ complete problem known as the knapsack problem which lends itself readily to the construction of a one-way function.

Let $y = f(x) = a \cdot x$ where $a$ is a known vector of $n$ integers ($a_1, a_2, \cdots, a_n$) and $x$ is a binary $n$-vector. Calculation of $y$ is simple, involving a sum of at most $n$ integers. The problem of inverting $f$ is known as the knapsack problem and requires finding a subset of the $\{a_i\}$ which sum to $y$.

Exhaustive search of all $2^n$ subsets grows exponentially and is computationally infeasible for $n$ greater than 100 or so. Care must be exercised, however, in selecting the parameters of the problem to ensure that shortcuts are not possible. For example if $n = 100$ and each $a_i$ is 32 bits long, $y$ is at most 39 bits long, and $f$ is highly degenerate; requiring on the average only $2^{38}$ tries to find a solution. Somewhat more trivially, if $a_i = 2^{i-1}$ then inverting $f$ is equivalent to finding the binary decomposition of $y$.

This example demonstrates both the great promise and the considerable shortcomings of contemporary complexity theory. The theory only tells us that the knapsack problem is probably difficult in the worst case. There is no indication of its difficulty for any particular array. It appears, however, that choosing the $\{a_i\}$ uniformly from $\{0,1,2,\ldots,2^{n-1}\}$ results in a hard problem with probability one as $n \to \infty$.

Another potential one-way function, of interest in the analysis of algorithms, is exponentiation mod $q$, which was suggested to the authors by Prof. John Gill of Stanford University. The one-wayness of this functions has already been discussed in Section III.
