---
paper: cortes-1995-svm
title: Support-Vector Networks
authors:
  - Corinna Cortes
  - Vladimir Vapnik
year: 1995
venue: Machine Learning
field: ai-ml
section: "3"
section_title: The Soft Margin Hyperplane
tag: "0842"
kind: section
lang: en
source: https://doi.org/10.1023/a:1022627411411
pdf_sha256: 561361e49eb22df6f5e14f8c19d681c6b596891f07057fc43703394383233002
pdf_pages: 8-10
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 6293f9451f2fed59dad996cd5c26063d612badbc12784574f75177ab2e1f0da5
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Consider the case where the training data cannot be separated without error. In this case one may want to separate the training set with a minimal number of errors. To express this formally let us introduce some non-negative variables $\xi_i \geq 0,\ i = 1, \ldots, \ell$.

We can now minimize the functional

$$
\Phi(\xi) = \sum_{i=1}^{\ell} \xi_i^{\sigma}
$$

for small $\sigma > 0$, subject to the constraints

$$
y_i (\mathbf{w} \cdot \mathbf{x}_i + b) \geq 1 - \xi_i, \quad i = 1, \ldots, \ell,
$$

$$
\xi_i \geq 0, \quad i = 1, \ldots, \ell.
$$

For sufficiently small $\sigma$ the functional (21) describes the number of the training errors$^5$.
Minimizing (21) one finds some minimal subset of training errors:

$$
(y_{i_1}, \mathbf{x}_{i_1}), \ldots, (y_{i_k}, \mathbf{x}_{i_k}).
$$

If these data are excluded from the training set one can separate the remaining part of the training set without errors. To separate the remaining part of the training data one can construct an optimal separating hyperplane.

This idea can be expressed formally as: minimize the functional

$$
\frac{1}{2} \mathbf{w}^2 + CF \left( \sum_{i=1}^{\ell} \xi_i^{\sigma} \right)
$$

subject to constraints (22) and (23), where $F(u)$ is a monotonic convex function and $C$ is a constant.

For sufficiently large $C$ and sufficiently small $\sigma$, the vector $\mathbf{w}_0$ and constant $b_0$, that minimize the functional (24) under constraints (22) and (23), determine the hyperplane that minimizes the number of errors on the training set and separate the rest of the elements with maximal margin.

Note, however, that the problem of constructing a hyperplane which minimizes the number of errors on the training set is in general NP-complete. To avoid NP-completeness of our problem we will consider the case of $\sigma = 1$ (the smallest value of $\sigma$ for which the optimization problem (15) has a unique solution). In this case the functional (24) describes (for sufficiently large $C$) the problem of constructing a separating hyperplane which minimizes *the sum of deviations*, $\xi$, of training errors and maximizes the margin for the correctly classified vectors. If the training data can be separated without errors the constructed hyperplane coincides with the optimal margin hyperplane.

In contrast to the case with $\sigma < 1$ there exists an efficient method for finding the solution of (24) in the case of $\sigma = 1$. Let us call this solution *the soft margin hyperplane*.

In Appendix A we consider the problem of minimizing the functional

$$
\frac{1}{2} \mathbf{w}^2 + CF \left( \sum_{i=1}^{\ell} \xi_i \right)
$$

subject to the constraints (22) and (23), where $F(u)$ is a monotonic convex function with $F(0) = 0$. To simplify the formulas we only describe the case of $F(u) = u^2$ in this section. For this function the optimization problem remains a quadratic programming problem.

In Appendix A we show that the vector $\mathbf{w}$, as for the optimal hyperplane algorithm, can be written as a linear combination of support vectors $\mathbf{x}_i$:

$$
\mathbf{w}_0 = \sum_{i=1}^{\ell} \alpha_i^0 y_i \mathbf{x}_i.
$$

To find the vector $\Lambda^T = (\alpha_1, \ldots, \alpha_{\ell})$ one has to solve the dual quadratic programming problem of maximizing

$$
W(\Lambda, \delta) = \Lambda^T 1 - \frac{1}{2} \left[ \Lambda^T D \Lambda + \frac{\delta^2}{C} \right]
$$

subject to constraints

$$
\Lambda^T \mathbf{Y} = 0,
$$

$$
\delta \geq 0,
$$

$$
0 \leq \Lambda \leq \delta 1,
$$

where $\mathbf{1}, \Lambda, Y,$ and $D$ are the same elements as used in the optimization problem for constructing an optimal hyperplane, $\delta$ is a scalar, and (29) describes coordinate-wise inequalities.

Note that (29) implies that the smallest admissible value $\delta$ in functional (26) is

$$
\delta = \alpha_{\max} = \max(\alpha_1, \ldots, \alpha_\ell).
$$

Therefore to find a soft margin classifier one has to find a vector $\Lambda$ that maximizes

$$
W(\Lambda) = \Lambda^T \mathbf{1} - \frac{1}{2} \left[ \Lambda^T D \Lambda + \frac{\alpha_{\max}^2}{C} \right]
$$

under the constraints $\Lambda \geq 0$ and (27). This problem differs from the problem of constructing an optimal margin classifier only by the additional term with $\alpha_{\max}$ in the functional (30). Due to this term the solution to the problem of constructing the soft margin classifier is unique and exists for any data set.

The functional (30) is not quadratic because of the term with $\alpha_{\max}$. Maximizing (30) subject to the constraints $\Lambda \geq 0$ and (27) belongs to the group of so-called convex programming problems. Therefore, to construct a soft margin classifier one can either solve the convex programming problem in the $\ell$-dimensional space of the parameters $\Lambda$, or one can solve the quadratic programming problem in the dual $\ell + 1$ space of the parameters $\Lambda$ and $\delta$. In our experiments we construct the soft margin hyperplanes by solving the dual quadratic programming problem.
