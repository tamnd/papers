---
paper: birrell-1984-rpc
title: Implementing Remote Procedure Calls
authors:
  - Andrew D. Birrell
  - Bruce Jay Nelson
year: 1984
venue: ACM TOCS
field: systems
section: "4"
section_title: PERFORMANCE
tag: "0641"
kind: section
lang: en
source: https://www.cs.cmu.edu/~dga/15-712/F07/papers/birrell842.pdf
pdf_sha256: 0c5058383786e2b3e8fa9894872358e362a6f6ffc58c06f29dc08b836318f432
pdf_pages: 18-20
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 4c817362cda602b90361f56b767453b47764b426079d7f110aea247081b1d169
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

As we have mentioned already, Nelson’s thesis included extensive analysis of several RPC protocols and implementations, and included an examination of the contributing factors to the differing performance characteristics. We do not repeat that information here.

We have made the following measurements of use of our RPC package. The measurements were made for remote calls between two Dorados connected by an

| Procedure | Minimum | Median | Transmission | Local-only |
| --- | --- | --- | --- | --- |
| no args/results | 1059 | 1097 | 131 | 9 |
| 1 arg/result | 1070 | 1105 | 142 | 10 |
| 2 args/results | 1077 | 1127 | 152 | 11 |
| 4 args/results | 1115 | 1171 | 174 | 12 |
| 10 args/results | 1222 | 1278 | 239 | 17 |
| 1 word array | 1069 | 1111 | 131 | 10 |
| 4 word array | 1106 | 1153 | 174 | 13 |
| 10 word array | 1214 | 1250 | 239 | 16 |
| 40 word array | 1643 | 1695 | 566 | 51 |
| 100 word array | 2915 | 2926 | 1219 | 98 |
| resume except'n | 2555 | 2637 | 284 | 134 |
| unwind except'n | 3374 | 3467 | 284 | 196 |

Ethernet. The Ethernet had a raw data rate of 2.94 megabits per second. The Dorados were running Cedar. The measurements were made on an Ethernet shared with other users, but the network was lightly loaded (apart from our tests), at five to ten percent of capacity. The times shown in Table I are all in microseconds, and were measured by counting Dorado microprocessor cycles and dividing by the known crystal frequency. They are accurate to within about ten percent. The times are elapsed times: they include time spent waiting for the network and time used by interference from other devices. We are measuring from when the user program invokes the local procedure exported by the user-stub until the corresponding return from that procedure call. This interval includes the time spent inside the user-stub, the RPCRuntime on both machines, the server-stub, and the server implementation of the procedures (and transmission times in both directions). The test procedures were all exported to a single interface. We were not using any of our encryption facilities.

We measured individually the elapsed times for 12,000 calls on each procedure. Table I shows the minimum elapsed time we observed, and the median time. We also present the total packet transmission times for each call (as calculated from the known packet sizes used by our protocol, rather than from direct measurement). Finally, we present the elapsed time for making corresponding calls if the user program is bound directly to the server program (i.e., when making a purely local call, without any involvement of the RPC package). The time for purely local calls should provide the reader with some calibration of the speed of the Dorado processor and the Mesa language. The times for local calls also indicate what part of the total time is due to the use of RPC.

The first five procedures had, respectively, 0, 1, 2, 4 and 10 arguments and 0, 1, 2, 4 and 10 results, each argument or result being 16 bits long. The next five procedures all had one argument and one result, each argument or result being an array of size 1, 4, 10, 40 and 100 words respectively. The second line from the bottom shows a call on a procedure that raises an exception which the caller resumes. The last line is for the same procedure raising an exception that the caller causes to be unwound.

For transferring large amounts of data in one direction, protocols other than RPC have an advantage, since they can transmit fewer packets in the other direction. Nevertheless, by interleaving parallel remote calls from multiple processes, we have achieved a data rate of 2 megabits per second transferring between Dorado main memories on the 3 megabit Ethernet. This is equal to the rate achieved by our most highly optimized byte stream implementation (written in BCPL).

We have not measured the cost of exporting or importing an interface. Both of these operations are dominated by the time spent talking to the Grapevine server(s). After locating the exporter machine, calling the exporter to determine the dispatcher identifier uses an RPC call with a few words of data.
