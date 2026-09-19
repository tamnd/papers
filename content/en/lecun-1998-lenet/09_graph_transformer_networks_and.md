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
section: VIII
section_title: Graph Transformer Networks and Transducers
tag: 08C0
kind: section
lang: en
source: https://doi.org/10.1109/5.726791
pdf_sha256: 346d2a5b49eb759da050572c187b93e35b68bd6a3b9c5d68c88e6ed96da386b7
pdf_pages: 32-36
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 05dd5b744726c34754f011ac78d0d16257d54267d054a1126cb6ba107a0a76f3
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

In Section IV, GTN’s were introduced as a generalization of multilayer, multimodule networks where the state information is represented as graphs instead of fixed-size vectors. This section reinterprets the GTN’s in the framework of generalized transduction and proposes a powerful graph composition algorithm.

A. Previous Work

Numerous authors in speech recognition have used gradient-based learning methods that integrate graph-based statistical models (notably HMM’s) with acoustic recognition modules, mainly Gaussian mixture models, but also NN’s [67], [78], [98], [99]. Similar ideas have been applied to handwriting recognition (see [38] for a review). However, there has been no proposal for a systematic approach to multilayer graph-based trainable systems. The idea of transforming graphs into other graphs has received considerable attention in computer science through the concept of weighted finite-state transducers [86]. Transducers have been applied to speech recognition [100] and language translation [101], and proposals have been made for handwriting recognition [102]. This line of work has been mainly focused on efficient search algorithms [103] and on the algebraic aspects of combining transducers and graphs (called acceptors in this context), but very little effort has been devoted to building globally trainable systems out of transducers. What is proposed in the following sections is a systematic approach to automatic training in graph-manipulating systems. A different approach to graph-based trainable systems, called input–output HMM, was proposed in [104] and [105].

B. Standard Transduction

In the established framework of finite-state transducers [86], discrete symbols are attached to arcs in the graphs. Acceptor graphs have a single symbol attached to each arc whereas transducer graphs have two symbols (an input symbol and an output symbol). A special null symbol is absorbed by any other symbol (when concatenating symbols to build a symbol sequence). Weighted transducers and acceptors also have a scalar quantity attached to each arc. In this framework, the composition operation takes as input an acceptor graph and a transducer graph and builds an output acceptor graph. Each path in this output graph (with symbol sequence $S_{out}$) corresponds to one path (with symbol sequence $S_{in}$) in the input acceptor graph and one path and a corresponding pair of input–output sequences ($S_{out}, S_{in}$) in the transducer graph. The weights on the arcs of the output graph are obtained by adding the weights from the matching arcs in the input acceptor and transducer graphs. In the rest of the paper, we will call this graph composition operation using transducers the (standard) transduction operation.

A simple example of transduction is shown in Fig. 28. In this simple example, the input and output symbols on the transducer arcs are always identical. This type of transducer graph is called a grammar graph. To better understand the transduction operation, imagine two tokens sitting each on the start nodes of the input acceptor graph and the transducer graph. The tokens can freely follow any arc labeled with a null input symbol. A token can follow an arc labeled with a nonnull input symbol if the other token also follows an arc labeled with the same input symbol. We have an acceptable trajectory when both tokens reach the end nodes of their graphs (i.e., the tokens have reached the terminal configuration). This trajectory represents a sequence of input symbols that complies with both the acceptor and the transducer. We can then collect the corresponding sequence of output symbols along the trajectory of the transducer token. The above procedure produces a tree, but a simple technique described in Section VIII-C can be used to avoid generating multiple copies of certain subgraphs by detecting when a particular output state has already been seen.

The transduction operation can be performed very efficiently [106], but presents complex bookkeeping problems concerning the handling of all combinations of null and nonnull symbols. If the weights are interpreted as probabilities (normalized appropriately) then an acceptor graph represents a probability distribution over the language defined by the set of label sequences associated to all possible paths (from the start to the end node) in the graph.

An example of application of the transduction operation is the incorporation of linguistic constraints (a lexicon or a grammar) when recognizing words or other character strings. The recognition transformer produces the recognition graph (an acceptor graph) by applying the NN recognizer to each candidate segment. This acceptor graph is composed with a transducer graph for the grammar. The grammar transducer contains a path for each legal sequence of symbol, possibly augmented with penalties to indicate the relative likelihoods of the possible sequences. The arcs contain identical input and output symbols. Another example of transduction was mentioned in Section V: the path selector used in the HOS training GTN is implementable by a composition. The transducer graph is linear graph which contains the correct label sequence. The composition of the interpretation graph with this linear graph yields the constrained graph.

Fig. 28. Example of composition of the recognition graph with the grammar graph in order to build an interpretation that is consistent with both of them. During the forward propagation (dark arrows), the methods check and fprop are used. Gradients (dashed arrows) are back propagated with the adaptation of the method group. {#lecun-1998-lenet-fig-28 .figure tag=08C1}

C. Generalized Transduction

If the data structures associated to each arc took only a finite number of values, composing the input graph and an appropriate transducer would be a sound solution. For our applications however, the data structures attached to the arcs of the graphs may be vectors, images or other high-dimensional objects that are not readily enumerated. We present a new composition operation that solves this problem.

Instead of only handling graphs with discrete symbols and penalties on the arcs, we are interested in considering graphs whose arcs may carry complex data structures, including continuous-valued data structures such as vectors and images. Composing such graphs requires additional information.

1) When examining a pair of arcs (one from each input graph), we need a criterion to decide whether to create corresponding arc(s) and node(s) in the output graph, based on the information attached to the input arcs. We can decide to build an arc, several arcs, or an entire subgraph with several nodes and arcs.
2) When that criterion is met, we must build the corresponding arc(s) and node(s) in the output graph and compute the information attached to the newly created arc(s) as a function that the information attached to the input arcs.

These functions are encapsulated in an object called a composition transformer. An instance of composition transformer implements the following three methods:

1) check (arc1, arc2) compares the data structures pointed to by arcs arc1 (from the first graph) and arc2 (from the second graph) and returns a boolean indicating whether corresponding arc(s) should be created in the output graph;
2) fprop (ngraph, upnode, downnode, arc1, arc2) is called when check (arc1, arc2) returns true; this method creates new arcs and nodes between nodes upnode and downnode in the output graph ngraph, and computes the information attached to these newly created arcs as a function of the attached information of the input arcs arc1 and arc2;
3) bprop (ngraph, upnode, downnode, arc1, arc2) is called during training in order to propagate gradient information from the output subgraph between upnode and downnode into the data structures on the arc1 and arc2, as well as with respect to the parameters that were used in the fprop call with the same arguments; this method assumes that the function used by fprop to compute the values attached to its output arcs is differentiable.

The check method can be seen as constructing a dynamic architecture of functional dependencies, while the fprop method performs a forward propagation through that architecture to compute the numerical information attached to the arcs. The bprop method performs a backward propagation through the same architecture to compute the partial derivatives of the loss function with respect to the information attached to the arcs. This is illustrated in Fig. 28.

Fig. 29 shows a simplified generalized graph composition algorithm. This simplified algorithm does not handle null transitions, and it does not check whether the tokens

Function generalized_composition(PGRAPH graph1,
                                 PGRAPH graph2,
                                 PTRANS trans)
{
    // Create new graph
    PGRAPH ngraph = new_graph()

// Create map between token positions
    // and nodes of the new graph
    PNODE map[PNODE,PNODE] = new_empty_map()
    map[endnode(graph1), endnode(graph2)] =
        endnode(newgraph)

// Recursive subroutine for simulating tokens
    Function simtokens(PNODE node1, PNODE node2)
    Returns PNODE
    {
        PNODE currentnode = map[node1, node2]
        // Check if already visited
        If (currentnode == nil)
            // Record new configuration
            currentnode = ngraph->create_node()
            map[node1, node2] = currentnode
            // Enumerate the possible non-null
            // joint token transitions
            For ARC arc1 in down_arcs(node1)
                For ARC arc2 in down_arcs(node2)
                    If (trans->check(arc1, arc2))
                        PNODE newnode =
                            simtokens(down_node(arc1),
                                      down_node(arc2))
                        trans->fprop(ngraph, currentnode,
                                    newnode, arc1, arc2)
        // Return node in composed graph
        Return currentnode
    }

// Perform token simulation
    simtokens(startnode(graph1), startnode(graph2))
    Delete map
    Return ngraph
} trajectory is acceptable (i.e., both tokens simultaneously reach the end nodes of their graphs). The management of null transitions is a straightforward modification of the token simulation function. Before enumerating the possible nonnull joint token transitions, we loop on the possible null transitions of each token, recursively call the token simulation function, and finally call the method fprop. The safest way for identifying acceptable trajectories consists of running a preliminary pass for identifying the token configurations from which we can reach the terminal configuration (i.e., both tokens on the end nodes). This is easily achieved by enumerating the trajectories in the opposite direction. We start on the end nodes and follow the arcs upstream. During the main pass, we only build the nodes that allow the tokens to reach the terminal configuration.

Fig. 29. Pseudocode for a simplified generalized composition algorithm. For simplifying the presentation, we do not handle null transitions nor implement dead end avoidance. The two main components of the composition appear clearly here: 1) the recursive function simtoken() enumerating the token trajectories and 2) the associative array map used for remembering which nodes of the composed graph have been visited. {#lecun-1998-lenet-fig-29 .figure tag=08C2}

Graph composition using transducers (i.e., standard transduction) is easily and efficiently implemented as a generalized transduction. The method check simply tests the equality of the input symbols on the two arcs, and the method fprop creates a single arc whose symbol is the output symbol on the transducer’s arc.

The composition between pairs of graphs is particularly useful for incorporating linguistic constraints in a handwriting recognizer. Examples of its use are given in the online handwriting recognition system described in Section IX (and in the check reading system described in Section X).

In the rest of the paper, the term composition transformer will denote a GT based on the generalized transductions of multiple graphs. The concept of generalized transduction is a very general one. In fact, many of the GT’s described earlier in this paper, such as the segmenter and the recognizer, can be formulated in terms of generalized transduction. In this case, the generalized transduction does not take two input graphs but a single input graph. The method fprop of the transformer may create several arcs or even a complete subgraph for each arc of the initial graph. In fact the pair check, fprop itself can be seen as procedurally defining a transducer.

In addition, it can be shown that the generalized transduction of a single graph is theoretically equivalent to the standard composition of this graph with a particular transducer graph. However, implementing the operation this way may be very inefficient since the transducer can be very complicated.

In practice, the graph produced by a generalized transduction is represented procedurally in order to avoid building the whole output graph (which may be huge when for example the interpretation graph is composed with the grammar graph). We only instantiate the nodes which are visited by the search algorithm during recognition (e.g., Viterbi). This strategy propagates the benefits of pruning algorithms (e.g., beam search) in all the GTN’s.

D. Notes on the Graph Structures

Section VI discussed the idea of global training by back-propagating gradient through simple GT’s. The bprop method is the basis of the back-propagation algorithm for generic GT’s. A generalized composition transformer can be seen as dynamically establishing functional relationships between the numerical quantities on the input and output arcs. Once the check function has decided that a relationship should be established, the fprop function implements the numerical relationship. The check function establishes the structure of the ephemeral network inside the composition transformer.

Since fprop is assumed to be differentiable, gradients can be back propagated through that structure. Most parameters affect the scores stored on the arcs of the successive graphs of the system. A few threshold parameters may determine whether an arc appears or not in the graph. Since nonexisting arcs are equivalent to arcs with very large penalties, we only consider the case of parameters affecting the penalties.

In the kind of systems we have discussed until now (and the application described in Section X), much of the knowledge about the structure of the graph that is produced by a GT is determined by the nature of the GT, but it may also depend on the value of the parameters and on the input. It may also be interesting to consider GT modules which attempt to learn the structure of the output graph. This might be considered a combinatorial problem and not amenable to gradient-based learning, but a solution to this problem is to generate a large graph that contains the graph candidates as subgraphs, and then select the appropriate subgraph.

E. GTN and HMM’s

GTN’s can be seen as a generalization and an extension of HMM’s. On the one hand, the probabilistic interpretation can be either kept (with penalties being log-probabilities), pushed to the final decision stage (with the difference of the constrained forward penalty and the unconstrained forward penalty being interpreted as negative log-probabilities of label sequences), or dropped altogether (the network just represents a decision surface for label sequences in input space). On the other hand, GTN’s extend HMM’s by allowing to combine in a well-principled framework multiple levels of processing, or multiple models (e.g., Pereira et al. have been using the transducer framework for stacking HMM’s representing different levels of processing in automatic speech recognition [86]).

Unfolding an HMM in time yields a graph that is very similar to our interpretation graph (at the final stage of processing of the GTN, before Viterbi recognition). It has nodes $n(t, i)$ associated to each time step $t$ and state $i$ in the model. The penalty $c_i$ for an arc from $n(t-1, j)$ to $n(t, i)$ then corresponds to the negative log-probability of emitting observed data $o_t$ at position $t$ and going from state $j$ to state $i$ in the time interval $(t-1, t)$. With this probabilistic interpretation, the forward penalty is the negative logarithm of the likelihood of whole observed data sequence (given the model).

In Section VI we mentioned that the collapsing phenomenon can occur when nondiscriminative loss functions are used to train NN’s/HMM hybrid systems. With classical HMM’s with fixed preprocessing, this problem does not occur because the parameters of the emission and transition probability models are forced to satisfy certain probabilistic constraints: the sum or the integral of the probabilities of a random variable over its possible values must be one. Therefore, when the probability of certain events is increased, the probability of other events must automatically be decreased. On the other hand, if the probabilistic assumptions in an HMM (or other probabilistic model) are not realistic, discriminative training, discussed in Section VI, can improve performance as this has been clearly shown for speech recognition systems [48]–[50], [107], [108].

The input–output HMM (IOHMM) [105], [109] is strongly related to GT’s. Viewed as a probabilistic model, an IOHMM represents the conditional distribution of output sequences given input sequences (of the same or a different length). It is parameterized from an emission probability module and a transition probability module. The emission probability module computes the conditional emission probability of an output variable (given an input value and the value of discrete “state” variable). The transition probability module computes conditional transition probabilities of a change in the value of the “state” variable, given the input value. Viewed as a GT, it assigns an output graph (representing a probability distribution over the sequences of the output variable) to each path in the input graph. All these output graphs have the same structure, and the penalties on their arcs are simply added in order to obtain the complete output graph. The input values of the emission and transition modules are read off the data structure on the input arcs of the IOHMM GT. In practice, the output graph may be very large, and needs not be completely instantiated (i.e., it is pruned: only the low penalty paths are created).
