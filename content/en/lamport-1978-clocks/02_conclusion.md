---
paper: lamport-1978-clocks
title: Time, Clocks, and the Ordering of Events in a Distributed System
authors:
  - Leslie Lamport
year: 1978
venue: Communications of the ACM
field: systems
section_title: Conclusion
kind: section
lang: en
source: https://lamport.azurewebsites.net/pubs/time-clocks.pdf
pdf_sha256: c55e7cab4230aa3d7126748a149b2db6f0d7a67296d5eccfdd50a210299a96b2
pdf_pages: "7"
extraction: vision
extraction_model: gpt-5
content_sha256: 76553848309d12a4f406998564bea2b11dfb3d3ebd1cdba6f0e2bb96ccd5dbe9
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

We have seen that the concept of “happening before” defines an invariant partial ordering of the events in a distributed multiprocess system. We described an algorithm for extending that partial ordering to a somewhat arbitrary total ordering, and showed how this total ordering can be used to solve a simple synchronization problem. A future paper will show how this approach can be extended to solve any synchronization problem.

The total ordering defined by the algorithm is somewhat arbitrary. It can produce anomalous behavior if it disagrees with the ordering perceived by the system’s users. This can be prevented by the use of properly synchronized physical clocks. Our theorem showed how closely the clocks can be synchronized.

In a distributed system, it is important to realize that the order in which events occur is only a partial ordering. We believe that this idea is useful in understanding any multiprocess system. It should help one to understand the basic problems of multiprocessing independently of the mechanisms used to solve them.
