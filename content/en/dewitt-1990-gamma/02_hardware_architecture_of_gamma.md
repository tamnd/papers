---
paper: dewitt-1990-gamma
title: The Gamma Database Machine Project
authors:
  - David J. DeWitt
  - Shahram Ghandeharizadeh
  - Donovan A. Schneider
  - Allan Bricker
  - Hui-I Hsiao
  - Rick Rasmussen
year: 1990
venue: IEEE Transactions on Knowledge and Data Engineering
field: databases
section: "2"
section_title: Hardware Architecture of Gamma
tag: 025C
kind: section
lang: en
source: http://db.cs.berkeley.edu/cs286/papers/gamma-tkde1990.pdf
pdf_sha256: 420d33f44b8e050f33517cdff1299a58838b4ad826d80a6617200332ea02be5e
pdf_pages: 4-7
extraction: vision
extraction_model: gpt-5
content_sha256: dc353fca75a59e3b1aa60852b79a0b11c6b8807748f7c81f7d98223066b8bf15
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

### 2.1. Overview {#dewitt-1990-gamma-s2-1 .section tag=025D}

Gamma is based on the concept of a shared-nothing architecture [STON86] in which processors do not share disk drives or random access memory and can only communicate with one another by sending messages through an interconnection network. Mass storage in such an architecture is generally distributed among the processors by connecting one or more disk drives to each processor as shown in Figure 1. There are a number of reasons why the shared-nothing approach has become the architecture of choice. First, there is nothing to prevent the architecture from scaling to 1000s of processors unlike shared-memory machines for which scaling beyond 30-40 processors may be impossible. Second, as demonstrated in [DEWI88, COPE88, TAND88], by associating a small number of

Figure 1 disks with each processor and distributing the tuples of each relation across the disk drives, it is possible to achieve very high aggregate I/O bandwidths without using custom disk controllers [KIM86, PATT88]. Furthermore, by employing off-the-shelf mass storage technology one can employ the latest technology in small 3 1/2" disk drives with embedded disk controllers. Another advantage of the shared nothing approach is that there is no longer any need to "roll your own" hardware. Recently, both Intel and Ncube have added mass storage to their hypercube-based multiprocessor products.

### 2.2. Gamma Version 1.0 {#dewitt-1990-gamma-s2-2 .section tag=025E}

The initial version of Gamma consisted of 17 VAX 11/750 processors, each with two megabytes of memory. An 80 megabit/second token ring [PROT85] was used to connect the processors to each other and to another VAX running Unix. This processor acted as the host machine for Gamma. Attached to eight of the processors were 333 megabyte Fujitsu disk drives that were used for storing the database. The diskless processors were used along with the processors with disks to execute join and aggregate function operators in order to explore whether diskless processors could be exploited effectively.

We encountered a number of problems with this prototype. First, the token ring had a maximum network packet size of 2K bytes. In the first version of the prototype the size of a disk page was set to 2K bytes in order to be able to transfer an "intact" disk page from one processor to another without a copy. This required, for example, that each disk page also contain space for the protocol header used by the interprocessor communication software. While this initially appeared to be a good idea, we quickly realized that the benefits of a larger disk page size more than offset the cost of having to copy tuples from a disk page into a network packet.

The second problem we encountered was that the network interface and the Unibus on the 11/750 were both bottlenecks [GERB87, DEWI88]. While the bandwidth of the token ring itself was 80 megabits/second, the Unibus on the 11/750 (to which the network interface was attached) has a bandwidth of only 4 megabits/second. When processing a join query without a selection predicate on either of the input relations, the Unibus became a bottleneck because the transfer rate of pages from the disk was higher than the speed of the Unibus [DEWI88]. The network interface was a bottleneck because it could only buffer two incoming packets at a time. Until one packet was transferred into the VAX’s memory, other incoming packets were rejected and had to be retransmitted by the communications protocol. While we eventually constructed an interface to the token ring that plugged directly into the backplane of the VAX, by the time the board was operational the VAX’s were obsolete and we elected not to spend additional funds to upgrade the entire system.

The other serious problem we encountered with this prototype was having only 2 megabytes of memory on each processor. This was especially a problem since the operating system used by Gamma does not provide virtual memory. The problem was exacerbated by the fact that space for join hash tables, stack space for processes, and the buffer pool were managed separately in order to avoid flushing hot pages from the buffer pool. While there are advantages to having these spaces managed separately by the software, in a configuration where memory is already tight, balancing the sizes of these three pools of memory proved difficult.

### 2.3. Gamma Version 2.0 {#dewitt-1990-gamma-s2-3 .section tag=025F}

In the fall of 1988, we replaced the VAX-based prototype with a 32 processor iPSC/2 hypercube from Intel. Each processor is configured with a 386 CPU, 8 megabytes of memory, and a 330-megabyte MAXTOR 4380 (5 1/4") disk drive. Each disk drive has an embedded SCSI controller which provides a 45 Kbyte RAM buffer that acts as a disk cache on read operations.

The nodes in the hypercube are interconnected to form a hypercube using custom VLSI routing modules. Each module supports eight[^1] full-duplex, serial, reliable communication channels operating at 2.8 megabytes/second. Small messages (<= 100 bytes) are sent as datagrams. For large messages, the hardware builds a communications circuit between the two nodes over which the entire message is transmitted without any software overhead or copying. After the message has been completely transmitted, the circuit is released. The length of a message is limited only by the size of the physical memory on each processor. Table 1 summarizes the transmission times from one Gamma process to another (on two different hypercube nodes) for a variety of message sizes.

| Packet Size (in bytes) | Transmission Time |
|---|---|
| 50 | 0.74 ms. |
| 500 | 1.46 ms. |
| 1000 | 1.57 ms. |
| 4000 | 2.69 ms. |
| 8000 | 4.64 ms. |

Table 1

The conversion of the Gamma software to the hypercube began in early December 1988. Because most users of the Intel hypercube tend to run a single process at a time while crunching numerical data, the operating system provided by Intel supports only a limited number of heavy weight processes. Thus, we began the conversion process by porting Gamma’s operating system, NOSE (see Section 3.5). In order to simplify the conversion, we elected to run NOSE as a thread package inside a single NX/2 process in order to avoid having to port NOSE to run on the bare hardware directly.

[^1]: On configurations with a mix of compute and I/O nodes, one of the 8 channels is dedicated for communication to the I/O subsystem.

Once NOSE was running, we began converting the Gamma software. This process took 4-6 man months but lasted about 6 months as, in the process of the conversion, we discovered that the interface between the SCSI disk controller and memory was not able to transfer disk blocks larger than 1024 bytes (the pitfall of being a beta test site). For the most part the conversion of the Gamma software was almost trivial as, by porting NOSE first, the differences between the two systems in initiating disk and message transfers were completely hidden from the Gamma software. In porting the code to the 386, we did discover a number of hidden bugs in the VAX version of the code as the VAX does not trap when a null pointer is dereferenced. The biggest problem we encountered was that nodes on the VAX multicomputer were numbered beginning with 1 while the hypercube uses 0 as the logical address of the first node. While we thought that making the necessary changes would be tedious but straightforward, we were about half way through the port before we realized that we would have to find and change every "for" loop in the system in which the loop index was also used as the address of the machine to which a message was to be set. While this sounds silly now, it took us several weeks to find all the places that had to be changed. In retrospect, we should have made NOSE mask the differences between the two addressing schemes.

From a database system perspective, however, there are a number of areas in which Intel could improve the design of the iPSC/2. First, a light-weight process mechanism should be provided as an alternative to NX/2. While this would have almost certainly increased the time required to do the port, in the long run we could have avoided maintaining NOSE. A much more serious problem with the current version of the system is that the disk controller does not perform DMA transfers directly into memory. Rather, as a block is read from the disk, the disk controller does a DMA transfer into a 4K byte FIFO. When the FIFO is half full, the CPU is interrupted and the contents of the FIFO are copied into the appropriate location in memory.[^1] While a block instruction is used for the copy operation, we have measured that about 10% of the available CPU cycles are being wasted doing the copy operation. In addition, the CPU is interrupted 13 times during the transfer of one 8 Kbyte block partially because a SCSI disk controller is used and partially because of the FIFO between the disk controller and memory.
