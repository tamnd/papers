---
paper: cortes-1995-svm
title: Support-Vector Networks
authors:
  - Corinna Cortes
  - Vladimir Vapnik
year: 1995
venue: Machine Learning
field: ai-ml
section: "7"
section_title: Conclusion
tag: "0853"
kind: section
lang: en
source: https://doi.org/10.1023/a:1022627411411
pdf_sha256: 561361e49eb22df6f5e14f8c19d681c6b596891f07057fc43703394383233002
pdf_pages: 18-24
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 1eb9d54f33600bdd95e263ace72cda5cd4c351266c2d30963d6e85392e4df1ff
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

This paper introduces the support-vector network as a new learning machine for two-group classification problems.

The support-vector network combines 3 ideas: the solution technique from optimal hyperplanes (that allows for an expansion of the solution vector on support vectors), the idea of convolution of the dot-product (that extends the solution surfaces from linear to non-linear), and the notion of soft margins (to allow for errors on the training set).

The algorithm has been tested and compared to the performance of other classical algorithms. Despite the simplicity of the design in its decision surface the new algorithm exhibits a very fine performance in the comparison study.

Other characteristics like capacity control and ease of changing the implemented decision surface render the support-vector network an extremely powerful and universal learning machine.

A. Constructing Separating Hyperplanes

In this appendix we derive both the method for constructing optimal hyperplanes and soft margin hyperplanes.

A.1. Optimal Hyperplane Algorithm

It was shown in Section 2, that to construct the optimal hyperplane

$$
w_0 \cdot x + b_0 = 0,
$$

which separates a set of training data

$$
(y_1, x_1), \ldots, (y_\ell, x_\ell),
$$

one has to minimize a functional

$$
\Phi = w \cdot w,
$$

subject to the constraints

$$
y_i(x_i \cdot w + b) \geq 1, \quad i = 1, \ldots, \ell.
$$

To do this we use a standard optimization technique. We construct a Lagrangian

$$
L(w, b, \Lambda) = \frac{1}{2} w \cdot w - \sum_{i=1}^\ell \alpha_i [y_i(x_i \cdot w + b) - 1],
$$

where $\Lambda^T = (\alpha_1, \ldots, \alpha_\ell)$ is the vector of non-negative Lagrange multipliers corresponding to the constraints (41).

It is known that the solution to the optimization problem is determined by the saddle point of this Lagrangian in the $2\ell + 1$-dimensional space of $w, \Lambda,$ and $b$, where the minimum should be taken with respect to the parameters $w$ and $b$, and the maximum should be taken with respect to the Lagrange multipliers $\Lambda$.

At the point of the minimum (with respect to $w$ and $b$) one obtains:

$$
\left. \frac{\partial L(w, b, \Lambda)}{\partial w} \right|_{w=w_0} = \left( w_0 - \sum_{i=1}^\ell \alpha_i y_i x_i \right) = 0,
$$

$$
\left. \frac{\partial L(w, b, \Lambda)}{\partial b} \right|_{b=b_0} = \sum_{\alpha_i} y_i \alpha_i = 0.
$$

From equality (43) we derive

$$
w_0 = \sum_{i=1}^{\ell} \alpha_i y_i x_i,
$$

which expresses, that the optimal hyperplane solution can be written as a linear combination of training vectors. Note, that only training vectors $x_i$ with $\alpha_i > 0$ have an effective contribution to the sum (45).

Substituting (45) and (44) into (42) we obtain

$$
W(\Lambda) = \sum_{i=1}^{\ell} \alpha_i - \frac{1}{2} w_0 \cdot w_0
$$

$$
= \sum_{i=1}^{\ell} \alpha_i - \frac{1}{2} \sum_{i=1}^{\ell} \sum_{j=1}^{\ell} \alpha_i \alpha_j y_i y_j x_i \cdot x_j.
$$

In vector notation this can be rewritten as

$$
W(\Lambda) = \Lambda^T 1 - \frac{1}{2} \Lambda^T D \Lambda,
$$

where $1$ is an $l$-dimensional unit vector, and $D$ is a symmetric $\ell \times \ell$-matrix with elements

$$
D_{ij} = y_i y_j x_i \cdot x_j.
$$

To find the desired saddle point it remains to locate the maximum of (48) under the constraints (43)

$$
\Lambda^T Y = 0,
$$

where $Y^T = (y_1, \ldots, y_\ell)$, and

$$
\Lambda \geq 0.
$$

The Kuhn-Tucker theorem plays an important part in the theory of optimization. According to this theorem, at our saddle point in $w_0, b_0, \Lambda_0$, any Lagrange multiplier $\alpha_i^0$ and its corresponding constraint are connected by an equality

$$
\alpha_i [y_i (x_i \cdot w_0 + b_0) - 1] = 0, \quad i = 1, \ldots, \ell.
$$

From this equality comes that non-zero values $\alpha_i$ are only achieved in the cases where

$$
y_i (x_i \cdot w_0 + b_0) - 1 = 0.
$$

In other words: $\alpha_i \neq 0$ only for cases were the inequality is met as an equality. We call vectors $x_i$ for which

$$
y_i (x_i \cdot w_0 + b_0) = 1
$$

for support-vectors. Note, that in this terminology the Eq. (45) states that the solution vector $w_0$ can be expanded on support vectors.

Another observation, based on the Kuhn-Tucker Eqs. (44) and (45) for the optimal solution, is the relationship between the maximal value $W(\Lambda_0)$ and the separation distance $\rho_0$:

$$
\mathbf{w}_0 \cdot \mathbf{w}_0 = \sum_{i=1}^{\ell} \alpha_i^0 y_i \mathbf{x}_i \cdot \mathbf{w}_0 = \sum_{i=1}^{\ell} \alpha_i^0 (1 - y_i b_0) = \sum_{i=1}^{\ell} \alpha_i^0.
$$

Substituting this equality into the expression (46) for $W(\Lambda_0)$ we obtain

$$
W(\Lambda_0) = \sum_{i=1}^{\ell} \alpha_i^0 - \frac{1}{2} \mathbf{w}_0 \cdot \mathbf{w}_0 = \frac{\mathbf{w}_0 \cdot \mathbf{w}_0}{2}.
$$

Taking into account the expression (13) from Section 2 we obtain

$$
W(\Lambda_0) = \frac{2}{\rho_0^2},
$$

where $\rho_0$ is the margin for the optimal hyperplane.

A.2. *Soft Margin Hyperplane Algorithm*

Below we first consider the case of $F(u) = u^k$. Then we describe the general result for a monotonic convex function $F(u)$.

To construct a soft margin separating hyperplane we maximize the functional

$$
\Phi = \frac{1}{2} \mathbf{w} \cdot \mathbf{w} + C \left( \sum_{i=1}^{\ell} \xi_i \right)^k, \quad k > 1,
$$

under the constraints

$$
y_i (\mathbf{x}_i \cdot \mathbf{w} + b) \geq 1 - \xi_i, \qquad i = 1, \ldots, \ell, \tag{49}
$$
{#cortes-1995-svm-eq-49 .equation tag=0854}

$$
\xi_i \geq 0, \qquad i = 1, \ldots, \ell. \tag{50}
$$
{#cortes-1995-svm-eq-50 .equation tag=0855}

The Lagrange functional for this problem is

$$
L(\mathbf{w}, \xi, b, \Lambda, \mathbf{R})
$$

$$
= \frac{1}{2} \mathbf{w} \cdot \mathbf{w} + C \left( \sum_{i=1}^{\ell} \xi_i \right)^k - \sum_{i=1}^{\ell} \alpha_i [y_i (\mathbf{x}_i \cdot \mathbf{w} + b) - 1 + \xi_i] - \sum_{i=1}^{\ell} r_i \xi_i, \tag{51}
$$
{#cortes-1995-svm-eq-51 .equation tag=0856}

where the non-negative multipliers $\Lambda^T = (\alpha_1, \alpha_2, \ldots, \alpha_l)$ arise from the constraint (49), and the multipliers $\mathbf{R}^T = (r_1, r_2, \ldots, r_l)$ enforce the constraint (50).

We have to find the saddle point of this functional (the minimum with respect to the variables $\mathbf{w}_i, b,$ and $\xi_i$, and the maximum with respect to the variables $\alpha_i$ and $r_i$).

Let us use the conditions for the minimum of this functional at the extremum point:

$$
\left. \frac{\partial L}{\partial \mathbf{w}} \right|_{\mathbf{w} = \mathbf{w}_0} = \mathbf{w}_0 - \sum_{i=1}^{\ell} \alpha_i y_i \mathbf{x}_i = 0, \tag{52}
$$
{#cortes-1995-svm-eq-52 .equation tag=0857}

$$
\left. \frac{\partial L}{\partial b} \right|_{b=b_0} = \sum_{i=1}^{\ell} \alpha_i y_i = 0,
$$

(53)

$$
\left. \frac{\partial L}{\partial \xi_i} \right|_{\xi_i=\xi_i^0} = kC \left( \sum_{i=1}^{\ell} \xi_i^0 \right)^{k-1} - \alpha_i - r_i.
$$

(54)

If we denote

$$
\sum_{i=1}^{\ell} \xi_i^0 = \left( \frac{\delta}{Ck} \right)^{\frac{1}{k-1}},
$$

(55) we can rewrite Eq. (54) as

$$
\delta - \alpha_i - r_i = 0.
$$

(56)

From the equalities (52)-(55) we find

$$
w_0 = \sum_{i=1}^{\ell} \alpha_i y_i x_i,
$$

$$
\sum_{i=1}^{\ell} \alpha_i y_i = 0,
$$

(57)

$$
\delta = \alpha_i + r_i.
$$

(58)

Substituting the expressions for $w_0, b_0,$ and $\delta$ into the Lagrange functional (51) we obtain

$$
W(\Lambda, \delta) = \sum_{i=1}^{\ell} \alpha_i - \frac{1}{2} \sum_{i=1}^{\ell} \sum_{j=1}^{\ell} \alpha_i \alpha_j y_i y_j x_i \cdot x_j - \frac{\delta^{k/k-1}}{(kC)^{1/k-1}} \left( 1 - \frac{1}{k} \right).
$$

(59)

To find the soft margin hyperplane solution one has to maximize the form functional (59) under the constraints (57)-(58) with respect to the non-negative variables $\alpha_i, r_i$ with $i = 1, \ldots, l$. In vector notation (59) can be rewritten as

$$
W(\Lambda, \delta) = \Lambda^T 1 - \left[ \frac{1}{2} \Lambda^T D \Lambda + \frac{\delta^{k/k-1}}{(kC)^{1/k-1}} \left( 1 - \frac{1}{k} \right) \right],
$$

(60) where $\Lambda$ and $D$ are as defined above. To find the desired saddle point one therefore has to find the maximum of (60) under the constraints

$$
\Lambda^T Y = 0,
$$

(61)

$$
\Lambda + R = \delta 1,
$$

(62)

$$
\Lambda \geq 0,
$$

(63) and

$$
R \geq 0.
$$

(64)

From (62) and (64) one obtains that the vector $\Lambda$ should satisfy the conditions

$$
0 \leq \Lambda \leq \delta 1.
$$

(65)

From conditions (62) and (64) one can also conclude that to maximize (60)

$$
\delta = \alpha_{\max} = \max(\alpha_1, \ldots, \alpha_\ell).
$$

Substituting this value of $\delta$ into (60) we obtain

$$
W(\Lambda) = \Lambda^T 1 - \left[ \frac{1}{2} \Lambda^T D \Lambda + \frac{\alpha_{\max}^{k/k-1}}{(kC)^{1/k-1}} \left( 1 - \frac{1}{k} \right) \right].
$$

To find the soft margin hyperplane one can therefore either find the maximum of the quadratic form (51) under the constraints (61) and (65), or one has to find the maximum of the convex function (60) under the constraints (61) and (56). For the experiments reported in this paper we used $k = 2$ and solved the quadratic programming problem (51).

For the case of $F(u) = u$ the same technique brings us to the problem of solving the following quadratic optimization problem: minimize the functional

$$
W(\Lambda) = \Lambda^T 1 - \frac{1}{2} \Lambda^T D \Lambda,
$$

under the constraints

$$
0 \leq \Lambda \leq C 1,
$$

and

$$
\Lambda^T Y = 0.
$$

The general solution for the case of a monotone convex function $F(u)$ can also be obtained from this technique. The soft margin hyperplane has a form

$$
w = \sum_{i=1}^\ell \alpha_i y_i x_i,
$$

where $\Lambda_0^T = (\alpha_0^0, \ldots, \alpha_\ell^0)$ is the solution of the following dual convex programming problem: maximize the functional

$$
W(\Lambda) = \Lambda^T 1 - \left[ \frac{1}{2} \Lambda^T D \Lambda + \left( \alpha_{\max} f^{-1} \left( \frac{\alpha_{\max}}{C} \right) \right) - CF \left( f^{-1} \left( \frac{\alpha_{\max}}{C} \right) \right) \right],
$$

under the constraints

$$
\Lambda^T Y = 0,
$$

$$
\Lambda \geq 0,
$$

where we denote

$$
f(u) = F'(u).
$$

For convex monotone functions $F(u)$ with $F(0) = 0$ the following inequality is valid:

$$
u F'(u) > F(u).
$$

Therefore the second term in square brackets is positive and goes to infinity when $\alpha_{\max}$ goes to infinity.

Finally, we can consider the hyperplane that minimizes the form

$$
\frac{1}{2} \left( \mathbf{w} \cdot \mathbf{w} + \sum_{i=1}^{\ell} \xi_i^2 \right)
$$

subject to the constraints (49)-(50), where the second term minimizes the least square value for the errors. This lead to the following quadratic programming problem: maximize the functional

$$
W(\Lambda) = \Lambda^T \mathbf{1} - \frac{1}{2} \left[ \Lambda^T D \Lambda + \frac{1}{C} \Lambda^T \Lambda \right]
$$

in the non-negative quadrant $\Lambda \geq 0$ subject to the constraint $\Lambda^T Y = 0$.
