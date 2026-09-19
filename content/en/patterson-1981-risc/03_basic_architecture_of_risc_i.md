---
paper: patterson-1981-risc
title: 'RISC I: A Reduced Instruction Set VLSI Computer'
authors:
  - David A. Patterson
  - Carlo H. Sequin
year: 1981
venue: ISCA
field: architecture
section_title: Basic Architecture of Risc I
kind: section
lang: en
source: https://people.eecs.berkeley.edu/~kubitron/courses/cs252-F00/handouts/papers/p216-patterson.pdf
pdf_sha256: d49afdf3db5a8374fbc757059fab0562b9a517b3ff7abec17c2e6b88c48f03e1
pdf_pages: 2-4
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: a2b254a1146f809bceea19a69003c1495658414966549569ca6d17d6e97261a7
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The RISC I instruction set contains a few simple operations (arithmetic, logical, and shift) that operate on registers. Instructions, data, addresses, and registers are 32 bits. RISC instructions fall into four categories (Figure 4): arithmetic-logical (ALU), memory access, branch, and miscellaneous. The execution time of a RISC I cycle is given by the time it takes to read a register, perform an ALU operation, and store the result back into a register. Register 0, which always contains 0, allows us to synthesize a variety of operations and addressing modes.

Load and store instructions move data between registers and memory. These instructions use two CPU cycles. We decided to make an exception to our constraint of single-cycle execution rather than to extend the general cycle to permit a complete memory access. There are eight variations of memory access instructions to accommodate sign-extended or zero-extended 8-bit, 16-bit, and 32-bit data. Although there appears to be only one addressing mode, index plus displacement, absolute and register indirect addressing can be synthesized using register 0 (Figure 5). (Using one register to always contain 0 dates back at least to CDC-6600 in 1964. It has also appeared in more recent designs.10)

Branch instructions include CALL, return, conditional and unconditional jump. The conditional instructions are the standard set used originally in PDP-11 and are found in most 16-bit microprocessors today. Most of the innovative features of RISC are found in CALL, return, and jump; they will be discussed in subsequent sections.

Figure 6 shows the 32-bit format used by register-to-register instructions and memory access instructions. For register-to-register instructions, DEST selects one of the 32 registers as the destination of the result of the operation, which itself is performed on the registers specified by SOURCE1 and SOURCE2. If IMM equals 0, the low-order 5 bits of SOURCE2 specify another register; if IMM equals 1, SOURCE2 expresses a sign-extended, 13-bit constant. Because of the frequency of occurrence of integer constants in high-level language programs, the immediate field has been made an option in every instruction. SCC determines if the condition codes are set. Memory access instructions use SOURCE1 to specify the index register and SOURCE2 to specify the offset. One other format, which combines the last three fields to form a 19-bit PC-relative address, is used primarily by the branch instructions.

Although comparative measurements of benchmarks are the real test of effectiveness, the examples in Figure 5 show that many of the important VAX instructions can be synthesized from simple RISC addressing modes and operation codes. Remember that register 0 (r0) always contains 0; specifying r0 as a destination does not change its value.

Register Windows

The previously mentioned investigations on using high-level languages indicate that the procedure CALL may be the most time-consuming operation in typical high-level language programs. Potentially, RISC programs may have an even larger number of calls, because the complex instructions found in CISCs are subroutines in RISC. Thus, the procedure CALL must be as fast as possible, perhaps no longer than a few jumps. The RISC register window scheme comes close to this goal. At the same time, this scheme also reduces the number of accesses to data memory.

Using procedures involves two groups of time-consuming operations: saving or restoring registers on each CALL or return, and passing parameters and results to and from the procedure. Because our measurements on high-level language programs indicate that local scalars are the most frequent operands, we wanted to support the allocation of locals in registers. Baskett$^{11}$ and Sites$^{12}$ suggested that microprocessors keep multiple banks of registers on the chip to avoid register saving and restoring. Thus, each procedure CALL results in a new set of registers being allocated for use by that new procedure. The return just alters a pointer, which restores the old set. A similar scheme was adopted by RISC I; however, some of the registers are not saved or restored on each procedure CALL. These registers ($r0$ through $r9$) are called *global* registers.

In addition, the sets of registers used by different processes are overlapped to allow parameters to be passed in registers. In other machines, parameters are usually passed on the stack with the calling procedure using a register (frame pointer) to point to the beginning of the parameters (and also to the end of the locals). Thus, all references to parameters are indexed references to memory. Our approach is to break the set of window registers ($r10$ to $r31$) into three parts (Figure 7). Registers 26 through 31 (HIGH) contain parameters passed from "above" the current procedure; that is, the calling procedure. Registers 16 through 25 (LOCAL) are used for the local scalar storage exactly as described previously. Registers 10 through 15 (LOW) are used for local storage and for parameters passed to the procedure "below" the current procedure (the called procedure). On each procedure CALL, a new set of registers, $r10$ to $r31$, is allocated; however, we want the LOW registers of the "caller" to become the HIGH registers of the "callee." This is accomplished by having the hardware overlap the LOW registers of the calling frame with the HIGH registers of the called frame; thus, without moving information, parameters in registers 10 through 15 appear in registers 25 through 31 in the called frame. Figure 8 illustrates this approach for the case in which procedure $A$ calls procedure $B$, which calls procedure $C$.

Multiple register banks require a mechanism to handle the case in which there are no free register banks available. RISC I handles this with a separate register overflow stack in memory and a stack pointer to it. Overflow and underflow are handled with a trap to a software routine that adjusts that stack. Because this routine can save or restore several sets of registers, the overflow/underflow frequency is based on the local variations in the depth of the stack rather than on the absolute depth. The effectiveness of this scheme depends on the relative frequency of overflows and underflows; studies by Halbert and Kessler$^{13}$ indicate that overflow will occur in less than 1% of the calls with only 4 to 8 register banks. (Other machines, such as BBN C/70, contain register banks, but they do not overlap their windows.)

The final step in allocating variables in registers is handling the problem of pointers. Pointers to variables require that variables have addresses. Because registers do not normally have addresses, one could let the compiler determine what variables have pointers and put such variables in memory. This precludes separate compilation, slows down access to these variables, and is beyond state-of-the-art compiler technology found in most companies and universities. RISC I solves that problem by giving addresses to the window registers. If we reserve a portion of the address space, we can determine, with one comparision, whether an address points to a register or to memory. Because the only instructions to access memory are load and store, and they take an extra cycle already, we can add this feature without reducing the performance of the load and store instructions. This permits the use of straightforward compiler technology and still leaves a large fraction of the variables in registers.

Delayed Jump

The normal RISC I instruction cycle is just long enough to execute the following sequence of operations:

1. Read a register
2. Perform an ALU operation
3. Store the result back into a register

We increase performance by prefetching the next instruction during the execution of the current instruction. This introduces difficulties with branch instructions. Several high-end machines have elaborate techniques to prefetch the appropriate instruction after the branch,$^{14}$ but these techniques are too complicated for a single-chip RISC. Our solution was to redefine jumps so that they do not take effect until after the following instruction; we refer to this as the *delayed jump*. (This approach to branching dates back to MANIAC I in 1952 and is now commonly used in microprogramming.)

The delayed jump allows RISC I always to prefetch the next instruction during the execution of the current instruction. The machine language code is suitably arranged so that the desired results are obtained. Because RISC I is always intended to be programmed in high-level languages, we will not "burden" the programmer with this complexity; the burden will be carried by the programmers of the compiler, the optimizer, and the debugger.

To illustrate how the delayed branch works, Figure 9a shows a sequence of instructions, which, in machines with normal jumps, would be executed in the order 100, 101, 102, 105, ... . To get that same effect in RISC I, we would have to insert NOP (Figure 9b). In this case, the sequence of instructions for RISC I is 100, 101, 102, 103, 106, ... . In the worst case, every jump could take two instructions. The RISC I software, however, includes an optimizer that tries to rearrange the sequence of instructions to perform the equivalent operations without NOP. Such an optimized RISC I sequence is 100, 101, 102, 105, ... (Figure 9c). Because the instruction following a jump is always executed, and the jump at 101 is not dependent on the ADD at 102, this sequence is equivalent to the original program segment in Figure 9a.
