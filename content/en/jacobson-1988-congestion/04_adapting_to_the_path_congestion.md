---
paper: jacobson-1988-congestion
title: Congestion Avoidance and Control
authors:
  - Van Jacobson
year: 1988
venue: SIGCOMM
field: networks
section: "3"
section_title: 'ADAPTING TO THE PATH: CONGESTION AVOIDANCE'
tag: "0258"
kind: section
lang: en
source: https://ee.lbl.gov/papers/congavoid.pdf
pdf_sha256: 9ca88dfa60f98d5cf736c3917df45420eb91861dd1de453a3dedf3d91c1836eb
pdf_pages: 8-10
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: cbeb4e1341872b69c6ca560964150f75e5b76cae37e6f769757028d5c5817f89
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Figure 6: Performance of a Mean+Variance retransmit timer {#jacobson-1988-congestion-fig-6 .figure tag=06C2}

Figure.

Same data as above but the solid line shows a retransmit timer computed according to the algorithm in appendix A.

To finesse a proof, note that a network is, to a very good approximation, a linear system. That is, it is composed of elements that behave like linear operators — integrators, delays, gain stages, etc. Linear system theory says that if a system is stable, the stability is exponential. This suggests that an unstable system (a network subject to random load shocks and prone to congestive collapse5) can be stabilized by adding some exponential damping (exponential timer backoff) to its primary excitation (senders, traffic sources).

3 Adapting to the path: congestion avoidance

If the timers are in good shape, it is possible to state with some confidence that a timeout indicates a lost packet and not a broken timer. At this point, something can be done about (3). Packets get lost for two reasons: they are damaged in transit, or the network is congested and somewhere on the path there was insufficient buffer capacity. On most network paths, loss due to damage is rare ($\ll 1\%$) so it is probable that a packet loss is due to congestion in the network.6 showing that no collision backoff slower than an exponential will guarantee stability on an Ethernet. Unfortunately, with an infinite user population even exponential backoff won’t guarantee stability (although it ‘almost’ does—see [1]). Fortunately, we don’t (yet) have to deal with an infinite user population.

5The phrase congestion collapse (describing a positive feedback instability due to poor retransmit timers) is again the coinage of John Nagle, this time from [[nagle-1984-congestion]].

6Because a packet loss empties the window, the throughput of any window flow control protocol is quite sensitive to damage loss. For an RFC793 standard TCP running with window w (where w is at most the bandwidth-delay product), a loss probability of p degrades throughput by a factor of $(1 + 2pw)^{-1}$. E.g., a 1% damage loss rate on an Arpanet path (8 packet window) degrades TCP throughput by 14%.

The congestion control scheme we propose is insensitive to damage loss until the loss rate is on the order of the window equilibration length (the number of packets it takes the window to regain its original size after a loss). If the pre-loss size is w, equilibration takes roughly $w^2/3$ packets so, for the Arpanet, the loss sensitivity

3 ADAPTING TO THE PATH: CONGESTION AVOIDANCE

A ‘congestion avoidance’ strategy, such as the one proposed in [15], will have two components: The network must be able to signal the transport endpoints that congestion is occurring (or about to occur). And the endpoints must have a policy that decreases utilization if this signal is received and increases utilization if the signal isn’t received.

If packet loss is (almost) always due to congestion and if a timeout is (almost) always due to a lost packet, we have a good candidate for the ‘network is congested’ signal. Particularly since this signal is delivered automatically by all existing networks, without special modification (as opposed to [15] which requires a new bit in the packet headers and a modification to all existing gateways to set this bit).

The other part of a congestion avoidance strategy, the endnode action, is almost identical in the DEC/ISO scheme and our TCP7 and follows directly from a first-order time-series model of the network:8 Say network load is measured by average queue length over fixed intervals of some appropriate length (something near the round trip time). If L_i is the load at interval i, an uncongested network can be modeled by saying L_i changes slowly compared to the sampling time. I.e.,

$$
L_i = N
$$

(N constant). If the network is subject to congestion, this zeroth order model breaks down. The average queue length becomes the sum of two terms, the N above that accounts for the average arrival rate of new traffic and intrinsic delay, and a new term that accounts for the fraction of traffic left over from the last time interval and the effect of this left-over traffic (e.g., induced retransmits):

$$
L_i = N + \gamma L_{i-1}
$$

(These are the first two terms in a Taylor series expansion of L(t). There is reason to believe one might eventually need a three term, second order model, but not until the Internet has grown substantially.)

When the network is congested, $\gamma$ must be large and the queue lengths will start increasing exponentially.9 The system will stabilize only if the traffic sources throttle back at least as quickly as the queues are growing. Since a source controls load in a window-based protocol by adjusting the size of the window, W, we end up with the sender policy

On congestion:

$$
W_i = d W_{i-1} \qquad (d < 1)
$$

I.e., a multiplicative decrease of the window size (which becomes an exponential decrease over time if the congestion persists).

7This is not an accident: We copied Jain’s scheme after hearing his presentation at [10] and realizing that the scheme was, in a sense, universal.
8See any good control theory text for the relationship between a system model and admissible controls for that system. A nice introduction appears in [21], chap. 8.
9I.e., the system behaves like $L_i \approx \gamma L_{i-1}$, a difference equation with the solution

$$
L_n = \gamma^n L_0
$$

which goes exponentially to infinity for any $\gamma > 1$.

threshold is about 5%. At this high loss rate, the empty window effect described above has already degraded throughput by 44% and the additional degradation from the congestion avoidance window shrinking is the least of one’s problems.

We are concerned that the congestion control noise sensitivity is quadratic in w but it will take at least another generation of network evolution to reach window sizes where this will be significant. If experience shows this sensitivity to be a liability, a trivial modification to the algorithm makes it linear in w. An in-progress paper explores this subject in detail.

3 ADAPTING TO THE PATH: CONGESTION AVOIDANCE

If there’s no congestion, γ must be near zero and the load approximately constant. The network announces, via a dropped packet, when demand is excessive but says nothing if a connection is using less than its fair share (since the network is stateless, it cannot know this). Thus a connection has to increase its bandwidth utilization to find out the current limit. E.g., you could have been sharing the path with someone else and converged to a window that gives you each half the available bandwidth. If she shuts down, 50% of the bandwidth will be wasted unless your window size is increased. What should the increase policy be?

The first thought is to use a symmetric, multiplicative increase, possibly with a longer time constant, $W_i = bW_{i-1},\ 1 < b \leq 1/d$. This is a mistake. The result will oscillate wildly and, on the average, deliver poor throughput. The analytic reason for this has to do with that fact that it is easy to drive the net into saturation but hard for the net to recover (what [18], chap. 2.1, calls the rush-hour effect).$^{10}$ Thus overestimating the available bandwidth is costly. But an exponential, almost regardless of its time constant, increases so quickly that overestimates are inevitable.

Without justification, we’ll state that the best increase policy is to make small, constant changes to the window size:$^{11}$

On no congestion:

$$
W_i = W_{i-1} + u \quad (u \ll W_{max})
$$

where $W_{max}$ is the pipesize (the delay-bandwidth product of the path minus protocol overhead — i.e., the largest sensible window for the unloaded path). This is the additive increase / multiplicative decrease policy suggested in [15] and the policy we’ve implemented in TCP. The only difference between the two implementations is the choice of constants for d and u. We used 0.5 and 1 for reasons partially explained in appendix D. A more complete analysis is in yet another in-progress paper.

The preceding has probably made the congestion control algorithm sound hairy but it’s not. Like slow-start, it’s three lines of code:

• On any timeout, set cwnd to half the current window size (this is the multiplicative decrease).

• On each ack for new data, increase cwnd by 1/cwnd (this is the additive increase).$^{12}$

$^{10}$ In fig. 1, note that the ‘pipesize’ is 16 packets, 8 in each path, but the sender is using a window of 22 packets. The six excess packets will form a queue at the entry to the bottleneck and that queue cannot shrink, even though the sender carefully clocks out packets at the bottleneck link rate. This stable queue is another, unfortunate, aspect of conservation: The queue would shrink only if the gateway could move packets into the skinny pipe faster than the sender dumped packets into the fat pipe. But the system tunes itself so each time the gateway pulls a packet off the front of its queue, the sender lays a new packet on the end.

A gateway needs excess output capacity (i.e., $\rho < 1$) to dissipate a queue and the clearing time will scale like $(1 - \rho)^{-2}$ ([18], chap. 2 is an excellent discussion of this). Since at equilibrium our transport connection ‘wants’ to run the bottleneck link at 100% ($\rho = 1$), we have to be sure that during the non-equilibrium window adjustment, our control policy allows the gateway enough free bandwidth to dissipate queues that inevitably form due to path testing and traffic fluctuations. By an argument similar to the one used to show exponential timer backoff is necessary, it’s possible to show that an exponential (multiplicative) window increase policy will be ‘faster’ than the dissipation time for some traffic mix and, thus, leads to an unbounded growth of the bottleneck queue.

$^{11}$ See [4] for a complete analysis of these increase and decrease policies. Also see [8] and [9] for a control-theoretic analysis of a similar class of control policies.

$^{12}$ This increment rule may be less than obvious. We want to increase the window by at most one packet over a time interval of length R (the round trip time). To make the algorithm ‘self-clocked’, it’s better to increment by a small amount on each ack rather than by a large amount at the end of the interval. (Assuming, of course,
