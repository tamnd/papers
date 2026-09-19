---
paper: shannon-1948-communication
title: A Mathematical Theory of Communication
authors:
  - Claude E. Shannon
year: 1948
venue: Bell System Technical Journal
field: theory
section: "22"
section_title: Entropy Loss in Linear Filters
tag: 04EA
kind: appendix
lang: en
source: https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf
pdf_sha256: 6e4e3411984f3edf99dbfe8b941cb5e8a321379ff0cae6ae5c1f592ad8882ca8
pdf_pages: 39-40
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: eab79dcf04b9736a707232f5b1f569fe33e33d0c7381cd784584891533d7f01f
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Theorem 14: *If an ensemble having an entropy $H_1$ per degree of freedom in band W is passed through a filter with characteristic $Y(f)$ the output ensemble has an entropy* {#shannon-1948-communication-thm-14 .statement tag=04EB}

$$
H_2 = H_1 + \frac{1}{W} \int_W \log |Y(f)|^2 \, d f.
$$

The operation of the filter is essentially a linear transformation of coordinates. If we think of the different frequency components as the original coordinate system, the new frequency components are merely the old ones multiplied by factors. The coordinate transformation matrix is thus essentially diagonalized in terms of these coordinates. The Jacobian of the transformation is (for n sine and n cosine components)

$$
J = \prod_{i=1}^n |Y(f_i)|^2
$$

where the $f_i$ are equally spaced through the band W. This becomes in the limit

$$
\exp \frac{1}{W} \int_W \log |Y(f)|^2 \, d f.
$$

Since J is constant its average value is the same quantity and applying the theorem on the change of entropy with a change of coordinates, the result follows. We may also phrase it in terms of the entropy power. Thus if the entropy power of the first ensemble is $N_1$ that of the second is

$$
N_1 \exp \frac{1}{W} \int_W \log |Y(f)|^2 \, d f.
$$

| GAIN | ENTROPY POWER FACTOR | ENTROPY POWER GAIN IN DECIBELS | IMPULSE RESPONSE |
| --- | --- | --- | --- |
| 1 1−ω→ 0 ω 1 | 1/$e^{2}$ | −8.69 | $sin^{2}$(t/2) $t^{2}$/2 |
| 1 1−$\omega^{2}$→ 0 ω 1 | $\left(\frac{2}{e}\right)^4$ | −5.33 | 2$\frac{\sin t}{t^3} - \frac{\cos t}{t^2}$ |
| 1 1−$\omega^{3}$→ 0 ω 1 | 0.411 | −3.87 | 6$\frac{\cos t - 1}{t^4} - \frac{\cos t}{2t^2} + \frac{\sin t}{t^3}$ |
| 1 $\sqrt{1-\omega^2}$→ 0 ω 1 | $\left(\frac{2}{e}\right)^2$ | −2.67 | $\frac{\pi}{2} \frac{J_1(t)}{t}$ |
| 1 → 0 ω 1 | $\frac{1}{e^{2\alpha}}$ | −8.69α | $\frac{1}{\alpha t^2} [\cos(1-\alpha)t - \cos t]$ |

The final entropy power is the initial entropy power multiplied by the geometric mean gain of the filter. If the gain is measured in db, then the output entropy power will be increased by the arithmetic mean db gain over W.

In Table I the entropy power loss has been calculated (and also expressed in db) for a number of ideal gain characteristics. The impulsive responses of these filters are also given for $W = 2\pi$, with phase assumed to be 0.

The entropy loss for many other cases can be obtained from these results. For example the entropy power factor $1/e^2$ for the first case also applies to any gain characteristic obtain from $1-\omega$ by a measure preserving transformation of the $\omega$ axis. In particular a linearly increasing gain $G(\omega) = \omega$, or a "saw tooth" characteristic between 0 and 1 have the same entropy loss. The reciprocal gain has the reciprocal factor. Thus $1/\omega$ has the factor $e^2$. Raising the gain to any power raises the factor to this power.
