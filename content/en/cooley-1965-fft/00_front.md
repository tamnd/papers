---
paper: cooley-1965-fft
title: An Algorithm for the Machine Calculation of Complex Fourier Series
authors:
  - James W. Cooley
  - John W. Tukey
year: 1965
venue: Mathematics of Computation
field: algorithms
section_title: Front Matter
kind: front
lang: en
source: https://doi.org/10.1090/s0025-5718-1965-0178586-1
pdf_sha256: b4fa04410bcbf324eca035ab9d94818f075cee2f2ae38e99ebb0e2348e64654a
pdf_pages: 1-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 75f827c0ac01a12a53f6f7d8ac49df10329caa98952de96c18f1d44bf14b5a54
prompt_sha256: 329630a0b9175a55e4af1b8e281a3e67eeab250f8d643953b7dcde99743c7628
---

An Algorithm for the Machine Calculation of Complex Fourier Series

By James W. Cooley and John W. Tukey

An efficient method for the calculation of the interactions of a $2^m$ factorial experiment was introduced by Yates and is widely known by his name. The generalization to $3^m$ was given by Box et al. [1]. Good [2] generalized these methods and gave elegant algorithms for which one class of applications is the calculation of Fourier series. In their full generality, Good’s methods are applicable to certain problems in which one must multiply an $N$-vector by an $N \times N$ matrix which can be factored into $m$ sparse matrices, where $m$ is proportional to $\log N$. This results in a procedure requiring a number of operations proportional to $N \log N$ rather than $N^2$. These methods are applied here to the calculation of complex Fourier series. They are useful in situations where the number of data points is, or can be chosen to be, a highly composite number. The algorithm is here derived and presented in a rather different form. Attention is given to the choice of $N$. It is also shown how special advantage can be obtained in the use of a binary computer with $N = 2^m$ and how the entire calculation can be performed within the array of $N$ data storage locations used for the given Fourier coefficients.

Consider the problem of calculating the complex Fourier series
