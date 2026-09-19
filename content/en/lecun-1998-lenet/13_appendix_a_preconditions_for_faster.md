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
section_title: Appendix a Preconditions for Faster Convergence
kind: appendix
lang: en
source: https://doi.org/10.1109/5.726791
pdf_sha256: 346d2a5b49eb759da050572c187b93e35b68bd6a3b9c5d68c88e6ed96da386b7
pdf_pages: "42"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 983920bbb33b542f2f035057cc3a64fec701aaa2fcafffd44f11eed5957cc8e2
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

As seen before, the squashing function used in our convolutional networks is $f(a) = A \tanh(Sa)$. Symmetric functions are believed to yield faster convergence, although the learning can become extremely slow if the weights are too small. The cause of this problem is that in weight space the origin is a fixed point of the learning dynamics and, although it is a saddle point, it is attractive in almost all directions [116]. For our simulations, we use $A = 1.7159$ and $S = 2/3$ (see [20], [34]). With this choice of parameters, the equalities $f(1) = 1$ and $f(-1) = -1$ are satisfied. The rationale behind this is that the overall gain of the squashing transformation is around one in normal operating conditions, and the interpretation of the state of the network is simplified. Moreover, the absolute value of the second derivative of $f$ is a maximum at $+1$ and $-1$, which improves the convergence toward the end of the learning session. This particular choice of parameters is merely a convenience, and does not affect the result.

Before training, the weights are initialized with random values using a uniform distribution between $-2.4/F_i$ and $2.4/F_i$, where $F_i$ is the number of inputs (fan-in) of the unit which the connection belongs to. Since several connections share a weight, this rule could be difficult to apply, but in our case all connections sharing a same weight belong to units with identical fan-ins. The reason for dividing by the fan-in is that we would like the initial standard deviation of the weighted sums to be in the same range for each unit and to fall within the normal operating region of the sigmoid. If the initial weights are too small, the gradients are very small and the learning is slow. If they are too large, the sigmoids are saturated and the gradient is also very small. The standard deviation of the weighted sum scales like the square root of the number of inputs when the inputs are independent, and it scales linearly with the number of inputs if the inputs are highly correlated. We chose to assume the second hypothesis since some units receive highly correlated signals.
