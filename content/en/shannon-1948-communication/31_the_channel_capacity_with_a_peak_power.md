---
paper: shannon-1948-communication
title: A Mathematical Theory of Communication
authors:
  - Claude E. Shannon
year: 1948
venue: Bell System Technical Journal
field: theory
section: "26"
section_title: THE CHANNEL CAPACITY WITH A PEAK POWER LIMITATION
tag: 04F4
kind: appendix
lang: en
source: https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf
pdf_sha256: 6e4e3411984f3edf99dbfe8b941cb5e8a321379ff0cae6ae5c1f592ad8882ca8
pdf_pages: 45-47
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: a973bc66dc3eccc0ad0d3cdb308886d3dcba45a9f6f61c946488668a34b8530a
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

In some applications the transmitter is limited not by the average power output but by the peak instantaneous power. The problem of calculating the channel capacity is then that of maximizing (by variation of the ensemble of transmitted symbols)

$$
H(y) - H(n)
$$

subject to the constraint that all the functions $f(t)$ in the ensemble be less than or equal to $\sqrt{S}$, say, for all t. A constraint of this type does not work out as well mathematically as the average power limitation. The most we have obtained for this case is a lower bound valid for all $\frac{S}{N}$, an “asymptotic” upper bound (valid for large $\frac{S}{N}$) and an asymptotic value of C for $\frac{S}{N}$ small.

Theorem 20: *The channel capacity C for a band W perturbed by white thermal noise of power N is bounded by* {#shannon-1948-communication-thm-20 .statement tag=04F5}

$$
C \geq W \log \frac{2}{\pi e^3} \frac{S}{N},
$$

*where S is the peak allowed transmitter power. For sufficiently large* $\frac{S}{N}$

$$
C \leq W \log \frac{\frac{2}{\pi e} S + N}{N} (1 + \epsilon)
$$

*where $\epsilon$ is arbitrarily small. As* $\frac{S}{N} \to 0$ *(and provided the band W starts at 0)*

$$
C / W \log \left( 1 + \frac{S}{N} \right) \to 1.
$$

We wish to maximize the entropy of the received signal. If $\frac{S}{N}$ is large this will occur very nearly when we maximize the entropy of the transmitted ensemble.

The asymptotic upper bound is obtained by relaxing the conditions on the ensemble. Let us suppose that the power is limited to S not at every instant of time, but only at the sample points. The maximum entropy of the transmitted ensemble under these weakened conditions is certainly greater than or equal to that under the original conditions. This altered problem can be solved easily. The maximum entropy occurs if the different samples are independent and have a distribution function which is constant from $-\sqrt{S}$ to $+\sqrt{S}$. The entropy can be calculated as

$$
W \log 4S.
$$

The received signal will then have an entropy less than

$$
W \log (4S + 2 \pi e N)(1 + \epsilon)
$$

with $\epsilon \to 0$ as $\frac{S}{N} \to \infty$ and the channel capacity is obtained by subtracting the entropy of the white noise, $W \log 2 \pi e N$:

$$
W \log (4S + 2 \pi e N)(1 + \epsilon) - W \log (2 \pi e N) = W \log \frac{\frac{2}{\pi e} S + N}{N} (1 + \epsilon).
$$

This is the desired upper bound to the channel capacity.

To obtain a lower bound consider the same ensemble of functions. Let these functions be passed through an ideal filter with a triangular transfer characteristic. The gain is to be unity at frequency 0 and decline linearly down to gain 0 at frequency W. We first show that the output functions of the filter have a peak power limitation S at all times (not just the sample points). First we note that a pulse $\frac{\sin 2 \pi W t}{2 \pi W t}$ going into the filter produces

$$
\frac{1}{2} \frac{\sin^2 \pi W t}{(\pi W t)^2}
$$

in the output. This function is never negative. The input function (in the general case) can be thought of as the sum of a series of shifted functions

$$
a \frac{\sin 2 \pi W t}{2 \pi W t}
$$

where a, the amplitude of the sample, is not greater than $\sqrt{S}$. Hence the output is the sum of shifted functions of the non-negative form above with the same coefficients. These functions being non-negative, the greatest positive value for any t is obtained when all the coefficients a have their maximum positive values, i.e., $\sqrt{S}$. In this case the input function was a constant of amplitude $\sqrt{S}$ and since the filter has unit gain for D.C., the output is the same. Hence the output ensemble has a peak power S.

The entropy of the output ensemble can be calculated from that of the input ensemble by using the theorem dealing with such a situation. The output entropy is equal to the input entropy plus the geometrical mean gain of the filter:

$$
\int_0^W \log G^2 \, df = \int_0^W \log \left( \frac{W - f}{W} \right)^2 \, df = -2W.
$$

Hence the output entropy is

$$
W \log 4S - 2W = W \log \frac{4S}{e^2}
$$

and the channel capacity is greater than

$$
W \log \frac{2}{\pi e^3} \frac{S}{N}.
$$

We now wish to show that, for small $\frac{S}{N}$ (peak signal power over average white noise power), the channel capacity is approximately

$$
C = W \log \left( 1 + \frac{S}{N} \right).
$$

More precisely $C / W \log \left( 1 + \frac{S}{N} \right) \to 1$ as $\frac{S}{N} \to 0$. Since the average signal power P is less than or equal to the peak S, it follows that for all $\frac{S}{N}$

$$
C \leq W \log \left( 1 + \frac{P}{N} \right) \leq W \log \left( 1 + \frac{S}{N} \right).
$$

Therefore, if we can find an ensemble of functions such that they correspond to a rate nearly $W \log \left( 1 + \frac{S}{N} \right)$ and are limited to band W and peak S the result will be proved. Consider the ensemble of functions of the following type. A series of t samples have the same value, either $+\sqrt{S}$ or $-\sqrt{S}$, then the next t samples have the same value, etc. The value for a series is chosen at random, probability $\frac{1}{2}$ for $+\sqrt{S}$ and $\frac{1}{2}$ for $-\sqrt{S}$. If this ensemble be passed through a filter with triangular gain characteristic (unit gain at D.C.), the output is peak limited to $\pm S$. Furthermore the average power is nearly S and can be made to approach this by taking t sufficiently large. The entropy of the sum of this and the thermal noise can be found by applying the theorem on the sum of a noise and a small signal. This theorem will apply if

$$
\sqrt{t} \frac{S}{N}
$$

is sufficiently small. This can be ensured by taking $\frac{S}{N}$ small enough (after t is chosen). The entropy power will be $S + N$ to as close an approximation as desired, and hence the rate of transmission as near as we wish to

$$
W \log \left( \frac{S + N}{N} \right).
$$

PART V: THE RATE FOR A CONTINUOUS SOURCE
