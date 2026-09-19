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
section: "6"
section_title: Quantizable Model and Quantized Inference
tag: "0961"
kind: section
lang: en
source: arxiv:1609.08144
pdf_sha256: 285fb4323972464ba0be4f7c76a0db1a3cc196d5e44be542152f085d47fe5812
pdf_pages: 9-12
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 15d01e45bc16720d5792ae2a790bb325c01636190710b13da83faf9feac9eb70
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

One of the main challenges in deploying our Neural Machine Translation model to our interactive production translation service is that it is computationally intensive at inference, making low latency translation difficult, and high volume deployment computationally expensive. Quantized inference using reduced precision arithmetic is one technique that can significantly reduce the cost of inference for these models, often providing efficiency improvements on the same computational devices. For example, in [43], it is demonstrated that a convolutional neural network model can be sped up by a factor of 4-6 with minimal loss on classification accuracy on the ILSVRC-12 benchmark. In [27], it is demonstrated that neural network model weights can be quantized to only three states, -1, 0, and +1.

Many of those previous studies [19, 20, 43, 27] however mostly focus on CNN models with relatively few layers. Deep LSTMs with long sequences pose a novel challenge in that quantization errors can be significantly amplified after many unrolled steps or after going through a deep LSTM stack.

In this section, we present our approach to speed up inference with quantized arithmetic. Our solution is tailored towards the hardware options available at Google. To reduce quantization errors, additional constraints are added to our model during training so that it is quantizable with minimal impact on the output of the model. That is, once a model is trained with these additional constraints, it can be subsequently quantized without loss to translation quality. Our experimental results suggest that those additional constraints do not hurt model convergence nor the quality of a model once it has converged.

Recall from equation 6 that in an LSTM stack with residual connections there are two accumulators: $c_t^i$ along the time axis and $x_t^i$ along the depth axis. In theory, both of the accumulators are unbounded, but in practice, we noticed their values remain quite small. For quantized inference, we explicitly constrain the values of these accumulators to be within $[-\delta, \delta]$ to guarantee a certain range that can be used for quantization later. The forward computation of an LSTM stack with residual connections is modified to the following:

$$
\begin{align*}
c_t'^i, m_t'^i &= \text{LSTM}_i(c_{t-1}^i, m_{t-1}^i, x_t^{i-1}; W^i) \\
c_t^i &= \max(-\delta, \min(\delta, c_t'^i)) \\
x_t'^i &= m_t'^i + x_t^{i-1} \\
x_t^i &= \max(-\delta, \min(\delta, x_t'^i)) \\
c_t'^{i+1}, m_t'^{i+1} &= \text{LSTM}_{i+1}(c_{t-1}^{i+1}, m_{t-1}^{i+1}, x_t^i; W^{i+1}) \\
c_t^{i+1} &= \max(-\delta, \min(\delta, c_t'^{i+1}))
\end{align*}
$$

Let us expand $\text{LSTM}_i$ in equation 10 to include the internal gating logic. For brevity, we drop all the superscripts $i$.

$$
\mathbf{W} = [\mathbf{W}_1, \mathbf{W}_2, \mathbf{W}_3, \mathbf{W}_4, \mathbf{W}_5, \mathbf{W}_6, \mathbf{W}_7, \mathbf{W}_8]
$$

$$
\mathbf{i}_t = \mathrm{sigmoid}(\mathbf{W}_1 \mathbf{x}_t + \mathbf{W}_2 \mathbf{m}_t)
$$

$$
\mathbf{i}'_t = \tanh(\mathbf{W}_3 \mathbf{x}_t + \mathbf{W}_4 \mathbf{m}_t)
$$

$$
\mathbf{f}_t = \mathrm{sigmoid}(\mathbf{W}_5 \mathbf{x}_t + \mathbf{W}_6 \mathbf{m}_t)
$$

$$
\mathbf{o}_t = \mathrm{sigmoid}(\mathbf{W}_7 \mathbf{x}_t + \mathbf{W}_8 \mathbf{m}_t)
$$

$$
\mathbf{c}_t = \mathbf{c}_{t-1} \odot \mathbf{f}_t + \mathbf{i}'_t \odot \mathbf{i}_t
$$

$$
\mathbf{m}_t = \mathbf{c}_t \odot \mathbf{o}_t
$$

When doing quantized inference, we replace all the floating point operations in equations 10 and 11 with fixed-point integer operations with either 8-bit or 16-bit resolution. The weight matrix $\mathbf{W}$ above is represented using an 8-bit integer matrix $\mathbf{WQ}$ and a float vector $\mathbf{s}$, as shown below:

$$
s_i = \max(\operatorname{abs}(\mathbf{W}[i,:]))
$$

$$
\mathbf{WQ}[i,j] = \operatorname{round}(\mathbf{W}[i,j]/s_i \times 127.0)
$$

All accumulator values ($\mathbf{c}_t^i$ and $\mathbf{x}_t^i$) are represented using 16-bit integers representing the range $[-\delta, \delta]$. All matrix multiplications (e.g., $\mathbf{W}_1 \mathbf{x}_t$, $\mathbf{W}_2 \mathbf{m}_t$, etc.) in equation 11 are done using 8-bit integer multiplication accumulated into larger accumulators. All other operations, including all the activations (sigmoid, tanh) and elementwise operations ($\odot, +$) are done using 16-bit integer operations.

We now turn our attention to the log-linear softmax layer. During training, given the decoder RNN network output $\mathbf{y}_t$, we compute the probability vector $\mathbf{p}_t$ over all candidate output symbols as follows:

$$
\mathbf{v}_t = \mathbf{W}_s * \mathbf{y}_t
$$

$$
\mathbf{v}'_t = \max(-\gamma, \min(\gamma, \mathbf{v}_t))
$$

$$
\mathbf{p}_t = \operatorname{softmax}(\mathbf{v}'_t)
$$

In equation 13, $\mathbf{W}_s$ is the weight matrix for the linear layer, which has the same number of rows as the number of symbols in the target vocabulary with each row corresponding to one unique target symbol. $\mathbf{v}$ represents the raw logits, which are first clipped to be between $-\gamma$ and $\gamma$ and then normalized into a probability vector $\mathbf{p}$. Input $\mathbf{y}_t$ is guaranteed to be between $-\delta$ and $\delta$ due to the quantization scheme we applied to the decoder RNN. The clipping range $\gamma$ for the logits $\mathbf{v}$ is determined empirically, and in our case, it is set to 25. In quantized inference, the weight matrix $\mathbf{W}_s$ is quantized into 8 bits as in equation 12 and the matrix multiplication is done using 8 bit arithmetic. The calculations within the $\operatorname{softmax}$ function and the attention model are not quantized during inference.

It is worth emphasizing that during training of the model we use full-precision floating point numbers. The only constraints we add to the model during training are the clipping of the RNN accumulator values into $[-\delta, \delta]$ and softmax logits into $[-\gamma, \gamma]$. $\gamma$ is fixed to be at 25.0, while the value for $\delta$ is gradually annealed from a generous bound of $\delta = 8.0$ at the beginning of training, to a rather stringent bound of $\delta = 1.0$ towards the end of training. At inference time, $\delta$ is fixed at 1.0. Those additional constraints do not degrade model convergence nor the decoding quality of the model when it has converged. In Figure 4, we compare the loss vs. steps for an unconstrained model (the blue curve) and a constrained model (the red curve) on WMT’14 English-to-French. We can see that the loss for the constrained model is slightly better, possibly due to regularization roles those constraints play.

Our solution strikes a good balance between efficiency and accuracy. Since the computationally expensive operations (the matrix multiplications) are done using 8-bit integer operations, our quantized inference is quite efficient. Also, since error-sensitive accumulator values are stored using 16-bit integers, our solution is very accurate and is robust to quantization errors.

In Table 1 we compare the inference speed and quality when decoding the WMT’14 English-to-French development set (a concatenation of newstest2012 and newstest2013 test sets for a total of 6003 sentences) on

Figure 4: Log perplexity vs. steps for normal (non-quantized) training and quantization-aware training on WMT’14 English to French during maximum likelihood training. Notice the training losses are similar, with the quantization-aware loss being slightly better. Our conjecture for quantization-aware training being slightly better is that the clipping constraints act as additional regularization which improves the model quality. {#wu-2016-gnmt-fig-4 .figure tag=08E6}

CPU, GPU and Google’s Tensor Processing Unit (TPU) respectively.$^1$ The model used here for comparison is trained with quantization constraints on the ML objective only (i.e., without reinforcement learning based model refinement). When the model is decoded on CPU and GPU, it is not quantized and all operations are done using full-precision floats. When it is decoded on TPU, certain operations, such as embedding lookup and attention module, remain on the CPU, and all other quantized operations are off-loaded to the TPU. In all cases, decoding is done on a single machine with two Intel Haswell CPUs, which consists in total of 88 CPU cores (hyperthreads). The machine is equipped with an NVIDIA GPU (Tesla k80) for the experiment with GPU or a single Google TPU for the experiment with TPU.

Table $^1$ shows that decoding using reduced precision arithmetics on the TPU suffers a very minimal loss of 0.0072 on log perplexity, and no loss on BLEU at all. This result matches previous work reporting that quantizing convolutional neural network models can retain most of the model quality.

Table $^1$ also shows that decoding our model on CPU is actually 2.3 times faster than on GPU. Firstly, our dual-CPUs host machine offers a theoretical peak FLOP performance which is more than two thirds that of the GPU. Secondly, the beam search algorithm forces the decoder to incur a non-trivial amount of data transfer between the host and the GPU at every decoding step. Hence, our current decoder implementation

$^1$ https://cloudplatform.googleblog.com/2016/05/Google-supercharges-machine-learning-tasks-with-custom-chip.html is not fully utilizing the computation capacities that a GPU can theoretically offer during inference.

Finally, Table 1 shows that decoding on TPUs is 3.4 times faster than decoding on CPUs, demonstrating that quantized arithmetics is much faster on TPUs than both CPUs or GPUs.

Table 1: Model inference on CPU, GPU and TPU. The model used here for comparison is trained with the ML objective only with quantization constraints. Results are obtained by decoding the WMT En→Fr development set on CPU, GPU and TPU respectively. {#wu-2016-gnmt-tab-1 .table tag=08E7}

|  | BLEU | Log Perplexity | Decoding time (s) |
| --- | --- | --- | --- |
| CPU | 31.20 | 1.4553 | 1322 |
| GPU | 31.20 | 1.4553 | 3028 |
| TPU | 31.21 | 1.4626 | 384 |

Unless otherwise noted, we always train and evaluate quantized models in our experiments. Because there is little difference from a quality perspective between a model decoded on CPUs and one decoded on TPUs, we use CPUs to decode for model evaluation during training and experimentation and use TPUs to serve production traffic.
