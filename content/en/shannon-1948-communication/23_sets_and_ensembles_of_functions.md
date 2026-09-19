---
paper: shannon-1948-communication
title: A Mathematical Theory of Communication
authors:
  - Claude E. Shannon
year: 1948
venue: Bell System Technical Journal
field: theory
section: "18"
section_title: SETS AND ENSEMBLES OF FUNCTIONS
tag: "04E5"
kind: appendix
lang: en
source: https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf
pdf_sha256: 6e4e3411984f3edf99dbfe8b941cb5e8a321379ff0cae6ae5c1f592ad8882ca8
pdf_pages: 32-34
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: b229838deb78ce843b65fe26dcb6b949093f1d4fc86a8ad19e21f6edcc4def0a
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

We shall have to deal in the continuous case with sets of functions and ensembles of functions. A set of functions, as the name implies, is merely a class or collection of functions, generally of one variable, time. It can be specified by giving an explicit representation of the various functions in the set, or implicitly by giving a property which functions in the set possess and others do not. Some examples are:

1. The set of functions:

$$
f_{\theta}(t) = \sin(t + \theta).
$$

Each particular value of $\theta$ determines a particular function in the set.

2. The set of all functions of time containing no frequencies over W cycles per second.

3. The set of all functions limited in band to W and in amplitude to A.

4. The set of all English speech signals as functions of time.

An ensemble of functions is a set of functions together with a probability measure whereby we may determine the probability of a function in the set having certain properties.$^1$ For example with the set,

$$
f_{\theta}(t) = \sin(t + \theta),
$$

we may give a probability distribution for $\theta$, $P(\theta)$. The set then becomes an ensemble.

Some further examples of ensembles of functions are:

1. A finite set of functions $f_k(t)$ ($k = 1, 2, \ldots, n$) with the probability of $f_k$ being $p_k$.

2. A finite dimensional family of functions

$$
f(\alpha_1, \alpha_2, \ldots, \alpha_n; t)
$$

with a probability distribution on the parameters $\alpha_i$:

$$
p(\alpha_1, \ldots, \alpha_n).
$$

For example we could consider the ensemble defined by

$$
f(a_1, \ldots, a_n, \theta_1, \ldots, \theta_n; t) = \sum_{i=1}^n a_i \sin i(\omega t + \theta_i)
$$

with the amplitudes $a_i$ distributed normally and independently, and the phases $\theta_i$ distributed uniformly (from 0 to $2\pi$) and independently.

$^1$ In mathematical terminology the functions belong to a measure space whose total measure is unity.

3. The ensemble

$$
f(a_i, t) = \sum_{n=-\infty}^{+\infty} a_n \frac{\sin \pi (2Wt - n)}{\pi (2Wt - n)}
$$

with the $a_i$ normal and independent all with the same standard deviation $\sqrt{N}$. This is a representation of “white” noise, band limited to the band from 0 to W cycles per second and with average power N.$^2$

4. Let points be distributed on the t axis according to a Poisson distribution. At each selected point the function $f(t)$ is placed and the different functions added, giving the ensemble

$$
\sum_{k=-\infty}^{\infty} f(t + t_k)
$$

where the $t_k$ are the points of the Poisson distribution. This ensemble can be considered as a type of impulse or shot noise where all the impulses are identical.

5. The set of English speech functions with the probability measure given by the frequency of occurrence in ordinary use.

An ensemble of functions $f_{\alpha}(t)$ is stationary if the same ensemble results when all functions are shifted any fixed amount in time. The ensemble

$$
f_{\theta}(t) = \sin(t + \theta)
$$

is stationary if $\theta$ is distributed uniformly from 0 to $2\pi$. If we shift each function by $t_1$ we obtain

$$
\begin{align*}
f_{\theta}(t + t_1) &= \sin(t + t_1 + \theta) \\
&= \sin(t + \varphi)
\end{align*}
$$

with $\varphi$ distributed uniformly from 0 to $2\pi$. Each function has changed but the ensemble as a whole is invariant under the translation. The other examples given above are also stationary.

An ensemble is ergodic if it is stationary, and there is no subset of the functions in the set with a probability different from 0 and 1 which is stationary. The ensemble

$$
\sin(t + \theta)
$$

is ergodic. No subset of these functions of probability $\neq 0, 1$ is transformed into itself under all time translations. On the other hand the ensemble

$$
a \sin(t + \theta)
$$

with a distributed normally and $\theta$ uniform is stationary but not ergodic. The subset of these functions with a between 0 and 1 for example is stationary.

Of the examples given, 3 and 4 are ergodic, and 5 may perhaps be considered so. If an ensemble is ergodic we may say roughly that each function in the set is typical of the ensemble. More precisely it is known that with an ergodic ensemble an average of any statistic over the ensemble is equal (with probability 1) to an average over the time translations of a particular function of the set.$^3$ Roughly speaking, each function can be expected, as time progresses, to go through, with the proper frequency, all the convolutions of any of the functions in the set.

$2$This representation can be used as a definition of band limited white noise. It has certain advantages in that it involves fewer limiting operations than do definitions that have been used in the past. The name “white noise,” already firmly entrenched in the literature, is perhaps somewhat unfortunate. In optics white light means either any continuous spectrum as contrasted with a point spectrum, or a spectrum which is flat with wavelength (which is not the same as a spectrum flat with frequency).

$3$This is the famous ergodic theorem or rather one aspect of this theorem which was proved in somewhat different formulations by Birkoff, von Neumann, and Koopman, and subsequently generalized by Wiener, Hopf, Hurewicz and others. The literature on ergodic theory is quite extensive and the reader is referred to the papers of these writers for precise and general formulations; e.g., E. Hopf, “Ergodentheorie,” Ergebnisse der Mathematik und ihrer Grenzgebiete, v. 5; “On Causality Statistics and Probability,” Journal of Mathematics and Physics, v. XIII, No. 1, 1934; N. Wiener, “The Ergodic Theorem,” Duke Mathematical Journal, v. 5, 1939.

Just as we may perform various operations on numbers or functions to obtain new numbers or functions, we can perform operations on ensembles to obtain new ensembles. Suppose, for example, we have an ensemble of functions $f_{\alpha}(t)$ and an operator T which gives for each function $f_{\alpha}(t)$ a resulting function $g_{\alpha}(t)$:

$$
g_{\alpha}(t) = T f_{\alpha}(t).
$$

Probability measure is defined for the set $g_{\alpha}(t)$ by means of that for the set $f_{\alpha}(t)$. The probability of a certain subset of the $g_{\alpha}(t)$ functions is equal to that of the subset of the $f_{\alpha}(t)$ functions which produce members of the given subset of g functions under the operation T. Physically this corresponds to passing the ensemble through some device, for example, a filter, a rectifier or a modulator. The output functions of the device form the ensemble $g_{\alpha}(t)$.

A device or operator T will be called invariant if shifting the input merely shifts the output, i.e., if

$$
g_{\alpha}(t) = T f_{\alpha}(t)
$$

implies

$$
g_{\alpha}(t + t_1) = T f_{\alpha}(t + t_1)
$$

for all $f_{\alpha}(t)$ and all $t_1$. It is easily shown (see Appendix 5 that if T is invariant and the input ensemble is stationary then the output ensemble is stationary. Likewise if the input is ergodic the output will also be ergodic.

A filter or a rectifier is invariant under all time translations. The operation of modulation is not since the carrier phase gives a certain time structure. However, modulation is invariant under all translations which are multiples of the period of the carrier.

Wiener has pointed out the intimate relation between the invariance of physical devices under time translations and Fourier theory.$^4$ He has shown, in fact, that if a device is linear as well as invariant Fourier analysis is then the appropriate mathematical tool for dealing with the problem.

An ensemble of functions is the appropriate mathematical representation of the messages produced by a continuous source (for example, speech), of the signals produced by a transmitter, and of the perturbing noise. Communication theory is properly concerned, as has been emphasized by Wiener, not with operations on particular functions, but with operations on ensembles of functions. A communication system is designed not for a particular speech function and still less for a sine wave, but for the ensemble of speech functions.
