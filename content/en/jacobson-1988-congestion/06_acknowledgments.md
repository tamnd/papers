---
paper: jacobson-1988-congestion
title: Congestion Avoidance and Control
authors:
  - Van Jacobson
year: 1988
venue: SIGCOMM
field: networks
section_title: Acknowledgments
kind: section
lang: en
source: https://ee.lbl.gov/papers/congavoid.pdf
pdf_sha256: 9ca88dfa60f98d5cf736c3917df45420eb91861dd1de453a3dedf3d91c1836eb
pdf_pages: 13-17
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: a9d9ed7f2ac584c295e91ff3c7d79bd62a9b568c2fea64b407495e469a5a3516
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

We are grateful to the members of the Internet Activity Board’s End-to-End and Internet-Engineering task forces for this past year’s interest, encouragement, cogent questions and network insights. Bob Braden of ISI and Craig Partridge of BBN were particularly helpful in the preparation of this paper: their careful reading of early drafts improved it immensely.

The first author is also deeply in debt to Jeff Mogul of DEC Western Research Lab. Without Jeff’s interest and patient prodding, this paper would never have existed.

Figure 9: Multiple, simultaneous TCPs with congestion avoidance {#jacobson-1988-congestion-fig-9 .figure tag=06C6}

Figure.

Trace data from four simultaneous TCP conversations using congestion avoidance over the paths shown in figure 7. 89 of 8281 packets sent were retransmissions (i.e., 1% of the data packets had to be retransmitted). Two of the conversations got 8 KBps and two got 4.5 KBps (i.e., all the link bandwidth is accounted for — see fig. 11). The difference between the high and low bandwidth senders was due to the receivers. The 4.5 KBps senders were talking to 4.3BSD receivers which would delay an ack until 35% of the window was filled or 200 ms had passed (i.e., an ack was delayed for 5–7 packets on the average). This meant the sender would deliver bursts of 5–7 packets on each ack.
The 8 KBps senders were talking to 4.3+BSD receivers which would delay an ack for at most one packet (because of an ack’s ‘clock’ rôle, the authors believe that the minimum ack frequency should be every other packet). I.e., the sender would deliver bursts of at most two packets. The probability of loss increases rapidly with burst size so senders talking to old-style receivers saw three times the loss rate (1.8% vs. 0.5%). The higher loss rate meant more time spent in retransmit wait and, because of the congestion avoidance, smaller average window sizes.

Figure 10: Total bandwidth used by old and new TCPs {#jacobson-1988-congestion-fig-10 .figure tag=06C7}

Figure.

The thin line shows the total bandwidth used by the four senders without congestion avoidance (fig. 8), averaged over 5 second intervals and normalized to the 25 KBps link bandwidth. Note that the senders send, on the average, 25% more than will fit in the wire. The thick line is the same data for the senders with congestion avoidance (fig. 9). The first 5 second interval is low (because of the slow-start), then there is about 20 seconds of damped oscillation as the congestion control 'regulator' for each TCP finds the correct window size. The remaining time the senders run at the wire bandwidth. (The activity around 110 seconds is a bandwidth 're-negotiation' due to connection one shutting down. The activity around 80 seconds is a reflection of the 'flat spot' in fig. 9 where most of conversation two's bandwidth is suddenly shifted to conversations three and four — competing conversations frequently exhibit this type of 'punctuated equilibrium' behavior and we hope to investigate its dynamics in a future paper.)

Figure 11: Effective bandwidth of old and new TCPs {#jacobson-1988-congestion-fig-11 .figure tag=06C8}

Figure.

Figure 10 showed the old TCPs were using 25% more than the bottleneck link bandwidth. Thus, once the bottleneck queue filled, 25% of the the senders’ packets were being discarded. If the discards, and only the discards, were retransmitted, the senders would have received the full 25 KBps link bandwidth (i.e., their behavior would have been anti-social but not self-destructive). But fig. 8 noted that around 25% of the link bandwidth was unaccounted for. Here we average the total amount of data acked per five second interval. (This gives the effective or delivered bandwidth of the link.) The thin line is once again the old TCPs. Note that only 75% of the link bandwidth is being used for data (the remainder must have been used by retransmissions of packets that didn’t need to be retransmitted). The thick line shows delivered bandwidth for the new TCPs. There is the same slow-start and turn-on transient followed by a long period of operation right at the link bandwidth.

Figure 12: Window adjustment detail {#jacobson-1988-congestion-fig-12 .figure tag=06C9}

Figure.

Because of the five second averaging time (needed to smooth out the spikes in the old TCP data), the congestion avoidance window policy is difficult to make out in figures 10 and 11. Here we show effective throughput (data acked) for TCPs with congestion control, averaged over a three second interval.
When a packet is dropped, the sender sends until it fills the window, then stops until the retransmission timeout. Since the receiver cannot ack data beyond the dropped packet, on this plot we’d expect to see a negative-going spike whose amplitude equals the sender’s window size (minus one packet). If the retransmit happens in the next interval (the intervals were chosen to match the retransmit timeout), we’d expect to see a positive-going spike of the same amplitude when receiver acks the out-of-order data it cached. Thus the height of these spikes is a direct measure of the sender’s window size.
The data clearly shows three of these events (at 15, 33 and 57 seconds) and the window size appears to be decreasing exponentially. The dotted line is a least squares fit to the six window size measurements obtained from these events. The fit time constant was 28 seconds. (The long time constant is due to lack of a congestion avoidance algorithm in the gateway. With a ‘drop’ algorithm running in the gateway, the time constant should be around 4 seconds)
