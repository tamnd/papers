---
paper: jacobson-1988-congestion
title: Congestion Avoidance and Control
authors:
  - Van Jacobson
year: 1988
venue: SIGCOMM
field: networks
section: B
section_title: SLOW-START + CONGESTION AVOIDANCE ALGORITHM
tag: 06CB
kind: appendix
lang: en
source: https://ee.lbl.gov/papers/congavoid.pdf
pdf_sha256: 9ca88dfa60f98d5cf736c3917df45420eb91861dd1de453a3dedf3d91c1836eb
pdf_pages: 20-21
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: e74b99ae0a4812807acdb70102f7102fc24bd7d986cb7a54b83f511d460be2b2
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Using a gain of .25 on the deviation and computing the retransmit timer, rto, as a + 4v, the final timer code looks like:

```text
m -= (sa >> 3);
    sa += m;
    if (m < 0)
        m = -m;
    m -= (sv >> 2);
    sv += m;
    rto = (sa >> 3) + sv;
```

In general this computation will correctly round rto: Because of the sa truncation when computing m – a, sa will converge to the true mean rounded up to the next tick. Likewise with sv. Thus, on the average, there is half a tick of bias in each. The rto computation should be rounded by half a tick and one tick needs to be added to account for sends being phased randomly with respect to the clock. So, the 1.75 tick bias contribution from 4v approximately equals the desired half tick rounding plus one tick phase correction.

B   The combined slow-start with congestion avoidance algorithm

The sender keeps two state variables for congestion control: a slow-start/congestion window, cwnd, and a threshold size, ssthresh, to switch between the two algorithms. The sender’s output routine always sends the minimum of cwnd and the window advertised by the receiver. On a timeout, half the current window size is recorded in ssthresh (this is the multiplicative decrease part of the congestion avoidance algorithm), then cwnd is set to 1 packet (this initiates slow-start). When new data is acked, the sender does if (cwnd < ssthresh)
        /* if we’re still doing slow–start
         * open window exponentially */
        cwnd += 1;
    else
        /* otherwise do Congestion
         * Avoidance increment–by–1 */
        cwnd += 1/cwnd;

Thus slow-start opens the window quickly to what congestion avoidance thinks is a safe operating point (half the window that got us into trouble), then congestion avoidance takes over and slowly increases the window size to probe for more bandwidth becoming available on the path.

Note that the else clause of the above code will malfunction if cwnd is an integer in unscaled, one-packet units. I.e., if the maximum window for the path is w packets, cwnd timer go up quickly and come down slowly, ‘automatically’ giving the behavior suggested in [22]. E.g., see the region between packets 50 and 80 in figure 6.

must cover the range 0..w with resolution of at least 1/w.$^{19}$ Since sending packets smaller than the maximum transmission unit for the path lowers efficiency, the implementor must take care that the fractionally sized cwnd does not result in small packets being sent. In reasonable TCP implementations, existing silly-window avoidance code should prevent runt packets but this point should be carefully checked.
