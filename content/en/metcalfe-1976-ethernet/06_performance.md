---
paper: metcalfe-1976-ethernet
title: 'Ethernet: Distributed Packet Switching for Local Computer Networks'
authors:
  - Robert M. Metcalfe
  - David R. Boggs
year: 1976
venue: Communications of the ACM
field: networks
section: "6"
section_title: Performance
tag: 02AF
kind: section
lang: en
source: https://www.cl.cam.ac.uk/teaching/0809/DigiCommI/metcalfe1976ethernet.pdf
pdf_sha256: e1e9d67146a1d0955a39b4fbb8e2951d6cefb4f7231a01acb9c78852280da227
pdf_pages: 6-8
extraction: vision
extraction_model: gpt-5
content_sha256: 060b2ce77214436db2b11b86e95d8353eacf4900ed56e0054fe464edc977d5e1
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

We present here a simple set of formulas with which to characterize the performance expected of an Ethernet when it is heavily loaded. More elaborate analyses and several detailed simulations have been done, but the following simple model has proven very useful in understanding the Ethernet’s distributed contention scheme, even when it is loaded beyond expectations [1, 20, 21, 22, 23, 27].

We develop a simple model of the performance of a loaded Ethernet by examining alternating Ether time periods. The first, called a *transmission interval*, is that

Communications  
of the ACM

July 1976  
Volume 19 during which the Ether has been acquired for a successful packet transmission. The second, called a *contention interval*, is that composed of the retransmission slots of Section 4.4, during which stations attempt to acquire control of the Ether. Because the model’s Ethernets are loaded and because stations defer to passing packets before starting transmission, the slots are synchronized by the tail of the preceding acquisition interval. A slot will be empty when no station chooses to attempt transmission in it and it will contain a collision if more than one station attempts to transmit. When a slot contains only one attempted transmission, then the Ether has been acquired for the duration of a packet, the contention interval ends, and a transmission interval begins.

Let $P$ be the number of bits in an Ethernet *packet*. Let $C$ be the peak *capacity* in bits per second, carried on the Ether. Let $T$ be the *time* in seconds of a slot, the number of seconds it takes to detect a collision after starting a transmission. Let us assume that there are $Q$ stations continuously *queued* to transmit a packet; either the acquiring station has a new packet immediately after a successful acquisition or another station comes ready. Note that $Q$ also happens to give the total *offered load* on the network which for this analysis is always 1 or greater. We assume that a queued station attempts to transmit in the current slot with probability $1/Q$, or delays with probability $1-(1/Q)$; this is known

Fig. 3. Collision control algorithm. {#metcalfe-1976-ethernet-fig-3 .figure tag=02B0}

### 6.1 Acquisition Probability {#metcalfe-1976-ethernet-s6-1 .section tag=02B1}

We now compute $A$, the probability that exactly one station attempts a transmission in a slot and therefore *acquires* the Ether. $A$ is $Q*(1/Q)*((1-(1/Q))**(Q-1))$; there are $Q$ ways in which one station can choose to transmit (with probability $(1/Q)$) while $Q-1$ stations choose to wait (with probability $1-(1/Q)$). Simplifying,

$$
A=(1-(1/Q))^{(Q-1)}.
$$

### 6.2 Waiting Time {#metcalfe-1976-ethernet-s6-2 .section tag=02B2}

We now compute $W$, the mean number of slots of *waiting* in a contention interval before a successful acquisition of the Ether by a station’s transmission. The probability of waiting no time at all is just $A$, the probability that one and only one station chooses to transmit in the first slot following a transmission. The probability of waiting 1 slot is $A*(1-A)$; the probability of waiting $i$ slots is $A*((1-A)**i)$. The mean of this geometric distribution is

$$
W=(1-A)/A.
$$

### 6.3 Efficiency {#metcalfe-1976-ethernet-s6-3 .section tag=02B3}

We now compute $E$, that fraction of time the Ether is carrying good packets, the *efficiency*. The Ether’s time is divided between transmission intervals and contention intervals. A packet transmission takes $P/C$ seconds. The mean time to acquisition is $W*T$. Therefore, by our simple model,

$$
E=(P/C)/((P/C)+(W*T)).
$$

Table I presents representative performance figures (i.e. $E$) for our experimental Ethernet with the indicated packet sizes and number of *continuously queued* stations. The efficiency figures given do not account for inevitable reductions due to headers and control packets nor for losses due to imprecise control of the retransmission parameter $1/Q$; the former is straightforwardly protocol-dependent and the latter requires analysis beyond the scope of this paper. Again, we feel that all of the Ethernets in the table are overloaded; normally loaded Ethernets will usually have a $Q$ much less than 1 and exhibit behavior not covered by this model.

For our calculations we use a $C$ of 3 megabits per second and a $T$ of 16 microseconds. The slot duration $T$ must be long enough to allow a collision to be detected or at least twice the Ether’s round trip time. We limit in software the maximum length of our packets to be near 4000 bits to keep the latency of network access down and to permit efficient use of station packet buffer storage.

For packets whose size is above 4000 bits, the efficiency of our experimental Ethernet stays well above 95

Communications  
of  
the ACM

July 1976  
Volume 19 percent. For packets with a size approximating that of a slot, Ethernet efficiency approaches $1/e$, the asymptotic efficiency of a slotted Aloha network [27].
