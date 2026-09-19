---
paper: lamport-1978-clocks
title: Time, Clocks, and the Ordering of Events in a Distributed System
authors:
  - Leslie Lamport
year: 1978
venue: Communications of the ACM
field: systems
section_title: Proof of the Theorem
kind: appendix
lang: en
source: https://lamport.azurewebsites.net/pubs/time-clocks.pdf
pdf_sha256: c55e7cab4230aa3d7126748a149b2db6f0d7a67296d5eccfdd50a210299a96b2
pdf_pages: 7-8
extraction: vision
extraction_model: gpt-5
content_sha256: 86412209fda4e70475569bb6e884a3cda7b1f5b164f09f570d77c09e2ec42ff7
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

### Appendix {#lamport-1978-clocks-s-appendix .section tag=096B}

For any $i$ and $t$, let us define $C_i^t$ to be a clock which is set equal to $C_i$ at time $t$ and runs at the same rate as $C_i$, but is never reset. In other words,

$$
C_i^t(t')=C_i(t)+\int_t^{t'}[dC_i(t)/dt]dt
\tag{1}
$$
{#lamport-1978-clocks-eq-1 .equation tag=0626}

for all $t' \ge t$. Note that

$$
C_i(t') \ge C_i^t(t')
$$

for all $t' \ge t$.

Suppose process $P_1$ at time $t_1$ sends a message to process $P_2$ which is received at time $t_2$ with an unpredictable delay $\le \xi$, where $t_0 \le t_1 \le t_2$. Then for all $t \ge t_2$ we have:

$$
C_2^t(t) \ge C_2^t(t_2)+(1-\kappa)(t-t_2)
$$

[by (1) and PC1]

$$
\ge C_1(t_1)+\mu_m+(1-\kappa)(t-t_2)
$$

[by IR2′(b)]

$$
=C_1(t_1)+(1-\kappa)(t-t_1)-[(t_2-t_1)-\mu_m]+ \kappa(t_2-t_1)
$$

$$
\ge C_1(t_1)+(1-\kappa)(t-t_1)-\xi.
$$

Hence, with these assumptions, for all $t\ge t_2$ we have:

$$
C_2^t(t)\ge C_1(t_1)+(1-\kappa)(t-t_1)-\xi.
\tag{3}
$$
{#lamport-1978-clocks-eq-3 .equation tag=0627}

Now suppose that for $i=1,\ldots,n$ we have $t_i\le t_i'<t_{i+1}$, $t_{i+1},t_0\le t_1$, and that at time $t_i$ process $P_i$ sends a message to process $P_{i+1}$ which is received at time $t_{i+1}$ with an unpredictable delay less than $\xi$. Then repeated application of the inequality (3) yields the following result for $t\ge t_{n+1}$:

$$
C_{n+1}^t(t)\ge C_1(t_1)+(1-\kappa)(t-t_1)-n\xi.
\tag{4}
$$
{#lamport-1978-clocks-eq-4 .equation tag=0628}

From PC1, IR1′ and 2′ we deduce that

$$
C_1(t_1')\ge C_1(t_1)+(1-\kappa)(t_1'-t_1).
$$

Combining this with (4) and using (2), we get

$$
C_{n+1}(t)\ge C_1(t_1)+(1-\kappa)(t-t_1)-n\xi
\tag{5}
$$
{#lamport-1978-clocks-eq-5 .equation tag=0629}

for $t\ge t_{n+1}$.

For any two processes $P$ and $P'$, we can find a sequence of processes $P=P_0,P_1,\ldots,P_{n+1}=P', n\le d$, with communication arcs from each $P_i$ to $P_{i+1}$. By hypothesis (b) we can find times $t_i,t_i'$ with $t_i'-t_i\le\tau$ and $t_{i+1}-t_i'\le\nu$, where $\nu=\mu+\xi$. Hence, an inequality of the form (5) holds with $n\le d$ whenever $t\ge t_1+d(\tau+\nu)$. For any $i,j$ and any $t,t_1$ with $t_1\ge t_0$ and $t\ge t_1+d(\tau+\nu)$ we therefore have:

$$
C_i(t)\ge C_j(t_1)+(1-\kappa)(t-t_1)-d\xi.
\tag{6}
$$
{#lamport-1978-clocks-eq-6 .equation tag=062A}

Now let $m$ be any message timestamped $T_m$, and suppose it is sent at time $t$ and received at time $t'$. We pretend that $m$ has a clock $C_m$ which runs at a constant rate such that $C_m(t)=t_m$ and $C_m(t')=t_m+\mu_m$. Then $|t'-t|\le\mu$ implies that $dC_m/dt\le1$. Rule IR2′(b) simply sets $C_j(t')$ to maximum $(C_j(t'-0),C_m(t'))$. Hence, clocks are reset only by setting them equal to other clocks.

For any time $t_x\ge t_0+\mu/(1-\kappa)$, let $C_x$ be the clock having the largest value at time $t_x$. Since all clocks run at a rate less than $1+\kappa$, we have for all $i$ and all $t\ge t_x$:

$$
C_i(t)\le C_x(t_x)+(1+\kappa)(t-t_x).
\tag{7}
$$
{#lamport-1978-clocks-eq-7 .equation tag=062B}

We now consider the following two cases: (i) $C_x$ is the clock $C_q$ of process $P_q$. (ii) $C_x$ is the clock $C_m$ of a message sent at time $t_1$ by process $P_q$. In case (i), (7) simply becomes

$$
C_i(t)\le C_q(t_x)+(1+\kappa)(t-t_x).
\tag{8i}
$$

In case (ii), since $C_m(t_1)=C_q(t_1)$ and $dC_m/dt\le1$, we have

$$
C_x(t_x)\le C_q(t_1)+(t_x-t_1).
$$

Hence, (7) yields

$$
C_i(t)\le C_q(t_1)+(1+\kappa)(t-t_1).
\tag{8ii}
$$

Since $t_x\ge t_0+\mu/(1-\kappa)$, we get

$$
C_q(t_x-\mu/(1-\kappa))\le C_q(t_x)-\mu
$$

[by PC1]

$$
\le C_m(t_x)-\mu
$$

[by choice of $m$]

$$
\le C_m(t_x)-(t_x-t_1)\mu_m/\nu_m
$$

[by $\mu_m\le\mu$ and $t_x-t_1\le\nu_m$]

$$
=T_m
$$

[by definition of $C_m$]

$$
=C_q(t_1)
$$

[by IR2′(a)].

Hence, $C_q(t_x-\mu/(1-\kappa))\le C_q(t_1)$, so $t_x-t_1\le\mu/(1-\kappa)$ and thus $t_1\ge t_0$.

Letting $t_1 = t_x$ in case (i), we can combine (8i) and (8ii) to deduce that for any $t, t_x$ with $t \geq t_x \geq t_0 + \mu/(1 - \kappa)$ there is a process $P_q$ and a time $t_1$ with $t_x - \mu/(1 - \kappa) \leq t_1 \leq t_x$ such that for all $i$:

$$
C_i(t) \leq C_q(t_1) + (1 + \kappa)(t - t_1).
$$

Choosing $t$ and $t_x$ with $t \geq t_x + d(\tau + \nu)$, we can combine (6) and (9) to conclude that there exists a $t_1$ and a process $P_q$ such that for all $i$:

$$
C_q(t_1) + (1 - \kappa)(t - t_1) - d\xi \leq C_i(t)
$$

$$
\leq C_q(t_1) + (1 + \kappa)(t - t_1)
$$

Letting $t = t_x + d(\tau + \nu)$, we get

$$
d(\tau + \nu) \leq t - t_1 \leq d(\tau + \nu) + \mu/(1 - \kappa).
$$

Combining this with (10), we get

$$
C_q(t_1) + (t - t_1) - \kappa d(\tau + \nu) - d\xi \leq C_i(t) \leq C_q(t_1)
$$

$$
+ (t - t_1) + \kappa[d(\tau + \nu) + \mu/(1 - \kappa)]
$$

Using the hypotheses that $\kappa \ll 1$ and $\mu \leq \nu \ll \tau$, we can rewrite (11) as the following approximate inequality.

$$
C_q(t_1) + (t - t_1) - d(\kappa \tau + \xi) \leq C_i(t)
$$

$$
\leq C_q(t_1) + (t - t_1) + d\kappa \tau.
$$

Since this holds for all $i$, we get

$$
|C_i(t) - C_j(t)| \leq d(2\kappa \tau + \xi),
$$

and this holds for all $t \geq t_0 + d\tau$.

Note that relation (11) of the proof yields an exact upper bound for $|C_i(t) - C_j(t)|$ in case the assumption $\mu + \xi \ll \tau$ is invalid. An examination of the proof suggests a simple method for rapidly initializing the clocks, or resynchronizing them if they should go out of synchrony for any reason. Each process sends a message which is relayed to every other process. The procedure can be initiated by any process, and requires less than $2d(\mu + \xi)$ seconds to effect the synchronization, assuming each of the messages has an unpredictable delay less than $\xi$.

Acknowledgment. The use of timestamps to order operations, and the concept of anomalous behavior are due to Paul Johnson and Robert Thomas.

Received March 1976; revised October 1977
