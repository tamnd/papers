---
paper: silver-2016-alphago
title: Mastering the game of Go with deep neural networks and tree search
authors:
  - David Silver
  - Aja Huang
  - Chris J. Maddison
  - Arthur Guez
  - Laurent Sifre
  - George van den Driessche
  - Julian Schrittwieser
  - Ioannis Antonoglou
  - Veda Panneershelvam
  - Marc Lanctot
year: 2016
venue: Nature
field: ai-ml
section_title: Method
kind: section
lang: en
source: https://storage.googleapis.com/deepmind-media/alphago/AlphaGoNaturePaper.pdf
pdf_sha256: 9c9184385a3d37b4f4e9d9715270986c43172747b1d08f29093128c1ef878b60
pdf_pages: 7-20
extraction: vision
extraction_model: gpt-5
content_sha256: 9c53bc52ae655c48d0b77a165038dafb236f7a503de02d376c6dee71c24f3a96
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Problem setting. Many games of perfect information, such as chess, checkers, othello, backgammon and Go, may be defined as alternating Markov games39. In these games, there is a state space $\mathcal{S}$ (where state includes an indication of the current player to play); an action space $\mathcal{A}(s)$ defining the legal actions in any given state $s \in \mathcal{S}$; a state transition function $f(s, a, \xi)$ defining the successor state after selecting action $a$ in state $s$ and random input $\xi$ (for example, dice); and finally a reward function $r^i(s)$ describing the reward received by player $i$ in state $s$. We restrict our attention to two-player zero-sum games, $r^1(s) = -r^2(s) = r(s)$, with deterministic state transitions, $f(s, a, \xi) = f(s, a)$, and zero rewards except at a terminal time step $T$. The outcome of the game $z_t = \pm r(s_T)$ is the terminal reward at the end of the game from the perspective of the current player at time step $t$.
A policy $p(a|s)$ is a probability distribution over legal actions $a \in \mathcal{A}(s)$. A value function is the expected outcome if all actions for both players are selected according to policy $p$, that is, $v^p(s) = \mathbb{E}[z_t|s_t = s, a_{t...T} \sim p]$. Zero-sum games have a unique optimal value function $v^*(s)$ that determines the outcome from state $s$ following perfect play by both players,

$$
v^*(s) = \begin{cases}
z_T & \text{if } s = s_T, \\
\max_a - v^*(f(s, a)) & \text{otherwise}
\end{cases}
$$

Prior work. The optimal value function can be computed recursively by minimax (or equivalently negamax) search40. Most games are too large for exhaustive minimax tree search; instead, the game is truncated by using an approximate value function $v(s) \approx v^*(s)$ in place of terminal rewards. Depth-first minimax search with alpha–beta pruning40 has achieved superhuman performance in chess4, checkers5 and othello6, but it has not been effective in Go7.

Reinforcement learning can learn to approximate the optimal value function directly from games of self-play39. The majority of prior work has focused on a linear combination $v_\theta(s) = \varphi(s) \cdot \theta$ of features $\varphi(s)$ with weights $\theta$. Weights were trained using temporal-difference learning41 in chess42,43, checkers44,45 and Go30; or using linear regression in othello6 and Scrabble9. Temporal-difference learning has also been used to train a neural network to approximate the optimal value function, achieving superhuman performance in backgammon46; and achieving weak kyu-level performance in small-board Go28,29,47 using convolutional networks.

An alternative approach to minimax search is Monte Carlo tree search (MCTS)11,12, which estimates the optimal value of interior nodes by a double approximation, $V^n(s) \approx v^{P^n}(s) \approx v^*(s)$. The first approximation, $V^n(s) \approx v^{P^n}(s)$, uses $n$ Monte Carlo simulations to estimate the value function of a simulation policy $P^n$. The second approximation, $v^{P^n}(s) \approx v^*(s)$, uses a simulation policy $P^n$ in place of minimax optimal actions. The simulation policy selects actions according to a search control function $\arg\max_a (Q^n(s, a) + u(s, a))$, such as UCT12, that selects children with higher action values, $Q^n(s, a) = -V^n(f(s, a))$, plus a bonus $u(s, a)$ that encourages exploration; or in the absence of a search tree at state $s$, it samples actions from a fast rollout policy $p_\pi(a|s)$. As more simulations are executed and the search tree grows deeper, the simulation policy becomes informed by increasingly accurate statistics. In the limit, both approximations become exact and MCTS (for example, with UCT) converges12 to the optimal value function $\lim_{n \to \infty} V^n(s) = \lim_{n \to \infty} v^{P^n}(s) = v^*(s)$. The strongest current Go programs are based on MCTS13–15,36.

MCTS has previously been combined with a policy that is used to narrow the beam of the search tree to high-probability moves13; or to bias the bonus term towards high-probability moves48. MCTS has also been combined with a value function that is used to initialize action values in newly expanded nodes16, or to mix Monte Carlo evaluation with minimax evaluation49. By contrast, AlphaGo’s use of value functions is based on truncated Monte Carlo search algorithms8,9, which terminate rollouts before the end of the game and use a value function in place of the terminal reward. AlphaGo’s position evaluation mixes full rollouts with truncated rollouts, resembling in some respects the well-known temporal-difference learning algorithm TD($\lambda$). AlphaGo also differs from prior work by using slower but more powerful representations of the policy and value function; evaluating deep neural networks is several orders of magnitude slower than linear representations and must therefore occur asynchronously.

The performance of MCTS is to a large degree determined by the quality of the rollout policy. Prior work has focused on handcrafted patterns50 or learning rollout policies by supervised learning13, reinforcement learning16, simulation balancing51,52 or online adaptation30,53; however, it is known that rollout-based position evaluation is frequently inaccurate54. AlphaGo uses relatively simple rollouts, and instead addresses the challenging problem of position evaluation more directly using value networks.

Search algorithm. To efficiently integrate large neural networks into AlphaGo, we implemented an asynchronous policy and value MCTS algorithm (APV-MCTS). Each node $s$ in the search tree contains edges $(s, a)$ for all legal actions $a \in \mathcal{A}(s)$. Each edge stores a set of statistics,

$$
\{P(s, a),\ N_v(s, a),\ N_r(s, a),\ W_v(s, a),\ W_r(s, a),\ Q(s, a)\}
$$

where $P(s, a)$ is the prior probability, $W_v(s, a)$ and $W_r(s, a)$ are Monte Carlo estimates of total action value, accumulated over $N_v(s, a)$ and $N_r(s, a)$ leaf evaluations and rollout rewards, respectively, and $Q(s, a)$ is the combined mean action value for that edge. Multiple simulations are executed in parallel on separate search threads. The APV-MCTS algorithm proceeds in the four stages outlined in Fig. 3.
Selection (Fig. 3a). The first in-tree phase of each simulation begins at the root of the search tree and finishes when the simulation reaches a leaf node at time step $L$. At each of these time steps, $t < L$, an action is selected according to the statistics in the search tree, $a_t = \arg\max_a (Q(s_t, a) + u(s_t, a))$ using a variant of the PUCT algorithm48, $u(s, a) = c_{\text{puct}} P(s, a) \frac{\sqrt{\sum_b N_r(s, b)}}{1 + N_r(s, a)}$, where $c_{\text{puct}}$ is a constant determining the level of exploration; this search control strategy initially prefers actions with high prior probability and low visit count, but asymptotically prefers actions with high action value.
Evaluation (Fig. 3c). The leaf position $s_L$ is added to a queue for evaluation $v_\theta(s_L)$ by the value network, unless it has previously been evaluated. The second rollout phase of each simulation begins at leaf node $s_L$ and continues until the end of the game. At each of these time-steps, $t \geq L$, actions are selected by both players according to the rollout policy, $a_t \sim p_\pi(\cdot|s_t)$. When the game reaches a terminal state, the outcome $z_t = \pm r(s_T)$ is computed from the final score.
Backup (Fig. 3d). At each in-tree step $t \leq L$ of the simulation, the rollout statistics are updated as if it has lost $n_{vl}$ games, $N_r(s_t, a_t) \leftarrow N_r(s_t, a_t) + n_{vl}$; $W_r(s_t, a_t) \leftarrow W_r(s_t, a_t) - n_{vl}$; this virtual loss55 discourages other threads from simultaneously exploring the identical variation. At the end of the simulation, the rollout statistics are updated in a backward pass through each step $t \leq L$, replacing the virtual losses by the outcome, $N_r(s_t, a_t) \leftarrow N_r(s_t, a_t) - n_{vl} + 1$; $W_r(s_t, a_t) \leftarrow W_r(s_t, a_t) + n_{vl} + z_t$. Asynchronously, a separate backward pass is initiated when the evaluation of the leaf position $s_L$ completes. The output of the value network $v_\theta(s_L)$ is used to update value statistics in a second backward pass through each step $t \leq L$, $N_v(s_t, a_t) \leftarrow N_v(s_t, a_t) + 1$, $W_v(s_t, a_t) \leftarrow W_v(s_t, a_t) + v_\theta(s_L)$. The overall evaluation of each state action is a weighted average of the Monte Carlo estimates,

$$
Q(s, a) = (1 - \lambda) \frac{W_v(s, a)}{N_v(s, a)} + \lambda \frac{W_r(s, a)}{N_r(s, a)},
$$

that mixes together the value network and rollout evaluations with weighting parameter $\lambda$. All updates are performed lock-free56.
Expansion (Fig. 3b). When the visit count exceeds a threshold, $N_r(s, a) > n_{thr}$, the successor state $s' = f(s, a)$ is added to the search tree. The new node is initialized to $\{N(s', a) = N_r(s', a) = 0,\ W(s', a) = W_r(s', a) = 0,\ P(s', a) = p_\sigma(a|s')\}$, using a tree policy $p_\tau(a|s')$ (similar to the rollout policy but with more features, see Extended Data Table 4) to provide placeholder prior probabilities for action selection. The position $s'$ is also inserted into a queue for asynchronous GPU evaluation by the policy network. Prior probabilities are computed by the SL policy network $p_\sigma^\beta(\cdot|s')$ with a softmax temperature set to $\beta$; these replace the placeholder prior probabilities, $P(s', a) \leftarrow p_\sigma^\beta(a|s')$, using an atomic update. The threshold $n_{thr}$ is adjusted dynamically to ensure that the rate at which positions are added to the policy queue matches the rate at which the GPUs evaluate the policy network. Positions are evaluated by both the policy network and the value network using a mini-batch size of 1 to minimize end-to-end evaluation time.

We also implemented a distributed APV-MCTS algorithm. This architecture consists of a single master machine that executes the main search, many remote worker CPUs that execute asynchronous rollouts, and many remote worker GPUs that execute asynchronous policy and value network evaluations. The entire search tree is stored on the master, which only executes the in-tree phase of each simulation. The leaf positions are communicated to the worker CPUs, which execute the rollout phase of simulation, and to the worker GPUs, which compute network features and evaluate the policy and value networks. The prior probabilities of the policy network are returned to the master, where they replace placeholder prior probabilities at the newly expanded node. The rewards from rollouts and the value network outputs are each returned to the master, and backed up the originating search path.

At the end of search AlphaGo selects the action with maximum visit count; this is less sensitive to outliers than maximizing action value15. The search tree is reused at subsequent time steps: the child node corresponding to the played action becomes the new root node; the subtree below this child is retained along with all its statistics, while the remainder of the tree is discarded. The match version of AlphaGo continues searching during the opponent’s move. It extends the search if the action maximizing visit count and the action maximizing action value disagree. Time controls were otherwise shaped to use most time in the middle-game57. AlphaGo resigns when its overall evaluation drops below an estimated 10% probability of winning the game, that is, $\max_a Q(s, a) < -0.8$.

AlphaGo does not employ the all-moves-as-first10 or rapid action value estimation58 heuristics used in the majority of Monte Carlo Go programs; when using policy networks as prior knowledge, these biased heuristics do not appear to give any additional benefit. In addition AlphaGo does not use progressive widening13, dynamic komi59 or an opening book60. The parameters used by AlphaGo in the Fan Hui match are listed in Extended Data Table 5.

Rollout policy. The rollout policy $p_\pi(a|s)$ is a linear softmax policy based on fast, incrementally computed, local pattern-based features consisting of both ‘response’ patterns around the previous move that led to state s, and ‘non-response’ patterns around the candidate move a in state s. Each non-response pattern is a binary feature matching a specific $3 \times 3$ pattern centred on a, defined by the colour (black, white, empty) and liberty count ($1, 2, \geq 3$) for each adjacent intersection. Each response pattern is a binary feature matching the colour and liberty count in a 12-point diamond-shaped pattern21 centred around the previous move. Additionally, a small number of handcrafted local features encode common-sense Go rules (see Extended Data Table 4). Similar to the policy network, the weights $\pi$ of the rollout policy are trained from 8 million positions from human games on the Tygem server to maximize log likelihood by stochastic gradient descent. Rollouts execute at approximately 1,000 simulations per second per CPU thread on an empty board.

Our rollout policy $p_\pi(a|s)$ contains less handcrafted knowledge than state-of-the-art Go programs13. Instead, we exploit the higher-quality action selection within MCTS, which is informed both by the search tree and the policy network. We introduce a new technique that caches all moves from the search tree and then plays similar moves during rollouts; a generalization of the ‘last good reply’ heuristic53. At every step of the tree traversal, the most probable action is inserted into a hash table, along with the $3 \times 3$ pattern context (colour, liberty and stone counts) around both the previous move and the current move. At each step of the rollout, the pattern context is matched against the hash table; if a match is found then the stored move is played with high probability.

Symmetries. In previous work, the symmetries of Go have been exploited by using rotationally and reflectionally invariant filters in the convolutional layers24,28,29. Although this may be effective in small neural networks, it actually hurts performance in larger networks, as it prevents the intermediate filters from identifying specific asymmetric patterns23. Instead, we exploit symmetries at run-time by dynamically transforming each position s using the dihedral group of eight reflections and rotations, $d_1(s), ..., d_8(s)$. In an explicit symmetry ensemble, a mini-batch of all 8 positions is passed into the policy network or value network and computed in parallel. For the value network, the output values are simply averaged, $\bar{v}_\theta(s) = \frac{1}{8} \sum_{j=1}^8 v_\theta(d_j(s))$. For the policy network, the planes of output probabilities are rotated/reflected back into the original orientation, and averaged together to provide an ensemble prediction, $\bar{p}_\sigma(\cdot|s) = \frac{1}{8} \sum_{j=1}^8 d_j^{-1}(p_\sigma(\cdot|d_j(s)))$; this approach was used in our raw network evaluation (see Extended Data Table 3). Instead, APV-MCTS makes use of an implicit symmetry ensemble that randomly selects a single rotation/reflection $j \in [1, 8]$ for each evaluation. We compute exactly one evaluation for that orientation only; in each simulation we compute the value of leaf node $s_L$ by $v_\theta(d_j(s_L))$, and allow the search procedure to average over these evaluations. Similarly, we compute the policy network for a single, randomly selected rotation/reflection, $d_j^{-1}(p_\sigma(\cdot|d_j(s)))$.

Policy network: classification. We trained the policy network $p_\sigma$ to classify positions according to expert moves played in the KGS data set. This data set contains 29.4 million positions from 160,000 games played by KGS 6 to 9 dan human players; 35.4% of the games are handicap games. The data set was split into a test set (the first million positions) and a training set (the remaining 28.4 million positions). Pass moves were excluded from the data set. Each position consisted of a raw board description s and the move a selected by the human. We augmented the data set to include all eight reflections and rotations of each position. Symmetry augmentation and input features were pre-computed for each position. For each training step, we sampled a randomly selected mini-batch of m samples from the augmented KGS data set, $\{s^k, a^k\}_{k=1}^m$ and applied an asynchronous stochastic gradient descent update to maximize the log likelihood of the action,

$$
\Delta \sigma = \frac{\alpha}{m} \sum_{k=1}^m \frac{\partial \log p_\sigma(a^k|s^k)}{\partial \sigma}
$$

The step size $\alpha$ was initialized to 0.003 and was halved every 80 million training steps, without momentum terms, and a mini-batch size of $m = 16$. Updates were applied asynchronously on 50 GPUs using DistBelief61; gradients older than 100 steps were discarded. Training took around 3 weeks for 340 million training steps.

Policy network: reinforcement learning. We further trained the policy network by policy gradient reinforcement learning25,26. Each iteration consisted of a mini-batch of n games played in parallel, between the current policy network $p_\rho$ that is being trained, and an opponent $p_{\rho^-}$ that uses parameters $\rho^-$ from a previous iteration, randomly sampled from a pool of opponents, so as to increase the stability of training. Weights were initialized to $\rho = \rho^- = \sigma$. Every 500 iterations, we added the current parameters $\rho$ to the opponent pool. Each game i in the mini-batch was played out until termination at step $T^i$, and then scored to determine the outcome $z_t^i = \pm r(s_{T^i})$ from each player’s perspective. The games were then replayed to determine the policy gradient update,

$$
\Delta \rho = \frac{\alpha}{n} \sum_{i=1}^n \sum_{t=1}^{T^i} \frac{\partial \log p_\rho(a_t^i|s_t^i)}{\partial \rho} (z_t^i - \nu(s_t^i)),
$$

using the REINFORCE algorithm25 with baseline $\nu(s_t^i)$ for variance reduction. On the first pass through the training pipeline, the baseline was set to zero; on the second pass we used the value network $v_\theta(s)$ as a baseline; this provided a small performance boost. The policy network was trained in this way for 10,000 mini-batches of 128 games, using 50 GPUs, for one day.

Value network: regression. We trained a value network $v_\theta(s) \approx v^{P_\rho}(s)$ to approximate the value function of the RL policy network $p_\rho$. To avoid overfitting to the strongly correlated positions within games, we constructed a new data set of uncorrelated self-play positions. This data set consisted of over 30 million positions, each drawn from a unique game of self-play. Each game was generated in three phases by randomly sampling a time step $U \sim \mathrm{unif}\{1, 450\}$, and sampling the first $t = 1, ... U - 1$ moves from the SL policy network, $a_t \sim p_\sigma(\cdot|s_t)$; then sampling one move uniformly at random from available moves, $a_U \sim \mathrm{unif}\{1, 361\}$ (repeatedly until $a_U$ is legal); then sampling the remaining sequence of moves until the game terminates, $t = U + 1, ... T$, from the RL policy network, $a_t \sim p_\rho(\cdot|s_t)$. Finally, the game is scored to determine the outcome $z_t = \pm r(s_T)$. Only a single training example $(s_{U+1}, z_{U+1})$ is added to the data set from each game. This data provides unbiased samples of the value function $v^{P_\rho}(s_{U+1}) = \mathbb{E}[z_{U+1}|s_{U+1}, a_{U+1}, ... T \sim p_\rho]$. During the first two phases of generation we sample from noisier distributions so as to increase the diversity of the data set. The training method was identical to SL policy network training, except that the parameter update was based on mean squared error between the predicted values and the observed rewards,

$$
\Delta \theta = \frac{\alpha}{m} \sum_{k=1}^m (z^k - v_\theta(s^k)) \frac{\partial v_\theta(s^k)}{\partial \theta}
$$

The value network was trained for 50 million mini-batches of 32 positions, using 50 GPUs, for one week.

Features for policy/value network. Each position s was pre-processed into a set of $19 \times 19$ feature planes. The features that we use come directly from the raw representation of the game rules, indicating the status of each intersection of the Go board: stone colour, liberties (adjacent empty points of stone’s chain), captures, legality, turns since stone was played, and (for the value network only) the current colour to play. In addition, we use one simple tactical feature that computes the outcome of a ladder search7. All features were computed relative to the current colour to play; for example, the stone colour at each intersection was represented as either player or opponent rather than black or white. Each integer feature value is split into multiple $19 \times 19$ planes of binary values (one-hot encoding). For example, separate binary feature planes are used to represent whether an intersection has 1 liberty, 2 liberties,..., $\geq 8$ liberties. The full set of feature planes are listed in Extended Data Table 2.

Neural network architecture. The input to the policy network is a $19 \times 19 \times 48$ image stack consisting of 48 feature planes. The first hidden layer zero pads the input into a $23 \times 23$ image, then convolves k filters of kernel size $5 \times 5$ with stride 1 with the input image and applies a rectifier nonlinearity. Each of the subsequent hidden layers 2 to 12 zero pads the respective previous hidden layer into a $21 \times 21$ image, then convolves k filters of kernel size $3 \times 3$ with stride 1, again followed by a rectifier nonlinearity. The final layer convolves 1 filter of kernel size $1 \times 1$ with stride 1, with a different bias for each position, and applies a softmax function. The match version of AlphaGo used $k = 192$ filters; Fig. 2b and Extended Data Table 3 additionally show the results of training with $k = 128, 256$ and 384 filters.

The input to the value network is also a $19 \times 19 \times 48$ image stack, with an additional binary feature plane describing the current colour to play. Hidden layers 2 to 11 are identical to the policy network, hidden layer 12 is an additional convolution layer, hidden layer 13 convolves 1 filter of kernel size $1 \times 1$ with stride 1, and hidden layer 14 is a fully connected linear layer with 256 rectifier units. The output layer is a fully connected linear layer with a single tanh unit.

Evaluation. We evaluated the relative strength of computer Go programs by running an internal tournament and measuring the Elo rating of each program. We estimate the probability that program a will beat program b by a logistic function

$$
p(a \text{ beats } b) = \frac{1}{1 + \exp(c_{elo}(e(b) - e(a))},
$$

and estimate the ratings $e(\cdot)$ by Bayesian logistic regression, computed by the BayesElo program37 using the standard constant $c_{elo} = 1/400$. The scale was anchored to the BayesElo rating of professional

Go player Fan Hui (2,908 at date of submission)62. All programs received a maximum of 5 s computation time per move; games were scored using Chinese rules with a komi of 7.5 points (extra points to compensate white for playing second). We also played handicap games where AlphaGo played white against existing Go programs; for these games we used a non-standard handicap system in which komi was retained but black was given additional stones on the usual handicap points. Using these rules, a handicap of K stones is equivalent to giving K — 1 free moves to black, rather than K — 1/2 free moves using standard no-komi handicap rules. We used these handicap rules because AlphaGo’s value network was trained specifically to use a komi of 7.5.

With the exception of distributed AlphaGo, each computer Go program was executed on its own single machine, with identical specifications, using the latest available version and the best hardware configuration supported by that program (see Extended Data Table 6). In Fig. 4, approximate ranks of computer programs are based on the highest KGS rank achieved by that program; however, the KGS version may differ from the publicly available version.

The match against Fan Hui was arbitrated by an impartial referee. Five formal games and five informal games were played with 7.5 komi, no handicap, and Chinese rules. AlphaGo won these games 5–0 and 3–2 respectively (Fig. 6 and Extended Data Table 1). Time controls for formal games were 1 h main time plus three periods of 30 s byoyomi. Time controls for informal games were three periods of 30 s byoyomi. Time controls and playing conditions were chosen by Fan Hui in advance of the match; it was also agreed that the overall match outcome would be determined solely by the formal games. To approximately assess the relative rating of Fan Hui to computer Go programs, we appended the results of all ten games to our internal tournament results, ignoring differences in time controls.

39. Littman, M. L. Markov games as a framework for multi-agent reinforcement learning. In 11th International Conference on Machine Learning, 157–163 (1994).
40. Knuth, D. E. & Moore, R. W. An analysis of alpha-beta pruning. Artif. Intell. 6, 293–326 (1975).
41. Sutton, R. Learning to predict by the method of temporal differences. Mach. Learn. 3, 9–44 (1988).
42. Baxter, J., Tridgell, A. & Weaver, L. Learning to play chess using temporal differences. Mach. Learn. 40, 243–263 (2000).
43. Veness, J., Silver, D., Blair, A. & Uther, W. Bootstrapping from game tree search. In Advances in Neural Information Processing Systems (2009).
44. Samuel, A. L. Some studies in machine learning using the game of checkers II - recent progress. IBM J. Res. Develop. 11, 601–617 (1967).
45. Schaeffer, J., Hlynka, M. & Jussila, V. Temporal difference learning applied to a high-performance game-playing program. In 17th International Joint Conference on Artificial Intelligence, 529–534 (2001).
46. Tesauro, G. TD-gammon, a self-teaching backgammon program, achieves master-level play. Neural Comput. 6, 215–219 (1994).
47. Dahl, F. Honte, a Go-playing program using neural nets. In Machines that learn to play games, 205–223 (Nova Science, 1999).
48. Rosin, C. D. Multi-armed bandits with episode context. Ann. Math. Artif. Intell. 61, 203–230 (2011).
49. Lanctot, M., Winands, M. H. M., Pepels, T. & Sturtevant, N. R. Monte Carlo tree search with heuristic evaluations using implicit minimax backups. In IEEE Conference on Computational Intelligence and Games, 1–8 (2014).
50. Gelly, S., Wang, Y., Munos, R. & Teytaud, O. Modification of UCT with patterns in Monte-Carlo Go. Tech. Rep. 6062, INRIA (2006).
51. Silver, D. & Tesauro, G. Monte-Carlo simulation balancing. In 26th International Conference on Machine Learning, 119 (2009).
52. Huang, S.-C., Coulom, R. & Lin, S.-S. Monte-Carlo simulation balancing in practice. In 7th International Conference on Computers and Games, 81–92 (Springer-Verlag, 2011).
53. Baier, H. & Drake, P. D. The power of forgetting: improving the last-good-reply policy in Monte Carlo Go. IEEE Trans. Comput. Intell. AI in Games 2, 303–309 (2010).
54. Huang, S. & Müller, M. Investigating the limits of Monte-Carlo tree search methods in computer Go. In 8th International Conference on Computers and Games, 39–48 (2013).
55. Segal, R. B. On the scalability of parallel UCT. Computers and Games 6515, 36–47 (2011).
56. Enzenberger, M. & Müller, M. A lock-free multithreaded Monte-Carlo tree search algorithm. In 12th Advances in Computer Games Conference, 14–20 (2009).
57. Huang, S.-C., Coulom, R. & Lin, S.-S. Time management for Monte-Carlo tree search applied to the game of Go. In International Conference on Technologies and Applications of Artificial Intelligence, 462–466 (2010).
58. Gelly, S. & Silver, D. Monte-Carlo tree search and rapid action value estimation in computer Go. Artif. Intell. 175, 1856–1875 (2011).
59. Baudiš, P. Balancing MCTS by dynamically adjusting the komi value. ICGA J. 34, 131 (2011).
60. Baier, H. & Winands, M. H. Active opening book application for Monte-Carlo tree search in 19×19 Go. In Benelux Conference on Artificial Intelligence, 3–10 (2011).
61. Dean, J. et al. Large scale distributed deep networks. In Advances in Neural Information Processing Systems, 1223–1231 (2012).
62. Go ratings. http://www.goratings.org.

Extended Data Table 1 | Details of match between AlphaGo and Fan Hui

| Date | Black | White | Category | Result |
| --- | --- | --- | --- | --- |
| 5/10/15 | Fan Hui | *AlphaGo* | Formal | *AlphaGo* wins by 2.5 points |
| 5/10/15 | Fan Hui | *AlphaGo* | Informal | Fan Hui wins by resignation |
| 6/10/15 | *AlphaGo* | Fan Hui | Formal | *AlphaGo* wins by resignation |
| 6/10/15 | *AlphaGo* | Fan Hui | Informal | *AlphaGo* wins by resignation |
| 7/10/15 | Fan Hui | *AlphaGo* | Formal | *AlphaGo* wins by resignation |
| 7/10/15 | Fan Hui | *AlphaGo* | Informal | *AlphaGo* wins by resignation |
| 8/10/15 | *AlphaGo* | Fan Hui | Formal | *AlphaGo* wins by resignation |
| 8/10/15 | *AlphaGo* | Fan Hui | Informal | *AlphaGo* wins by resignation |
| 9/10/15 | Fan Hui | *AlphaGo* | Formal | *AlphaGo* wins by resignation |
| 9/10/15 | *AlphaGo* | Fan Hui | Informal | Fan Hui wins by resignation |

The match consisted of five formal games with longer time controls, and five informal games with shorter time controls. Time controls and playing conditions were chosen by Fan Hui in advance of the match.

Extended Data Table 2 | Input features for neural networks

| Feature | # of planes | Description |
| --- | --- | --- |
| Stone colour | 3 | Player stone / opponent stone / empty |
| Ones | 1 | A constant plane filled with 1 |
| Turns since | 8 | How many turns since a move was played |
| Liberties | 8 | Number of liberties (empty adjacent points) |
| Capture size | 8 | How many opponent stones would be captured |
| Self-atari size | 8 | How many of own stones would be captured |
| Liberties after move | 8 | Number of liberties after this move is played |
| Ladder capture | 1 | Whether a move at this point is a successful ladder capture |
| Ladder escape | 1 | Whether a move at this point is a successful ladder escape |
| Sensibleness | 1 | Whether a move is legal and does not fill its own eyes |
| Zeros | 1 | A constant plane filled with 0 |
| Player color | 1 | Whether current player is black |

Feature planes used by the policy network (all but last feature) and value network (all features).

| Architecture |  |  | Evaluation |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Filters | Symmetries | Features | Test accuracy % | Train accuracy % | Raw net wins % | AlphaGo wins % | Forward time (ms) |
| 128 | 1 | 48 | 54.6 | 57.0 | 36 | 53 | 2.8 |
| 192 | 1 | 48 | 55.4 | 58.0 | 50 | 50 | 4.8 |
| 256 | 1 | 48 | 55.9 | 59.1 | 67 | 55 | 7.1 |
| 256 | 2 | 48 | 56.5 | 59.8 | 67 | 38 | 13.9 |
| 256 | 4 | 48 | 56.9 | 60.2 | 69 | 14 | 27.6 |
| 256 | 8 | 48 | 57.0 | 60.4 | 69 | 5 | 55.3 |
| 192 | 1 | 4 | 47.6 | 51.4 | 25 | 15 | 4.8 |
| 192 | 1 | 12 | 54.7 | 57.1 | 30 | 34 | 4.8 |
| 192 | 1 | 20 | 54.7 | 57.2 | 38 | 40 | 4.8 |
| 192 | 8 | 4 | 49.2 | 53.2 | 24 | 2 | 36.8 |
| 192 | 8 | 12 | 55.7 | 58.3 | 32 | 3 | 36.8 |
| 192 | 8 | 20 | 55.8 | 58.4 | 42 | 3 | 36.8 |

The policy network architecture consists of 128, 192 or 256 filters in convolutional layers; an explicit symmetry ensemble over 2, 4 or 8 symmetries; using only the first 4, 12 or 20 input feature planes listed in Extended Data Table 1. The results consist of the test and train accuracy on the KGS data set; and the percentage of games won by given policy network against AlphaGo’s policy network (highlighted row 2): using the policy networks to select moves directly (raw wins); or using AlphaGo’s search to select moves (AlphaGo wins); and finally the computation time for a single evaluation of the policy network.

Extended Data Table 4 | Input features for rollout and tree policy

| Feature | # of patterns | Description |
| --- | --- | --- |
| Response | 1 | Whether move matches one or more response pattern features |
| Save atari | 1 | Move saves stone(s) from capture |
| Neighbour | 8 | Move is 8-connected to previous move |
| Nakade | 8192 | Move matches a *nakade* pattern at captured stone |
| Response pattern | 32207 | Move matches 12-point diamond pattern near previous move |
| Non-response pattern | 69338 | Move matches $3 \times 3$ pattern around move |
| Self-atari | 1 | Move allows stones to be captured |
| Last move distance | 34 | Manhattan distance to previous two moves |
| Non-response pattern | 32207 | Move matches 12-point diamond pattern centred around move |

Features used by the rollout policy (first set) and tree policy (first and second set). Patterns are based on stone colour (black/white/empty) and liberties (1, 2, $\geq 3$) at each intersection of the pattern.

Extended Data Table 5 | Parameters used by AlphaGo

| Symbol | Parameter | Value |
| --- | --- | --- |
| $\beta$ | Softmax temperature | 0.67 |
| $\lambda$ | Mixing parameter | 0.5 |
| $n_{vl}$ | Virtual loss | 3 |
| $n_{thr}$ | Expansion threshold | 40 |
| $c_{puct}$ | Exploration constant | 5 |

| Short name | Computer Player | Version | Time settings | CPU | GPU | KGS Rank | Elo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| $\alpha_{rvp}^d$ | Distributed AlphaGo | See Methods | 5 seconds | 1202 | 176 | – | 3140 |
| $\alpha_{rvp}$ | AlphaGo | See Methods | 5 seconds | 48 | 8 | – | 2890 |
| *CS* | CrazyStone | 2015 | 5 seconds | 32 | – | 6d | 1929 |
| *ZN* | Zen | 5 | 5 seconds | 8 | – | 6d | 1888 |
| *PC* | Pachi | 10.99 | 400,000 sims | 16 | – | 2d | 1298 |
| *FG* | Fuego | svn1989 | 100,000 sims | 16 | – | – | 1148 |
| *GG* | GnuGo | 3.8 | level 10 | 1 | – | 5k | 431 |
| *CS_4* | CrazyStone | 4 handicap stones | 5 seconds | 32 | – | – | 2526 |
| *ZN_4* | Zen | 4 handicap stones | 5 seconds | 8 | – | – | 2413 |
| *PC_4* | Pachi | 4 handicap stones | 400,000 sims | 16 | – | – | 1756 |

Each program played with a maximum of 5 s thinking time per move; the games against Fan Hui were conducted using longer time controls, as described in Methods. CN_4, ZN_4 and PC_4 were given 4 handicap stones; komi was 7.5 in all games. Elo ratings were computed by BayesElo.

| Short name | Policy network | Value network | Rollouts | Mixing constant | Policy GPUs | Value GPUs | Elo rating |
| --- | --- | --- | --- | --- | --- | --- | --- |
| $\alpha_{rvp}$ | $p_\sigma$ | $v_\theta$ | $p_\pi$ | $\lambda = 0.5$ | 2 | 6 | 2890 |
| $\alpha_{vp}$ | $p_\sigma$ | $v_\theta$ | — | $\lambda = 0$ | 2 | 6 | 2177 |
| $\alpha_{rp}$ | $p_\sigma$ | — | $p_\pi$ | $\lambda = 1$ | 8 | 0 | 2416 |
| $\alpha_{rv}$ | $[p_\tau]$ | $v_\theta$ | $p_\pi$ | $\lambda = 0.5$ | 0 | 8 | 2077 |
| $\alpha_v$ | $[p_\tau]$ | $v_\theta$ | — | $\lambda = 0$ | 0 | 8 | 1655 |
| $\alpha_r$ | $[p_\tau]$ | — | $p_\pi$ | $\lambda = 1$ | 0 | 0 | 1457 |
| $\alpha_p$ | $p_\sigma$ | — | — | — | 0 | 0 | 1517 |

Evaluating positions using rollouts only ($\alpha_{rp}, \alpha_r$), value nets only ($\alpha_{vp}, \alpha_v$), or mixing both ($\alpha_{rvp}, \alpha_{rv}$); either using the policy network $p_\sigma(\alpha_{rvp}, \alpha_{vp}, \alpha_{rp})$, or no policy network ($\alpha_{rvp}, \alpha_{vp}, \alpha_{rp}$), that is, instead using the placeholder probabilities from the tree policy $p_\tau$ throughout. Each program used 5 s per move on a single machine with 48 CPUs and 8 GPUs. Elo ratings were computed by BayesElo.

Extended Data Table 8 | Results of a tournament between AlphaGo and distributed AlphaGo, testing scalability with hardware

| AlphaGo | Search threads | CPU | GPU | Elo |
| --- | --- | --- | --- | --- |
| Asynchronous | 1 | 48 | 8 | 2203 |
| Asynchronous | 2 | 48 | 8 | 2393 |
| Asynchronous | 4 | 48 | 8 | 2564 |
| Asynchronous | 8 | 48 | 8 | 2665 |
| Asynchronous | 16 | 48 | 8 | 2778 |
| Asynchronous | 32 | 48 | 8 | 2867 |
| Asynchronous | 40 | 48 | 8 | 2890 |
| Asynchronous | 40 | 48 | 1 | 2181 |
| Asynchronous | 40 | 48 | 2 | 2738 |
| Asynchronous | 40 | 48 | 4 | 2850 |
| Distributed | 12 | 428 | 64 | 2937 |
| Distributed | 24 | 764 | 112 | 3079 |
| Distributed | 40 | 1202 | 176 | 3140 |
| Distributed | 64 | 1920 | 280 | 3168 |

Each program played with a maximum of 2 s thinking time per move. Elo ratings were computed by BayesElo.

|  | $\alpha_{rvp}$ | $\alpha_{vp}$ | $\alpha_{rp}$ | $\alpha_{rv}$ | $\alpha_r$ | $\alpha_v$ | $\alpha_p$ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| $\alpha_{rvp}$ | - | 1 [0; 5] | 5 [4; 7] | 0 [0; 4] | 0 [0; 8] | 0 [0; 19] | 0 [0; 19] |
| $\alpha_{vp}$ | 99 [95; 100] | - | 61 [52; 69] | 35 [25; 48] | 6 [1; 27] | 0 [0; 22] | 1 [0; 6] |
| $\alpha_{rp}$ | 95 [93; 96] | 39 [31; 48] | - | 13 [7; 23] | 0 [0; 9] | 0 [0; 22] | 4 [1; 21] |
| $\alpha_{rv}$ | 100 [96; 100] | 65 [52; 75] | 87 [77; 93] | - | 0 [0; 18] | 29 [8; 64] | 48 [33; 65] |
| $\alpha_r$ | 100 [92; 100] | 94 [73; 99] | 100 [91; 100] | 100 [82; 100] | - | 78 [45; 94] | 78 [71; 84] |
| $\alpha_v$ | 100 [81; 100] | 100 [78; 100] | 100 [78; 100] | 71 [36; 92] | 22 [6; 55] | - | 30 [16; 48] |
| $\alpha_p$ | 100 [81; 100] | 99 [94; 100] | 96 [79; 99] | 52 [35; 67] | 22 [16; 29] | 70 [52; 84] | - |
| *CS* | 100 [97; 100] | 74 [66; 81] | 98 [94; 99] | 80 [70; 87] | 5 [3; 7] | 36 [16; 61] | 8 [5; 14] |
| *ZN* | 99 [93; 100] | 84 [67; 93] | 98 [93; 99] | 92 [67; 99] | 6 [2; 19] | 40 [12; 77] | 100 [65; 100] |
| *PC* | 100 [98; 100] | 99 [95; 100] | 100 [98; 100] | 98 [89; 100] | 78 [73; 81] | 87 [68; 95] | 55 [47; 62] |
| *FG* | 100 [97; 100] | 99 [93; 100] | 100 [96; 100] | 100 [91; 100] | 78 [73; 83] | 100 [65; 100] | 65 [55; 73] |
| *GG* | 100 [44; 100] | 100 [34; 100] | 100 [68; 100] | 100 [57; 100] | 99 [97; 100] | 67 [21; 94] | 99 [95; 100] |
| *$CS_{4}$* | 77 [69; 84] | 12 [8; 18] | 53 [44; 61] | 15 [8; 24] | 0 [0; 3] | 0 [0; 30] | 0 [0; 8] |
| *$ZN_{4}$* | 86 [77; 92] | 25 [16; 38] | 67 [56; 76] | 14 [7; 27] | 0 [0; 12] | 0 [0; 43] | - |
| *$PC_{4}$* | 99 [97; 100] | 82 [75; 88] | 98 [95; 99] | 89 [79; 95] | 32 [26; 39] | 13 [3; 36] | 35 [25; 46] |

95% Agresti–Coull confidence intervals in grey. Each program played with a maximum of 5 s thinking time per move. $CN_{4}$, $ZN_{4}$ and $PC_{4}$ were given 4 handicap stones; komi was 7.5 in all games. Distributed AlphaGo scored 77% [70; 82] against $\alpha_{rvp}$ and 100% against all other programs (no handicap games were played).

Extended Data Table 10 | Cross-table of win rates in per cent between programs in the single-machine scalability study

```text
Threads  GPU
1  2  4  8  16  32  40  40  40  40
1  8  -  70 [61;78]  90 [84;94]  94 [83;98]  86 [72;94]  98 [91;100]  98 [92;99]  100 [76;100]  96 [91;98]  38 [25;52]
2  8  30 [22;39]  -  72 [61;81]  81 [71;88]  86 [76;93]  92 [83;97]  93 [86;96]  83 [69;91]  84 [75;90]  26 [17;38]
4  8  10 [6;16]  28 [19;39]  -  62 [53;70]  71 [61;80]  82 [71;89]  84 [74;90]  81 [69;89]  78 [63;88]  18 [10;28]
8  8  6 [2;17]  19 [12;29]  38 [30;47]  -  61 [51;71]  65 [51;76]  73 [62;82]  74 [59;85]  64 [55;73]  12 [3;34]
16  8  14 [6;28]  14 [7;24]  29 [20;39]  39 [29;49]  -  52 [41;63]  61 [50;71]  52 [41;64]  41 [32;51]  5 [1;25]
32  8  2 [0;9]  8 [3;17]  18 [11;29]  35 [24;49]  48 [37;59]  -  52 [42;63]  44 [32;57]  26 [17;36]  0 [0;30]
40  8  2 [1;8]  8 [4;14]  16 [10;26]  27 [18;38]  39 [29;50]  48 [37;58]  -  43 [30;56]  41 [26;58]  4 [1;18]
40  4  0 [0;24]  17 [9;31]  19 [11;31]  26 [15;41]  48 [36;59]  56 [43;68]  57 [44;70]  -  29 [18;41]  2 [0;11]
40  2  4 [2;9]  16 [10;25]  22 [12;37]  36 [27;45]  59 [49;68]  74 [64;83]  59 [42;74]  71 [59;82]  -  5 [1;17]
40  1  62 [48;75]  74 [62;83]  82 [72;90]  88 [66;97]  95 [75;99]  100 [70;100]  96 [82;99]  98 [89;100]  95 [83;99]  -
```

95% Agresti–Coull confidence intervals in grey. Each program played with 2 s per move; komi was 7.5 in all games.

Extended Data Table 11 | Cross-table of win rates in per cent between programs
in the distributed scalability study

```text
Threads          40     12     24     40     64
                 8      64     112    176    280
                 48     428    764    1202   1920

40     8     48   -      52 [43; 61]   68 [59; 76]   77 [70; 82]   81 [65; 91]
12     64    428  48 [39; 57]   -     64 [54; 73]   62 [41; 79]   83 [55; 95]
24     112   764  32 [24; 41]   36 [27; 46]   -   36 [20; 57]   60 [51; 69]
40     176   1202 23 [18; 30]   38 [21; 59]   64 [43; 80]   -   53 [39; 67]
64     280   1920 19 [9; 35]    17 [5; 45]    40 [31; 49]   47 [33; 61]   -
```

95% Agresti–Coull confidence intervals in grey. Each program played with 2 s per move; komi was 7.5 in all games.

© 2016 Macmillan Publishers Limited. All rights reserved.
