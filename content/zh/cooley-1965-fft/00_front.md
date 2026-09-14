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
tag: "0040"
kind: front
lang: zh
source: https://doi.org/10.1090/s0025-5718-1965-0178586-1
pdf_sha256: b4fa04410bcbf324eca035ab9d94818f075cee2f2ae38e99ebb0e2348e64654a
pdf_pages: 1-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 677c81e332823dbced872f18cdb3d8e479272bc30da692d38e400aadd163fd2d
translated_from: content/en/cooley-1965-fft/00_front.md
source_content_sha256: 75f827c0ac01a12a53f6f7d8ac49df10329caa98952de96c18f1d44bf14b5a54
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: efacc7653691a9b863e3c4cb746743abfecf7d31e7791764c13a541e1906db0f
prompt_sha256: da0c2696badfbe5d93fdc534847b1b0ca3b25ec37e0ce29843665f6e701c278e
---

一种用于机器计算复傅里叶级数的算法

作者：James W. Cooley和John W. Tukey

Yates提出了一种用于计算$2^m$阶乘实验交互作用的高效方法，并以其名字广为人知。Box等人[1]给出了向$3^m$的推广。Good[2]进一步推广了这些方法，并给出了优雅的算法，其中一类应用是计算傅里叶级数。在最一般的形式下，Good的方法适用于这样一类问题：必须将一个$N$-向量与一个$N \times N$矩阵相乘，而该矩阵可以分解为$m$个稀疏矩阵，其中$m$与$\log N$成正比。由此得到的过程所需的运算次数与$N \log N$成正比，而不是与$N^2$成正比。本文将这些方法应用于复傅里叶级数的计算。当数据点数是或可以选择为一个高度合成数时，这些方法很有用。本文以一种颇为不同的形式推导并给出了该算法。文中还讨论了$N$的选择。此外，本文说明了在$N = 2^m$的二进制计算机上如何获得特殊的优势，以及如何在用于给定傅里叶系数的$N$个数据存储位置组成的数组内完成整个计算。

考虑计算复傅里叶级数的问题
