---
paper: gal-2009-tracejit
title: Trace-based Just-in-Time Type Specialization for Dynamic Languages
authors:
  - Andreas Gal
  - Brendan Eich
  - Mike Shaver
  - David Anderson
  - David Mandelin
year: 2009
venue: PLDI
field: languages
section: "2"
section_title: 'Overview: Example Tracing Run'
tag: 05F6
kind: section
lang: en
source: https://mozilla.github.io/pdf.js/web/compressed.tracemonkey-pldi-09.pdf
pdf_sha256: 3662ff519e485810520552bf301d8c3b2b917fd2f83303f4965d7abed367e113
pdf_pages: 2-4
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 8daee3182157958d74ba23add824daa50b46997eebeda34c6a5409c95359c410
edited: true
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

This section provides an overview of our system by describing how TraceMonkey executes an example program. The example program, shown in Figure 1, computes the first 100 prime numbers with nested loops. The narrative should be read along with Figure 2, which describes the activities TraceMonkey performs and when it transitions between the loops.

TraceMonkey always begins executing a program in the bytecode interpreter. Every loop back edge is a potential trace point. When the interpreter crosses a loop edge, TraceMonkey invokes the *trace monitor*, which may decide to record or execute a native trace. At the start of execution, there are no compiled traces yet, so the trace monitor counts the number of times each loop back edge is executed until a loop becomes *hot*, currently after 2 crossings. Note that the way our loops are compiled, the loop edge is crossed before entering the loop, so the second crossing occurs immediately after the first iteration.

Here is the sequence of events broken down by outer loop iteration:

```javascript
for (var i = 2; i < 100; ++i) {
    if (!primes[i])
        continue;
    for (var k = i + i; i < 100; k += i)
        primes[k] = false;
}
```

Figure 1. Sample program: sieve of Eratosthenes. primes is initialized to an array of 100 false values on entry to this code snippet. {#gal-2009-tracejit-fig-1 .figure tag=042C}

Figure.

Figure 2. State machine describing the major activities of TraceMonkey and the conditions that cause transitions to a new activity. In the dark box, TM executes JS as compiled traces. In the light gray boxes, TM executes JS in the standard interpreter. White boxes are overhead. Thus, to maximize performance, we need to maximize time spent in the darkest box and minimize time spent in the white boxes. The best case is a loop where the types at the loop edge are the same as the types on entry–then TM can stay in native code until the loop is done. {#gal-2009-tracejit-fig-2 .figure tag=042D}

```text
v0 := ld state[748]    // load primes from the trace activation record
    st sp[0], v0      // store primes to interpreter stack
v1 := ld state[764]      // load k from the trace activation record
v2 := i2f(v1)

// convert k from int to double
    st sp[8], v1      // store k to interpreter stack
    st sp[16], 0      // store false to interpreter stack
v3 := ld v0[4]           // load class word for primes
v4 := and v3, -4         // mask out object class tag for primes
v5 := eq v4, Array       // test whether primes is an array
xf v5

// side exit if v5 is false
v6 := js_Array_set(v0, v2, false)   // call function to set array element
v7 := eq v6, 0           // test return value from call
```

xt v7             // side exit if js_Array_set returns false.

Figure 3. LIR snippet for sample program. This is the LIR recorded for line 5 of the sample program in Figure 1. The LIR encodes the semantics in SSA form using temporary variables. The LIR also encodes all the stores that the interpreter would do to its data stack. Sometimes these stores can be optimized away as the stack locations are live only on exits to the interpreter. Finally, the LIR records guards and side exits to verify the assumptions made in this recording: that primes is an array and that the call to set its element succeeds. {#gal-2009-tracejit-fig-3 .figure tag=042E}

```asm
mov edx, ebx(748)        // load primes from the trace activation record
mov edi(0), edx          // (*) store primes to interpreter stack
mov esi, ebx(764)        // load k from the trace activation record
mov edi(8), esi          // (*) store k to interpreter stack
mov edi(16), 0           // (*) store false to interpreter stack
mov eax, edx(4)          // (*) load object class word for primes
and eax, -4              // (*) mask out object class tag for primes
cmp eax, Array           // (*) test whether primes is an array
jne side_exit_1          // (*) side exit if primes is not an array
sub esp, 8               // bump stack for call alignment convention
push false               // push last argument for call
push esi                 // push first argument for call
call js_Array_set        // call function to set array element
add esp, 8               // clean up extra stack space
mov ecx, ebx             // (*) created by register allocator
test eax, eax            // (*) test return value of js_Array_set
je side_exit_2           // (*) side exit if call failed
...
side_exit_1:
mov ecx, ebp(-4)         // restore ecx
mov esp, ebp             // restore esp
jmp epilog               // jump to ret statement
```

i=2. This is the first iteration of the outer loop. The loop on lines 4-5 becomes hot on its second iteration, so TraceMonkey enters recording mode on line 4. In recording mode, TraceMonkey records the code along the trace in a low-level compiler intermediate representation we call *LIR*. The LIR trace encodes all the operations performed and the types of all operands. The LIR trace also encodes *guards*, which are checks that verify that the control flow and types are identical to those observed during trace recording. Thus, on later executions, if and only if all guards are passed, the trace has the required program semantics.

Figure 4. x86 snippet for sample program. This is the x86 code compiled from the LIR snippet in Figure 3. Most LIR instructions compile to a single x86 instruction. Instructions marked with (*) would be omitted by an idealized compiler that knew that none of the side exits would ever be taken. The 17 instructions generated by the compiler compare favorably with the 100+ instructions that the interpreter would execute for the same code snippet, including 4 indirect jumps. {#gal-2009-tracejit-fig-4 .figure tag=042F}

TraceMonkey stops recording when execution returns to the loop header or exits the loop. In this case, execution returns to the loop header on line 4.

After recording is finished, TraceMonkey compiles the trace to native code using the recorded type information for optimization. The result is a native code fragment that can be entered if the interpreter PC and the types of values match those observed when trace recording was started. The first trace in our example, $T_{45}$, covers lines 4 and 5. This trace can be entered if the PC is at line 4, i and k are integers, and primes is an object. After compiling $T_{45}$, TraceMonkey returns to the interpreter and loops back to line 1.

i=3. Now the loop header at line 1 has become hot, so TraceMonkey starts recording. When recording reaches line 4, TraceMonkey observes that it has reached an inner loop header that already has a compiled trace, so TraceMonkey attempts to nest the inner loop inside the current trace. The first step is to call the inner trace as a subroutine. This executes the loop on line 4 to completion and then returns to the recorder. TraceMonkey verifies that the call was successful and then records the call to the inner trace as part of the current trace. Recording continues until execution reaches line 1, and at which point TraceMonkey finishes and compiles a trace for the outer loop, $T_{16}$.

i=4. On this iteration, TraceMonkey calls $T_{16}$. Because i=4, the if statement on line 2 is taken. This branch was not taken in the original trace, so this causes $T_{16}$ to fail a guard and take a side exit. The exit is not yet hot, so TraceMonkey returns to the interpreter, which executes the continue statement.

i=5. TraceMonkey calls $T_{16}$, which in turn calls the nested trace $T_{45}$. $T_{16}$ loops back to its own header, starting the next iteration without ever returning to the monitor.

i=6. On this iteration, the side exit on line 2 is taken again. This time, the side exit becomes hot, so a trace $T_{23,1}$ is recorded that covers line 3 and returns to the loop header. Thus, the end of $T_{23,1}$ jumps directly to the start of $T_{16}$. The side exit is patched so that on future iterations, it jumps directly to $T_{23,1}$.

At this point, TraceMonkey has compiled enough traces to cover the entire nested loop structure, so the rest of the program runs entirely as native code.
