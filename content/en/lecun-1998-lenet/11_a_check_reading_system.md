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
section: X
section_title: A CHECK READING SYSTEM
tag: 08C6
kind: section
lang: en
source: https://doi.org/10.1109/5.726791
pdf_sha256: 346d2a5b49eb759da050572c187b93e35b68bd6a3b9c5d68c88e6ed96da386b7
pdf_pages: 39-41
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 5b8502c345af03f155e42e62d95f1b508ba5448b894183ca626a3c103e804faf
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

This section describes a GTN based check reading system, intended for immediate industrial deployment. It also shows how the use of gradient based-learning and GTN’s make this deployment fast and cost-effective while yielding an accurate and reliable solution.

The verification of the amount on a check is a task that is extremely time and money consuming for banks. As a consequence, there is a very high interest in automating the process as much as possible (see, for example, [112]–[114]). Even a partial automation would result in considerable cost reductions. The threshold of economic viability for automatic check readers, as set by the bank, is when 50% of the checks are read with less than 1% error. The other 50% of the check being rejected and sent to human operators. In such a case, we describe the performance of the system as 50% correct/49% reject/1% error. The system presented here was one of the first to cross that threshold on representative mixtures of business and personal checks.

Checks contain at least two versions of the amount. The courtesy amount is written with numerals, while the legal amount is written with letters. On business checks, which are generally machine-printed, these amounts are relatively easy to read but quite difficult to find due to the lack of standard for business check layout. On the other hand, these amounts on personal checks are easy to find but much harder to read.

For simplicity (and speed requirements), our initial task is to read the courtesy amount only. This task consists of two main steps.

1) The system has to find, among all the fields (lines of text), the candidates that are the most likely to contain the courtesy amount. This is obvious for many personal checks, where the position of the amount is standardized. However, as already noted, finding the amount can be rather difficult in business checks, even for the human eye. There are many strings of digits, such as the check number, the date, or even “not to exceed” amounts, that can be confused with the actual amount. In many cases, it is very difficult to decide which candidate is the courtesy amount before performing a full recognition.

Figure.

Fig. 33. A complete check amount reader implemented as a single cascade of GT modules. Successive graph transformations progressively extract higher level information. {#lecun-1998-lenet-fig-33 .figure tag=08C7}

2) In order to read (and choose) some courtesy amount candidates, the system has to segment the fields into characters, read and score the candidate characters, and finally find the best interpretation of the amount using contextual knowledge represented by a stochastic grammar for check amounts.

The GTN methodology was used to build a check amount reading system that handles both personal checks and business checks.

A. A GTN for Check Amount Recognition

We now describe the successive graph transformations that allow this network to read the check amount (cf. Fig. 33). Each GT produces a graph whose paths encode and score the current hypotheses considered at this stage of the system.

The input to the system is a trivial graph with a single arc that carries the image of the whole check (cf. Fig. 33).

1) The Field Location Transformer: $T_{field}$ first performs classical image analysis (including connected component analysis, ink density histograms, layout analysis, etc.) and heuristically extracts rectangular zones that may contain the check amount. $T_{field}$ produces an output graph, called the field graph (cf. Fig. 33) such that each candidate zone is associated with one arc that links the start node to the end node. Each arc contains the image of the zone and a penalty term computed from simple features extracted from the zone (absolute position, size, aspect ratio, etc.). The penalty term is close to zero if the features suggest that the field is a likely candidate and is large if the field is deemed less likely to be an amount. The penalty function is differentiable, therefore its parameters are globally tunable.

An arc may represent separate dollar and cent amounts as a sequence of fields. In fact, in handwritten checks, the cent amount may be written over a fractional bar and not aligned at all with the dollar amount. In the worst case, one may find several cent amount candidates (above and below the fraction bar) for the same dollar amount.

2) *The Segmentation Transformer*: $T_{seg}$, similar to the one described in Section VIII, examines each zone contained in the field graph and cuts each image into pieces of ink using heuristic image processing techniques. Each piece of ink may be a whole character or a piece of character. Each arc in the field graph is replaced by its corresponding segmentation graph that represents all possible groupings of pieces of ink. Each field segmentation graph is appended to an arc that contains the penalty of the field in the field graph. Each arc carries the segment image, together with a penalty that provides a first evaluation of the likelihood that the segment actually contains a character. This penalty is obtained with a differentiable function that combines a few simple features such as the space between the pieces of ink or the compliance of the segment image with a global baseline, and a few tunable parameters. The segmentation graph represents all the possible segmentations of all the field images. We can compute the penalty for one segmented field by adding the arc penalties along the corresponding path. As before, using a differentiable function for computing the penalties will ensure that the parameters can be optimized globally.

The segmenter uses a variety of heuristics to find candidate cut. One of the most important ones is called “hit and deflect” [115]. The idea is to cast lines downward from the top of the field image. When a line hits a black pixel, it is deflected so as to follow the contour of the object. When a line hits a local minimum of the upper profile, i.e., when it cannot continue downward without crossing a black pixel, it is just propagated vertically downward through the ink. When two such lines meet each other, they are merged into a single cut. The procedure can be repeated from the bottom up. This strategy allows the separation of touching characters such as double zeros.

3) *The Recognition Transformer*: $T_{rec}$ iterates over all segment arcs in the segmentation graph and runs a character recognizer on the corresponding segment image. In our case, the recognizer is LeNet-5, the convolutional NN described in Section II, whose weights constitute the largest and most important subset of tunable parameters. The recognizer classifies segment images into one of 95 classes (fully printable ASCII set) plus a rubbish class for unknown symbols or badly formed characters. Each arc in the input graph $T_{rec}$ is replaced by 96 arcs in the output graph. Each of those 96 arcs contains the label of one of the classes, and a penalty that is the sum of the penalty of the corresponding arc in the input (segmentation) graph, and the penalty associated with classifying the image in the corresponding class, as computed by the recognizer. In other words, the recognition graph represents a weighted trellis of scored character classes. Each path in this graph represents a possible character string for the corresponding field. We can compute a penalty for this interpretation by adding the penalties along the path. This sequence of characters may or may not be a valid check amount.

4) *The Composition Transformer*: $T_{gram}$ selects the paths of the recognition graph that represent valid character sequences for check amounts. This transformer takes two graphs as input: the recognition graph and the grammar graph. The grammar graph contains all possible sequences of symbols that constitute a well-formed amount. The output of the composition transformer, called the interpretation graph, contains all the paths in the recognition graph that are compatible with the grammar. The operation that combines the two input graphs to produce the output is a generalized transduction (see Section IX). A differentiable function is used to compute the data attached to the output arc from the data attached to the input arcs. In our case, the output arc receives the class label of the two arcs and a penalty computed by simply summing the penalties of the two input arcs (the recognizer penalty and the arc penalty in the grammar graph). Each path in the interpretation graph represents one interpretation of one segmentation of one field on the check. The sum of the penalties along the path represents the “badness” of the corresponding interpretation and combines evidence from each of the modules along the process, as well as from the grammar.

5) *The Viterbi Transformer*: The Viterbi transformer finally selects the path with the lowest accumulated penalty corresponding to the best grammatically correct interpretations.

*B. Gradient-Based Learning*

Each stage of this check reading system contains tunable parameters. While some of these parameters could be manually adjusted (e.g., the parameters of the field locator and segmenter), the vast majority of them must be learned, particularly the weights of the NN recognizer.

Prior to globally optimizing the system, each module parameters are initialized with reasonable values. The parameters of the field locator and the segmenter are initialized by hand, while the parameters of the NN character recognizer are initialized by training on a database of presegmented and labeled characters. Then, the entire system is trained globally from whole check images labeled with the correct amount. No explicit segmentation of the amounts is needed to train the system: it is trained at the check level.

The loss function $E$ minimized by our global training procedure is the discriminative forward criterion described in Section VI: the difference between 1) the forward penalty of the constrained interpretation graph (constrained by the correct label sequence) and 2) the forward penalty of the unconstrained interpretation graph. Derivatives can be back propagated through the entire structure, although it is only practical to do it down to the segmenter.

*C. Rejecting Low Confidence Checks*

In order to be able to reject checks which are the most likely to carry erroneous Viterbi answers, we must rate them with a confidence and reject the check if this confidence is below a given threshold. To compare the unnormalized Viterbi penalties of two different checks would be meaningless when it comes to decide which answer we trust the most.

Fig. 34. Additional processing required to compute the confidence. {#lecun-1998-lenet-fig-34 .figure tag=08C8}

The optimal measure of confidence is the probability of the Viterbi answer given the input image. As seen in Section VI-E, given a target sequence (which, in this case, would be the Viterbi answer), the discriminative forward loss function is an estimate of the logarithm of this probability. Therefore, a simple solution to obtain a good estimate of the confidence is to reuse the interpretation graph (see Fig. 33) to compute the discriminative forward loss as described in Fig. 21, using as our desired sequence the Viterbi answer. This is summarized in Fig. 34, with

$$
\text{confidence} = \exp(E_{dforw}).
$$

D. Results

A version of the above system was fully implemented and tested on machine-print business checks. This system is basically a generic GTN engine with task specific heuristics encapsulated in the check and fprop method. As a consequence, the amount of code to write was minimal: mostly the adaptation of an earlier segmenter into the segmentation transformer. The system that deals with handwritten or personal checks was based on earlier implementations that used the GTN concept in a restricted way.

The NN classifier was initially trained on 500 000 images of character images from various origins spanning the entire printable ASCII set. This contained both handwritten and machine-printed characters that had been previously size normalized at the string level. Additional images were generated by randomly distorting the original images using simple affine transformations of the images. The network was then further trained on character images that had been automatically segmented from check images and manually truthed. The network was also initially trained to reject noncharacters that resulted from segmentation errors. The recognizer was then inserted in the check-reading system and a small subset of the parameters were trained globally (at the field level) on whole check images.

On 646 business checks that were automatically categorized as machine printed, the performance was 82% correctly recognized checks, 1% errors, and 17% rejects. This can be compared to the performance of the previous system on the same test set: 68% correct, 1% errors, and 31% rejects. A check is categorized as machine-printed when characters that are near a standard position dollar sign are detected as machine printed, or when, if nothing is found in the standard position, at least one courtesy amount candidate is found somewhere else. The improvement is attributed to three main causes. First the NN recognizer was bigger and trained on more data. Second, because of the GTN architecture, the new system could take advantage of grammatical constraints in a much more efficient way than the previous system. Third, the GTN architecture provided extreme flexibility for testing heuristics, adjusting parameters, and tuning the system. This last point is more important than it seems. The GTN framework separates the “algorithmic” part of the system from the “knowledge-based” part of the system, allowing easy adjustments of the latter. The importance of global training was only minor in this task because the global training only concerned a small subset of the parameters.

An independent test performed by systems integrators in 1995 showed the superiority of this system over other commercial courtesy amount reading systems. The system was integrated in NCR’s line of check reading systems. It has been fielded in several banks across the United States since June 1996, and it has been reading millions of checks per day since then.
