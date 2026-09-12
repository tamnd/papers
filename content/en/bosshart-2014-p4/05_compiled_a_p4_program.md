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
section: "5"
section_title: COMPILED A P4 PROGRAM
tag: "0099"
kind: section
lang: en
source: arxiv:1312.1719
pdf_sha256: 2bb0ccb7b5410868efdecc9ef5208d235c6f3aa75dee84aa992751aed117a42f
pdf_pages: 6-7
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: e046a2c6e449cf6ed2859fb8364a2597a86453bb726a088c6be79fd0f8dbbe19
prompt_sha256: 329630a0b9175a55e4af1b8e281a3e67eeab250f8d643953b7dcde99743c7628
---

For a network to implement our P4 program, we need a compiler to map the target-independent description onto the target switch’s specific hardware or software platform. Doing so involves allocating the target’s resources and generating appropriate configuration for the device.

### 5.1 Compiling Packet Parsers {#bosshart-2014-p4-s5-1 .section tag=009A}

For devices with programmable parsers, the compiler translates the parser description into a parsing state machine, while for fixed parsers, the compiler merely verifies that the parser description is consistent with the target’s parser. Details of generating a state machine and state table entries can be found in [16].

Table 2 shows state table entries for the vlan and mTag sections of the parser (§4.3). Each entry specifies the current state, the field value to match, and the next state. Other columns are omitted for brevity.

| Current State | Lookup Value | Next State |
| --- | --- | --- |
| vlan | 0xaaaa | mTag |
| vlan | 0x800 | ipv4 |
| vlan | * | stop |
| mTag | 0x800 | ipv4 |
| mTag | * | stop |

Table 2: Parser state table entries for the mTag example. {#bosshart-2014-p4-tab-2 .table tag=009B}

### 5.2 Compiling Control Programs {#bosshart-2014-p4-s5-2 .section tag=009C}

The imperative control-flow representation in §4.6 is a convenient way to specify the logical forwarding behavior of a switch, but does not explicitly call out dependencies between tables or opportunities for concurrency. We therefore employ a compiler to analyze the control program to identify dependencies and look for opportunities to process header fields in parallel. Finally, the compiler generates the target configuration for the switch. There are many potential targets: for example, a software switch [17], a multicore software switch [18], an NPU [19], a fixed function switch [20], or a reconfigurable match table (RMT) pipeline [2].

As discussed in §3 the compiler follows a two-stage compilation process. It first converts the P4 control program into an intermediate table dependency graph representation which it analyzes to determine dependencies between tables. A target-specific back-end then maps this graph onto the switch’s specific resources.

We briefly examine how the mTag example would be implemented in different kinds of switches:

Software switches: A software switch provides complete flexibility: the table count, table configuration, and parsing are under software control. The compiler directly maps the mTag table graph to switch tables. The compiler uses table type information to constrain table widths, heights, and matching criterion (e.g., exact, prefix, or wildcard) of each table. The compiler might also optimize ternary or prefix matching with software data structures.

Hardware switches with RAM and TCAM: A compiler can configure hashing to perform efficient exact-matching using RAM, for the mTag_table in edge switches. In contrast, the core mTag forwarding table that matches on a subset of tag bits would be mapped to TCAM.

Switches supporting parallel tables: The compiler can detect data dependencies and arrange tables in parallel or in series. In the mTag example, the tables local_switching and mTag_table can execute in parallel up to the execution of the action of setting an mTag.

Switches that apply actions at the end of the pipeline: For switches with action processing only at the end of a pipeline, the compiler can tell intermediate stages to generate metadata that is used to perform the final writes. In the mTag example, whether the mTag is added or removed could be represented in metadata.

Switches with a few tables: The compiler can map a large number of P4 tables to a smaller number of physical tables. In the mTag example, the local switching could be combined with the mTag table. When the controller installs new rules at runtime, the compiler’s rule translator can “compose” the rules in the two P4 tables to generate the rules for the single physical table.
