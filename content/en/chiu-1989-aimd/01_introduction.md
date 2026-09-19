---
paper: chiu-1989-aimd
title: Analysis of the Increase and Decrease Algorithms for Congestion Avoidance in Computer Networks
authors:
  - Dah-Ming Chiu
  - Raj Jain
year: 1989
venue: Computer Networks and ISDN Systems
field: networks
section: "1"
section_title: Introduction
tag: 03B8
kind: section
lang: en
source: https://www.cse.wustl.edu/~jain/papers/cong_av.htm
pdf_sha256: fd0b0386c611744e744969d3c5ec3e236dc6036344128ed16e7f378a9e257be2
pdf_pages: 1-6
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: bebcf15478211066fffb7187dda8552bd12ca9b202dc70b9e0ef3949b57c6ab3
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

### 1.1. Background {#chiu-1989-aimd-s1-1 .section tag=03B9}

Congestion in computer networks is becoming an important issue due to the increasing mismatch in link speeds caused by intermixing of old and new technology. Recent technological advances

Dah-Ming Chiu received the B.Sc. degree with first class honours from Imperial College of Science and Technology, London University, in 1975, and the M.S. and Ph.D. degrees from Harvard University, Cambridge, MA, in 1976 and 1980 respectively.

From 1979 to 1980, he was with AT&T Bell Laboratories, where he worked on applying queuing theory to network modeling. Since 1980, he has been with Digital Equipment Corporation, where he has worked on performance modeling and analysis of computer systems and networks. Currently, he is a member of the Distributed Systems Architecture group, where he is working on the name service architecture and analyzing various distributed algorithms. His research interests include operation systems, distributed systems, computer networks, performance analysis, and optimization theories.

Dr. Chiu is a member of the ACM and the IEEE.

Raj Jain received the B.E. degree from A.P.S. University, Rewa, India, the M.E. degree from Indian Institute of Science, Bangalore, India, and the Ph.D. degree from Harvard University, Cambridge, MA, in 1972, 1974, and 1978, respectively.

His Ph.D. dissertation, entitled "Control Theoretic Formulation of Operating Systems Resource Management Policies," was published by Garland Publishing, Inc. of New York in their "Outstanding Dissertations in the Computer Sciences" series. Since 1978, he has been with Digital Equipment Corporation, where he has been involved in performance modeling and analysis of a number of computer systems and networks including VAX Clusters, DECnet, and Ethernet. Currently, he is a Consulting Engineer in the Distributed Systems Architecture and Performance Group. He spent the 1983-1984 academic year on a sabbatical at the Massachusetts Institute of Technology doing research on the performance of networks and local area systems. For three years he also taught a graduate course on computer systems performance techniques at MIT and is writing a textbook on this subject, to be published by Wiley-Interscience.

Dr. Jain is a member of the Association for Computing Machinery, and a senior member of IEEE.

such as local area networks (LANs) and fiber optic LANs have resulted in a significant increase in the bandwidths of computer network links. However, these new technologies must coexist with the old low bandwidth media such as the twisted pair. This heterogeneity has resulted in a mismatch of arrival and service rates in the intermediate nodes in the network causing increased queuing and congestion.

Traditional congestion control schemes help improve performance after congestion has occurred. Figure 1 shows general patterns of response time and throughput of a network as the network load increases. If the load is small, throughput generally keeps up with the load. As the load increases, throughput increases. After the load reaches the network capacity, throughput stops increasing. If the load is increased any further, the queues start building, potentially resulting in packets being dropped. Throughput may suddenly drop when the load increases beyond this point and the network is said to be congested. The response-time curve follows a similar pattern. At first the response time increases little with load. When the queues start building up, the response time increases linearly until finally, as the queues start overflowing, the response time increases drastically.

The point at which the packets start getting lost is called a cliff due to the fact that the throughput falls off rapidly after this point. We use the term knee to describe the point after which the increase in the throughput is small, but when a significant increase in the response time results.

A scheme that allows the network to operate at the knee is called a congestion avoidance scheme, as distinguished from a congestion control scheme that tries to keep the network operating in the zone to the left of the cliff. A properly designed congestion avoidance scheme will ensure that the users are encouraged to increase their traffic load as long as this does not significantly affect the response time, and are required to decrease them if that happens. Thus, the network load oscillates around the knee.

Both congestion avoidance and congestion control mechanisms are dynamic resource management problems that can be formulated as system control problems in which the system senses its state and feeds this back to its users who adjust their controls. For the congestion problem, the state consists of the load on the network and the control is the number of packets put into the network by the users. Often a window mechanism is used in the transport layer protocols to limit the number of packets put into the network. An alternative mechanism consists of setting a limit on the rate (packets per second or bits per second) that can be sent by a user. In either case, the control (window or rate) can be dynamically adjusted as the total load on the system changes. This control, which we call the increase/decrease algorithm, is at the heart of all congestion avoidance mechanisms.

We have investigated a number of congestion avoidance mechanisms, reported in a series of papers, and this paper is a part of that series [7,8,10,11]. The concept of congestion avoidance and several alternatives are described in [7]. We chose a particular alternative called the "binary feedback scheme" which is described in detail in [11]. This scheme is later extended in [10] to include a "selective feedback" mechanism in which the routers monitor different users and permit some users to increase load while requesting others to decrease load. All of our work on congestion avoidance is summarized in [8].

This paper concentrates on a detailed analysis of the increase/decrease algorithms. This analysis resulted in the selection of the increase/decrease algorithms used in the binary feedback scheme proposed in [11] and [10]. However, the analysis presented here is general and applies to many other applications besides congestion avoidance.

Briefly, the binary feedback scheme for congestion avoidance operates as follows. The resources in the network monitor their usage and determine if they are loaded below or above an optimal load level. Depending upon the load level, the resource sends a binary feedback (1 = overloaded, 0 = underloaded) to the users who then adjust their load using an increase/decrease algorithm. This binary feedback is sent by setting a bit in the packet header. The use of a bit in the packet header as a feedback mechanism has been incorporated into the OSI connectionless networking protocol standards [4]. The bit is called a "congestion experienced bit" and is a part of a field called "quality of service" in the network layer header.

The abstract model assumes that all the users sharing the same bottleneck will receive the same feedback. Based on this feedback, the users try to adjust their load so that the bottleneck is efficiently used as well as equally shared by all users. In this abstracted context, we assume that the feedback and control loop for all users is synchronous, that is, all users receive the same feedback and react to it; the next feedback is then generated after all users have reacted to the feedback and so on. Also, we concentrate on one bottleneck resource and the users that share it. Because of these abstractions, we are able to demonstrate some of the subtle behavior of this type of algorithm. The results presented here were verified by detailed simulations of real networks [7,10,11].

### 1.2. Past Work {#chiu-1989-aimd-s1-2 .section tag=03BA}

The algorithms studied here belong to a class of distributed algorithms for managing distributed

At the other end of the spectrum, we have decentralized decision-making. In this case the decisions are made by the users while the resources feed information regarding current resource usage. Algorithms studied by Jaffe [5] and later extensions by Gafni [2] and Mosely [9] are all good examples of this approach.

In this paper we analyze a class of decentralized decision-making algorithms that are based on a special form of feedback, namely the feedback from the resource is a binary signal. This binary signal indicates whether the resource is currently overloaded or underutilized. A very good reason for considering a binary form of feedback is the motivation of making the controller/manager of the resource as simple and efficient as possible. The requirement of a binary feedback often minimizes the work at the resource in generating the feedback.

### 1.3. Notations and Definitions {#chiu-1989-aimd-s1-3 .section tag=03BB}

Figure 2 shows the assumed model of the network with $n$ users sharing it. The congestion state of the system is determined by the number of packets in the system. We assume a discrete time operation with time divided into small slots. These slots basically represent intervals at the beginning of which the users set their load level based on the network feedback received during the previous interval. If during time slot $t$, the $i$th user's load is $x_i(t)$, then the total load at the bottleneck resource would be $\sum x_i(t)$, and the state of the system is denoted by the $n$-dimensional vector $x(t) = \{ x_1(t), x_2(t), \ldots, x_n(t) \}$. Since we are operating at or near the knee, all resources demanded by the users are granted (this is not true at the cliff). Thus, $x_i(t)$ denotes the $i$th user's

Figure.

Fig. 2. A control system model of $n$ users sharing a network. {#chiu-1989-aimd-fig-2 .figure tag=03BC}

demand as well as allocation of the system's resources. During the interval, the system determines its load level and sends a binary feedback $y(t)$, which is interpreted by the users as follows:

$$
y(t) = \begin{cases}
0 \Rightarrow \text{Increase load}, \\
1 \Rightarrow \text{Decrease load}.
\end{cases}
$$

The users cooperate with the system and change (increase of decrease) their demands by an amount $u_i(t)$. Thus,

$$
x_i(t+1) = x_i(t) + u_i(t).
\tag{1}
$$
{#chiu-1989-aimd-eq-1 .equation tag=03F6}

The change $u_i(t)$ represents $i$th user's control. It is a function of the user's previous demand and the system feedback:

$$
u_i(t) = f(x_i(t),\ y(t)).
\tag{2}
$$
{#chiu-1989-aimd-eq-2 .equation tag=03F7}

In other words,

$$
x_i(t+1) = x_i(t) + f(x_i(t),\ y(t)).
$$

Notice that the users are not aware of other user's individual demands and, thus, cannot make $u_i(t)$ a function of $x_j(t),\ j \neq i$. In general, the control function $f()$ can be any linear or nonlinear function. However, we will focus first on *linear* controls. The state equations (1) reduce to

$$
x_i(t+1)
$$

$$
= \begin{cases}
a_1 + b_1 x_i(t) & \text{if } y(t) = 0 \Rightarrow \text{Increase}, \\
a_D + b_D x_i(t) & \text{if } y(t) = 1 \Rightarrow \text{Decrease}.
\end{cases}
$$

Here, $a_1, b_1, a_D, b_D$ are constants. The following are some examples of the control functions:

(1) *Multiplicative Increase/Multiplicative Decrease*:

$$
x_i(t+1) = \begin{cases}
b_1 x_i(t) & \text{if } y(t) = 0 \Rightarrow \text{Increase}, \\
b_D x_i(t) & \text{if } y(t) = 1 \Rightarrow \text{Decrease}.
\end{cases}
$$

Here, $b_1 > 1$ and $0 < b_D < 1$. All users increase their demands by multiplying their previous demands by a constant factor. The decrease is also multiplicative.

(2) *Additive Increase/Additive Decrease*:

$$
x_i(t+1)
$$

$$
= \begin{cases}
a_1 + x_i(t) & \text{if } y(t) = 0 \Rightarrow \text{Increase}, \\
a_D + x_i(t) & \text{if } y(t) = 1 \Rightarrow \text{Decrease}.
\end{cases}
$$

Here, $a_1 > 0$ and $a_D < 0$. All users increase their demands by adding a constant amount to their previous demands. The decrease is also additive.\footnote{It is assumed that truncation is applied when $a_D + x_i(t)$ is less than zero, so that $x_i(t)$ will never become negative.}

(3) *Additive Increase/Multiplicative Decrease*:

$$
x_i(t+1)
$$

$$
= \begin{cases}
a_1 + x_i(t) & \text{if } y(t) = 0 \Rightarrow \text{Increase}, \\
b_D x_i(t) & \text{if } y(t) = 1 \Rightarrow \text{Decrease}.
\end{cases}
$$

The increase is by a constant amount but the decrease is by a constant factor.

(4) *Multiplicative Increase/Additive Decrease*:

$$
x_i(t+1)
$$

$$
= \begin{cases}
b_1 x_i(t) & \text{if } y(t) = 0 \Rightarrow \text{Increase}, \\
a_D + x_i(t) & \text{if } y(t) = 1 \Rightarrow \text{Decrease}.
\end{cases}
$$

In order to evaluate the effectiveness of these controls, we next define a set of criteria explicitly in the next section.

### 1.4. Criteria for Selecting Controls {#chiu-1989-aimd-s1-4 .section tag=03BD}

The key criteria are: *efficiency*, *fairness*, *distributedness*, and *convergence*. We define them formally as follows:

(1) *Efficiency*: The efficiency of a resource usage is defined by the closeness of the total load on the resource to its knee. If $X_{goal}$ denotes the desired load level at the knee, then the resource is operating efficiently as long as the total allocation $X(t) = \sum x_i(t)$ is close to $X_{goal}$. Overload ($X(t) > X_{goal}$) or underload ($X(t) < X_{goal}$) are both undesirable and are considered inefficient. We consider both as equally undesirable.

Notice, that efficiency relates only to the total allocations and thus two different allocations can both be efficient as long as the total allocation is close to the goal. The distribution of the total allocation among individual users is measured by the fairness criterion.

(2) *Fairness*: The fairness criterion has been widely studied in the literature. When multiple users share multiple resources, the *maxmin fairness* criterion has been widely adopted [2,3,5,10]. Essentially, the set of users are partitioned into equivalent classes according to which resource is their primary bottleneck. The *maxmin* criterion then asserts that the users in the same equivalent class ought to have the equal share of the bottleneck. Thus, a system in which $x_i(t) = x_j(t) \forall i, j$ sharing the same bottleneck is operating fairly. If all users do not get exactly equal allocations, the system is less fair and we need an index or a function that quantifies the fairness. One such index is [6]:

$$
\text{Fairness: } F(x) = \frac{(\sum x_i)^2}{n (\sum x_i^2)}.
$$

This index has the following properties:
(a) The fairness is bounded between 0 and 1 (or 0% and 100%). A totally fair allocation (with all $x_i$'s equal) has a fairness of 1 and a totally unfair allocation (with all resources given to only one user) has a fairness of $1/n$ which is 0 in the limit as $n$ tends to $\infty$.
(b) The fairness is independent of scale, i.e., unit of measurement does not matter.
(c) The fairness is a continuous function. Any slight change in allocation shows up in the fairness.
(d) If only $k$ of $n$ users share the resource equally with the remaining $n - k$ users not receiving any resource, then the fairness is $k/n$.

For other properties of this fairness function, see [6].

(3) *Distributedness*: The next requirement that we put on the control scheme is that it be distributed. A centralized scheme requires complete knowledge of the state of the system. For example, we may want to know each individual user's demand or their sum. This information may be available at the resource. However, conveying this information to each and every user causes considerable overhead, especially since a user may be using several resources at the same time. We are thus primarily interested in control schemes that can be implemented in real networks and, therefore, we assume that the system does the minimum amount of feedback. It only tells whether it is underloaded or overloaded via the binary feedback bits. Other information such as $X_{goal}$ and the number of users sharing the resource are assumed to be unknown by the users. This restricts the set of feasible schemes. We, therefore, describe the set of feasible schemes with and without this restriction.

Figure.

Fig. 3. Responsiveness and smoothness. {#chiu-1989-aimd-fig-3 .figure tag=03BE}

(4) *Convergence*: Finally we require the control scheme to converge. Convergence is generally measured by the speed with which (or time taken till) the system approaches the goal state from any starting state. However, due to the binary nature of the feedback, the system does not generally converge to a single steady state. Rather, the system reaches an "equilibrium" in which it oscillates around the optimal state. The time taken to reach this "equilibrium" and the size of the oscillations jointly determine the convergence. The time determines the *responsiveness*, and the size of the oscillations determine the *smoothness* of the control. Ideally, we would like the time as well as oscillations to be small. Thus, the controls with smaller time and smaller amplitude of oscillations are called more responsive and more smooth, respectively, as shown in Fig. 3.

### 1.5. Outline of this Paper {#chiu-1989-aimd-s1-5 .section tag=03BF}

In this paper, we develop a simple and intuitive methodology to explain when and why a control converges. We address the following questions: *What are all the possible solutions that converge to efficient and fair states? How do we compare those controls that converge?*

The paper is organized as follows. In Section 2 we will characterize the set of all *linear* controls that converge and, thus, identify the set of feasible controls. Then we narrow down the feasible set to a subset that satisfies our distributedness criterion. These subset still includes controls that have unacceptable magnitudes of oscillation or those that converge too slowly. Then in Section 3, we discuss how to find the subset of feasible distributed controls that represent the optimal trade-off of responsiveness and smoothness, as we defined in convergence. In Section 4, we discuss how the results extend to nonlinear controls. And in the last section we summarize the results and discuss some of the practical considerations (such as simplicity, robustness, and scalability).
