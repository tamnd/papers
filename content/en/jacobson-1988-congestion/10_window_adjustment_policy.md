---
paper: jacobson-1988-congestion
title: Congestion Avoidance and Control
authors:
  - Van Jacobson
year: 1988
venue: SIGCOMM
field: networks
section: D
section_title: WINDOW ADJUSTMENT POLICY
tag: 06CD
kind: appendix
lang: en
source: https://ee.lbl.gov/papers/congavoid.pdf
pdf_sha256: 9ca88dfa60f98d5cf736c3917df45420eb91861dd1de453a3dedf3d91c1836eb
pdf_pages: 22-23
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: b06b8b3f4ea61169c6e9553902159e778dac6778811c144ad9c22c1906522098
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Spurious retransmission due to a window increase can occur during the congestion avoidance window increment since the window can only be changed in one packet increments so, for a packet size s, there may be as many as s − 1 packets between increments, long enough for any V increase due to the last window increment to decay away to nothing. But this problem is unlikely on a bandwidth-dominated path since the increments would have to be more than twelve packets apart (the decay time of the V filter times its gain in the rto calculation) which implies that a ridiculously large window is being used for the path.22 Thus one should regard these timeouts as appropriate punishment for gross mis-tuning and their effect will simply be to reduce the window to something more appropriate for the path.

Although slow-start and congestion avoidance are designed to not trigger this kind of spurious retransmission, an interaction with higher level protocols frequently does: Application protocols like SMTP and NNTP have a ‘negotiation’ phase where a few packets are exchanged stop-and-wait, followed by data transfer phase where all of a mail message or news article is sent. Unfortunately, the ‘negotiation’ exchanges open the congestion window so the start of the data transfer phase will dump several packets into the network with no slow-start and, on a bandwidth-dominated path, faster than rto can track the RTT increase caused by these packets. The root cause of this problem is the same one described in sec. 1: dumping too many packets into an empty pipe (the pipe is empty since the negotiation exchange was conducted stop-and-wait) with no ack ‘clock’. The fix proposed in sec. 1, slow-start, will also prevent this problem if the TCP implementation can detect the phase change. And detection is simple: The pipe is empty because we haven’t sent anything for at least a round-trip-time (another way to view RTT is as the time it takes the pipe to empty after the most recent send). So, if nothing has been sent for at least one RTT, the next send should set cwnd to one packet to force a slow-start. I.e., if the connection state variable lastsnd holds the time the last packet was sent, the following code should appear early in the TCP output routine:

```text
int idle = (snd_max == snd_una);
if (idle && now − lastsnd > rto)
    cwnd = 1;
```

The boolean idle is true if there is no data in transit (all data sent has been acked) so the if says “if there’s nothing in transit and we haven’t sent anything for ‘a long time’, slow-start.” Our experience has been that either the current RTT estimate or the rto estimate can be used for ‘a long time’ with good results23

D  Window Adjustment Policy

A reason for using $\frac{1}{2}$ as a the decrease term, as opposed to the $\frac{7}{8}$ in [15], was the following handwaving: When a packet is dropped, you’re either starting (or restarting after a drop) or steady-state sending. If you’re starting, you know that half the current window size ‘worked’, i.e., that a window’s worth of packets were exchanged with no drops (slow-start guarantees this). Thus on congestion you set the window to the largest size that you know works then slowly increase the size. If the connection is steady-state running and

22 The the largest sensible window for a path is the bottleneck bandwidth times the round-trip delay and, by definition, the delay is negligible for a bandwidth-dominated path so the window should only be a few packets.
23 The rto estimate is more convenient since it is kept in units of time while RTT is scaled.

a packet is dropped, it’s probably because a new connection started up and took some of your bandwidth. We usually run our nets with $\rho \leq 0.5$ so it’s probable that there are now exactly two conversations sharing the bandwidth. I.e., you should reduce your window by half because the bandwidth available to you has been reduced by half. And, if there are more than two conversations sharing the bandwidth, halving your window is conservative — and being conservative at high traffic intensities is probably wise.

Although a factor of two change in window size seems a large performance penalty, in system terms the cost is negligible: Currently, packets are dropped only when a large queue has formed. Even with the ISO IP ‘congestion experienced’ bit [11] to force senders to reduce their windows, we’re stuck with the queue because the bottleneck is running at 100% utilization with no excess bandwidth available to dissipate the queue. If a packet is tossed, some sender shuts up for two RTT, exactly the time needed to empty the queue. If that sender restarts with the correct window size, the queue won’t reform. Thus the delay has been reduced to minimum without the system losing any bottleneck bandwidth.

The 1-packet increase has less justification than the 0.5 decrease. In fact, it’s almost certainly too large. If the algorithm converges to a window size of w, there are $O(w^2)$ packets between drops with an additive increase policy. We were shooting for an average drop rate of < 1% and found that on the Arpanet (the worst case of the four networks we tested), windows converged to 8–12 packets. This yields 1 packet increments for a 1% average drop rate.

But, since we’ve done nothing in the gateways, the window we converge to is the maximum the gateway can accept without dropping packets. I.e., in the terms of [15], we are just to the left of the cliff rather than just to the right of the knee. If the gateways are fixed so they start dropping packets when the queue gets pushed past the knee, our increment will be much too aggressive and should be dropped by about a factor of four (since our measurements on an unloaded Arpanet place its ‘pipe size’ at 4–5 packets). It appears trivial to implement a second order control loop to adaptively determine the appropriate increment to use for a path. But second order problems are on hold until we’ve spent some time on the first order part of the algorithm for the gateways.
