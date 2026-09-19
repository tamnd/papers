---
paper: cortes-1995-svm
title: Support-Vector Networks
authors:
  - Corinna Cortes
  - Vladimir Vapnik
year: 1995
venue: Machine Learning
field: ai-ml
section: "2"
section_title: Optimal Hyperplanes
tag: 083F
kind: section
lang: en
source: https://doi.org/10.1023/a:1022627411411
pdf_sha256: 561361e49eb22df6f5e14f8c19d681c6b596891f07057fc43703394383233002
pdf_pages: 5-8
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 80e19c748e80db276b8230a55c7d004eccb7b6f591a9266f7778a77dce90d12f
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

In this section we review the method of optimal hyperplanes (Vapnik, 1982) for separation of training data without errors. In the next section we introduce a notion of soft margins, that will allow for an analytic treatment of learning with errors on the training set.

### 2.1. The Optimal Hyperplane Algorithm {#cortes-1995-svm-s2-1 .section tag=0840}

The set of labeled training patterns

$$
(y_1, \mathbf{x}_1), \ldots, (y_\ell, \mathbf{x}_\ell), \quad y_i \in \{-1, 1\}
$$

is said to be linearly separable if there exists a vector $\mathbf{w}$ and a scalar $b$ such that the inequalities

$$
\begin{align*}
\mathbf{w} \cdot \mathbf{x}_i + b &\geq 1 \quad \text{if } y_i = 1, \\
\mathbf{w} \cdot \mathbf{x}_i + b &\leq -1 \quad \text{if } y_i = -1,
\end{align*}
$$

Figure 4. Classification of an unknown pattern by a support-vector network. The pattern is in input space compared to support vectors. The resulting values are non-linearly transformed. A linear function of these transformed values determine the output of the classifier. {#cortes-1995-svm-fig-4 .figure tag=0841}

are valid for all elements of the training set (8). Below we write the inequalities (9) in the form⁴:

$$
y_i (\mathbf{w} \cdot \mathbf{x}_i + b) \geq 1, \quad i = 1, \ldots, \ell.
$$

The optimal hyperplane

$$
\mathbf{w}_0 \cdot \mathbf{x} + b_0 = 0
$$

is the unique one which separates the training data with a maximal margin: it determines the direction $\mathbf{w}/|\mathbf{w}|$ where the distance between the projections of the training vectors of two different classes is maximal, recall Fig. 2. This distance $\rho(\mathbf{w}, b)$ is given by

$$
\rho(\mathbf{w}, b) = \min_{\{\mathbf{x}: y=1\}} \frac{\mathbf{x} \cdot \mathbf{w}}{|\mathbf{w}|} - \max_{\{\mathbf{x}: y=-1\}} \frac{\mathbf{x} \cdot \mathbf{w}}{|\mathbf{w}|}.
$$

The optimal hyperplane $(\mathbf{w}_0, b_0)$ is the arguments that maximize the distance (12). It follows from (12) and (10) that

$$
\rho(\mathbf{w}_0, b_0) = \frac{2}{|\mathbf{w}_0|} = \frac{2}{\sqrt{\mathbf{w}_0 \cdot \mathbf{w}_0}}.
$$

This means that the optimal hyperplane is the unique one that minimizes $\mathbf{w} \cdot \mathbf{w}$ under the constraints (10). Constructing an optimal hyperplane is therefore a quadratic programming problem.

Vectors $\mathbf{x}_i$ for which $y_i (\mathbf{w} \cdot \mathbf{x}_i + b) = 1$ will be termed *support vectors*. In Appendix A.1 we show that the vector $\mathbf{w}_0$ that determines the optimal hyperplane can be written as a linear combination of training vectors:

$$
\mathbf{w}_0 = \sum_{i=1}^{\ell} y_i \alpha_i^0 \mathbf{x}_i,
$$

where $\alpha_i^0 \geq 0$. Since $\alpha > 0$ only for support vectors (see Appendix), the expression (14) represents a compact form of writing $\mathbf{w}_0$. We also show that to find the vector of parameters $\alpha_i$:

$$
\Lambda_0^T = (\alpha_1^0, \ldots, \alpha_\ell^0),
$$

one has to solve the following quadratic programming problem:

$$
W(\Lambda) = \Lambda^T \mathbf{1} - \frac{1}{2} \Lambda^T D \Lambda
$$

with respect to $\Lambda^T = (\alpha_1, \ldots, \alpha_\ell)$, subject to the constraints:

$$
\begin{align*}
\Lambda &\geq 0, \\
\Lambda^T Y &= 0,
\end{align*}
$$

where $\mathbf{1}^T = (1, \ldots, 1)$ is an $\ell$-dimensional unit vector, $Y^T = (y_1, \ldots, y_\ell)$ is the $\ell$-dimensional vector of labels, and $D$ is a symmetric $\ell \times \ell$-matrix with elements

$$
D_{ij} = y_i y_j \mathbf{x}_i \cdot \mathbf{x}_j, \quad i, j = 1, \ldots, \ell.
$$

The inequality (16) describes the nonnegative quadrant. We therefore have to maximize the quadratic form (15) in the nonnegative quadrant, subject to the constraints (17).

When the training data (8) can be separated without errors we also show in Appendix A the following relationship between the maximum of the functional (15), the pair $(\Lambda_0, b_0)$, and the maximal margin $\rho_0$ from (13):

$$
W(\Lambda_0) = \frac{2}{\rho_0^2}.
$$

If for some $\Lambda_*$ and large constant $W_0$ the inequality

$$
W(\Lambda_*) > W_0
$$

is valid, one can accordingly assert that all hyperplanes that separate the training data (8) have a margin

$$
\rho < \sqrt{\frac{2}{W_0}}.
$$

If the training set (8) cannot be separated by a hyperplane, the margin between patterns of the two classes becomes arbitrary small, resulting in the value of the functional $W(\Lambda)$ turning arbitrary large. Maximizing the functional (15) under constraints (16) and (17) one therefore either reaches a maximum (in this case one has constructed the hyperplane with the maximal margin $\rho_0$), or one finds that the maximum exceeds some given (large) constant $W_0$ (in which case a separation of the training data with a margin larger then $\sqrt{2/W_0}$ is impossible).

The problem of maximizing functional (15) under constraints (16) and (17) can be solved very efficiently using the following scheme. Divide the training data into a number of portions with a reasonable small number of training vectors in each portion. Start out by solving the quadratic programming problem determined by the first portion of training data. For this problem there are two possible outcomes: either this portion of the data cannot be separated by a hyperplane (in which case the full set of data as well cannot be separated), or the optimal hyperplane for separating the first portion of the training data is found.

Let the vector that maximizes functional (15) in the case of separation of the first portion be $\Lambda_1$. Among the coordinates of vector $\Lambda_1$ some are equal to zero. They correspond to non-support training vectors of this portion. Make a new set of training data containing the support vectors from the first portion of training data and the vectors of the second portion that do not satisfy constraint (10), where w is determined by $\Lambda_1$. For this set a new functional $W_2(\Lambda)$ is constructed and maximized at $\Lambda_2$. Continuing this process of incrementally constructing a solution vector $\Lambda_*$ covering all the portions of the training data one either finds that it is impossible to separate the training set without error, or one constructs the optimal separating hyperplane for the full data set, $\Lambda_* = \Lambda_0$. Note, that during this process the value of the functional $W(\Lambda)$ is monotonically increasing, since more and more training vectors are considered in the optimization, leading to a smaller and smaller separation between the two classes.
