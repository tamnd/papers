---
paper: cortes-1995-svm
title: Support-Vector Networks
authors:
  - Corinna Cortes
  - Vladimir Vapnik
year: 1995
venue: Machine Learning
field: ai-ml
section: "4"
section_title: The Method of Convolution of the Dot-Product in Feature Space
tag: "0843"
kind: section
lang: en
source: https://doi.org/10.1023/a:1022627411411
pdf_sha256: 561361e49eb22df6f5e14f8c19d681c6b596891f07057fc43703394383233002
pdf_pages: 10-12
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: d7a0793a7237b5a29fefb94dcb4a017d126340841231652a0f670bdc6bcc09e8
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The algorithms described in the previous sections construct hyperplanes in the input space. To construct a hyperplane in a feature space one first has to transform the $n$-dimensional input vector $\mathbf{x}$ into an $N$-dimensional feature vector through a choice of an $N$-dimensional vector function $\phi$:

$$
\phi : \mathbb{R}^n \to \mathbb{R}^N.
$$

An $N$ dimensional linear separator $w$ and a bias $b$ is then constructed for the set of transformed vectors

$$
\phi(\mathbf{x}_i) = \phi_1(\mathbf{x}_i), \phi_2(\mathbf{x}_i), \ldots, \phi_N(\mathbf{x}_i), \quad i = 1, \ldots, \ell.
$$

Classification of an unknown vector $\mathbf{x}$ is done by first transforming the vector to the separating space ($\mathbf{x} \mapsto \phi(\mathbf{x})$) and then taking the sign of the function

$$
f(\mathbf{x}) = \mathbf{w} \cdot \phi(\mathbf{x}) + b.
$$

According to the properties of the soft margin classifier method the vector $\mathbf{w}$ can be written as a linear combination of support vectors (in the feature space). That means

$$
\mathbf{w} = \sum_{i=1}^\ell y_i \alpha_i \phi(\mathbf{x}_i).
$$

SUPPORT-VECTOR NETWORKS

The linearity of the dot-product implies, that the classification function $f$ in (31) for an unknown vector $\mathbf{x}$ only depends on the dot-products:

$$
f(\mathbf{x}) = \phi(\mathbf{x}) \cdot \mathbf{w} + b = \sum_{i=1}^{\ell} y_i \alpha_i \phi(\mathbf{x}) \cdot \phi(\mathbf{x}_i) + b.
$$

The idea of constructing support-vector networks comes from considering general forms of the dot-product in a Hilbert space (Anderson & Bahadur, 1966):

$$
\phi(\mathbf{u}) \cdot \phi(\mathbf{v}) \equiv K(\mathbf{u}, \mathbf{v}).
$$

According to the Hilbert-Schmidt Theory (Courant & Hilbert, 1953) any symmetric function $K(\mathbf{u}, \mathbf{v})$, with $K(\mathbf{u}, \mathbf{v}) \in L_2$, can be expanded in the form

$$
K(\mathbf{u}, \mathbf{v}) = \sum_{i=1}^{\infty} \lambda_i \phi_i(\mathbf{u}) \cdot \phi_i(\mathbf{v}),
$$

where $\lambda_i \in \mathfrak{R}$ and $\phi_i$ are eigenvalues and eigenfunctions

$$
\int K(\mathbf{u}, \mathbf{v}) \phi_i(\mathbf{u}) d\mathbf{u} = \lambda_i \phi_i(\mathbf{v}).
$$

of the integral operator defined by the kernel $K(\mathbf{u}, \mathbf{v})$. A sufficient condition to ensure that (34) defines a dot-product in a feature space is that all the eigenvalues in the expansion (35) are positive. To guarantee that these coefficients are positive, it is necessary and sufficient (Mercer’s Theorem) that the condition

$$
\int \int K(\mathbf{u}, \mathbf{v}) g(\mathbf{u}) g(\mathbf{v}) d\mathbf{u} d\mathbf{v} > 0
$$

is satisfied for all $g$ such that

$$
\int g^2(\mathbf{u}) d\mathbf{u} < \infty.
$$

Functions that satisfy Mercer’s theorem can therefore be used as dot-products. Aizerman, Braverman and Rozonoer (1964) consider a convolution of the dot-product in the feature space given by function of the form

$$
K(\mathbf{u}, \mathbf{v}) = \exp \left( - \frac{|\mathbf{u} - \mathbf{v}|}{\sigma} \right),
$$

which they call Potential Functions.

However, the convolution of the dot-product in feature space can be given by any function satisfying Mercer’s condition; in particular, to construct a polynomial classifier of degree $d$ in $n$-dimensional input space one can use the following function

$$
K(\mathbf{u}, \mathbf{v}) = (\mathbf{u} \cdot \mathbf{v} + 1)^d.
$$

Using different dot-products $K(\mathbf{u}, \mathbf{v})$ one can construct different learning machines with arbitrary types of decision surfaces (Boser, Guyon & Vapnik, 1992). The decision surface of these machines has a form

$$
f(\mathbf{x}) = \sum_{i=1}^{\ell} y_i \alpha_i K(\mathbf{x}, \mathbf{x}_i),
$$

where $\mathbf{x}_i$ is the image of a support vector in input space and $\alpha_i$ is the weight of a support vector in the feature space.

To find the vectors $\mathbf{x}_i$ and weights $\alpha_i$ one follows the same solution scheme as for the original optimal margin classifier or soft margin classifier. The only difference is that instead of matrix $D$ (determined by (18)) one uses the matrix

$$
D_{ij} = y_i y_j K(\mathbf{x}_i, \mathbf{x}_j), \qquad i,\ j = 1, \ldots, l.
$$
