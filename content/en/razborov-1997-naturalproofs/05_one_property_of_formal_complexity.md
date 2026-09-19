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
section_title: '**One property of formal complexity measures**'
tag: "0222"
kind: section
lang: en
source: https://doi.org/10.1006/jcss.1997.1494
pdf_sha256: 6cf137cf878d01654aeff5dbf031e97a624cd72367b87415ff61080447de7682
pdf_pages: 19-22
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 25f8349a6282861c73e447b2b6f939c2fd10eacee7dfa197c0e3b9b3df27927f
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

A *formal complexity measure* (see e.g. [38, Section 8.8], [31]) is an integer-valued function $\mu$ on $F_n$ such that $\mu(f) \leq 1$ for $f \in \{-x_1, \ldots, -x_n, x_1, \ldots, x_n\}$ and $\mu(f * g) \leq \mu(f) +$

$\mu(g)$ for all $f, g \in F_n$ and $* \in \{\wedge, \vee\}$. The meaning of this definition is that for every formal complexity measure $\mu, \mu(f)$ provides a lower bound on the formula size of $f$, and actually many known lower bounds, both for monotone and non-monotone formulae, can be viewed from this perspective. See the above-cited sources for examples. Also, for any approximation model $\mathcal{M}$ (see [39, 32] for most general definitions), we have $\rho(f * g, \mathcal{M}) \leq \rho(f, \mathcal{M}) + \rho(g, \mathcal{M}) + 1$, hence $\rho(f, \mathcal{M}) + 1$ is a formal complexity measure.

In this section we show that any formal complexity measure $\mu$ which takes a large value at a single function, must take large values almost everywhere. In particular, every combinatorial property based on such a measure automatically satisfies the largeness condition in the definition of natural property.

More specifically, we have the following:

Theorem 5.1. Let $\mu$ be a formal complexity measure on $F_n$, and $\mu(f) = t$ for some $f \in F_n$. Then: {#razborov-1997-naturalproofs-thm-5-1 .statement tag=0223}

a) for at least $1/4$ fraction of all functions $g \in F_n$, $\mu(g) \geq t/4$;

b) for any $\epsilon = \epsilon(n)$ we have that for at least $(1 - \epsilon)$ fraction of $g \in F_n$,

$$
\mu(g) \geq \Omega \left( \frac{t}{\left( n + \log \frac{1}{\epsilon} \right)^2} \right) - n.
$$

In fact, the main argument used in the proof of this theorem is valid for arbitrary Boolean algebras, and we formulate it as a separate result since this might be of independent interest.

Theorem 5.2. Let $B$ be a finite Boolean algebra with $N$ atoms and $S \subseteq B$. {#razborov-1997-naturalproofs-thm-5-2 .statement tag=0224}

a) if $|S| > \frac{3}{4}|B|$ then every element of $B$ can be represented in the form

$$
(s_1 \wedge s_2) \vee (s_3 \wedge s_4); \quad s_i \in S \ (1 \leq i \leq 4);
$$

b) if $S$ contains all atoms and coatoms of $B$ then every element of $B$ can be represented in the form

$$
\bigwedge_{i=1}^{\ell} \bigwedge_{j=1}^{\ell} s_{ij},
$$

where $s_{ij} \in S$ and $\ell \leq O \left( \log \frac{N \cdot |B|}{|S|} \right)$.

**Proof of Theorem 5.1 from Theorem 5.2.** Let $S=\{g\mid \mu(g)<t/4\}$ for part a), and

$$
S=\left\{g\mid \mu(g)\leq\delta\cdot\frac{t}{(n+\log\frac{1}{\epsilon})^2}\right\},
$$

where $\delta$ is a sufficiently small constant, for part b). Note that in part b) we may assume that $\delta\cdot\frac{t}{(n+\log\frac{1}{\epsilon})^2}\geq n+1$ since otherwise there is nothing to prove. Since $\mu(\bigwedge_{i=1}^n p_i)\leq n$ and $\mu(\bigvee_{i=1}^n p_i)\leq n$, where $p_i$ is either $x_i$ or $\neg x_i$, this implies that $S$ contains all atoms and coatoms of $F_n$, the latter being viewed as a Boolean algebra.

Now, if $|S|\geq\frac{3}{4}|B|$ in part a) or $|S|\geq\epsilon|B|$ in part b), then we would apply Theorem 5.2 and represent $f$ in the form (9), (10) respectively. This representation in both cases would imply the bound $\mu(f)<t$, the contradiction.■

Now we prove Theorem 5.2. Denote by $b$ a randomly chosen element of $B$.

**Proof of Theorem 5.2 a).** Fix $b_0\in B$ and consider the representation

$$
b_0=(b\wedge(\neg b\oplus b_0))\vee(\neg b\wedge(b\oplus b_0)).
$$

As all four random variables $b$, $(\neg b\oplus b_0)$, $\neg b$, $(b\oplus b_0)$ are uniformly distributed on $B$ and $|S|>\frac{3}{4}|B|$, for at least one particular choice $b$ of $\mathbf{b}$ we have $b$, $(\neg b\oplus b_0)$, $\neg b$, $(b\oplus b_0)\in S$.■

For proving part b) of Theorem 5.2 we need the following

**Lemma 5.3.** Let $B$ be a finite Boolean algebra with $N$ atoms and $S\subset B$. Then there exists a subset $S_0\subset S$ of cardinality $O(\log N)$ such that $\bigwedge S_0$ contains at most $O\left(\log\frac{|B|}{|S|}\right)$ atoms. {#razborov-1997-naturalproofs-lem-5-3 .statement tag=0225}

**Proof of Lemma 5.3.** Let us call an atom $a$ good if $\mathbf{P}[a\leq s]\leq 2/3$ and bad otherwise. Here $s$ is picked at random from $S$.

Now, the standard entropy-counting argument gives us that there are at most

$$
O\left(\log\frac{|B|}{|S|}\right)
$$

bad atoms. An equally standard argument implies that if we take a random subset $S_0\subset S$ of cardinality $C\log N$, the constant $C$ being sufficiently large, then for any good atom $a$,

$$
\mathbf{P}[a\leq\bigwedge S_0]<N^{-1}.
$$

Hence, for at least one particular choice $S_0$ of $S_0$, $\bigwedge S_0$ contains only bad atoms, and the lemma follows.■

**Proof of Theorem 5.2 b).** Denote $\frac{|S|}{|B|}$ by $\epsilon$. Once again, fix $b_0\in B$. Let us call $c\leq b_0$ good if

$$
\mathbf{P}[b\in S\mid b\wedge b_0=c]\geq\frac{\epsilon}{2}
$$

and bad otherwise. Note that $b\wedge b_0$ is uniformly distributed on the Boolean algebra B 0 f c j c b 0 g . Hence

P [ c is good] 2 ; (11) where c is chosen from B 0 at random.

Now, x a good c 2 B 0 . The set B ( c ) f b 2 B j b ^ b 0 = c g is a Boolean algebra. Applying Lemma 5.3 to this algebra and to S := S \ B ( c ), we come up with S 0 S of cardinality O (log N ) such that c ^ S and ( ^ S n c ) has at most O log 1 atoms. We

0 0 extend S 0 by including to it the V corresponding coatoms and nd that every good c 2 B 0 can be represented in the form ` s ; s 2 S; ` O log N .

j =1 j j Next we apply the dual version of Lemma 5.3 to the Boolean algebra B 0 and W S := f c 2 B 0 j c is good g . In view of (11), the same argument as above yields that b 0 = `i =1 c i , where c i are either good or atoms. The statement follows.
