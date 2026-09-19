---
paper: metcalfe-1976-ethernet
title: 'Ethernet: Distributed Packet Switching for Local Computer Networks'
authors:
  - Robert M. Metcalfe
  - David R. Boggs
year: 1976
venue: Communications of the ACM
field: networks
section: "5"
section_title: Growth
tag: 02AB
kind: section
lang: en
source: https://www.cl.cam.ac.uk/teaching/0809/DigiCommI/metcalfe1976ethernet.pdf
pdf_sha256: e1e9d67146a1d0955a39b4fbb8e2951d6cefb4f7231a01acb9c78852280da227
pdf_pages: "6"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: f6bc07e07c4a485b7df1078f9549d0b03a1bd7585c5e32b0a984fddfacea080a
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

### 5.1 Signal Cover {#metcalfe-1976-ethernet-s5-1 .section tag=02AC}

One can expand an Ethernet just so far by adding transceivers and Ether. At some point, the transceivers and Ether will be unable to carry the required signals. The signal cover can be extended with a simple unbuffered packet repeater. In our experimental Ethernet, where because of transceiver simplicity the Ether cannot be branched passively, a simple repeater may join any number of Ether segments to enrich the topology while extending the signal cover.

We operate an experimental two-segment packet repeater, but hope to avoid relying on them. In branching the Ether and extending its signal cover, there is a trade-off between using sophisticated transceivers and using repeaters. With increased power and sensitivity, transceivers become more expensive and less reliable. The introduction of repeaters into an Ethernet makes the centrally interconnecting Ether active. The failure of a transceiver will sever the communications of its owner; the failure of a repeater partitions the Ether severing many communications.

### 5.2 Traffic Cover {#metcalfe-1976-ethernet-s5-2 .section tag=02AD}

One can expand an Ethernet just so far by adding Ether and packet repeaters. At some point the Ether will be so busy that additional stations will just divide more finely the already inadequate bandwidth. The traffic cover can be extended with an unbuffered traffic-filtering repeater or packet filter, which passes packets from one Ether segment to another only if the destination station is located on the new segment. A packet filter also extends the signal cover.

### 5.3 Address Cover {#metcalfe-1976-ethernet-s5-3 .section tag=02AE}

One can expand an Ethernet just so far by adding Ether, repeaters, and traffic filters. At some point there will be too many stations to be addressed with the Ethernet’s 8-bit addresses. The address cover can be extended with packet gateways and the software addressing conventions they implement [[cerf-1974-tcpip]]. Addresses can be expanded in two directions: down into the station by adding fields to identify destination ports or processes within a station, and up into the internetwork by adding fields to identify destination stations on remote networks. A gateway also extends the traffic and signal covers.

There can be only one repeater or packet filter connecting two Ether segments; a packet repeated onto a segment by multiple repeaters would interfere with itself. However, there is no limit to the number of gateways connecting two segments; a gateway only repeats packets addressed to itself as an intermediary. Failure of the single repeater connecting two segments partitions the network; failure of a gateway need not partition the net if there are paths through other gateways between the segments.
