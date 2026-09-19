---
paper: cortes-1995-svm
title: Support-Vector Networks
authors:
  - Corinna Cortes
  - Vladimir Vapnik
year: 1995
venue: Machine Learning
field: ai-ml
section: "1"
section_title: Introduction
tag: 083D
kind: section
lang: en
source: https://doi.org/10.1023/a:1022627411411
pdf_sha256: 561361e49eb22df6f5e14f8c19d681c6b596891f07057fc43703394383233002
pdf_pages: 1-5
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 6ec15714d0e3a9a46f496f71370573320139c8c8a659f5f02f0b2247fbd751b7
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

More than 60 years ago R.A. Fisher (Fisher, 1936) suggested the first algorithm for pattern recognition. He considered a model of two normal distributed populations, $N(\mathbf{m}_1, \Sigma_1)$ and $N(\mathbf{m}_2, \Sigma_2)$ of $n$ dimensional vectors $\mathbf{x}$ with mean vectors $\mathbf{m}_1$ and $\mathbf{m}_2$ and co-variance matrices $\Sigma_1$ and $\Sigma_2$, and showed that the optimal (Bayesian) solution is a quadratic decision function:

$$
F_{sq}(\mathbf{x}) = \operatorname{sign}\left[ \frac{1}{2} (\mathbf{x} - \mathbf{m}_1)^T \Sigma_1^{-1} (\mathbf{x} - \mathbf{m}_1) - \frac{1}{2} (\mathbf{x} - \mathbf{m}_2)^T \Sigma_2^{-1} (\mathbf{x} - \mathbf{m}_2) + \ln \frac{|\Sigma_2|}{|\Sigma_1|} \right].
$$

In the case where $\Sigma_1 = \Sigma_2 = \Sigma$ the quadratic decision function (1) degenerates to a linear function:

$$
F_{lin}(\mathbf{x}) = \operatorname{sign}\left[ (\mathbf{m}_1 - \mathbf{m}_2)^T \Sigma^{-1} \mathbf{x} - \frac{1}{2} (\mathbf{m}_1^T \Sigma^{-1} \mathbf{m}_1 - \mathbf{m}_2^T \Sigma^{-1} \mathbf{m}_2) \right].
$$

To estimate the quadratic decision function one has to determine $\frac{n(n+3)}{2}$ free parameters. To estimate the linear function only $n$ free parameters have to be determined. In the case where the number of observations is small (say less than $10 n^2$) estimating $o(n^2)$ parameters is not reliable. Fisher therefore recommended, even in the case of $\Sigma_1 \neq \Sigma_2$, to use the linear discriminator function (2) with $\Sigma$ of the form:

$$
\Sigma = \tau \Sigma_1 + (1 - \tau) \Sigma_2,
$$

where $\tau$ is some constant$^1$. Fisher also recommended a linear decision function for the case where the two distributions are not normal. Algorithms for pattern recognition perceptron output
weights of the output unit,
$\alpha_1, \ldots, \alpha_5$
output from the 5 hidden units: $z_1, \ldots, z_5$
weights of the 5 hidden units
output from the 4 hidden units
weights of the 4 hidden units
input vector, $x$ were therefore from the very beginning associated with the construction of linear decision surfaces.

Figure 1. A simple feed-forward perceptron with 8 input units, 2 layers of hidden units, and 1 output unit. The gray-shading of the vector entries reflects their numeric value. {#cortes-1995-svm-fig-1 .figure tag=049F}

In 1962 Rosenblatt (Rosenblatt, 1962) explored a different kind of learning machines: perceptrons or neural networks. The perceptron consists of connected neurons, where each neuron implements a separating hyperplane, so the perceptron as a whole implements a piecewise linear separating surface. See Fig. 1.

No algorithm that minimizes the error on a set of vectors by adjusting all the weights of the network was found in Rosenblatt’s time, and Rosenblatt suggested a scheme where only the weights of the output unit were adaptive. According to the fixed setting of the other weights the input vectors are non-linearly transformed into the feature space, $Z$, of the last layer of units. In this space a linear decision function is constructed:

$$
I(x) = \operatorname{sign}\left( \sum_i \alpha_i z_i(x) \right)
$$

by adjusting the weights $\alpha_i$ from the $i$th hidden unit to the output unit so as to minimize some error measure over the training data. As a result of Rosenblatt’s approach, construction of decision rules was again associated with the construction of linear hyperplanes in some space.

An algorithm that allows for all weights of the neural network to adapt in order locally to minimize the error on a set of vectors belonging to a pattern recognition problem was found in 1986 (Rumelhart, Hinton & Williams, 1986, 1987; Parker, 1985; LeCun, 1985) when the back-propagation algorithm was discovered. The solution involves a slight modification of the mathematical model of neurons. Therefore, neural networks implement “piece-wise linear-type” decision functions.

In this article we construct a new type of learning machine, the so-called support-vector network. The support-vector network implements the following idea: it maps the input vectors into some high dimensional feature space $Z$ through some non-linear mapping chosen a priori. In this space a linear decision surface is constructed with special properties that ensure high generalization ability of the network.

Figure 2. An example of a separable problem in a 2 dimensional space. The support vectors, marked with grey squares, define the margin of largest separation between the two classes. {#cortes-1995-svm-fig-2 .figure tag=04A0}

EXAMPLE. To obtain a decision surface corresponding to a polynomial of degree two, one can create a feature space, $Z$, which has $N = \frac{n(n+3)}{2}$ coordinates of the form:

$$
z_1 = x_1, \ldots, z_n = x_n, \quad n \text{ coordinates},
$$

$$
z_{n+1} = x_1^2, \ldots, z_{2n} = x_n^2, \quad n \text{ coordinates},
$$

$$
z_{2n+1} = x_1 x_2, \ldots, z_N = x_n x_{n-1}, \quad \frac{n(n-1)}{2} \text{ coordinates},
$$

where $\mathbf{x} = (x_1, \ldots, x_n)$. The hyperplane is then constructed in this space.

Two problems arise in the above approach: one conceptual and one technical. The conceptual problem is how to find a separating hyperplane that will generalize well: the dimensionality of the feature space will be huge, and not all hyperplanes that separate the training data will necessarily generalize well$^2$. The technical problem is how computationally to treat such high-dimensional spaces: to construct polynomial of degree 4 or 5 in a 200 dimensional space it may be necessary to construct hyperplanes in a billion dimensional feature space.

The conceptual part of this problem was solved in 1965 (Vapnik, 1982) for the case of *optimal hyperplanes* for separable classes. An optimal hyperplane is here defined as the linear decision function with maximal margin between the vectors of the two classes, see Fig. 2. It was observed that to construct such optimal hyperplanes one only has to take into account a small amount of the training data, the so called *support vectors*, which determine this margin. It was shown that if the training vectors are separated without errors by an optimal hyperplane the expectation value of the probability of committing an error on a test example is bounded by the ratio between the expectation value of the number of support vectors and the number of training vectors:

$$
E[\Pr(\text{error})] \leq \frac{E[\text{number of support vectors}]}{\text{number of training vectors}}.
$$

Note that this bound does not explicitly contain the dimensionality of the space of separation. It follows from this bound, that if the optimal hyperplane can be constructed from a small number of support vectors relative to the training set size the generalization ability will be high—even in an infinite dimensional space. In Section 5 we will demonstrate that the ratio (5) for a real life problems can be as low as 0.03 and the optimal hyperplane generalizes well in a billion dimensional feature space.

Let

$$
w_0 \cdot z + b_0 = 0
$$

be the optimal hyperplane in feature space. We will show, that the weights $w_0$ for the optimal hyperplane in the feature space can be written as some linear combination of support vectors

$$
w_0 = \sum_{\text{support vectors}} \alpha_i z_i.
$$

The linear decision function $I(z)$ in the feature space will accordingly be of the form:

$$
I(z) = \operatorname{sign}\left( \sum_{\text{support vectors}} \alpha_i z_i \cdot z + b_0 \right),
$$

where $z_i \cdot z$ is the dot-product between support vectors $z_i$ and vector $z$ in feature space. The decision function can therefore be described as a two layer network (Fig. 3).

However, even if the optimal hyperplane generalizes well the technical problem of how to treat the high dimensional feature space remains. In 1992 it was shown (Boser, Guyon, & Vapnik, 1992), that the order of operations for constructing a decision function can be interchanged: instead of making a non-linear transformation of the input vectors followed by dot-products with support vectors in feature space, one can first compare two vectors in input space (by e.g. taking their dot-product or some distance measure), and then make a non-linear transformation of the value of the result (see Fig. 4). This enables the construction of rich classes of decision surfaces, for example polynomial decision surfaces of arbitrary degree. We will call this type of learning machine a support-vector network$^3$.

The technique of support-vector networks was first developed for the restricted case of separating training data without errors. In this article we extend the approach of support-vector networks to cover when separation without error on the training vectors is impossible. With this extension we consider the support-vector networks as a new class of learning machine, as powerful and universal as neural networks. In Section 5 we will demonstrate how well it generalizes for high degree polynomial decision surfaces (up to order 7) in a high dimensional space (dimension 256). The performance of the algorithm is compared to that of classical learning machines e.g. linear classifiers, $k$-nearest neighbors classifiers, and neural networks. Sections 2, 3, and 4 are devoted to the major points of the derivation of the algorithm and a discussion of some of its properties. Details of the derivation are relegated to an appendix.

Figure 3. Classification by a support-vector network of an unknown pattern is conceptually done by first transforming the pattern into some high-dimensional feature space. An optimal hyperplane constructed in this feature space determines the output. The similarity to a two-layer perceptron can be seen by comparison to Fig. 1. {#cortes-1995-svm-fig-3 .figure tag=083E}
