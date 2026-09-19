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
section: XI
section_title: CONCLUSIONS
tag: 08C9
kind: section
lang: en
source: https://doi.org/10.1109/5.726791
pdf_sha256: 346d2a5b49eb759da050572c187b93e35b68bd6a3b9c5d68c88e6ed96da386b7
pdf_pages: 41-42
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 6204d4070836a32e426d0518d61763d97163840d3793f6863d16b74bf46134f2
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

During the short history of automatic pattern recognition, increasing the role of learning seems to have invariably improved the overall performance of recognition systems. The systems described in this paper are more evidence to this fact. Convolutional NN’s have been shown to eliminate the need for hand-crafted feature extractors. GTN’s have been shown to reduce the need for hand-crafted heuristics, manual labeling, and manual parameter tuning in document recognition systems. As training data becomes plentiful, as computers get faster, and as our understanding of learning algorithms improves, recognition systems will rely more and more of learning and their performance will improve.

Just as the back-propagation algorithm elegantly solved the credit assignment problem in multilayer NN’s, the gradient-based learning procedure for GTN’s introduced in this paper solves the credit assignment problem in systems whose functional architecture dynamically changes with each new input. The learning algorithms presented here are in a sense nothing more than unusual forms of gradient descent in complex, dynamic architectures, with efficient back-propagation algorithms to compute the gradient. The results in this paper help establish the usefulness and relevance of gradient-based minimization methods as a general organizing principle for learning in large systems.

It was shown that all the steps of a document analysis system can be formulated as GT’s through which gradients can be back propagated. Even in the nontrainable parts of the system, the design philosophy in terms of graph transformation provides a clear separation between domain-specific heuristics (e.g., segmentation heuristics) and generic, procedural knowledge (the generalized transduction algorithm)

It is worth pointing out that data generating models (such as HMM’s) and the maximum likelihood principle were not called upon to justify most of the architectures and the training criteria described in this paper. Gradient-based learning applied to global discriminative loss functions guarantees optimal classification and rejection without the use of “hard to justify” principles that put strong constraints on the system architecture, often at the expense of performances.

More specifically, the methods and architectures presented in this paper offer generic solutions to a large number of problems encountered in pattern recognition systems.

1) Feature extraction is traditionally a fixed transform, and it is generally derived from some expert prior knowledge about the task. This relies on the probably incorrect assumption that the human designer is able to capture all the relevant information in the input. We have shown that the application of gradient-based learning to convolutional NN’s allows us to learn appropriate features from examples. The success of this approach was demonstrated in extensive comparative digit recognition experiments on the NIST database.

2) Segmentation and recognition of objects in images cannot be completely decoupled. Instead of taking hard segmentation decisions too early, we have used HOS to generate and evaluate a large number of hypotheses in parallel, postponing any decision until the overall criterion is minimized.

3) Hand-truthing images to obtain segmented characters for training a character recognizer is expensive and does not take into account the way in which a whole document or sequence of characters will be recognized (in particular, the fact that some segmentation candidates may be wrong, even though they may look like true characters). Instead we train multinode systems to optimize a global measure of performance, which does not require time consuming detailed hand-truthing and yields significantly better recognition performance because it allows to train these modules to cooperate toward a common goal.

4) Ambiguities inherent in the segmentation, character recognition, and linguistic model should be integrated optimally. Instead of using a sequence of task-dependent heuristics to combine these sources of information, we have proposed a unified framework in which generalized transduction methods are applied to graphs representing a weighted set of hypotheses about the input. The success of this approach was demonstrated with a commercially deployed check-reading system that reads millions of business and personal checks per day: the generalized transduction engine resides in only a few hundred lines of code.

5) Traditional recognition systems rely on many hand-crafted heuristics to isolate individually recognizable objects. The promising SDNN approach draws on the robustness and efficiency of convolutional NN’s to avoid explicit segmentation altogether. Simultaneous automatic learning of segmentation and recognition can be achieved with gradient-based learning methods.

This paper presents a small number of examples of GT modules, but it is clear that the concept can be applied to many situations where the domain knowledge or the state information can be represented by graphs. This is the case in many audio signal recognition tasks, and visual scene analysis applications. Future work will attempt to apply GT networks to such problems, with the hope of allowing more reliance on automatic learning and less on detailed engineering.
