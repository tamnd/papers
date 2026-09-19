---
paper: shannon-1948-communication
title: A Mathematical Theory of Communication
authors:
  - Claude E. Shannon
year: 1948
venue: Bell System Technical Journal
field: theory
section: "25"
section_title: Channel Capacity with an Average Power Limitation
tag: 04F0
kind: appendix
lang: en
source: https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf
pdf_sha256: 6e4e3411984f3edf99dbfe8b941cb5e8a321379ff0cae6ae5c1f592ad8882ca8
pdf_pages: 43-45
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 734917bae8bf151e5999175194e50b265b244b8192fea50ff3d94a2b7a059524
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

A simple application of Theorem 16 is the case when the noise is a white thermal noise and the transmitted signals are limited to a certain average power P. Then the received signals have an average power P + N where N is the average noise power. The maximum entropy for the received signals occurs when they also form a white noise ensemble since this is the greatest possible entropy for a power P + N and can be obtained by a suitable choice of transmitted signals, namely if they form a white noise ensemble of power P. The entropy (per second) of the received ensemble is then

$$
H(y) = W \log 2 \pi e (P + N),
$$

and the noise entropy is

$$
H(n) = W \log 2 \pi e N.
$$

The channel capacity is

$$
C = H(y) - H(n) = W \log \frac{P + N}{N}.
$$

Summarizing we have the following:
Theorem 17: *The capacity of a channel of band W perturbed by white thermal noise power N when the average transmitter power is limited to P is given by* {#shannon-1948-communication-thm-17 .statement tag=04F1}

$$
C = W \log \frac{P + N}{N}.
$$

This means that by sufficiently involved encoding systems we can transmit binary digits at the rate W log$_2$ $\frac{P + N}{N}$ bits per second, with arbitrarily small frequency of errors. It is not possible to transmit at a higher rate by any encoding system without a definite positive frequency of errors.
To approximate this limiting rate of transmission the transmitted signals must approximate, in statistical properties, a white noise.$^6$ A system which approaches the ideal rate may be described as follows: Let

$^6$This and other properties of the white noise case are discussed from the geometrical point of view in “Communication in the Presence of Noise,” loc. cit.

M = 2^s samples of white noise be constructed each of duration T. These are assigned binary numbers from 0 to M − 1. At the transmitter the message sequences are broken up into groups of s and for each group the corresponding noise sample is transmitted as the signal. At the receiver the M samples are known and the actual received signal (perturbed by noise) is compared with each of them. The sample which has the least R.M.S. discrepancy from the received signal is chosen as the transmitted signal and the corresponding binary number reconstructed. This process amounts to choosing the most probable (a posteriori) signal. The number M of noise samples used will depend on the tolerable frequency $\epsilon$ of errors, but for almost all selections of samples we have

$$
\lim_{\epsilon \to 0} \lim_{T \to \infty} \frac{\log M(\epsilon, T)}{T} = W \log \frac{P + N}{N},
$$

so that no matter how small $\epsilon$ is chosen, we can, by taking T sufficiently large, transmit as near as we wish to TW log $\frac{P + N}{N}$ binary digits in the time T.

Formulas similar to $C = W \log \frac{P + N}{N}$ for the white noise case have been developed independently by several other writers, although with somewhat different interpretations. We may mention the work of N. Wiener,$^7$ W. G. Tuller,$^8$ and H. Sullivan in this connection.

In the case of an arbitrary perturbing noise (not necessarily white thermal noise) it does not appear that the maximizing problem involved in determining the channel capacity C can be solved explicitly. However, upper and lower bounds can be set for C in terms of the average noise power N the noise entropy power $N_1$. These bounds are sufficiently close together in most practical cases to furnish a satisfactory solution to the problem.

Theorem 18: *The capacity of a channel of band W perturbed by an arbitrary noise is bounded by the inequalities* {#shannon-1948-communication-thm-18 .statement tag=04F2}

$$
W \log \frac{P + N_1}{N_1} \leq C \leq W \log \frac{P + N}{N_1}
$$

*where*

$$
P = \text{average transmitter power}
$$

$$
N = \text{average noise power}
$$

$$
N_1 = \text{entropy power of the noise}.
$$

Here again the average power of the perturbed signals will be P + N. The maximum entropy for this power would occur if the received signal were white noise and would be W log $2 \pi e (P + N)$. It may not be possible to achieve this; i.e., there may not be any ensemble of transmitted signals which, added to the perturbing noise, produce a white thermal noise at the receiver, but at least this sets an upper bound to H(y). We have, therefore

$$
C = \operatorname{Max} H(y) - H(n)
$$

$$
\leq W \log 2 \pi e (P + N) - W \log 2 \pi e N_1.
$$

This is the upper limit given in the theorem. The lower limit can be obtained by considering the rate if we make the transmitted signal a white noise, of power P. In this case the entropy power of the received signal must be at least as great as that of a white noise of power $P + N_1$ since we have shown in in a previous theorem that the entropy power of the sum of two ensembles is greater than or equal to the sum of the individual entropy powers. Hence

$$
\operatorname{Max} H(y) \geq W \log 2 \pi e (P + N_1)
$$

$^7$ Cybernetics, loc. cit.
$^8$ "Theoretical Limitations on the Rate of Transmission of Information," Proceedings of the Institute of Radio Engineers, v. 37, No. 5, May, 1949, pp. 468–78.

and

$$
C \geq W \log 2 \pi e (P + N_1) - W \log 2 \pi e N_1 \\
= W \log \frac{P + N_1}{N_1}.
$$

As P increases, the upper and lower bounds approach each other, so we have as an asymptotic rate

$$
W \log \frac{P + N}{N_1}.
$$

If the noise is itself white, $N = N_1$ and the result reduces to the formula proved previously:

$$
C = W \log \left( 1 + \frac{P}{N} \right).
$$

If the noise is Gaussian but with a spectrum which is not necessarily flat, $N_1$ is the geometric mean of the noise power over the various frequencies in the band W. Thus

$$
N_1 = \exp \frac{1}{W} \int_W \log N(f) \, df
$$

where $N(f)$ is the noise power at frequency f.

Theorem 19: *If we set the capacity for a given transmitter power P equal to* {#shannon-1948-communication-thm-19 .statement tag=04F3}

$$
C = W \log \frac{P + N - \eta}{N_1}
$$

*then $\eta$ is monotonic decreasing as P increases and approaches 0 as a limit.*

Suppose that for a given power $P_1$ the channel capacity is

$$
W \log \frac{P_1 + N - \eta_1}{N_1}.
$$

This means that the best signal distribution, say $p(x)$, when added to the noise distribution $q(x)$, gives a received distribution $r(y)$ whose entropy power is $(P_1 + N - \eta_1)$. Let us increase the power to $P_1 + \Delta P$ by adding a white noise of power $\Delta P$ to the signal. The entropy of the received signal is now at least

$$
H(y) = W \log 2 \pi e (P_1 + N - \eta_1 + \Delta P)
$$

by application of the theorem on the minimum entropy power of a sum. Hence, since we can attain the H indicated, the entropy of the maximizing distribution must be at least as great and $\eta$ must be monotonic decreasing. To show that $\eta \to 0$ as $P \to \infty$ consider a signal which is white noise with a large P. Whatever the perturbing noise, the received signal will be approximately a white noise, if P is sufficiently large, in the sense of having an entropy power approaching $P + N$.
