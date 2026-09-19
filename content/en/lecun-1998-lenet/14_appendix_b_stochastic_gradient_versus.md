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
section_title: Appendix B Stochastic Gradient Versus Batch Gradient
kind: appendix
lang: en
source: https://doi.org/10.1109/5.726791
pdf_sha256: 346d2a5b49eb759da050572c187b93e35b68bd6a3b9c5d68c88e6ed96da386b7
pdf_pages: "43"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 8621f38e3c9da49583114406881e86b2c39a1f9b5ac90ccf4f61b8da7b6652ad
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Gradient-based learning algorithms can use one of two classes of methods to update the parameters. The first method, dubbed “batch gradient,” is the classical one: the gradients are accumulated over the entire training set, and the parameters are updated after the exact gradient has been so computed. In the second method, called “stochastic gradient,” a partial, or noisy, gradient is evaluated on the basis of one single training sample (or a small number of samples), and the parameters are updated using this approximate gradient. The training samples can be selected randomly or according to a properly randomized sequence. In the stochastic version the gradient estimates are noisy, but the parameters are updated much more often than with the batch version. An empirical result of considerable practical importance is that on tasks with large, redundant data sets, the stochastic version is considerably faster than the batch version, sometimes by orders of magnitude [117]. Although the reasons for this are not totally understood theoretically, an intuitive explanation can be found in the following extreme example. Let us take an example where the training database is composed of two copies of the same subset. Then accumulating the gradient over the whole set would cause redundant computations to be performed. On the other hand, running Stochastic Gradient once on this training set would amount to performing two complete learning iterations over the small subset. This idea can be generalized to training sets where there exist no precise repetition of the same pattern but where some redundancy is present. In fact stochastic update must be better when there is redundancy, i.e., when a certain level of generalization is expected.

Many authors have claimed that second-order methods should be used in lieu of gradient descent for NN training. The literature abounds with recommendations [118] for classical second-order methods such as the Gauss–Newton or Levenberg–Marquardt algorithms for quasi-Newton methods such as Broyden–Fletcher–Goldfarb–Shanno, limited-storage Broyden–Fletcher–Goldfarb–Shanno, or for various versions of the conjugate gradients method. Unfortunately, all of the above methods are unsuitable for training large NN’s on large data sets. The Gauss–Newton and Levenberg–Marquardt methods require $O(N^3)$ operations per update, where $N$ is the number of parameters, which makes them impractical for even moderate size networks. Quasi-Newton methods require “only” $O(N^2)$ operations per update, but that still makes them impractical for large networks. Limited-storage Broyden–Fletcher–Goldfarb–Shanno’s and conjugate gradients require only $O(N)$ operations per update so they would appear appropriate. Unfortunately, their convergence speed relies on an accurate evaluation of successive “conjugate descent directions” which only makes sense in “batch” mode. For large data sets, the speed-up brought by these methods over regular batch gradient descent cannot match the enormous speed up brought by the use of stochastic gradient. Several authors have attempted to use conjugate gradient with small batches or batches of increasing sizes [119], [120], but those attempts have not yet been demonstrated to surpass a carefully tuned stochastic gradient. Our experiments were performed with a stochastic method that scales the parameter axes so as to minimize the eccentricity of the error surface.
