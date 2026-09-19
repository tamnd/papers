---
paper: freund-1997-adaboost
title: A Decision-Theoretic Generalization of On-Line Learning and an Application to Boosting
authors:
  - Yoav Freund
  - Robert E. Schapire
year: 1997
venue: Journal of Computer and System Sciences
field: ai-ml
section: "1"
section_title: INTRODUCTION
tag: 04A1
kind: section
lang: en
source: https://doi.org/10.1006/jcss.1997.1504
pdf_sha256: 01f49de027c4c2c146869da85f8e8482d6b723344cb80ce957d11e93c615e7cc
pdf_pages: 1-2
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 82359e512eda1e7fa1db4be734296be83dec5ed19627f6d0f16fdfce9ba808cb
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

A gambler, frustrated by persistent horse-racing losses and envious of his friends’ winnings, decides to allow a group of his fellow gamblers to make bets on his behalf. He decides he will wager a fixed sum of money in every race, but that he will apportion his money among his friends based on how well they are doing. Certainly, if he knew psychically ahead of time which of his friends would win the most, he would naturally have that friend handle all his wagers. Lacking such clairvoyance, however, he attempts to allocate each race’s wager in such a way that his total winnings for the season will be reasonably close to what he would have won had he bet everything with the luckiest of his friends.

In this paper, we describe a simple algorithm for solving such dynamic allocation problems, and we show that our solution can be applied to a great assortment of learning problems. Perhaps the most surprising of these applications is the derivation of a new algorithm for “boosting,” i.e., for converting a “weak” PAC learning algorithm that performs just slightly better than random guessing into one with arbitrarily high accuracy.

We formalize our *on-line allocation model* as follows. The allocation agent $A$ has $N$ options or *strategies* to choose from; we number these using the integers $1, ..., N$. At each time step $t = 1, 2, ..., T$, the allocator $A$ decides on a distribution $\mathbf{p}^t$ over the strategies; that is $p_i^t \geq 0$ is the amount allocated to strategy $i$, and $\sum_{i=1}^N p_i^t = 1$. Each strategy $i$ then suffers some *loss* $\ell_i^t$ which is determined by the (possibly adversarial) “environment.” The loss suffered by $A$ is then $\sum_{i=1}^N p_i^t \ell_i^t = \mathbf{p}^t \cdot \boldsymbol{\ell}^t$, i.e., the average loss of the strategies with respect to $A$’s chosen allocation rule. We call this loss function the *mixture loss*.

In this paper, we always assume that the loss suffered by any strategy is bounded so that, without loss of generality, $\ell_i^t \in [0, 1]$. Besides this condition, we make no assumptions about the form of the loss vectors $\boldsymbol{\ell}^t$, or about the manner in which they are generated; indeed, the adversary’s choice for $\boldsymbol{\ell}^t$ may even depend on the allocator’s chosen mixture $\mathbf{p}^t$.

The goal of the algorithm $A$ is to minimize its cumulative loss relative to the loss suffered by the best strategy. That is, $A$ attempts to minimize its *net loss*

$$
L_A - \min_i L_i
$$

where

$$
L_A = \sum_{t=1}^T \mathbf{p}^t \cdot \boldsymbol{\ell}^t
$$

is the total cumulative loss suffered by algorithm $A$ on the first $T$ trials, and

$$
L_i = \sum_{t=1}^T \ell_i^t
$$

is strategy $i$’s cumulative loss. In Section 2, we show that Littlestone and Warmuth’s [20] “weighted majority” algorithm can be generalized to

[^1]: An extended abstract of this work appeared in the “Proceedings of the Second European Conference on Computational Learning Theory, Barcelona, March, 1995.”

[^2]: E-mail: {yoav, schapire}@research.att.com.

0022-0000/97 \$25.00  
Copyright © 1997 by Academic Press  
All rights of reproduction in any form reserved.

handle this problem, and we prove a number of bounds on the net loss. For instance, one of our results shows that the net loss of our algorithm can be bounded by $O(\sqrt{T \ln N})$ or, put another way, that the average per trial net loss is decreasing at the rate $O(\sqrt{(\ln N)/T})$. Thus, as $T$ increases, this difference decreases to zero.

Our results for the on-line allocation model can be applied to a wide variety of learning problems, as we describe in Section 3. In particular, we generalize the results of Littlestone and Warmuth [20] and Cesa-Bianchi et al. [4] for the problem of predicting a binary sequence using the advice of a team of “experts.” Whereas these authors proved worst-case bounds for making on-line randomized decisions over a binary decision and outcome space with a $\{0, 1\}$-valued discrete loss, we prove (slightly weaker) bounds that are applicable to any bounded loss function over any decision and outcome spaces. Our bounds express explicitly the rate at which the loss of the learning algorithm approaches that of the best expert.

Related generalizations of the expert prediction model were studied by Vovk [25], Kivinen and Warmuth [19], and Haussler et al. [15]. Like us, these authors focused primarily on multiplicative weight-update algorithms. Chung [5] also presented a generalization, giving the problem a game-theoretic treatment.

Boosting

Returning to the horse-racing story, suppose now that the gambler grows weary of choosing among the experts and instead wishes to create a computer program that will accurately predict the winner of a horse race based on the usual information (number of races recently won by each horse, betting odds for each horse, etc.). To create such a program, he asks his favorite expert to explain his betting strategy. Not surprisingly, the expert is unable to articulate a grand set of rules for selecting a horse. On the other hand, when presented with the data for a specific set of races, the expert has no trouble coming up with a “rule-of-thumb” for that set of races (such as, “Bet on the horse that has recently won the most races” or “Bet on the horse with the most favored odds”). Although such a rule-of-thumb, by itself, is obviously very rough and inaccurate, it is not unreasonable to expect it to provide predictions that are at least a little bit better than random guessing. Furthermore, by repeatedly asking the expert’s opinion on different collections of races, the gambler is able to extract many rules-of-thumb.

In order to use these rules-of-thumb to maximum advantage, there are two problems faced by the gambler: First, how should he choose the collections of races presented to the expert so as to extract rules-of-thumb from the expert that will be the most useful? Second, once he has collected many rules-of-thumb, how can they be combined into a single, highly accurate prediction rule?

Boosting refers to this general problem of producing a very accurate prediction rule by combining rough and moderately inaccurate rules-of-thumb. In the second part of the paper, we present and analyze a new boosting algorithm inspired by the methods we used for solving the on-line allocation problem.

Formally, boosting proceeds as follows: The booster is provided with a set of labelled training examples $(x_1, y_1), ..., (x_N, y_N)$, where $y_i$ is the label associated with instance $x_i$; for instance, in the horse-racing example, $x_i$ might be the observable data associated with a particular horse race, and $y_i$ the outcome (winning horse) of that race. On each round $t = 1, ..., T$, the booster devises a distribution $D_t$ over the set of examples, and requests (from an unspecified oracle) a weak hypothesis (or rule-of-thumb) $h_t$ with low error $\varepsilon_t$ with respect to $D_t$ (that is, $\varepsilon_t = \Pr_{i \sim D_t}[h_t(x_i) \neq y_i]$). Thus, distribution $D_t$ specifies the relative importance of each example for the current round. After $T$ rounds, the booster must combine the weak hypotheses into a single prediction rule.

Unlike the previous boosting algorithms of Freund [10, 11] and Schapire [22], the new algorithm needs no prior knowledge of the accuracies of the weak hypotheses. Rather, it adapts to these accuracies and generates a weighted majority hypothesis in which the weight of each weak hypothesis is a function of its accuracy. For binary prediction problems, we prove in Section 4 that the error of this final hypothesis (with respect to the given set of examples) is bounded by $\exp(-2 \sum_{t=1}^T \gamma_t^2)$ where $\varepsilon_t = 1/2 - \gamma_t$ is the error of the $t$th weak hypothesis. Since a hypothesis that makes entirely random guesses has error $1/2$, $\gamma_t$ measures the accuracy of the $t$th weak hypothesis relative to random guessing. Thus, this bound shows that if we can consistently find weak hypotheses that are slightly better than random guessing, then the error of the final hypothesis drops exponentially fast.

Note that the bound on the accuracy of the final hypothesis improves when *any* of the weak hypotheses is improved. This is in contrast with previous boosting algorithms whose performance bound depended only on the accuracy of the least accurate weak hypothesis. At the same time, if the weak hypotheses all have the same accuracy, the performance of the new algorithm is very close to that achieved by the best of the known boosting algorithms.

In Section 5, we give two extensions of our boosting algorithm to multi-class prediction problems in which each example belongs to one of several possible classes (rather than just two). We also give an extension to regression problems in which the goal is to estimate a real-valued function.
