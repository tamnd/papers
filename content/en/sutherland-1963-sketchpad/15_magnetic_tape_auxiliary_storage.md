---
paper: sutherland-1963-sketchpad
title: 'Sketchpad: A Man-Machine Graphical Communication System'
authors:
  - Ivan E. Sutherland
year: 1963
venue: MIT PhD thesis / AFIPS Spring Joint Computer Conference
field: graphics
section: "7"
section_title: Magnetic Tape Auxiliary Storage
tag: 095D
kind: appendix
lang: en
source: https://www.cl.cam.ac.uk/techreports/UCAM-CL-TR-574.pdf
pdf_sha256: e052281b553622badc8dd308003c127617aa5723e4ec3dbfa79b781d8e712742
pdf_pages: 137-140
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 84f69d649c06e2c0042843d0516001b4a8cae1260f8a9b46c823a2b2b423eea8
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

### 3 Addressable arithmetic element registers {#sutherland-1963-sketchpad-s3 .section tag=0959}

### 4 Especially flexible in-out {#sutherland-1963-sketchpad-s4 .section tag=095A}

### 5 64 index registers {#sutherland-1963-sketchpad-s5 .section tag=095B}

### 6 Indirect — i.e. deferred addressing {#sutherland-1963-sketchpad-s6 .section tag=095C}

IN-OUT

The phrase “simultaneous use of in-out machines” should be taken quite literally. It does not mean simultaneous control. Each unit has its own buffer register and only one of these can be processed by TX-2 at any given instant. It

*By Alexander Vanderburgh is the *relative* speed that is important. For example, the in-out instruction that “fills” the display scope buffer takes no more than 10 microseconds, but the display itself takes from 20 to 100 microseconds, i.e., up to ten times as long. While the display is busy, the computer can compute the next datum of course, but it can also initiate other in-out transfers. In practice, since most in-out units are much slower than their associated programs, the computer spends a significant percentage of the time just waiting (in “Limbo”), even when several devices are in use. Interleaved initiation of in-out data transfers is partly automatic and partly program controlled. Each in-out routine is independently coded and is operated by TX-2 according to its “priority.” Each unit has a “Flag Flip-Flop” to indicate to control that it is ready for further attention. When a unit is ready for further attention its routine will be operated unless another unit of higher priority also needs attention. An index register is reserved for each in-out unit and is used as a “place-keeper” when its routine is not being operated. The sharing among in-out routines of storage, index memory, and the arithmetic element is the programmer’s responsibility.

“CONFIGURED” DATA PROCESSING

The “normal” word length for TX-2 is 36 bits. For many applications 18 or 9 bits would suffice, and in some cases each piece of data requires the same processing. Configuration control permits “fracture” of the normal word into two 18 bit pieces, four 9 bit pieces, or one 27 bit and one 9 bit. These “subwords” are completely independent — for example, there are separate overflow indicators. In addition to “fracture” there is “activity” and “quarter permutation”. Any quarter word can be made “inactive” i.e., inoperative. The 9 bit quarters of a datum from memory may be rearranged (permuted) before use. There are 8 standard permutations — for example, the right half of memory can be used with the left half of the arithmetic element. Nine bits are required for complete configuration specification. Since only 5 bits are available for bit thin film memory is addressed by each instruction word, a special 32 word, 9 bit thin film memory is addressed by each instruction that processes data directly. A complete change to any of 32 configurations is therefore possible from instruction to instruction.

THE SMALLER VIRTUES

*Overlap*: TX-2 has two core memories — “S” memory, a vacuum tube driven 65,536 word core memory, and “T” memory, a transistor driven 4096 word core memory about 20% faster. Instruction readout can be done concurrently with the previous data readout if program and data are in separate memories.

The use of the arithmetic element is also overlapped. Instructions that follow a multiply or divide operation will be done during the arithmetic time if they make no reference to the arithmetic element. The overlap is entirely automatic and may be ignored if the programmer chooses. A careful programmer can gain speed by doing indexing after multiply or divide and by putting program and data in separate memories.

Bit Sensing Instruction: One instruction — SKM — uses a single bit of any memory word as its operand. Control bits provide 32 variations of skipping setting, clearing, and/or complementing the selected bit. This instruction can also cycle the whole word right one place if desired.

Addressable Arithmetic Element: Seventeen bits of the TX-2 instruction word are reserved for addressing an operand. This would allow a 131,072 word memory. TX-2 has only 69,632 registers of core storage. The toggle switch and plugboard memories, the real time clock register, the knob register (shaft encoder), and the arithmetic element registers use 55 of the remaining addressing capability. The arithmetic element registers are therefore part of the memory system and can be addressed, e.g., one can add the accumulator to itself.

Flexible In-Out: The TX-2 user must program each and every datum transfer. The lack of complex automatic in-out controls may seem to be a burden, but the simplicity of the system gives the programmer much more precise and variable control than automatic systems provide. For example, coordination of separate in-out units such as display and light pen is possible. Moreover, it is relatively easy to attach new in-out machines as they become available.

Index Memory and Indirect Addressing: Of the 64 index registers, one must devote a few to each in-out unit’s program. With all 21 in-out devices concurrently in use, each program would have two index registers for normal programming use. In practice, one seldom uses more than half a dozen in-out units, and each routine would then have 9 — clearly a luxury. Indirect addressing provides a means for indexing normally nonindexable instructions, or for double indexing normal instructions.

Magnetic Tape Auxiliary Storage: Each TX-2 magnetic tape unit stores about 70 million bits, 34 times the capacity of the core memory system. Like a magnetic drum the tape is addressable. It can be read in either direction at any speed from 60 to 600 ips, and can be searched at a maximum of 1200 ips. It is used at present primarily for program storage. “Turn around time” — i.e. the time required to save one program and read-in in a different one is seldom more than 2 minutes and often less than 30 seconds. (The read-in time, once the desired section of the tape is found, is about 12 seconds for 69,632 words.) A standard IBM 729 tape unit is also available.

SUMMARY OF VITAL STATISTICS — TX-2 — DECEMBER 1962

Word Length:      36 bits, plus parity bit, plus debugging tag bit
Memory:
    256 × 256 core   65,536 words   6.0 $\mu$sec cycle time
    64 × 64 core     4,096 words   4.4 $\mu$sec cycle time
    Toggle switch        16 words
    Plugboard            32 words
Auxiliary Memory: Magnetic Tape 2+ million words, 70+ million bits per unit (2 units in use, total of 10 planned)
Tape Speeds:      selectable 60-300 inches/sec, search at 1000 inches/sec (i.e. about 1600 to 8000 36 bit words/sec)

IN-OUT EQUIPMENT

Input :

• Paper Tape Reader: 400-2000 6 bit lines/sec
• 2 keyboards — Lincoln writer 6 bit codes
• Random number generator — average 57.6 $\mu$sec per 9 bit number
• IBM Magnetic Tape (Model 729 M6)
• Miscellaneous pulse inputs — 9 channels — push buttons or other source
• Analog input — Epsco Datrac — nominal 11 bit sample, 27 kilocycle max. rate
• 2 light pens — work with either scope or both on one

Special memory registers :

• Real time clock
• 4 shaft encoder knobs, 9 bits each
• 592 toggle switches (16 registers)
• 37 push buttons — any or all can be pushed at once

Output :

• Paper tape punch — 300 6 bit lines/sec
• 2 typewriters — 10 characters per second
• IBM Magnetic Tape (729 M6)
• Miscellaneous pulse/light/relay contacts — 9 channels (low rates)
• Xerox printer — 1300 char. sec
• 2 display scopes — 7 × 7 inch usable area, 1024 × 1024 raster
• Large board pen and ink plotter — 29”×29” plotting area. 15 in/sec slew speed. Off line paper tape control as well as direct computer control.
