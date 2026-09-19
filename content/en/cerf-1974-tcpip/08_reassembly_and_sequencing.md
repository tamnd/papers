---
paper: cerf-1974-tcpip
title: A Protocol for Packet Network Intercommunication
authors:
  - Vinton G. Cerf
  - Robert E. Kahn
year: 1974
venue: IEEE Transactions on Communications
field: networks
section_title: Reassembly and Sequencing
kind: section
lang: en
source: https://doi.org/10.21236/ada634240
pdf_sha256: f7c614a116516e0efec906885fa3ffd9261c5101900d117b72d26d92de96d2f1
pdf_pages: 6-7
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 95b6d264fa875be25cb6d8473efedea2b49139db2d529035aa92bd4a8abf7461
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The reconstruction of a message at the receiving TCP clearly requires$^1$ that each internetwork packet carry a sequence number which is unique to its particular destination port message stream. The sequence numbers must be monotonic increasing (or decreasing) since they are used to reorder and reassemble arriving packets into a message. If the space of sequence numbers were infinite, we could simply assign the next one to each new packet. Clearly, this space cannot be infinite, and we will consider what problems a finite sequence number space will cause when we discuss retransmission and duplicate detection in the next section. We propose the following scheme for performing the sequencing of packets and hence the reconstruction of messages by the destination TCP.

A pair of ports will exchange one or more messages over a period of time. We could view the sequence of messages produced by one port as if it were embedded in an infinitely long stream of bytes. Each byte of the message has a unique sequence number which we take to be its byte location relative to the beginning of the stream. When a segment is extracted from the message by the source TCP and formatted for internetwork transmission, the relative location of the first byte of segment text is used as the sequence number for the packet. The byte count field in the internetwork header accounts for all the text in the segment (but does not include the check-sum bytes or the bytes in either internetwork or process header). We emphasise that

$^1$ In the case of encrypted packets, a preliminary stage of reassembly may be required prior to decryption.

Fig. 7. Assignment of sequence numbers. {#cerf-1974-tcpip-fig-7 .figure tag=039A}

Fig. 8. Internetwork header flag field. {#cerf-1974-tcpip-fig-8 .figure tag=039B}

Fig. 9. Message splitting and packet splitting. {#cerf-1974-tcpip-fig-9 .figure tag=039C}

the sequence number associated with a given packet is unique only to the pair of ports that are communicating (see Fig. 7). Arriving packets are examined to determine for which port they are intended. The sequence numbers on each arriving packet are then used to determine the relative location of the packet text in the messages under reconstruction. We note that this allows the exact position of the data in the reconstructed message to be determined even when pieces are still missing.

Every segment produced by a source TCP is packaged in a single internetwork packet and a check sum is computed over the text and process header associated with the segment.

The splitting of messages into segments by the TCP and the potential splitting of segments into smaller pieces by GATEWAY creates the necessity for indicating to the destination TCP when the end of a segment (ES) has arrived and when the end of a message (EM) has arrived. The flag field of the internetwork header is used for this purpose (see Fig. 8).

The ES flag is set by the source TCP each time it prepares a segment for transmission. If it should happen that the message is completely contained in the segment, then the EM flag would also be set. The EM flag is also set on the last segment of a message, if the message could not be contained in one segment. These two flags are used by the destination TCP, respectively, to discover the presence of a check sum for a given segment and to discover that a complete message has arrived.

The ES and EM flags in the internetwork header are known to the GATEWAY and are of special importance when packets must be split apart from propagation through the next local network. We illustrate their use with an example in Fig. 9.

The original message A in Fig. 9 is shown split into two segments $A_1$ and $A_2$ and formatted by the TCP into a pair of internetwork packets. Packets $A_1$ and $A_2$ have their ES bits set, and $A_2$ has its EM bit set as well. When packet $A_1$ passes through the GATEWAY, it is split into two pieces: packet $A_{11}$ for which neither EM nor ES bits are set, and packet $A_{12}$ whose ES bit is set. Similarly, packet $A_2$ is split such that the first piece, packet $A_{21}$, has neither bit set, but packet $A_{22}$ has both bits set. The sequence number field (SEQ) and the byte count field (CT) of each packet is modified by the GATEWAY to properly identify the text bytes of each packet. The GATEWAY need only examine the internetwork header to do fragmentation.

The destination TCP, upon reassembling segment $A_1$, will detect the ES flag and will verify the check sum it knows is contained in packet $A_{12}$. Upon receipt of packet $A_{22}$, assuming all other packets have arrived, the destination TCP detects that it has reassembled a complete message and can now advise the destination process of its receipt.
