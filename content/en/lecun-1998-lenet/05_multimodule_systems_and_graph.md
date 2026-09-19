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
section: IV
section_title: MULTIMODULE SYSTEMS AND GRAPH TRANSFORMER NETWORKS
tag: 08B1
kind: section
lang: en
source: https://doi.org/10.1109/5.726791
pdf_sha256: 346d2a5b49eb759da050572c187b93e35b68bd6a3b9c5d68c88e6ed96da386b7
pdf_pages: 18-21
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 883f00fcdd9001863443126b08c6756752fa9db55097aa296921fd37382a0a7f
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The classical back-propagation algorithm, as described and used in the previous sections, is a simple form of gradient-based learning. However, it is clear that the gradient back-propagation algorithm given by (4) describes a more general situation than simple multilayer feedforward networks composed of alternated linear transformations and sigmoidal functions. In principle, derivatives can be back-propagated through any arrangement of functional modules, as long as we can compute the product of the Jacobians of those modules by any vector. Why would we want to train systems composed of multiple heterogeneous modules? The answer is that large and complex trainable systems need to be built out of simple, specialized modules. The simplest example is LeNet-5, which mixes convolutional layers, subsampling layers, fully connected layers, and RBF layers. Another less trivial example, described in Sections IV-A and IV-B, is a system for recognizing words, that can be trained to simultaneously segment and recognize words without ever being given the correct segmentation.

Fig. 14 shows an example of a trainable multimodular system. A multimodule system is defined by the function implemented by each of the modules and by the graph of interconnection of the modules to each other. The graph implicitly defines a partial order according to which the modules must be updated in the forward pass. For example in Fig. 14, module 0 is first updated, then modules 1 and 2 are updated (possibly in parallel), followed by module 3. Modules may or may not have trainable parameters. Loss functions, which measure the performance of the system, are implemented as module 4. In the simplest case, the loss function module receives an external input that carries the desired output. In this framework, there is no qualitative difference between trainable parameters (W1,

Fig. 13. Examples of unusual, distorted, and noisy characters correctly recognized by LeNet-5. {#lecun-1998-lenet-fig-13 .figure tag=08B2}
The grey level of the output label represents the penalty (lighter for higher penalties).

Complex modules can be constructed from simpler modules by simply defining a new class whose slots will contain the member modules and the intermediate state variables between those modules. The fprop method for the class simply calls the fprop methods of the member modules, with the appropriate intermediate state variables or external input and outputs as arguments. Although the algorithms are easily generalizable to any network of such modules, including those whose influence graph has cycles, we will limit the discussion to the case of directed acyclic graphs (feed-forward networks).
Computing derivatives in a multimodule system is just as simple. A “backward propagation” method, called bprop, for each module class can be defined for that purpose. The bprop method of a module takes the same arguments as the fprop method. All the derivatives in the system can be computed by calling the bprop method on all the modules in reverse order compared to the forward propagation phase. The state variables are assumed to contain slots for storing the gradients computed during the backward pass, in addition to storage for the states computed in the forward pass. The backward pass effectively computes the partial derivatives of the loss $E$ with respect to all the state variables and all the parameters in the system. There is an interesting duality property between the forward and backward functions of certain modules. For example, a sum of several variables in the forward direction is transformed into a simple fan-out (replication) in the backward w2 in the figure), external inputs and outputs ($Z, D, E$), and intermediate state variables ($X1, X2, X3, X4, X5$).

Fig. 14. A trainable system composed of heterogeneous modules. {#lecun-1998-lenet-fig-14 .figure tag=08B3}

A. An Object-Oriented Approach

Object-oriented programming offers a particularly convenient way of implementing multimodule systems. Each module is an instance of a class. Module classes have a “forward propagation” method (or member function) called fprop whose arguments are the inputs and outputs of the module. For example, computing the output of module 3 in Fig. 14 can be done by calling the method fprop on module 3 with the arguments X3, X4, X5.

direction. Conversely, a fan-out in the forward direction is transformed into a sum in the backward direction. The software environment used to obtain the results described in this paper, called SN3.1, uses the above concepts. It is based on a home-grown object-oriented dialect of Lisp with a compiler to C.

The fact that derivatives can be computed by propagation in the reverse graph is easy to understand intuitively. The best way to justify it theoretically is through the use of Lagrange functions [21], [22]. The same formalism can be used to extend the procedures to networks with recurrent connections.

B. Special Modules

NN’s and many other standard pattern recognition techniques can be formulated in terms of multimodular systems trained with gradient-based learning. Commonly used modules include matrix multiplications and sigmoidal modules, the combination of which can be used to build conventional NN’s. Other modules include convolutional layers, subsampling layers, RBF layers, and “softmax” layers [65]. Loss functions are also represented as modules whose single output produces the value of the loss. Commonly used modules have simple bprop methods. In general, the bprop method of a function $F$ is a multiplication by the Jacobian of $F$. Here are a few commonly used examples. The bprop method of a fanout (a “Y” connection) is a sum, and vice versa. The bprop method of a multiplication by a coefficient is a multiplication by the same coefficient. The bprop method of a multiplication by a matrix is a multiplication by the transpose of that matrix. The bprop method of an addition with a constant is the identity.

Interestingly, certain nondifferentiable modules can be inserted in a multinode system without adverse effect. An interesting example of that is the multiplexer module. It has two (or more) regular inputs, one switching input, and one output. The module selects one of its inputs, depending upon the (discrete) value of the switching input, and copies it on its output. While this module is not differentiable with respect to the switching input, it is differentiable with respect to the regular inputs. Therefore the overall function of a system that includes such modules will be differentiable with respect to its parameters as long as the switching input does not depend upon the parameters. For example, the switching input can be an external input.

Another interesting case is the min module. This module has two (or more) inputs and one output. The output of the module is the minimum of the inputs. The function of this module is differentiable everywhere, except on the switching surface which is a set of measure zero. Interestingly, this function is continuous and reasonably regular, and that is sufficient to ensure the convergence of a gradient-based learning algorithm.

The object-oriented implementation of the multinode idea can easily be extended to include a bbprop method that propagates Gauss–Newton approximations of the second derivatives. This leads to a direct generalization for modular systems of the second-derivative back propagation (22) given in Appendix C.

The multiplexer module is a special case of a much more general situation, described at length in Section IX, where the architecture of the system changes dynamically with the input data. Multiplexer modules can be used to dynamically rewire (or reconfigure) the architecture of the system for each new input pattern.

C. GTN’s

Multimodule systems are very flexible tools for building a large trainable system. However, the descriptions in the previous sections implicitly assumed that the set of parameters, and the state information communicated between the modules, are all fixed-size vectors. The limited flexibility of fixed-size vectors for data representation is a serious deficiency for many applications, notably for tasks that deal with variable length inputs (e.g., continuous speech recognition and handwritten word recognition) or for tasks that require encoding relationships between objects or features whose number and nature can vary (invariant perception, scene analysis, recognition of composite objects). An important special case is the recognition of strings of characters or words.

More generally, fixed-size vectors lack flexibility for tasks in which the state must encode probability distributions over sequences of vectors or symbols, as is the case in linguistic processing. Such distributions over sequences are best represented by stochastic grammars, or, in the more general case, directed graphs in which each arc contains a vector (stochastic grammars are special cases in which the vector contains probabilities and symbolic information). Each path in the graph represents a different sequence of vectors. Distributions over sequences can be represented by interpreting elements of the data associated with each arc as parameters of a probability distribution or simply as a penalty. Distributions over sequences are particularly handy for modeling linguistic knowledge in speech or handwriting recognition systems: each sequence, i.e., each path in the graph, represents an alternative interpretation of the input. Successive processing modules progressively refine the interpretation. For example, a speech recognition system might start with a single sequence of acoustic vectors, transform it into a lattice of phonemes (distribution over phoneme sequences), then into a lattice of words (distribution over word sequences), and then into a single sequence of words representing the best interpretation.

In our work on building large-scale handwriting recognition systems, we have found that these systems could be developed and designed much more easily and quickly by viewing the system as a networks of modules that take one or several graphs as input and produce graphs as output. Such modules are called GT’s, and the complete systems are called GTN’s. Modules in a GTN communicate their states and gradients in the form of directed graphs whose arcs carry numerical information (scalars or vectors) [66].

From the statistical point of view, the fixed-size state vectors of conventional networks can be seen as representing the means of distributions in state space. In variable-size networks such as the space-displacement NN’s described in Section VII, the states are variable-length sequences of fixed size vectors. They can be seen as representing the mean of a probability distribution over variable-length sequences of fixed-size vectors. In GTN’s the states are represented as graphs, which can be seen as representing mixtures of probability distributions over structured collections (possibly sequences) of vectors (Fig. 15).

Fig. 15. Traditional NN’s and multimodule systems communicate fixed-size vectors between layers. Multilayer GTN’s are composed of trainable modules that operate on and produce graphs whose arcs carry numerical information. {#lecun-1998-lenet-fig-15 .figure tag=08B4}

One of the main points of the next several sections is to show that gradient-based learning procedures are not limited to networks of simple modules that communicate through fixed-size vectors but can be generalized to GTN’s. Gradient back propagation through a GT takes gradients with respect to the numerical information in the output graph and computes gradients with respect to the numerical information attached to the input graphs, and with respect to the module’s internal parameters. Gradient-based learning can be applied as long as differentiable functions are used to produce the numerical data in the output graph from the numerical data in the input graph and the functions parameters.

The second point of the next several sections is to show that the functions implemented by many of the modules used in typical document processing systems (and other image recognition systems), though commonly thought to be combinatorial in nature, are indeed differentiable with respect to their internal parameters as well as with respect to their inputs, and are therefore usable as part of a globally trainable system.

In most of the following, we will purposely avoid making references to probability theory. All the quantities manipulated are viewed as penalties, or costs, which if necessary can be transformed into probabilities by taking exponentials and normalizing.
