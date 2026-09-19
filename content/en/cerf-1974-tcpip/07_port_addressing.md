---
paper: cerf-1974-tcpip
title: A Protocol for Packet Network Intercommunication
authors:
  - Vinton G. Cerf
  - Robert E. Kahn
year: 1974
venue: IEEE Transactions on Communications
field: networks
section_title: Port Addressing
kind: section
lang: en
source: https://doi.org/10.21236/ada634240
pdf_sha256: f7c614a116516e0efec906885fa3ffd9261c5101900d117b72d26d92de96d2f1
pdf_pages: 5-6
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: a5a8138ddf835a8bd8236e01118eeac698c8516f19cbb9d70f473710a624f970
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

A receiving TCP is faced with the task of demultiplexing the stream of internetwork packets it receives and reconstructing the original messages for each destination process. Each operating system has its own internal means of identifying processes and ports. We assume that 16 bits are sufficient to serve as internetwork port identifiers. A sending process need not know how the destination port identification will be used. The destination TCP will be able to parse this number appropriately to find the proper buffer into which it will place arriving packets. We permit a large port number field to support processes which want to distinguish between many different message streams concurrently. In reality, we do not care how the 16 bits are sliced up by the TCP’s involved.

Figure.

Fig. 4. TCP address. {#cerf-1974-tcpip-fig-4 .figure tag=0397}

Even though the transmitted port name field is large, it is still a compact external name for the internal representation of the port. The use of short names for port identifiers is often desirable to reduce transmission overhead and possibly reduce packet processing time at the destination TCP. Assigning short names to each port, however, requires an initial negotiation between source and destination to agree on a suitable short name assignment, the subsequent maintenance of conversion tables at both the source and the destination, and a final transaction to release the short name. For dynamic assignment of port names, this negotiation is generally necessary in any case.

SEGMENT AND PACKET FORMATS

As shown in Fig. 5, messages are broken by the TCP into segments whose format is shown in more detail in Fig. 6. The field lengths illustrated are

Fig. 5. Creation of segments and packets from messages. {#cerf-1974-tcpip-fig-5 .figure tag=0398}

Fig. 6. Segment format (process header and text). {#cerf-1974-tcpip-fig-6 .figure tag=0399}

merely suggestive. The first two fields (source port and destination port in the figure) have already been discussed in the preceding section on addressing. The uses of the third and fourth fields (window and acknowledgement in the figure) will be discussed later in the section on retransmission and duplicate detection.

We recall from Fig. 3 that an internetwork header contains both a sequence number and a byte count, as well as a flag field and a check sum. The uses of these fields are explained in the following section.
