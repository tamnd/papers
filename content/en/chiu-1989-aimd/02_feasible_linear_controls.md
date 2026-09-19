---
paper: chiu-1989-aimd
title: Analysis of the Increase and Decrease Algorithms for Congestion Avoidance in Computer Networks
authors:
  - Dah-Ming Chiu
  - Raj Jain
year: 1989
venue: Computer Networks and ISDN Systems
field: networks
section: "2"
section_title: Feasible Linear Controls
tag: 03C0
kind: section
lang: en
source: https://www.cse.wustl.edu/~jain/papers/cong_av.htm
pdf_sha256: fd0b0386c611744e744969d3c5ec3e236dc6036344128ed16e7f378a9e257be2
pdf_pages: 6-10
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 0ae39af4a99f833869cc800e52f7e204c4c3794d9596462f2f67c1dbdb19c847
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

### 2.1. Vector Representation of the Dynamics {#chiu-1989-aimd-s2-1 .section tag=03C1}

In determining the set of feasible controls, it is helpful to view the system state transitions as a trajectory through an n-dimensional vector space. We describe this method using a 2-user case, which can be viewed in a 2-dimensional space.

As shown in Fig. 4, any 2-user resource allocation $\{x_1(t), x_2(t)\}$ can be represented as a point $(x_1, x_2)$ in a 2-dimensional space. In this figure, the horizontal axis represents allocations to user 1, and the vertical axis represents allocations to user 2. All allocations for which $x_1 + x_2 = X_{goal}$ are efficient allocations. This corresponds to the straight line marked "efficiency line". All allocations for which $x_1 = x_2$ are fair allocations. This corresponds to the straight line marked "fairness line". The two lines intersect at the point $(X_{goal}/2, X_{goal}/2)$ that is the optimal point. The goal of control schemes should be to bring the system to this point regardless of the starting position.

All points below the efficiency line represent an "underloaded" system and ideally the system would ask users to increase their load. Consider, for example, the point $x_0 = (x_{10}, x_{20})$. The additive increase policy of increasing both users' allocations by $a_1$ corresponds to moving along a $45^\circ$ line. The multiplicative increase policy of increasing both users' allocations by a factor $b_1$ corresponds to moving along the line that connects the origin to the point. Similarly, all points above the efficiency line represent an "overloaded" system and additive decrease is represented by a $45^\circ$ line, while multiplicative decrease is represented by the line joining the point to the origin.

The fairness at any point $(x_1, x_2)$ is given by

$$
\text{Fairness} = \frac{(x_1 + x_2)^2}{2(x_1^2 + x_2^2)}.
$$

Notice that multiplying both allocations by a factor $b$ does not change the fairness. That is, $(bx_1, bx_2)$ has the same fairness as $(x_1, x_2)$ for all values of $b$. Thus, all points on the line joining a point to origin have the same fairness. We, therefore, call a line passing through the origin a "equi-fairness" line. The fairness decreases as the slope of the line either increases above or decreases below the fairness line.

Figure 5 shows a complete trajectory of the two-user system starting from point $x_0$ using an additive increase/multiplicative decrease control policy. The point $x_0$ is below the efficiency line and so both users are asked to increase. They do so additively by moving along at an angle of $45^\circ$. This brings them to $x_1$ which happens to be above the efficiency line. The users are asked to decrease and they do so multiplicatively. This corresponds to moving towards the origin on the line joining $x_1$ and the origin. This brings them to point $x_2$, which happens to be below the efficiency line and the cycle repeats. Notice that $x_2$ has higher fairness than $x_0$. Thus, with every cycle, the fairness increases slightly, and eventually, the system converges to the optimal state in the sense that it keeps oscillating around the goal.

Similar trajectories can be drawn for other control policies. Although not all control policies converge. For example, Fig. 6 shows the trajectory for the additive increase/additive decrease control

Figure.

Fig. 5. Additive Increase/Multiplicative Decrease converges to the optimal point. {#chiu-1989-aimd-fig-5 .figure tag=06D0}

policy starting from the position $x_0$. The system keeps moving back and forth along a $45^\circ$ line through $x_0$. With such a policy, the system can converge to efficiency, but not to fairness. The conditions for convergence to efficiency and fairness are derived algebraically in the next section.

Fig. 6. Additive Increase/Additive Decrease does not converge. {#chiu-1989-aimd-fig-6 .figure tag=06D1}

### 2.2. Convergence to Efficiency {#chiu-1989-aimd-s2-2 .section tag=03C2}

In order to guarantee convergence to efficiency we need to first make sure that at each step the system react correctly to the feedback by moving in the right direction. That is, when the system asks the users to decrease, we should ensure that the total load will not increase and when the system asks the users to increase, the total load will not decrease This is the principle of *negative feedback.* Algebraically:

$$
y(t) = 0 \implies \Sigma x_i(t+1) > \Sigma x_i(t),
$$

$$
y(t) = 1 \implies \Sigma x_i(t+1) < \Sigma x_i(t).
$$

In terms of the policy parameters, this means that the parameter values should be

$$
na_1 + (b_1 + 1)\Sigma x_i(t) > 0 \quad \forall n \text{ and } \forall \Sigma x_i(t),
$$

$$
na_D + (b_D - 1)\Sigma x_i(t) < 0 \quad \forall n \text{ and } \forall \Sigma x_i(t),
$$

or, equivalently,

$$
b_1 > 1 - \frac{na_1}{\Sigma x_i(t)}
$$

$$
b_D < 1 - \frac{na_D}{\Sigma x_i(t)} \quad \forall n \text{ and } \forall \Sigma x_i(t). \tag{3}
$$
{#chiu-1989-aimd-eq-3 .equation tag=03C3}

### 2.3. Convergence to Fairness {#chiu-1989-aimd-s2-3 .section tag=03C4}

Convergence to fairness is defined as moving towards the fairness index of one, i.e.,

$$
F(x(t)) \to 1 \quad \text{as } t \to \infty.
$$

The linear control policies affect the fairness as follows:

$$
F(x(t+1)) = \frac{\Sigma x_i^2(t+1)}{n(\Sigma x_i^2(t+1))} \tag{4}
$$
{#chiu-1989-aimd-eq-4 .equation tag=03C5}

$$
= \frac{(\Sigma a + bx_i(t))^2}{n\Sigma(a + bx_i(t))^2} \tag{5}
$$
{#chiu-1989-aimd-eq-5 .equation tag=03C6}

$$
= \frac{(\Sigma c + x_i(t))^2}{n\Sigma(c + x_i(t))^2}
$$

where $c = a/b$ \tag{6}

$$
= F(x(t)) + (1 - F(x(t))) 
\times \left( 1 - \frac{\Sigma x_i^2(t)}{\Sigma (c + x_i(t))^2} \right). \tag{7}
$$
{#chiu-1989-aimd-eq-7 .equation tag=03C7}

The last expression in the above equation is an increasing function of $c$. Thus, it is sufficient to ensure that $c \geq 0$ to guarantee non-decrease of fairness. Note that $c = 0 \Rightarrow F(x(t+1)) = F(x(t))$, i.e., the fairness stays the same. To ensure convergence to fairness, we require $c > 0$ for either increase or decrease policy. In terms of increase/decrease parameters, this implies

$$
\frac{a_1}{b_1} \geq 0 \quad \text{and} \quad \frac{a_D}{b_D} > 0 \tag{8}
$$
{#chiu-1989-aimd-eq-8 .equation tag=03C8}

or

$$
\frac{a_1}{b_1} > 0 \quad \text{and} \quad \frac{a_D}{b_D} \geq 0. \tag{9}
$$
{#chiu-1989-aimd-eq-9 .equation tag=03C9}

In (8), the fairness goes up during decrease and either goes up or stays the same during increase. Similarly, (9) ensures that fairness goes up during increase and either goes up or stays the same during decrease. This is sufficient to ensure convergence to fairness. We do not need the fairness to go up during both increase and decrease.

Equations (8) and (9) basically state that $a_1$ and $b_1$ should not be of opposite signs. Similarly, $a_D$ and $b_D$ should not be of opposite signs.

To satisfy (8) or (9), it follows that all four parameters $a_1, b_1, a_D,$ and $b_D$ must be positive, for otherwise $x_i(t)$ can become negative. Also,

$$
a_1 \geq 0, \quad b_1 \geq 0,
$$

$$
a_D \geq 0, \quad 0 \leq b_D < 1 \tag{10}
$$
{#chiu-1989-aimd-eq-10 .equation tag=03CA}

where $a_1$ and $b_1$ cannot be both zero, else it would imply zero increase; and $a_1$ and $a_D$ cannot be both zero, else it would imply $c$ is always zero.

### 2.4. Distributedness {#chiu-1989-aimd-s2-4 .section tag=03CB}

The requirement of having no information about system state other than the feedback $y(t)$ further limits the set of feasible linear controls. Since the fairness requirements (Equation (8) or (9)) do not involve any system state, it already satisfies the distributedness criterion. The ef-

2 Note that satisfying the negative feedback condition alone only guarantees that the system will oscillate about the efficiency point, but says nothing about the size of oscillation. So this is strictly speaking weaker than the efficiency condition. We will, however, explore how the oscillation size can be minimized when we talk about the optimality of a policy in the next section.

ficiency convergence conditions stated in (3), however, require knowledge of $\Sigma x_i(t)$ and $n$ at each user. In the absence of such knowledge, each user must try to satisfy the negative feedback condition by itself. This means a stronger condition to guarantee convergence to efficiency:

$$
y(t) = 0 \implies x_i(t+1) > x_i(t) \quad \forall i,
$$

$$
y(t) = 1 \implies x_i(t+1) < x_i(t) \quad \forall i.
\tag{11}
$$
{#chiu-1989-aimd-eq-11 .equation tag=03F8}

Which translates into

$$
a_1 + (b_1 - 1)x_i(t) > 0 \quad \forall x_i(t) \geq 0,
$$

$$
a_D + (b_D - 1)x_i(t) < 0 \quad \forall x_i(t) \geq 0.
$$

This implies further constraining equation (10) to be

$$
a_1 > 0, \quad b_1 \geq 1,
$$

$$
a_D = 0, \quad 0 \leq b_D < 1.
\tag{12}
$$
{#chiu-1989-aimd-eq-12 .equation tag=03F9}

We shall demonstrate these constrains graphically later, using the vector representations.

There is, however, a simple variation for us to make the conditions in (12) less restrictive for parameters $b_1$ and $a_D$. If each user $i$ truncates its control whenever the conditions in (11) would otherwise be violated, as below

$$
x_i(t+1) = \begin{cases}
\max(a_1 + b_1 x_i(t), x_i(t)) \\
\text{if } y(t) = 0 \Rightarrow \text{Increase}, \\
\min(a_D + b_D x_i(t), x_i(t)) \\
\text{if } y(t) = 1 \Rightarrow \text{Decrease},
\end{cases}
\tag{13}
$$
{#chiu-1989-aimd-eq-13 .equation tag=03FA}

then (10) can guarantee both convergence to efficiency with the distributed requirements. There is one catch, however, that is all users could truncate at the same time (thus stopping any progress). To prevent this possibility, let's consider the following conditions:

$$
a_1 + (b_1 - 1)X_{\max} > 0,
$$

$$
N_{\max} a_D + (b_D - 1)X_{\min} < 0
\tag{14}
$$
{#chiu-1989-aimd-eq-14 .equation tag=03FB}

for some $X_{\min}$ and $X_{\max}$ satisfying

$$
X_{\min} \leq X_{\text{goal}} \leq X_{\max}.
\tag{15}
$$
{#chiu-1989-aimd-eq-15 .equation tag=03FC}

Here, $N_{\max}$ is the upper bound on the number of users that would share the resource. The claim is that when (14) and (15) are satisfied, it is impossible for $\sum x_i(t+1) = \sum x_i(t)$.

Let us suppose the contrary is true for the case $y = 0$. This means that

$$
a_1 + b_1 x_i(t) < x_i(t) \quad \forall i
$$

which means

$$
n a_1 + (b_1 - 1) \sum x_i(t) < 0.
$$

Since $a_1, b_1$, and all $x_i$'s are positive, the above inequality is possible only if $b_1 - 1$ is negative and if so, substituting $X_{\max}$ which is more than $\sum x_i(t)$ will make the left-hand side even more negative:

$$
n a_1 + (b_1 - 1) X_{\max} < 0.
$$

This violates (14); thus a contradiction with our assumption.

For the case $y = 1$, if all users truncate, then it means

$$
n a_D + b_D x_i(t) > x_i(t) \quad \forall i,
$$

thus

$$
n a_D + (b_D - 1) \sum x_i(t) > 0.
$$

Since $b_D$ is less than 1, the second term in the left-hand side of the above equation is negative. $y = 1$ implies $\sum x_i(t)$ is greater than $X_{\text{goal}}$, hence $X_{\min}$. Substituting $N_{\max}$ in place of $n$, and $X_{\min}$ in place of $\sum x_i(t)$, should maintain the inequality. That is, we must have

$$
N_{\max} a_D + (b_D - 1) X_{\min} > 0.
$$

This leads to a violation of (14); thus a contradiction.

So the linear controls with truncation leave us with a set of conditions weaker than (12) and stronger than (10):

$$
a_1 > 0, \quad b_1 > 1 - \frac{a_1}{X_{\max}},
$$

$$
0 \leq a_D < (1 - b_D) \frac{X_{\min}}{N_{\max}}, \quad 0 \leq b_D < 1. $$ (16)

Notice that in the case that we do not have any knowledge to bound $X_{\text{goal}}$ or $n$, that simply corresponds to $N_{\max} = \infty, X_{\min} = 0$ and $X_{\max} = \infty$. Then the conditions on linear control with truncation reduce to the same ones as those on the strictly linear control. We have essentially proven the following propositions:

Proposition 1. *In order to satisfy the requirements of distributed convergence to efficiency and fairness without truncation, the linear decrease policy should be multiplicative, and the linear increase policy should always have an additive component, and optionally it may have a multiplicative component with the coefficient no less than one.*

Proposition 2. For the linear controls with truncation (as defined in Equation (13)), the increase and decrease policies can each have both additive and multiplicative components, satisfying the constraints in Equations (16) and (15).

The vectorial representation in the next section should help illustrate these results further.

### 2.5. Vectorial Representation of Feasibility Conditions

The constraint on the control imposed by the efficiency and fairness convergence conditions are depicted in Fig. 7 for the 2-user case. Let us first consider a point in the overloaded region. As shown in Fig. 7(a), the users start at the point $x^H = (x_1^H, x_2^H)$, which is above the efficiency line. The system asks the users to decrease. The line $x_1 + x_2 = x_1^H + x_2^H$ represents an "equi-efficiency" line. All points on this line have the same efficiency as $x^H$. For convergence to efficiency it is sufficient to ensure that the next decrease moves into the shaded area.

The requirement of linear controls and distributedness puts additional restrictions. Linear controls imply that the new state vector $x(t+1)$ is a sum of two vectors corresponding to $a$ and $b x(t)$. In two dimensions, $a$ vector is represented by a 45° line through $x(t)$. This is shown in Fig. 7(b) by the line marked $b = 1$. All future states corresponding to $b = 1$ lie on this line. Points to the left of the line can be reached if and only if we choose $b > 1$. Similarly, points to the right of the line can be reached if $b < 1$. The second vector corresponding to $b x(t)$ is represented by the line marked $a = 0$ in Fig. 7(b). If we choose $a = 0$, the state $x(t+1)$ will lie on this line. Points to the left of this line can be reached by choosing $a < 0$. Similarly, points to the right of this line can be reached by $a > 0$. Depending upon the values of $a$ and $b$, the set of reachable states will lie in one of the four regions formed by the two lines $a = 0$ and $b = 1$. Only one of these four regions, the one corresponding to $a \leq 0$ and $b \leq 1$, is completely below the equi-efficiency line. This region is shown shaded in Fig. 7(b). If we choose parameter values corresponding to other regions, the next state can not be guaranteed to be always below the equi-efficiency line.

For fairness, we note that the points between the fairness line and the line passing through $x^H$ have higher fairness than $x^H$ (see Fig. 7(c)). If we locate the mirror image of $x^H$—the point $x^{H'} = (x_2^H, x_1^H)$—this point has the same fairness as $x^H$, and all points between the fairness line and the line joining $x^{H'}$ have higher fairness than $x^{H'}$. Thus, for convergence to fairness, it is sufficient that the next point be in the region bounded by the two lines joining origin to the points $x^H$ and $x^{H'}$.

Combining the effect of all the restrictions, the region for distributively converging to efficiency and fairness is given by the intersection of the regions shown in Fig. 7(b), and (c), i.e., by the line joining $x^H$ to the origin as shown in Fig. 7(d). Thus the only policies that would distributively satisfy the fairness and efficiency convergence conditions are those that move the operating point along this line. In other words, the decrease must be multiplicative.

Similarly, starting with a point $x_L = (x_1^L, x_2^L)$ in the underloaded region, the region for distributively converging to efficiency and fairness is given by the region shown in Fig. 7(e).

Equations (12), (16), and (15) are basically the algebraic statement of these conditions.
