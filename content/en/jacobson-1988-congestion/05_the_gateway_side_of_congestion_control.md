---
paper: jacobson-1988-congestion
title: Congestion Avoidance and Control
authors:
  - Van Jacobson
year: 1988
venue: SIGCOMM
field: networks
section: "4"
section_title: THE GATEWAY SIDE OF CONGESTION CONTROL
tag: 06C3
kind: section
lang: en
source: https://ee.lbl.gov/papers/congavoid.pdf
pdf_sha256: 9ca88dfa60f98d5cf736c3917df45420eb91861dd1de453a3dedf3d91c1836eb
pdf_pages: 11-13
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 88840c85b5de42188042ab7f1db564728fc1022c41991cf5e87125b1868bd44b
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

• When sending, send the minimum of the receiver’s advertised window and cwnd.

Note that this algorithm is only congestion avoidance, it doesn’t include the previously described slow-start. Since the packet loss that signals congestion will result in a re-start, it will almost certainly be necessary to slow-start in addition to the above. But, because both congestion avoidance and slow-start are triggered by a timeout and both manipulate the congestion window, they are frequently confused. They are actually independent algorithms with completely different objectives. To emphasize the difference, the two algorithms have been presented separately even though in practise they should be implemented together. Appendix B describes a combined slow-start/congestion avoidance algorithm.13

Figures 7 through 12 show the behavior of TCP connections with and without congestion avoidance. Although the test conditions (e.g., 16 KB windows) were deliberately chosen to stimulate congestion, the test scenario isn’t far from common practice: The Arpanet IMP end-to-end protocol allows at most eight packets in transit between any pair of gateways. The default 4.3BSD window size is eight packets (4 KB). Thus simultaneous conversations between, say, any two hosts at Berkeley and any two hosts at MIT would exceed the network capacity of the UCB–MIT IMP path and would lead14 to the type of behavior shown.

4 Future work: the gateway side of congestion control

While algorithms at the transport endpoints can insure the network capacity isn’t exceeded, they cannot insure fair sharing of that capacity. Only in gateways, at the convergence of flows, is there enough information to control sharing and fair allocation. Thus, we view the gateway ‘congestion detection’ algorithm as the next big step.

the sender has effective silly window avoidance (see [5], section 3) and doesn’t attempt to send packet fragments because of the fractionally sized window.) A window of size cwnd packets will generate at most cwnd acks in one R. Thus an increment of 1/cwnd per ack will increase the window by at most one packet in one R. In TCP, windows and packet sizes are in bytes so the increment translates to maxseg*maxseg/cwnd where maxseg is the maximum segment size and cwnd is expressed in bytes, not packets.

13 We have also developed a rate-based variant of the congestion avoidance algorithm to apply to connection-less traffic (e.g., domain server queries, RPC requests). Remembering that the goal of the increase and decrease policies is bandwidth adjustment, and that ‘time’ (the controlled parameter in a rate-based scheme) appears in the denominator of bandwidth, the algorithm follows immediately: The multiplicative decrease remains a multiplicative decrease (e.g., double the interval between packets). But subtracting a constant amount from interval does not result in an additive increase in bandwidth. This approach has been tried, e.g., [19] and [24], and appears to oscillate badly. To see why, note that for an inter-packet interval I and decrement c, the bandwidth change of a decrease-interval-by-constant policy is

$$
\frac{1}{I} \rightarrow \frac{1}{I - c}
$$

a non-linear, and destabilizing, increase.

An update policy that does result in a linear increase of bandwidth over time is

$$
I_i = \frac{\alpha I_{i-1}}{\alpha + I_{i-1}}
$$

where $I_i$ is the interval between sends when the ith packet is sent and $\alpha$ is the desired rate of increase in packets per packet/sec.

We have simulated the above algorithm and it appears to perform well. To test the predictions of that simulation against reality, we have a cooperative project with Sun Microsystems to prototype RPC dynamic congestion control algorithms using NFS as a test-bed (since NFS is known to have congestion problems yet it would be desirable to have it work over the same range of networks as TCP).

14 did lead.

4 THE GATEWAY SIDE OF CONGESTION CONTROL

Figure 7: Multiple conversation test setup {#jacobson-1988-congestion-fig-7 .figure tag=06C4}

Figure.

Test setup to examine the interaction of multiple, simultaneous TCP conversations sharing a bottleneck link. 1 MByte transfers (2048 512-data-byte packets) were initiated 3 seconds apart from four machines at LBL to four machines at UCB, one conversation per machine pair (the dotted lines above show the pairing). All traffic went via a 230.4 Kbps link connecting IP router csam at LBL to IP router cartan at UCB. The microwave link queue can hold up to 50 packets. Each connection was given a window of 16 KB (32 512-byte packets). Thus any two connections could overflow the available buffering and the four connections exceeded the queue capacity by 160%.

The goal of this algorithm to send a signal to the endnodes as early as possible, but not so early that the gateway becomes starved for traffic. Since we plan to continue using packet drops as a congestion signal, gateway ‘self protection’ from a mis-behaving host should fall-out for free: That host will simply have most of its packets dropped as the gateway trys to tell it that it’s using more than its fair share. Thus, like the endnode algorithm, the gateway algorithm should reduce congestion even if no endnode is modified to do congestion avoidance. And nodes that do implement congestion avoidance will get their fair share of bandwidth and a minimum number of packet drops.

Since congestion grows exponentially, detecting it early is important. If detected early, small adjustments to the senders’ windows will cure it. Otherwise massive adjustments are necessary to give the net enough spare capacity to pump out the backlog. But, given the bursty nature of traffic, reliable detection is a non-trivial problem. Jain[15] proposes a scheme based on averaging between queue regeneration points. This should yield good burst filtering but we think it might have convergence problems under high load or significant second-order dynamics in the traffic.\footnote{These problems stem from the fact that the average time between regeneration points scales like $(1-\rho)^{-1}$ and the variance like $(1-\rho)^{-3}$ (see Feller[7], chap. VI.9). Thus the congestion detector becomes sluggish as congestion increases and its signal-to-noise ratio decreases dramatically.} We plan to use some of our earlier work on ARMAX models for round-trip-time/queue length prediction as the basis of detection.

Figure 8: Multiple, simultaneous TCPs with no congestion avoidance {#jacobson-1988-congestion-fig-8 .figure tag=06C5}

Figure.

Trace data from four simultaneous TCP conversations without congestion avoidance over the paths shown in figure 7. 4,000 of 11,000 packets sent were retransmissions (i.e., half the data packets were retransmitted). Since the link data bandwidth is 25 KBps, each of the four conversations should have received 6 KBps. Instead, one conversation got 8 KBps, two got 5 KBps, one got 0.5 KBps and 6 KBps has vanished.

Preliminary results suggest that this approach works well at high load, is immune to second-order effects in the traffic and is computationally cheap enough to not slow down kilopacket-per-second gateways.
