---
paper: metcalfe-1976-ethernet
title: 'Ethernet: Distributed Packet Switching for Local Computer Networks'
authors:
  - Robert M. Metcalfe
  - David R. Boggs
year: 1976
venue: Communications of the ACM
field: networks
section: "7"
section_title: Protocol
tag: 02B4
kind: section
lang: en
source: https://www.cl.cam.ac.uk/teaching/0809/DigiCommI/metcalfe1976ethernet.pdf
pdf_sha256: e1e9d67146a1d0955a39b4fbb8e2951d6cefb4f7231a01acb9c78852280da227
pdf_pages: 8-9
extraction: vision
extraction_model: gpt-5
content_sha256: e91e91190dc8078b9071e78d4984320c8e5a3414468313325dd4880b00ad81ff
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

There is more to the construction of a viable packet communication system than simply providing the mechanisms for packet transport. Methods for error correction, flow control, process naming, security, and accounting must also be provided through higher-level protocols implemented on top of the Ether control protocol described in Sections 3 and 4 above. [[cerf-1974-tcpip]], [10], [12], [21], [28], [34]. Ether control includes packet framing, error detection, addressing and multi-access control; like other line control procedures, Ethernet is used to support numerous network and multiprocessor architectures [30, 31].

Here is a brief description of one simple error-controlling packet protocol. The EFTP (Ethernet File Transfer Protocol) is of interest both because it is relatively easy to understand and implement correctly and because it has dutifully carried many valuable files during the development of more general and efficient protocols.

### 7.1. General Terminology {#metcalfe-1976-ethernet-s7-1 .section tag=02B5}

In discussing packet protocols, we use the following generally useful terminology. A packet is said to have a *source* and a *destination*. A flow of data is said to have a *sender* and a *receiver*, recognizing that to support a flow of data some packets (typically acknowledgments) will be sourced at the receiver and destined for the sender. A connection is said to have a *listener* and an *initiator* and a service is said to have a *server* and a *user*. It is very useful to treat these as orthogonal descriptors of the participants in a communication. Of course, a server is usually a listener and the source of data-bearing packets is usually the sender.

### 7.2 EFTP {#metcalfe-1976-ethernet-s7-2 .section tag=02B6}

The first 16 bits of all Ethernet packets contain its interface-interpretable destination and source station addresses, a byte each, in that order (see Figure 2). By software convention, the second 16 bits of all Ethernet packets contain the packet type. Different protocols use disjoint sets of packet types. The EFTP uses 5 packet types: data, ack, abort, end, and endreply. Following the 16-bit type word of an EFTP packet are 16 bits of sequence number, 16 bits of length, optionally some 16-bit data words, and finally a 16-bit software checksum word (see Figure 4). The Ethernet’s hardware checksum is present only on the Ether and is not counted at this level of protocol.

It should be obvious that little care has been taken to cram certain fields into just the right number of bits. The emphasis here is on simplicity and ease of programming. Despite this disclaimer, we do feel that it is more advisable to err on the side of spacious fields; try as you may, one field or another will always turn out to be too small.

The software checksum word is used to lower the probability of an undetected error. It serves not only as a backup for the experimental Ethernet’s serial hardware 16-bit cyclic redundancy checksum (in Figure 2), but also for protection against failures in parallel data paths within stations which are not checked by the CRC. The checksum used by the EFTP is a 1’s complement add and cycle over the entire packet, including header and content data. The checksum can be ignored at the user’s peril at either end; the sender may put all 1’s (an impossible value) into the checksum word to indicate to the receiver that no checksum was computed.

### 7.2.1 Data transfer. {#metcalfe-1976-ethernet-s7-2-1 .section tag=02B7}

The 16-bit words of a file are carried from sending station to receiving station in data packets consecutively numbered from 0. Each data packet is retransmitted periodically by the sender until an ack packet with a matching sequence number is returned from the receiver. The receiver ignores all damaged packets, packets from a station other than the sender, and packets whose sequence number does not match either the expected one ‘or the one preceding. When a packet has the expected sequence number, the packet is acked, its data is accepted as part of the file, and the sequence number is incremented. When a packet arrives with a sequence number one less than that expected, it is acknowledged and discarded; the presumption is that its ack was lost and needs retransmission [21].

### 7.2.2 End. {#metcalfe-1976-ethernet-s7-2-2 .section tag=02B8}

When all the data has been transmitted, an end packet is sent with the next consecutive sequence number and than the sender waits for a matching end-reply. Having accepted an end packet in sequence, the data receiver responds with a matching endreply and then dallys for some reasonably long period of time (10 seconds). Upon getting the endreply, the sending station transmits an echoing endreply and is free to go off with the assurance that the file has been transferred successfully. The dallying receiver then gets the echoed end-reply and it too goes off assured.

Table I. Ethernet Efficiency.

| $Q$ | $P = 4096$ | $P = 1024$ | $P = 512$ | $P = 48$ |
|---:|---:|---:|---:|---:|
| 1 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| 2 | 0.9884 | 0.9552 | 0.9143 | 0.5000 |
| 3 | 0.9857 | 0.9447 | 0.8951 | 0.4444 |
| 4 | 0.9842 | 0.9396 | 0.8862 | 0.4219 |
| 5 | 0.9834 | 0.9367 | 0.8810 | 0.4096 |
| 10 | 0.9818 | 0.9310 | 0.8709 | 0.3874 |
| 32 | 0.9807 | 0.9272 | 0.8642 | 0.3737 |
| 64 | 0.9805 | 0.9263 | 0.8627 | 0.3708 |
| 128 | 0.9804 | 0.9259 | 0.8620 | 0.3693 |
| 256 | 0.9803 | 0.9257 | 0.8616 | 0.3686 |

Communications  
of  
the ACM

July 1976  
Volume 19

Fig. 4. EFTP packet layout. {#metcalfe-1976-ethernet-fig-4 .figure tag=02B9}

The comparatively complex end-dally sequence is intended to make it practically certain that the sender and receiver of a file will agree on whether the file has been transmitted correctly. If the end packet is lost, the data sender simply retransmits it as it would any packet with an overdue acknowledgement. If the endreply from the data receiver is lost, the data sender will time out in the same way and retransmit the end packet which will in turn be acknowledged by the dallying receiver. If the echoed endreply is lost, the dallying receiver will be inconvenienced having to wait for it, but when it has timed out, the receiver can nevertheless be assured of successful transfer of the file because the end packet has been received.

At any time during all of this, either side is free to decide communication has failed and just give up; it is considered polite to send an abort packet to end the communication promptly in the event of, say, a user-initiated abort or a file system error.

### 7.2.3 EFTP shortcomings. {#metcalfe-1976-ethernet-s7-2-3 .section tag=02BA}

The EFTP has been very useful, but its shortcomings are many. First, the protocol provides only for file transfer from station to station in a single network and specifically not from process to process within stations either on the same network or through a gateway. Second, process rendezvous is degenerate in that there are no mechanisms for finding processes by name or for convenient handling of multiple users by a single server. Third, there is no real flow control. If data arrives at a receiver unable to accept it into its buffers, the data can simply be thrown away with complete assurance that it will be retransmitted eventually. There is no way for a receiver to quench the flow of such wasted transmissions or to expedite retransmission. Fourth, data is transmitted in integral numbers of 16-bit words belonging to unnamed files and thus the EFTP is either terribly restrictive or demands some nested file transfer formats internal to its data words. And fifth, functional generality is lost because the receiver is also the listener and server.
