---
paper: jacobson-1988-congestion
title: Congestion Avoidance and Control
authors:
  - Van Jacobson
year: 1988
venue: SIGCOMM
field: networks
section: C
section_title: Interaction of window adjustment with round-trip timing
tag: 06CC
kind: appendix
lang: en
source: https://ee.lbl.gov/papers/congavoid.pdf
pdf_sha256: 9ca88dfa60f98d5cf736c3917df45420eb91861dd1de453a3dedf3d91c1836eb
pdf_pages: "21"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 6c2e64e6129ee03525d28896d2da88559cb9d7d0adccfe24fdc86f8e1f93d4e9
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Some TCP connections, particularly those over a very low speed link such as a dial-up SLIP line[25], may experience an unfortunate interaction between congestion window adjustment and retransmit timing: Network paths tend to divide into two classes: delay-dominated, where the store-and-forward and/or transit delays determine the RTT, and bandwidth-dominated, where (bottleneck) link bandwidth and average packet size determine the RTT.$^{20}$ On a bandwidth-dominated path of bandwidth b, a congestion-avoidance window increment of w will increase the RTT of post-increment packets by

$$
R \approx \frac{w}{b}
$$

If the path RTT variation V is small, R may exceed the 4V cushion in rto, a retransmit timeout will occur and, after a few cycles of this, ssthresh (and, thus, cwnd) end up clamped at small values.

The rto calculation in appendix A was designed to prevent this type of spurious retransmission timeout during slow-start. In particular, the RTT variation V is multiplied by four in the rto calculation because of the following: A spurious retransmit occurs if the retransmit timeout computed at the end of slow-start round i, rtoi, is ever less than or equal to the actual RTT of the next round. In the worst case of all the delay being due the window, R doubles each round (since the window size doubles). Thus $R_{i+1} = 2R_i$ (where $R_i$ is the measured RTT at slow-start round i). But

$$
\begin{align*}
V_i &= R_i - R_{i-1} \\
    &= R_i / 2
\end{align*}
$$

and

$$
\begin{align*}
rtoi &= R_i + 4V_i \\
     &= 3R_i \\
     &> 2R_i \\
     &> R_{i+1}
\end{align*}
$$

so spurious retransmit timeouts cannot occur.$^{21}$

\footnotetext{
$^{19}$For TCP this happens automatically since windows are expressed in bytes, not packets. For protocols such as ISO TP4, the implementor should scale cwnd so that the calculations above can be done with integer arithmetic and the scale factor should be large enough to avoid the fixed point (zero) of $[1/cwnd]$ in the congestion avoidance increment.
$^{20}$E.g., TCP over a 2400 baud packet radio link is bandwidth-dominated since the transmission time for a (typical) 576 byte IP packet is 2.4 seconds, longer than any possible terrestrial transit delay.
$^{21}$The original SIGCOMM '88 version of this paper suggested calculating rto as $R + 2V$ rather than $R + 4V$. Since that time we have had much more experience with low speed SLIP links and observed spurious retransmissions during connection startup. An investigation of why these occured led to the analysis above and the change to the rto calculation in app. A.
}
