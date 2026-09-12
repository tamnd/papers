---
paper: rumelhart-1986-backprop
title: Learning Representations by Back-propagating Errors
authors:
  - David E. Rumelhart
  - Geoffrey E. Hinton
  - Ronald J. Williams
year: 1986
venue: Nature
field: ai-ml
section_title: Front Matter
kind: front
lang: en
source: https://www.iro.umontreal.ca/~vincentp/ift3395/lectures/backprop_old.pdf
pdf_sha256: 2c011a4ffae95e49e1ad0f09a966b386f47db75eab718384bc48c87e90aeffdd
pdf_pages: 1-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: e4e258b8d5ddd5267175bbf36f016ae2f5273bb9c3f3772bec7ceaac8fd928af
prompt_sha256: 329630a0b9175a55e4af1b8e281a3e67eeab250f8d643953b7dcde99743c7628
---

Learning representations by back-propagating errors

David E. Rumelhart*, Geoffrey E. Hinton† & Ronald J. Williams*

* Institute for Cognitive Science, C-015, University of California, San Diego, La Jolla, California 92093, USA

† Department of Computer Science, Carnegie-Mellon University, Pittsburgh, Philadelphia 15213, USA

We describe a new learning procedure, back-propagation, for networks of neurone-like units. The procedure repeatedly adjusts the weights of the connections in the network so as to minimize a measure of the difference between the actual output vector of the net and the desired output vector. As a result of the weight adjustments, internal 'hidden' units which are not part of the input or output come to represent important features of the task domain, and the regularities in the task are captured by the interactions of these units. The ability to create useful new features distinguishes back-propagation from earlier, simpler methods such as the perceptron-convergence procedure¹.

There have been many attempts to design self-organizing neural networks. The aim is to find a powerful synaptic modification rule that will allow an arbitrarily connected neural network to develop an internal structure that is appropriate for a particular task domain. The task is specified by giving the desired state vector of the output units for each state vector of the input units.
