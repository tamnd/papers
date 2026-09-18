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
pdf_pages: "4"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 1d077d66391ffcbf27cb15acdc31c785e7a580df3e1aae77f93f9f75f4da755c
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

tends to be small. Therefore some pages of $W(t, \tau)$ will still be in use after time $t$ (i.e. pages in $W(t + \alpha, \alpha)$; since
