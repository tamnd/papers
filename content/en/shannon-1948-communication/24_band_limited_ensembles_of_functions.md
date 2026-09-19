---
paper: shannon-1948-communication
title: A Mathematical Theory of Communication
authors:
  - Claude E. Shannon
year: 1948
venue: Bell System Technical Journal
field: theory
section: "19"
section_title: Band Limited Ensembles of Functions
tag: "04E6"
kind: appendix
lang: en
source: https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf
pdf_sha256: 6e4e3411984f3edf99dbfe8b941cb5e8a321379ff0cae6ae5c1f592ad8882ca8
pdf_pages: 34-35
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 0ecd39433ce8834e922ac184666fed1d0dcb2dc25f7f654f8c76d3aa3670393c
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

If a function of time $f(t)$ is limited to the band from 0 to W cycles per second it is completely determined by giving its ordinates at a series of discrete points spaced $\frac{1}{2W}$ seconds apart in the manner indicated by the following result.$^5$

Theorem 13: *Let $f(t)$ contain no frequencies over W. Then* {#shannon-1948-communication-thm-13 .statement tag=04E7}

$$
f(t) = \sum_{-\infty}^{\infty} X_n \frac{\sin \pi (2Wt - n)}{\pi (2Wt - n)}
$$

*where*

$$
X_n = f \left( \frac{n}{2W} \right).
$$

$^4$Communication theory is heavily indebted to Wiener for much of its basic philosophy and theory. His classic NDRC report, The Interpolation, Extrapolation and Smoothing of Stationary Time Series (Wiley, 1949), contains the first clear-cut formulation of communication theory as a statistical problem, the study of operations on time series. This work, although chiefly concerned with the linear prediction and filtering problem, is an important collateral reference in connection with the present paper. We may also refer here to Wiener’s Cybernetics (Wiley, 1948), dealing with the general problems of communication and control.

$^5$For a proof of this theorem and further discussion see the author’s paper “Communication in the Presence of Noise” published in the Proceedings of the Institute of Radio Engineers, v. 37, No. 1, Jan., 1949, pp. 10–21.

In this expansion f(t) is represented as a sum of orthogonal functions. The coefficients X_n of the various terms can be considered as coordinates in an infinite dimensional “function space.” In this space each function corresponds to precisely one point and each point to one function.

A function can be considered to be substantially limited to a time T if all the ordinates X_n outside this interval of time are zero. In this case all but 2TW of the coordinates will be zero. Thus functions limited to a band W and duration T correspond to points in a space of 2TW dimensions.

A subset of the functions of band W and duration T corresponds to a region in this space. For example, the functions whose total energy is less than or equal to E correspond to points in a 2TW dimensional sphere with radius r = $\sqrt{2WE}$.

An ensemble of functions of limited duration and band will be represented by a probability distribution p(x_1, ..., x_n) in the corresponding n dimensional space. If the ensemble is not limited in time we can consider the 2TW coordinates in a given interval T to represent substantially the part of the function in the interval T and the probability distribution p(x_1, ..., x_n) to give the statistical structure of the ensemble for intervals of that duration.
