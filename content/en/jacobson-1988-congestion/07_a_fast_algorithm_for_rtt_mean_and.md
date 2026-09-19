---
paper: jacobson-1988-congestion
title: Congestion Avoidance and Control
authors:
  - Van Jacobson
year: 1988
venue: SIGCOMM
field: networks
section: A
section_title: A fast algorithm for rtt mean and variation
tag: 06CA
kind: appendix
lang: en
source: https://ee.lbl.gov/papers/congavoid.pdf
pdf_sha256: 9ca88dfa60f98d5cf736c3917df45420eb91861dd1de453a3dedf3d91c1836eb
pdf_pages: 18-19
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 4d4dfbc6e0f13a22700bebb90fbc4fe6658552f07abe676faa29dbdcac221a7f
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

A.1 Theory

The RFC793 algorithm for estimating the mean round trip time is one of the simplest examples of a class of estimators called recursive prediction error or stochastic gradient algorithms. In the past 20 years these algorithms have revolutionized estimation and control theory [20] and it’s probably worth looking at the RFC793 estimator in some detail.

Given a new measurement m of the RTT (round trip time), TCP updates an estimate of the average RTT a by

$$
a \leftarrow (1 - g)a + gm
$$

where g is a ‘gain’ ($0 < g < 1$) that should be related to the signal-to-noise ratio (or, equivalently, variance) of m. This makes a more sense, and computes faster, if we rearrange and collect terms multiplied by g to get

$$
a \leftarrow a + g(m - a)
$$

Think of a as a prediction of the next measurement. $m - a$ is the error in that prediction and the expression above says we make a new prediction based on the old prediction plus some fraction of the prediction error. The prediction error is the sum of two components: (1) error due to ‘noise’ in the measurement (random, unpredictable effects like fluctuations in competing traffic) and (2) error due to a bad choice of a. Calling the random error $E_r$ and the estimation error $E_e$,

$$
a \leftarrow a + gE_r + gE_e
$$

The $gE_e$ term gives a a kick in the right direction while the $gE_r$ term gives it a kick in a random direction. Over a number of samples, the random kicks cancel each other out so this algorithm tends to converge to the correct average. But g represents a compromise: We want a large g to get mileage out of $E_e$ but a small g to minimize the damage from $E_r$. Since the $E_e$ terms move a toward the real average no matter what value we use for g, it’s almost always better to use a gain that’s too small rather than one that’s too large. Typical gain choices are 0.1–0.2 (though it’s a good idea to take long look at your raw data before picking a gain).

It’s probably obvious that a will oscillate randomly around the true average and the standard deviation of a will be g sdev(m). Also that a converges to the true average exponentially with time constant $1/g$. So a smaller g gives a stabler a at the expense of taking a much longer time to get to the true average.

If we want some measure of the variation in m, say to compute a good value for the TCP retransmit timer, there are several alternatives. Variance, $\sigma^2$, is the conventional choice because it has some nice mathematical properties. But computing variance requires squaring $(m - a)$ so an estimator for it will contain a multiply with a danger of integer overflow. Also, most applications will want variation in the same units as a and m, so we’ll be forced to take the square root of the variance to use it (i.e., at least a divide, multiply and two adds).

A variation measure that’s easy to compute is the mean prediction error or mean deviation, the average of $|m - a|$. Also, since

$$
mdev^2 = (\sum |m - a|)^2 \geq \sum |m - a|^2 = \sigma^2
$$

mean deviation is a more conservative (i.e., larger) estimate of variation than standard deviation.$^{16}$

There’s often a simple relation between mdev and sdev. E.g., if the prediction errors are normally distributed, $\mathrm{mdev} = \sqrt{\pi/2} \mathrm{sdev}$. For most common distributions the factor to go from sdev to mdev is near one ($\sqrt{\pi/2} \approx 1.25$). I.e., mdev is a good approximation of sdev and is much easier to compute.

A.2 Practice

Fast estimators for average a and mean deviation v given measurement m follow directly from the above. Both estimators compute means so there are two instances of the RFC793 algorithm:

$$
\begin{align*}
\mathrm{Err} &\equiv m - a \\
a &\leftarrow a + g \mathrm{Err} \\
v &\leftarrow v + g(|\mathrm{Err}| - v)
\end{align*}
$$

To be computed quickly, the above should be done in integer arithmetic. But the expressions contain fractions ($g < 1$) so some scaling is needed to keep everything integer. A reciprocal power of 2 (i.e., $g = 1/2^n$ for some n) is a particularly good choice for g since the scaling can be implemented with shifts. Multiplying through by $1/g$ gives

$$
\begin{align*}
2^n a &\leftarrow 2^n a + \mathrm{Err} \\
2^n v &\leftarrow 2^n v + (|\mathrm{Err}| - v)
\end{align*}
$$

To minimize round-off error, the scaled versions of a and v, sa and sv, should be kept rather than the unscaled versions. Picking $g = .125 = \frac{1}{8}$ (close to the .1 suggested in RFC793) and expressing the above in C:

$$
\begin{align*}
/* \text{update Average estimator} */ \\
m &= (sa >> 3); \\
sa &= m; \\
/* \text{update Deviation estimator} */ \\
if (m < 0) \\
    m &= -m; \\
m &= (sv >> 3); \\
sv &= m;
\end{align*}
$$

It’s not necessary to use the same gain for a and v. To force the timer to go up quickly in response to changes in the RTT, it’s a good idea to give v a larger gain. In particular, because of window–delay mismatch there are often RTT artifacts at integer multiples of the window size.$^{17}$ To filter these, one would like $1/g$ in the a estimator to be at least as large as the window size (in packets) and $1/g$ in the v estimator to be less than the window size.$^{18}$

\footnotetext{
$^{16}$Purists may note that we elided a factor of $1/n$, the number of samples, from the previous inequality. It makes no difference to the result.
$^{17}$E.g., see packets 10–50 of figure 5. Note that these window effects are due to characteristics of the Arpa/Milnet subnet. In general, window effects on the timer are at most a second-order consideration and depend a great deal on the underlying network. E.g., if one were using the Wideband with a 256 packet window, 1/256 would not be a good gain for a (1/16 might be).
$^{18}$Although it may not be obvious, the absolute value in the calculation of v introduces an asymmetry in the timer: Because v has the same sign as an increase and the opposite sign of a decrease, more gain in v makes the
}
