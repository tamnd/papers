---
paper: razborov-1997-naturalproofs
title: Natural Proofs
authors:
  - Alexander A. Razborov
  - Steven Rudich
year: 1997
venue: Journal of Computer and System Sciences
field: theory
section: "5"
section_title: One property of formal complexity measures
tag: "0222"
kind: section
lang: en
source: https://doi.org/10.1006/jcss.1997.1494
pdf_sha256: 6cf137cf878d01654aeff5dbf031e97a624cd72367b87415ff61080447de7682
pdf_pages: 19-22
extraction: vision
extraction_model: gpt-5
content_sha256: 44d1c6b9f892d0e94406ceda7d4e23ae48e0f0bd1fd2615e07d9b4cf59af9b09
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

A formal complexity measure (see e.g. [38, Section 8.8], [31]) is an integer-valued function on F n such that ( f ) 1 for f 2 f: x 1 ; : : : ; : x n ; x 1 ; : : : ; x n g and ( f g ) ( f ) +

$\mu(g)$ for all $f,g \in F_n$ and $* \in \{\wedge,\vee\}$. The meaning of this definition is that for every formal complexity measure $\mu$, $\mu(f)$ provides a lower bound on the formula size of $f$, and actually many known lower bounds, both for monotone and non-monotone formulae, can be viewed from this perspective. See the above- sources for examples. Also, for any approximation model $\mathcal{M}$ (see [39, 32] for most general definitions), we have $\rho(f * g,\mathcal{M}) \leq \rho(f,\mathcal{M})+\rho(g,\mathcal{M})+1$, hence $\rho(f,\mathcal{M})+1$ is a formal complexity measure.

In this section we show that any formal complexity measure $\mu$ which takes a large value at a single function, must take large values almost everywhere. In particular, every combinatorial property based on such a measure automatically satisfies the largeness condition in the definition of natural property.

More specifically, we have the following:

**Theorem 5.1.** Let $\mu$ be a formal complexity measure on $F_n$, and $\mu(f)=t$ for some $f \in F_n$. Then: {#razborov-1997-naturalproofs-thm-5-1 .statement tag=0223}

a) for at least $1/4$ fraction of all functions $g \in F_n$, $\mu(g) \geq t/4$;

b) for any $\epsilon=\epsilon(n)$ we have that for at least $(1-\epsilon)$ fraction of $g \in F_n$,

$$
\mu(g) \geq \Omega\left(\left(\frac{t}{(n+\log \frac{1}{\epsilon})^2}\right)\right)-n.
$$

In fact, the main argument used in the proof of this theorem is valid for arbitrary Boolean algebras, and we formulate it as a separate result since this might be of independent interest.

**Theorem 5.2.** Let $B$ be a finite Boolean algebra with $N$ atoms and $S \subseteq B$. {#razborov-1997-naturalproofs-thm-5-2 .statement tag=0224}

a) if $|S|>\frac{3}{4}|B|$ then every element of $B$ can be represented in the form

$$
(s_1 \wedge s_2) \vee (s_3 \wedge s_4); \quad s_i \in S\ (1 \leq i \leq 4);
\tag{9}
$$
{#razborov-1997-naturalproofs-eq-9 .equation tag=0229}

b) if $S$ contains all atoms and coatoms of $B$ then every element of $B$ can be represented in the form

$$
\bigvee_{i=1}^{\ell}\bigwedge_{j=1}^{\ell}s_{ij},
\tag{10}
$$
{#razborov-1997-naturalproofs-eq-10 .equation tag=022A}

where $s_{ij} \in S$ and $\ell \leq O\left(\log \frac{N\cdot |B|}{|S|}\right)$.

Proof ( of Theorem 5.1 from ) Theorem 5.2. Let S f g j ( g ) < t= 4 g for part a), and

S g ( g ) t , where is a suciently small constant, for part b). Note

( n +log 1 ) 2 that in part b) we may assume that t n +1 since otherwise there is nothing to

( n +log 1 ) 2 prove. Since ( V n p ) n and ( W n p ) n , where p is either x or : x , this implies i =1 i i =1 i i i i that S contains all atoms and coatoms of F n , the latter being viewed as a Boolean algebra.

Now, if j S j > 3 j B j in part a) or j S j j B j in part b), then we would apply Theorem

4 5.2 and represent f in the form (9), (10) respectively. This representation in both cases would imply the bound ( f ) < t , the contradiction.

Now we prove Theorem 5.2. Denote by b a randomly chosen element of B . Proof of Theorem 5.2 a). Fix b 0 2 B and consider the representation b 0 = ( b ^ ( : b b 0 )) _ ( : b ^ ( b b 0 )) :

As all four random variables b ; ( : b b 0 ) ; : b ; ( b b 0 ) are uniformly distributed on B and j S j > 3 j B j , for at least one particular choice b of b we have b; ( : b b ) ; : b; ( b b ) 2 S .

4 0 0 For proving part b) of Theorem 5.2 we need the following

Lemma 5.3. Let B be a nite Boolean algebra with N atoms and S B . Then there j j exists a subset S S of cardinality O (log N ) such that ^ S contains at most O log B {#razborov-1997-naturalproofs-lem-5-3 .statement tag=0225}

0 0 j S j atoms.

Proof of Lemma 5.3. Let us call an atom a good if P [ a s ] 2 = 3 and bad otherwise. Here s is picked at random from S .

Now, the standard entropy-counting argument gives us that there are at most j B j ! O log j S j bad atoms. An equally standard argument implies that if we take a random subset S 0 S of cardinality C log N , the constant C being suciently large, then for any good atom a , P [ a ^ S ] < N ? 1 . Hence, for at least one particular choice S of S , ^ S contains only

0 0 0 0 bad atoms, and the lemma follows.

Proof of Theorem 5.2 b). Denote j S j by . Once again, x b 2 B . Let us call j B j 0 c b 0 good if P [ b 2 S j b ^ b 0 = c ] 2 and bad otherwise. Note that b ^ b 0 is uniformly distributed on the Boolean algebra B 0 f c j c b 0 g . Hence

P [ c is good] 2 ; (11) where c is chosen from B 0 at random.

Now, x a good c 2 B 0 . The set B ( c ) f b 2 B j b ^ b 0 = c g is a Boolean algebra. Applying Lemma 5.3 to this algebra and to S := S \ B ( c ), we come up with S 0 S of cardinality O (log N ) such that c ^ S and ( ^ S n c ) has at most O log 1 atoms. We

0 0 extend S 0 by including to it the V corresponding coatoms and nd that every good c 2 B 0 can be represented in the form ` s ; s 2 S; ` O log N .

j =1 j j Next we apply the dual version of Lemma 5.3 to the Boolean algebra B 0 and W S := f c 2 B 0 j c is good g . In view of (11), the same argument as above yields that b 0 = `i =1 c i , where c i are either good or atoms. The statement follows.
