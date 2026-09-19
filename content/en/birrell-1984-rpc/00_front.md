---
paper: birrell-1984-rpc
title: Implementing Remote Procedure Calls
authors:
  - Andrew D. Birrell
  - Bruce Jay Nelson
year: 1984
venue: ACM TOCS
field: systems
section_title: Front Matter
tag: "0051"
kind: front
lang: en
source: https://www.cs.cmu.edu/~dga/15-712/F07/papers/birrell842.pdf
pdf_sha256: 0c5058383786e2b3e8fa9894872358e362a6f6ffc58c06f29dc08b836318f432
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: c678c750b704938e994f8d08160dc7133d0affb557b036222f5c87351d4654e4
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Implementing Remote Procedure Calls

ANDREW D. BIRRELL and BRUCE JAY NELSON
Xerox Palo Alto Research Center

Remote procedure calls (RPC) appear to be a useful paradigm for providing communication across a network between programs written in a high-level language. This paper describes a package providing a remote procedure call facility, the options that face the designer of such a package, and the decisions we made. We describe the overall structure of our RPC mechanism, our facilities for binding RPC clients, the transport level communication protocol, and some performance measurements. We include descriptions of some optimizations used to achieve high performance and to minimize the load on server machines that have many clients.

CR Categories and Subject Descriptors: C.2.2 [Computer-Communication Networks]: Network Protocols—protocol architecture; C.2.4 [Computer-Communication Networks]: Distributed Systems—distributed applications, network operating systems; D.4.4 [Operating Systems]: Communications Management—message sending, network communication; D.4.7[Operating Systems]: Organization and Design—distributed systems

General Terms: Design, Experimentation, Performance, Security

Additional Keywords and Phrases: Remote procedure calls, transport layer protocols, distributed naming and binding, inter-process communication, performance of communication protocols.
