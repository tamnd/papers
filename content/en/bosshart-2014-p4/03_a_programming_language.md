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
section: "3"
section_title: A PROGRAMMING LANGUAGE
tag: "0092"
kind: section
lang: en
source: arxiv:1312.1719
pdf_sha256: 2bb0ccb7b5410868efdecc9ef5208d235c6f3aa75dee84aa992751aed117a42f
pdf_pages: 3-4
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 7bf7da21ab26ca0b6c4ef7f306fd670f183052624ab69610e2dbd8cbb5944f5d
prompt_sha256: 329630a0b9175a55e4af1b8e281a3e67eeab250f8d643953b7dcde99743c7628
---

We use the abstract forwarding model to define a language to express how a switch is to be configured and how packets are to be processed. This paper’s main goal is to propose the P4 programming language. However, we recognize that many languages are possible, and they will likely share the common characteristics we describe here. For example, the language needs a way to express how the parser is programmed so that the parser knows what packet formats to expect; hence a programmer needs a way to declare what header types are possible. As an example, the programmer could specify the format of an IPv4 header and what headers may legally follow the IP header. This motivates defining parsing in P4 by declaring legal header types. Similarly, the programmer needs to express how packet headers are to be processed. For example, TTL fields must be decremented and tested, new tunnel headers may need to be added, and checksums may need to be computed. This motivates P4’s use of an imperative control flow program to describe header field processing using the declared header types and a primitive set of actions.

We could use a language such as Click [10], which builds switches from modules composed of arbitrary C++. Click is extremely expressive, and very suitable for expressing how packets are processed in the kernel of a CPU. But it is insufficiently constrained for our needs—we need a language that mirrors the parse-match-action pipelines in dedicated hardware. In addition, Click is not designed for a controller-switch architecture and hence does not allow programmers to describe match+action tables that are dynamically populated by well-typed rules. Finally, Click makes it difficult to infer dependencies that constrain parallel execution—as we now discuss.

A packet processing language must allow the programmer to express (implicitly or explicitly) any serial dependencies between header fields. Dependencies determine which tables can be executed in parallel. For example, sequential execution is required for an IP routing table and an ARP table due to the data dependency between them. Dependencies can be identified by analyzing Table Dependency Graphs (TDGs); these graphs describe the field inputs, actions, and control flow between tables. Figure 3 shows an example table dependency graph for an L2/L3 switch. TDG nodes map directly to match+action tables, and a dependency analysis identifies where each table may reside in the pipeline. Unfortunately TDGs are not readily accessible to most programmers; programmers tend to think of packet processing algorithms using imperative constructs rather than graphs.

Figure.

Figure 3: Table dependency graph for an L2/L3 switch. {#bosshart-2014-p4-fig-3 .figure tag=0093}

This leads us to propose a two-step compilation process. At the highest level, programmers express packet processing programs using an imperative language representing the control flow (P4); below this, a compiler translates the P4 representation to TDGs to facilitate dependency analysis, and then maps the TDG to a specific switch target. P4 is designed to make it easy to translate a P4 program into a TDG. In summary, P4 can be considered to be a sweet spot between the generality of say Click (that makes it difficult to infer dependencies and map to hardware) and the inflexibility of OpenFlow 1.0 (that makes it impossible to reconfigure protocol processing).
