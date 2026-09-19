---
paper: cortes-1995-svm
title: Support-Vector Networks
authors:
  - Corinna Cortes
  - Vladimir Vapnik
year: 1995
venue: Machine Learning
field: ai-ml
section: "5"
section_title: General Features of Support-Vector Networks
tag: "0844"
kind: section
lang: en
source: https://doi.org/10.1023/a:1022627411411
pdf_sha256: 561361e49eb22df6f5e14f8c19d681c6b596891f07057fc43703394383233002
pdf_pages: 12-14
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 4e8f7e8056c663e0dcd2861b2d0b76cf3e49012431477b52e63f0140b61174c9
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

### 5.1. Constructing the Decision Rules by Support-Vector Networks is Efficient {#cortes-1995-svm-s5-1 .section tag=0845}

To construct a support-vector network decision rule one has to solve a quadratic optimization problem:

$$
W(\Lambda) = \Lambda^T 1 - \frac{1}{2} \left[ \Lambda^T D \Lambda + \frac{\delta^2}{C} \right],
$$

under the simple constraints:

$$
0 \leq \Lambda \leq \delta 1,
$$

$$
\Lambda^T Y = 0,
$$

where matrix

$$
D_{ij} = y_i y_j K(\mathbf{x}_i, \mathbf{x}_j), \qquad i,\ j = 1, \ldots, l.
$$

is determined by the elements of the training set, and $K(\mathbf{u}, \mathbf{v})$ is the function determining the convolution of the dot-products.

The solution to the optimization problem can be found efficiently by solving intermediate optimization problems determined by the training data, that currently constitute the support vectors. This technique is described in Section 3. The obtained optimal decision function is unique$^6$.

Each optimization problem can be solved using any standard techniques.

### 5.2. The Support-Vector Network is a Universal Machine {#cortes-1995-svm-s5-2 .section tag=0846}

By changing the function $K(\mathbf{u}, \mathbf{v})$ for the convolution of the dot-product one can implement different networks.

In the next section we will consider support-vector network machines that use polynomial decision surfaces. To specify polynomials of different order $d$ one can use the following functions for convolution of the dot-product

$$
K(\mathbf{u}, \mathbf{v}) = (\mathbf{u} \cdot \mathbf{v} + 1)^d.
$$

Radial Basis Function machines with decision functions of the form

$$
f(\mathbf{x}) = \operatorname{sign}\left( \sum_{i=1}^n \alpha_i \exp\left\{ \frac{|\mathbf{x} - \mathbf{x}_i|^2}{\sigma^2} \right\} \right)
$$

can be implemented by using convolutions of the type

$$
K(\mathbf{u}, \mathbf{v}) = \exp\left\{ -\frac{|\mathbf{u} - \mathbf{v}|^2}{\sigma^2} \right\}.
$$

In this case the support-vector network machine will construct both the centers $\mathbf{x}_i$ of the approximating function and the weights $\alpha_i$.

One can also incorporate a priori knowledge of the problem at hand by constructing special convolution functions. Support-vector networks are therefore a rather general class of learning machines which changes its set of decision functions simply by changing the form of the dot-product.

### 5.3. *Support-Vector Networks and Control of Generalization Ability* {#cortes-1995-svm-s5-3 .section tag=0847}

To control the generalization ability of a learning machine one has to control two different factors: the error-rate on the training data and the capacity of the learning machine as measured by its VC-dimension (Vapnik, 1982). There exists a bound for the probability of errors on the test set of the following form: with probability $1 - \eta$ the inequality

$$
\Pr(\text{test error}) \leq \text{Frequency}(training\ error) + \text{Confidence Interval}
$$

is valid. In the bound (38) the confidence interval depends on the VC-dimension of the learning machine, the number of elements in the training set, and the value of $\eta$.

The two factors in (38) form a trade-off: the smaller the VC-dimension of the set of functions of the learning machine, the smaller the confidence interval, but the larger the value of the error frequency.

A general way for resolving this trade-off was proposed as the principle of structural risk minimization: for the given data set one has to find a solution that minimizes their sum. A particular case of structural risk minimization principle is the Occam-Razor principle: keep the first term equal to zero and minimize the second one.

It is known that the VC-dimension of the set of linear indicator functions

$$
I(\mathbf{x}) = \operatorname{sign}(\mathbf{w} \cdot \mathbf{x} + b), \quad |\mathbf{x}| \leq C_x
$$

with fixed threshold $b$ is equal to the dimensionality of the input space. However, the VC-dimension of the subset

$$
I(\mathbf{x}) = \operatorname{sign}(\mathbf{w} \cdot \mathbf{x} + b), \quad |\mathbf{x}| \leq C, \quad |\mathbf{w}| \leq C_w
$$

(the set of functions with bounded norm of the weights) can be less than the dimensionality of the input space and will depend on $C_w$.

From this point of view the optimal margin classifier method executes an Occam-Razor principle. It keeps the first term of (38) equal to zero (by satisfying the inequality (9)) and it minimizes the second term (by minimizing the functional $w \cdot w$). This minimization prevents an over-fitting problem.

However, even in the case where the training data are separable one may obtain better generalization by minimizing the confidence term in (38) even further at the expense of errors on the training set. In the soft margin classifier method this can be done by choosing appropriate values of the parameter $C$. In the support-vector network algorithm one can control the trade-off between complexity of decision rule and frequency of error by changing the parameter $C$, even in the more general case where there exists no solution with zero error on the training set. Therefore the support-vector network can control both factors for generalization ability of the learning machine.
