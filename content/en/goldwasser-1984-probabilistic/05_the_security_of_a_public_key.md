---
paper: goldwasser-1984-probabilistic
title: Probabilistic Encryption
authors:
  - Shafi Goldwasser
  - Silvio Micali
year: 1984
venue: Journal of Computer and System Sciences
field: security
section: "5"
section_title: THE SECURITY OF A PUBLIC KEY CRYPTOSYSTEM
tag: "07E8"
kind: section
lang: en
source: https://people.csail.mit.edu/silvio/Selected%20Scientific%20Papers/Encryption/Probabilistic_Encryption.pdf
pdf_sha256: b3d2f75d09da80c0bc3b39e3001ea3dd782b42af46df9c5bde0741f2dab7aa4a
pdf_pages: 13-21
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: f43e5591d95b3c442151656a0c07edeaf4f614b9ac3268b51965f90c399f6ea7
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

We proceed to discuss the notion of security of a public key cryptosystem. Clearly, the notion of security in a public key cryptosystem depends on the model of possible behavior of an adversary. In this paper the adversary is a passive *line-tapper*. This adversary knows the message space and its probability distribution, knows the encryption algorithm, is given the cyphertext, and tries, by computing, to retrieve the cleartext.

### 5.1. Polynomial Security {#goldwasser-1984-probabilistic-s5-1 .section tag=07E9}

Informal Setting

Let the message-finder $F$ and the line-tapper $T$ be your favorite computational model with polynomially bounded computational resources. Such $F$ and $T$ may be polynomial time Turing machines, probabilistic polynomial time Turing machine, "small" circuits etc. Intuitively, we say that a public key cryptosystem is polynomially secure if for all message spaces $M$ with any probability distribution, the encryption algorithms produced by the server will be such that: the polynomially bounded message finder $F$ cannot find two messages $m_1$ and $m_2$ in $M$ whose encryptions are distinguishable by the polynomially bounded line-tapper $T$. That is, given $\alpha$ (an encryption of either $m_1$ or $m_2$) $T$ should not have any advantage in understanding which of the two messages is being encoded by $\alpha$. Notice that there might very well be a pair of messages whose encryptions are distinguishable by $T$, but it will be impossible for the polynomially bounded $F$ to find such a pair. Note that PKCs generating deterministic encryption algorithms (e.g., RSA) cannot be polynomially secure.

In this paper, the message-finder and the line-tapper are chosen to be circuits.

Formal Setting

Let $\Pi$ be a PKC. Let MG be a message generator. We write $M_k$ for MG$k$. Without loss of generality, we assume that all $m \in M_k$ have the same length $l_k = Q(k)$ for some polynomial $Q$.

A k-line tapper is a circuit C with one Boolean output and enough Boolean inputs to receive (the description of an encryption algorithm) $E \in \Pi(k, MG)$ and $\alpha \in E(m)$, where $m \in M_k$ (see Fig. 1). Let $m_1, m_2 \in M_k$. Let $p_1^E$ be the probability with which C outputs 1 on inputs $E \in \Pi(k, MG)$ and $\alpha \in E(m_1)$ and $p_2^E$ be the probability with which C outputs 1 on inputs $E \in \Pi(k, MG)$ and $\alpha \in E(m_2)$. We say that C P-distinguishes $m_1$ from $m_2$ with respect to $E$ if $|p_1^E - p_2^E| > 1/P(k)$.

A k-message-finder is a circuit C with $2l_k$ Boolean outputs and enough Boolean inputs to describe an $E \in \Pi[k, MG]$. On input $E$, C outputs two messages $m_1, m_2 \in M_k$ (see Fig. 2).

Notice that $F_k$ may have a built-in description of MG.

Definition (Polynomially secure public key cryptosystems). Let $Q, P_1, P_2$ be polynomials. Let $\Pi$ be a public key cryptosystem and MG a message generator. Let $T = \{T_k\}$, where $T_k$ is a k-line-tapper with less than $Q(k)$ gates. Let $s_k^T$ be the size of a minimum size message-finder $F$ that with probability greater than $1/P_1(k)$ on input $E \in \Pi(k, MG)$ and MG outputs two messages $m_1$ and $m_2$ in $M_k$ such that $T_k$ $P_2$-distinguishes $m_1$ from $m_2$. We say that $\Pi$ is a polynomially secure with respect to MG if for any sequence of line-tappers $T$, $s_k^T$ grows faster than any polynomial in $k$. We say that $\Pi$ is a polynomially secure if for any message generator MG, $\Pi$ is polynomially secure with respect to MG.

Remark. Notice that in the definition of a polynomially secure public key cryptosystem we are not putting any constraints on the probability of $m_1$ and $m_2$. Thus, not even two messages that are very unlikely to occur and are distinguishable by $T_k$ can be easily found.

It is intuitive, and will be formally proved that polynomial security implies more traditional notions of security. Informally, if a public key cryptosystem is polynomially secure then no polynomially bounded line-tapper $T$ can, given the cyphertext, retrieve the cleartext or any partial information about it.

We first show that the newly introduced probabilistic PKCs are indeed polynomially secure.

Remarks about Theorem 5.1. The underlying idea of the proof of Theorem 5.1 is a sampling walk. Assume that every vertex $v$ in a $d$-dimensional hypercube $C$ is labeled with a real number $\lambda(v)$ in between 0 and 1 and that it is easy to find two vertices $u$ and $v$ such that $|\lambda(u) - \lambda(v)| > \varepsilon$. Then it is easy to find two adjacent vertices $s$ and $t$ such that $|\lambda(s) - \lambda(t)| > \varepsilon / d$: just find vertices $u$ and $v$ in $C$ such that $|\lambda(u) - \lambda(v)| > \varepsilon$; then consider $(\omega_0, ..., \omega_k)$, a minimum length vertex-walk from $u$ to $v$ and look at the pairs $(\omega_l, \omega_{l+1})$.

In our case, every vertex $v$ of the hypercube is a $d$-bit word. The label $\lambda(v)$ is the frequency with which the line-tapper outputs 1 on the probabilistic encryptions of $v$. We quickly approximate these frequencies by sampling. Then we find two adjacent words $s$ and $t$ with a jump in their associated frequency, and use $s$ and $t$ to approximate the UTP on which the system is based.

Theorem 5.1. Each probabilistic public key cryptosystem is polynomially secure. {#goldwasser-1984-probabilistic-thm-5-1 .statement tag=07EA}

Proof of Theorem 5.1. Let

$$
B = \{ B_i : \Omega_i \to \{0, 1\} \mid i \in S_k \text{ and } k \in N' \}
$$

be an unapproximable trapdoor predicate. Let $\Pi$ be a PPKC that on inputs $k$ and MG outputs $i \in S_k$ and $\sigma(i)$ with probability $1/|S_k|$. This specifies a probabilistic encryption algorithm $E$, as specified in Subsection 4.3. Recall, that $T_k$, the line-tapper, is a poly($k$) size circuit which upon receiving as input $i$ and a probabilistic encoding of $m$ in $M_k$ encoded using $B_i$, outputs either a 0 or a 1.

Let $f_{i,m}$ be the frequency with which $T_k$ outputs a 1 when given as input all the probabilistic encodings of $m$ using $B_i$.

Let $P_1$ and $P_2$ be polynomials. For $k \in N$ set

$$
\varepsilon_k = \frac{1}{P_1(k)} \quad \text{and} \quad \eta_k = \frac{1}{P_2(k)}
$$

and let $F_k$ be a message-finder. Let $N''$ be an infinite subset of $N'$. Assume that for a fraction $\eta_k$ of the $i \in S_k$ $F_k$ outputs two messages $m_1^i$ and $m_2^i$ such that

$$
|f_{i,m_1^i} - f_{i,m_2^i}| > \varepsilon_k.
$$

Then we will show that for all $k \in N''$, there is a probabilistic poly$(k, \delta^{-1})$ time Turing machine $G$ with oracles $F_k$ and $T_k$ that with probability $1 - \delta$, $(\varepsilon_k/5l_k)$-approximates $B_i$ for a fraction $\eta_k/2$ of the $i \in S_k$.

Consequently, as the size of $T_k$ is bounded by a polynomial in $k$, if also the size of $F_k$ were bounded by a polynomial in $k$, $G$ could easily be converted, for each $k \in N''$, into a poly$(k)$ size circuit $C_k$ that $(\varepsilon_k/5l_k)$-approximates $B_i$ for at least a fraction $\eta_k/2$ of the $i \in S_k$. This would contradict the unapproximability of $B$. Thus, the size of $F_k$ must grow faster than any polynomial in $k$ and $\Pi$ is polynomially secure.

The *Hamming distance* between $a$ and $b \in \{0, 1\}^{l_k}$ is the number of bits in which $a$ and $b$ differ, and we say that $a$ and $b$ are *adjacent* if the distance between them is 1.

We proceed to construct the Turing machine $G$. Let $\Omega_i^{l_k}$ denote the set of all $l_k$-long sequences of elements of $\Omega_i$. On input $i \in S_k$ and $y \in \Omega_i$, $G$ guesses $B_i(y)$ as follows:

*Part 1.* It calls the oracle $F_k$ with input $i$ to find $m_1^i$ and $m_2^i$ in $M_k$ such that

$$
|f_{i,m_1^i} - f_{i,m_2^i}| > \varepsilon_k.
$$

Let $\Delta$ be the distance between $m_1^i$ and $m_2^i$. Let $a_0, a_1, ..., a_\Delta$ be a sequence of $l_k$-bit strings such that $a_0 = m_1$, $a_\Delta = m_2$ and $a_j$ is adjacent to $a_{j+1}$ for $0 \leq j < \Delta$. As $|f_{i,m_1^i} - f_{i,m_2^i}| > \varepsilon_k$ there must exist $x, 0 \leq x \leq \Delta - 1$, such that $|f_{i,a_x} - f_{i,a_{x+1}}| > \varepsilon_k/l_k$.

Assign $\Omega_i$ and $\Omega_i^{l_k}$ the uniform probability distribution. By the trapdoor property of $B$, in probabilistic poly$(k, \delta^{-1})$ time, such $a_x$ and $a_{x+1}$ can be correctly found with probability greater than $1 - \delta$ by means of a Monte Carlo experiment. For notational convenience, let $s = a_x$ and $t = a_{x+1}$. Compute $f_{i,s}$ and $f_{i,t}$.

As $s = (s_1, ..., s_{l_k})$ and $t = (t_1, ..., t_{l_k})$ are adjacent, they differ in exactly one location. Call this location $d$.

*Part 2.* Assume, without loss of generality, that $f_{i,s} > f_{i,t}$.

*Case 1.* $s_d = 1, t_d = 0$.

Then, pick $x = (x_1, x_2, ..., x_{l_k}) \in \Omega_i^{l_k}$ at random among all the elements $e = (e_1, ..., e_{l_k})$ in $\Omega_i^{l_k}$ such that $B_i(e_j) = s_j = t_j$ for $j \neq d$ and $e_d = y$.

(Recall that $y$ is the input of $G$.)

if $T_k(x) = 1$ then $G[y] = 1$
else if $T_k(x) = 0$ then $G[y] = 0$.

*Case 2.* $s_d = 0$ and $t_d = 1$.

Proceed as in Case 1, but set $G[y] = 1 - T_k[x]$. This completes the description of $G$.

Let us prove that, if $s$ and $t$ have been correctly found, for a fraction $\eta_k/2$ of the $i$'s in $S_k$, for $y \in \Omega_i$,

$$
\Pr(G[y] = B_i[y]) > \frac{1}{2} + \frac{\varepsilon_k}{5l_k}.
$$

Remark 5.1. As $B$ is unapproximable, by Remark 3.1, for all sufficiently large $k$, for a fraction $1 - (\eta_k/2)$ of the $i \in S_k$, $|\Omega_i^0|/|\Omega_i| > \frac{1}{2} - (\varepsilon_k/4l_k)$ and $|\Omega_i^1|/|\Omega_i| > \frac{1}{2} - (\varepsilon_k/4l_k)$. Thus, for a fraction greater than $\eta_k(1 - (\eta_k/2)) > (\eta_k/2)$ of the $i$'s in $S_k$, $F_k$ outputs an $m_1^i$ and $m_2^i$ such that $|f_{i,m_1^i} - f_{i,m_2^i}| > \varepsilon_k$; AND both $|\Omega_i^0|/|\Omega_i|$ and $|\Omega_i^1|/|\Omega_i|$ are greater than $\frac{1}{2} - (\varepsilon_k/4l_k)$. {#goldwasser-1984-probabilistic-rem-5-1 .statement tag=07EB}

The $i$-signature$(x)$, where $x = (x_1, ..., x_{l_k}) \in \Omega_{i,k}^{l_k}$, will denote the binary string $B_i(x_1) \cdots B_i(x_{l_k})$. Then, for such $i$, in Case 1,

$$
\Pr(G[y] = B_i(y)) = \sum_{c=0,1} (\Pr(G[y] = c \mid B_i(y) = c) \Pr(B_i(y) = c))
$$

$$
> \left( \frac{1}{2} - \frac{\varepsilon_k}{4l_k} \right) [\Pr(G[y] = 1 \mid B_i(y) = 1) + \Pr(G[y] = 0 \mid B_i(y) = 0)]
$$

$$
= \left( \frac{1}{2} - \frac{\varepsilon_k}{4l_k} \right) [\Pr(T_k[x] = 1 \mid i\text{-signature}(x) = s)]
$$

$$
+ \Pr[T_k[x] = 0 \mid i\text{-signature}(x) = t]]
$$

$$
= \left( \frac{1}{2} - \frac{\varepsilon_k}{4l_k} \right) (f_{i,s} + (1 - f_{i,t}))
$$

$$
> \left( \frac{1}{2} - \frac{\varepsilon_k}{4l_k} \right) \left( 1 + \frac{\varepsilon_k}{l_k} \right)
$$

$$
> \frac{1}{2} + \frac{\varepsilon_k}{5l_k}.
$$

In Case 2, following a similar proof, again $G$ will $(\varepsilon_k/5l_k)$-approximate $B_i$.

### 5.2. Semantic Security {#goldwasser-1984-probabilistic-s5-2 .section tag=07EC}

In this section we define our second criteria of security for a public key cryptosystem, called Semantic Security. Informally, a system is semantically secure if whatever an eavesdropper can compute about the cleartext given the ciphertext, he can also compute without the ciphertext. We prove that every polynomially secure public key cryptosystem is semantically secure. Thus probabilistic PKCs are semantically secure. Thus, our encryption scheme passes a polynomially bounded version of Shannon's [23] perfect secrecy definition: Restricting our attention to adversaries with polynomially bounded resources available for the analysis of intercepted messages, the *a posteriori* probabilities of an intercepted cryptogram representing various messages, are the same as the *a priori* probabilities of the same messages before interception.

Informal Setting

Let $f$ be any function defined on a message space $M$. Thus $f$ need not be fast computable or even recursive. We say that $f(m)$ constitutes *information* about the message $m \in M$. In practice, typical $f$'s of interest are the identity function, a Boolean predicate, a hashing function, etc.

We want that extracting any information about messages from their encoding should be hard even if the probability distribution associated with the message space is known.

Let $M$ be a message space and $f$ be a function defined on $M$. For all $m \in M$, let $p_m = \operatorname{Prob}(x = m \mid x \in M)$. Consider the image $f(M)$. Define $p^M = \max_{v \in V} (\sum_{m \in f^{-1}(v)} p_m)$ and $v^M$ a value in $f(M)$ that achieves the maximum probability. Let $E$ be an encryption algorithm. Consider the following three games. Let $E$ be known to an adversary.

Game 1. Randomly pick $m \in M$ (each $x \in M$ has probability $p_x$ of being picked). In this game an adversary is asked to guess the value of $f(m)$ without being told what $m$ is.

If the adversary always guesses $v^M$ he would be right with probability $p^M$. There is no strategy for the adversary that would give him a better winning probability.

Game 2. Randomly pick $m \in M$. Compute one encryption $\alpha \in E(m)$. Give $\alpha$ to the adversary. Now, ask the adversary to guess $f(m)$.

Game 3. Let the adversary pick a function $f_E$ defined on $M$. Randomly pick $m \in M$. Compute one encryption $\alpha \in E(m)$. Give $\alpha$ to the adversary. Now, ask the adversary to guess $f_E(m)$.

Informally, we say that $\Pi$ is a semantically secure public key cryptosystem if the adversary cannot win Game 3 with higher probability than Game 1.

Formal Setting

Definition (Semantically secure public-key cryptosystems). Let $\Pi$ be a public key cryptosystem. Let MG be a message generator. As before $M_k = \mathrm{MG}[k]$. For all $m \in M_k$, $p_m$ will denote the probability that MG will output $m$ on input $k$. Let $f_{MG} = \{ f_E : M_k \to V \mid E \in \Pi(k, \mathrm{MG}), k \in N \}$ be a set of functions on MG. For each $E \in \Pi(k, \mathrm{MG})$ let $p_E = \max_{v \in V} (\sum_{m \in f_E^{-1}} p_m)$.

Let $C$ be a circuit that on input $E \in \Pi(k, \mathrm{MG})$ and $\alpha \in E(m)$, where $m \in M_k$ outputs a string $y$. Let $P, Q$ be polynomials. We say that $C$ $(P, Q, k)$-computes $f_{MG}$ from $\Pi$ if the $\operatorname{Prob}(y = f_E(m) \mid m \in M_k, \alpha \in E(m)) > p_E + (1/Q(k))$ for all $E$ belonging to a subset $S \subseteq \Pi(k, \mathrm{MG})$ having probability at least $1/P(k)$.

Let $P, Q$ be polynomials. Let $C_k^{Q,P}$ denote the size of a smallest size circuit $C$ that $(P, Q, k)$-computes $f_{MG}$ from $\Pi$.

We say that $\Pi$ is semantically secure if for all MG, for all $f_{MG}$, for all $P, Q$, $C_k^{P,Q}$ grows faster than any polynomial in $k$.

Theorem 5.2. Each polynomially secure public key cryptosystem is semantically secure. {#goldwasser-1984-probabilistic-thm-5-2 .statement tag=07ED}

Proof. Let $\Pi$ be a polynomially secure public key cryptosystem.
Assume for contradiction that $\Pi$ is not semantically secure. Then there are a message generator MG, a set of functions for MG, $f_{MG} = \{ f_E \}$, polynomials $P_1, P_2$ and $Q$, an infinite subset $N' \subseteq N$ and a sequence of circuits $\{ C_k \}$ such that:

(1) $C_k$ has less than $P_2(k)$ gates,
(2) the subset $S_k \subseteq \Pi(k, MG)$ has probability greater than $1/P(k)$, and
(3) for all $E \in S_k$ on inputs $E$ and $\alpha \in E(m)$, where $m \in MG[k]$, $C$ will output $f_E(m)$ with probability (taken over the input $\alpha$) greater than $p_E + (1/Q(k))$.

For the remaining part of the proof, $k$ will belong to $N'$ and $i$ to $S_k$. Let $\varepsilon_k = 1/Q(k)$ and $p_E = \max_{\nu \in V} \sum_{m \in f_E^{-1}(\nu)} p_m$.

Let $r_{m,y}^E$ denote the probability that $C_k$ outputs $y$ on inputs $E$ and $\alpha \in E(m)$. Then, $r_{m,f_E(m)}^E$ is the probability that $C_k$ correctly evaluates $f_E$ on inputs $E$ and $\alpha \in E(m)$.

Thus, what we assumed for contradiction can be expressed as

$$
\sum_{m \in M_k} p_m r_{m,f_E(m)}^E > p_E + \varepsilon_k.
$$

Pick $\mu$ from $M_k$ and fix it for the rest of the proof. Define $\overline{M} \subseteq M_k$ to be the set of messages $m$ such that

$$
|r_{m,\nu}^E - r_{\mu,\nu}^E| > \frac{\varepsilon_k^2}{10} \quad \text{for some } \nu \in V.
$$

We observe the following two lemmas.

Lemma A. For all constants $c > 0$, there exists a probabilistic poly($k$) time algorithm that on input $i \in S_k$ and $\xi \in \overline{M}$ finds a $\nu \in V$ such that

$$
|r_{\xi,\nu}^E - r_{\mu,\nu}^E| > \frac{\varepsilon_k^2}{20}
$$

with probability $1 - (1/k^c)$.

Proof. Construct a random sample of encodings of message $\xi$ using encryption algorithm $E$. Let $\{ x_1, ..., x_s \}$ denote this sample. Compute $C_k[E, x_j]$ for $1 \leq j \leq s$. Let

$$
I_\nu(x) = \begin{cases}
1 & \text{if } C_k[E, x] = \nu, \\
0 & \text{if } C_k[E, x] \neq \nu,
\end{cases}
$$

and set $\alpha_\nu = \sum_{1 < j < s} I_\nu(x_j)/s$ for all the $\nu \in V$ such that $C[E, x_j] = \nu$ for some $j$ between 1 and $s$. There are at most $s$ values in $V$ for which this frequency is nonzero.

Similarly, construct a random sample of encodings of message $\mu$ using encryption algorithm $E_1$. Let $\{ y_1, ..., y_s \}$ denote this sample. Set $\beta_\nu = \sum_{1 < j < s} I_\nu(y_j)/s$ for all the $\nu \in V$ such that $C_k[E, y_j] = \nu$ for some $j$ between 1 and $s$. Examine the two lists (each of size less than s) of $\alpha_v$'s and $\beta_v$'s. If there exists a $\bar{v}$ in at least one of the two lists such that $|\alpha_{\bar{v}} - \beta_{\bar{v}}| > 3\varepsilon_k^2/40$, output $\bar{v}$.

We claim that for an appropriate choice of sample size s this output is correct with probability $1 - 1/k^c$. The reasoning is as follows. Set $s = 1/(4[1/2k^c][\varepsilon_k^2/80]^2)$. Then, for the $v$'s such that $|r_{u,v}^E - r_{t,v}^E| > \varepsilon_k^2/10$. (Remember that such a $v$ exists as $\xi \in \bar{M}$), the weak law of large numbers guarantees that the,

$$
\operatorname{Prob}\left(|\alpha_v - r_{u,v}^E| < \frac{\varepsilon_k^2}{80}\right) > 1 - \frac{1}{2k^c}
$$

and

$$
\operatorname{Prob}\left(|\beta_v - r_{t,v}^E| < \frac{\varepsilon_k^2}{80}\right) > 1 - \frac{1}{2k^c}.
$$

And finally,

$$
\operatorname{Prob}\left(|\alpha_v - \beta_v| > \frac{3\varepsilon_k^2}{40}\right)
$$

$$
> \operatorname{Prob}\left(|\alpha_v - r_{u,v}^E| < \frac{\varepsilon_k^2}{80}\right) \cdot \operatorname{Prob}\left(|\beta_v - r_{t,v}^E| < \frac{\varepsilon_k^2}{80}\right)
$$

$$
> \left(1 - \frac{1}{2k^c}\right)^2 > 1 - \frac{1}{k^c}.
$$

And inversely, for a $v$ such that $|\alpha_v - \beta_v| > 3\varepsilon_k^2/40$, the

$$
\operatorname{Prob}\left(|r_{u,v}^E - r_{t,v}^E| > \frac{\varepsilon_k^2}{20}\right) > 1 - \frac{1}{k^c}.
$$

Lemma B. $\sum_{m \in \bar{M}} p_m > \varepsilon_k/10$.

Proof. Let $V_3 = \{v \in V \mid r_{u,v} > \varepsilon_k/6\}$, $V_4 = \{v \in V \mid r_{u,v} \leq \varepsilon_k/6\}$, and, respectively, $M_3 = \{m \in M_k - \bar{M} \mid r_{u,s_E(m)} > \varepsilon_k/6\}$ and $M_4 = M_k - \bar{M} - M_3$. $M_3$ includes all messages $m \notin \bar{M}$ such that $f_E(m) \in V_3$ and $M_4$ includes all messages $m \notin \bar{M}$ such that $f_E(m)$ is not in $V_3$. Clearly, $l = |V_3| < 6/\varepsilon_k$. Denote the values in $V_3$ as $\{v_1, ..., v_l\}$.

Then,

$$
p_E + \varepsilon_k < \sum_{m \in M_k} p_m r_{m,s_E(m)}^E
$$

$$
= \sum_{m \in \bar{M}} p_m r_{m,s_E(m)}^E + \sum_{m \in M_k - \bar{M}} p_m r_{m,s_E(m)}^E
$$

$$
\leq \sum_{m \in \bar{M}} p_m + \sum_{m \in M_3} p_m r_{m,s_E(m)}^E + \sum_{m \in M_4} p_m r_{m,s_E(m)}^E,
$$

which (since $\forall m \notin \overline{M}, |r_{m,f_E(m)}^E - r_{\mu,f_E(m)}^E| < \varepsilon_k^2/10$) is less than or equal to

$$
\sum_{m \in \overline{M}} p_m + \sum_{m \in M_3} p_m \left( r_{\mu,f_E(m)}^E + \frac{\varepsilon_k^2}{10} \right) + \sum_{m \in M_4} p_m \left( r_{\mu,f_E(m)}^E + \frac{\varepsilon_k^2}{10} \right)
$$

$$
= \sum_{m \in \overline{M}} p_m + \sum_{m \in f_E^{-1}(V_3)} p_m \left( r_{\mu,f_E(m)}^E + \frac{\varepsilon_k^2}{10} \right) + \sum_{m \in M_4} p_m \left( \frac{\varepsilon_k}{6} + \frac{\varepsilon_k^2}{10} \right)
$$

$$
\leq \sum_{m \in \overline{M}} p_m + \sum_{m \in f_E^{-1}(v_1)} p_m \left( r_{\mu,v_1}^E + \frac{\varepsilon_k^2}{10} \right)
$$

$$
+ \cdots + \sum_{m \in f_E^{-1}(v_l)} p_m \left( r_{\mu,v_1}^E + \frac{\varepsilon_k^2}{10} \right) + \left( \frac{\varepsilon_k}{6} + \frac{\varepsilon_k^2}{10} \right)
$$

$$
\leq \sum_{m \in \overline{M}} p_m + \left( \frac{\varepsilon_k}{6} + \frac{\varepsilon_k^2}{10} \right)
$$

$$
+ \left( \frac{l \varepsilon_k^2}{10} + (r_{\mu,v_1}^E + \cdots + r_{\mu,v_l}^E) \right) \cdot \max_{1 \leq j \leq l} \left\{ \sum_{m \in f_E^{-1}(v_j)} p_m \right\}
$$

$$
\leq \sum_{m \in \overline{M}} p_m + \left( \frac{\varepsilon_k}{6} + \frac{\varepsilon_k^2}{10} \right) + \frac{6 \varepsilon_k^2 p_E}{10 \varepsilon_k} + (r_{\mu,v_1}^E + \cdots + r_{\mu,v_l}^E) p_E
$$

$$
\leq \sum_{m \in \overline{M}} p_m + \left( \frac{\varepsilon_k}{6} + \frac{\varepsilon_k^2}{10} \right) + \frac{6 \varepsilon_k}{10} \cdot 1 + 1 \cdot p_E
$$

$$
\leq \sum_{m \in \overline{M}} p_m + p_E + \frac{13 \varepsilon_k}{15}.
$$

After rearranging both sides of the equation we get, $\sum_{m \in \overline{M}} p_m > \varepsilon_k/10$.

Lemmas A and B imply that for all $k \in N'$ there exists a poly($k$) circuit $F_k$ such that on input $E \in S_k$, $F_k$ produces two messages $m_1$ and $m_2$ in $M_k$ and a value $v$ in $f^{-1}(M_k)$ such that $|r_{m_1,v}^E - r_{m_2,v}^E| > \varepsilon_k^2/20$.

$F_k$ works as follows. On inputs $E$ it randomly picks a $\mu$ in $M_k$. Then, it randomly generates an element $\xi$ in $M_k$. (With probability at least $\varepsilon_k/10$, Lemma B tells us that $\xi \in \overline{M}$; if it is not, do not worry.) A $v \in V$ is then sought using Lemma A such that $|r_{\xi,v} - r_{\mu,v}| > \varepsilon_k^2/20$ with high probability. If such a $v$ is not found, it is probably because $\xi$ was not in $\overline{M}$ after all, and we pick another $\xi$ until success comes after an expected polynomial number of trials. If $v$ is found, set $m_1 = \xi$ and $m_2 = \mu$.

Now, define $T_k[i,x] = 1$ if $C_k[i,x] = v$ and 0 otherwise. Then $T_k$ is a poly($k$) linetapper that $(\varepsilon_k^2/20)$-distinguishes the two messages $m_1$ and $m_2$ found by $F_k$. This contradicts the hypothesis that $\Pi$ was a polynomially secure public key cryptosystem.
