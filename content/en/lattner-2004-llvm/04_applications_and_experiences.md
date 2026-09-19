---
paper: lattner-2004-llvm
title: 'LLVM: A Compilation Framework for Lifelong Program Analysis & Transformation'
authors:
  - Chris Lattner
  - Vikram Adve
year: 2004
venue: CGO
field: languages
section: "4"
section_title: APPLICATIONS AND EXPERIENCES
tag: "05E6"
kind: section
lang: en
source: https://doi.org/10.1109/cgo.2004.1281665
pdf_sha256: 0352543b42fca1c88c3a74b3223a9da68f686435a64d3321450bda4655e4965c
pdf_pages: 7-10
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: b2cc8726fa4ee42f0fac34b7d2e163ab90fb4523dee6b47e62aaa24f11f194b6
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Sections 2 and 3 describe the design of the LLVM code representation and compiler architecture. In this section, we evaluate this design in terms of three categories of issues: (a) the characteristics of the representation; (b) the speed of performing whole-program analyses and transformations in the compiler; and (c) illustrative uses of the LLVM system for challenging compiler problems, focusing on how the novel capabilities in LLVM benefit these uses.

### 4.1 Representation Issues {#lattner-2004-llvm-s4-1 .section tag=05E7}

We evaluate three important characteristics of the LLVM representation. First, a key aspect of the representation is the language-independent type system. Does this type system provide any useful information when it can be violated with casts? Second, how do high-level language features map onto the LLVM type system and code representation? Third, how large is the LLVM representation when written to disk?

### 4.1.1 What value does type information provide? {#lattner-2004-llvm-s4-1-1 .section tag=05E8}

Reliable type information about programs can enable the optimizer to perform aggressive transformations that would be difficult otherwise, such as reordering two fields of a structure or optimizing memory management [12, 30]. As noted in Section 2.2, however, declared type information in LLVM is not reliable and some analysis (typically including a pointer analysis) must check the declared type information before it can be used. A key question is how much *reliable* type information is available in programs compiled to LLVM?

LLVM includes a flow-insensitive, field-sensitive and context-sensitive points-to analysis called Data Structure Analysis (DSA) [31]. Several transformations in LLVM are based on DSA, including Automatic Pool Allocation [30]). As part of the analysis, DSA extracts LLVM types for a subset of memory objects in the program. It does this by using declared types in the LLVM code as speculative type information, and checks conservatively whether memory accesses to an object are consistent with those declared types\footnote{DSA is actually quite aggressive: it can often extract type information for objects stored into and loaded out of “generic” void* data structure, despite the casts to and from void*.} (note that it does not perform any type-inference or enforce type safety).

For a wide range of benchmarks, we measured the *fraction of static load and store operations* for which reliable type information about the accessed objects is available using DSA. Table 1 shows this statistic for the C benchmarks in SPEC CPU2000. Benchmarks written in a more disciplined style, (e.g., the Olden and Ptrdist benchmarks) had nearly perfect results, scoring close to 100% in most cases.

| Benchmark Name | Typed Accesses | Untyped Accesses | Typed Percent |
| --- | --- | --- | --- |
| 164.gzip | 1654 | 61 | 96.4% |
| 175.vpr | 4038 | 371 | 91.6% |
| 176.gcc | 25747 | 33179 | 43.7% |
| 177.mesa | 2811 | 19668 | 12.5% |
| 179.art | 572 | 0 | 100.0% |
| 181.mcf | 571 | 0 | 100.0% |
| 183.equake | 799 | 114 | 87.5% |
| 186.crafty | 9734 | 383 | 96.2% |
| 188.ammp | 2109 | 2598 | 44.8% |
| 197.parser | 1577 | 2257 | 41.1% |
| 253.perlbmk | 9678 | 22302 | 30.3% |
| 254.gap | 6432 | 15117 | 29.8% |
| 255.vortex | 13397 | 8915 | 60.0% |
| 256.bzip2 | 1011 | 52 | 95.1% |
| 300.twolf | 13028 | 1196 | 91.6% |
| average |  |  | 68.04% |

Table 1: *Loads and Stores which are provably typed* {#lattner-2004-llvm-tab-1 .table tag=05E9}

The table shows that many of these programs (164, 175, 179, 181, 183, 186, 256, & 300) have a surprisingly high proportion of memory accesses with reliable type information, despite using a language that does not encourage disciplined use of types. The leading cause of loss of type information in the remaining programs is the use of custom memory allocators (in 197, 254, & 255), inherently non-type-safe program constructs such as using different structure types for the same objects in different places (176, 253 & 254) and imprecision due to DSA (in 177 & 188). Overall, despite the use of custom allocators, casting to and from *void*, and other C tricks, DSA is still able to verify the type information for an average of 68% of accesses across these programs.

It is important to note that similar results would be very difficult to obtain if LLVM had been an untyped representation. Intuitively, checking that declared types are respected is much easier than inferring those types, for structure and array types in a low-level code representation. As an example, an earlier version of the LLVM C front-end was based on GCC’s RTL internal representation, which provided little useful type information, and both DSA and pool allocation were much less effective. Our new C/C++ front-end is based on the GCC Abstract Syntax Tree representation, which makes much more type information available.

### 4.1.2 How do high-level features map onto LLVM? {#lattner-2004-llvm-s4-1-2 .section tag=05EA}

Compared to source languages, LLVM is a much lower level representation. Even C, which itself is quite low-level, has many features which must be lowered by a compiler targeting LLVM. For example, complex numbers, structure copies, unions, bit-fields, variable sized arrays, and setjmp/longjmp all must be lowered by an LLVM C compiler. In order for the representation to support effective analyses and transformations, the mapping from source-language features to LLVM should capture the high-level operational behavior as cleanly as possible.

We discuss this issue by using C++ as an example, since it is the richest language for which we have an implemented front-end. We believe that all the complex, high-level features of C++ are expressed clearly in LLVM, allowing their behavior to be effectively analyzed and optimized:

• Implicit calls (e.g. copy constructors) and parameters (e.g. ‘this’ pointers) are made explicit.

• Templates are fully instantiated by the C++ front end before LLVM code is generated. (True polymorphic types in other languages would be expanded into equivalent code using non-polymorphic types in LLVM.)

• Base classes are expanded into nested structure types. For this C++ fragment:

class base1 { int Y; };
class base2 { float X; };
class derived : base1, base2 { short Z; };

the LLVM type for class derived is ‘{ {int}, {float}, short }’. If the classes have virtual functions, a v-table pointer would also be included and initialized at object allocation time to point to the virtual function table, described below.

• A virtual function table is represented as a global, *constant* array of typed function pointers, plus the type-id object for the class. With this representation, virtual method call resolution can be performed by the LLVM optimizer as effectively as by a typical source compiler (more effectively if the source compiler uses only per-module instead of cross-module pointer analysis).

• C++ exceptions are lowered to the ‘invoke’ and ‘unwind’ instructions as described in Section 2.4, exposing exceptional control flow in the CFG. In fact, having this information available at link time enables LLVM to use an interprocedural analysis to eliminate unused exception handlers. This optimization is much less effective if done on a per-module basis in a source-level compiler.

We believe that similarly clean LLVM implementations exist for most constructs in other language families like Scheme, the ML family, SmallTalk, Java and Microsoft CLI. We aim to explore these issues in the future, and preliminary work is underway on the implementation of JVM and OCaml front-ends.

### 4.1.3 How compact is the LLVM representation? {#lattner-2004-llvm-s4-1-3 .section tag=05EB}

Since code for the compiled program is stored in the LLVM representation throughout its lifetime, it is important that it not be too large. The flat, three-address form of LLVM is well suited for a simple linear layout, with most instructions requiring only a single 32-bit word each in the file. Figure 5 shows the size of LLVM files for SPEC CPU2000 executables after linking, compared to native X86 and 32-bit Sparc executables compiled by GCC 3.3 at optimization level -O3.

Figure.

Figure 5: Executable sizes for LLVM, X86, Sparc (in KB) {#lattner-2004-llvm-fig-5 .figure tag=05EC}

The figure shows that LLVM code is about the same size as native X86 executables (a denser, variable-size instruction set), and significantly smaller than SPARC (a traditional 32-bit instruction RISC machine). We believe this is a very good result given that LLVM encodes an infinite register set, rich type information, control flow information, and data-flow (SSA) information that native executables do not.

Currently, large programs are encoded less efficiently than smaller ones because they have a larger set of register values available at any point, making it harder to fit instructions into a 32-bit encoding. When an instruction does not fit into a 32-bit encoding, LLVM falls back on a 64-bit or larger encoding, as needed. Though it would be possible to make the fall back case more efficient, we have not attempted to do so. Also, as with native executables, general purpose file compression tools (e.g. bzip2) are able to reduce the size of bytecode files to about 50% of their uncompressed size, indicating substantial margin for improvement.

### 4.1.4 How fast is LLVM? {#lattner-2004-llvm-s4-1-4 .section tag=05ED}

An important aspect of LLVM is that the low-level representation enables efficient analysis and transformation, because of the small, uniform instruction set, the explicit CFG and SSA representations, and careful implementation of data structures. This speed is important for uses “late” in the compilation process (i.e., at link-time or run-time). In order to provide a sense for the speed of LLVM, Table 2 shows the table of runtimes for several interprocedural optimizations. All timings were collected on a 3.06GHz Intel Xeon processor. The LLVM compiler system was compiled using the GCC 3.3 compiler at optimization level -O3.

| Benchmark | DGE | DAE | inline | GCC |
| --- | --- | --- | --- | --- |
| 164.gzip | 0.0018 | 0.0063 | 0.0127 | 1.937 |
| 175.vpr | 0.0096 | 0.0082 | 0.0564 | 5.804 |
| 176.gcc | 0.0496 | 0.1058 | 0.6455 | 55.436 |
| 177.mesa | 0.0051 | 0.0312 | 0.0788 | 20.844 |
| 179.art | 0.0002 | 0.0007 | 0.0085 | 0.591 |
| 181.mcf | 0.0010 | 0.0007 | 0.0174 | 1.193 |
| 183.equake | 0.0000 | 0.0009 | 0.0100 | 0.632 |
| 186.crafty | 0.0016 | 0.0162 | 0.0531 | 9.444 |
| 188.ammp | 0.0200 | 0.0072 | 0.1085 | 5.663 |
| 197.parser | 0.0021 | 0.0096 | 0.0516 | 5.593 |
| 253.perlbmk | 0.0137 | 0.0439 | 0.8861 | 25.644 |
| 254.gap | 0.0065 | 0.0384 | 0.1317 | 18.250 |
| 255.vortex | 0.1081 | 0.0539 | 0.2462 | 20.621 |
| 256.bzip2 | 0.0015 | 0.0028 | 0.0122 | 1.520 |
| 300.twolf | 0.0712 | 0.0152 | 0.1742 | 11.986 |

Table 2: Interprocedural optimization timings (in seconds) {#lattner-2004-llvm-tab-2 .table tag=05EE}

The table includes numbers for several transformations: DGE (aggressive$^9$ Dead Global variable and function Elimination), DAE (aggressive Dead Argument and return value Elimination), and inline (a function integration pass). All these interprocedural optimizations work on the whole program at link-time. In addition, they spend most of their time traversing and modifying the code representation directly, so they reflect the costs of processing the representation.$^{10}$ As a reference for comparison, the GCC column indicates the total time the GCC 3.3 compiler takes to compile the program at -O3.

We find that in all cases, the optimization time is substantially less than that to compile the program with GCC, despite the fact that GCC does *no* cross module optimization, and very little interprocedural optimization within a translation unit. In addition, the interprocedural optimizations scale mostly linear with the number of transformations they perform. For example, DGE eliminates 331 functions and 557 global variables (which include string constants) from 255.vortex, DAE eliminates 103 arguments and 96 return values from 176.gcc, and ‘inline’ inlines 1368 functions (deleting 438 which are no longer referenced) in 176.gcc.

### 4.2 Applications using life-time analysis and optimization capabilities of LLVM {#lattner-2004-llvm-s4-2 .section tag=05EF}

Finally, to illustrate the capabilities provided by the compiler framework, we briefly describe three examples of how LLVM has been used for widely varying compiler problems, emphasizing some of the novel capabilities described in the introduction.

### 4.2.1 Projects using LLVM as a general compiler infrastructure {#lattner-2004-llvm-s4-2-1 .section tag=05F0}

As noted earlier, we have implemented several compiler techniques in LLVM. The most aggressive of these are

$^9$ “Aggressive” DCEs assume objects are dead until proven otherwise, allowing dead objects with cycles to be deleted.
$^{10}$ **DSA** (Data Structure Analysis) is a much more complex analysis, and it spends a negligible fraction of its time processing the code representation itself, so its run times are not indicative of the efficiency of the representation. It is interesting to note, however, that those times also are relatively fast compared with GCC compile times [31].

Data Structure Analysis (DSA) and Automatic Pool Allocation [30], which analyze and transform programs in terms of their logical data structures. These techniques inherit a few significant benefits from LLVM, especially, (a) these techniques are only effective if most of the program is available, i.e., at link-time; (b) type information is crucial for their effectiveness, especially pointers and structures; (c) the techniques are source-language independent; and (d) SSA significantly improves the precision of DSA, which is flow-insensitive.

Other researchers not affiliated with our group have been actively using or exploring the use of the LLVM compiler framework, in a number of different ways. These include using LLVM as an intermediate representation for binary-to-binary transformations, as a compiler back-end to support a hardware-based trace cache and optimization system, as a basis for runtime optimization and adaptation of Grid programs, and as an implementation platform for a novel programming language.

### 4.2.2 SAFECode: A safe low-level representation and execution environment {#lattner-2004-llvm-s4-2-2 .section tag=05F1}

SAFECode is a “safe” code representation and execution environment, based on a type-safe subset of LLVM. The goal of the work is to enforce memory safety of programs in the SAFECode representation through static analysis, by using a variant of automatic pool allocation instead of garbage collection [19], and using extensive interprocedural static analysis to minimize runtime checks [28, 19].

The SAFECode system exploits nearly all capabilities of the LLVM framework, except runtime optimization. It directly uses the LLVM code representation, which provides the ability to analyze C and C++ programs, which is crucial for supporting embedded software, middle-ware, and system libraries. SAFECode relies on the type information in LLVM (with no syntactic changes) to check and enforce type safety. It relies on the array type information in LLVM to enforce array bounds safety, and uses interprocedural analysis to eliminate runtime bounds checks in many cases [28]. It uses interprocedural safety checking techniques, exploiting the link-time framework to retain the benefits of separate compilation (a key difficulty that led previous such systems to avoid using interprocedural techniques [17, 23]).

### 4.2.3 External ISA design for Virtual Instruction Set Computers {#lattner-2004-llvm-s4-2-3 .section tag=05F2}

Virtual Instruction Set Computers [40, 16, 2] are processor designs that use two distinct instruction sets: an externally visible, virtual instruction set (V-ISA) which serves as the program representation for all software, and a hidden implementation-specific instruction set (I-ISA) that is the actual hardware ISA. A software translator co-designed with the hardware translates V-ISA code to the I-ISA transparently for execution, and is the only software that is aware of the I-ISA. This translator is essentially a sophisticated, implementation-specific back-end compiler.

In recent work, we argued that an extended version of the LLVM instruction set could be a good choice for the external V-ISA for such processor designs [2]. We proposed a novel implementation strategy for the virtual-to-native translator that enables offline code translation and caching of translated code in a completely OS-independent manner.

That work exploits the important features of the instruction set representation, and extends it to be suitable as a V-ISA for hardware. The fundamental benefit of LLVM for this work is that the LLVM code representation is low-level enough to represent arbitrary external software (including operating system code), yet provides rich enough information to support sophisticated compiler techniques in the translator. A second key benefit is the ability to do both offline and online translation, which is exploited by the OS-independent translation strategy.
