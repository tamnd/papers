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
section: V
section_title: 'MULTIPLE OBJECT RECOGNITION: HOS'
tag: 08B5
kind: section
lang: en
source: https://doi.org/10.1109/5.726791
pdf_sha256: 346d2a5b49eb759da050572c187b93e35b68bd6a3b9c5d68c88e6ed96da386b7
pdf_pages: 21-23
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 26f718cecce152cb0e8b14e4d648221cd1cdd9e9afcb1967a71f0e1950d9e627
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

One of the most difficult problems of handwriting recognition is to recognize not just isolated characters, but strings of characters such as zip codes, check amounts, or words. Since most recognizers can only deal with one character at a time, we must first segment the string into individual character images. However, it is almost impossible to devise image analysis techniques that will infallibly segment naturally written sequences of characters into well formed characters.

The recent history of automatic speech recognition [28], [67] is here to remind us that training a recognizer by optimizing a global criterion (at the word or sentence level) is much preferable to merely training it on hand-segmented phonemes or other units. Several recent works have shown that the same is true for handwriting recognition [38]: optimizing a word-level criterion is preferable to solely training a recognizer on presegmented characters because the recognizer can learn not only to recognize individual characters, but also to reject missegmented characters, thereby minimizing the overall word error.

This section and Section VI describe in detail a simple example of GTN to address the problem of reading strings of characters, such as words or check amounts. The method avoids the expensive and unreliable task of hand-truthing the result of the segmentation often required in more traditional systems trained on individually labeled character images.

A. Segmentation Graph

A now classical method for segmentation and recognition is called HOS [68], [69]. Its main advantages over other approaches to segmentation are that it avoids making hard decisions about the segmentation by taking a large number of different segmentations into consideration. The idea is to use heuristic image processing techniques to find candidate cuts of the word or string, and then to use the recognizer to score the alternative segmentations thereby generated. The process is depicted in Fig. 16. First, a number of candidate cuts are generated. Good candidate locations for cuts can be found by locating minima in the vertical projection profile, or minima of the distance between the upper and lower contours of the word. Better segmentation heuristics are described in Section XI. The cut generation heuristic is designed so as to generate more cuts than necessary in the hope that the “correct” set of cuts will be included. Once the cuts have been generated, alternative segmentations are best represented by a graph, called the segmentation graph. The segmentation graph is a directed acyclic graph with a start node and an end node. Each internal node is associated with a candidate cut produced by the segmentation algorithm. Each arc between a source node and a destination node is associated with an image that contains all the ink between the cut associated with the source node and the cut associated with the destination node. An arc is created between two nodes if the segmentor decided that the ink between the corresponding cuts could form a candidate character. Typically, each individual piece of ink would be associated with an arc. Pairs of successive pieces of ink would also be included, unless they are separated by a wide gap, which is a clear indication that they belong to different characters. Each complete path through the graph contains each piece of ink once and only once. Each path corresponds to a different way of associating pieces of ink together so as to form characters.

Fig. 17. Recognizing a character string with a GTN. For readability, only the arcs with low penalties are shown. {#lecun-1998-lenet-fig-17 .figure tag=08B6}

B. Recognition Transformer and Viterbi Transformer

A simple GTN to recognize character strings is shown in Fig. 17. It is composed of two GT’s called the recognition transformer $T_{rec}$ and the Viterbi transformer $T_{vit}$. The goal of the recognition transformer is to generate a graph, called the interpretation graph or recognition graph $G_{int}$, that contains all the possible interpretations for all the possible segmentations of the input. Each path in $G_{int}$ represents one possible interpretation of one particular segmentation of the input. The role of the Viterbi transformer is to extract the best interpretation from the interpretation graph.

The recognition transformer $T_{rec}$ takes the segmentation graph $G_{seg}$ as input, and applies the recognizer for single characters to the images associated with each of the arcs in the segmentation graph. The interpretation graph $G_{int}$ has almost the same structure as the segmentation graph, except that each arc is replaced by a set of arcs from and to the same node. In this set of arcs, there is one arc for each possible class for the image associated with the corresponding arc in $G_{seg}$. As shown in Fig. 18, to each arc is attached a class label, and the penalty that the image belongs to this class as produced by the recognizer. If the segmentor has computed penalties for the candidate segments, these penalties are combined with the penalties computed by the character recognizer to obtain the penalties on the arcs of the interpretation graph. Although combining penalties of different nature seems highly heuristic, the GTN training procedure will tune the penalties and take advantage of this combination anyway. Each path in the interpretation graph corresponds to a possible interpretation of the input word. The penalty of a particular interpretation for a particular segmentation is given by the sum of the arc penalties along the corresponding path in the interpretation graph. Computing the penalty of an interpretation independently of the segmentation requires to combine the penalties of all the paths with that interpretation. An appropriate rule for combining the penalties of parallel paths is given in Section VI-C.

Fig. 18. The recognition transformer refines each arc of the segmentation arc into a set of arcs in the interpretation graph, one per character class, with attached penalties and labels. {#lecun-1998-lenet-fig-18 .figure tag=08B7}

The Viterbi transformer produces a graph $G_{vit}$ with a single path. This path is the path of least cumulated penalty in the Interpretation graph. The result of the recognition can be produced by reading off the labels of the arcs along the graph $G_{vit}$ extracted by the Viterbi transformer. The Viterbi transformer owes its name to the famous Viterbi algorithm [70], an application of the principle of dynamic programming to find the shortest path in a graph efficiently. Let $c_i$ be the penalty associated to arc $i$, with source node $s_i$ and destination node $d_i$ (note that there can be multiple arcs between two nodes). In the interpretation graph, arcs also have a label $l_i$. The Viterbi algorithm proceeds as follows. Each node $n$ is associated with a cumulated Viterbi penalty $v_n$. Those cumulated penalties are computed in any order that satisfies the partial order defined by the interpretation graph (which is directed and acyclic). The start node is initialized with the cumulated penalty $v_{start} = 0$. The other nodes cumulated penalties $v_n$ are computed recursively from the $v$ values of their parent nodes, through the upstream arcs $U_n = \{ \text{arc } i \text{ with destination } d_i = n \}$

$$
v_n = \min_{i \in U_n} (c_i + v_{s_i}).
$$

Furthermore, the value of $i$ for each node $n$ which minimizes the right-hand side is noted $m_n$, the minimizing entering arc. When the end node is reached we obtain in $v_{end}$, the total penalty of the path with the smallest total penalty. We call this penalty the Viterbi penalty, and this sequence of arcs and nodes the Viterbi path. To obtain the Viterbi path with nodes $n_1 \ldots n_T$ and arcs $i_1 \ldots i_{T-1}$, we trace back these nodes and arcs as follows, starting with $n_T =$ the end node, and recursively using the minimizing entering arc: $i_t = m_{n_{t+1}}$, and $n_t = s_{i_t}$ until the start node is reached. The label sequence can then be read off the arcs of the Viterbi path.
