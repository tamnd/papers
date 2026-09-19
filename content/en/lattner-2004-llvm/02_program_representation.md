---
paper: lattner-2004-llvm
title: 'LLVM: A Compilation Framework for Lifelong Program Analysis & Transformation'
authors:
  - Chris Lattner
  - Vikram Adve
year: 2004
venue: CGO
field: languages
section: "2"
section_title: PROGRAM REPRESENTATION
tag: "0429"
kind: section
lang: en
source: https://doi.org/10.1109/cgo.2004.1281665
pdf_sha256: 0352543b42fca1c88c3a74b3223a9da68f686435a64d3321450bda4655e4965c
pdf_pages: 2-5
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 7001b161e190043e421a117b163e7141a1c1d114a4f701a3c342f04a4a5f1c94
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The code representation is one of the key factors that differentiates LLVM from other systems. The representation is designed to provide high-level information about programs that is needed to support sophisticated analyses and transformations, while being low-level enough to represent arbitrary programs and to permit extensive optimization in static compilers. This section gives an overview of the LLVM instruction set and describes the language-independent type

²See the LLVM home-page: http://llvm.cs.uiuc.edu/.

system, the memory model, exception handling mechanisms, and the offline and in-memory representations. The detailed syntax and semantics of the representation are defined in the LLVM reference manual [29].

### 2.1 Overview of the LLVM Instruction Set {#lattner-2004-llvm-s2-1 .section tag=042A}

The LLVM instruction set captures the key operations of ordinary processors but avoids machine-specific constraints such as physical registers, pipelines, and low-level calling conventions. LLVM provides an infinite set of typed virtual registers which can hold values of *primitive types* (Boolean, integer, floating point, and pointer). The virtual registers are in Static Single Assignment (SSA) form [15]. LLVM is a load/store architecture: programs transfer values between registers and memory solely via load and store operations using typed pointers. The LLVM memory model is described in Section 2.3.

The entire LLVM instruction set consists of only 31 opcodes. This is possible because, first, we avoid multiple opcodes for the same operations\footnote{For example, there are no unary operators: **not** and **neg** are implemented in terms of **xor** and **sub**, respectively.}. Second, most opcodes in LLVM are overloaded (for example, the add instruction can operate on operands of any integer or floating point operand type). Most instructions, including all arithmetic and logical operations, are in three-address form: they take one or two operands and produce a single result.

LLVM uses SSA form as its primary code representation, i.e., each virtual register is written in exactly one instruction, and each use of a register is dominated by its definition. Memory locations in LLVM are *not* in SSA form because many possible locations may be modified at a single store through a pointer, making it difficult to construct a reasonably compact, explicit SSA code representation for such locations. The LLVM instruction set includes an explicit phi instruction, which corresponds directly to the standard (non-gated) $\phi$ function of SSA form. SSA form provides a compact def-use graph that simplifies many dataflow optimizations and enables fast, flow-insensitive algorithms to achieve many of the benefits of flow-sensitive algorithms without expensive dataflow analysis. Non-loop transformations in SSA form are further simplified because they do not encounter anti- or output dependences on SSA registers. Non-memory transformations are also greatly simplified because (unrelated to SSA) registers cannot have aliases.

LLVM also makes the Control Flow Graph (CFG) of every function explicit in the representation. A function is a set of basic blocks, and each basic block is a sequence of LLVM instructions, ending in exactly one terminator instruction (branches, return, unwind, or invoke; the latter two are explained later below). Each terminator explicitly specifies its successor basic blocks.

### 2.2 Language-independent Type Information, Cast, and GetElementPtr {#lattner-2004-llvm-s2-2 .section tag=042B}

One of the fundamental design features of LLVM is the inclusion of a language-independent type system. Every SSA register and explicit memory object has an associated type, and all operations obey strict type rules. This type information is used in conjunction with the instruction opcode to determine the exact semantics of an instruction (e.g. floating point vs. integer add). This type information enables a broad class of *high-level* transformations on *low-level* code (for example, see Section 4.1.1). In addition, type mismatches are useful for detecting optimizer bugs.

The LLVM type system includes source-language-independent primitive types with predefined sizes (void, bool, signed/unsigned integers from 8 to 64 bits, and single- and double-precision floating-point types). This makes it possible to write portable code using these types, though non-portable code can be expressed directly as well. LLVM also includes (only) four derived types: pointers, arrays, structures, and functions. We believe that most high-level language data types are eventually represented using some combination of these four types in terms of their operational behavior. For example, C++ classes with inheritance are implemented using structures, functions, and arrays of function pointers, as described in Section 4.1.2.

Equally important, the four derived types above capture the type information used even by sophisticated language-independent analyses and optimizations. For example, field-sensitive points-to analyses [25, 31], call graph construction (including for object-oriented languages like C++), scalar promotion of aggregates, and structure field reordering transformations [12], only use pointers, structures, functions, and primitive data types, while array dependence analysis and loop transformations use all those plus array types.

Because LLVM is language independent and must support weakly-typed languages, *declared* type information in a legal LLVM program may not be reliable. Instead, some pointer analysis algorithm must be used to distinguish memory accesses for which the type of the pointer target is reliably known from those for which it is not. LLVM includes such an analysis described in Section 4.1.1. Our results show that despite allowing values to be arbitrarily cast to other types, reliable type information is available for a large fraction of memory accesses in C programs compiled to LLVM.

The LLVM 'cast' instruction is used to convert a value of one type to another arbitrary type, and is the *only* way to perform such conversions. Casts thus make all type conversions explicit, including type coercion (there are no mixed-type operations in LLVM), explicit casts for physical subtyping, and reinterpreting casts for non-type-safe code. A program without *casts* is necessarily type-safe (in the absence of memory access errors, e.g., array overflow [19]).

A critical difficulty in preserving type information for low-level code is implementing address arithmetic. The getelementptr instruction is used by the LLVM system to perform pointer arithmetic in a way that both preserves type information and has machine-independent semantics. Given a typed pointer to an object of some aggregate type, this instruction calculates the address of a sub-element of the object in a type-preserving manner (effectively a combined '.' and '[ ]' operator for LLVM). For example, the C statement "X[i].a = 1;" could be translated into the pair of LLVM instructions:

%p = getelementptr %xty* %X, long %i, ubyte 3;
    store int 1, int* %p;

where we assume *a* is field number 3 within the structure X[i], and the structure is of type %xty. Making all address arithmetic explicit is important so that it is exposed to all LLVM optimizations (most importantly, reassociation and redundancy elimination); getelementptr achieves this without obscuring the type information. Load and store instructions take a single pointer and do not perform any indexing, which makes the processing of memory accesses simple and uniform.

### 2.3 Explicit Memory Allocation and Unified Memory Model {#lattner-2004-llvm-s2-3 .section tag=05D9}

LLVM provides instructions for typed memory allocation. The malloc instruction allocates one or more elements of a specific type on the heap, returning a typed pointer to the new memory. The free instruction releases memory allocated through malloc$^4$. The alloca instruction is similar to malloc except that it allocates memory in the stack frame of the current function instead of the heap, and the memory is automatically deallocated on return from the function. All stack-resident data (including “automatic” variables) are allocated explicitly using alloca.

In LLVM, all addressable objects (“lvalues”) are explicitly allocated. Global variable and function definitions define a symbol which provides the address of the object, not the object itself. This gives a unified memory model in which all memory operations, including call instructions, occur through typed pointers. There are no implicit accesses to memory, simplifying memory access analysis, and the representation needs no “address of” operator.

### 2.4 Function Calls and Exception Handling {#lattner-2004-llvm-s2-4 .section tag=05DA}

For ordinary function calls, LLVM provides a call instruction that takes a typed function pointer (which may be a function name or an actual pointer value) and typed actual arguments. This abstracts away the calling conventions of the underlying machine and simplifies program analysis.

One of the most unusual features of LLVM is that it provides an explicit, low-level, machine-independent mechanism to implement exception handling in high-level languages. In fact, the same mechanism also supports setjmp and longjmp operations in C, allowing these operations to be analyzed and optimized in the same way that exception features in other languages are. The common exception mechanism is based on two instructions, invoke and unwind.

The invoke and unwind instructions together support an abstract exception handling model logically based on stack unwinding (though LLVM-to-native code generators may use either “zero cost” table-driven methods [9] or setjmp/longjmp to implement the instructions). invoke is used to specify exception handling code that must be executed during stack unwinding for an exception. unwind is used to throw an exception or to perform a longjmp. We first describe the mechanisms and then describe how they can be used for implementing exception handling.

The invoke instruction works just like a call, but specifies an extra basic block that indicates the starting block for an unwind handler. When the program executes an unwind instruction, it logically unwinds the stack until it removes an activation record created by an invoke. It then transfers control to the basic block specified by the invoke. These two instructions expose exceptional control flow in the LLVM CFG.

These two primitives can be used to implement a wide variety of exception handling mechanisms. To date, we have implemented full support for C’s setjmp/longjmp calls and the C++ exception model; in fact, both coexist cleanly in our implementation [13]. At a call site, if some code must be executed when an exception is thrown (for example, setjmp, “catch” blocks, or automatic variable destructors in C++), the code uses the invoke instruction for the call. When an exception is thrown, this causes the stack unwinding to stop in the current function, execute the desired code, then continue execution or unwinding as appropriate.

```text
{
    AClass Obj;      // Has a destructor
func();
// Might throw; must execute destructor
    ...
}
```

Figure 1: $C++$ exception handling example {#lattner-2004-llvm-fig-1 .figure tag=05DB}

For example, consider Figure 1, which shows a case where “cleanup code” needs to be generated by the C++ front-end. If the ‘func()’ call throws an exception, C++ guarantees that the destructor for the Object object will be run. To implement this, an invoke instruction is used to halt unwinding, the destructor is run, then unwinding is continued with the unwind instruction. The generated LLVM code is shown in Figure 2. Note that a front-end for Java would use similar code to unlock locks that are acquired through synchronized blocks or methods when exceptions are thrown.

...
; Allocate stack space for object:
%Obj = alloca %AClass, uint 1
; Construct object:
call void %AClass::AClass(%AClass* %Obj)
; Call 'func()':
invoke void %func() to label %OkLabel
    unwind to label %ExceptionLabel
OkLabel:
    ; ... execution continues...
ExceptionLabel:
    ; If unwind occurs, excecution continues here. First, destroy the object:
    call void %AClass::~AClass(%AClass* %Obj)
    ; Next, continue unwinding:
    unwind

Figure 2: LLVM code for the $C++$ example. The handler code specified by invoke executes the destructor. {#lattner-2004-llvm-fig-2 .figure tag=05DC}

A key feature of our approach is that the complex, language-specific details of what code must be executed to throw and recover from exceptions is isolated to the language front-end and language-specific runtime library (so it does not complicate the LLVM representation), *but yet the exceptional control-flow due to stack unwinding is encoded within the application code* and therefore exposed in a language-independent manner to the optimizer. The C++ exception handling model is very complicated, supporting many related features such as try/catch blocks, checked exception specifications, function try blocks, etc., and requiring complex semantics for the dynamic lifetime of an exception object. The C++ front-end supports these semantics by generating calls to a simple runtime library.

For example, consider the expression ‘throw 1’. This constructs and throws an exception with integer type. The generated LLVM code is shown in Figure 3. The example code illustrates the key feature mentioned above. The runtime handles all of the implementation-specific details, such as allocating memory for exceptions$^5$. Second, the runtime

$^4$When native code is generated for a program, *malloc* and *free* instructions are converted to the appropriate native function calls, allowing custom memory allocators to be used.

$^5$For example, the implementation has to be careful to re; Allocate an exception object
%t1 = call sbyte* %__llvm_cxxeh_alloc_exc(uint 4)
%t2 = cast sbyte* %t1 to int*
; Construct the thrown value into the memory
store int 1, int* %t2
; 'Throw' an integer expression, specifying the
; exception object, the typeid for the object, and
; the destructor for the exception (null for int).
call void %__llvm_cxxeh_throw(sbyte* %t1,
    <typeinfo for int>,
    void (sbyte*)* null)
unwind ; Unwind the stack.

Figure 3: LLVM code uses a runtime library for C++ exceptions support while exposing control-flow. {#lattner-2004-llvm-fig-3 .figure tag=05DD}

functions manipulate the thread-local state of the exception handling runtime, but don’t actually unwind the stack. Because the calling code performs the stack unwind, the optimizer has a better view of the control flow of the function without having to perform interprocedural analysis. This allows LLVM to turn stack unwinding operations into direct branches when the unwind target is the same function as the unwinder (this often occurs due to inlining, for example).

Finally, try/catch blocks are implemented in a straightforward manner, using the same mechanisms and runtime support. Any function call within the try block becomes an invoke. Any throw within the try-block becomes a call to the runtime library (as in the example above), followed by an explicit branch to the appropriate catch block. The “catch block” then uses the C++ runtime library to determine if the top-level current exception is of one of the types that is handled in the catch block. If so, it transfers control to the appropriate block, otherwise it calls unwind to continue unwinding. The runtime library handles the language-specific semantics of determining whether the current exception is of a caught type.

### 2.5 Plain-text, Binary, and In-memory Representations {#lattner-2004-llvm-s2-5 .section tag=05DE}

The LLVM representation is a first class language which defines equivalent textual, binary, and in-memory (i.e., compiler’s internal) representations. The instruction set is designed to serve effectively both as a persistent, offline code representation and as a compiler internal representation, with no semantic conversions needed between the two6. Being able to convert LLVM code between these representations without information loss makes debugging transformations much simpler, allows test cases to be written easily, and decreases the amount of time required to understand the in-memory representation.
