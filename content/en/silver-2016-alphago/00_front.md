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
section_title: Front Matter
tag: 01A4
kind: front
lang: en
source: https://storage.googleapis.com/deepmind-media/alphago/AlphaGoNaturePaper.pdf
pdf_sha256: 9c9184385a3d37b4f4e9d9715270986c43172747b1d08f29093128c1ef878b60
pdf_pages: 1-5
extraction: vision
extraction_model: gpt-5
content_sha256: 716e7fc9dd7b9835939ccf0e0f1f9fa8c328a04529b63ef02fbf57afe49851be
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

ARTICLE

doi:10.1038/nature16961

Mastering the game of Go with deep neural networks and tree search

David Silver¹*, Aja Huang¹*, Chris J. Maddison¹, Arthur Guez¹, Laurent Sifre¹, George van den Driessche¹,  
Julian Schrittwieser¹, Ioannis Antonoglou¹, Veda Panneershelvam¹, Marc Lanctot¹, Sander Dieleman¹, Dominik Grewe¹,  
John Nham², Nal Kalchbrenner¹, Ilya Sutskever², Timothy Lillicrap¹, Madeleine Leach¹, Koray Kavukcuoglu¹,  
Thore Graepel¹ & Demis Hassabis¹

**The game of Go has long been viewed as the most challenging of classic games for artificial intelligence owing to its enormous search space and the difficulty of evaluating board positions and moves. Here we introduce a new approach to computer Go that uses ‘value networks’ to evaluate board positions and ‘policy networks’ to select moves. These deep neural networks are trained by a novel combination of supervised learning from human expert games, and reinforcement learning from games of self-play. Without any lookahead search, the neural networks play at the level of state-of-the-art Monte Carlo tree search programs that simulate thousands of random games of self-play. We also introduce a new search algorithm that combines Monte Carlo simulation with value and policy networks. Using this search algorithm, our program AlphaGo achieved a 99.8% winning rate against other Go programs, and defeated the human European Go champion by 5 games to 0. This is the first time that a computer program has defeated a human professional player in the full-sized game of Go, a feat previously thought to be at least a decade away.**

All games of perfect information have an optimal value function, $v^*(s)$, policies¹³⁻¹⁵ or value functions¹⁶ based on a linear combination of input features. which determines the outcome of the game, from every board position or state $s$, under perfect play by all players. These games may be solved by recursively computing the optimal value function in a search tree containing approximately $b^d$ possible sequences of moves, where $b$ is the game’s breadth (number of legal moves per position) and $d$ is its depth (game length). In large games, such as chess ($b \approx 35$, $d \approx 80$)¹ and especially Go ($b \approx 250$, $d \approx 150$), exhaustive search is infeasible²,³, but the effective search space can be reduced by two general principles. First, the depth of the search may be reduced by position evaluation: truncating the search tree at state $s$ and replacing the subtree below $s$ by an approximate value function $v(s) \approx v^*(s)$ that predicts the outcome from state $s$. This approach has led to superhuman performance in chess⁴, checkers⁵ and othello⁶, but it was believed to be intractable in Go due to the complexity of the game⁷. Second, the breadth of the search may be reduced by sampling actions from a policy $p(a|s)$ that is a probability distribution over possible moves in a position $s$. For example, Monte Carlo rollouts⁸ search to maximum depth without branching at all, by sampling long sequences of actions for both players from a policy $p$. Averaging over such rollouts can provide an effective position evaluation, achieving superhuman performance in backgammon⁸ and Scrabble⁹, and weak amateur level play in Go¹⁰.

Monte Carlo tree search (MCTS)¹¹,¹² uses Monte Carlo rollouts to estimate the value of each state in a search tree. As more simulations are executed, the search tree grows larger and the relevant values become more accurate. The policy used to select actions during search is also improved over time, by selecting children with higher values. Asymptotically, this policy converges to optimal play, and the evaluations converge to the optimal value function¹². The strongest current Go programs are based on MCTS, enhanced by policies that are trained to predict human expert moves¹³. These policies are used to narrow the search to a beam of high-probability actions, and to sample actions during rollouts. This approach has achieved strong amateur play¹³⁻¹⁵. However, prior work has been limited to shallow

Recently, deep convolutional neural networks have achieved unprecedented performance in visual domains: for example, image classification¹⁷, face recognition¹⁸, and playing Atari games¹⁹. They use many layers of neurons, each arranged in overlapping tiles, to construct increasingly abstract, localized representations of an image²⁰. We employ a similar architecture for the game of Go. We pass in the board position as a $19 \times 19$ image and use convolutional layers to construct a representation of the position. We use these neural networks to reduce the effective depth and breadth of the search tree: evaluating positions using a value network, and sampling actions using a policy network.

We train the neural networks using a pipeline consisting of several stages of machine learning (Fig. 1). We begin by training a supervised learning (SL) policy network $\rho_\sigma$ directly from expert human moves. This provides fast, efficient learning without immediate feedback and high-quality gradients. Similar to prior work¹³,¹⁵, we also train a fast policy $\rho_\pi$ that can rapidly sample actions during rollouts. Next, we train a reinforcement learning (RL) policy network $\rho_\rho$ that improves the SL policy network by optimizing the final outcome of games of self-play. This adjusts the policy towards the correct goal of winning games, rather than maximizing predictive accuracy. Finally, we train a value network $v_\theta$ that predicts the winner of games played by the RL policy network against itself. Our program AlphaGo efficiently combines the policy and value networks with MCTS.

### Supervised learning of policy networks {#silver-2016-alphago-s-supervised-learning-of-policy-networks .section tag=04AC}

For the first stage of the training pipeline, we build on prior work on predicting expert moves in the game of Go using supervised learning¹³,²¹⁻²⁴. The SL policy network $\rho_\sigma(a|s)$ alternates between five convolutional layers with weights $\sigma$, and rectifier nonlinearities. A final softmax layer outputs a probability distribution over all legal moves $a$. The inputs to the policy network is a simple representation of the board state (see Extended Data Table 2). The policy network is trained on randomly

[^1]: Google DeepMind, 5 New Street Square, London EC4A 3TW, UK.  
[^2]: Google, 1600 Amphitheatre Parkway, Mountain View, California 94043, USA.  
*These authors contributed equally to this work.

NATURE | VOL 529 | 28 JANUARY 2016

© 2016 Macmillan Publishers Limited. All rights reserved.

Figure 1 | Neural network training pipeline and architecture. a, A fast rollout policy $p_\pi$ and supervised learning (SL) policy network $p_\sigma$ are trained to predict human expert moves in a data set of positions. A reinforcement learning (RL) policy network $p_\rho$ is initialized to the SL policy network, and is then improved by policy gradient learning to maximize the outcome (that is, winning more games) against previous versions of the policy network. A new data set is generated by playing games of self-play with the RL policy network. Finally, a value network $v_\theta$ is trained by regression to predict the expected outcome (that is, whether the current player wins) in positions from the self-play data set.
b, Schematic representation of the neural network architecture used in AlphaGo. The policy network takes a representation of the board position s as its input, passes it through many convolutional layers with parameters $\sigma$ (SL policy network) or $\rho$ (RL policy network), and outputs a probability distribution $p_\sigma(a|s)$ or $p_\rho(a|s)$ over legal moves a, represented by a probability map over the board. The value network similarly uses many convolutional layers with parameters $\theta$, but outputs a scalar value $v_\theta(s')$ that predicts the expected outcome in position $s'$.

sampled state-action pairs ($s, a$), using stochastic gradient ascent to maximize the likelihood of the human move $a$ selected in state $s$

$$
\Delta \sigma \propto \frac{\partial \log p_\sigma(a|s)}{\partial \sigma}
$$

We trained a 13-layer policy network, which we call the SL policy network, from 30 million positions from the KGS Go Server. The network predicted expert moves on a held out test set with an accuracy of 57.0% using all input features, and 55.7% using only raw board position and move history as inputs, compared to the state-of-the-art from other research groups of 44.4% at date of submission$^{24}$ (full results in Extended Data Table 3). Small improvements in accuracy led to large improvements in playing strength (Fig. 2a); larger networks achieve better accuracy but are slower to evaluate during search. We also trained a faster but less accurate rollout policy $p_\pi(a|s)$, using a linear softmax of small pattern features (see Extended Data Table 4) with weights $\pi$; this achieved an accuracy of 24.2%, using just 2$\mu$s to select an action, rather than 3 ms for the policy network.

Reinforcement learning of policy networks
The second stage of the training pipeline aims at improving the policy network by policy gradient reinforcement learning (RL)$^{25,26}$. The RL policy network $p_\rho$ is identical in structure to the SL policy network, and its weights $\rho$ are initialized to the same values, $\rho = \sigma$. We play games between the current policy network $p_\rho$ and a randomly selected previous iteration of the policy network. Randomizing from a pool of opponents in this way stabilizes training by preventing overfitting to the current policy. We use a reward function $r(s)$ that is zero for all non-terminal time steps $t < T$. The outcome $z_t = \pm r(s_T)$ is the terminal reward at the end of the game from the perspective of the current player at time step $t$: +1 for winning and −1 for losing. Weights are then updated at each time step $t$ by stochastic gradient ascent in the direction that maximizes expected outcome$^{25}$

$$
\Delta \rho \propto \frac{\partial \log p_\rho(a_t|s_t)}{\partial \rho} z_t
$$

We evaluated the performance of the RL policy network in game play, sampling each move $a_t \sim p_\rho(\cdot|s_t)$ from its output probability distribution over actions. When played head-to-head, the RL policy network won more than 80% of games against the SL policy network. We also tested against the strongest open-source Go program, Pachi$^{14}$, a sophisticated Monte Carlo search program, ranked at 2 amateur dan on KGS, that executes 100,000 simulations per move. Using no search at all, the RL policy network won 85% of games against Pachi. In comparison, the previous state-of-the-art, based only on supervised

Figure 2 | Strength and accuracy of policy and value networks.
a, Plot showing the playing strength of policy networks as a function of their training accuracy. Policy networks with 128, 192, 256 and 384 convolutional filters per layer were evaluated periodically during training; the plot shows the winning rate of AlphaGo using that policy network against the match version of AlphaGo. b, Comparison of evaluation accuracy between the value network and rollouts with different policies.

Positions and outcomes were sampled from human expert games. Each position was evaluated by a single forward pass of the value network $v_\theta$, or by the mean outcome of 100 rollouts, played out using either uniform random rollouts, the fast rollout policy $p_\pi$, the SL policy network $p_\sigma$ or the RL policy network $p_\rho$. The mean squared error between the predicted value and the actual game outcome is plotted against the stage of the game (how many moves had been played in the given position).

Figure 3 | Monte Carlo tree search in AlphaGo. a, Each simulation traverses the tree by selecting the edge with maximum action value Q, plus a bonus u(P) that depends on a stored prior probability P for that edge. b, The leaf node may be expanded; the new node is processed once by the policy network p_σ and the output probabilities are stored as prior probabilities P for each action. c, At the end of a simulation, the leaf node learning of convolutional networks, won 11% of games against Pachi^{23} and 12% against a slightly weaker program, Fuego^{24}.

Reinforcement learning of value networks
The final stage of the training pipeline focuses on position evaluation, estimating a value function v^p(s) that predicts the outcome from position s of games played by using policy p for both players^{28–30}

$$
v^p(s) = \mathbb{E}[z_t|s_t = s,\ a_{t...T} \sim p]
$$

Ideally, we would like to know the optimal value function under perfect play v^*(s); in practice, we instead estimate the value function v^{p_ρ} for our strongest policy, using the RL policy network p_ρ. We approximate the value function using a value network v_θ(s) with weights θ, v_θ(s) ≈ v^{p_ρ}(s) ≈ v^*(s). This neural network has a similar architecture to the policy network, but outputs a single prediction instead of a probability distribution. We train the weights of the value network by regression on state-outcome pairs (s, z), using stochastic gradient descent to minimize the mean squared error (MSE) between the predicted value v_θ(s), and the corresponding outcome z

$$
\Delta \theta \propto \frac{\partial v_\theta(s)}{\partial \theta} (z - v_\theta(s))
$$

The naive approach of predicting game outcomes from data consisting of complete games leads to overfitting. The problem is that successive positions are strongly correlated, differing by just one stone, but the regression target is shared for the entire game. When trained on the KGS data set in this way, the value network memorized the game outcomes rather than generalizing to new positions, achieving a minimum MSE of 0.37 on the test set, compared to 0.19 on the training set. To mitigate this problem, we generated a new self-play data set consisting of 30 million distinct positions, each sampled from a separate game. Each game was played between the RL policy network and itself until the game terminated. Training on this data set led to MSEs of 0.226 and 0.234 on the training and test set respectively, indicating minimal overfitting. Figure 2b shows the position evaluation accuracy of the value network, compared to Monte Carlo rollouts using the fast rollout policy p_π; the value function was consistently more accurate. A single evaluation of v_θ(s) also approached the accuracy of Monte Carlo rollouts using the RL policy network p_ρ, but using 15,000 times less computation.

Searching with policy and value networks
AlphaGo combines the policy and value networks in an MCTS algorithm (Fig. 3) that selects actions by lookahead search. Each edge is evaluated in two ways: using the value network v_θ; and by running a rollout to the end of the game with the fast rollout policy p_π, then computing the winner with function r. d, Action values Q are updated to track the mean value of all evaluations r(·) and v_θ(·) in the subtree below that action.

(s, a) of the search tree stores an action value Q(s, a), visit count N(s, a), and prior probability P(s, a). The tree is traversed by simulation (that is, descending the tree in complete games without backup), starting from the root state. At each time step t of each simulation, an action a_t is selected from state s_t

$$
a_t = \underset{a}{\operatorname{argmax}} (Q(s_t, a) + u(s_t, a))
$$

so as to maximize action value plus a bonus

$$
u(s, a) \propto \frac{P(s, a)}{1 + N(s, a)}
$$

that is proportional to the prior probability but decays with repeated visits to encourage exploration. When the traversal reaches a leaf node s_L at step L, the leaf node may be expanded. The leaf position s_L is processed just once by the SL policy network p_σ. The output probabilities are stored as prior probabilities P for each legal action a, P(s, a) = p_σ(a|s). The leaf node is evaluated in two very different ways: first, by the value network v_θ(s_L); and second, by the outcome z_L of a random rollout played out until terminal step T using the fast rollout policy p_π; these evaluations are combined, using a mixing parameter λ, into a leaf evaluation V(s_L)

$$
V(s_L) = (1 - \lambda)v_\theta(s_L) + \lambda z_L
$$

At the end of simulation, the action values and visit counts of all traversed edges are updated. Each edge accumulates the visit count and mean evaluation of all simulations passing through that edge

$$
\begin{align*}
N(s, a) &= \sum_{i=1}^n 1(s, a, i) \\
Q(s, a) &= \frac{1}{N(s, a)} \sum_{i=1}^n 1(s, a, i) V(s_L^i)
\end{align*}
$$

where s_L^i is the leaf node from the ith simulation, and 1(s, a, i) indicates whether an edge (s, a) was traversed during the ith simulation. Once the search is complete, the algorithm chooses the most visited move from the root position.

It is worth noting that the SL policy network p_σ performed better in AlphaGo than the stronger RL policy network p_ρ, presumably because humans select a diverse beam of promising moves, whereas RL optimizes for the single best move. However, the value function v_θ(s) ≈ v^{p_ρ}(s) derived from the stronger RL policy network performed

Figure 4 | Tournament evaluation of AlphaGo. a, Results of a tournament between different Go programs (see Extended Data Tables 6–11). Each program used approximately 5 s computation time per move. To provide a greater challenge to AlphaGo, some programs (pale upper bars) were given four handicap stones (that is, free moves at the start of every game) against all opponents. Programs were evaluated on an Elo scale37: a 230 point gap corresponds to a 79% probability of winning, which roughly corresponds to one amateur dan rank advantage on KGS38; an approximate correspondence to human ranks is also shown, better in AlphaGo than a value function $v_{\theta}(s) \approx v^{P_{\sigma}}(s)$ derived from the SL policy network.

Evaluating policy and value networks requires several orders of magnitude more computation than traditional search heuristics. To efficiently combine MCTS with deep neural networks, AlphaGo uses an asynchronous multi-threaded search that executes simulations on CPUs, and computes policy and value networks in parallel on GPUs. The final version of AlphaGo used 40 search threads, 48 CPUs, and 8 GPUs. We also implemented a distributed version of AlphaGo that exploited multiple machines, 40 search threads, 1,202 CPUs and 176 GPUs. The Methods section provides full details of asynchronous and distributed MCTS.

Evaluating the playing strength of AlphaGo
To evaluate AlphaGo, we ran an internal tournament among variants of AlphaGo and several other Go programs, including the strongest commercial programs Crazy Stone13 and Zen, and the strongest open source programs Pachi14 and Fuego15. All of these programs are based horizontal lines show KGS ranks achieved online by that program. Games against the human European champion Fan Hui were also included; these games used longer time controls. 95% confidence intervals are shown. b, Performance of AlphaGo, on a single machine, for different combinations of components. The version solely using the policy network does not perform any search. c, Scalability study of MCTS in AlphaGo with search threads and GPUs, using asynchronous search (light blue) or distributed search (dark blue), for 2 s per move.

Figure 5 | How AlphaGo (black, to play) selected its move in an informal game against Fan Hui. For each of the following statistics, the location of the maximum value is indicated by an orange circle. a, Evaluation of all successors $s'$ of the root position $s$, using the value network $v_{\theta}(s')$; estimated winning percentages are shown for the top evaluations. b, Action values $Q(s, a)$ for each edge $(s, a)$ in the tree from root position $s$; averaged over value network evaluations only ($\lambda = 0$). c, Action values $Q(s, a)$, averaged over rollout evaluations only ($\lambda = 1$).

d, Move probabilities directly from the SL policy network, $p_{\sigma}(a|s)$; reported as a percentage (if above 0.1%). e, Percentage frequency with which actions were selected from the root during simulations. f, The principal variation (path with maximum visit count) from AlphaGo’s search tree. The moves are presented in a numbered sequence. AlphaGo selected the move indicated by the red circle; Fan Hui responded with the move indicated by the white square; in his post-game commentary he preferred the move (labelled 1) predicted by AlphaGo.

Game 1
Fan Hui (Black), AlphaGo (White)
AlphaGo wins by 2.5 points

Game 2
AlphaGo (Black), Fan Hui (White)
AlphaGo wins by resignation

Game 3
Fan Hui (Black), AlphaGo (White)
AlphaGo wins by resignation

Game 4
AlphaGo (Black), Fan Hui (White)
AlphaGo wins by resignation

Game 5
Fan Hui (Black), AlphaGo (White)
AlphaGo wins by resignation

Figure 6 | Games from the match between AlphaGo and the European champion, Fan Hui. Moves are shown in a numbered sequence corresponding to the order in which they were played. Repeated moves on the same intersection are shown in pairs below the board. The first move number in each pair indicates when the repeat move was played, at an intersection identified by the second move number (see Supplementary Information).

on high-performance MCTS algorithms. In addition, we included the open source program GnuGo, a Go program using state-of-the-art search methods that preceded MCTS. All programs were allowed 5 s of computation time per move.

The results of the tournament (see Fig. 4a) suggest that single-machine AlphaGo is many dan ranks stronger than any previous Go program, winning 494 out of 495 games (99.8%) against other Go programs. To provide a greater challenge to AlphaGo, we also played games with four handicap stones (that is, free moves for the opponent); AlphaGo won 77%, 86%, and 99% of handicap games against Crazy Stone, Zen and Pachi, respectively. The distributed version of AlphaGo was significantly stronger, winning 77% of games against single-machine AlphaGo and 100% of its games against other programs.

We also assessed variants of AlphaGo that evaluated positions using just the value network ($\lambda = 0$) or just rollouts ($\lambda = 1$) (see Fig. 4b). Even without rollouts AlphaGo exceeded the performance of all other Go programs, demonstrating that value networks provide a viable alternative to Monte Carlo evaluation in Go. However, the mixed evaluation ($\lambda = 0.5$) performed best, winning $\geq 95$% of games against other variants. This suggests that the two position-evaluation mechanisms are complementary: the value network approximates the outcome of games played by the strong but impractically slow $p_\rho$, while the rollouts can precisely score and evaluate the outcome of games played by the weaker but faster rollout policy $p_\pi$. Figure 5 visualizes the evaluation of a real game position by AlphaGo.

Finally, we evaluated the distributed version of AlphaGo against Fan Hui, a professional 2 dan, and the winner of the 2013, 2014 and 2015 European Go championships. Over 5–9 October 2015 AlphaGo and Fan Hui competed in a formal five-game match. AlphaGo won the match 5 games to 0 (Fig. 6 and Extended Data Table 1). This is the first time that a computer Go program has defeated a human professional player, without handicap, in the full game of Go—a feat that was previously believed to be at least a decade away$^{3,7,31}$.
