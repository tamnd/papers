---
paper: wu-2016-gnmt
title: 'Google''s Neural Machine Translation System: Bridging the Gap between Human and Machine Translation'
authors:
  - Yonghui Wu
  - Mike Schuster
  - Zhifeng Chen
  - Quoc V. Le
  - Mohammad Norouzi
  - Wolfgang Macherey
  - Maxim Krikun
  - Yuan Cao
  - Qin Gao
  - Klaus Macherey
  - Jeff Klingner
  - Apurva Shah
  - Melvin Johnson
  - Xiaobing Liu
  - Łukasz Kaiser
  - Stephan Gouws
  - Yoshikiyo Kato
  - Taku Kudo
  - Hideto Kazawa
  - Keith Stevens
  - George Kurian
  - Nishant Patil
  - Wei Wang
  - Cliff Young
  - Jason Smith
  - Jason Riesa
  - Alex Rudnick
  - Oriol Vinyals
  - Greg Corrado
  - Macduff Hughes
  - Jeffrey Dean
year: 2016
venue: arXiv
field: ai-ml
section: "3"
section_title: Model Architecture
tag: 08DD
kind: section
lang: en
source: arxiv:1609.08144
pdf_sha256: 285fb4323972464ba0be4f7c76a0db1a3cc196d5e44be542152f085d47fe5812
pdf_pages: 3-7
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: f59c3eb6ec442357ab97f9ee2f682b2f041ba42f0988111baeb1791b3a82f298
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Our model (see Figure 1) follows the common sequence-to-sequence learning framework [[sutskever-2014-seq2seq]] with attention [2]. It has three components: an encoder network, a decoder network, and an attention network. The encoder transforms a source sentence into a list of vectors, one vector per input symbol. Given this list of vectors, the decoder produces one symbol at a time, until the special end-of-sentence symbol (EOS) is produced. The encoder and decoder are connected through an attention module which allows the decoder to focus on different regions of the source sentence during the course of decoding.

For notation, we use bold lower case to denote vectors (e.g., v, o_i), bold upper case to represent matrices (e.g., U, W), cursive upper case to represent sets (e.g., V, T), capital letters to represent sequences (e.g. X, Y), and lower case to represent individual symbols in a sequence, (e.g., x_1, x_2).

Let (X, Y) be a source and target sentence pair. Let X = x_1, x_2, x_3, ..., x_M be the sequence of M symbols in the source sentence and let Y = y_1, y_2, y_3, ..., y_N be the sequence of N symbols in the target sentence. The encoder is simply a function of the following form:

$$
\mathbf{x}_1, \mathbf{x}_2, ..., \mathbf{x}_M = EncoderRNN(x_1, x_2, x_3, ..., x_M)
$$

In this equation, $\mathbf{x}_1, \mathbf{x}_2, ..., \mathbf{x}_M$ is a list of fixed size vectors. The number of members in the list is the same as the number of symbols in the source sentence (M in this example). Using the chain rule the conditional probability of the sequence $P(Y|X)$ can be decomposed as:

$$
P(Y|X) = P(Y|\mathbf{x}_1, \mathbf{x}_2, \mathbf{x}_3, ..., \mathbf{x}_M)
$$

$$
= \prod_{i=1}^N P(y_i|y_0, y_1, y_2, ..., y_{i-1}; \mathbf{x}_1, \mathbf{x}_2, \mathbf{x}_3, ..., \mathbf{x}_M)
$$

where $y_0$ is a special “beginning of sentence” symbol that is prepended to every target sentence.

During inference we calculate the probability of the next symbol given the source sentence encoding and the decoded target sequence so far:

$$
P(y_i|y_0, y_1, y_2, y_3, ..., y_{i-1}; \mathbf{x}_1, \mathbf{x}_2, \mathbf{x}_3, ..., \mathbf{x}_M)
$$

Our decoder is implemented as a combination of an RNN network and a softmax layer. The decoder RNN network produces a hidden state $\mathbf{y}_i$ for the next symbol to be predicted, which then goes through the softmax layer to generate a probability distribution over candidate output symbols.

In our experiments we found that for NMT systems to achieve good accuracy, both the encoder and decoder RNNs have to be deep enough to capture subtle irregularities in the source and target languages. This observation is similar to previous observations that deep LSTMs significantly outperform shallow LSTMs [[sutskever-2014-seq2seq]]. In that work, each additional layer reduced perplexity by nearly 10%. Similar to [31], we use a deep stacked Long Short Term Memory (LSTM) [23] network for both the encoder RNN and the decoder RNN.

Our attention module is similar to [2]. More specifically, let $\mathbf{y}_{i-1}$ be the decoder-RNN output from the past decoding time step (in our implementation, we use the output from the bottom decoder layer). Attention context $\mathbf{a}_i$ for the current time step is computed according to the following formulas:

Figure 1: The model architecture of GNMT, Google’s Neural Machine Translation system. On the left is the encoder network, on the right is the decoder network, in the middle is the attention module. The bottom encoder layer is bi-directional: the pink nodes gather information from left to right while the green nodes gather information from right to left. The other layers of the encoder are uni-directional. Residual connections start from the layer third from the bottom in the encoder and decoder. The model is partitioned into multiple GPUs to speed up training. In our setup, we have 8 encoder LSTM layers (1 bi-directional layer and 7 uni-directional layers), and 8 decoder layers. With this setting, one model replica is partitioned 8-ways and is placed on 8 different GPUs typically belonging to one host machine. During training, the bottom bi-directional encoder layers compute in parallel first. Once both finish, the uni-directional encoder layers can start computing, each on a separate GPU. To retain as much parallelism as possible during running the decoder layers, we use the bottom decoder layer output only for obtaining recurrent attention context, which is sent directly to all the remaining decoder layers. The softmax layer is also partitioned and placed on multiple GPUs. Depending on the output vocabulary size we either have them run on the same GPUs as the encoder and decoder networks, or have them run on a separate set of dedicated GPUs. {#wu-2016-gnmt-fig-1 .figure tag=08DE}

$$
s_t = AttentionFunction(\mathbf{y}_{i-1}, \mathbf{x}_t) \quad \forall t,\quad 1 \leq t \leq M
$$

$$
p_t = \exp(s_t) / \sum_{t=1}^{M} \exp(s_t) \quad \forall t,\quad 1 \leq t \leq M
$$

$$
\mathbf{a}_i = \sum_{t=1}^{M} p_t \cdot \mathbf{x}_t
$$

where $AttentionFunction$ in our implementation is a feed forward network with one hidden layer.

### 3.1 Residual Connections {#wu-2016-gnmt-s3-1 .section tag=08DF}

As mentioned above, deep stacked LSTMs often give better accuracy over shallower models. However, simply stacking more layers of LSTM works only to a certain number of layers, beyond which the network becomes too slow and difficult to train, likely due to exploding and vanishing gradient problems [33, 22]. In our experience with large-scale translation tasks, simple stacked LSTM layers work well up to 4 layers, barely with 6 layers, and very poorly beyond 8 layers.

![The difference between normal stacked LSTM and our stacked LSTM with residual connections. On the left: simple stacked LSTM layers [[sutskever-2014-seq2seq]]. On the right: our implementation of stacked LSTM layers with residual connections. With residual connections, input to the bottom LSTM layer ($\mathbf{x}_i^0$'s to LSTM$_1$) is element-wise added to the output from the bottom layer ($\mathbf{x}_i^1$'s). This sum is then fed to the top LSTM layer (LSTM$_2$) as the new input.](figures/fig2.png)

Figure 2: The difference between normal stacked LSTM and our stacked LSTM with residual connections. On the left: simple stacked LSTM layers [[sutskever-2014-seq2seq]]. On the right: our implementation of stacked LSTM layers with residual connections. With residual connections, input to the bottom LSTM layer ($\mathbf{x}_i^0$'s to LSTM$_1$) is element-wise added to the output from the bottom layer ($\mathbf{x}_i^1$'s). This sum is then fed to the top LSTM layer (LSTM$_2$) as the new input. {#wu-2016-gnmt-fig-2 .figure tag=08E0}

Motivated by the idea of modeling differences between an intermediate layer’s output and the targets, which has shown to work well for many projects in the past [16], [[he-2016-resnet]], [40], we introduce residual connections among the LSTM layers in a stack (see Figure 2). More concretely, let LSTM$_i$ and LSTM$_{i+1}$ be the $i$-th and $(i+1)$-th LSTM layers in a stack, whose parameters are $\mathbf{W}^i$ and $\mathbf{W}^{i+1}$ respectively. At the $t$-th time step, for the stacked LSTM without residual connections, we have:

$$
\begin{align*}
\mathbf{c}_t^i, \mathbf{m}_t^i &= \mathrm{LSTM}_i(\mathbf{c}_{t-1}^i, \mathbf{m}_{t-1}^i, \mathbf{x}_t^{i-1}; \mathbf{W}^i) \\
\mathbf{x}_t^i &= \mathbf{m}_t^i \\
\mathbf{c}_t^{i+1}, \mathbf{m}_t^{i+1} &= \mathrm{LSTM}_{i+1}(\mathbf{c}_{t-1}^{i+1}, \mathbf{m}_{t-1}^{i+1}, \mathbf{x}_t^i; \mathbf{W}^{i+1})
\end{align*}
$$

where $\mathbf{x}_t^i$ is the input to LSTM$_i$ at time step $t$, and $\mathbf{m}_t^i$ and $\mathbf{c}_t^i$ are the hidden states and memory states of LSTM$_i$ at time step $t$, respectively.

With residual connections between LSTM$_i$ and LSTM$_{i+1}$, the above equations become:

$$
\begin{align*}
\mathbf{c}_t^i, \mathbf{m}_t^i &= \mathrm{LSTM}_i(\mathbf{c}_{t-1}^i, \mathbf{m}_{t-1}^i, \mathbf{x}_t^{i-1}; \mathbf{W}^i) \\
\mathbf{x}_t^i &= \mathbf{m}_t^i + \mathbf{x}_t^{i-1} \\
\mathbf{c}_t^{i+1}, \mathbf{m}_t^{i+1} &= \mathrm{LSTM}_{i+1}(\mathbf{c}_{t-1}^{i+1}, \mathbf{m}_{t-1}^{i+1}, \mathbf{x}_t^i; \mathbf{W}^{i+1})
\end{align*}
$$

Residual connections greatly improve the gradient flow in the backward pass, which allows us to train very deep encoder and decoder networks. In most of our experiments, we use 8 LSTM layers for the encoder and decoder, though residual connections can allow us to train substantially deeper networks (similar to what was observed in [45]).

### 3.2 Bi-directional Encoder for First Layer {#wu-2016-gnmt-s3-2 .section tag=08E1}

For translation systems, the information required to translate certain words on the output side can appear anywhere on the source side. Often the source side information is approximately left-to-right, similar to the target side, but depending on the language pair the information for a particular output word can be distributed and even be split up in certain regions of the input side.

To have the best possible context at each point in the encoder network it makes sense to use a bi-directional RNN [36] for the encoder, which was also used in [2]. To allow for maximum possible parallelization during computation (to be discussed in more detail in section 3.3), bi-directional connections are only used for the bottom encoder layer – all other encoder layers are uni-directional. Figure 3 illustrates our use of bi-directional LSTMs at the bottom encoder layer. The layer LSTM_f processes the source sentence from left to right, while the layer LSTM_b processes the source sentence from right to left. Outputs from LSTM_f ($\overrightarrow{x}_t^f$) and LSTM_b ($\overleftarrow{x}_t^b$) are first concatenated and then fed to the next layer LSTM_1.

Figure.

Figure 3: The structure of bi-directional connections in the first layer of the encoder. LSTM layer LSTM_f processes information from left to right, while LSTM layer LSTM_b processes information from right to left. Output from LSTM_f and LSTM_b are first concatenated and then fed to the next LSTM layer LSTM_1. {#wu-2016-gnmt-fig-3 .figure tag=08E2}

### 3.3 Model Parallelism {#wu-2016-gnmt-s3-3 .section tag=08E3}

Due to the complexity of our model, we make use of both model parallelism and data parallelism to speed up training. Data parallelism is straightforward: we train n model replicas concurrently using a Downpour SGD algorithm [12]. The n replicas all share one copy of model parameters, with each replica asynchronously updating the parameters using a combination of Adam [25] and SGD algorithms. In our experiments, n is often around 10. Each replica works on a mini-batch of m sentence pairs at a time, which is often 128 in our experiments.

In addition to data parallelism, model parallelism is used to improve the speed of the gradient computation on each replica. The encoder and decoder networks are partitioned along the depth dimension and are placed on multiple GPUs, effectively running each layer on a different GPU. Since all but the first encoder layer are uni-directional, layer i + 1 can start its computation before layer i is fully finished, which improves training speed. The softmax layer is also partitioned, with each partition responsible for a subset of symbols in the output vocabulary. Figure 1 shows more details of how partitioning is done.

Model parallelism places certain constraints on the model architectures we can use. For example, we cannot afford to have bi-directional LSTM layers for all the encoder layers, since doing so would reduce parallelism among subsequent layers, as each layer would have to wait until both forward and backward directions of the previous layer have finished. This would effectively constrain us to make use of only 2 GPUs in parallel (one for the forward direction and one for the backward direction). For the attention portion of the model, we chose to align the bottom decoder output to the top encoder output to maximize parallelism when running the decoder network. Had we aligned the top decoder layer to the top encoder layer, we would have removed all parallelism in the decoder network and would not benefit from using more than one GPU for decoding.
