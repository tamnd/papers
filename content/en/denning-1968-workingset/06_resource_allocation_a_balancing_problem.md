---
paper: denning-1968-workingset
title: The Working Set Model for Program Behavior
authors:
  - Peter J. Denning
year: 1968
venue: Communications of the ACM
field: systems
section: "6"
section_title: 'Resource Allocation: A Balancing Problem'
tag: "0608"
kind: section
lang: en
source: https://doi.org/10.1145/800001.811670
pdf_sha256: 3585991156b07c7e878ea9dff16ef7721401adff09ee328f5ee247b016289e0f
pdf_pages: 8-10
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 63d9eb477c01f14e590ce14e2d49e8724ee6e93f561752be8a8c0a5f34183151
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

We have already pointed out that a computation places demands jointly on the processor and memory resources of a computer system. A computation's processor demand manifests itself as a process; its memory demand manifests itself as a working set. In this section we show how notions of "demand" can be made precise and how resource allocation can be formulated as a problem of balancing processor and memory demands against available equipment.

Demand. Our purpose here is to define "memory demand" and "processor demand," then combine these into the single notion "system demand."

We define the *memory demand* $m_i$ of computation $i$ to be

$$
m_i = \min \left( \frac{w_i}{M}, 1 \right), \qquad 0 \leq m_i \leq 1,
$$

where $M$ is the number of pages of main memory, and $w_i = \omega_i(t, \tau)$ is the working set count, such as maintained by the scheduler of Figure 7. If a working set contains more than $M$ pages (it is bigger than main memory), we regard its demand to be $m = 1$. Presumably $M$ is large enough so that the probability (over the ensemble of all processes) $\Pr[m = 1]$ is very small.

"Processor demand" is more difficult to define. Just as memory demand is in some sense a prediction of memory requirements in the immediate future, so processor demand should be a prediction of processor requirements for the

Figure.

Fig. 8. Probability density function for $q$ {#denning-1968-workingset-fig-8 .figure tag=0609}

$^4$ If a segment is shared, there will be an entry for it in the segment tables of each participating process; however, each entry points to the same page table. Each physical segment has exactly one page table describing it, but a name for the segment may appear in many segment tables.

near future. There are many ways in which processor demand could be defined. The method we have chosen, described below, defines a computation’s processor demand to be the fraction of a standard interval a process is expected to use before it blocks.

Let q be the random variable of processor time used by a process between interactions. (A process “interacts” when it communicates with something outside its name space, e.g. with a user, or with another process.) In general character, $f_q(z)$, the probability density function for q, is hyper-exponential (for a complete discussion, see Fife [16]):

$$
f_q(z) = cae^{-az} + (1 - c)be^{-bz}, \qquad 0 < a < b,
$$

$$
0 < c < 1,
$$

where $f_q(z)$ is diagrammed in Figure 8; most of the probability is concentrated toward small q (i.e. frequently interacting processes), but $f_q(z)$ has a long exponential tail.

Given that it has been $\gamma$ seconds (process time) since the last interaction, the conditional density function for the time beyond $\gamma$ until the next interaction is

$$
f_{q|\gamma}(z) = \frac{f_q(z + \gamma)}{\int_\gamma^\infty f_q(y) dy}
$$

$$
= \frac{cae^{-a(z+\gamma)} + (1 - c)be^{-b(z+\gamma)}}{ce^{-a\gamma} + (1 - c)e^{-b\gamma}}, \quad z \geq 0,
$$

which is just that portion of $f_q(z)$ for $q \geq \gamma$ with its area normalized to unity. The conditional expectation of q, given $\gamma$, is

$$
Q(\gamma) = \int_0^\infty zf_{q|\gamma}(z) dz
$$

$$
= \frac{(c/a)e^{-a\gamma} + [(1 - c)/b]e^{-b\gamma}}{ce^{-a\gamma} + (1 - c)e^{-b\gamma}}.
$$

The conditional expectation function $Q(\gamma)$ is shown in Figure 9. It starts at $Q(0) = c/a + [(1 - c)/b]$ and rises toward a constant maximum of $Q(\infty) = 1/a$. Note that, for large enough $\gamma$, the conditional expectation becomes independent of $\gamma$.

The conditional expectation $Q(\gamma)$ is a useful prediction function—if $\gamma$ seconds of processor time have been consumed by a process since its last interaction, we may expect $Q(\gamma)$ seconds of process time to elapse before its next interaction. It should be clear that the conditional expectation function $Q(\gamma)$ can be determined and updated automatically by the operating system.

In order to make a definition of processor demand “reasonable,” it is useful to establish symmetry between space and time. Just as we are unwilling to allocate more than M pages of memory, so we may be unwilling to allocate processor time for more than a standard interval A into the future. A can be chosen to reflect the maximum tolerable response time to a user: for if processor time is allocated to some set of processes such that their expected times till interactions total A, no process in that set expects to wait more than A time units before its own interaction.

We define the processor demand $p_i$ of computation i to be

$$
p_i = \frac{Q(t_i)}{NA}, \qquad \frac{Q(0)}{NA} \leq p_i \leq \frac{Q(\infty)}{NA},
$$

where N is the number of processors and $t_i$ is the time-used quantity for process i, such as maintained by the scheduler of Figure 7.

The (system) demand $\mathbf{D}_i$ of computation i is a pair

$$
\mathbf{D}_i = (p_i, m_i),
$$

where $p_i$ is its processor demand [eq. (21)] and $m_i$ its memory demand [eq. (17)].

That the processor demand is $p_i$ tells us to expect computation i to use $p_i$ of the processors for the next A units of execution time, before its next interaction.5 That the memory demand is $m_i$ tells us to expect computation i to use ($m_iM$) pages of memory during the immediate future.

Balance. Let constants $\alpha$ and $\beta$ be given. The computer system is said to be balanced if simultaneously

$$
\sum_{\text{processes in running list}} p = \alpha, \qquad 0 < \alpha \leq 1;
$$

and

$$
\sum_{\text{processes in running list}} m = \beta, \qquad 0 < \beta \leq 1,
$$

where p is a processor demand, m a memory demand, and $\alpha, \beta$ are constants chosen to cause any desired fraction of resource to constitute balance. If the system is balanced, the total demand presented by running processes just consumes the available fractions of processor and memory resources. Equation (23) defines “processor balance” and eq. (24) defines “memory balance.” We can write eqs. (23) and (24) in the more compact form

$$
S = \sum_{\text{processes in running list}} \mathbf{D} = (\alpha, \beta), \quad \mathbf{D} = (p, m),
$$

so that balance exists whenever eq. (25) holds; that is, whenever $S = (\alpha, \beta)$.

Figure.

Fig. 9. Conditional expectation function for q {#denning-1968-workingset-fig-9 .figure tag=060A}

5 A reasonable choice for the quantum $q_i$ (Fig. 7) granted to computation i might be $q_i = kQ(t_i)$, for some suitable constant $k \geq 1$.

Whenever the system is balanced, it means that $(\beta M)$ pages of memory have been committed to running computations, and that $(\alpha NA)$ units of processor time have been committed to running computations.

Dynamic maintenance of $S = \sum D$ is straightforward. Whenever a process of demand $(p, m)$ is admitted to the running list, $S + (p, m) \rightarrow S$. Whenever a process of demand $(p, m)$ exits the running list (except for page faults), $S - (p, m) \rightarrow S$. Therefore $S$ always measures the current total running list demand.

BALANCE POLICIES. A "balance policy" is a resource allocation policy whose objective is to keep the computer system in balance. Expressed as a minimization problem it is:

$$
\{\text{minimize } (S - (\alpha, \beta))\}.
$$

Instead of a priority in the ready list, a process has associated its demand $D$. In the event of imbalance, the next job (or set of jobs) to leave the ready list should be that whose demand comes closest to restoring balance. [Means of formulating this type of policy are currently under investigation as part of doctoral research into the whole problem of resource allocation.]

We do not wish to venture further here into the alluring problems of allocation policies; our aim is primarily to stimulate new thinking by sowing seeds of ideas. There are, however, three points we want to stress about policy (26):

(1) It is quite clear that system performance is particularly sensitive to overcommitment of memory: when too many working sets occupy main memory, each is displacing another's pages in an attempt to have its own pages present. This phenomenon, known as "thrashing," can easily result in a large number of programs stalled in the page-wait state, implying sticky congestion on the channel to auxiliary memory and serious degradation of service. It is, therefore, highly desirable first to balance memory, then to balance processor. That is, in the event of imbalance, the next job selected from the ready list should be the one that comes closest to restoring memory balance; if there are several jobs available to accomplish this purpose, the tie can be broken by selecting the one that comes closest to restoring processor balance.

(2) The balance criterion is basically an equipment utilization criterion. It is well known that equipment utilization and good response to users are not mutually-aiding criteria. As it stands, policy (26) will tend to favor jobs of small demand and discriminate against jobs of large demand; but with modifications and the methods suggested by Figure 7, together with proper adjustment of the "balance constants" $\alpha$ and $\beta$, it is possible to maintain "almost-balance" along with good service to users.

(3) Even with intuitively simple strategies such as balance, the allocation problem is far from trivial—interactions such as those between process and working set, and between balance and good service, are not yet fully understood.
