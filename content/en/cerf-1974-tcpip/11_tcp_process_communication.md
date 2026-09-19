---
paper: cerf-1974-tcpip
title: A Protocol for Packet Network Intercommunication
authors:
  - Vinton G. Cerf
  - Robert E. Kahn
year: 1974
venue: IEEE Transactions on Communications
field: networks
section_title: Tcp/process Communication
kind: section
lang: en
source: https://doi.org/10.21236/ada634240
pdf_sha256: f7c614a116516e0efec906885fa3ffd9261c5101900d117b72d26d92de96d2f1
pdf_pages: 9-10
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: ca72b425ece6b028a421f27360d7b897049efa88b6e63251f109789c7bc23d5d
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

In order to send a message, a process sets up its text in a buffer region in its own address space, inserts the requisite control information (described in the following list) in a transmit control block (TCB) and passes control to the TCP. The exact form of a TCB is not specified here, but it might take the form of a passed pointer, a pseudointerrupt, or various other forms. To receive a message in its address space, a process sets up a receive buffer, inserts the requisite control information in a receive control block (RCB) and again passes control to the TCP.

In some simple systems, the buffer space may in fact be provided by the TCP. For simplicity we assume that a ring buffer is used by each process, but other structures (e.g., buffer chaining) are not ruled out.

A possible format for the TCB is shown in Fig. 11. The TCB contains information necessary to allow the TCP to extract and send the process data. Some of the information might be implicitly known, but we are not concerned with that level of detail. The various fields in the TCB are described as follows.

1) Source Address: This is the full net/HOST/TCP/port address of the transmitter.
2) Destination Address: This is the full net/HOST/TCP/port of the receiver.
3) Next Packet Sequence Number: This is the sequence number to be used for the next packet the TCP will transmit from this port.
4) Current Buffer Size: This is the present size of the process transmit buffer.
5) Next Write Position: This is the address of the next position in the buffer at which the process can place new data for transmission.
6) Next Read Position: This is the address at which the TCP should begin reading to build the next segment for output.
7) End Read Position: This is the address at which the TCP should halt transmission. Initially 6) and 7) bound the message which the process wishes to transmit.
8) Number of Retransmissions/Maximum Retransmissions: These fields enable the TCP to keep track of the number of times it has retransmitted the data and could be omitted if the TCP is not to give up.
9) Timeout/Flags: The timeout field specifies the delay after which unacknowledged data should be retransmitted. The flag field is used for semaphores and other TCP/process synchronization status reporting, etc.
10) Current Acknowledgment/Window: The current acknowledgment field identifies the first byte of data still unacknowledged by the destination TCP.

The read and write positions move circularly around the transmit buffer, with the write position always to the left (module the buffer size) of the read position.

The next packet sequence number should be constrained to be less than or equal to the sum of the current acknowledgment and the window fields. In any event, the next sequence number should not exceed the sum of the current acknowledgment and half of the maximum possible sequence number (to avoid confusing the receiver’s duplicate detection algorithm). A possible buffer layout is shown in Fig. 12.

The RCB is substantially the same, except that the end read field is replaced by a partial segment check-sum register which permits the receiving TCP to compute and remember partial check sums in the event that a segment arrives in several packets. When the final packet of the segment arrives, the TCP can verify the check sum and if successful, acknowledge the segment.
