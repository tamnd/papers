---
paper: shannon-1948-communication
title: A Mathematical Theory of Communication
authors:
  - Claude E. Shannon
year: 1948
venue: Bell System Technical Journal
field: theory
section_title: Appendix 4
kind: appendix
lang: en
source: https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf
pdf_sha256: 6e4e3411984f3edf99dbfe8b941cb5e8a321379ff0cae6ae5c1f592ad8882ca8
pdf_pages: 30-32
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 83076e895c8e99e207d0c4b82830c656a637040767090b782381bc5b279e5264
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

MAXIMIZING THE RATE FOR A SYSTEM OF CONSTRAINTS

Suppose we have a set of constraints on sequences of symbols that is of the finite state type and can be represented therefore by a linear graph. Let $\ell_{ij}^{(s)}$ be the lengths of the various symbols that can occur in passing from state i to state j. What distribution of probabilities $P_i$ for the different states and $p_{ij}^{(s)}$ for choosing symbol s in state i and going to state j maximizes the rate of generating information under these constraints? The constraints define a discrete channel and the maximum rate must be less than or equal to the capacity C of this channel, since if all blocks of large length were equally likely, this rate would result, and if possible this would be best. We will show that this rate can be achieved by proper choice of the $P_i$ and $p_{ij}^{(s)}$.

The rate in question is

$$
\frac{-\sum P_i p_{ij}^{(s)} \log p_{ij}^{(s)}}{\sum P_i p_{ij}^{(s)} \ell_{ij}^{(s)}} = \frac{N}{M}.
$$

Let $\ell_{ij} = \sum_s \ell_{ij}^{(s)}$. Evidently for a maximum $p_{ij}^{(s)} = k \exp \ell_{ij}^{(s)}$. The constraints on maximization are $\sum P_i = 1, \sum_j p_{ij} = 1, \sum P_i (p_{ij} - \delta_{ij}) = 0$. Hence we maximize

$$
U = \frac{-\sum P_i p_{ij} \log p_{ij}}{\sum P_i p_{ij} \ell_{ij}} + \lambda \sum_i P_i + \sum \mu_i p_{ij} + \sum \eta_j P_i (p_{ij} - \delta_{ij})
$$

$$
\frac{\partial U}{\partial p_{ij}} = -\frac{M P_i (1 + \log p_{ij}) + N P_i \ell_{ij}}{M^2} + \lambda + \mu_i + \eta_i P_i = 0.
$$

Solving for $p_{ij}$

$$
p_{ij} = A_i B_j D^{-\ell_{ij}}.
$$

Since

$$
\sum_j p_{ij} = 1, \quad A_i^{-1} = \sum_j B_j D^{-\ell_{ij}}
$$

$$
p_{ij} = \frac{B_j D^{-\ell_{ij}}}{\sum_s B_s D^{-\ell_{is}}}.
$$

The correct value of D is the capacity C and the $B_j$ are solutions of

$$
B_i = \sum B_j C^{-\ell_{ij}}
$$

for then

$$
p_{ij} = \frac{B_j}{B_i} C^{-\ell_{ij}}
$$

$$
\sum P_i \frac{B_j}{B_i} C^{-\ell_{ij}} = P_j
$$

or

$$
\sum \frac{P_i}{B_i} C^{-\ell_{ij}} = \frac{P_j}{B_j}.
$$

So that if $\lambda_i$ satisfy

$$
\sum \gamma_i C^{-\ell_{ij}} = \gamma_j \\
P_i = B_i \gamma_i.
$$

Both the sets of equations for $B_i$ and $\gamma_i$ can be satisfied since C is such that

$$
|C^{-\ell_{ij}} - \delta_{ij}| = 0.
$$

In this case the rate is

$$
-\frac{\sum P_i p_{ij} \log \frac{B_j}{B_i} C^{-\ell_{ij}}}{\sum P_i p_{ij} \ell_{ij}} = C - \frac{\sum P_i p_{ij} \log \frac{B_j}{B_i}}{\sum P_i p_{ij} \ell_{ij}}
$$

but

$$
\sum P_i p_{ij} (\log B_j - \log B_i) = \sum_j P_j \log B_j - \sum P_i \log B_i = 0
$$

Hence the rate is C and as this could never be exceeded this is the maximum, justifying the assumed solution.

PART III: MATHEMATICAL PRELIMINARIES

In this final installment of the paper we consider the case where the signals or the messages or both are continuously variable, in contrast with the discrete nature assumed heretofore. To a considerable extent the continuous case can be obtained through a limiting process from the discrete case by dividing the continuum of messages and signals into a large but finite number of small regions and calculating the various parameters involved on a discrete basis. As the size of the regions is decreased these parameters in general approach as limits the proper values for the continuous case. There are, however, a few new effects that appear and also a general change of emphasis in the direction of specialization of the general results to particular cases.

We will not attempt, in the continuous case, to obtain our results with the greatest generality, or with the extreme rigor of pure mathematics, since this would involve a great deal of abstract measure theory and would obscure the main thread of the analysis. A preliminary study, however, indicates that the theory can be formulated in a completely axiomatic and rigorous manner which includes both the continuous and discrete cases and many others. The occasional liberties taken with limiting processes in the present analysis can be justified in all cases of practical interest.
