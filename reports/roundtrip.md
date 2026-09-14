# Back translation

27 pages checked: 8 the same, 7 differ in wording, 12 differ materially

Run 20260914T070941Z. Every abstract, every section of the first 100 papers of the canon, and a 5% sample of the rest.

88,111 tokens in, 22,656 out.

## Differs materially

### `content/ja/goodfellow-2014-gan/02_related_work.md`

paper 86 of the canon, checked whole, translated by gpt-5, put back by gpt-5, judged by gpt-5. The fleet had nothing else free, so this is a model marking its own work.

- The original says DBNs incur the computational difficulties associated with both undirected and directed models, whereas the back-translation says only that DBNs have computational difficulties associated with both types of models, which is equivalent.
- The original says learning slows dramatically after NCE has learned even an approximately correct distribution over a small subset of the observed variables, whereas the back-translation says the learning rate drops dramatically after it has learned an approximately correct distribution for a small subset, omitting the original emphasis on “even” an approximately correct distribution and changing “learning slows” to “learning rate drops.”
- The original says piecewise linear units improve backpropagation performance but have problems with unbounded activation when used in a feedback loop, whereas the back-translation says the units have the problem that activations become unbounded in feedback loops while improving backpropagation performance, preserving the substantive claim.

The English as it stands:

> An alternative to directed graphical models with latent variables are undirected graphical models with latent variables, such as restricted Boltzmann machines (RBMs) [27, 16], deep Boltzmann machines (DBMs) [26] and their numerous variants. The interactions within such models are represented as the product of unnormalized potential functions, normalized by a global summation/integration over all states of the random variables. This quantity (the *partition function*) and its gradient are intractable for all but the most trivial instances, although they can be estimated by Markov chain Monte Carlo (MCMC) methods. Mixing poses a significant problem for learning algorithms that rely on MCMC [3, 5].
>
> Deep belief networks (DBNs) [16] are hybrid models containing a single undirected layer and several directed layers. While a fast approximate layer-wise training criterion exists, DBNs incur the computational difficulties associated with both undirected and directed models.
>
> Alternative criteria that do not approximate or bound the log-likelihood have also been proposed, such as score matching [18] and noise-contrastive estimation (NCE) [13]. Both of these require the learned probability density to be analytically specified up to a normalization constant. Note that in many interesting generative models with several layers of latent variables (such as DBNs and DBMs), it is not even possible to derive a tractable unnormalized probability density. Some models such as denoising auto-encoders [30] and contractive autoencoders have learning rules very similar to score matching applied to RBMs. In NCE, as in this work, a discriminative training criterion is employed to fit a generative model. However, rather than fitting a separate discriminative model, the generative model itself is used to discriminate generated data from samples a fixed noise distribution. Because NCE uses a fixed noise distribution, learning slows dramatically after the model has learned even an approximately correct distribution over a small subset of the observed variables.
>
> Finally, some techniques do not involve defining a probability distribution explicitly, but rather train a generative machine to draw samples from the desired distribution. This approach has the advantage that such machines can be designed to be trained by back-propagation. Prominent recent work in this area includes the generative stochastic network (GSN) framework [5], which extends generalized denoising auto-encoders [4]: both can be seen as defining a parameterized Markov chain, i.e., one learns the parameters of a machine that performs one step of a generative Markov chain. Compared to GSNs, the adversarial nets framework does not require a Markov chain for sampling. Because adversarial nets do not require feedback loops during generation, they are better able to leverage piecewise linear units [19, 9, 10], which improve the performance of backpropagation but have problems with unbounded activation when used in a feedback loop. More recent examples of training a generative machine by back-propagating into it include recent work on auto-encoding variational Bayes [20] and stochastic backpropagation [24].

What came back:

> As an alternative to directed graphical models with latent variables, there are undirected graphical models with latent variables, such as restricted Boltzmann machines (RBMs) [27, 16], deep Boltzmann machines (DBMs) [26], and their numerous variants. The interactions in such models are represented as a product of unnormalized potential functions, and are normalized by a global summation/integration over all states of the random variables. This quantity (the *partition function*) and its gradient are difficult to handle except in the most trivial cases, but can be estimated by Markov chain Monte Carlo (MCMC) methods. Mixing becomes a serious problem for learning algorithms that depend on MCMC [3, 5].
>
> Deep belief networks (DBNs) [16] are hybrid models that contain a single undirected layer and multiple directed layers. While fast approximate layer-wise learning criteria exist, DBNs have computational difficulties associated with both undirected and directed models.
>
> Alternative criteria that do not approximate the log likelihood or provide upper/lower bounds have also been proposed, such as score matching [18] and noise-contrastive estimation (NCE) [13]. Both of these require the learned probability density to be described analytically up to a normalization constant. For many interesting generative models with multiple layers of latent variables (such as DBNs and DBMs), it is not even possible to derive a tractable unnormalized probability density. Some models, such as denoising auto-encoders [30] and contractive autoencoders, have learning rules very similar to score matching applied to RBMs. In NCE, as in this work, a discriminative learning criterion is used to fit a generative model. However, instead of fitting a separate discriminative model, the generative model itself is used to discriminate between samples from a fixed noise distribution and generated data. Because NCE uses a fixed noise distribution, the learning rate drops dramatically after the model has learned an approximately correct distribution for a small subset of the observed variables.
>
> Finally, there are methods that, rather than explicitly defining a probability distribution, learn a generative machine that generates samples from the desired distribution. This approach has the advantage that such a machine can be designed so that it can be trained by backpropagation. A recent representative work in this field is the generative stochastic network (GSN) framework [5], which extends generalized denoising auto-encoders [4]. Both can be viewed as defining a parameterized Markov chain. That is, the parameters of the machine that performs one step of the generative Markov chain are learned. Compared with GSN, the adversarial nets framework does not require a Markov chain for sampling. Because adversarial nets do not require a feedback loop during generation, they can more effectively utilize piecewise linear units [19, 9, 10], which have the problem that activations become unbounded when used in feedback loops, while improving the performance of backpropagation. More recent examples of learning by performing backpropagation on a generative machine include recent work on auto-encoding variational Bayes [20] and stochastic backpropagation [24].

### `content/ja/goodfellow-2014-gan/03_adversarial_nets.md`

paper 86 of the canon, checked whole, translated by gpt-5, put back by gpt-5, judged by gpt-5. The fleet had nothing else free, so this is a model marking its own work.

- The original claims that the framework is most straightforward when both models are multilayer perceptrons, defines \(p_z\), \(G(\boldsymbol z;\theta_g)\), and \(D(\boldsymbol x;\theta_d)\), explains \(D\)'s probability interpretation, and states how \(D\) and \(G\) are trained, whereas the back-translation drops this entire paragraph and leaves only a fragment before the equation.
- The original explicitly states that \(D\) and \(G\) play a two-player minimax game with value function \(V(G,D)\), whereas the back-translation omits this statement and presents only a truncated equation fragment.

The English as it stands:

> The adversarial modeling framework is most straightforward to apply when the models are both multilayer perceptrons. To learn the generator’s distribution $p_g$ over data $\boldsymbol{x}$, we define a prior on input noise variables $p_z(\boldsymbol{z})$, then represent a mapping to data space as $G(\boldsymbol{z}; \theta_g)$, where $G$ is a differentiable function represented by a multilayer perceptron with parameters $\theta_g$. We also define a second multilayer perceptron $D(\boldsymbol{x}; \theta_d)$ that outputs a single scalar. $D(\boldsymbol{x})$ represents the probability that $\boldsymbol{x}$ came from the data rather than $p_g$. We train $D$ to maximize the probability of assigning the correct label to both training examples and samples from $G$. We simultaneously train $G$ to minimize $\log(1 - D(G(\boldsymbol{z})))$:
>
> In other words, $D$ and $G$ play the following two-player minimax game with value function $V(G,D)$:
>
> $$\min_G \max_D V(D,G) = \mathbb{E}_{x\sim p_{\mathrm{data}}(x)}[\log D(x)] + \mathbb{E}_{z\sim p_z(z)}[\log(1-D(G(z)))]. \tag{1}$$
> {#goodfellow-2014-gan-eq-1 .equation tag=00C4}
>
> In the next section, we present a theoretical analysis of adversarial nets, essentially showing that the training criterion allows one to recover the data generating distribution as $G$ and $D$ are given enough capacity, i.e., in the non-parametric limit. See Figure 1 for a less formal, more pedagogical explanation of the approach. In practice, we must implement the game using an iterative, numerical approach. Optimizing $D$ to completion in the inner loop of training is computationally prohibitive, and on finite datasets would result in overfitting. Instead, we alternate between $k$ steps of optimizing $D$ and one step of optimizing $G$. This results in $D$ being maintained near its optimal solution, so long as $G$ changes slowly enough. This strategy is analogous to the way that SML/PCD [31, 29] training maintains samples from a Markov chain from one learning step to the next in order to avoid burning in a Markov chain as part of the inner loop of learning. The procedure is formally presented in Algorithm 1.
>
> In practice, equation 1 may not provide sufficient gradient for $G$ to learn well. Early in learning, when $G$ is poor, $D$ can reject samples with high confidence because they are clearly different from the training data. In this case, $\log(1-D(G(z)))$ saturates. Rather than training $G$ to minimize $\log(1-D(G(z)))$ we can train $G$ to maximize $\log D(G(z))$. This objective function results in the same fixed point of the dynamics of $G$ and $D$ but provides much stronger gradients early in learning.
>
> Figure 1: Generative adversarial nets are trained by simultaneously updating the discriminative distribution ($D$, blue, dashed line) so that it discriminates between samples from the data generating distribution (black, dotted line) $p_x$ from those of the generative distribution $p_g$ ($G$) (green, solid line). The lower horizontal line is the domain from which $z$ is sampled, in this case uniformly. The horizontal line above is part of the domain of $x$. The upward arrows show how the mapping $x=G(z)$ imposes the non-uniform distribution $p_g$ on transformed samples. $G$ contracts in regions of high density and expands in regions of low density of $p_g$. (a) Consider an adversarial pair near convergence: $p_g$ is similar to $p_{\mathrm{data}}$ and $D$ is a partially accurate classifier. (b) In the inner loop of the algorithm $D$ is trained to discriminate samples from data, converging to $D^*(x)=\frac{p_{\mathrm{data}}(x)}{p_{\mathrm{data}}(x)+p_g(x)}$. (c) After an update to $G$, gradient of $D$ has guided $G(z)$ to flow to regions that are more likely to be classified as data. (d) After several steps of training, if $G$ and $D$ have enough capacity, they will reach a point at which both cannot improve because $p_g=p_{\mathrm{data}}$. The discriminator is unable to differentiate between the two distributions, i.e. $D(x)=\frac{1}{2}$. {#goodfellow-2014-gan-fig-1 .figure tag=00C5}

What came back:

> The adversarial modeling framework is most directly applicable when both\sim p_z(z)}[\log(1-D(G(z)))]. \tag{1}$$
> {#goodfellow-2014-gan-eq-1 .equation tag=00C4}
>
> In the next section, we present a theoretical analysis of adversarial nets. Basically, we show that with this training criterion, when $G$ and $D$ are given sufficient capacity, that is, in the non-parametric limit, the data-generating distribution can be recovered. See Figure 1 for a less formal, educational explanation. In practice, this game must be implemented using iterative numerical methods. Fully optimizing $D$ in the inner loop of training is computationally prohibitively expensive and causes overfitting on finite datasets. Instead, alternately repeat optimizing $D$ for $k$ steps, and then optimizing $G$ for 1 step. This keeps $D$ near its optimal solution as long as $G$ changes sufficiently slowly. This strategy is similar to the way SML/PCD [31, 29] training maintains samples from a Markov chain from one training step to the next in order to avoid burning in the Markov chain as part of the inner loop of training. This procedure is formally shown in Algorithm 1.
>
> In practice, Equation 1 may not provide sufficient gradients for $G$ to learn well enough. In the early stages of training, when the performance of $G$ is low, $D$ can reject the samples with high confidence because the samples are clearly different from the training data. In this case, $\log(1-D(G(z)))$ saturates. Instead of training $G$ toward minimizing $\log(1-D(G(z)))$, we can train $G$ to maximize $\log D(G(z))$. This objective function produces the same fixed point in the dynamical system of $G$ and $D$, but provides much stronger gradients in the early stages of training.
>
> Figure 1: Generative adversarial nets are learned by simultaneously updating the discriminative distribution ($D$, blue, dashed). This distinguishes between samples from the data-generating distribution (black, dotted) $p_x$ and samples from the generative distribution $p_g$ ($G$) (green, solid). The lower horizontal line is the domain from which $z$ is sampled, which is uniform in this case. The upper horizontal line is part of the domain of $x$. The upward arrows show how the mapping $x=G(z)$ imposes a non-uniform distribution $p_g$ on the transformed samples. $G$ contracts in high-density regions and expands in low-density regions of $p_g$. (a) Consider an adversarial pair near convergence. $p_g$ is similar to $p_{\mathrm{data}}$, and $D$ is a partially accurate classifier. (b) In the inner loop of the algorithm, $D$ is trained to distinguish samples from the data, and converges to $D^*(x)=\frac{p_{\mathrm{data}}(x)}{p_{\mathrm{data}}(x)+p_g(x)}$. (c) After the update of $G$, the gradient of $D$ guides $G(z)$ to flow toward regions more likely to be classified as data. (d) After several steps of training, if $G$ and $D$ have sufficient capacity, they reach a point where neither can improve because $p_g=p_{\mathrm{data}}$. The discriminator cannot distinguish between the two distributions, that is, $D(x)=\frac{1}{2}$. {#goodfellow-2014-gan-fig-1 .figure tag=00C5}

### `content/ja/goodfellow-2014-gan/04_theoretical_results.md`

paper 86 of the canon, checked whole, translated by gpt-5, put back by gpt-5, judged by gpt-5. The fleet had nothing else free, so this is a model marking its own work.

- The original says the function \(y\rightarrow a\log(y)+b\log(1-y)\) achieves its maximum **in** \([0,1]\) at \(\frac{a}{a+b}\), while the back-translation says it achieves its maximum **at** \(\frac{a}{a+b}\) on \([0,1]\); this is only a wording difference.
- The original says the Jensen–Shannon divergence is non-negative and zero only when the distributions are equal, while the back-translation says the same and is therefore equivalent.
- The original says the multilayer perceptrons' excellent performance **in practice suggests** they are a reasonable model despite lacking theoretical guarantees, while the back-translation says their **actual good performance suggests** they are reasonable models; this is only a slight wording change.
- The original proof of Proposition 2 concludes that \(p_g\) converges to \(p_x\), while the proposition itself states convergence to \(p_{\mathrm{data}}\); the back-translation preserves the same mismatch.

The English as it stands:

> The generator $G$ implicitly defines a probability distribution $p_g$ as the distribution of the samples $G(z)$ obtained when $z\sim p_z$. Therefore, we would like Algorithm 1 to converge to a good estimator of $p_{\mathrm{data}}$, if given enough capacity and training time. The results of this section are done in a non-parametric setting, e.g. we represent a model with infinite capacity by studying convergence in the space of probability density functions.
>
> We will show in section 4.1 that this minimax game has a global optimum for $p_g=p_{\mathrm{data}}$. We will then show in section 4.2 that Algorithm 1 optimizes Eq 1, thus obtaining the desired result.
>
> **Algorithm 1** Minibatch stochastic gradient descent training of generative adversarial nets. The number of steps to apply to the discriminator, $k$, is a hyperparameter. We used $k = 1$, the least expensive option in our experiments.
>
> **for** number of training iterations **do**
>
> **for** $k$ steps **do**
>
> - Sample minibatch of $m$ noise samples $\{z^{(1)}, \ldots, z^{(m)}\}$ from noise prior $p_g(z)$.
> - Sample minibatch of $m$ examples $\{x^{(1)}, \ldots, x^{(m)}\}$ from data generating distribution $p_{\text{data}}(x)$.
> - Update the discriminator by ascending its stochastic gradient:
>
> $$\nabla_{\theta_d}\frac{1}{m}\sum_{i=1}^{m}\left[\log D\left(x^{(i)}\right)+\log\left(1-D\left(G\left(z^{(i)}\right)\right)\right)\right].$$
>
> **end for**
>
> - Sample minibatch of $m$ noise samples $\{z^{(1)}, \ldots, z^{(m)}\}$ from noise prior $p_g(z)$.
> - Update the generator by descending its stochastic gradient:
>
> $$\nabla_{\theta_g}\frac{1}{m}\sum_{i=1}^{m}\log\left(1-D\left(G\left(z^{(i)}\right)\right)\right).$$
>
> **end for**
>
> The gradient-based updates can use any standard gradient-based learning rule. We used momentum in our experiments.
>
> ### 4.1 Global Optimality of $p_g = p_{\text{data}}$ {#goodfellow-2014-gan-s4-1 .section tag=00C7}
>
> We first consider the optimal discriminator $D$ for any given generator $G$.
>
> **Proposition 1.** *For $G$ fixed, the optimal discriminator $D$ is* {#goodfellow-2014-gan-prop-1 .statement tag=00C8}
>
> $$D_G^*(x)=\frac{p_{\text{data}}(x)}{p_{\text{data}}(x)+p_g(x)}\tag{2}$$
> {#goodfellow-2014-gan-eq-2 .equation tag=014B}
>
> *Proof.* The training criterion for the discriminator D, given any generator G, is to maximize the quantity $V(G,D)$
>
> $$\begin{aligned}
> V(G,D)&=\int_x p_{\text{data}}(x)\log(D(x))dx+\int_z p_z(z)\log(1-D(g(z)))dz\\
> &=\int_x p_{\text{data}}(x)\log(D(x))+p_g(x)\log(1-D(x))dx
> \end{aligned}\tag{3}$$
> {#goodfellow-2014-gan-eq-3 .equation tag=014C}
>
> For any $(a,b)\in\mathbb{R}^2\setminus\{0,0\}$, the function $y\rightarrow a\log(y)+b\log(1-y)$ achieves its maximum in $[0,1]$ at $\frac{a}{a+b}$. The discriminator does not need to be defined outside of $Supp(p_{\text{data}})\cup Supp(p_g)$, concluding the proof. $\square$
>
> Note that the training objective for $D$ can be interpreted as maximizing the log-likelihood for estimating the conditional probability $P(Y=y|x)$, where $Y$ indicates whether $x$ comes from $p_{\text{data}}$ (with $y=1$) or from $p_g$ (with $y=0$). The minimax game in Eq. 1 can now be reformulated as:
>
> $$\begin{aligned}
> C(G)&=\max_D V(G,D)\\
> &=\mathbb{E}_{x\sim p_{\text{data}}}\left[\log D_G^*(x)\right]+\mathbb{E}_{z\sim p_z}\left[\log(1-D_G^*(G(z)))\right]\\
> &=\mathbb{E}_{x\sim p_{\text{data}}}\left[\log D_G^*(x)\right]+\mathbb{E}_{x\sim p_g}\left[\log(1-D_G^*(x))\right]\\
> &=\mathbb{E}_{x\sim p_{\text{data}}}\left[\log\frac{p_{\text{data}}(x)}{p_{\text{data}}(x)+p_g(x)}\right]+\mathbb{E}_{x\sim p_g}\left[\log\frac{p_g(x)}{p_{\text{data}}(x)+p_g(x)}\right]
> \end{aligned}\tag{4}$$
> {#goodfellow-2014-gan-eq-4 .equation tag=014D}
>
> **Theorem 1.** *The global minimum of the virtual training criterion $C(G)$ is achieved if and only if $p_g = p_{\mathrm{data}}$. At that point, $C(G)$ achieves the value $-\log 4$.* {#goodfellow-2014-gan-thm-1 .statement tag=0111}
>
> *Proof.* For $p_g = p_{\mathrm{data}}$, $D_G^*(x) = \frac{1}{2}$, (consider Eq. 2). Hence, by inspecting Eq. 4 at $D_G^*(x) = \frac{1}{2}$, we find $C(G) = \log \frac{1}{2} + \log \frac{1}{2} = -\log 4$. To see that this is the best possible value of $C(G)$, reached only for $p_g = p_{\mathrm{data}}$, observe that
>
> $$\mathbb{E}_{x\sim p_{\mathrm{data}}}[-\log 2] + \mathbb{E}_{x\sim p_g}[-\log 2] = -\log 4$$
>
> and that by subtracting this expression from $C(G) = V(D_G^*, G)$, we obtain:
>
> $$C(G) = -\log(4) + KL\left(p_{\mathrm{data}} \left\| \frac{p_{\mathrm{data}} + p_g}{2}\right.\right) + KL\left(p_g \left\| \frac{p_{\mathrm{data}} + p_g}{2}\right.\right) \tag{5}$$
> {#goodfellow-2014-gan-eq-5 .equation tag=014E}
>
> where KL is the Kullback–Leibler divergence. We recognize in the previous expression the Jensen–Shannon divergence between the model’s distribution and the data generating process:
>
> $$C(G) = -\log(4) + 2 \cdot JSD(p_{\mathrm{data}} \| p_g) \tag{6}$$
> {#goodfellow-2014-gan-eq-6 .equation tag=014F}
>
> Since the Jensen–Shannon divergence between two distributions is always non-negative and zero only when they are equal, we have shown that $C^* = -\log(4)$ is the global minimum of $C(G)$ and that the only solution is $p_g = p_{\mathrm{data}}$, i.e., the generative model perfectly replicating the data generating process. $\square$
>
> ### 4.2 Convergence of Algorithm 1 {#goodfellow-2014-gan-s4-2 .section tag=0112}
>
> **Proposition 2.** *If $G$ and $D$ have enough capacity, and at each step of Algorithm 1, the discriminator is allowed to reach its optimum given $G$, and $p_g$ is updated so as to improve the criterion* {#goodfellow-2014-gan-prop-2 .statement tag=0113}
>
> $$\mathbb{E}_{x\sim p_{\mathrm{data}}}[\log D_G^*(x)] + \mathbb{E}_{x\sim p_g}[\log(1 - D_G^*(x))]$$
>
> *then $p_g$ converges to $p_{\mathrm{data}}$*
>
> *Proof.* Consider $V(G, D) = U(p_g, D)$ as a function of $p_g$ as done in the above criterion. Note that $U(p_g, D)$ is convex in $p_g$. The subderivatives of a supremum of convex functions include the derivative of the function at the point where the maximum is attained. In other words, if $f(x) = \sup_{\alpha\in\mathcal{A}} f_\alpha(x)$ and $f_\alpha(x)$ is convex in $x$ for every $\alpha$, then $\partial f_\beta(x) \in \partial f$ if $\beta = \arg \sup_{\alpha\in\mathcal{A}} f_\alpha(x)$. This is equivalent to computing a gradient descent update for $p_g$ at the optimal $D$ given the corresponding $G$. $\sup_D U(p_g, D)$ is convex in $p_g$ with a unique global optima as proven in Thm 1, therefore with sufficiently small updates of $p_g$, $p_g$ converges to $p_x$, concluding the proof. $\square$
>
> In practice, adversarial nets represent a limited family of $p_g$ distributions via the function $G(z; \theta_g)$, and we optimize $\theta_g$ rather than $p_g$ itself. Using a multilayer perceptron to define $G$ introduces multiple critical points in parameter space. However, the excellent performance of multilayer perceptrons in practice suggests that they are a reasonable model to use despite their lack of theoretical guarantees.

What came back:

> The generator $G$ implicitly defines a probability distribution $p_g$ as the distribution of samples $G(z)$ obtained when $z\sim p_z$. Therefore, given sufficient capacity and training time, we hope that Algorithm 1 converges to a good estimator of $p_{\mathrm{data}}$. The results in this section are obtained in a nonparametric setting. For example, we represent a model with infinite capacity by examining convergence in the space of probability density functions.
>
> In Section 4.1, we show that this minimax game has a global optimum for $p_g=p_{\mathrm{data}}$. Subsequently, in Section 4.2, we show that Algorithm 1 optimizes Equation 1, and show that this produces the desired result.
>
> **Algorithm 1** Learning generative adversarial networks by minibatch stochastic gradient descent. The number of steps $k$ applied to the discriminator is a hyperparameter. In our experiments, we used $k = 1$, which is the least computationally expensive choice.
>
> **for** number of training iterations **do**
>
> **for** $k$ steps **do**
>
> - Sample a minibatch of $m$ noise samples $\{z^{(1)}, \ldots, z^{(m)}\}$ from the noise prior distribution $p_g(z)$.
> - Sample a minibatch of $m$ examples $\{x^{(1)}, \ldots, x^{(m)}\}$ from the data-generating distribution $p_{\text{data}}(x)$.
> - Update the discriminator by ascending along the stochastic gradient.
>
> $$\nabla_{\theta_d}\frac{1}{m}\sum_{i=1}^{m}\left[\log D\left(x^{(i)}\right)+\log\left(1-D\left(G\left(z^{(i)}\right)\right)\right)\right].$$
>
> **end for**
>
> - Sample a minibatch of $m$ noise samples $\{z^{(1)}, \ldots, z^{(m)}\}$ from the noise prior distribution $p_g(z)$.
> - Update the generator by descending along the stochastic gradient.
>
> $$\nabla_{\theta_g}\frac{1}{m}\sum_{i=1}^{m}\log\left(1-D\left(G\left(z^{(i)}\right)\right)\right).$$
>
> **end for**
>
> Any standard gradient-based learning rule can be used for the gradient-based updates. In our experiments, we used momentum.
>
> ### 4.1 Global optimality of $p_g = p_{\text{data}}$ {#goodfellow-2014-gan-s4-1 .section tag=00C7}
>
> First, consider the optimal discriminator $D$ for any given generator $G$.
>
> **Proposition 1.** *When $G$ is fixed, the optimal discriminator $D$ is as follows* {#goodfellow-2014-gan-prop-1 .statement tag=00C8}
>
> $$D_G^*(x)=\frac{p_{\text{data}}(x)}{p_{\text{data}}(x)+p_g(x)}\tag{2}$$
> {#goodfellow-2014-gan-eq-2 .equation tag=014B}
>
> *Proof.* Given any generator G, the training criterion of the discriminator D is to maximize the quantity $V(G,D)$.
>
> $$\begin{aligned}
> V(G,D)&=\int_x p_{\text{data}}(x)\log(D(x))dx+\int_z p_z(z)\log(1-D(g(z)))dz\\
> &=\int_x p_{\text{data}}(x)\log(D(x))+p_g(x)\log(1-D(x))dx
> \end{aligned}\tag{3}$$
> {#goodfellow-2014-gan-eq-3 .equation tag=014C}
>
> For any $(a,b)\in\mathbb{R}^2\setminus\{0,0\}$, the function $y\rightarrow a\log(y)+b\log(1-y)$ achieves its maximum at $\frac{a}{a+b}$ on $[0,1]$. Since the discriminator does not need to be defined outside $Supp(p_{\text{data}})\cup Supp(p_g)$, the proof is complete. $\square$
>
> Note that the training objective function of $D$ can be interpreted as maximizing the log-likelihood for estimating the conditional probability $P(Y=y|x)$. Here $Y$ indicates whether $x$ came from $p_{\text{data}}$ ($y=1$) or from $p_g$ ($y=0$). The minimax game of Equation 1 can be reformulated as follows.
>
> $$\begin{aligned}
> C(G)&=\max_D V(G,D)\\
> &=\mathbb{E}_{x\sim p_{\text{data}}}\left[\log D_G^*(x)\right]+\mathbb{E}_{z\sim p_z}\left[\log(1-D_G^*(G(z)))\right]\\
> &=\mathbb{E}_{x\sim p_{\text{data}}}\left[\log D_G^*(x)\right]+\mathbb{E}_{x\sim p_g}\left[\log(1-D_G^*(x))\right]\\
> &=\mathbb{E}_{x\sim p_{\text{data}}}\left[\log\frac{p_{\text{data}}(x)}{p_{\text{data}}(x)+p_g(x)}\right]+\mathbb{E}_{x\sim p_g}\left[\log\frac{p_g(x)}{p_{\text{data}}(x)+p_g(x)}\right]
> \end{aligned}\tag{4}$$
> {#goodfellow-2014-gan-eq-4 .equation tag=014D}
>
> **Theorem 1.** *The global minimum of the virtual training criterion $C(G)$ is achieved if and only if $p_g = p_{\mathrm{data}}$. At that time, $C(G)$ achieves the value $-\log 4$.* {#goodfellow-2014-gan-thm-1 .statement tag=0111}
>
> *Proof.* When $p_g = p_{\mathrm{data}}$, $D_G^*(x) = \frac{1}{2}$ (see Equation 2). Therefore, by examining Equation 4 at $D_G^*(x) = \frac{1}{2}$, we obtain $C(G) = \log \frac{1}{2} + \log \frac{1}{2} = -\log 4$. To show that this is the best value that $C(G)$ can take, and that it is achieved only when $p_g = p_{\mathrm{data}}$, observe the following.
>
> $$\mathbb{E}_{x\sim p_{\mathrm{data}}}[-\log 2] + \mathbb{E}_{x\sim p_g}[-\log 2] = -\log 4$$
>
> And by subtracting this equation from $C(G) = V(D_G^*, G)$, we obtain the following.
>
> $$C(G) = -\log(4) + KL\left(p_{\mathrm{data}} \left\| \frac{p_{\mathrm{data}} + p_g}{2}\right.\right) + KL\left(p_g \left\| \frac{p_{\mathrm{data}} + p_g}{2}\right.\right) \tag{5}$$
> {#goodfellow-2014-gan-eq-5 .equation tag=014E}
>
> Here, KL is the Kullback–Leibler divergence. In the preceding expression, we can recognize the Jensen–Shannon divergence between the model distribution and the data-generating process.
>
> $$C(G) = -\log(4) + 2 \cdot JSD(p_{\mathrm{data}} \| p_g) \tag{6}$$
> {#goodfellow-2014-gan-eq-6 .equation tag=014F}
>
> Since the Jensen–Shannon divergence between two distributions is always nonnegative and is zero only when they are equal, we have shown that $C^* = -\log(4)$ is the global minimum of $C(G)$, and the unique solution is $p_g = p_{\mathrm{data}}$, that is, the generative model completely reproduces the data-generating process. $\square$
>
> ### 4.2 Convergence of Algorithm 1 {#goodfellow-2014-gan-s4-2 .section tag=0112}
>
> **Proposition 2.** *If $G$ and $D$ have sufficient capacity, and at each step of Algorithm 1, the discriminator is allowed to reach the optimal value for the given $G$, and furthermore $p_g$ is updated to improve the following criterion* {#goodfellow-2014-gan-prop-2 .statement tag=0113}
>
> $$\mathbb{E}_{x\sim p_{\mathrm{data}}}[\log D_G^*(x)] + \mathbb{E}_{x\sim p_g}[\log(1 - D_G^*(x))]$$
>
> *$p_g$ converges to $p_{\mathrm{data}}$*
>
> *Proof.* As was done with the above criterion, consider $V(G, D) = U(p_g, D)$ as a function of $p_g$. Note that $U(p_g, D)$ is convex with respect to $p_g$. The subdifferential of the supremum of a family of convex functions contains the derivative of the function at the point where the maximum is achieved. In other words, if $f(x) = \sup_{\alpha\in\mathcal{A}} f_\alpha(x)$ and $f_\alpha(x)$ is convex with respect to $x$ for every $\alpha$, then when $\beta = \arg \sup_{\alpha\in\mathcal{A}} f_\alpha(x)$, $\partial f_\beta(x) \in \partial f$. This is equivalent to calculating the gradient descent update for $p_g$ at the optimal $D$ given the corresponding $G$. As proved in Theorem 1, $\sup_D U(p_g, D)$ is convex with respect to $p_g$, and has a unique global optimum. Therefore, if the update of $p_g$ is sufficiently small, $p_g$ converges to $p_x$, completing the proof. $\square$
>
> In practice, adversarial networks represent a restricted family of the $p_g$ distribution through the function $G(z; \theta_g)$, and optimize $\theta_g$ rather than $p_g$ itself. When a multilayer perceptron is used to define $G$, multiple critical points are introduced into the parameter space. However, the fact that multilayer perceptrons actually show good performance suggests that they are reasonable models to use despite the lack of theoretical guarantees.

### `content/ja/goodfellow-2014-gan/05_experiments.md`

paper 86 of the canon, checked whole, translated by gpt-5, put back by gpt-5, judged by gpt-5. The fleet had nothing else free, so this is a model marking its own work.

- The original says that \(p(x)\) is intractable and **may** be approximated with AIS, whereas the back-translation says it is infeasible but **can** be approximated with AIS, changing a qualified possibility into an unqualified capability.

The English as it stands:

> We trained adversarial nets on a range of datasets including MNIST[[lecun-1998-lenet]], the Toronto Face Database (TFD) [28], and CIFAR-10 [21]. The generator nets used a mixture of rectifier linear activations [19, 9] and sigmoid activations, while the discriminator net used maxout [10] activations. Dropout [17] was applied in training the discriminator net. While our theoretical framework permits the use of dropout and other noise at intermediate layers of the generator, we used noise as the input to only the bottommost layer of the generator network.
>
> We estimate probability of the test set data under $p_g$ by fitting a Gaussian Parzen window to the samples generated with $G$ and reporting the log-likelihood under this distribution. The $\sigma$ parameter
>
> | Model | MNIST | TFD |
> |---|---|---|
> | DBN [3] | $138 \pm 2$ | $1909 \pm 66$ |
> | Stacked CAE [3] | $121 \pm 1.6$ | $\mathbf{2110 \pm 50}$ |
> | Deep GSN [6] | $214 \pm 1.1$ | $1890 \pm 29$ |
> | Adversarial nets | $\mathbf{225 \pm 2}$ | $\mathbf{2057 \pm 26}$ |
>
> Table 1: Parzen window-based log-likelihood estimates. The reported numbers on MNIST are the mean log-likelihood of samples on test set, with the standard error of the mean computed across examples. On TFD, we computed the standard error across folds of the dataset, with a different $\sigma$ chosen using the validation set of each fold. On TFD, $\sigma$ was cross validated on each fold and mean log-likelihood on each fold were computed. For MNIST we compare against other models of the real-valued (rather than binary) version of dataset. {#goodfellow-2014-gan-tab-1 .table tag=00CA}
>
> of the Gaussians was obtained by cross validation on the validation set. This procedure was introduced in Breuleux *et al.* [8] and used for various generative models for which the exact likelihood is not tractable [25, 3, 5]. Results are reported in Table 1. This method of estimating the likelihood has somewhat high variance and does not perform well in high dimensional spaces but it is the best method available to our knowledge. Advances in generative models that can sample but not estimate likelihood directly motivate further research on how to evaluate such models.
>
> In Figures 2 and 3 we show samples drawn from the generator net after training. While we make no claim that these samples are better than samples generated by existing methods, we believe that these samples are at least competitive with the better generative models in the literature and highlight the potential of the adversarial framework.
>
> Figure 2: Visualization of samples from the model. Rightmost column shows the nearest training example of the neighboring sample, in order to demonstrate that the model has not memorized the training set. Samples are fair random draws, not cherry-picked. Unlike most other visualizations of deep generative models, these images show actual samples from the model distributions, not conditional means given samples of hidden units. Moreover, these samples are uncorrelated because the sampling process does not depend on Markov chain mixing. a) MNIST b) TFD c) CIFAR-10 (fully connected model) d) CIFAR-10 (convolutional discriminator and “deconvolutional” generator) {#goodfellow-2014-gan-fig-2 .figure tag=00CB}
>
> Figure 3: Digits obtained by linearly interpolating between coordinates in $z$ space of the full model. {#goodfellow-2014-gan-fig-3 .figure tag=00CC}
>
> |  | Deep directed graphical models | Deep undirected graphical models | Generative autoencoders | Adversarial models |
> |---|---|---|---|---|
> | Training | Inference needed during training. | Inference needed during training. MCMC needed to approximate partition function gradient. | Enforced tradeoff between mixing and power of reconstruction generation | Synchronizing the discriminator with the generator. Helvetica. |
> | Inference | Learned approximate inference | Variational inference | MCMC-based inference | Learned approximate inference |
> | Sampling | No difficulties | Requires Markov chain | Requires Markov chain | No difficulties |
> | Evaluating $p(x)$ | Intractable, may be approximated with AIS | Intractable, may be approximated with AIS | Not explicitly represented, may be approximated with Parzen density estimation | Not explicitly represented, may be approximated with Parzen density estimation |
> | Model design | Nearly all models incur extreme difficulty | Careful design needed to ensure multiple properties | Any differentiable function is theoretically permitted | Any differentiable function is theoretically permitted |
>
> Table 2: Challenges in generative modeling: a summary of the difficulties encountered by different approaches to deep generative modeling for each of the major operations involving a model. {#goodfellow-2014-gan-tab-2 .table tag=00CD}

What came back:

> Trained adversarial nets on various datasets including MNIST[[lecun-1998-lenet]], Toronto Face Database (TFD) [28], and CIFAR-10 [21]. The generator net used a mixture of rectifier linear activation [19, 9] and sigmoid activation, while the discriminator net used maxout [10] activation. Dropout [17] was applied to train the discriminator net. In the theoretical framework it is possible to use dropout and other noise in the intermediate layers of the generator, but in this study noise was used only as input to the lowest layer of the generator network.
>
> By fitting a Gaussian Parzen window to the samples generated by $G$ and reporting the log-likelihood under this distribution, we estimate the probability of test set data under $p_g$. The $\sigma$ parameter
>
> | Model | MNIST | TFD |
> |---|---|---|
> | DBN [3] | $138 \pm 2$ | $1909 \pm 66$ |
> | Stacked CAE [3] | $121 \pm 1.6$ | $\mathbf{2110 \pm 50}$ |
> | Deep GSN [6] | $214 \pm 1.1$ | $1890 \pm 29$ |
> | Adversarial net | $\mathbf{225 \pm 2}$ | $\mathbf{2057 \pm 26}$ |
>
> Table 1: Log-likelihood estimates based on Parzen window. The numbers reported for MNIST are the average log-likelihood of samples on the test set, and the standard error of the mean was calculated across samples. For TFD, the standard error was calculated across each fold of the dataset, and a different $\sigma$ was selected using the validation set of each fold. For TFD, cross-validation of $\sigma$ was performed for each fold, and the average log-likelihood of each fold was calculated. For MNIST, we compare against other models on the real-valued version of the dataset rather than the binary version. {#goodfellow-2014-gan-tab-1 .table tag=00CA}
>
> The Gaussian was obtained by cross-validation on the validation set. This method was introduced by Breuleux *et al.* [8] and has been used for various generative models for which exact likelihood calculation is infeasible [25, 3, 5]. The results are shown in Table 1. This likelihood estimation method has somewhat high variance and does not work well in high-dimensional spaces, but to the best of our knowledge it is the best available method. Progress in generative models that can sample but cannot directly estimate likelihood is encouraging further research on methods for evaluating such models.
>
> Figures 2 and 3 show samples obtained from the generator net after training. We do not claim that these samples are superior to samples generated by existing methods, but we believe that they are at least competitive with good generative models in the literature and demonstrate the potential of the adversarial framework.
>
> Figure 2: Visualization of samples from the model. The rightmost column shows the training sample closest to the adjacent sample, intended to demonstrate that the model has not memorized the training set. The samples are not arbitrarily selected, but are fair random draws. Unlike many other visualizations of deep generative models, these images show actual samples from the model distribution rather than conditional means conditioned on samples of hidden units. Furthermore, because the sampling process does not depend on mixing of a Markov chain, these samples are uncorrelated. a) MNIST b) TFD c) CIFAR-10 (fully connected model) d) CIFAR-10 (convolutional discriminator and “deconvolutional” generator) {#goodfellow-2014-gan-fig-2 .figure tag=00CB}
>
> Figure 3: Digits obtained by linearly interpolating between coordinates in the $z$ space of the full model. {#goodfellow-2014-gan-fig-3 .figure tag=00CC}
>
> |  | Deep directed graphical models | Deep undirected graphical models | Generative autoencoder | Adversarial model |
> |---|---|---|---|---|
> | Training | Inference is required during training. | Inference is required during training. MCMC is required to approximate the gradient of the partition function. | Forces a trade-off between mixing and reconstruction generation ability. | Synchronization of discriminator and generator.Helvetica。 |
> | Inference | Learned approximate inference | Variational inference | MCMC-based inference | Learned approximate inference |
> | Sampling | No difficulty | Markov chain required | Markov chain required | No difficulty |
> | $p(x)$ evaluation | Infeasible but can be approximated by AIS | Infeasible but can be approximated by AIS | Not explicitly represented, but can be approximated by Parzen density estimation | Not explicitly represented, but can be approximated by Parzen density estimation |
> | Model design | Extreme difficulty arises in almost all models | Careful design is required to guarantee multiple properties | Any differentiable function is theoretically allowed | Any differentiable function is theoretically allowed |
>
> Table 2: Challenges in generative modeling. A summary of the difficulties encountered by different approaches to deep generative modeling for each of the major operations involving the model. {#goodfellow-2014-gan-tab-2 .table tag=00CD}

### `content/vi/goodfellow-2014-gan/00_front.md`

every abstract is checked, translated by gpt-5, put back by gpt-5, judged by gpt-5. The fleet had nothing else free, so this is a model marking its own work.

- The original says there is no need for Markov chains or unrolled approximate inference networks during training or sample generation, whereas the back-translation says no Markov chains or approximate inference networks need to be implemented extensively during those phases, weakening and changing the claim about unrolled networks and the extent of the requirement.

The English as it stands:

> Generative Adversarial Nets
>
> **Ian J. Goodfellow, Jean Pouget-Abadie[^1], Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair[^2], Aaron Courville, Yoshua Bengio[^3]**
>
> Département d’informatique et de recherche opérationnelle  
> Université de Montréal  
> Montréal, QC H3C 3J7
>
> arXiv:1406.2661v1 [stat.ML] 10 Jun 2014
>
> Abstract
>
> We propose a new framework for estimating generative models via an adversarial process, in which we simultaneously train two models: a generative model $G$ that captures the data distribution, and a discriminative model $D$ that estimates the probability that a sample came from the training data rather than $G$. The training procedure for $G$ is to maximize the probability of $D$ making a mistake. This framework corresponds to a minimax two-player game. In the space of arbitrary functions $G$ and $D$, a unique solution exists, with $G$ recovering the training data distribution and $D$ equal to $\frac{1}{2}$ everywhere. In the case where $G$ and $D$ are defined by multilayer perceptrons, the entire system can be trained with backpropagation. There is no need for any Markov chains or unrolled approximate inference networks during either training or generation of samples. Experiments demonstrate the potential of the framework through qualitative and quantitative evaluation of the generated samples.

What came back:

> Generative Adversarial Networks
>
> **Ian J. Goodfellow, Jean Pouget-Abadie[^1], Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair[^2], Aaron Courville, Yoshua Bengio[^3]**
>
> Department of computer science and operations research  
> University of Montreal  
> Montreal, QC H3C 3J7
>
> arXiv:1406.2661v1 [stat.ML] 10 Jun 2014
>
> Abstract
>
> We propose a new framework for estimating generative models through an adversarial process, in which we simultaneously train two models: a generative model $G$ that captures the data distribution, and a discriminative model $D$ that estimates the probability that a sample comes from the training data rather than from $G$. The training procedure for $G$ is to maximize the probability that $D$ makes a mistake. This framework corresponds to a two-player minimax game. In the space of arbitrary functions $G$ and $D$, there exists a unique solution, in which $G$ recovers the training data distribution and $D$ equals $\frac{1}{2}$ everywhere. In the case where $G$ and $D$ are defined by multilayer perceptrons, the entire system can be trained by backpropagation. No Markov chains or approximate inference networks need to be implemented extensively in either the training phase or the generation phase. Experiments show the potential of this framework through qualitative and quantitative evaluation of the generated samples.

### `content/vi/goodfellow-2014-gan/02_related_work.md`

paper 86 of the canon, checked whole, translated by gpt-5, put back by gpt-5, judged by gpt-5. The fleet had nothing else free, so this is a model marking its own work.

- The original says DBNs have several directed layers, while the back-translation says they have many directed layers; this is a slight quantity change.
- The original says NCE learning slows “dramatically,” while the back-translation says it slows “significantly”; this softens the stated degree of slowdown.
- The original says the model has learned an “approximately correct” distribution, while the back-translation says it has learned a “correct approximate” distribution; this does not materially change the claim.
- The original says adversarial nets are “better able to leverage” piecewise linear units, while the back-translation says they “have the potential to make better use” of them; this changes a claim of demonstrated comparative ability into a hedged potential.
- The original says GSNs “extend” generalized denoising auto-encoders, while the back-translation says GSN is “an extension” of them; this preserves the claim.
- The original says more recent examples involve back-propagating “into it,” while the back-translation says “into itself”; this slightly narrows the wording but does not materially alter the claim.

The English as it stands:

> An alternative to directed graphical models with latent variables are undirected graphical models with latent variables, such as restricted Boltzmann machines (RBMs) [27, 16], deep Boltzmann machines (DBMs) [26] and their numerous variants. The interactions within such models are represented as the product of unnormalized potential functions, normalized by a global summation/integration over all states of the random variables. This quantity (the *partition function*) and its gradient are intractable for all but the most trivial instances, although they can be estimated by Markov chain Monte Carlo (MCMC) methods. Mixing poses a significant problem for learning algorithms that rely on MCMC [3, 5].
>
> Deep belief networks (DBNs) [16] are hybrid models containing a single undirected layer and several directed layers. While a fast approximate layer-wise training criterion exists, DBNs incur the computational difficulties associated with both undirected and directed models.
>
> Alternative criteria that do not approximate or bound the log-likelihood have also been proposed, such as score matching [18] and noise-contrastive estimation (NCE) [13]. Both of these require the learned probability density to be analytically specified up to a normalization constant. Note that in many interesting generative models with several layers of latent variables (such as DBNs and DBMs), it is not even possible to derive a tractable unnormalized probability density. Some models such as denoising auto-encoders [30] and contractive autoencoders have learning rules very similar to score matching applied to RBMs. In NCE, as in this work, a discriminative training criterion is employed to fit a generative model. However, rather than fitting a separate discriminative model, the generative model itself is used to discriminate generated data from samples a fixed noise distribution. Because NCE uses a fixed noise distribution, learning slows dramatically after the model has learned even an approximately correct distribution over a small subset of the observed variables.
>
> Finally, some techniques do not involve defining a probability distribution explicitly, but rather train a generative machine to draw samples from the desired distribution. This approach has the advantage that such machines can be designed to be trained by back-propagation. Prominent recent work in this area includes the generative stochastic network (GSN) framework [5], which extends generalized denoising auto-encoders [4]: both can be seen as defining a parameterized Markov chain, i.e., one learns the parameters of a machine that performs one step of a generative Markov chain. Compared to GSNs, the adversarial nets framework does not require a Markov chain for sampling. Because adversarial nets do not require feedback loops during generation, they are better able to leverage piecewise linear units [19, 9, 10], which improve the performance of backpropagation but have problems with unbounded activation when used in a feedback loop. More recent examples of training a generative machine by back-propagating into it include recent work on auto-encoding variational Bayes [20] and stochastic backpropagation [24].

What came back:

> An alternative to directed graphical models with latent variables is undirected graphical models with latent variables, such as restricted Boltzmann machines (RBMs) [27, 16], deep Boltzmann machines (DBMs) [26] and their many variants. The interactions within such models are represented as a product of unnormalized potential functions, normalized by a global summation/integration over all states of the random variables. This quantity ( *partition function* ) and its gradient are intractable for all but the most trivial cases, although they can be estimated using Markov chain Monte Carlo (MCMC) methods. Mixing poses a significant problem for learning algorithms dependent on MCMC [3, 5].
>
> Deep belief networks (DBNs) [16] are hybrid models containing a single undirected layer and many directed layers. Although a fast approximate layer-wise training criterion exists, DBNs must bear the computational difficulties associated with both undirected and directed models.
>
> Alternative criteria that neither approximate nor bound the log-likelihood have also been proposed, such as score matching [18] and noise-contrastive estimation (NCE) [13]. Both require the learned probability density to be specified analytically up to a normalization constant. Note that in many interesting generative models with multiple layers of latent variables (such as DBN and DBM), it is not even possible to derive a tractable unnormalized probability density. Some models such as denoising auto-encoders [30] and contractive autoencoders have learning rules very similar to score matching applied to RBM. In NCE, as in this work, a discriminative training criterion is used to fit a generative model. However, instead of fitting a separate discriminative model, the generative model itself is used to discriminate generated data from samples from a fixed noise distribution. Because NCE uses a fixed noise distribution, learning slows down significantly after the model has learned even a correct approximate distribution on a small subset of the observed variables.
>
> Finally, some techniques do not involve explicitly defining a probability distribution, but instead train a generative machine to draw samples from the desired distribution. This approach has the advantage that such machines can be designed to be trained by backpropagation. Notable recent work in this area includes the generative stochastic network (GSN) framework [5], an extension of generalized denoising auto-encoders [4]: both can be viewed as defining a parameterized Markov chain, that is, one learns the parameters of a machine that performs one step of a generative Markov chain. Compared to GSN, the adversarial nets framework does not require a Markov chain for sampling. Because adversarial nets do not require feedback loops during generation, they have the potential to make better use of piecewise linear units [19, 9, 10], which improve the performance of backpropagation but have problems with unbounded activations when used in a feedback loop. More recent examples of training a generative machine by backpropagating into itself include recent work on auto-encoding variational Bayes [20] and stochastic backpropagation [24].

### `content/vi/goodfellow-2014-gan/04_theoretical_results.md`

paper 86 of the canon, checked whole, translated by gpt-5, put back by gpt-5, judged by gpt-5. The fleet had nothing else free, so this is a model marking its own work.

- The original claims the minimax game has a global optimum at \(p_g=p_{\mathrm{data}}\), whereas the back-translation claims it has a global maximum there.
- The original says the discriminator’s optimum is reached “given \(G\),” whereas the back-translation says it is reached “with \(G\) given,” which is equivalent.
- The original proof concludes that \(p_g\) converges to \(p_x\), whereas the back-translation also says \(p_g\) converges to \(p_x\); however, this is a named-variable inconsistency already present in the original and therefore not a translation difference.
- The original says adversarial networks represent a limited family of \(p_g\) distributions, whereas the back-translation says they represent a finite family; “finite” is stronger than merely “limited.”

The English as it stands:

> The generator $G$ implicitly defines a probability distribution $p_g$ as the distribution of the samples $G(z)$ obtained when $z\sim p_z$. Therefore, we would like Algorithm 1 to converge to a good estimator of $p_{\mathrm{data}}$, if given enough capacity and training time. The results of this section are done in a non-parametric setting, e.g. we represent a model with infinite capacity by studying convergence in the space of probability density functions.
>
> We will show in section 4.1 that this minimax game has a global optimum for $p_g=p_{\mathrm{data}}$. We will then show in section 4.2 that Algorithm 1 optimizes Eq 1, thus obtaining the desired result.
>
> **Algorithm 1** Minibatch stochastic gradient descent training of generative adversarial nets. The number of steps to apply to the discriminator, $k$, is a hyperparameter. We used $k = 1$, the least expensive option in our experiments.
>
> **for** number of training iterations **do**
>
> **for** $k$ steps **do**
>
> - Sample minibatch of $m$ noise samples $\{z^{(1)}, \ldots, z^{(m)}\}$ from noise prior $p_g(z)$.
> - Sample minibatch of $m$ examples $\{x^{(1)}, \ldots, x^{(m)}\}$ from data generating distribution $p_{\text{data}}(x)$.
> - Update the discriminator by ascending its stochastic gradient:
>
> $$\nabla_{\theta_d}\frac{1}{m}\sum_{i=1}^{m}\left[\log D\left(x^{(i)}\right)+\log\left(1-D\left(G\left(z^{(i)}\right)\right)\right)\right].$$
>
> **end for**
>
> - Sample minibatch of $m$ noise samples $\{z^{(1)}, \ldots, z^{(m)}\}$ from noise prior $p_g(z)$.
> - Update the generator by descending its stochastic gradient:
>
> $$\nabla_{\theta_g}\frac{1}{m}\sum_{i=1}^{m}\log\left(1-D\left(G\left(z^{(i)}\right)\right)\right).$$
>
> **end for**
>
> The gradient-based updates can use any standard gradient-based learning rule. We used momentum in our experiments.
>
> ### 4.1 Global Optimality of $p_g = p_{\text{data}}$ {#goodfellow-2014-gan-s4-1 .section tag=00C7}
>
> We first consider the optimal discriminator $D$ for any given generator $G$.
>
> **Proposition 1.** *For $G$ fixed, the optimal discriminator $D$ is* {#goodfellow-2014-gan-prop-1 .statement tag=00C8}
>
> $$D_G^*(x)=\frac{p_{\text{data}}(x)}{p_{\text{data}}(x)+p_g(x)}\tag{2}$$
> {#goodfellow-2014-gan-eq-2 .equation tag=014B}
>
> *Proof.* The training criterion for the discriminator D, given any generator G, is to maximize the quantity $V(G,D)$
>
> $$\begin{aligned}
> V(G,D)&=\int_x p_{\text{data}}(x)\log(D(x))dx+\int_z p_z(z)\log(1-D(g(z)))dz\\
> &=\int_x p_{\text{data}}(x)\log(D(x))+p_g(x)\log(1-D(x))dx
> \end{aligned}\tag{3}$$
> {#goodfellow-2014-gan-eq-3 .equation tag=014C}
>
> For any $(a,b)\in\mathbb{R}^2\setminus\{0,0\}$, the function $y\rightarrow a\log(y)+b\log(1-y)$ achieves its maximum in $[0,1]$ at $\frac{a}{a+b}$. The discriminator does not need to be defined outside of $Supp(p_{\text{data}})\cup Supp(p_g)$, concluding the proof. $\square$
>
> Note that the training objective for $D$ can be interpreted as maximizing the log-likelihood for estimating the conditional probability $P(Y=y|x)$, where $Y$ indicates whether $x$ comes from $p_{\text{data}}$ (with $y=1$) or from $p_g$ (with $y=0$). The minimax game in Eq. 1 can now be reformulated as:
>
> $$\begin{aligned}
> C(G)&=\max_D V(G,D)\\
> &=\mathbb{E}_{x\sim p_{\text{data}}}\left[\log D_G^*(x)\right]+\mathbb{E}_{z\sim p_z}\left[\log(1-D_G^*(G(z)))\right]\\
> &=\mathbb{E}_{x\sim p_{\text{data}}}\left[\log D_G^*(x)\right]+\mathbb{E}_{x\sim p_g}\left[\log(1-D_G^*(x))\right]\\
> &=\mathbb{E}_{x\sim p_{\text{data}}}\left[\log\frac{p_{\text{data}}(x)}{p_{\text{data}}(x)+p_g(x)}\right]+\mathbb{E}_{x\sim p_g}\left[\log\frac{p_g(x)}{p_{\text{data}}(x)+p_g(x)}\right]
> \end{aligned}\tag{4}$$
> {#goodfellow-2014-gan-eq-4 .equation tag=014D}
>
> **Theorem 1.** *The global minimum of the virtual training criterion $C(G)$ is achieved if and only if $p_g = p_{\mathrm{data}}$. At that point, $C(G)$ achieves the value $-\log 4$.* {#goodfellow-2014-gan-thm-1 .statement tag=0111}
>
> *Proof.* For $p_g = p_{\mathrm{data}}$, $D_G^*(x) = \frac{1}{2}$, (consider Eq. 2). Hence, by inspecting Eq. 4 at $D_G^*(x) = \frac{1}{2}$, we find $C(G) = \log \frac{1}{2} + \log \frac{1}{2} = -\log 4$. To see that this is the best possible value of $C(G)$, reached only for $p_g = p_{\mathrm{data}}$, observe that
>
> $$\mathbb{E}_{x\sim p_{\mathrm{data}}}[-\log 2] + \mathbb{E}_{x\sim p_g}[-\log 2] = -\log 4$$
>
> and that by subtracting this expression from $C(G) = V(D_G^*, G)$, we obtain:
>
> $$C(G) = -\log(4) + KL\left(p_{\mathrm{data}} \left\| \frac{p_{\mathrm{data}} + p_g}{2}\right.\right) + KL\left(p_g \left\| \frac{p_{\mathrm{data}} + p_g}{2}\right.\right) \tag{5}$$
> {#goodfellow-2014-gan-eq-5 .equation tag=014E}
>
> where KL is the Kullback–Leibler divergence. We recognize in the previous expression the Jensen–Shannon divergence between the model’s distribution and the data generating process:
>
> $$C(G) = -\log(4) + 2 \cdot JSD(p_{\mathrm{data}} \| p_g) \tag{6}$$
> {#goodfellow-2014-gan-eq-6 .equation tag=014F}
>
> Since the Jensen–Shannon divergence between two distributions is always non-negative and zero only when they are equal, we have shown that $C^* = -\log(4)$ is the global minimum of $C(G)$ and that the only solution is $p_g = p_{\mathrm{data}}$, i.e., the generative model perfectly replicating the data generating process. $\square$
>
> ### 4.2 Convergence of Algorithm 1 {#goodfellow-2014-gan-s4-2 .section tag=0112}
>
> **Proposition 2.** *If $G$ and $D$ have enough capacity, and at each step of Algorithm 1, the discriminator is allowed to reach its optimum given $G$, and $p_g$ is updated so as to improve the criterion* {#goodfellow-2014-gan-prop-2 .statement tag=0113}
>
> $$\mathbb{E}_{x\sim p_{\mathrm{data}}}[\log D_G^*(x)] + \mathbb{E}_{x\sim p_g}[\log(1 - D_G^*(x))]$$
>
> *then $p_g$ converges to $p_{\mathrm{data}}$*
>
> *Proof.* Consider $V(G, D) = U(p_g, D)$ as a function of $p_g$ as done in the above criterion. Note that $U(p_g, D)$ is convex in $p_g$. The subderivatives of a supremum of convex functions include the derivative of the function at the point where the maximum is attained. In other words, if $f(x) = \sup_{\alpha\in\mathcal{A}} f_\alpha(x)$ and $f_\alpha(x)$ is convex in $x$ for every $\alpha$, then $\partial f_\beta(x) \in \partial f$ if $\beta = \arg \sup_{\alpha\in\mathcal{A}} f_\alpha(x)$. This is equivalent to computing a gradient descent update for $p_g$ at the optimal $D$ given the corresponding $G$. $\sup_D U(p_g, D)$ is convex in $p_g$ with a unique global optima as proven in Thm 1, therefore with sufficiently small updates of $p_g$, $p_g$ converges to $p_x$, concluding the proof. $\square$
>
> In practice, adversarial nets represent a limited family of $p_g$ distributions via the function $G(z; \theta_g)$, and we optimize $\theta_g$ rather than $p_g$ itself. Using a multilayer perceptron to define $G$ introduces multiple critical points in parameter space. However, the excellent performance of multilayer perceptrons in practice suggests that they are a reasonable model to use despite their lack of theoretical guarantees.

What came back:

> :::writing{variant="document" id="58321" title="English Translation"}
> The generator $G$ implicitly defines a probability distribution $p_g$ as the distribution of the samples $G(z)$ obtained when $z\sim p_z$. Therefore, we want Algorithm 1 to converge to a good estimator of $p_{\mathrm{data}}$, if provided with sufficient capacity and training time. The results of this section are carried out in the nonparametric setting, for example we represent a model with infinite capacity by studying convergence in the space of probability density functions.
>
> We will show in Section 4.1 that this minimax game has a global maximum at $p_g=p_{\mathrm{data}}$. Then, we will show in Section 4.2 that Algorithm 1 optimizes Eq 1, thereby obtaining the desired result.
>
> **Algorithm 1** Training adversarial networks by minibatch stochastic gradient descent. The number of steps applied to the discriminator, $k$, is a hyperparameter. We use $k = 1$, the least expensive choice in our experiments.
>
> **for** number of training iterations **do**
>
> **for** $k$ steps **do**
>
> - Sample a minibatch of $m$ noise samples $\{z^{(1)}, \ldots, z^{(m)}\}$ from the noise prior $p_g(z)$.
> - Sample a minibatch of $m$ examples $\{x^{(1)}, \ldots, x^{(m)}\}$ from the data-generating distribution $p_{\text{data}}(x)$.
> - Update the discriminator by ascending its stochastic gradient:
>
> $$\nabla_{\theta_d}\frac{1}{m}\sum_{i=1}^{m}\left[\log D\left(x^{(i)}\right)+\log\left(1-D\left(G\left(z^{(i)}\right)\right)\right)\right].$$
>
> **end for**
>
> - Sample a minibatch of $m$ noise samples $\{z^{(1)}, \ldots, z^{(m)}\}$ from the noise prior $p_g(z)$.
> - Update the generator by descending its stochastic gradient:
>
> $$\nabla_{\theta_g}\frac{1}{m}\sum_{i=1}^{m}\log\left(1-D\left(G\left(z^{(i)}\right)\right)\right).$$
>
> **end for**
>
> The gradient-based updates can use any standard gradient-based learning rule. We use momentum in our experiments.
>
> ### 4.1 Global Optimality of $p_g = p_{\text{data}}$ {#goodfellow-2014-gan-s4-1 .section tag=00C7}
>
> First, we consider the optimal discriminator $D$ for any given generator $G$.
>
> **Proposition 1.** *For fixed $G$, the optimal discriminator $D$ is* {#goodfellow-2014-gan-prop-1 .statement tag=00C8}
>
> $$D_G^*(x)=\frac{p_{\text{data}}(x)}{p_{\text{data}}(x)+p_g(x)}\tag{2}$$
> {#goodfellow-2014-gan-eq-2 .equation tag=014B}
>
> *Proof.* The training criterion for discriminator D, with any generator G, is to maximize the quantity $V(G,D)$
>
> $$\begin{aligned}
> V(G,D)&=\int_x p_{\text{data}}(x)\log(D(x))dx+\int_z p_z(z)\log(1-D(g(z)))dz\\
> &=\int_x p_{\text{data}}(x)\log(D(x))+p_g(x)\log(1-D(x))dx
> \end{aligned}\tag{3}$$
> {#goodfellow-2014-gan-eq-3 .equation tag=014C}
>
> For every $(a,b)\in\mathbb{R}^2\setminus\{0,0\}$, the function $y\rightarrow a\log(y)+b\log(1-y)$ achieves its maximum in $[0,1]$ at $\frac{a}{a+b}$. The discriminator does not need to be defined outside $Supp(p_{\text{data}})\cup Supp(p_g)$, completing the proof. $\square$
>
> The training criterion for $D$ can be interpreted as maximizing the log-likelihood to estimate the conditional probability $P(Y=y|x)$, where $Y$ indicates whether $x$ comes from $p_{\text{data}}$ (with $y=1$) or from $p_g$ (with $y=0$). The minimax game in Eq. 1 can now be rewritten as:
>
> $$\begin{aligned}
> C(G)&=\max_D V(G,D)\\
> &=\mathbb{E}_{x\sim p_{\text{data}}}\left[\log D_G^*(x)\right]+\mathbb{E}_{z\sim p_z}\left[\log(1-D_G^*(G(z)))\right]\\
> &=\mathbb{E}_{x\sim p_{\text{data}}}\left[\log D_G^*(x)\right]+\mathbb{E}_{x\sim p_g}\left[\log(1-D_G^*(x))\right]\\
> &=\mathbb{E}_{x\sim p_{\text{data}}}\left[\log\frac{p_{\text{data}}(x)}{p_{\text{data}}(x)+p_g(x)}\right]+\mathbb{E}_{x\sim p_g}\left[\log\frac{p_g(x)}{p_{\text{data}}(x)+p_g(x)}\right]
> \end{aligned}\tag{4}$$
> {#goodfellow-2014-gan-eq-4 .equation tag=014D}
>
> **Theorem 1.** *The global minimum of the virtual training criterion $C(G)$ is achieved if and only if $p_g = p_{\mathrm{data}}$. At that point, $C(G)$ achieves the value $-\log 4$.* {#goodfellow-2014-gan-thm-1 .statement tag=0111}
>
> *Proof.* With $p_g = p_{\mathrm{data}}$, $D_G^*(x) = \frac{1}{2}$, (consider Eq. 2). Therefore, by considering Eq. 4 at $D_G^*(x) = \frac{1}{2}$, we have $C(G) = \log \frac{1}{2} + \log \frac{1}{2} = -\log 4$. To see that this is the best possible value of $C(G)$, achieved only when $p_g = p_{\mathrm{data}}$, consider
>
> $$\mathbb{E}_{x\sim p_{\mathrm{data}}}[-\log 2] + \mathbb{E}_{x\sim p_g}[-\log 2] = -\log 4$$
>
> and by subtracting this expression from $C(G) = V(D_G^*, G)$, we obtain:
>
> $$C(G) = -\log(4) + KL\left(p_{\mathrm{data}} \left\| \frac{p_{\mathrm{data}} + p_g}{2}\right.\right) + KL\left(p_g \left\| \frac{p_{\mathrm{data}} + p_g}{2}\right.\right) \tag{5}$$
> {#goodfellow-2014-gan-eq-5 .equation tag=014E}
>
> where KL is the Kullback–Leibler divergence. In the above expression, we recognize the Jensen–Shannon divergence between the model distribution and the data-generating process:
>
> $$C(G) = -\log(4) + 2 \cdot JSD(p_{\mathrm{data}} \| p_g) \tag{6}$$
> {#goodfellow-2014-gan-eq-6 .equation tag=014F}
>
> Since the Jensen–Shannon divergence between two distributions is always non-negative and is equal to zero only when they are equal, we have proved that $C^* = -\log(4)$ is the global minimum of $C(G)$ and the unique solution is $p_g = p_{\mathrm{data}}$, that is, the generative model perfectly reproduces the data-generating process. $\square$
>
> ### 4.2 Convergence of Algorithm 1 {#goodfellow-2014-gan-s4-2 .section tag=0112}
>
> **Proposition 2.** *If $G$ and $D$ have sufficient capacity, and at each step of Algorithm 1, the discriminator is allowed to reach its optimum with $G$ given, and $p_g$ is updated so as to improve the criterion* {#goodfellow-2014-gan-prop-2 .statement tag=0113}
>
> $$\mathbb{E}_{x\sim p_{\mathrm{data}}}[\log D_G^*(x)] + \mathbb{E}_{x\sim p_g}[\log(1 - D_G^*(x))]$$
>
> *then $p_g$ converges to $p_{\mathrm{data}}$*
>
> *Proof.* Consider $V(G, D) = U(p_g, D)$ as a function of $p_g$ in the way done in the above criterion. Note that $U(p_g, D)$ is a convex function in $p_g$. The subderivatives of a supremum of convex functions include the derivative of the function at the point achieving the maximum. In other words, if $f(x) = \sup_{\alpha\in\mathcal{A}} f_\alpha(x)$ and $f_\alpha(x)$ is convex in $x$ for every $\alpha$, then $\partial f_\beta(x) \in \partial f$ if $\beta = \arg \sup_{\alpha\in\mathcal{A}} f_\alpha(x)$. This is equivalent to calculating a gradient descent update for $p_g$ at the optimal $D$ corresponding to the corresponding $G$. $\sup_D U(p_g, D)$ is convex in $p_g$ with a unique global extremum as proved in Theorem 1, therefore with sufficiently small $p_g$ updates, $p_g$ converges to $p_x$, completing the proof. $\square$
>
> In practice, adversarial networks represent a finite family of distributions $p_g$ through the function $G(z; \theta_g)$, and we optimize $\theta_g$ instead of $p_g$ itself. The use of multilayer perceptrons to define $G$ introduces many critical points in the parameter space. However, the excellent performance of multilayer perceptrons in practice shows that they are a reasonable model to use despite the lack of theoretical guarantees.
>
> =====

### `content/vi/goodfellow-2014-gan/05_experiments.md`

paper 86 of the canon, checked whole, translated by gpt-5, put back by gpt-5, judged by gpt-5. The fleet had nothing else free, so this is a model marking its own work.

- The original says the samples are “not cherry-picked,” whereas the back-translation says they are “not selected,” which is only a slight wording difference and preserves the claim.
- The original says the samples are at least competitive with “the better generative models in the literature,” whereas the back-translation says they are competitive with “better generative models,” which slightly blurs the comparison but does not materially change it.
- The original says Parzen likelihood estimation “may be approximated” for the relevant models in Table 2, whereas the back-translation says it “can be approximated,” strengthening the modality from possibility to capability.
- The original says any differentiable function is “theoretically permitted” for model design, whereas the back-translation says any differentiable function is “allowed in theory,” preserving the claim.

The English as it stands:

> We trained adversarial nets on a range of datasets including MNIST[[lecun-1998-lenet]], the Toronto Face Database (TFD) [28], and CIFAR-10 [21]. The generator nets used a mixture of rectifier linear activations [19, 9] and sigmoid activations, while the discriminator net used maxout [10] activations. Dropout [17] was applied in training the discriminator net. While our theoretical framework permits the use of dropout and other noise at intermediate layers of the generator, we used noise as the input to only the bottommost layer of the generator network.
>
> We estimate probability of the test set data under $p_g$ by fitting a Gaussian Parzen window to the samples generated with $G$ and reporting the log-likelihood under this distribution. The $\sigma$ parameter
>
> | Model | MNIST | TFD |
> |---|---|---|
> | DBN [3] | $138 \pm 2$ | $1909 \pm 66$ |
> | Stacked CAE [3] | $121 \pm 1.6$ | $\mathbf{2110 \pm 50}$ |
> | Deep GSN [6] | $214 \pm 1.1$ | $1890 \pm 29$ |
> | Adversarial nets | $\mathbf{225 \pm 2}$ | $\mathbf{2057 \pm 26}$ |
>
> Table 1: Parzen window-based log-likelihood estimates. The reported numbers on MNIST are the mean log-likelihood of samples on test set, with the standard error of the mean computed across examples. On TFD, we computed the standard error across folds of the dataset, with a different $\sigma$ chosen using the validation set of each fold. On TFD, $\sigma$ was cross validated on each fold and mean log-likelihood on each fold were computed. For MNIST we compare against other models of the real-valued (rather than binary) version of dataset. {#goodfellow-2014-gan-tab-1 .table tag=00CA}
>
> of the Gaussians was obtained by cross validation on the validation set. This procedure was introduced in Breuleux *et al.* [8] and used for various generative models for which the exact likelihood is not tractable [25, 3, 5]. Results are reported in Table 1. This method of estimating the likelihood has somewhat high variance and does not perform well in high dimensional spaces but it is the best method available to our knowledge. Advances in generative models that can sample but not estimate likelihood directly motivate further research on how to evaluate such models.
>
> In Figures 2 and 3 we show samples drawn from the generator net after training. While we make no claim that these samples are better than samples generated by existing methods, we believe that these samples are at least competitive with the better generative models in the literature and highlight the potential of the adversarial framework.
>
> Figure 2: Visualization of samples from the model. Rightmost column shows the nearest training example of the neighboring sample, in order to demonstrate that the model has not memorized the training set. Samples are fair random draws, not cherry-picked. Unlike most other visualizations of deep generative models, these images show actual samples from the model distributions, not conditional means given samples of hidden units. Moreover, these samples are uncorrelated because the sampling process does not depend on Markov chain mixing. a) MNIST b) TFD c) CIFAR-10 (fully connected model) d) CIFAR-10 (convolutional discriminator and “deconvolutional” generator) {#goodfellow-2014-gan-fig-2 .figure tag=00CB}
>
> Figure 3: Digits obtained by linearly interpolating between coordinates in $z$ space of the full model. {#goodfellow-2014-gan-fig-3 .figure tag=00CC}
>
> |  | Deep directed graphical models | Deep undirected graphical models | Generative autoencoders | Adversarial models |
> |---|---|---|---|---|
> | Training | Inference needed during training. | Inference needed during training. MCMC needed to approximate partition function gradient. | Enforced tradeoff between mixing and power of reconstruction generation | Synchronizing the discriminator with the generator. Helvetica. |
> | Inference | Learned approximate inference | Variational inference | MCMC-based inference | Learned approximate inference |
> | Sampling | No difficulties | Requires Markov chain | Requires Markov chain | No difficulties |
> | Evaluating $p(x)$ | Intractable, may be approximated with AIS | Intractable, may be approximated with AIS | Not explicitly represented, may be approximated with Parzen density estimation | Not explicitly represented, may be approximated with Parzen density estimation |
> | Model design | Nearly all models incur extreme difficulty | Careful design needed to ensure multiple properties | Any differentiable function is theoretically permitted | Any differentiable function is theoretically permitted |
>
> Table 2: Challenges in generative modeling: a summary of the difficulties encountered by different approaches to deep generative modeling for each of the major operations involving a model. {#goodfellow-2014-gan-tab-2 .table tag=00CD}

What came back:

> We trained adversarial networks on a variety of datasets, including MNIST[[lecun-1998-lenet]], Toronto Face Database (TFD) [28] and CIFAR-10 [21]. The generative networks use a combination of rectified linear activation functions [19, 9] and sigmoid activation functions, while the discriminative network uses maxout activation functions [10]. Dropout [17] is applied during training of the discriminative network. Although our theoretical framework allows the use of dropout and other noise at intermediate layers of the generator, we only use noise as input to the lowest layer of the generator network.
>
> We estimate the probability of test set data under $p_g$ by fitting a Gaussian Parzen window to the samples generated by $G$ and report the log-likelihood under this distribution. The parameter $\sigma$
>
> | Model | MNIST | TFD |
> |---|---|---|
> | DBN [3] | $138 \pm 2$ | $1909 \pm 66$ |
> | Stacked CAE [3] | $121 \pm 1.6$ | $\mathbf{2110 \pm 50}$ |
> | Deep GSN [6] | $214 \pm 1.1$ | $1890 \pm 29$ |
> | Adversarial net | $\mathbf{225 \pm 2}$ | $\mathbf{2057 \pm 26}$ |
>
> Table 1: Log-likelihood estimates based on Parzen windows. The numbers reported on MNIST are the average log-likelihood of the samples on the test set, with the standard error of the mean computed over the examples. On TFD, we compute the standard error over the folds of the dataset, with a different $\sigma$ selected by the validation set of each fold. On TFD, $\sigma$ is cross-validated on each fold and the average log-likelihood over each fold is computed. For MNIST, we compare with other models of the version of the dataset with real values (rather than binary). {#goodfellow-2014-gan-tab-1 .table tag=00CA}
>
> of the Gaussians is determined by cross-validation on the validation set. This procedure is introduced in Breuleux *et al.* [8] and is used for many different generative models for which exact likelihood is not tractable [25, 3, 5]. The results are reported in Table 1. This likelihood estimation method has relatively high variance and does not work well in spaces with high dimensionality, but to our knowledge, this is the best method currently available. Advances in generative models that can sample but cannot directly estimate likelihood motivate further research on how to evaluate such models.
>
> In Figures 2 and 3, we present samples drawn from the generator network after training. Although we do not claim that these samples are better than the samples generated by existing methods, we believe that these samples are at least competitive with better generative models in the literature and highlight the potential of the adversarial framework.
>
> Figure 2: Visualization of samples from the model. The far right column shows the nearest training example of the neighboring sample, to demonstrate that the model does not memorize the training set. The samples are fair random draws, not selected. Unlike most other visualizations of deep generative models, these images show actual samples from the model distributions, rather than conditional means given samples of the hidden units. Furthermore, these samples are uncorrelated because the sampling process does not depend on the mixing of a Markov chain. a) MNIST b) TFD c) CIFAR-10 (fully connected model) d) CIFAR-10 (convolutional discriminator and “deconvolutional” generator) {#goodfellow-2014-gan-fig-2 .figure tag=00CB}
>
> Figure 3: Digits obtained by linearly interpolating between coordinates in the $z$ space of the full model. {#goodfellow-2014-gan-fig-3 .figure tag=00CC}
>
> |  | Directed deep graph models | Undirected deep graph models | Generative autoencoder | Adversarial models |
> |---|---|---|---|---|
> | Training | Inference is needed during training. | Inference is needed during training. MCMC is needed to approximate the gradient of the partition function. | Imposes a tradeoff between mixing and capacity of the generative reconstruction process | Synchronize the discriminator with the generator. Helvetica. |
> | Inference | Learned approximate inference | Variational inference | MCMC-based inference | Learned approximate inference |
> | Sampling | No difficulty | Requires a Markov chain | Requires a Markov chain | No difficulty |
> | Evaluating $p(x)$ | Intractable, can be approximated by AIS | Intractable, can be approximated by AIS | Not explicitly represented, can be approximated by Parzen density estimation | Not explicitly represented, can be approximated by Parzen density estimation |
> | Model design | Nearly all models encounter extremely great difficulty | Careful design is needed to ensure many properties | In theory, any differentiable function is allowed | In theory, any differentiable function is allowed |
>
> Table 2: Challenges in generative modeling: summary of the difficulties encountered by different approaches to deep generative modeling for each main operation involved in a model. {#goodfellow-2014-gan-tab-2 .table tag=00CD}

### `content/vi/goodfellow-2014-gan/07_conclusions_and_future_work.md`

paper 86 of the canon, checked whole, translated by gpt-5, put back by gpt-5, judged by gpt-5. The fleet had nothing else free, so this is a model marking its own work.

- The original says the research directions “could prove useful,” whereas the back-translation says they “can be useful,” changing a hedged possibility into a more definite claim.

The English as it stands:

> This framework admits many straightforward extensions:
>
> 1. A *conditional* generative model $p(\mathbf{x}\mid\mathbf{c})$ can be obtained by adding $\mathbf{c}$ as input to both $G$ and $D$.
> 2. *Learned approximate inference* can be performed by training an auxiliary network to predict $\mathbf{z}$ given $\mathbf{x}$. This is similar to the inference net trained by the wake-sleep algorithm [15] but with the advantage that the inference net may be trained for a fixed generator net after the generator net has finished training.
>
> 3. One can approximately model all conditionals $p(x_S \mid x_{\not S})$ where $S$ is a subset of the indices of $x$ by training a family of conditional models that share parameters. Essentially, one can use adversarial nets to implement a stochastic extension of the deterministic MP-DBM [11].
> 4. *Semi-supervised learning:* features from the discriminator or inference net could improve performance of classifiers when limited labeled data is available.
> 5. *Efficiency improvements:* training could be accelerated greatly by divising better methods for coordinating $G$ and $D$ or determining better distributions to sample $z$ from during training.
>
> This paper has demonstrated the viability of the adversarial modeling framework, suggesting that these research directions could prove useful.

What came back:

> This framework allows several simple extensions:
>
> 1. A *conditional* generative model $p(\mathbf{x}\mid\mathbf{c})$ can be obtained by adding $\mathbf{c}$ as an input to both $G$ and $D$.
> 2. It is possible to perform *learned approximate inference* by training an auxiliary network to predict $\mathbf{z}$ when given $\mathbf{x}$. This is similar to the inference network trained by the wake-sleep algorithm [15], but has the advantage that the inference network can be trained with a fixed generative network after the generative network has completed its training.
>
> 3. It is possible to approximate modeling all conditional distributions $p(x_S \mid x_{\not S})$ in which $S$ is a subset of the indices of $x$, by training a family of conditional models sharing parameters. Basically, adversarial networks can be used to implement a stochastic extension of the deterministic MP-DBM [11].
> 4. *Semi-supervised learning:* features from the discriminator or inference network can improve the performance of classifiers when limited labeled data are available.
> 5. *Efficiency improvement:* the training process can be accelerated significantly by constructing better methods to coordinate $G$ and $D$ or determining better distributions for sampling $z$ during training.
>
> This paper has demonstrated the feasibility of the adversarial modeling framework, showing that these research directions can be useful.

### `content/zh/goodfellow-2014-gan/01_introduction.md`

paper 86 of the canon, checked whole, translated by gpt-5, put back by gpt-5, judged by gpt-5. The fleet had nothing else free, so this is a model marking its own work.

- The original says the deep-learning successes use piecewise linear units with a particularly well-behaved gradient, while the back-translation says their gradients merely have particularly good properties, which slightly weakens the specific claim.
- The original says deep generative models have had less impact partly because of difficulty approximating many intractable probabilistic computations arising in maximum likelihood estimation and related strategies, while the back-translation says there is difficulty approximating maximum likelihood estimation itself and the many intractable probability calculations arising in related strategies, changing what is described as difficult to approximate.
- The original calls the framework “adversarial nets,” while the back-translation calls it “adversarial network” and later says “an adversarial network” for the special case; this changes the named term from the paper’s plural name to a singular one.
- The original footnote [^3] says Yoshua Bengio is a “CIFAR Senior Fellow,” while the back-translation says he is a “CIFAR Senior Researcher.”
- The original says all code and hyperparameters are available at the specified GitHub URL, while the back-translation gives a corrupted and substantially altered rendering of that URL rather than the same usable link.

The English as it stands:

> The promise of deep learning is to discover rich, hierarchical models [2] that represent probability distributions over the kinds of data encountered in artificial intelligence applications, such as natural images, audio waveforms containing speech, and symbols in natural language corpora. So far, the most striking successes in deep learning have involved discriminative models, usually those that map a high-dimensional, rich sensory input to a class label [14], [[krizhevsky-2012-imagenet]]. These striking successes have primarily been based on the backpropagation and dropout algorithms, using piecewise linear units [19, 9, 10] which have a particularly well-behaved gradient . Deep *generative* models have had less of an impact, due to the difficulty of approximating many intractable probabilistic computations that arise in maximum likelihood estimation and related strategies, and due to difficulty of leveraging the benefits of piecewise linear units in the generative context. We propose a new generative model estimation procedure that sidesteps these difficulties. [^4]
>
> In the proposed *adversarial nets* framework, the generative model is pitted against an adversary: a discriminative model that learns to determine whether a sample is from the model distribution or the data distribution. The generative model can be thought of as analogous to a team of counterfeiters, trying to produce fake currency and use it without detection, while the discriminative model is analogous to the police, trying to detect the counterfeit currency. Competition in this game drives both teams to improve their methods until the counterfeits are indistinguishable from the genuine articles.
>
> [^1]: Jean Pouget-Abadie is visiting Université de Montréal from Ecole Polytechnique.
> [^2]: Sherjil Ozair is visiting Université de Montréal from Indian Institute of Technology Delhi
> [^3]: Yoshua Bengio is a CIFAR Senior Fellow.
> [^4]: All code and hyperparameters available at http://www.github.com/goodfeli/adversarial
>
> This framework can yield specific training algorithms for many kinds of model and optimization algorithm. In this article, we explore the special case when the generative model generates samples by passing random noise through a multilayer perceptron, and the discriminative model is also a multilayer perceptron. We refer to this special case as *adversarial nets*. In this case, we can train both models using only the highly successful backpropagation and dropout algorithms [17] and sample from the generative model using only forward propagation. No approximate inference or Markov chains are necessary.

What came back:

> The prospect of deep learning lies in discovering rich, hierarchical models[2], which represent probability distributions over various types of data encountered in artificial intelligence applications, such as natural images, audio waveforms containing speech, and symbols in natural language corpora. So far, the most striking successes of deep learning have mainly come from discriminative models, usually models that map high-dimensional, rich perceptual inputs to class labels[14], [[krizhevsky-2012-imagenet]]. These remarkable successes have mainly been built on backpropagation and Dropout algorithms, using piecewise linear units[19, 9, 10], whose gradients have particularly good properties. The impact of deep *generative* models has been smaller, due to the difficulty of approximating maximum likelihood estimation and the many intractable probability calculations that arise in related strategies, and also due to the difficulty of exploiting the advantages of piecewise linear units in the generative setting. We propose a new generative model estimation procedure that bypasses these difficulties.[^4]
>
> In the proposed *adversarial network* framework, a generative model is set against an opponent: a discriminative model that learns to determine whether a sample comes from the model distribution or the data distribution. The generative model can be viewed as a group of counterfeiters, trying to manufacture and use fake currency without being discovered; while the discriminative model is like the police, trying to identify counterfeit currency. The competition in this game drives both sides to continuously improve their respective methods, until the forgeries cannot be distinguished from the genuine articles.
>
> [^1]: Jean Pouget-Abadie is visiting the University of Montreal from Ecole Polytechnique.
> [^2]: Sherjil Ozair is visiting the University of Montreal from Indian Institute of Technology Delhi
> [^3]: Yoshua Bengio is a CIFAR Senior Researcher.
> [^4]: All code and hyperparameters can be found at [[http://www.github.com/goodfeli/adversarial\](http://www.github.com/goodfeli/adversarial)获得](http://www.github.com/goodfeli/adversarial]\(http://www.github.com/goodfeli/adversarial\)获得)
>
> The framework can derive specific training algorithms for many types of models and optimization algorithms. This paper explores a special case: the generative model generates samples by passing random noise into a multilayer perceptron, and the discriminative model is also a multilayer perceptron. We call this special case an *adversarial network*. In this case, we only need to use the extremely successful backpropagation and Dropout algorithms[17] to train the two models, and only forward propagation is needed to sample from the generative model. Approximate inference or Markov chains are not needed.

### `content/zh/goodfellow-2014-gan/04_theoretical_results.md`

paper 86 of the canon, checked whole, translated by gpt-5, put back by gpt-5, judged by gpt-5. The fleet had nothing else free, so this is a model marking its own work.

- The original says that with sufficiently small updates of \(p_g\), \(p_g\) converges to \(p_x\), while the back-translation likewise says it converges to \(p_x\); however, the surrounding theorem establishes the unique optimum as \(p_g=p_{\mathrm{data}}\), so the unchanged \(p_x\) appears to be a source-text inconsistency rather than a translation difference.

The English as it stands:

> The generator $G$ implicitly defines a probability distribution $p_g$ as the distribution of the samples $G(z)$ obtained when $z\sim p_z$. Therefore, we would like Algorithm 1 to converge to a good estimator of $p_{\mathrm{data}}$, if given enough capacity and training time. The results of this section are done in a non-parametric setting, e.g. we represent a model with infinite capacity by studying convergence in the space of probability density functions.
>
> We will show in section 4.1 that this minimax game has a global optimum for $p_g=p_{\mathrm{data}}$. We will then show in section 4.2 that Algorithm 1 optimizes Eq 1, thus obtaining the desired result.
>
> **Algorithm 1** Minibatch stochastic gradient descent training of generative adversarial nets. The number of steps to apply to the discriminator, $k$, is a hyperparameter. We used $k = 1$, the least expensive option in our experiments.
>
> **for** number of training iterations **do**
>
> **for** $k$ steps **do**
>
> - Sample minibatch of $m$ noise samples $\{z^{(1)}, \ldots, z^{(m)}\}$ from noise prior $p_g(z)$.
> - Sample minibatch of $m$ examples $\{x^{(1)}, \ldots, x^{(m)}\}$ from data generating distribution $p_{\text{data}}(x)$.
> - Update the discriminator by ascending its stochastic gradient:
>
> $$\nabla_{\theta_d}\frac{1}{m}\sum_{i=1}^{m}\left[\log D\left(x^{(i)}\right)+\log\left(1-D\left(G\left(z^{(i)}\right)\right)\right)\right].$$
>
> **end for**
>
> - Sample minibatch of $m$ noise samples $\{z^{(1)}, \ldots, z^{(m)}\}$ from noise prior $p_g(z)$.
> - Update the generator by descending its stochastic gradient:
>
> $$\nabla_{\theta_g}\frac{1}{m}\sum_{i=1}^{m}\log\left(1-D\left(G\left(z^{(i)}\right)\right)\right).$$
>
> **end for**
>
> The gradient-based updates can use any standard gradient-based learning rule. We used momentum in our experiments.
>
> ### 4.1 Global Optimality of $p_g = p_{\text{data}}$ {#goodfellow-2014-gan-s4-1 .section tag=00C7}
>
> We first consider the optimal discriminator $D$ for any given generator $G$.
>
> **Proposition 1.** *For $G$ fixed, the optimal discriminator $D$ is* {#goodfellow-2014-gan-prop-1 .statement tag=00C8}
>
> $$D_G^*(x)=\frac{p_{\text{data}}(x)}{p_{\text{data}}(x)+p_g(x)}\tag{2}$$
> {#goodfellow-2014-gan-eq-2 .equation tag=014B}
>
> *Proof.* The training criterion for the discriminator D, given any generator G, is to maximize the quantity $V(G,D)$
>
> $$\begin{aligned}
> V(G,D)&=\int_x p_{\text{data}}(x)\log(D(x))dx+\int_z p_z(z)\log(1-D(g(z)))dz\\
> &=\int_x p_{\text{data}}(x)\log(D(x))+p_g(x)\log(1-D(x))dx
> \end{aligned}\tag{3}$$
> {#goodfellow-2014-gan-eq-3 .equation tag=014C}
>
> For any $(a,b)\in\mathbb{R}^2\setminus\{0,0\}$, the function $y\rightarrow a\log(y)+b\log(1-y)$ achieves its maximum in $[0,1]$ at $\frac{a}{a+b}$. The discriminator does not need to be defined outside of $Supp(p_{\text{data}})\cup Supp(p_g)$, concluding the proof. $\square$
>
> Note that the training objective for $D$ can be interpreted as maximizing the log-likelihood for estimating the conditional probability $P(Y=y|x)$, where $Y$ indicates whether $x$ comes from $p_{\text{data}}$ (with $y=1$) or from $p_g$ (with $y=0$). The minimax game in Eq. 1 can now be reformulated as:
>
> $$\begin{aligned}
> C(G)&=\max_D V(G,D)\\
> &=\mathbb{E}_{x\sim p_{\text{data}}}\left[\log D_G^*(x)\right]+\mathbb{E}_{z\sim p_z}\left[\log(1-D_G^*(G(z)))\right]\\
> &=\mathbb{E}_{x\sim p_{\text{data}}}\left[\log D_G^*(x)\right]+\mathbb{E}_{x\sim p_g}\left[\log(1-D_G^*(x))\right]\\
> &=\mathbb{E}_{x\sim p_{\text{data}}}\left[\log\frac{p_{\text{data}}(x)}{p_{\text{data}}(x)+p_g(x)}\right]+\mathbb{E}_{x\sim p_g}\left[\log\frac{p_g(x)}{p_{\text{data}}(x)+p_g(x)}\right]
> \end{aligned}\tag{4}$$
> {#goodfellow-2014-gan-eq-4 .equation tag=014D}
>
> **Theorem 1.** *The global minimum of the virtual training criterion $C(G)$ is achieved if and only if $p_g = p_{\mathrm{data}}$. At that point, $C(G)$ achieves the value $-\log 4$.* {#goodfellow-2014-gan-thm-1 .statement tag=0111}
>
> *Proof.* For $p_g = p_{\mathrm{data}}$, $D_G^*(x) = \frac{1}{2}$, (consider Eq. 2). Hence, by inspecting Eq. 4 at $D_G^*(x) = \frac{1}{2}$, we find $C(G) = \log \frac{1}{2} + \log \frac{1}{2} = -\log 4$. To see that this is the best possible value of $C(G)$, reached only for $p_g = p_{\mathrm{data}}$, observe that
>
> $$\mathbb{E}_{x\sim p_{\mathrm{data}}}[-\log 2] + \mathbb{E}_{x\sim p_g}[-\log 2] = -\log 4$$
>
> and that by subtracting this expression from $C(G) = V(D_G^*, G)$, we obtain:
>
> $$C(G) = -\log(4) + KL\left(p_{\mathrm{data}} \left\| \frac{p_{\mathrm{data}} + p_g}{2}\right.\right) + KL\left(p_g \left\| \frac{p_{\mathrm{data}} + p_g}{2}\right.\right) \tag{5}$$
> {#goodfellow-2014-gan-eq-5 .equation tag=014E}
>
> where KL is the Kullback–Leibler divergence. We recognize in the previous expression the Jensen–Shannon divergence between the model’s distribution and the data generating process:
>
> $$C(G) = -\log(4) + 2 \cdot JSD(p_{\mathrm{data}} \| p_g) \tag{6}$$
> {#goodfellow-2014-gan-eq-6 .equation tag=014F}
>
> Since the Jensen–Shannon divergence between two distributions is always non-negative and zero only when they are equal, we have shown that $C^* = -\log(4)$ is the global minimum of $C(G)$ and that the only solution is $p_g = p_{\mathrm{data}}$, i.e., the generative model perfectly replicating the data generating process. $\square$
>
> ### 4.2 Convergence of Algorithm 1 {#goodfellow-2014-gan-s4-2 .section tag=0112}
>
> **Proposition 2.** *If $G$ and $D$ have enough capacity, and at each step of Algorithm 1, the discriminator is allowed to reach its optimum given $G$, and $p_g$ is updated so as to improve the criterion* {#goodfellow-2014-gan-prop-2 .statement tag=0113}
>
> $$\mathbb{E}_{x\sim p_{\mathrm{data}}}[\log D_G^*(x)] + \mathbb{E}_{x\sim p_g}[\log(1 - D_G^*(x))]$$
>
> *then $p_g$ converges to $p_{\mathrm{data}}$*
>
> *Proof.* Consider $V(G, D) = U(p_g, D)$ as a function of $p_g$ as done in the above criterion. Note that $U(p_g, D)$ is convex in $p_g$. The subderivatives of a supremum of convex functions include the derivative of the function at the point where the maximum is attained. In other words, if $f(x) = \sup_{\alpha\in\mathcal{A}} f_\alpha(x)$ and $f_\alpha(x)$ is convex in $x$ for every $\alpha$, then $\partial f_\beta(x) \in \partial f$ if $\beta = \arg \sup_{\alpha\in\mathcal{A}} f_\alpha(x)$. This is equivalent to computing a gradient descent update for $p_g$ at the optimal $D$ given the corresponding $G$. $\sup_D U(p_g, D)$ is convex in $p_g$ with a unique global optima as proven in Thm 1, therefore with sufficiently small updates of $p_g$, $p_g$ converges to $p_x$, concluding the proof. $\square$
>
> In practice, adversarial nets represent a limited family of $p_g$ distributions via the function $G(z; \theta_g)$, and we optimize $\theta_g$ rather than $p_g$ itself. Using a multilayer perceptron to define $G$ introduces multiple critical points in parameter space. However, the excellent performance of multilayer perceptrons in practice suggests that they are a reasonable model to use despite their lack of theoretical guarantees.

What came back:

> The generator $G$ implicitly defines a probability distribution $p_g$ as the distribution of samples $G(z)$ obtained when $z\sim p_z$. Therefore, given sufficient capacity and training time, we hope that Algorithm 1 can converge to a good estimator of $p_{\mathrm{data}}$. The results in this section are obtained in the nonparametric setting, for example, we represent models with infinite capacity by studying convergence in the space of probability density functions.
>
> We will prove in Section 4.1 that when $p_g=p_{\mathrm{data}}$, the minimax game has a global optimum. Subsequently, we will prove in Section 4.2 that Algorithm 1 optimizes Equation 1, thereby obtaining the desired result.
>
> **Algorithm 1** Minibatch stochastic gradient descent training of generative adversarial networks. The number of steps $k$ applied to the discriminator is a hyperparameter. In our experiments $k = 1$ was used, which is the least costly choice.
>
> **for** number of training iterations **do**
>
> **for** $k$ steps **do**
>
> - Sample a minibatch of $m$ noise samples $\{z^{(1)}, \ldots, z^{(m)}\}$ from the noise prior $p_g(z)$.
> - Sample a minibatch of $m$ samples $\{x^{(1)}, \ldots, x^{(m)}\}$ from the data generating distribution $p_{\text{data}}(x)$.
> - Update the discriminator by ascending along its stochastic gradient:
>
> $$\nabla_{\theta_d}\frac{1}{m}\sum_{i=1}^{m}\left[\log D\left(x^{(i)}\right)+\log\left(1-D\left(G\left(z^{(i)}\right)\right)\right)\right].$$
>
> **end for**
>
> - Sample a minibatch of $m$ noise samples $\{z^{(1)}, \ldots, z^{(m)}\}$ from the noise prior $p_g(z)$.
> - Update the generator by descending along its stochastic gradient:
>
> $$\nabla_{\theta_g}\frac{1}{m}\sum_{i=1}^{m}\log\left(1-D\left(G\left(z^{(i)}\right)\right)\right).$$
>
> **end for**
>
> The gradient-based updates can use any standard gradient-based learning rule. Momentum was used in our experiments.
>
> ### 4.1 Global optimality of $p_g = p_{\text{data}}$ {#goodfellow-2014-gan-s4-1 .section tag=00C7}
>
> We first consider the optimal discriminator $D$ corresponding to any given generator $G$.
>
> **Proposition 1.** *For fixed $G$, the optimal discriminator $D$ is* {#goodfellow-2014-gan-prop-1 .statement tag=00C8}
>
> $$D_G^*(x)=\frac{p_{\text{data}}(x)}{p_{\text{data}}(x)+p_g(x)}\tag{2}$$
> {#goodfellow-2014-gan-eq-2 .equation tag=014B}
>
> *Proof.* Given any generator G, the training criterion for the discriminator D is to maximize the quantity $V(G,D)$
>
> $$\begin{aligned}
> V(G,D)&=\int_x p_{\text{data}}(x)\log(D(x))dx+\int_z p_z(z)\log(1-D(g(z)))dz\\
> &=\int_x p_{\text{data}}(x)\log(D(x))+p_g(x)\log(1-D(x))dx
> \end{aligned}\tag{3}$$
> {#goodfellow-2014-gan-eq-3 .equation tag=014C}
>
> For any $(a,b)\in\mathbb{R}^2\setminus\{0,0\}$, the function $y\rightarrow a\log(y)+b\log(1-y)$ attains its maximum on the interval $[0,1]$ at $\frac{a}{a+b}$. The discriminator need not be defined outside $Supp(p_{\text{data}})\cup Supp(p_g)$, completing the proof. $\square$
>
> Notice that the training objective of $D$ can be interpreted as maximizing the log-likelihood for estimating the conditional probability $P(Y=y|x)$, where $Y$ indicates whether $x$ comes from $p_{\text{data}}$ (in which case $y=1$) or from $p_g$ (in which case $y=0$). The minimax game in Equation 1 can now be rewritten as:
>
> $$\begin{aligned}
> C(G)&=\max_D V(G,D)\\
> &=\mathbb{E}_{x\sim p_{\text{data}}}\left[\log D_G^*(x)\right]+\mathbb{E}_{z\sim p_z}\left[\log(1-D_G^*(G(z)))\right]\\
> &=\mathbb{E}_{x\sim p_{\text{data}}}\left[\log D_G^*(x)\right]+\mathbb{E}_{x\sim p_g}\left[\log(1-D_G^*(x))\right]\\
> &=\mathbb{E}_{x\sim p_{\text{data}}}\left[\log\frac{p_{\text{data}}(x)}{p_{\text{data}}(x)+p_g(x)}\right]+\mathbb{E}_{x\sim p_g}\left[\log\frac{p_g(x)}{p_{\text{data}}(x)+p_g(x)}\right]
> \end{aligned}\tag{4}$$
> {#goodfellow-2014-gan-eq-4 .equation tag=014D}
>
> **Theorem 1.** *The global minimum of the virtual training criterion $C(G)$ is achieved if and only if $p_g = p_{\mathrm{data}}$. At this time, $C(G)$ takes the value $-\log 4$.* {#goodfellow-2014-gan-thm-1 .statement tag=0111}
>
> *Proof.* When $p_g = p_{\mathrm{data}}$, $D_G^*(x) = \frac{1}{2}$ (see Equation 2). Therefore, considering Equation 4 when $D_G^*(x) = \frac{1}{2}$, we obtain $C(G) = \log \frac{1}{2} + \log \frac{1}{2} = -\log 4$. To show that this is the best value that $C(G)$ can achieve, and that it is achieved only when $p_g = p_{\mathrm{data}}$, notice that
>
> $$\mathbb{E}_{x\sim p_{\mathrm{data}}}[-\log 2] + \mathbb{E}_{x\sim p_g}[-\log 2] = -\log 4$$
>
> and subtracting this expression from $C(G) = V(D_G^*, G)$, we obtain:
>
> $$C(G) = -\log(4) + KL\left(p_{\mathrm{data}} \left\| \frac{p_{\mathrm{data}} + p_g}{2}\right.\right) + KL\left(p_g \left\| \frac{p_{\mathrm{data}} + p_g}{2}\right.\right) \tag{5}$$
> {#goodfellow-2014-gan-eq-5 .equation tag=014E}
>
> where KL is the Kullback–Leibler divergence. We can identify the Jensen–Shannon divergence between the model distribution and the data generating process in the preceding expression:
>
> $$C(G) = -\log(4) + 2 \cdot JSD(p_{\mathrm{data}} \| p_g) \tag{6}$$
> {#goodfellow-2014-gan-eq-6 .equation tag=014F}
>
> Since the Jensen–Shannon divergence between two distributions is always nonnegative, and is zero only when they are equal, we have proved that $C^* = -\log(4)$ is the global minimum of $C(G)$, and the unique solution is $p_g = p_{\mathrm{data}}$, that is, the generative model perfectly reproduces the data generating process. $\square$
>
> ### 4.2 Convergence of Algorithm 1 {#goodfellow-2014-gan-s4-2 .section tag=0112}
>
> **Proposition 2.** *If $G$ and $D$ have sufficient capacity, and at every step of Algorithm 1, the discriminator is allowed to reach its optimum given $G$, while updating $p_g$ to improve the criterion* {#goodfellow-2014-gan-prop-2 .statement tag=0113}
>
> $$\mathbb{E}_{x\sim p_{\mathrm{data}}}[\log D_G^*(x)] + \mathbb{E}_{x\sim p_g}[\log(1 - D_G^*(x))]$$
>
> *then $p_g$ converges to $p_{\mathrm{data}}$*
>
> *Proof.* Following the approach in the above criterion, regard $V(G, D) = U(p_g, D)$ as a function of $p_g$. Notice that $U(p_g, D)$ is convex with respect to $p_g$. The subderivative of the supremum of convex functions contains the derivative of the function at the point where the maximum is attained. In other words, if $f(x) = \sup_{\alpha\in\mathcal{A}} f_\alpha(x)$, and $f_\alpha(x)$ is convex with respect to $x$ for every $\alpha$, then when $\beta = \arg \sup_{\alpha\in\mathcal{A}} f_\alpha(x)$, $\partial f_\beta(x) \in \partial f$. This is equivalent to calculating one gradient descent update for $p_g$ at the optimal $D$ given the corresponding $G$. According to the result already proved in Theorem 1, $\sup_D U(p_g, D)$ is convex with respect to $p_g$, and has a unique global optimum, therefore when the update of $p_g$ is sufficiently small, $p_g$ converges to $p_x$, completing the proof. $\square$
>
> In practice, adversarial networks represent a restricted family of the $p_g$ distribution through the function $G(z; \theta_g)$, while what we optimize is $\theta_g$ rather than $p_g$ itself. Using a multilayer perceptron to define $G$ introduces multiple critical points in parameter space. However, the excellent performance of multilayer perceptrons in practice indicates that, despite the lack of theoretical guarantees, they are still reasonably usable models.

### `content/zh/goodfellow-2014-gan/08_acknowledgments.md`

paper 86 of the canon, checked whole, translated by gpt-5, put back by gpt-5, judged by gpt-5. The fleet had nothing else free, so this is a model marking its own work.

- The original says Ian Goodfellow is supported by the 2013 Google Fellowship in Deep Learning, while the back-translation says he was supported by the 2013 Google Deep Learning Scholarship.

The English as it stands:

> We would like to acknowledge Patrice Marcotte, Olivier Delalleau, Kyunghyun Cho, Guillaume Alain and Jason Yosinski for helpful discussions. Yann Dauphin shared his Parzen window evaluation code with us. We would like to thank the developers of Pylearn2 [12] and Theano [7, 1], particularly Frédéric Bastien who shared a Theano feature specifically to benefit this project. Arnaud Bergeron provided much-needed support with $\LaTeX$ typesetting. We would also like to thank CIFAR, and Canada Research Chairs for funding, and Compute Canada, and Calcul Québec for providing computational resources. Ian Goodfellow is supported by the 2013 Google Fellowship in Deep Learning. Finally, we would like to thank Les Trois Brasseurs for stimulating our creativity.

What came back:

> We thank Patrice Marcotte, Olivier Delalleau, Kyunghyun Cho, Guillaume Alain, and Jason Yosinski for the helpful discussions. Yann Dauphin shared his Parzen window evaluation code with us. We thank the developers of Pylearn2 [12] and Theano [7, 1], especially Frédéric Bastien, who shared a Theano feature specifically to help with this project. Arnaud Bergeron provided extremely important support in $\LaTeX$ typesetting. We also thank CIFAR and Canada Research Chairs for funding support, and Compute Canada and Calcul Québec for providing computing resources. Ian Goodfellow was supported by the 2013 Google Deep Learning Scholarship. Finally, we thank Les Trois Brasseurs for inspiring our creativity.

## Differs in wording

### `content/ja/goodfellow-2014-gan/01_introduction.md`

paper 86 of the canon, checked whole, translated by gpt-5, put back by gpt-5, judged by gpt-5. The fleet had nothing else free, so this is a model marking its own work.

- The original says the piecewise linear units have a particularly well-behaved gradient, while the back-translation says they have particularly convenient gradients, which slightly blurs the stated property but does not materially change the claim.
- The original says the framework can yield specific training algorithms for many kinds of model and optimization algorithm, while the back-translation says it can provide specific learning algorithms for many types of models and optimization algorithms, preserving the claim.

The English as it stands:

> The promise of deep learning is to discover rich, hierarchical models [2] that represent probability distributions over the kinds of data encountered in artificial intelligence applications, such as natural images, audio waveforms containing speech, and symbols in natural language corpora. So far, the most striking successes in deep learning have involved discriminative models, usually those that map a high-dimensional, rich sensory input to a class label [14], [[krizhevsky-2012-imagenet]]. These striking successes have primarily been based on the backpropagation and dropout algorithms, using piecewise linear units [19, 9, 10] which have a particularly well-behaved gradient . Deep *generative* models have had less of an impact, due to the difficulty of approximating many intractable probabilistic computations that arise in maximum likelihood estimation and related strategies, and due to difficulty of leveraging the benefits of piecewise linear units in the generative context. We propose a new generative model estimation procedure that sidesteps these difficulties. [^4]
>
> In the proposed *adversarial nets* framework, the generative model is pitted against an adversary: a discriminative model that learns to determine whether a sample is from the model distribution or the data distribution. The generative model can be thought of as analogous to a team of counterfeiters, trying to produce fake currency and use it without detection, while the discriminative model is analogous to the police, trying to detect the counterfeit currency. Competition in this game drives both teams to improve their methods until the counterfeits are indistinguishable from the genuine articles.
>
> [^1]: Jean Pouget-Abadie is visiting Université de Montréal from Ecole Polytechnique.
> [^2]: Sherjil Ozair is visiting Université de Montréal from Indian Institute of Technology Delhi
> [^3]: Yoshua Bengio is a CIFAR Senior Fellow.
> [^4]: All code and hyperparameters available at http://www.github.com/goodfeli/adversarial
>
> This framework can yield specific training algorithms for many kinds of model and optimization algorithm. In this article, we explore the special case when the generative model generates samples by passing random noise through a multilayer perceptron, and the discriminative model is also a multilayer perceptron. We refer to this special case as *adversarial nets*. In this case, we can train both models using only the highly successful backpropagation and dropout algorithms [17] and sample from the generative model using only forward propagation. No approximate inference or Markov chains are necessary.

What came back:

> The promise of deep learning lies in discovering rich, hierarchical models [2] that represent probability distributions over the kinds of data encountered in artificial intelligence applications, such as natural images, acoustic waveforms including speech, and symbols in natural language corpora. So far, the most striking successes in deep learning have been with discriminative models, which usually map high-dimensional, rich sensory inputs to class labels [14], [[krizhevsky-2012-imagenet]]. These striking successes have been based mainly on the algorithms of backpropagation and dropout, using piecewise-linear units [19, 9, 10] with particularly convenient gradients. Deep *generative* models have had a smaller impact because of the difficulty of approximating many intractable probabilistic computations that arise in maximum likelihood estimation and related strategies, and the difficulty of exploiting the advantages of piecewise-linear units in the context of generation. In this paper, we propose a new generative model estimation procedure that avoids these difficulties. [^4]
>
> In the proposed *adversarial nets* framework, the generative model confronts an adversary. That is, a discriminative model that learns to determine whether a sample came from the model distribution or the data distribution. The generative model can be thought of as resembling a group of counterfeiters who produce counterfeit currency and try to use it without being discovered. On the other hand, the discriminative model resembles the police who try to detect that counterfeit currency. The competition in this game encourages both sides to improve their methods until the counterfeits become indistinguishable from the genuine ones.
>
> [^1]: Jean Pouget-Abadie is visiting Université de Montréal from Ecole Polytechnique.
> [^2]: Sherjil Ozair is visiting Université de Montréal from Indian Institute of Technology Delhi.
> [^3]: Yoshua Bengio is a CIFAR Senior Fellow.
> [^4]: All code and hyperparameters are available at [[http://www.github.com/goodfeli/adversarial\](http://www.github.com/goodfeli/adversarial)で利用可能である。](http://www.github.com/goodfeli/adversarial]\(http://www.github.com/goodfeli/adversarial\)で利用可能である。)
>
> This framework can provide specific learning algorithms for many types of models and optimization algorithms. In this paper, we consider the special case in which the generative model generates samples by passing random noise through a multilayer perceptron, and the discriminative model is also a multilayer perceptron. We call this special case *adversarial nets*. In this case, both models can be trained using only the highly successful algorithms of backpropagation and dropout [17], and sampling from the generative model can also be performed using only forward propagation. Approximate inference and Markov chains are unnecessary.

### `content/ja/goodfellow-2014-gan/06_advantages_and_disadvantages.md`

paper 86 of the canon, checked whole, translated by gpt-5, put back by gpt-5, judged by gpt-5. The fleet had nothing else free, so this is a model marking its own work.


The English as it stands:

> This new framework comes with advantages and disadvantages relative to previous modeling frameworks. The disadvantages are primarily that there is no explicit representation of $p_g(x)$, and that $D$ must be synchronized well with $G$ during training (in particular, $G$ must not be trained too much without updating $D$, in order to avoid “the Helvetica scenario” in which $G$ collapses too many values of $\mathbf{z}$ to the same value of $\mathbf{x}$ to have enough diversity to model $p_{\text{data}}$), much as the negative chains of a Boltzmann machine must be kept up to date between learning steps. The advantages are that Markov chains are never needed, only backprop is used to obtain gradients, no inference is needed during learning, and a wide variety of functions can be incorporated into the model. Table 2 summarizes the comparison of generative adversarial nets with other generative modeling approaches.
>
> The aforementioned advantages are primarily computational. Adversarial models may also gain some statistical advantage from the generator network not being updated directly with data examples, but only with gradients flowing through the discriminator. This means that components of the input are not copied directly into the generator’s parameters. Another advantage of adversarial networks is that they can represent very sharp, even degenerate distributions, while methods based on Markov chains require that the distribution be somewhat blurry in order for the chains to be able to mix between modes.

What came back:

> This new framework has advantages and disadvantages compared with conventional modeling frameworks. The disadvantages are mainly that there is no explicit representation of $p_g(x)$ and that $D$ must be well synchronized with $G$ during training (in particular, $G$ must not be overtrained without updating $D$ in order to avoid the “Helvetica scenario,” in which $G$ collapses too many values of $\mathbf{z}$ onto the same value of $\mathbf{x}$, so as to have enough diversity to model $p_{\text{data}}$). This is similar to how the negative chain of a Boltzmann machine must always be kept up to date between training steps. The advantages are that no Markov chain is needed at all, only backpropagation is used to obtain gradients, inference is not needed during training, and a wide variety of functions can be incorporated into the model. Table 2 summarizes the comparison of generative adversarial networks with other generative modeling methods.
>
> The aforementioned advantages are mainly computational. Adversarial models may also have some statistical advantages because the generator network is not updated directly by data examples, but only by gradients flowing through the discriminator. This means that components of the input are not directly copied into the parameters of the generator. Another advantage of adversarial networks is that they can represent very sharp, even degenerate distributions. On the other hand, in methods based on Markov chains, the distribution needs to be blurred to some extent so that the chain can mix between modes.

### `content/vi/goodfellow-2014-gan/01_introduction.md`

paper 86 of the canon, checked whole, translated by gpt-5, put back by gpt-5, judged by gpt-5. The fleet had nothing else free, so this is a model marking its own work.


The English as it stands:

> The promise of deep learning is to discover rich, hierarchical models [2] that represent probability distributions over the kinds of data encountered in artificial intelligence applications, such as natural images, audio waveforms containing speech, and symbols in natural language corpora. So far, the most striking successes in deep learning have involved discriminative models, usually those that map a high-dimensional, rich sensory input to a class label [14], [[krizhevsky-2012-imagenet]]. These striking successes have primarily been based on the backpropagation and dropout algorithms, using piecewise linear units [19, 9, 10] which have a particularly well-behaved gradient . Deep *generative* models have had less of an impact, due to the difficulty of approximating many intractable probabilistic computations that arise in maximum likelihood estimation and related strategies, and due to difficulty of leveraging the benefits of piecewise linear units in the generative context. We propose a new generative model estimation procedure that sidesteps these difficulties. [^4]
>
> In the proposed *adversarial nets* framework, the generative model is pitted against an adversary: a discriminative model that learns to determine whether a sample is from the model distribution or the data distribution. The generative model can be thought of as analogous to a team of counterfeiters, trying to produce fake currency and use it without detection, while the discriminative model is analogous to the police, trying to detect the counterfeit currency. Competition in this game drives both teams to improve their methods until the counterfeits are indistinguishable from the genuine articles.
>
> [^1]: Jean Pouget-Abadie is visiting Université de Montréal from Ecole Polytechnique.
> [^2]: Sherjil Ozair is visiting Université de Montréal from Indian Institute of Technology Delhi
> [^3]: Yoshua Bengio is a CIFAR Senior Fellow.
> [^4]: All code and hyperparameters available at http://www.github.com/goodfeli/adversarial
>
> This framework can yield specific training algorithms for many kinds of model and optimization algorithm. In this article, we explore the special case when the generative model generates samples by passing random noise through a multilayer perceptron, and the discriminative model is also a multilayer perceptron. We refer to this special case as *adversarial nets*. In this case, we can train both models using only the highly successful backpropagation and dropout algorithms [17] and sample from the generative model using only forward propagation. No approximate inference or Markov chains are necessary.

What came back:

> The promise of deep learning is to discover rich, hierarchical structured models [2] representing probability distributions over the kinds of data encountered in artificial intelligence applications, such as natural images, speech-containing sound waveforms, and symbols in natural language corpora. So far, the most notable successes of deep learning concern discriminative models, often models that map a high-dimensional, information-rich perceptual input to a class label [14], [[krizhevsky-2012-imagenet]]. These notable successes have mainly relied on backpropagation and dropout algorithms, using piecewise linear units [19, 9, 10] with particularly stable gradients. Deep \*generative\* models have had less impact, due to difficulties in approximating many intractable probability computations that arise explicitly in maximum likelihood estimation and related strategies, as well as difficulties in exploiting the benefits of piecewise linear units in the context of data generation. We propose a new generative model estimation procedure that avoids these difficulties. [^4]
>
> In the \*adversarial nets\* framework proposed, the generative model is placed against an opponent: a discriminative model learns to determine whether a sample comes from the model's distribution or from the data distribution. The generative model can be viewed as similar to a group of counterfeiters, trying to produce counterfeit money and use it without being detected, while the discriminative model is similar to the police force, trying to detect counterfeit money. The competition in this game drives both sides to improve their methods until the counterfeits become indistinguishable from the real ones.
>
> [^1]: Jean Pouget-Abadie is visiting Université de Montréal from Ecole Polytechnique.
> [^2]: Sherjil Ozair is visiting Université de Montréal from Indian Institute of Technology Delhi
> [^3]: Yoshua Bengio is a CIFAR Senior Fellow.
> [^4]: The complete source code and hyperparameters are available at [[http://www.github.com/goodfeli/adversarial\](http://www.github.com/goodfeli/adversarial)](http://www.github.com/goodfeli/adversarial]\(http://www.github.com/goodfeli/adversarial\))
>
> This framework can produce specific training algorithms for many types of models and optimization algorithms. In this paper, we examine the special case in which the generative model generates samples by passing random noise through a multilayer perceptron, and the discriminative model is also a multilayer perceptron. We call this special case \*adversarial nets\*. In this case, we can train both models only with very successful backpropagation and dropout algorithms [17], while sampling from the generative model only by forward propagation. No approximate inference or Markov chains are needed.

### `content/zh/goodfellow-2014-gan/00_front.md`

every abstract is checked, translated by gpt-5, put back by gpt-5, judged by gpt-5. The fleet had nothing else free, so this is a model marking its own work.


The English as it stands:

> Generative Adversarial Nets
>
> **Ian J. Goodfellow, Jean Pouget-Abadie[^1], Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair[^2], Aaron Courville, Yoshua Bengio[^3]**
>
> Département d’informatique et de recherche opérationnelle  
> Université de Montréal  
> Montréal, QC H3C 3J7
>
> arXiv:1406.2661v1 [stat.ML] 10 Jun 2014
>
> Abstract
>
> We propose a new framework for estimating generative models via an adversarial process, in which we simultaneously train two models: a generative model $G$ that captures the data distribution, and a discriminative model $D$ that estimates the probability that a sample came from the training data rather than $G$. The training procedure for $G$ is to maximize the probability of $D$ making a mistake. This framework corresponds to a minimax two-player game. In the space of arbitrary functions $G$ and $D$, a unique solution exists, with $G$ recovering the training data distribution and $D$ equal to $\frac{1}{2}$ everywhere. In the case where $G$ and $D$ are defined by multilayer perceptrons, the entire system can be trained with backpropagation. There is no need for any Markov chains or unrolled approximate inference networks during either training or generation of samples. Experiments demonstrate the potential of the framework through qualitative and quantitative evaluation of the generated samples.

What came back:

> Generative Adversarial Networks
>
> **Ian J. Goodfellow, Jean Pouget-Abadie[^1], Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair[^2], Aaron Courville, Yoshua Bengio[^3]**
>
> Département d’informatique et de recherche opérationnelle  
> Université de Montréal  
> Montréal, QC H3C 3J7
>
> arXiv:1406.2661v1 [stat.ML] 10 Jun 2014
>
> Abstract
>
> We propose a new framework for estimating generative models through an adversarial process, in which two models are trained simultaneously: a generative model $G$ that captures the data distribution, and a discriminative model $D$ that estimates the probability that a given sample comes from the training data rather than from $G$. The training process of $G$ is to maximize the probability that $D$ makes a mistake. This framework corresponds to a minimax two-player game. In the space of arbitrary functions $G$ and $D$, there exists a unique solution, where $G$ recovers the training data distribution, and $D$ equals $\frac{1}{2}$ at all locations. When $G$ and $D$ are defined by multilayer perceptrons, the entire system can be trained by backpropagation. Neither Markov chains nor unfolded approximate inference networks are needed during training or during the generation of samples. Experiments demonstrate the potential of this framework through qualitative and quantitative evaluation of generated samples.

### `content/zh/goodfellow-2014-gan/03_adversarial_nets.md`

paper 86 of the canon, checked whole, translated by gpt-5, put back by gpt-5, judged by gpt-5. The fleet had nothing else free, so this is a model marking its own work.


The English as it stands:

> The adversarial modeling framework is most straightforward to apply when the models are both multilayer perceptrons. To learn the generator’s distribution $p_g$ over data $\boldsymbol{x}$, we define a prior on input noise variables $p_z(\boldsymbol{z})$, then represent a mapping to data space as $G(\boldsymbol{z}; \theta_g)$, where $G$ is a differentiable function represented by a multilayer perceptron with parameters $\theta_g$. We also define a second multilayer perceptron $D(\boldsymbol{x}; \theta_d)$ that outputs a single scalar. $D(\boldsymbol{x})$ represents the probability that $\boldsymbol{x}$ came from the data rather than $p_g$. We train $D$ to maximize the probability of assigning the correct label to both training examples and samples from $G$. We simultaneously train $G$ to minimize $\log(1 - D(G(\boldsymbol{z})))$:
>
> In other words, $D$ and $G$ play the following two-player minimax game with value function $V(G,D)$:
>
> $$\min_G \max_D V(D,G) = \mathbb{E}_{x\sim p_{\mathrm{data}}(x)}[\log D(x)] + \mathbb{E}_{z\sim p_z(z)}[\log(1-D(G(z)))]. \tag{1}$$
> {#goodfellow-2014-gan-eq-1 .equation tag=00C4}
>
> In the next section, we present a theoretical analysis of adversarial nets, essentially showing that the training criterion allows one to recover the data generating distribution as $G$ and $D$ are given enough capacity, i.e., in the non-parametric limit. See Figure 1 for a less formal, more pedagogical explanation of the approach. In practice, we must implement the game using an iterative, numerical approach. Optimizing $D$ to completion in the inner loop of training is computationally prohibitive, and on finite datasets would result in overfitting. Instead, we alternate between $k$ steps of optimizing $D$ and one step of optimizing $G$. This results in $D$ being maintained near its optimal solution, so long as $G$ changes slowly enough. This strategy is analogous to the way that SML/PCD [31, 29] training maintains samples from a Markov chain from one learning step to the next in order to avoid burning in a Markov chain as part of the inner loop of learning. The procedure is formally presented in Algorithm 1.
>
> In practice, equation 1 may not provide sufficient gradient for $G$ to learn well. Early in learning, when $G$ is poor, $D$ can reject samples with high confidence because they are clearly different from the training data. In this case, $\log(1-D(G(z)))$ saturates. Rather than training $G$ to minimize $\log(1-D(G(z)))$ we can train $G$ to maximize $\log D(G(z))$. This objective function results in the same fixed point of the dynamics of $G$ and $D$ but provides much stronger gradients early in learning.
>
> Figure 1: Generative adversarial nets are trained by simultaneously updating the discriminative distribution ($D$, blue, dashed line) so that it discriminates between samples from the data generating distribution (black, dotted line) $p_x$ from those of the generative distribution $p_g$ ($G$) (green, solid line). The lower horizontal line is the domain from which $z$ is sampled, in this case uniformly. The horizontal line above is part of the domain of $x$. The upward arrows show how the mapping $x=G(z)$ imposes the non-uniform distribution $p_g$ on transformed samples. $G$ contracts in regions of high density and expands in regions of low density of $p_g$. (a) Consider an adversarial pair near convergence: $p_g$ is similar to $p_{\mathrm{data}}$ and $D$ is a partially accurate classifier. (b) In the inner loop of the algorithm $D$ is trained to discriminate samples from data, converging to $D^*(x)=\frac{p_{\mathrm{data}}(x)}{p_{\mathrm{data}}(x)+p_g(x)}$. (c) After an update to $G$, gradient of $D$ has guided $G(z)$ to flow to regions that are more likely to be classified as data. (d) After several steps of training, if $G$ and $D$ have enough capacity, they will reach a point at which both cannot improve because $p_g=p_{\mathrm{data}}$. The discriminator is unable to differentiate between the two distributions, i.e. $D(x)=\frac{1}{2}$. {#goodfellow-2014-gan-fig-1 .figure tag=00C5}

What came back:

> When both models are multilayer perceptrons, the adversarial modeling framework is easiest to apply. To learn the distribution $p_g$ of the generator over data $\boldsymbol{x}$, we define a prior distribution $p_z(\boldsymbol{z})$ of the input noise variables, and then represent the mapping to data space as $G(\boldsymbol{z}; \theta_g)$, where $G$ is a differentiable function represented by a multilayer perceptron with parameters $\theta_g$. We also define a second multilayer perceptron $D(\boldsymbol{x}; \theta_d)$ whose output is a single scalar. $D(\boldsymbol{x})$ represents the probability that $\boldsymbol{x}$ comes from the data rather than from $p_g$. We train $D$ to maximize the probability of assigning the correct labels to both training examples and samples from $G$. At the same time, we train $G$ to minimize $\log(1 - D(G(\boldsymbol{z})))$:
>
> In other words, $D$ and $G$ play the following two-player minimax game with $V(G,D)$ as the value function:
>
> \min_G \max_D V(D,G) = \mathbb{E}_{x\sim p_{\mathrm{data}}(x)}[\log D(x)] + \mathbb{E}_{z\sim p_z(z)}[\log(1-D(G(z)))]. \tag{1}
>
> {#goodfellow-2014-gan-eq-1 .equation tag=00C4}
>
> In the next section, we will give a theoretical analysis of adversarial networks, whose essence is to show: when $G$ and $D$ are given sufficient capacity, that is, in the nonparametric limit, this training criterion can recover the data-generating distribution. For a less formal and more pedagogical explanation of this method, see Figure 1. In practice, we must use an iterative numerical method to implement this game. Optimizing $D$ to completion in the inner loop of training is computationally too expensive, and on finite datasets it will cause overfitting. Instead, we alternately perform $k$ steps of optimization of $D$ and one step of optimization of $G$. As long as $G$ changes sufficiently slowly, this can make $D$ always remain near its optimal solution. This strategy is similar to the practice in SML/PCD [31, 29] training, which continuously maintains samples from a Markov chain from one learning step to the next, thereby avoiding warming up the Markov chain in the inner loop of learning. This process is formally described in Algorithm 1.
>
> In practice, Equation 1 may not provide enough gradient for $G$ to achieve good learning. At the beginning of learning, when $G$ performs poorly, $D$ can reject samples with very high confidence because they are obviously different from the training data. In this case, $\log(1-D(G(z)))$ saturates. Rather than training $G$ to minimize $\log(1-D(G(z)))$, we can train $G$ to maximize $\log D(G(z))$. This objective function produces the same fixed points as the dynamics of $G$ and $D$, but can provide much stronger gradients at the beginning of learning.
>
> Figure 1: Generative adversarial networks are trained by simultaneously updating the discriminative distribution ($D$, blue dashed line), enabling it to distinguish samples from the data-generating distribution (black dotted line) $p_x$ from samples from the generative distribution $p_g$ ($G$) (green solid line). The horizontal line below is the domain from which $z$ is sampled, in this case uniformly sampled. The horizontal line above is part of the domain of $x$. The upward arrows show how the mapping $x=G(z)$ imposes a non-uniform distribution $p_g$ on the transformed samples. $G$ contracts in high-density regions and expands in low-density regions of $p_g$. (a) Consider an adversarial game pair close to convergence: $p_g$ is similar to $p_{\mathrm{data}}$, while $D$ is a partially accurate classifier. (b) In the inner loop of the algorithm, $D$ is trained to distinguish samples from the data and converges to $D^*(x)=\frac{p_{\mathrm{data}}(x)}{p_{\mathrm{data}}(x)+p_g(x)}$. (c) After one update of $G$, the gradient of $D$ guides $G(z)$ to flow toward regions more likely to be classified as data. (d) After several steps of training, if $G$ and $D$ have sufficient capacity, they will reach a point where neither can improve further, because $p_g=p_{\mathrm{data}}$. The discriminator cannot distinguish the two distributions, that is, $D(x)=\frac{1}{2}$. {#goodfellow-2014-gan-fig-1 .figure tag=00C5}

### `content/zh/goodfellow-2014-gan/05_experiments.md`

paper 86 of the canon, checked whole, translated by gpt-5, put back by gpt-5, judged by gpt-5. The fleet had nothing else free, so this is a model marking its own work.


The English as it stands:

> We trained adversarial nets on a range of datasets including MNIST[[lecun-1998-lenet]], the Toronto Face Database (TFD) [28], and CIFAR-10 [21]. The generator nets used a mixture of rectifier linear activations [19, 9] and sigmoid activations, while the discriminator net used maxout [10] activations. Dropout [17] was applied in training the discriminator net. While our theoretical framework permits the use of dropout and other noise at intermediate layers of the generator, we used noise as the input to only the bottommost layer of the generator network.
>
> We estimate probability of the test set data under $p_g$ by fitting a Gaussian Parzen window to the samples generated with $G$ and reporting the log-likelihood under this distribution. The $\sigma$ parameter
>
> | Model | MNIST | TFD |
> |---|---|---|
> | DBN [3] | $138 \pm 2$ | $1909 \pm 66$ |
> | Stacked CAE [3] | $121 \pm 1.6$ | $\mathbf{2110 \pm 50}$ |
> | Deep GSN [6] | $214 \pm 1.1$ | $1890 \pm 29$ |
> | Adversarial nets | $\mathbf{225 \pm 2}$ | $\mathbf{2057 \pm 26}$ |
>
> Table 1: Parzen window-based log-likelihood estimates. The reported numbers on MNIST are the mean log-likelihood of samples on test set, with the standard error of the mean computed across examples. On TFD, we computed the standard error across folds of the dataset, with a different $\sigma$ chosen using the validation set of each fold. On TFD, $\sigma$ was cross validated on each fold and mean log-likelihood on each fold were computed. For MNIST we compare against other models of the real-valued (rather than binary) version of dataset. {#goodfellow-2014-gan-tab-1 .table tag=00CA}
>
> of the Gaussians was obtained by cross validation on the validation set. This procedure was introduced in Breuleux *et al.* [8] and used for various generative models for which the exact likelihood is not tractable [25, 3, 5]. Results are reported in Table 1. This method of estimating the likelihood has somewhat high variance and does not perform well in high dimensional spaces but it is the best method available to our knowledge. Advances in generative models that can sample but not estimate likelihood directly motivate further research on how to evaluate such models.
>
> In Figures 2 and 3 we show samples drawn from the generator net after training. While we make no claim that these samples are better than samples generated by existing methods, we believe that these samples are at least competitive with the better generative models in the literature and highlight the potential of the adversarial framework.
>
> Figure 2: Visualization of samples from the model. Rightmost column shows the nearest training example of the neighboring sample, in order to demonstrate that the model has not memorized the training set. Samples are fair random draws, not cherry-picked. Unlike most other visualizations of deep generative models, these images show actual samples from the model distributions, not conditional means given samples of hidden units. Moreover, these samples are uncorrelated because the sampling process does not depend on Markov chain mixing. a) MNIST b) TFD c) CIFAR-10 (fully connected model) d) CIFAR-10 (convolutional discriminator and “deconvolutional” generator) {#goodfellow-2014-gan-fig-2 .figure tag=00CB}
>
> Figure 3: Digits obtained by linearly interpolating between coordinates in $z$ space of the full model. {#goodfellow-2014-gan-fig-3 .figure tag=00CC}
>
> |  | Deep directed graphical models | Deep undirected graphical models | Generative autoencoders | Adversarial models |
> |---|---|---|---|---|
> | Training | Inference needed during training. | Inference needed during training. MCMC needed to approximate partition function gradient. | Enforced tradeoff between mixing and power of reconstruction generation | Synchronizing the discriminator with the generator. Helvetica. |
> | Inference | Learned approximate inference | Variational inference | MCMC-based inference | Learned approximate inference |
> | Sampling | No difficulties | Requires Markov chain | Requires Markov chain | No difficulties |
> | Evaluating $p(x)$ | Intractable, may be approximated with AIS | Intractable, may be approximated with AIS | Not explicitly represented, may be approximated with Parzen density estimation | Not explicitly represented, may be approximated with Parzen density estimation |
> | Model design | Nearly all models incur extreme difficulty | Careful design needed to ensure multiple properties | Any differentiable function is theoretically permitted | Any differentiable function is theoretically permitted |
>
> Table 2: Challenges in generative modeling: a summary of the difficulties encountered by different approaches to deep generative modeling for each of the major operations involving a model. {#goodfellow-2014-gan-tab-2 .table tag=00CD}

What came back:

> We trained adversarial networks on multiple datasets, including MNIST[[lecun-1998-lenet]], the Toronto Face Database (TFD) [28], and CIFAR-10 [21]. The generator network used a mixture of rectified linear activation functions [19, 9] and sigmoid activation functions, while the discriminator network used maxout [10] activation functions. Dropout [17] was applied when training the discriminator network. Although our theoretical framework allows dropout and other noise to be used in the intermediate layers of the generator, we only used noise as the input to the lowest layer of the generator network.
>
> We estimated the probability of test set data under $p_g$ by fitting a Gaussian Parzen window to samples generated by $G$ and reporting the log likelihood under this distribution. The $\sigma$ parameter
>
> | Model | MNIST | TFD |
> |---|---|---|
> | DBN [3] | $138 \pm 2$ | $1909 \pm 66$ |
> | Stacked CAE [3] | $121 \pm 1.6$ | $\mathbf{2110 \pm 50}$ |
> | Deep GSN [6] | $214 \pm 1.1$ | $1890 \pm 29$ |
> | Adversarial networks | $\mathbf{225 \pm 2}$ | $\mathbf{2057 \pm 26}$ |
>
> Table 1: Parzen window-based log likelihood estimates. The reported values on MNIST are the mean of the test set sample log likelihoods, and the standard error of the mean is calculated across samples. On TFD, we calculated the standard error across the folds of the dataset, and used the validation set of each fold to select a different $\sigma$. On TFD, $\sigma$ was determined by cross-validation on each fold, and the mean log likelihood on each fold was calculated. For MNIST, we compare with other models on the real-valued version of the dataset (rather than the binary version). {#goodfellow-2014-gan-tab-1 .table tag=00CA}
>
> The parameters of these Gaussian distributions were obtained through cross-validation on the validation set. This procedure was proposed by Breuleux *et al.* [8] and used for multiple generative models that cannot calculate exact likelihoods [25, 3, 5]. The results are shown in Table 1. This likelihood estimation method has high variance and performs poorly in high-dimensional spaces, but to our knowledge, it is the best method currently available. The development of generative models that can sample but cannot directly estimate likelihood has prompted further research into how to evaluate such models.
>
> In Figures 2 and 3, we show samples drawn from the generator network after training. Although we do not claim that these samples are better than those generated by existing methods, we believe that these samples can at least compete with the better generative models in the literature and demonstrate the potential of the adversarial framework.
>
> Figure 2: Visualization of model samples. The rightmost column shows the nearest training sample to the adjacent sample, to prove that the model did not memorize the training set. The samples are all fairly randomly drawn, rather than deliberately selected. Unlike visualizations of most other deep generative models, these images show real samples from the model distribution, rather than conditional means given a latent unit sample. In addition, these samples are uncorrelated with each other, because the sampling process does not depend on Markov chain mixing. a) MNIST b) TFD c) CIFAR-10 (fully connected model) d) CIFAR-10 (convolutional discriminator and “deconvolutional” generator) {#goodfellow-2014-gan-fig-2 .figure tag=00CB}
>
> Figure 3: Digits obtained by linearly interpolating between the $z$ space coordinates of the complete model. {#goodfellow-2014-gan-fig-3 .figure tag=00CC}
>
> |  | Deep directed graphical models | Deep undirected graphical models | Generative autoencoders | Adversarial models |
> |---|---|---|---|---|
> | Training | Inference is required during training. | Inference is required during training. MCMC is required to approximate the partition function gradient. | Forced tradeoff between mixing ability and reconstruction generation ability | Synchronize the discriminator and generator.Helvetica。 |
> | Inference | Learned approximate inference | Variational inference | MCMC-based inference | Learned approximate inference |
> | Sampling | No difficulty | Requires a Markov chain | Requires a Markov chain | No difficulty |
> | Evaluate $p(x)$ | Intractable, can be approximated with AIS | Intractable, can be approximated with AIS | Not explicitly represented, can be approximated with Parzen density estimation | Not explicitly represented, can be approximated with Parzen density estimation |
> | Model design | Almost all models encounter great difficulties | Needs to be carefully designed to guarantee multiple properties | Theoretically allows any differentiable function | Theoretically allows any differentiable function |
>
> Table 2: Challenges in generative modeling: a summary of the difficulties encountered by different approaches to deep generative modeling in the various major operations involving the model. {#goodfellow-2014-gan-tab-2 .table tag=00CD}

### `content/zh/goodfellow-2014-gan/07_conclusions_and_future_work.md`

paper 86 of the canon, checked whole, translated by gpt-5, put back by gpt-5, judged by gpt-5. The fleet had nothing else free, so this is a model marking its own work.


The English as it stands:

> This framework admits many straightforward extensions:
>
> 1. A *conditional* generative model $p(\mathbf{x}\mid\mathbf{c})$ can be obtained by adding $\mathbf{c}$ as input to both $G$ and $D$.
> 2. *Learned approximate inference* can be performed by training an auxiliary network to predict $\mathbf{z}$ given $\mathbf{x}$. This is similar to the inference net trained by the wake-sleep algorithm [15] but with the advantage that the inference net may be trained for a fixed generator net after the generator net has finished training.
>
> 3. One can approximately model all conditionals $p(x_S \mid x_{\not S})$ where $S$ is a subset of the indices of $x$ by training a family of conditional models that share parameters. Essentially, one can use adversarial nets to implement a stochastic extension of the deterministic MP-DBM [11].
> 4. *Semi-supervised learning:* features from the discriminator or inference net could improve performance of classifiers when limited labeled data is available.
> 5. *Efficiency improvements:* training could be accelerated greatly by divising better methods for coordinating $G$ and $D$ or determining better distributions to sample $z$ from during training.
>
> This paper has demonstrated the viability of the adversarial modeling framework, suggesting that these research directions could prove useful.

What came back:

> :::writing{variant="document" id="58321" title="Translated Passage"}
> This framework allows many direct extensions:
>
> 1. By adding $\mathbf{c}$ as input to both $G$ and $D$, a *conditional* generative model $p(\mathbf{x}\mid\mathbf{c})$ can be obtained.
> 2. By training an auxiliary network to predict $\mathbf{z}$ from $\mathbf{x}$, *learned approximate inference* can be achieved. This is similar to the inference network trained by the wake-sleep algorithm [15], but has the advantage that, after the generator network has completed training, the inference network can be trained for a fixed generator network.
>
> 3. By training a family of conditional models that share parameters, all conditional distributions $p(x_S \mid x_{\not S})$ can be approximately modeled, where $S$ is a subset of the index set of $x$. In essence, adversarial networks can be used to implement a stochastic extension of deterministic MP-DBM [11].
> 4. *Semi-supervised learning:* Features from the discriminator or inference network can improve the performance of a classifier when labeled data is limited.
> 5. *Efficiency improvements:* Training can be greatly accelerated by designing better methods to coordinate $G$ and $D$, or by determining a better sampling distribution for $z$ during training.
>
> This paper has demonstrated the feasibility of the adversarial modeling framework, indicating that these research directions may be valuable.
> :::

## The same

- `content/ja/goodfellow-2014-gan/00_front.md` every abstract is checked, translated by gpt-5, put back by gpt-5, judged by gpt-5. The fleet had nothing else free, so this is a model marking its own work.
- `content/ja/goodfellow-2014-gan/07_conclusions_and_future_work.md` paper 86 of the canon, checked whole, translated by gpt-5, put back by gpt-5, judged by gpt-5. The fleet had nothing else free, so this is a model marking its own work.
- `content/ja/goodfellow-2014-gan/08_acknowledgments.md` paper 86 of the canon, checked whole, translated by gpt-5, put back by gpt-5, judged by gpt-5. The fleet had nothing else free, so this is a model marking its own work.
- `content/vi/goodfellow-2014-gan/03_adversarial_nets.md` paper 86 of the canon, checked whole, translated by gpt-5, put back by gpt-5, judged by gpt-5. The fleet had nothing else free, so this is a model marking its own work.
- `content/vi/goodfellow-2014-gan/06_advantages_and_disadvantages.md` paper 86 of the canon, checked whole, translated by gpt-5, put back by gpt-5, judged by gpt-5. The fleet had nothing else free, so this is a model marking its own work.
- `content/vi/goodfellow-2014-gan/08_acknowledgments.md` paper 86 of the canon, checked whole, translated by gpt-5, put back by gpt-5, judged by gpt-5. The fleet had nothing else free, so this is a model marking its own work.
- `content/zh/goodfellow-2014-gan/02_related_work.md` paper 86 of the canon, checked whole, translated by gpt-5, put back by gpt-5, judged by gpt-5. The fleet had nothing else free, so this is a model marking its own work.
- `content/zh/goodfellow-2014-gan/06_advantages_and_disadvantages.md` paper 86 of the canon, checked whole, translated by gpt-5, put back by gpt-5, judged by gpt-5. The fleet had nothing else free, so this is a model marking its own work.

