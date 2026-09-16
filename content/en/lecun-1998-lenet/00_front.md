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
section_title: Front Matter
tag: 019F
kind: front
lang: en
source: https://doi.org/10.1109/5.726791
pdf_sha256: 346d2a5b49eb759da050572c187b93e35b68bd6a3b9c5d68c88e6ed96da386b7
pdf_pages: "2"
extraction: vision
extraction_model: gpt-5
content_sha256: 0069e98c470b2235463d2b782f74d728991b47787d9889e2d44fd4325d1ff38e
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

# Gradient-Based Learning Applied {#lecun-1998-lenet-s-gradient-based-learning-applied .section tag=0283}
# to Document Recognition {#lecun-1998-lenet-s-to-document-recognition .section tag=0284}

YANN LECUN, MEMBER, IEEE, LÉON BOTTOU, YOSHUA BENGIO, AND PATRICK HAFFNER

*Multilayer neural networks trained with the back-propagation algorithm constitute the best example of a successful gradient-based learning technique. Given an appropriate network architecture, gradient-based learning algorithms can be used to synthesize a complex decision surface that can classify high-dimensional patterns, such as handwritten characters, with minimal preprocessing. This paper reviews various methods applied to handwritten character recognition and compares them on a standard handwritten digit recognition task. Convolutional neural networks, which are specifically designed to deal with the variability of two dimensional (2-D) shapes, are shown to outperform all other techniques.*

*Real-life document recognition systems are composed of multiple modules including field extraction, segmentation, recognition, and language modeling. A new learning paradigm, called graph transformer networks (GTN’s), allows such multimodule systems to be trained globally using gradient-based methods so as to minimize an overall performance measure.*

*Two systems for online handwriting recognition are described. Experiments demonstrate the advantage of global training, and the flexibility of graph transformer networks.*

*A graph transformer network for reading a bank check is also described. It uses convolutional neural network character recognizers combined with global training techniques to provide record accuracy on business and personal checks. It is deployed commercially and reads several million checks per day.*

*Keywords— Convolutional neural networks, document recognition, finite state transducers, gradient-based learning, graph transformer networks, machine learning, neural networks, optical character recognition (OCR).*
