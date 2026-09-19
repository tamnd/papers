---
paper: denning-1968-workingset
title: The Working Set Model for Program Behavior
authors:
  - Peter J. Denning
year: 1968
venue: Communications of the ACM
field: systems
section: "3"
section_title: Working Set Model
tag: 036E
kind: section
lang: en
source: https://doi.org/10.1145/800001.811670
pdf_sha256: 3585991156b07c7e878ea9dff16ef7721401adff09ee328f5ee247b016289e0f
pdf_pages: 4-7
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: abe3833966feef14e40684f9d7ef6f035bf5a9b63ec7182b60a77c886ea84630
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

From the programmer's standpoint, the working set of information is the smallest collection of information that must be present in main memory to assure efficient execution of his program. We have already stressed that there will be no advance notice from either the programmer or the compiler regarding what information "ought" to be in main memory. It is up to the operating system to determine, on the basis of page reference patterns, whether pages are in use. Therefore the working set of information associated with a process is, from the system standpoint, the set of most recently referenced pages.

We define the working set of information $W(t, \tau)$ of a process at time $t$ to be the collection of information referenced by the process during the process time interval $(t - \tau, t)$.

Thus, the information a process has referenced during the last $\tau$ seconds of its execution constitutes its working set (Figure 2). $\tau$ will be called the working set parameter. We

Figure.

Fig. 2. Definition of $W(t, \tau)$ {#denning-1968-workingset-fig-2 .figure tag=036F}

regard the elements of $W(t, \tau)$ as being pages, though they could just as well be any other named units of information. The working set size $\omega(t, \tau)$ is

$$
\omega(t, \tau) = \text{number of pages in } W(t, \tau).
$$

Let the random variable $x$ denote the process-time interval between successive references to the same page; let $F_x(\alpha) = \Pr[x \leq \alpha]$ be its distribution function; let $f_x(\alpha) = dF_x(\alpha)/d\alpha$ be its density function; and $\bar{x}$ denote its mean:

$$
\bar{x} = \int_0^{\infty} \alpha f_x(\alpha) d\alpha.
$$

These interreference intervals $x$ are useful for expressing working set properties.

A working set $W(t, \tau)$ has four important, general properties. All are properties of typical programs and need not hold in special cases. During the following discussion of these properties, assume that $W(t, \tau)$ is continuously in main memory, that its process is never interrupted except for page faults, that a page is removed from main memory the moment it leaves $W(t, \tau)$, and that no two working sets overlap (there is no sharing of information).

P1. Size. It should be clear immediately that $\omega(t, 0) = 0$ since no page reference can occur in zero time. It should be equally clear that, as a function of $\tau$, $\omega(t, \tau)$ is monotonically increasing, since more pages can be referenced in longer intervals. $\omega(t, \tau)$ is concave downward. To see this, note that

$$
W(t, 2\tau) = W(t, \tau) \cup W(t - \tau, \tau),
$$

which implies that

$$
\omega(t, 2\tau) \leq \omega(t, \tau) + \omega(t - \tau, \tau).
$$

Assuming statistical regularity, $\omega(t, \tau)$ behaves on the average like $\omega(t - \tau, \tau)$, so that on the average

$$
\omega(t, 2\tau) \leq 2\omega(t, \tau).
$$

The general character of $\omega(t, \tau)$ is suggested by the smoothed curve of Figure 3.

Figure.

Fig. 3. Behavior of $\omega(t, \tau)$ {#denning-1968-workingset-fig-3 .figure tag=0370}

P2. Prediction. We expect intuitively that the immediate past page reference behavior of a program constitutes a good prediction of its immediate future page reference behavior: for small time separations $\alpha$, the set $W(t, \tau)$ is a good predictor for the set $W(t + \alpha, \tau)$. To see this more clearly, suppose $\alpha < \tau$. Then

$$
W(t + \alpha, \tau) = W(t + \alpha, \alpha) \cup W(t, \tau - \alpha).
$$

Because references to the same page tend to cluster in time, the probability

$$
\Pr[W(t + \alpha, \alpha) \cap W(t, \tau) = \varphi]
$$

tends to be small. Therefore some pages of $W(t, \tau)$ will still be in use after time $t$ (i.e. pages in $W(t + \alpha, \alpha)$; since also

$$
W(t, \tau - \alpha) \subseteq W(t, \tau) \cap W(t + \alpha, \tau),
$$

$W(t, \tau)$ is a good predictor for $W(t + \alpha, \tau)$. On the other hand, for large time separations $\alpha$ (say, $\alpha \gg \tau$) control will have passed through a great many program modules during the interval $(t, t + \alpha)$, and $W(t, \tau)$ is not a good predictor for $W(t + \alpha, \tau)$.

P3. *Reentry Rate.* As $\tau$ is reduced, $\omega(t, \tau)$ decreases, so the probability that useful pages are not in $W(t, \tau)$ increases; correspondingly the rate at which pages are recalled to $W(t, \tau)$ increases. We define two functions: a process-time reentry rate $\lambda(\tau)$ defined so that the mean process time between the instants at which a given page reenters $W(t, \tau)$ is $1/\lambda(\tau)$, and a real-time reentry rate $\varphi(\tau)$ defined so that the mean real-time between the instants at which a given page reenters $W(t, \tau)$ is $1/\varphi(\tau)$.

Let $\{t_n\}_{n \geq 0}$ be a sequence of instants in process time at which successive references to a given page occur. The $n$th interreference interval is $x_n = t_n - t_{n-1}$; but we are assuming the interreference intervals $\{x_n\}_{n \geq 1}$ are independent, identically distributed random variables, so that for all $n \geq 1$, $f_{x_n}(\alpha) = f_x(\alpha)$. A *reentry point* is a reference instant which finds the page not in $W(t, \tau)$: at such an instant the page reenters $W(t, \tau)$. The reference instant $t_n$ is a reentry point if $x_n > \tau$, independently of other reference instants. Suppose $t_0$ is a reentry point; we are interested in $\pi_n$, the probability that $t_n$ is the first reentry point after $t_0$. The probabilities $\{\pi_n\}_{n \geq 1}$ are distributed geometrically:

$$
\pi_n = \Pr[t_n \text{ first reentry after } t_0] = \zeta^{n-1}(1-\zeta),
$$

where $\zeta = \Pr[x \leq \tau] = F_x(\tau)$. That is, $t_n$ is the first reentry after $t_0$ if all the instants $\{t_1, \cdots, t_{n-1}\}$ are not reentry instants, and $t_n$ is a reentry. The expected number $\bar{n}$ of reference instants until the first reentry is

$$
\bar{n} = \sum_{n=1}^{\infty} n \pi_n = \frac{1}{1-\zeta}.
$$

Each reference interval is of expected length $\bar{x}$ [eq. (2)], so the mean time $m(\tau)$ between reentries is $m(\tau) = \bar{n} \bar{x}$. Therefore

$$
m(\tau) = \frac{\bar{x}}{1 - F_x(\tau)}.
$$

We define the *reentry rate* $\lambda(\tau)$ to be

$$
\lambda(\tau) = \frac{1}{m(\tau)} = \frac{1 - F_x(\tau)}{\bar{x}},
$$

where $\lambda(\tau)$ is the average process-time rate at which one page is reentering $W(t, \tau)$.

Assuming that storage management mechanisms retain in main memory only the pages of $W(t, \tau)$, every page reentering $W(t, \tau)$ must be recalled from auxiliary memory and contributes to page traffic; we here estimate this contribution. In an interval $A$ of process time, the expected number of times a single page reenters $W(t, \tau)$ is $A \lambda(\tau)$; each reentry causes the process to enter a "page-wait" state for one traverse time $T$, a total of $(A \lambda(\tau) T)$ seconds spent in page wait. Therefore the total real-time spent to recall a page $A \lambda(\tau)$ times is $(A + A \lambda(\tau) T)$. The *return traffic rate* $\varphi(\tau)$ is

$$
\varphi(\tau) = \frac{A \lambda(\tau)}{A + A \lambda(\tau) T},
$$

that is,

$$
\varphi(\tau) = \frac{\lambda(\tau)}{1 + \lambda(\tau) T},
$$

where $\varphi(\tau)$ estimates the average real-time rate at which one page is reentering $W(t, \tau)$. That is, the mean real-time between reentries is $1/\varphi(\tau)$.

Later in the paper we define "memory balance," a condition in which the collection of working sets residing in main memory at any time just consumes some predetermined portion $\beta$ of the available $M$ pages of main memory. That is, on the average,

$$
\sum_{\text{working sets in main memory}} \omega(t, \tau) = \beta M.
$$

In this case, the average number of pages in memory belonging to working sets is $\beta M$; we define the *total return traffic rate* $\Phi(\tau)$ to be the total reentry rate in real-time to main memory, when the working sets contained therein are not interrupted except for page waits:

$$
\Phi(\tau) = \beta M \varphi(\tau) = \frac{\beta M \lambda(\tau)}{1 + \lambda(\tau) T},
$$

where $\Phi(\tau)$ estimates the average number of pages per unit real-time returning to main memory from auxiliary memory. Since "memory balance" is an equilibrium condition, there must also be a flow of pages $\Phi(\tau)$ from main to auxiliary memory. Therefore $2 \Phi(\tau)$ measures the capacity required of the channel bridging the two memory levels.

It must be emphasized that the reentry rate functions $\lambda(\tau), \varphi(\tau), \Phi(\tau)$ are estimates. The important point is: starting from the probability density function $f_x(\alpha)$ for the page interreference intervals $x$, it is possible to estimate the page traffic which results from the use of working sets for memory allocation.

P4. *$\tau$-Sensitivity.* It is useful to define a sensitivity function $\sigma(\tau)$ that measures how sensitive is the reentry rate $\lambda(\tau)$ to changes in $\tau$. We define the $\tau$-*sensitivity* of a working set $W(t, \tau)$ to be

$$
\sigma(\tau) = -\frac{d}{d\tau} \lambda(\tau) = \frac{f_x(\tau)}{\bar{x}}.
$$

That is, if $\tau$ is decreased by $d\tau$, $\lambda(\tau)$ increases by $\sigma(\tau)\ d\tau$. It is obvious that $\sigma(\tau) \geq 0$; reducing $\tau$ can never result in a decrease in the reentry rate $\lambda(\tau)$.

Choice of $\tau$. The value ultimately selected for $\tau$ will reflect the working set properties and efficiency requirements and will be influenced by system parameters such as core memory size and memory traverse time. Should $\tau$ be too small, pages may be removed from main memory while still useful, resulting in a high traffic of returning pages. The return traffic functions $\lambda(\tau), \varphi(\tau),$ and $\Phi(\tau)$, and the $\tau$-sensitivity $\sigma(\tau)$, play roles in determining when $\tau$ is "too small." Should $\tau$ be too large, pages may remain in main memory long after they were used, resulting in wasted main memory. The desired number of working sets simultaneously to occupy a core memory of given size plays a role in determining when $\tau$ is "too large." Thus the value selected for $\tau$ will have to represent a compromise between too much page traffic and too much wasted memory space.

The following consideration leads us to recommend for $\tau$ a value comparable to the memory traverse time $T$. Define the residency of a page to be the fraction of time it is potentially available in core memory. Assuming that memory allocation procedures balk at removing from main memory any page in a working set, once a page has entered $W(t, \tau)$ it will remain in main memory for at least $\tau$ seconds. Letting $x$ be the interreference interval to a given page, we have:

(1) If $x \leq \tau$, the page will reside in main memory 100 percent of the time.

(2) If $\tau < x \leq (\tau + T)$, the page will reside in main memory $\tau / (\tau + 2T)$ of the time: it resides in main memory for an interval of $\tau$ seconds, after which it is dispatched to auxiliary memory; while in transit it is rereferenced, so it must begin a return trip as soon as it reaches auxiliary memory, a total of two traverse times for the round trip. Therefore the page reappears in main memory $(\tau + 2T)$ seconds after the previous reference.

(3) If $x > (\tau + T)$, the page will reside in main memory $\tau / (x + T)$ of the time: it resides in main memory for an interval of $\tau$ seconds, after which it is dispatched to auxiliary memory; sometime after having reached auxiliary memory it is rereferenced, requiring $T$ seconds for the return trip. Therefore the page reappears in main memory $(x + T)$ seconds after the previous reference.

Figure.

Fig. 4. Residency {#denning-1968-workingset-fig-4 .figure tag=0604}

Figure 4 shows the residency as a function of $x$. In the interest of efficiency, it is desirable that the drop from 100 percent to $\tau / (\tau + 2T)$ at $x = \tau$ is not too severe; thus, for example, should we wish to limit the drop to 50 percent, we should have to choose $\tau \approx 2T$.

Detecting $W(t, \tau)$. According to our definition, $W(t, \tau)$ is the set of its pages a process has referenced within the last $\tau$ seconds of its execution. This suggests that memory management can be controlled with hardware mechanisms, by associating with each page of main memory a timer. Each time a page is referenced, its timer is set to $\tau$ and begins to run down; if the timer succeeds in running down, a flag is set to mark the page for removal whenever the space is needed. In the Appendix we describe a hardware memory management mechanism that could be housed within the memory boxes. It has two interesting features:

(1) It operates asynchronously and independently of the supervisor, whose only responsibility in memory management is handling page faults. Quite literally, memory manages itself.

(2) Analog devices such as capacitative timers could be used to measure intervals.

Unfortunately it is not practical to add hardware to existing systems. We seek a method of handling memory management within the software. The procedure we propose here samples the page table entries of pages in core memory at process-time intervals of $\sigma$ seconds ($\sigma$ is called the "sampling interval") where $\sigma = \tau / K$, $K$ an integer constant chosen to make the sampling intervals as "fine grain" as desired. On the basis of page references during each of the last $K$ sampling intervals, the working set $W(t, K\sigma)$ can be determined.

As indicated by Figure 5, each page table entry contains an "in-core" bit $M$, where $M = 1$ if and only if the page is present in main memory. It also contains a string of use bits $u_0, u_1, \ldots, u_K$. Each time a page reference occurs $1 \rightarrow u_0$. At the end of each sampling interval $\sigma$, the bit

Figure.

TYPICAL PAGE TABLE ENTRY

Figure.

SHIFT AT END OF SAMPLING INTERVAL pattern contained in $u_0, u_1, \cdots, u_K$ is shifted one position, a 0 enters $u_0$, and $u_K$ is discarded:

Fig. 5. Page table entries for detecting $W(t, K\sigma)$ {#denning-1968-workingset-fig-5 .figure tag=0605}

$$
u_{K-1} \longrightarrow u_K \\
\vdots \\
u_0 \longrightarrow u_1 \\
0 \longrightarrow u_0 .
$$

(15)

Then the logical sum $U$ of the use bits is computed:

$$
U = u_0 + u_1 + \cdots + u_K ,
$$

so that $U = 1$ if and only if the page has been referenced during the last $K$ sampling intervals; of all the pages associated with a process, those with $U = 1$ constitute its working set $W(t, K\sigma)$. If $U = 0$ when $M = 1$, the page is no longer in a working set and may be removed from main memory.

MEMORY ALLOCATION. The basic assumption in memory allocation is that a program will not be run unless there is space in memory for its working set.

In our discussion so far we have seen two alternative quantities of possible use in memory allocation: the working set $W(t, \tau)$ and the working set size $\omega(t, \tau)$. Use of $\omega(t, \tau)$ is sufficient.

Complete knowledge of $W(t, \tau)$, page for page, would be needed if look-ahead were contemplated. We have already discussed why past paging policies have eschewed look-ahead: the strong possibility that preloading could be futile. A program organization likely to be typical of interactive, modular programs, shown in Figure 6, fortifies our previous argument against look-ahead. The user sends requests to the interface procedure $A$; having interpreted the request, $A$ calls on one of the procedures $B_1, \cdots, B_n$ to perform an operation on the data $D$. The called $B$-procedure then returns to $A$ for the next user request. Each time the process of this program blocks, the working set $W(t, \tau)$ is likely to change radically—sometimes only $A$ may be in $W(t, \tau)$, at other times one of the $B$-procedures and $D$ may be in $W(t, \tau)$. The pages of $W(t, \tau)$ are likely to be different. Thus, that a process blocks for an interaction (not page faults) can be a strong indication of an imminent change in $W(t, \tau)$. Therefore the look-ahead, which is most often used just after a process unblocks, would probably load pages not likely to be used.

Knowledge of only $\omega(t, \tau)$ with demand paging suffices to manage memory well. Before running a process we insure that there are enough pages of memory free to contain its working set $W(t, \tau)$, whose pages fill free slots upon demand. By implication, enough free storage has been reserved so that no page of a working set of another program is displaced by a page of $W(t, \tau)$, as can be the case with other page-turning policies. $\omega(t, \tau)$ is a good measure of memory demand.
