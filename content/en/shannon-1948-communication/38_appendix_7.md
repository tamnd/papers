---
paper: shannon-1948-communication
title: A Mathematical Theory of Communication
authors:
  - Claude E. Shannon
year: 1948
venue: Bell System Technical Journal
field: theory
section_title: Appendix 7
kind: appendix
lang: en
source: https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf
pdf_sha256: 6e4e3411984f3edf99dbfe8b941cb5e8a321379ff0cae6ae5c1f592ad8882ca8
pdf_pages: 54-55
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: b8c386a6062bacad73226d2704b8ba6f7fad2d42c0c83da48bbcae0d8486fe35
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The following will indicate a more general and more rigorous approach to the central definitions of communication theory. Consider a probability measure space whose elements are ordered pairs (x, y). The variables x, y are to be identified as the possible transmitted and received signals of some long duration T. Let us call the set of all points whose x belongs to a subset S₁ of x points the strip over S₁, and similarly the set whose y belong to S₂ the strip over S₂. We divide x and y into a collection of non-overlapping measurable subsets Xᵢ and Yᵢ approximate to the rate of transmission R by

$$
R_1 = \frac{1}{T} \sum_i P(X_i, Y_i) \log \frac{P(X_i, Y_i)}{P(X_i)P(Y_i)}
$$

where

$$
\begin{align*}
P(X_i) &\text{ is the probability measure of the strip over } X_i \\
P(Y_i) &\text{ is the probability measure of the strip over } Y_i \\
P(X_i, Y_i) &\text{ is the probability measure of the intersection of the strips.}
\end{align*}
$$

A further subdivision can never decrease R₁. For let X₁ be divided into $X_1 = X_1' + X_1''$ and let

$$
\begin{align*}
P(Y_1) &= a & P(X_1) &= b + c \\
P(X_1') &= b & P(X_1', Y_1) &= d \\
P(X_1'') &= c & P(X_1'', Y_1) &= e \\
P(X_1, Y_1) &= d + e.
\end{align*}
$$

Then in the sum we have replaced (for the X₁, Y₁ intersection)

$$
(d + e) \log \frac{d + e}{a(b + c)} \quad \text{by} \quad d \log \frac{d}{ab} + e \log \frac{e}{ac}.
$$

It is easily shown that with the limitation we have on b, c, d, e,

$$
\left[ \frac{d + e}{b + c} \right]^{d+e} \leq \frac{d^d e^e}{b^d c^e}
$$

and consequently the sum is increased. Thus the various possible subdivisions form a directed set, with R monotonic increasing with refinement of the subdivision. We may define R unambiguously as the least upper bound for R₁ and write it

$$
R = \frac{1}{T} \iint P(x, y) \log \frac{P(x, y)}{P(x)P(y)} \, dx dy.
$$

This integral, understood in the above sense, includes both the continuous and discrete cases and of course many others which cannot be represented in either form. It is trivial in this formulation that if x and u are in one-to-one correspondence, the rate from u to y is equal to that from x to y. If v is any function of y (not necessarily with an inverse) then the rate from x to y is greater than or equal to that from x to v since, in the calculation of the approximations, the subdivisions of y are essentially a finer subdivision of those for v. More generally if y and v are related not functionally but statistically, i.e., we have a probability measure space (y, v), then $R(x, v) \leq R(x, y)$. This means that any operation applied to the received signal, even though it involves statistical elements, does not increase R.

Another notion which should be defined precisely in an abstract formulation of the theory is that of “dimension rate,” that is the average number of dimensions required per second to specify a member of an ensemble. In the band limited case 2W numbers per second are sufficient. A general definition can be framed as follows. Let $f_\alpha(t)$ be an ensemble of functions and let $\rho_T[f_\alpha(t), f_\beta(t)]$ be a metric measuring the “distance” from $f_\alpha$ to $f_\beta$ over the time T (for example the R.M.S. discrepancy over this interval.) Let $N(\epsilon, \delta, T)$ be the least number of elements f which can be chosen such that all elements of the ensemble apart from a set of measure $\delta$ are within the distance $\epsilon$ of at least one of those chosen. Thus we are covering the space to within $\epsilon$ apart from a set of small measure $\delta$. We define the dimension rate $\lambda$ for the ensemble by the triple limit

$$
\lambda = \lim_{\delta \to 0} \lim_{\epsilon \to 0} \lim_{T \to \infty} \frac{\log N(\epsilon, \delta, T)}{T \log \epsilon}.
$$

This is a generalization of the measure type definitions of dimension in topology, and agrees with the intuitive dimension rate for simple ensembles where the desired result is obvious.
