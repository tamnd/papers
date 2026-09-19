---
paper: krizhevsky-2012-imagenet
title: ImageNet Classification with Deep Convolutional Neural Networks
authors:
  - Alex Krizhevsky
  - Ilya Sutskever
  - Geoffrey E. Hinton
year: 2012
venue: NIPS
field: ai-ml
section: "2"
section_title: The Dataset
tag: 04A7
kind: section
lang: en
source: https://ci.nii.ac.jp/naid/20001617881
pdf_sha256: 90137160c57217953d5f61857e64ca58e85f06e1b13b4f475c918b1b582b9771
pdf_pages: "2"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: dd190c997efee7a28e768339945726ceae5c48ee4ab19d279a2c54186715c20d
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

ImageNet is a dataset of over 15 million labeled high-resolution images belonging to roughly 22,000 categories. The images were collected from the web and labeled by human labelers using Amazon’s Mechanical Turk crowd-sourcing tool. Starting in 2010, as part of the Pascal Visual Object Challenge, an annual competition called the ImageNet Large-Scale Visual Recognition Challenge (ILSVRC) has been held. ILSVRC uses a subset of ImageNet with roughly 1000 images in each of 1000 categories. In all, there are roughly 1.2 million training images, 50,000 validation images, and 150,000 testing images.

ILSVRC-2010 is the only version of ILSVRC for which the test set labels are available, so this is the version on which we performed most of our experiments. Since we also entered our model in the ILSVRC-2012 competition, in Section 6 we report our results on this version of the dataset as well, for which test set labels are unavailable. On ImageNet, it is customary to report two error rates: top-1 and top-5, where the top-5 error rate is the fraction of test images for which the correct label is not among the five labels considered most probable by the model.

ImageNet consists of variable-resolution images, while our system requires a constant input dimensionality. Therefore, we down-sampled the images to a fixed resolution of $256 \times 256$. Given a rectangular image, we first rescaled the image such that the shorter side was of length 256, and then cropped out the central $256 \times 256$ patch from the resulting image. We did not pre-process the images in any other way, except for subtracting the mean activity over the training set from each pixel. So we trained our network on the (centered) raw RGB values of the pixels.
