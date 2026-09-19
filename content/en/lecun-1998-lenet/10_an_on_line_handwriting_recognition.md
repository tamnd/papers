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
section: IX
section_title: AN ON-LINE HANDWRITING RECOGNITION SYSTEM
tag: 08C3
kind: section
lang: en
source: https://doi.org/10.1109/5.726791
pdf_sha256: 346d2a5b49eb759da050572c187b93e35b68bd6a3b9c5d68c88e6ed96da386b7
pdf_pages: 36-39
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 6a912949a4c78ecadf16fdf61002cd7706c3c9dfa351cfdfb4eafe35d14b8274
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Natural handwriting is often a mixture of different “styles,” i.e., lower case printed, upper case, and cursive. A reliable recognizer for such handwriting would greatly improve interaction with pen-based devices, but its implementation presents new technical challenges. Characters taken in isolation can be very ambiguous, but considerable information is available from the context of the whole word. We have built a word recognition system for pen-based devices based on four main modules: 1) a preprocessor that normalizes a word, or word group, by fitting a geometrical model to the word structure; 2) a module that produces an “annotated image” from the normalized pen trajectory; 3) a replicated convolutional NN that spots and recognizes characters; and 4) a GTN that interprets the networks output by taking word-level constraints into account. The network and the GTN are jointly trained to minimize an error measure defined at the word level.

In this work, we have compared a system based on SDNN’s (such as described in Section VII), and a system based on HOS (such as described in Section V). Because of the sequential nature of the information in the pen trajectory (which reveals more information than the purely optical input from in image), HOS can be very efficient in proposing candidate character cuts, especially for noncursive script.

A. Preprocessing

Input normalization reduces intracharacter variability, thereby simplifying character recognition. We have used a word normalization scheme [92] based on fitting a geometrical model of the word structure. Our model has four “flexible” lines representing respectively the ascenders line, the core line, the base line, and the descenders line. The lines are fitted to local minima or maxima of the pen trajectory. The parameters of the lines are estimated with a modified version of the EM algorithm to maximize the joint probability of observed points and parameter values, using a prior on parameters that prevents the lines from collapsing on each other.

The recognition of handwritten characters from a pen trajectory on a digitizing surface is often done in the time domain [44], [110], [111]. Typically, trajectories are normalized and local geometrical or dynamical features are extracted. The recognition may then be performed using curve matching [110], or other classification techniques such as TDNN’s [44], [111]. While these representations have several advantages, their dependence on stroke ordering and individual writing styles makes them difficult to use in high accuracy, writer independent systems that integrate the segmentation with the recognition.

Since the intent of the writer is to produce a legible image, it seems natural to preserve as much of the pictorial nature of the signal as possible, while at the same time exploit the sequential information in the trajectory. For this purpose we have designed a representation scheme called AMAP [38], where pen trajectories are represented by low-resolution images in which each picture element contains information about the local properties of the trajectory. An AMAP can be viewed as an “annotated image” in which each pixel is a five-element feature vector: four features are associated to four orientations of the pen trajectory in the area around the pixel and the fifth one is associated to local curvature in the area around the pixel. A particularly useful feature of the AMAP representation is that it makes very few assumptions about the nature of the input trajectory. It does not depend on stroke ordering or writing speed, and it can be used with all types of handwriting (capital, lower case, cursive, punctuation, symbols). Unlike many other representations (such as global features), AMAP’s can be computed for complete words without requiring segmentation.

Fig. 31. An online handwriting recognition GTN based on SDNN. {#lecun-1998-lenet-fig-31 .figure tag=08C4}

B. Network Architecture

One of the best networks we found for both online and offline character recognition is a five-layer convolutional network somewhat similar to LeNet-5 (Fig. 2), but with multiple input planes and different numbers of units on the last two layers—layer one: convolution with eight kernels of size $3 \times 3$; layer two: $2 \times 2$ subsampling; layer three: convolution with 25 kernels of size $5 \times 5$; layer four: convolution with 84 kernels of size $4 \times 4$; layer five: $2 \times 1$ subsampling; classification layer: 95 RBF units (one per class in the full printable ASCII set). The distributed codes on the output are the same as for LeNet-5, except they are adaptive unlike with LeNet-5. When used in the HOS system, the input to above network consisted of an AMAP with five planes, 20 rows, and 18 columns. It was determined that this resolution was sufficient for representing handwritten characters. In the SDNN version, the number of columns was varied according to the width of the input word. Once the number of subsampling layers and the sizes of the kernels are chosen, the sizes of all the layers, including the input, are determined unambiguously. The only architectural parameters that remain to be selected are the number of feature maps in each layer and the information as to what feature map is connected to what other feature map. In our case, the subsampling rates were chosen as small as possible ($2 \times 2$) and the kernels as small as possible in the first layer ($3 \times 3$) to limit the total number of connections. Kernel sizes in the upper layers are chosen to be as small as possible while satisfying the size constraints mentioned above. Larger architectures did not necessarily perform better and required considerably more time to be trained. A very small architecture with half the input field also performed worse because of insufficient input resolution. Note that the input resolution is nonetheless much less than for OCR because the angle and curvature provide more information than would a single grey level at each pixel.

C. Network Training

Training proceeded in two phases. First, we kept the centers of the RBF’s fixed and trained the network weights so as to minimize the output distance of the RBF unit corresponding to the correct class. This is equivalent to minimizing the MSE between the previous layer and the center of the correct-class RBF. This bootstrap phase was performed on isolated characters. In the second phase, all the parameters, network weights, and RBF centers were trained globally to minimize a discriminative criterion at the word level.

With the HOS approach, the GTN was composed of four main GT’s.

1) The segmentation transformer performs the HOS and outputs the segmentation graph. An AMAP is then computed for each image attached to the arcs of this graph.
2) The character recognition transformer applies the convolutional network character recognizer to each candidate segment and outputs the recognition graph with penalties and classes on each arc.
3) The composition transformer composes the recognition graph with a grammar graph representing a language model incorporating lexical constraints.
4) The beam search transformer extracts a good interpretation from the interpretation graph. This task could have been achieved with the usual Viterbi Transformer. The beam search algorithm, however, implements pruning strategies which are appropriate for large interpretation graphs.

With the SDNN approach, the main GT’s are the following.

1) The SDNN transformer replicates the convolutional network over the a whole word image and outputs a recognition graph that is a linear graph with class penalties for every window centered at regular intervals on the input image.
2) The *character-level composition transformer* composes the recognition graph with a left-to-right HMM for each character class (as in Fig. 27).
3) The *word-level composition transformer* composes the output of the previous transformer with a language model incorporating lexical constraints and outputs the interpretation graph.
4) The *beam search transformer* extracts a good interpretation from the interpretation graph.

Fig. 32. Comparative results (character error rates) showing the improvement brought by global training on the SDNN/HMM hybrid, and on the HOS, without and with a 25461-word dictionary. {#lecun-1998-lenet-fig-32 .figure tag=08C5}

In this application, the language model simply constrains the final output graph to represent sequences of character labels from a given dictionary. Furthermore, the interpretation graph is not actually completely instantiated: the only nodes created are those that are needed by the beam search module. The interpretation graph is therefore represented procedurally rather than explicitly.

A crucial contribution of this research was the joint training of all GT modules within the network with respect to a single criterion, as explained in Sections VI and VII. We used the discriminative forward loss function on the final output graph: minimize the forward penalty of the constrained interpretation (i.e., along all the “correct” paths) while maximizing the forward penalty of the whole interpretation graph (i.e., along all the paths).

During global training, the loss function was optimized with the stochastic diagonal Levenberg–Marquardt procedure described in Appendix C, which uses second derivatives to compute optimal learning rates. This optimization operates on all the parameters in the system, most notably the network weights and the RBF centers.

*D. Experimental Results*

In the first set of experiments, we evaluated the generalization ability of the NN classifier coupled with the word normalization preprocessing and AMAP input representation. All results are in writer independent mode (different writers in training and testing). Initial training on isolated characters was performed on a database of approximately 100 000 hand printed characters (95 classes of upper case, lower case, digits, and punctuation). Tests on a database of isolated characters were performed separately on the four types of characters: upper case (2.99% error on 9122 patterns), lower case (4.15% error on 8201 patterns), digits (1.4% error on 2938 patterns), and punctuation (4.3% error on 881 patterns). Experiments were performed with the network architecture described above. To enhance the robustness of the recognizer to variations in position, size, orientation, and other distortions, additional training data was generated by applying local affine transformations to the original characters.

The second and third set of experiments concerned the recognition of lower case words (writer independent). The tests were performed on a database of 881 words. First we evaluated the improvements brought by the word normalization to the system. For the SDNN/HMM system we have to use word-level normalization since the network sees one whole word at a time. With the HOS system, and before doing any word-level training, we obtained with character-level normalization 7.3% and 3.5% word and character errors (adding insertions, deletions and substitutions) when the search was constrained within a 25 461-word dictionary. When using the word normalization preprocessing instead of a character level normalization, error rates dropped to 4.6% and 2.0% for word and character errors respectively, i.e., a relative drop of 37% and 43% in word and character error respectively. This suggests that normalizing the word in its entirety is better than first segmenting it and then normalizing and processing each of the segments.

In the third set of experiments, we measured the improvements obtained with the joint training of the NN and the postprocessor with the word-level criterion, in comparison to training based only on the errors performed at the character level. After initial training on individual characters as above, global word-level discriminative training was performed with a database of 3500 lower case words. For the SDNN/HMM system, without any dictionary constraints, the error rates dropped from 38% and 12.4% word and character error to 26% and 8.2% respectively after word-level training, i.e., a relative drop of 32% and 34%.

For the HOS system and a slightly improved architecture, without any dictionary constraints, the error rates dropped from 22.5% and 8.5% word and character error to 17% and 6.3% respectively, i.e., a relative drop of 24.4% and 25.6%. With a 25 461-word dictionary, errors dropped from 4.6% and 2.0% word and character errors to 3.2% and 1.4%, respectively, after word-level training, i.e., a relative drop of 30.4% and 30.0%. Even lower error rates can be obtained by drastically reducing the size of the dictionary to 350 words, yielding 1.6% and 0.94% word and character errors.

These results clearly demonstrate the usefulness of globally trained NN/HMM hybrids for handwriting recognition. This confirms similar results obtained earlier in speech recognition [77].
