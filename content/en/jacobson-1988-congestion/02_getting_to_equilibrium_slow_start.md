---
paper: jacobson-1988-congestion
title: Congestion Avoidance and Control
authors:
  - Van Jacobson
year: 1988
venue: SIGCOMM
field: networks
section: "1"
section_title: 'GETTING TO EQUILIBRIUM: SLOW-START'
tag: "0256"
kind: section
lang: en
source: https://ee.lbl.gov/papers/congavoid.pdf
pdf_sha256: 9ca88dfa60f98d5cf736c3917df45420eb91861dd1de453a3dedf3d91c1836eb
pdf_pages: 2-4
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 8e21bae37398576a4a42ae259a5ad6ebfaa7794d059547ffe2fecf06836b4055
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Since that time, we have put seven new algorithms into the 4BSD TCP:

(i) round-trip-time variance estimation
    (ii) exponential retransmit timer backoff
    (iii) slow-start
    (iv) more aggressive receiver ack policy
    (v) dynamic window sizing on congestion
    (vi) Karn’s clamped retransmit backoff
    (vii) fast retransmit

Our measurements and the reports of beta testers suggest that the final product is fairly good at dealing with congested conditions on the Internet.

This paper is a brief description of (i) – (v) and the rationale behind them. (vi) is an algorithm recently developed by Phil Karn of Bell Communications Research, described in [16]. (vii) is described in a soon-to-be-published RFC (ARPANET “Request for Comments”).

Algorithms (i) – (v) spring from one observation: The flow on a TCP connection (or ISO TP-4 or Xerox NS SPP connection) should obey a ‘conservation of packets’ principle. And, if this principle were obeyed, congestion collapse would become the exception rather than the rule. Thus congestion control involves finding places that violate conservation and fixing them.

By ‘conservation of packets’ we mean that for a connection ‘in equilibrium’, i.e., running stably with a full window of data in transit, the packet flow is what a physicist would call ‘conservative’: A new packet isn’t put into the network until an old packet leaves. The physics of flow predicts that systems with this property should be robust in the face of congestion.\footnote{A conservative flow means that for any given time, the integral of the packet density around the sender–receiver–sender loop is a constant. Since packets have to ‘diffuse’ around this loop, the integral is sufficiently continuous to be a Lyapunov function for the system. A constant function trivially meets the conditions for Lyapunov stability so the system is stable and any superposition of such systems is stable. (See [3], chap. 11–12 or [21], chap. 9 for excellent introductions to system stability theory.)} Observation of the Internet suggests that it was not particularly robust. Why the discrepancy?
There are only three ways for packet conservation to fail:

1. The connection doesn’t get to equilibrium, or
2. A sender injects a new packet before an old packet has exited, or
3. The equilibrium can’t be reached because of resource limits along the path.

In the following sections, we treat each of these in turn.

1  Getting to Equilibrium: Slow-start

Failure (1) has to be from a connection that is either starting or restarting after a packet loss. Another way to look at the conservation property is to say that the sender uses acks as a ‘clock’ to strobe new packets into the network. Since the receiver can generate acks no

1  GETTING TO EQUILIBRIUM: SLOW-START

Figure 1: Window Flow Control ‘Self-clocking’ {#jacobson-1988-congestion-fig-1 .figure tag=025A}

Figure.

This is a schematic representation of a sender and receiver on high bandwidth networks connected by a slower, long-haul net. The sender is just starting and has shipped a window’s worth of packets, back-to-back. The ack for the first of those packets is about to arrive back at the sender (the vertical line at the mouth of the lower left funnel).
The vertical dimension is bandwidth, the horizontal dimension is time. Each of the shaded boxes is a packet. Bandwidth × Time = Bits so the area of each box is the packet size. The number of bits doesn’t change as a packet goes through the network so a packet squeezed into the smaller long-haul bandwidth must spread out in time. The time P_b represents the minimum packet spacing on the slowest link in the path (the bottleneck). As the packets leave the bottleneck for the destination net, nothing changes the inter-packet interval so on the receiver’s net packet spacing P_r = P_b. If the receiver processing time is the same for all packets, the spacing between acks on the receiver’s net A_r = P_r = P_b. If the time slot P_b was big enough for a packet, it’s big enough for an ack so the ack spacing is preserved along the return path. Thus the ack spacing on the sender’s net A_s = P_b.
So, if packets after the first burst are sent only in response to an ack, the sender’s packet spacing will exactly match the packet time on the slowest link in the path.

faster than data packets can get through the network, the protocol is ‘self clocking’ (fig. 1). Self clocking systems automatically adjust to bandwidth and delay variations and have a wide dynamic range (important considering that TCP spans a range from 800 Mbps Cray channels to 1200 bps packet radio links). But the same thing that makes a self-clocked system stable when it’s running makes it hard to start — to get data flowing there must be acks to clock out packets but to get acks there must be data flowing.

To start the ‘clock’, we developed a slow-start algorithm to gradually increase the amount of data in-transit.$^2$ Although we flatter ourselves that the design of this algorithm is rather subtle, the implementation is trivial — one new state variable and three lines of code in the sender:

$^2$Slow-start is quite similar to the CUTE algorithm described in [14]. We didn’t know about CUTE at the time we were developing slow-start but we should have—CUTE preceded our work by several months.
When describing our algorithm at the Feb., 1987, Internet Engineering Task Force (IETF) meeting, we called it soft-start, a reference to an electronics engineer’s technique to limit in-rush current. The name slow-start was coined by John Nagle in a message to the IETF mailing list in March, ’87. This name was clearly superior to ours and we promptly adopted it.

1  GETTING TO EQUILIBRIUM: SLOW-START

Figure 2: The Chronology of a Slow-start {#jacobson-1988-congestion-fig-2 .figure tag=06BE}

Figure.

The horizontal direction is time. The continuous time line has been chopped into one-round-trip-time pieces stacked vertically with increasing time going down the page. The grey, numbered boxes are packets. The white numbered boxes are the corresponding acks. As each ack arrives, two packets are generated: one for the ack (the ack says a packet has left the system so a new packet is added to take its place) and one because an ack opens the congestion window by one packet. It may be clear from the figure why an add-one-packet-to-window policy opens the window exponentially in time.
If the local net is much faster than the long haul net, the ack’s two packets arrive at the bottleneck at essentially the same time. These two packets are shown stacked on top of one another (indicating that one of them would have to occupy space in the gateway’s outbound queue). Thus the short-term queue demand on the gateway is increasing exponentially and opening a window of size W packets will require W/2 packets of buffer capacity at the bottleneck.

• Add a congestion window, cwnd, to the per-connection state.

• When starting or restarting after a loss, set cwnd to one packet.

• On each ack for new data, increase cwnd by one packet.

• When sending, send the minimum of the receiver’s advertised window and cwnd.

Actually, the slow-start window increase isn’t that slow: it takes time Rlog₂ W where R is the round-trip-time and W is the window size in packets (fig. 2). This means the window opens quickly enough to have a negligible effect on performance, even on links with a large bandwidth–delay product. And the algorithm guarantees that a connection will source data at a rate at most twice the maximum possible on the path. Without slow-start, by contrast, when 10 Mbps Ethernet hosts talk over the 56 Kbps Arpanet via IP gateways, the
