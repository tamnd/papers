---
paper: bosshart-2014-p4
title: 'P4: Programming Protocol-Independent Packet Processors'
authors:
  - Pat Bosshart
  - Dan Daly
  - Glen Gibb
  - Martin Izzard
  - Nick McKeown
  - Jennifer Rexford
  - Cole Schlesinger
  - Dan Talayco
  - Amin Vahdat
  - George Varghese
  - David Walker
year: 2014
venue: ACM SIGCOMM Computer Communication Review
field: networks
section: "2"
section_title: ABSTRACT FORWARDING MODEL
tag: "0090"
kind: section
lang: en
source: arxiv:1312.1719
pdf_sha256: 2bb0ccb7b5410868efdecc9ef5208d235c6f3aa75dee84aa992751aed117a42f
pdf_pages: 2-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 05698be2c0f93db00cd6cf1e551213006816fd5c3e699517631731cd535d3ccc
prompt_sha256: 329630a0b9175a55e4af1b8e281a3e67eeab250f8d643953b7dcde99743c7628
---

In our abstract model (Fig. 2), switches forward packets via a programmable parser followed by multiple stages of match+action, arranged in series, parallel, or a combination of both. Derived from OpenFlow, our model makes three generalizations. First, OpenFlow assumes a fixed parser, whereas our model supports a programmable parser to allow new headers to be defined. Second, OpenFlow assumes the match+action stages are in series, whereas in our model they can be in parallel or in series. Third, our model assumes that actions are composed from protocol-independent primitives supported by the switch.

Our abstract model generalizes how packets are processed in different forwarding devices (e.g., Ethernet switches, routers, load-balancers) and by different technologies (e.g., fixed-function switch ASICs, NPUs, reconfigurable switches, software switches, FPGAs). This allows us to devise a common language (P4) to represent how packets are processed in terms of our common abstract model. Hence, programmers can create target-independent programs that a compiler can map to a variety of different forwarding devices, ranging from relatively slow software switches to the fastest ASIC-based switches.

Figure.

Figure 2: The abstract forwarding model. {#bosshart-2014-p4-fig-2 .figure tag=0091}

The forwarding model is controlled by two types of operations: Configure and Populate. Configure operations program the parser, set the order of match+action stages, and specify the header fields processed by each stage. Configuration determines which protocols are supported and how the switch may process packets. Populate operations add (and remove) entries to the match+action tables that were specified during configuration. Population determines the policy applied to packets at any given time.

For the purposes of this paper, we assume that configuration and population are two distinct phases. In particular, the switch need not process packets during configuration. However, we expect implementations will allow packet processing during partial or full reconfiguration enabling upgrades with no downtime. Our model deliberately allows for, and encourages, reconfiguration that does not interrupt forwarding.

Clearly, the configuration phase has little meaning in fixed-function ASIC switches; for this type of switch, the compiler’s job is to simply check if the chip can support the P4 program. Instead, our goal is to capture the general trend towards fast reconfigurable packet-processing pipelines, as described in [2][3].

Arriving packets are first handled by the parser. The packet body is assumed to be buffered separately, and unavailable for matching. The parser recognizes and extracts fields from the header, and thus defines the protocols supported by the switch. The model makes no assumptions about the meaning of protocol headers, only that the parsed representation defines a collection of fields on which matching and actions operate.

The extracted header fields are then passed to the match+action tables. The match+action tables are divided between ingress and egress. While both may modify the packet header, ingress match+action determines the egress port(s) and determines the queue into which the packet is placed. Based on ingress processing, the packet may be forwarded, replicated (for multicast, span, or to the control plane), dropped, or trigger flow control. Egress match+action performs per-instance modifications to the packet header – e.g., for multicast copies. Action tables (counters, policers, etc.) can be associated with a flow to track frame-to-frame state.

Packets can carry additional information between stages, called metadata, which is treated identically to packet header fields. Some examples of metadata include the ingress port, the transmit destination and queue, a timestamp that can be used for packet scheduling, and data passed from table-to-table that does not involve changing the parsed representation of the packet such as a virtual network identifier.

Queueing disciplines are handled in the same way as the current OpenFlow: an action maps a packet to a queue, which is configured to receive a particular service discipline. The service discipline (e.g., minimum rate, DRR) is chosen as part of the switch configuration.

Although beyond the scope of this paper, action primitives can be added to allow the programmer to implement new or existing congestion control protocols. For example, the switch might be programmed to set the ECN bit based on novel conditions, or it might implement a proprietary congestion control mechanism using match+action tables.
