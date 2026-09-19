---
paper: chiu-1989-aimd
title: Analysis of the Increase and Decrease Algorithms for Congestion Avoidance in Computer Networks
authors:
  - Dah-Ming Chiu
  - Raj Jain
year: 1989
venue: Computer Networks and ISDN Systems
field: networks
section: "3"
section_title: Optimizing the Control Schemes
tag: 03CF
kind: section
lang: en
source: https://www.cse.wustl.edu/~jain/papers/cong_av.htm
pdf_sha256: fd0b0386c611744e744969d3c5ec3e236dc6036344128ed16e7f378a9e257be2
pdf_pages: 10-12
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: aa48e445c4e088a63da2ed0fc119648abd29977f59a4b4839b4b7e86da661534
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Having established the feasible control region, the next step is to determine the optimal policy—a policy that takes the system to the goal quickly. In this section, therefore, we discuss the selection of control parameters to minimize the time to convergence and to minimize the oscillations.

### 3.1. Optimal Convergence to Efficiency {#chiu-1989-aimd-s3-1 .section tag=03D0}

In this subsection, we deal exclusively with the tradeoff of time to converge to efficiency, $t_e$, with the oscillation size, $s_e$. More figuratively, we also refer to these two metrics as *responsiveness* and *smoothness*, respectively.

The $n$ state equations corresponding for $n$ users are

$$
x_i(t+1) = a + b x_i(t), \quad i = 1, 2, \ldots, n.
$$

(a) Convergence to Efficiency
Equi-Efficiency Line

(b) Distributed Convergence to Efficiency

(c) Convergence to Fairness
Fairness Line

(d) Distributed Convergence to Efficiency and Fairness

(e) Increase

Fig. 7. Vectorial representation of efficiency and fairness feasibility conditions. {#chiu-1989-aimd-fig-7 .figure tag=06D2}

These $n$ equations can be added to form a single state equation:

$$
\Sigma x_i(t+1) = na + b \Sigma x_i(t)
$$

or,

$$
X(t+1) = na + b X(t) \quad \text{where } X = \Sigma x_i.
$$

Given initial state $X(0)$, the time to reach $X_{goal}$ is

$$
t_e = \begin{cases}
\frac{\log \left( \frac{an + (b-1) X_{goal}}{an + (b-1) X(0)} \right)}{\log(b)}, & b > 0, \\
\frac{X_{goal} - X(0)}{an}, & b = 0.
\end{cases}
$$

After converging to $X_{goal}$ there will be a maximum overshoot of

$$
s_e = |an + (b-1) X_{goal}|.
$$

Notice that $t_e$ is a monotonically decreasing function of $a$ and $b$, while $s_e$ is a monotonically increasing function of $a$ and $b$. Thus, any attempt to increase responsiveness (decrease $t_e$) also results in decreased smoothness (increased $s_e$), and vice versa.

### 3.2. *Optimal Convergence to Fairness* {#chiu-1989-aimd-s3-2 .section tag=03D1}

Equation (7) shows that the per step improvement in fairness $F(x(t-1)) - F(x(t))$ is a monotonically increasing function of $c = a/b$. Thus, larger values of $a$ and smaller values $b$ give quicker convergence to fairness.

For the case of strict linear controls, this leads to an elegantly simple conclusion. For decrease, feasibility conditions required $a_D = 0$. Thus, the fairness remains the same at every decrease step and the parameter $b_D$ has no effect on time to converge to a fair state. For increase, smaller $b_1$ results in quicker convergence to fairness. Thus, the optimal value of $b_1$ is its minimum value—one. (See Equation (12).) Choosing $b_1 = 1$ is equivalent to saying that additive increase gives us the quickest convergence to fairness. This result can be formally stated as:

**Proposition 3.** *For both feasibility and optimal convergence to fairness, the increase policy should be additive and the decrease policy should be multiplicative.* {#chiu-1989-aimd-prop-3 .statement tag=03D2}

This is in fact the form of the control we are proposing for our congestion avoidance schemes [10,11].
