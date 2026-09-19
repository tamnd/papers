---
paper: lecun-1998-lenet
title: Gradient-Based Learning Applied to Document Recognition
authors:
  - Yann LeCun
  - Leon Bottou
  - Yoshua Bengio
  - Patrick Haffner
year: 1998
venue: Proceedings of the IEEE
field: ai-ml
section_title: Appendix C Stochastic Diagonal Levenberg–marquardt
kind: appendix
lang: en
source: https://doi.org/10.1109/5.726791
pdf_sha256: 346d2a5b49eb759da050572c187b93e35b68bd6a3b9c5d68c88e6ed96da386b7
pdf_pages: 43-44
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 602acab7978ebda4bcf0e3d2a75cef2895c714649e3506482392de7155e66772
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Owing to the reasons given in Appendix B, we prefer to update the weights after each presentation of a single pattern in accordance with stochastic update methods. The patterns are presented in a constant random order, and the training set is typically repeated 20 times.

Our update algorithm is dubbed the stochastic diagonal Levenberg–Marquardt method where an individual learning rate (step size) is computed for each parameter (weight) before each pass through the training set [20], [34], [121]. These learning rates are computed using the diagonal terms of an estimate of the Gauss–Newton approximation to the Hessian (second derivative) matrix. This algorithm is not believed to bring a tremendous increase in learning speed but it converges reliably without requiring extensive adjustments of the learning parameters. It corrects major ill-conditioning of the loss function that are due to the peculiarities of the network architecture and the training data. The additional cost of using this procedure over standard stochastic gradient descent is negligible.

At each learning iteration a particular parameter $w_k$ is updated according to the following stochastic update rule:

$$
w_k \leftarrow w_k - \epsilon_k \frac{\partial E^p}{\partial w_k}
$$

where $E^p$ is the instantaneous loss function for pattern $p$. In convolutional NN’s, because of the weight sharing, the partial derivative $\partial E^p / \partial w_k$ is the sum of the partial derivatives with respect to the connections that share the parameter $w_k$

$$
\frac{\partial E^p}{\partial w_k} = \sum_{(i,j) \in V_k} \frac{\partial E^p}{\partial u_{ij}}
$$

where $u_{ij}$ is the connection weight from unit $j$ to unit $i$, $V_k$ is the set of unit index pairs $(i, j)$ such that the connection between $i$ and $j$ share the parameter $w_k$, i.e.,

$$
u_{ij} = w_k \quad \forall (i, j) \in V_k.
$$

As stated previously, the step sizes $\epsilon_k$ are not constant but are function of the second derivative of the loss function along the axis $w_k$

$$
\epsilon_k = \frac{\eta}{\mu + h_{kk}}
$$

where $\mu$ is a hand-picked constant and $h_{kk}$ is an estimate of the second derivative of the loss function $E$ with respect to $w_k$. The larger $h_{kk}$ is, the smaller the weight update. The parameter $\mu$ prevents the step size from becoming too large when the second derivative is small, very much like the “model-trust” methods, and the Levenberg–Marquardt methods in nonlinear optimization [8]. The exact formula to compute $h_{kk}$ from the second derivatives with respect to the connection weights is

$$
h_{kk} = \sum_{(i,j) \in V_k} \sum_{(k,l) \in V_k} \frac{\partial^2 E}{\partial u_{ij} \partial u_{kl}}.
$$

However, we make three approximations. The first approximation is to drop the off-diagonal terms of the Hessian with respect to the connection weights in (22)

$$
h_{kk} = \sum_{(i,j) \in V_k} \frac{\partial^2 E}{\partial u_{ij}^2}.
$$

Naturally, the terms $\partial^2 E / \partial u_{ij}^2$ are the average over the training set of the local second derivatives

$$
\frac{\partial^2 E}{\partial u_{ij}^2} = \frac{1}{P} \sum_{p=1}^P \frac{\partial^2 E^p}{\partial u_{ij}^2}.
$$

Those local second derivatives with respect to connection weights can be computed from local second derivatives with respect to the total input of the downstream unit

$$
\frac{\partial^2 E^p}{\partial u_{ij}^2} = \frac{\partial^2 E^p}{\partial a_i^2} x_j^2
$$

where $x_j$ is the state of unit $j$ and $\partial^2 E^p / \partial a_i^2$ is the second derivative of the instantaneous loss function with respect to the total input to unit $i$ (denoted $a_i$). Interestingly, there is an efficient algorithm to compute those second derivatives which is very similar to the back-propagation procedure used to compute the first derivatives [20], [21]

$$
\frac{\partial^2 E^p}{\partial a_i^2} = f'(a_i)^2 \sum_k u_{ki}^2 \frac{\partial^2 E^p}{\partial a_k^2} + f''(a_i) \frac{\partial E^p}{\partial x_i}.
$$

Unfortunately, using those derivatives leads to well-known problems associated with every Newton-like algorithm: these terms can be negative and can cause the gradient algorithm to move uphill instead of downhill. Therefore, our second approximation is a well-known trick called the Gauss–Newton approximation, which guarantees that the second derivative estimates are nonnegative. The Gauss–Newton approximation essentially ignores the nonlinearity of the estimated function (the NN, in our case), but not that of the loss function. The back propagation equation for Gauss-Newton approximations of the second derivatives is

$$
\frac{\partial^2 E^p}{\partial a_i^2} = f'(a_i)^2 \sum_k u_{ki}^2 \frac{\partial^2 E^p}{\partial a_k^2}.
$$

This is very similar to the formula for back propagating the first derivatives, except that the sigmoid’s derivative and the weight values are squared. The right-hand side is a sum of products of nonnegative terms, therefore the left-hand side term is nonnegative.

The third approximation we make is that we do not run the average in (24) over the entire training set, but run it on a small subset of the training set instead. In addition the re-estimation does not need to be done often since the second-order properties of the error surface change rather slowly. In the experiments described in this paper, we re-estimate the $h_{kk}$ on 500 patterns before each training pass through the training set. Since the size of the training set is 60 000, the additional cost of re-estimating the $h_{kk}$ is negligible. The estimates are not particularly sensitive to the particular subset of the training set used in the averaging. This seems to suggest that the second-order properties of the error surface are mainly determined by the structure of the network, rather than by the detailed statistics of the samples. This algorithm is particularly useful for shared-weight networks because the weight sharing creates ill conditioning of the error surface. Because of the sharing, one single parameter in the first few layers can have an enormous influence on the output. Consequently, the second derivative of the error with respect to this parameter may be very large, while it can be quite small for other parameters elsewhere in the network. The above algorithm compensates for that phenomenon.

Unlike most other second-order acceleration methods for back-propagation, the above method works in stochastic mode. It uses a diagonal approximation of the Hessian. Like the classical Levenberg–Marquardt algorithm, it uses a “safety” factor $\mu$ to prevent the step sizes from getting too large if the second derivative estimates are small. Hence the method is called the stochastic diagonal Levenberg–Marquardt method.
