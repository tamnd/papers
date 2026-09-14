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
section: "4"
section_title: P4 LANGUAGE BY EXAMPLE
tag: "0094"
kind: section
lang: en
source: arxiv:1312.1719
pdf_sha256: 2bb0ccb7b5410868efdecc9ef5208d235c6f3aa75dee84aa992751aed117a42f
pdf_pages: 4-6
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 24413c13df1e70b3110a60b447ad2d111d385d331e5d1f4c69927d24d384703d
prompt_sha256: 329630a0b9175a55e4af1b8e281a3e67eeab250f8d643953b7dcde99743c7628
---

We explore P4 by examining a simple example in-depth. Many network deployments differentiate between an edge and a core; end-hosts are directly connected to edge devices, which are in turn interconnected by a high-bandwidth core. Entire protocols have been designed to support this architecture (such as MPLS [11] and PortLand [12]), aimed primarily at simplifying forwarding in the core.

Consider an example L2 network deployment with top-of-rack (ToR) switches at the edge connected by a two-tier core. We will assume the number of end-hosts is growing and the core L2 tables are overflowing. MPLS is an option to simplify the core, but implementing a label distribution protocol with multiple tags is a daunting task. PortLand looks interesting but requires rewriting MAC addresses—possibly breaking existing network debugging tools—and requires new agents to respond to ARP requests.

P4 lets us express a custom solution with minimal changes to the network architecture. We call our toy example mTag: it combines the hierarchical routing of PortLand with simple MPLS-like tags. The routes through the core are encoded by a 32-bit tag composed of four single-byte fields. The 32-bit tag can carry a “source route” or a destination locator (like PortLand’s Pseudo MAC). Each core switch need only examine one byte of the tag and switch on that information. In our example, the tag is added by the first ToR switch, although it could also be added by the end-host NIC.

The mTag example is intentionally very simple to focus our attention on the P4 language. The P4 program for an entire switch would be many times more complex in practice.

### 4.1 P4 Concepts {#bosshart-2014-p4-s4-1 .section tag=0095}

A P4 program contains definitions of the following key components:
• Headers: A header definition describes the sequence and structure of a series of fields. It includes specification of field widths and constraints on field values.
• Parsers: A parser definition specifies how to identify headers and valid header sequences within packets.
• Tables: Match+action tables are the mechanism for performing packet processing. The P4 program defines the fields on which a table may match and the actions it may execute.
• Actions: P4 supports construction of complex actions from simpler protocol-independent primitives. These complex actions are available within match+action tables.
• Control Programs: The control program determines the order of match+action tables that are applied to a packet. A simple imperative program describe the flow of control between match+action tables.
Next, we show how each of these components contributes to the definition of an idealized mTag processor in P4.

### 4.2 Header Formats {#bosshart-2014-p4-s4-2 .section tag=0096}

A design begins with the specification of header formats. Several domain-specific languages have been proposed for this [13, 14, 15]; P4 borrows a number of ideas from them. In general, each header is specified by declaring an ordered list of field names together with their widths. Optional field annotations allow constraints on value ranges or maximum lengths for variable-sized fields. For example, standard Ethernet and VLAN headers are specified as follows:

header ethernet {
    fields {
        dst_addr : 48; // width in bits
        src_addr : 48;
        ethertype : 16;
    }
}

header vlan {
    fields {
        pcp : 3;
        cfi : 1;
        vid : 12;
        ethertype : 16;
    }
}

The mTag header can be added without altering existing declarations. The field names indicate that the core has two layers of aggregation. Each core switch is programmed with rules to examine one of these bytes determined by its location in the hierarchy and the direction of travel (up or down).

header mTag {
    fields {
        up1 : 8;
        up2 : 8;
        down1 : 8;
        down2 : 8;
        ethertype : 16;
    }
}

### 4.3 The Packet Parser {#bosshart-2014-p4-s4-3 .section tag=0097}

P4 assumes the underlying switch can implement a state machine that traverses packet headers from start to finish, extracting field values as it goes. The extracted field values are sent to the match+action tables for processing.

P4 describes this state machine directly as the set of transitions from one header to the next. Each transition may be triggered by values in the current header. For example, we describe the mTag state machine as follows.

parser start{
ethernet;
}

parser ethernet {
    switch(ethertype) {
        case 0x8100: vlan;
        case 0x9100: vlan;
        case 0x800: ipv4;
        // Other cases
    }
}

parser vlan {
    switch(ethertype) {
        case 0xaaaa: mTag;
        case 0x800: ipv4;
        // Other cases
    }
}

parser mTag {
    switch(ethertype) {
        case 0x800: ipv4;
        // Other cases
    }
}

Parsing starts in the start state and proceeds until an explicit stop state is reached or an unhandled case is encountered (which may be marked as an error). Upon reaching a state for a new header, the state machine extracts the header using its specification and proceeds to identify its next transition. The extracted headers are forwarded to match+action processing in the back-half of the switch pipeline.

The parser for $mTag$ is very simple: it has only four states. Parsers in real networks require many more states; for example, the parser defined by Gibb *et. al.* [16, Figure 3(e)] expands to over one hundred states.

### 4.4 Table Specification {#bosshart-2014-p4-s4-4 .section tag=0123}

Next, the programmer describes how the defined header fields are to be matched in the match+action stages (e.g., should they be exact matches, ranges, or wildcards?) and what actions should be performed when a match occurs.

In our simple $mTag$ example, the edge switch matches on the L2 destination and VLAN ID, and selects an $mTag$ to add to the header. The programmer defines a table to match on these fields and apply an action to add the $mTag$ header (see below). The **reads** attribute declares which fields to match, qualified by the match type (exact, ternary, etc). The **actions** attribute lists the possible actions which may be applied to a packet by the table. Actions are explained in the following section. The **max_size** attribute specifies how many entries the table should support.

The table specification allows a compiler to decide how much memory it needs, and the memory type (e.g., TCAM or SRAM) to implement the table.

table mTag_table {

reads {
        ethernet.dst_addr : exact;
        vlan.vid : exact;
    }
    actions {
        // At runtime, entries are programmed with params
        // for the mTag action. See below.
        add_mTag;
    }
    max_size : 20000;
}

For completeness and for later discussion, we present brief definitions of other tables that are referenced by the Control Program (\S4.6).

table source_check {
    // Verify mtag only on ports to the core
    reads {
        mtag : valid; // Was mtag parsed?
        metadata.ingress_port : exact;
    }
    actions { // Each table entry specifies *one* action
        // If inappropriate mTag, send to CPU
        fault_to_cpu;

// If mtag found, strip and record in metadata
        strip_mtag;

// Otherwise, allow the packet to continue
        pass;
    }
    max_size : 64; // One rule per port
}

table local_switching {
    // Reads destination and checks if local
    // If miss occurs, goto mtag table.
}

table egress_check {
    // Verify egress is resolved
    // Do not retag packets received with tag
    // Reads egress and whether packet was mTagged
}

### 4.5 Action Specifications {#bosshart-2014-p4-s4-5 .section tag=0124}

P4 defines a collection of primitive actions from which more complicated actions are built. Each P4 program declares a set of action functions that are composed of action primitives; these action functions simplify table specification and population. P4 assumes parallel execution of primitives within an action function. (Switches incapable of parallel execution may emulate the semantics.)

The **add_mTag** action referred to above is implemented as follows:

action add_mTag(up1, up2, down1, down2, egr_spec) {
    add_header(mTag);
    // Copy VLAN ethertype to mTag
    copy_field(mTag.ethertype, vlan.ethertype);
// Set VLAN’s ethertype to signal mTag
set_field(vlan.ethertype, 0xaaaa);
set_field(mTag.up1, up1);
set_field(mTag.up2, up2);
set_field(mTag.down1, down1);
set_field(mTag.down2, down2);

// Set the destination egress port as well
set_field(metadata.egress_spec, egr_spec);
}

If an action needs parameters (e.g., the up1 value for the mTag), it is supplied from the match table at runtime.

In this example, the switch inserts the mTag after the VLAN tag, copies the VLAN tag’s ethertype into the mTag to indicate what follows, and sets the VLAN tag’s ethertype to 0xaaaa to signal mTag. Not shown are the inverse action specification that strips an mTag from a packet and the table to apply this action in edge switches.

P4’s primitive actions include:
• set_field: Set a specific field in a header to a value. Masked sets are supported.
• copy_field: Copy one field to another.
• add_header: Set a specific header instance (and all its fields) as valid.
• remove_header: Delete (“pop”) a header (and all its fields) from a packet.
• increment: Increment or decrement the value in a field.
• checksum: Calculate a checksum over some set of header fields (e.g., an IPv4 checksum).
We expect most switch implementations will restrict action processing to permit only header modifications that are consistent with the specified packet format.

### 4.6 The Control Program {#bosshart-2014-p4-s4-6 .section tag=0106}

Once tables and actions are defined, the only remaining task is to specify the flow of control from one table to the next. Control flow is specified as a program via a collection of functions, conditionals, and table references.

Figure.

Figure 4: Flow chart for the mTag example. {#bosshart-2014-p4-fig-4 .figure tag=0098}

Figure 4 shows a graphical representation of the desired control flow for the mTag implementation on edge switches. After parsing, the source_check table verifies consistency between the received packet and the ingress port. For example, mTags should only be seen on ports connected to core switches. The source_check also strips mTags from the packet, recording whether the packet had an mTag in metadata. Tables later in the pipeline may match on this metadata to avoid retagging the packet.

The local_switching table is then executed. If this table “misses,” it indicates that the packet is not destined for a locally connected host. In that case, the mTag_table (defined above) is applied to the packet. Both local and core forwarding control can be processed by the egress_check table which handles the case of an unknown destination by sending a notification up the SDN control stack.

The imperative representation of this packet processing pipeline is as follows:

control main() {
    // Verify mTag state and port are consistent
    table(source_check);

// If no error from source_check, continue
    if (!defined(metadata.ingress_error)) {
        // Attempt to switch to end hosts
        table(local_switching);

if (!defined(metadata.egress_spec)) {
            // Not a known local host; try mtagging
            table(mTag_table);
        }

// Check for unknown egress state or bad retagging with mTag.
        table(egress_check);
    }
}
