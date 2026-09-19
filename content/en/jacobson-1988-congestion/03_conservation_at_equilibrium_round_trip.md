---
paper: jacobson-1988-congestion
title: Congestion Avoidance and Control
authors:
  - Van Jacobson
year: 1988
venue: SIGCOMM
field: networks
section: "2"
section_title: 'CONSERVATION AT EQUILIBRIUM: ROUND-TRIP TIMING'
tag: "0257"
kind: section
lang: en
source: https://ee.lbl.gov/papers/congavoid.pdf
pdf_sha256: 9ca88dfa60f98d5cf736c3917df45420eb91861dd1de453a3dedf3d91c1836eb
pdf_pages: 5-7
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 08a37ee83154e5db7adbaaf17b54fe91f93fbfe8aed0da0166884226090cb73f
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Figure 3: Startup behavior of TCP without Slow-start {#jacobson-1988-congestion-fig-3 .figure tag=06BF}

Figure.

Trace data of the start of a TCP conversation between two Sun 3/50s running Sun os 3.5 (the 4.3BSD TCP). The two Suns were on different Ethernets connected by IP gateways driving a 230.4 Kbps point-to-point link (essentially the setup shown in fig. 7). The window size for the connection was 16KB (32 512-byte packets) and there were 30 packets of buffer available at the bottleneck gateway. The actual path contains six store-and-forward hops so the pipe plus gateway queue has enough capacity for a full window but the gateway queue alone does not.
Each dot is a 512 data-byte packet. The x-axis is the time the packet was sent. The y-axis is the sequence number in the packet header. Thus a vertical array of dots indicate back-to-back packets and two dots with the same y but different x indicate a retransmit.
‘Desirable’ behavior on this graph would be a relatively smooth line of dots extending diagonally from the lower left to the upper right. The slope of this line would equal the available bandwidth. Nothing in this trace resembles desirable behavior.
The dashed line shows the 20 KBps bandwidth available for this connection. Only 35% of this bandwidth was used; the rest was wasted on retransmits. Almost everything is retransmitted at least once and data from 54 to 58 KB is sent five times.

first-hop gateway sees a burst of eight packets delivered at 200 times the path bandwidth. This burst of packets often puts the connection into a persistent failure mode of continuous retransmissions (figures 3 and 4).

2  Conservation at equilibrium: round-trip timing

Once data is flowing reliably, problems (2) and (3) should be addressed. Assuming that the protocol implementation is correct, (2) must represent a failure of sender’s retransmit timer. A good round trip time estimator, the core of the retransmit timer, is the single most

2  CONSERVATION AT EQUILIBRIUM: ROUND-TRIP TIMING

Figure 4: Startup behavior of TCP with Slow-start {#jacobson-1988-congestion-fig-4 .figure tag=06C0}

Figure.

Same conditions as the previous figure (same time of day, same Suns, same network path, same buffer and window sizes), except the machines were running the 4.3+TCP with slow-start. No bandwidth is wasted on retransmits but two seconds is spent on the slow-start so the effective bandwidth of this part of the trace is 16 KBps — two times better than figure 3. (This is slightly misleading: Unlike the previous figure, the slope of the trace is 20 KBps and the effect of the 2 second offset decreases as the trace lengthens. E.g., if this trace had run a minute, the effective bandwidth would have been 19 KBps. The effective bandwidth without slow-start stays at 7 KBps no matter how long the trace.)

important feature of any protocol implementation that expects to survive heavy load. And it is frequently botched ([26] and [13] describe typical problems).

One mistake is not estimating the variation, $\sigma_R$, of the round trip time, R. From queuing theory we know that R and the variation in R increase quickly with load. If the load is $\rho$ (the ratio of average arrival rate to average departure rate), R and $\sigma_R$ scale like $(1 - \rho)^{-1}$. To make this concrete, if the network is running at 75% of capacity, as the Arpanet was in last April’s collapse, one should expect round-trip-time to vary by a factor of sixteen ($-2\sigma$ to $+2\sigma$).

The TCP protocol specification[2] suggests estimating mean round trip time via the low-pass filter

$$
R \leftarrow \alpha R + (1 - \alpha) M
$$

where R is the average RTT estimate, M is a round trip time measurement from the most recently acked data packet, and $\alpha$ is a filter gain constant with a suggested value of 0.9. Once the R estimate is updated, the retransmit timeout interval, rto, for the next packet sent is set to $\beta R$.

2  CONSERVATION AT EQUILIBRIUM: ROUND-TRIP TIMING

Figure 5: Performance of an RFC793 retransmit timer {#jacobson-1988-congestion-fig-5 .figure tag=06C1}

Figure.

Trace data showing per-packet round trip time on a well-behaved Arpanet connection. The x-axis is the packet number (packets were numbered sequentially, starting with one) and the y-axis is the elapsed time from the send of the packet to the sender’s receipt of its ack. During this portion of the trace, no packets were dropped or retransmitted. The packets are indicated by a dot. A dashed line connects them to make the sequence easier to follow. The solid line shows the behavior of a retransmit timer computed according to the rules of RFC793.

The parameter $\beta$ accounts for RTT variation (see [5], section 5). The suggested $\beta = 2$ can adapt to loads of at most 30%. Above this point, a connection will respond to load increases by retransmitting packets that have only been delayed in transit. This forces the network to do useless work, wasting bandwidth on duplicates of packets that will eventually be delivered, at a time when it’s known to be having trouble with useful work. I.e., this is the network equivalent of pouring gasoline on a fire.

We developed a cheap method for estimating variation (see appendix A)$^3$ and the resulting retransmit timer essentially eliminates spurious retransmissions. A pleasant side effect of estimating $\beta$ rather than using a fixed value is that low load as well as high load performance improves, particularly over high delay paths such as satellite links (figures 5 and 6).

Another timer mistake is in the backoff after a retransmit: If a packet has to be retransmitted more than once, how should the retransmits be spaced? For a transport endpoint embedded in a network of unknown topology and with an unknown, unknowable and constantly changing population of competing conversations, only one scheme has any hope of working—exponential backoff—but a proof of this is beyond the scope of this paper.$^4$

$^3$ We are far from the first to recognize that transport needs to estimate both mean and variation. See, for example, [6]. But we do think our estimator is simpler than most.

$^4$ See [8]. Several authors have shown that backoffs ‘slower’ than exponential are stable given finite populations and knowledge of the global traffic. However, [17] shows that nothing slower than exponential behavior will work in the general case. To feed your intuition, consider that an IP gateway has essentially the same behavior as the ‘ether’ in an ALOHA net or Ethernet. Justifying exponential retransmit backoff is the same as
