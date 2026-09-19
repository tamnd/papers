---
paper: goldwasser-1985-zk
title: The Knowledge Complexity of Interactive Proof-Systems
authors:
  - Shafi Goldwasser
  - Silvio Micali
  - Charles Rackoff
year: 1985
venue: STOC
field: theory
section_title: Equivalent Do Body
kind: section
lang: en
source: https://people.csail.mit.edu/silvio/Selected%20Scientific%20Papers/Proof%20Systems/The_Knowledge_Complexity_Of_Interactive_Proof_Systems.pdf
pdf_sha256: 17b24f25b180ba64559a089efb443337c61c916078f73be4c496bf8d27410222
pdf_pages: 15-20
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 57ee6d12bba08ae6d9781eac840ad9b08e20b858734ca88e1e4cb00932bfeaf3
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

$$
\begin{align*}
u_{i+1} & := \text{a random quadratic residue mod } x. \\
bit_{i+1} & := \text{a random bit} \\
\text{IF } bit_{i+1} = f(x, y, H, v_i, u_{i+1}) & \text{ THEN} \\
& \text{IF } bit_{i+1} = 0 \text{ THEN } w_{i+1} := \text{a random square root mod } x \text{ of } u_{i+1} \text{ FI} \\
& \text{IF } bit_{i+1} = 1 \text{ THEN } w_{i+1} := \text{a random square root mod } x \text{ of } (u_{i+1}y) \text{ FI} \\
& \text{HALT and output } (u_{i+1}, bit_{i+1}, w_{i+1}) \\
& \text{FI}
\end{align*}
$$

It is clear that the equivalent body halts (and outputs) with probability $\frac{1}{2}$, and therefore that the actual DO loop halts in expected polynomial time. Since for each value of $u_{i+1}$ the equivalent body is equally likely to halt, $U'_{i+1}$ gets assigned (by the DO loop) a random quadratic residue. BIT'_{i+1} will be assigned $f(x, y, H, v_i, u_{i+1})$. Lastly, we can see from the equivalent body that in the case where the DO loop halts, $W'_{i+1}$ gets assigned a random square root of $u_{i+1}$ or of $(u_{i+1}y)$, depending on $bit_{i+1}$, as required.

6. Zero-knowledge proofs of quadratic nonresiduousity. We define QNR = $\{ (x, y) | y \in Z_n^*, (y/x) = 1, Q_x(y) = 1 \}$, where $x$ and $y$ are presented in binary.

Let $(A, B)$ be an interactive protocol given as input $(x, y)$ such that $|x| = m$.

The basic idea of the protocol is that $B$ generates at random elements $w$ of two types: $w \equiv r^2 \mod x$ (type 1) and $w \equiv r^2 y \mod x$ (type 2), and sends these elements to $A$. If $(x, y) \in \mathrm{QNR}$ then $A$ can tell of which type $w$ is by computing whether $w$ is a quadratic residue (type 1) or not (type 2). If $(x, y)$ is not a member of QNR, $w$ is always a quadratic residue mod $x$ and $A$ cannot guess its type better than guessing at random. Thus, $A$ will not be able to tell the types of the $w$'s and $B$ will not be convinced that $(x, y) \in \mathrm{QNR}$.

This idea is sufficient as a proof system but not as a zero-knowledge proof system. The danger is that $B$ may not have followed the protocol and generated elements $w$ in a manner differently than specified in the protocol. We get over this difficulty by complicating the protocol to force $B$ to convince $A$ that indeed $B$ knows whether $w$ is of type 1 or type 2. He does this by convincing $A$ that he knows either a square root of $w$ or a square root of $wy^{-1} \mod x$, without giving $A$ any information (in the information-theoretic sense) of which one he really knows.

Our original protocol, which appeared in [GMR], was more complex to prove than the one presented here. The simplified protocol presented here was suggested by Cohen [Co].

As was done for the QR language, we will first informally describe an interactive protocol, which we claim is a statistical zero-knowledge interactive proof system for QNR, and then describe it with more rigor.

The following $(A, B)$ protocol on input $(x, y)$ should be repeated $m$ times.

• $B$ picks at random $r \in \mathbb{Z}_x^*$ and $bit \in \{0, 1\}$. If $bit = 0$, $B$ sets $w = r^2 \mod x$; otherwise $B$ sets $w = r^2 y \mod x$. $B$ sends $w$ to $A$.
For $1 \leq j \leq m$, $B$ picks random $r_{j1}, r_{j2} \in \mathbb{Z}_x^*$ and a random $bit_j \in \{0, 1\}$. $B$ sets $a_j = r_{j1}^2 \mod x$, and $b_j = yr_{j2}^2 \mod x$. If $bit_j = 1$, $B$ sends $A$ the ordered pair, $pair_j = (a_j, b_j)$; else if $bit_j = 0$, $B$ sends to $A$ pair$_j = (b_j, a_j)$.
• $A$ sends $B$ an $m$-long random bit vector $i = i_1 i_2 \cdots i_m$.
• $B$ sends $A$ the sequence $v = v_1, v_2, \ldots, v_m$; if $i_j = 0$ then $v_j = (r_{j1}, r_{j2})$; if $i_j = 1$ then $v_j = rr_{j1} \mod x$ (a square root of $wa_j \mod x$) if $bit = 0$, and $v_j = yrr_{j2} \mod x$ (a square root of $wb_j \mod x$) if $bit = 1$.
(The intuition behind this step is as follows: if $i_j = 0$, then $B$ is convincing $A$ that pair$_j$ was chosen correctly; if $i_j = 1$, then $B$ is convincing that *if* pair$_j$ was chosen correctly, then $w$ was chosen correctly.)
• $A$ verifies that the sequence $v$ was properly constructed. If not, $A$ sends *terminate* to $B$ and halts. Otherwise, $A$ sets $answer = 0$ if $w$ is a quadratic residue mod $x$ and 1 otherwise. $A$ sends $answer$ to $B$.
• $B$ checks whether $answer = bit$. If so $B$ continues the protocol, otherwise $B$ rejects and halts.

After $m$ repetitions of this protocol, if $B$ did not reject thus far, $B$ accepts and halts.

More formally, we proceed to describe first the protocol for $B$ and then the protocol for $A$. The protocol consists of $B$ going through its first stage, followed by $A$'s first stage, followed by $B$'s second stage, followed by $A$'s second stage, etc., until either $A$ or $B$ chooses to terminate the protocol.

Denote by $v = \{v; v_j\}$ the result of extending sequence $v$ with element $v_j$.

*B's PROTOCOL ON INPUT* $(x, y)$.
Check that $x \geq 1$ and that $y \in \mathbb{Z}_x^*$ and that $(y/x) = 1$.
Set $m = |x|$.
Repeat Stages 1–3 $m$ times.
*Stage 1.*¹
use random bits to pick $r \in \mathbb{Z}_x^*$ and $bit \in \{0, 1\}$.
IF $bit = 0$ set $w \equiv r^2 \mod x$, else set $w \equiv r^2 y \mod x$ FI
FOR $j = 1, 2, \ldots, m$
choose random $r_{j1}, r_{j2} \in \mathbb{Z}_x^*$ and random $bit_j \in \{0, 1\}$.
set $a_j \equiv r_{j1}^2 \mod x$ and $b_j \equiv r_{j2}^2 y \mod x$.

¹ The careful reader may observe that picking $r \in Z_x^*$ "exactly at random" can be done in expected polynomial time, while our $B$ must by definition run in a fixed polynomial number of steps. Fortunately, $B$ can pick $r \in Z_x^*$ "almost at random" in a fixed polynomial time. This will have a negligible effect on the result and we omit any further details on this point.

IF $bit_j = 0$ set $pair_j = (a_j, b_j)$ else set $pair_j = (b_j, a_j)$ FI
END FOR
SEND ($w, pair_j$ for $j = 1, \cdots, m$) to $A$.
Stage 2.
GET from $A$ and $m$-long bit vector $i = i_1 \cdots i_m$, where $i_j \in \{0, 1\}$.
Initialize the sequence $v$ to the empty sequence.
FOR $j = 1, \cdots, m$
    IF $i_j = 0$ then set $v_j = (r_{j1}, r_{j2})$ and set $v = \{v; v_j\}$ FI
    IF $i_j = 1$ do one of the following:
        IF $bit = 0$ then set $v_j = rr_{j1} \mod x = \sqrt{w a_j} \mod x$ and set $v = \{v; v_j\}$
        otherwise set $v_j = yrr_{j2} \mod x = \sqrt{w b_j} \mod x$ and set $v = \{v; v_j\}$ FI
    FI
END FOR
SEND $v$ to $A$.
Stage 3.
GET $answer \in \{0, 1\}$ from $A$.
IF $answer \neq bit$ then reject and halt
otherwise go to stage 1 FI.
After $m$ iterations of Stages 1–3, if the protocol has not halted by now, accept and halt.

A’s PROTOCOL ON INPUT $(x, y) \in \mathrm{QNR}$.

Stage 1.
GET ($w, pair_j$ for $j = 1, \cdots, m$) from $B$.
Pick at random $i = i_1 \cdots i_m$ where $i_j \in \{0, 1\}$.
SEND $i$ to $B$.
Stage 2.
GET sequence $v$ from $B$
for every $j = 1, \cdots, m$ check that, if $i_j = 0$, then $v_j$ is a pair $(s, t)$ such that $(s^2 \mod x, t^2 y \mod x)$ equals $pair_j$, possibly with the elements interchanged; and if $i_j = 1$, then $(v_j^2) w^{-1} \mod x$ is a member of $pair_j$. If not, SEND terminate to $B$ and halt.
(Assume that the above checks have succeeded.)
If $w$ is a quadratic residue mod $x$, set $answer = 0$ and if $w$ is a quadratic nonresidue mod $x$, set $answer = 1$.
SEND $answer$ to $B$.
Go to Stage 1.

We first prove that $(A, B)$ is an interactive proof system for QNR.

CLAIM 2. $(A, B)$ is an interactive proof system for QNR.

Proof. Clearly $(A, B)$ is an interactive protocol. If $(x, y) \in \mathrm{QNR}$ and $A$ and $B$ follow the specification of the protocol, then for every execution of Stages 1–2 by $B$, $w$ is a quadratic nonresidue mod $x$ if and only if $bit = 1$. Thus, in $A$'s Stage 2, $A$ can always decide whether $w$ is a quadratic residue mod $x$ or not and send $answer$ to $B$ such that $answer = bit$ and $B$ will always accept.

Suppose that $(x, y)$ not in QNR (i.e., $y$ is a quadratic residue mod $x$) and that $B$ is interacting with an arbitrary prover $A'$, in the $k$th iteration of Stages 1–3. Then we claim that even an $A'$ with infinite computation power cannot distinguish an interaction with $B$ where $bit = 0$ from an interaction with $B$ where $bit = 1$. This is argued as follows. At Stage 1, $A'$ gets the list $(w, pair_j$ for $j = 1, \cdots, m)$, where $w$ is a random quadratic residue, and where $pair_j$ simply consists of a pair of random quadratic residues. This gives absolutely no information about the value of $bit$.

Now consider Stage 2, where $i_j = 0$. $A$ gets $(r_{j1}, r_{j2})$. Note that $r_{j1}$ is just a random square root of $a_j$ and $r_{j2}$ is a random square root of $b_j / y \mod x$. So all that $A$ sees is the result of randomly choosing (or not) to reorder pair$_j$, and then taking a random square root of the first element and a random square root of the result of dividing the second element by $y$ (all mod $x$, of course). This gives no information about *bit*.

Now consider the case where $i_j = 1$. If $bit = 0$ then $A$ gets $rr_{j1} \mod x$, which is a random square root of $wa_j \mod x$. If $bit = 1$ then $A$ gets $yrr_{j2} \mod x$, which is a random square root of $wb_j \mod x$. Since pair$_j$ is a random reordering of $(a_j, b_j)$, $v_j$ is equally likely to be a random square root of $w$ times the first element of pair$_j$ as it is to be a random square root of $w$ times the second element of pair$_j$, no matter what *bit* is.

Thus, from the information that $A'$ receives in Stages 1 and 2, the value of *bit* is as likely to be 0 as it is to be 1 and the chance that $A'$ predicts *bit* correctly is no greater than $\frac{1}{2}$. In $m$ iterations through Stages 1–3, the probability that $A'$ computed *answer* such that *answer* = *bit* is at most $1/2^m$.

Proving that the $(A, B)$ proof system is statistically zero-knowledge for QNR is much more complex.

**Theorem 2.** *The above protocol $(A, B)$ is a statistically zero-knowledge proof system for QNR.* {#goldwasser-1985-zk-thm-2 .statement tag=052A}

*Proof.* Let $B'$ be an arbitrary probabilistic polynomial time interactive Turing machine interacting with $A$. Let $(x, y) \in \mathrm{QNR}$ be input to $(A, B')$, let $m = |x|$, and let $H$ be the extra input to $B'$.

For convenience, consider the random variable $\mathrm{View}_{A,B'}((x, y), H)$ ($B'$'s view of an iteration of the protocol) to consist of the random variables:

$$
\mathrm{RAN}, \quad \text{and}
$$

$$
\{ W^k, \{ \mathrm{PAIR}_j^k : 1 \leq j \leq m \}, \{ I_j^k : 1 \leq j \leq m \}, V^k, \mathrm{ANSWER}^k | 1 \leq k \leq m \}.
$$

$\mathrm{RAN}$ is the string of random bits generated by $B'$; $W^k$ takes on the value of $w$ in the $k$th iteration of the protocol; $\mathrm{PAIR}_j^k$ takes on the value of pair$_j$ in the $k$th iteration of the protocol; $I_j^k$ takes on the value of $i_j$ in the $k$th iteration of the protocol; $V^k = \{ V_j^k \}$ takes on the value of the sequence $v$ in the $k$th iteration of the protocol; and $\mathrm{ANSWER}^k$ takes on the value of *answer* in the $k$th iteration of the protocol.

For simplicity (notational and otherwise) we concentrate on showing that a single iteration of the protocol is zero-knowledge. Doing the general case implies carrying along the view of the protocol so far as was done in the proof of Theorem 1. Thus, from here on we drop all superscripts and work with the random variables: RAN, $W$, $\{ \mathrm{PAIR}_j \}$, $\{ I_j \}$, $V = \{ V_j \}$, and ANSWER.

Note that in a good execution of the protocol (namely, if $B'$'s protocol is followed), we expect that $W = r^2 \mod x$ or $W = r^2 y \mod x$, where $r$ is a substring of RAN; and that $\mathrm{PAIR}_j = (r_{j1}^2 \mod x, r_{j2}^2 y \mod x)$ or $(r_{j2}^2 y \mod x, r_{j1}^2 \mod x)$, where $r_{j1}$ and $r_{j2}$ are substrings of RAN; and that for all $1 \leq j \leq m$, if $I_j = 0$ then $V_j$ will equal $(r_{j1}, r_{j2})$; and if $I_j = 1$ then $V_j = rr_{j1} \mod x$ or $yrr_{j2} \mod x$.

However, since $B'$ may not follow the protocol, all we can say about these random variables is that RAN is a random binary string; $W$ (and $\mathrm{PAIR}_j$) are assigned values $w$ (and pair$_j$) computed by $B'$ on inputs $x, y, H$ and RAN; $I$ is a random binary string of length $m$; and $V_j$ is a value computed by $B'$ on inputs $x, y, H, \mathrm{RAN}, I$.

We will now describe a probabilistic Turing machine $M$ that, given $(x, y) \in \mathrm{QNR}$ and $H$, runs in expected polynomial time, and whose output distribution is statistically indistinguishable from $\mathrm{View}_{A,B'}((x, y), H)$.

M starts by outputting a random string ran of the appropriate length and running B' on inputs (x, y, H), and random tape ran on it. B' goes through Stage 1 outputting w, pair_j, for $1 \leq j \leq m$.
Next, M chooses $i_1, \ldots, i_m$ at random in {0, 1}, sets $i = i_1 \cdots i_m$, and writes i on B's communication tape, activating B's Stage 2.
B' goes into Stage 2, writing on its communication tapes a sequence $v = \{ v_i \}$. M outputs $w\{pair_j\}, i, v$.
Next M does the checking that A does in Stage 2.
If the check fails M outputs "terminate" and halts.

Let us assume that the check succeeds. Think of x, y, H, ran as being fixed, so that w and {pair_j} are also fixed. The fact that the check succeeds means that A sending i to B' causes B' to send a v to A, which causes A to send a one-bit answer to B' (rather than terminate); let us call any such i' special. M has just computed that i is special, and now wants to compute the value of answer that A would send. This value is 0 if w is a quadratic residue mod x, and 1 otherwise. Since B' may not have computed w the way B would have, it is not obvious how to compute the quadratic residuosity of w, i.e., answer.

It turns out that finding one other special string $i' \neq i$ will allow M to determine if w is a quadratic residue, as follows:

Say that $i_j = 0$ and $i'_j = 1$ and i, i' are special. Let $v, v'$ be the sequences sent by B' after receiving i or i' (respectively); these can be computed in polynomial time by running B'. Since $i_j = 0$, $v_j = (s, t)$, where $(s^2 \mod x, t^2 y \mod x)$ equals pair_j, possibly with the elements reversed. Since $i'_j = 1$, $(v_j)^2 w^{-1} \mod x \in \text{pair}_j$. If $(v_j)^2 w^{-1} \mod x = s^2 \mod x$, then w is a quadratic residue mod x; if $(v_j)^2 w^{-1} \mod x = t^2 y \mod x$ then w is a quadratic nonresidue mod x.

It therefore remains to find a special $i' \neq i \mod x$. M uses the following algorithm.

ALGORITHM TO FIND A SPECIAL $i' \neq i$.

Test $2^m$ random $i'$ of length m (with replacement), halting when either a special $i' \neq i$ is found, or when $2^m$ strings have been tried. If no special $i' \neq i$ has been found, then test all m-bit strings (in order), looking for a special $i' \neq i$.

If a special $i' \neq i$ is found, then M calculates answer as explained above and outputs answer. If no such $i'$ exists, then M outputs "?"; note that this will happen when i is the only special string.

In order to show that M operates in expected polynomial time, it is sufficient to show that M operates in expected polynomial time for each fixed value of (x, y, H, ran). Say that x, y, H, ran are fixed, and so w, pair are also fixed. Let k be the number of strings i that are special. If $k = 0$, then the ALGORITHM TO FIND A SPECIAL $i'$ will not be invoked, and the running time is clearly polynomial in m. If $k = 1$, then with probability $(1/2^m)$ M will choose a special i; in that case the ALGORITHM will run for time $2^m m^c$ (for some c), so the expected running time is $(1/2^m)2^m m^c +$ a polynomial in m.

Assume that $k > 1$. M will choose a special i with probability $k/2^m$. To calculate an upper bound on the expected running time of the ALGORITHM, imagine that it was changed so that it tested random $i'$, including i and with replacement, halting if and when a special $i' \neq i$ is found; the expected running time would be at least half that of the ALGORITHM. In effect, a coin is being tossed until "heads" comes up, where the probability of "heads" is exactly $(k-1)/2^m$. It is well known that the expected number of coin tosses is exactly $2^m/(k-1)$. Hence the expected time for the

ALGORITHM is $\leq (2^m/(k-1))m^c$ (for some $c$). The total expected time is $\leq (k/2^m)-(2^m/(k-1))m^c+$ a polynomial in $m$, which is polynomial in $m$.

Recall that $M((x,y),H)$ is the random variable denoting the distribution of $M$'s output given $x,y,H$. It remains to show that $M$ is statistically close to $\mathrm{View}_{A,B'}((x,y),H)$. Fix $x,y,H$. If $ran$ is such that the number of special strings is not exactly 1, then any output string $\alpha$ beginning with $ran$ is taken on by $\mathrm{View}_{A,B'}((x,y),H)$ with exactly the same probability as by $M((x,y),H)$. Let $S$ be the set of $(ran,w,\{pair\},i,u,answer)$ where $i$ is the unique special string determined by $ran$. The probability that $\mathrm{View}_{A,B'}((x,y),H)$ takes on a value in $S$ is $\leq 1/2^m$, since for each $ran$ there is at most one $i$, which will be the unique special string. Similarly, the probability that $M((x,y),H)$ takes on a value in $S$ is $\leq 1/2^m$. Thus,

$$
\sum_{\alpha}\left|\operatorname{prob}(M((x,y),H)=\alpha)-\operatorname{prob}(\mathrm{View}_{A,B'}((x,y),H)=\alpha)\right|
$$

$$
=\sum_{\alpha\notin S}\left|\operatorname{prob}(M((x,y),H)=\alpha)-\operatorname{prob}(\mathrm{View}_{A,B'}((x,y),H)=\alpha)\right|
$$

$$
+\sum_{\alpha\in S}\left|\operatorname{prob}(M((x,y),H)=\alpha)-\operatorname{prob}(\mathrm{View}_{A,B'}((x,y),H)=\alpha)\right|
$$

$$
\leq 0+\frac{1}{2^m}+\frac{1}{2^m}=\frac{2}{2^m}.
$$

And for $m$ iterations of the protocol, the difference is

$$
\sum_{\alpha}\left|\operatorname{prob}(M((x,y),H)=\alpha)-\operatorname{prob}(\mathrm{View}_{A,B'}((x,y),H)=\alpha)\right|\leq\frac{2m}{2^m}.
$$

This completes our proof. □

*Remarks.* In fact, the above protocol can be shown to be perfect zero-knowledge. We just have to change $M$ so that when it discovers that $i$ is the unique special string it factors $x$ in time roughly $2^m$, and then determines if $w$ is a quadratic residue mod $x$ in polynomial time. This does not change the expected running time by more than a polynomial factor, since when $M$ decides to do this extra work, it has already spent time $2^m$.
