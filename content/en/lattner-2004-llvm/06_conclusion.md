---
paper: lattner-2004-llvm
title: 'LLVM: A Compilation Framework for Lifelong Program Analysis & Transformation'
authors:
  - Chris Lattner
  - Vikram Adve
year: 2004
venue: CGO
field: languages
section: "6"
section_title: CONCLUSION
tag: 05F4
kind: section
lang: en
source: https://doi.org/10.1109/cgo.2004.1281665
pdf_sha256: 0352543b42fca1c88c3a74b3223a9da68f686435a64d3321450bda4655e4965c
pdf_pages: 11-12
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: c4300e6b914e622e156d59bb38e674ac3186074455abe87a2e3a8eeeb7b6af35
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

This paper has described LLVM, a system for performing lifelong code analysis and transformation, while remaining transparent to programmers. The system uses a low-level, typed, SSA-based instruction set as the persistent representation of a program, but without imposing a specific runtime environment. The LLVM representation is language independent, allowing all the code for a program, including system libraries and portions written in different languages, to be compiled and optimized together. The LLVM compiler framework is designed to permit optimization at all stages of a software lifetime, including extensive static optimization, online optimization using information from the LLVM code, and idle-time optimization using profile information gathered from programmers in the field. The current implementation includes a powerful link-time global and interprocedural optimizer, a low-overhead tracing technique for runtime optimization, and Just-In-Time and static code generators.

We showed experimentally and based on experience that LLVM makes available extensive type information even for C programs, which can be used to safely perform a number of aggressive transformations that would normally be attempted only on type-safe languages in source-level compilers. We also showed that the LLVM representation is comparable in size to X86 machine code and about 25% smaller than SPARC code on average, despite capturing much richer type information as well as an infinite register set in SSA form. Finally, we gave several examples of whole-program optimizations that are very efficient to perform on the LLVM representation. A key question we are exploring currently is whether high-level language virtual machines can be implemented effectively on top of the LLVM runtime optimization and code generation framework.

7. REFERENCES
[1] A.-R. Adl-Tabatabai, G. Langdale, S. Lucco, and R. Wahbe. Efficient and language-independent mobile programs. In Proc. ACM SIGPLAN 1996 Conference on Programming Language Design and Implementation, pages 127–136. ACM Press, 1996.
[2] V. Adve, C. Lattner, M. Brukman, A. Shukla, and B. Gaeke. LLVA: A Low-level Virtual Instruction Set Architecture. In 36th Int’l Symp. on Microarchitecture, pages 205–216, San Diego, CA, Dec 2003.
[3] W. Amme, N. Dalton, J. von Ronne, and M. Franz. SafeTSA: A type safe and referentially secure mobile-code representation based on static single assignment form. In PLDI, June 2001.
[4] ANDF Consortium. The Architectural Neutral Distribution Format. http://www.andf.org/.
[5] A. Ayers, S. de Jong, J. Peyton, and R. Schooler. Scalable cross-module optimization. ACM SIGPLAN Notices, 33(5):301–312, 1998.
[6] V. Bala, E. Duesterwald, and S. Banerjia. Dynamo: A transparent dynamic optimization system. In PLDI, pages 1–12, June 2000.
[7] M. Burke and L. Torczon. Interprocedural optimization: eliminating unnecessary recompilation. Trans. Prog. Lang. and Sys, 15(3):367–399, 1993.

[8] M. G. Burke et al. The Jalapeño Dynamic Optimizing Compiler for Java. In Java Grande, pages 129–141, 1999.
[9] D. Chase. Implementation of exception handling. The Journal of C Language Translation, 5(4):229–240, June 1994.
[10] J. Chen, D. Wu, A. W. Appel, and H. Fang. A provably sound TAL for back-end optimization. In PLDI, San Diego, CA, Jun 2003.
[11] A. Chernoff, et al. FX!32: A profile-directed binary translator. IEEE Micro, 18(2):56–64, 1998.
[12] T. M. Chilimbi, B. Davidson, and J. R. Larus. Cache-conscious structure definition. In ACM Symp. on Prog. Lang. Design and Implementation, Atlanta, GA, May 1999.
[13] CodeSourcery, Compaq, et al. C++ ABI for Itanium. http://www.codesourcery.com/cxx-abi/abi.html, 2001.
[14] R. Cohn, D. Goodwin, and P. Lowney. Optimizing Alpha executables on Windows NT with Spike. Digital Technical Journal, 9(4), 1997.
[15] R. Cytron, J. Ferrante, B. K. Rosen, M. N. Wegman, and F. K. Zadeck. Efficiently computing static single assignment form and the control dependence graph. Trans. Prog. Lang. and Sys., pages 13(4):451–490, October 1991.
[16] J. C. Dehnert, et al. The Transmeta Code Morphing Software: Using speculation, recovery and adaptive retranslation to address real-life challenges. In 1st IEEE/ACM Symp. Code Generation and Optimization, San Francisco, CA, Mar 2003.
[17] R. DeLine and M. Fahndrich. Enforcing high-level protocols in low-level software. In PLDI, Snowbird, UT, June 2001.
[18] L. P. Deutsch and A. M. Schiffman. Efficient implementation of the smalltalk-80 system. In 11th Symp. on Principles of Programming Languages, pages 297–301, Jan 1984.
[19] D. Dhurjati, S. Kowshik, V. Adve, and C. Lattner. Memory safety without runtime checks or garbage collection. In Languages, Compilers, and Tools for Embedded Systems (LCTES), San Diego, Jun 2003.
[20] K. Ebcioğlu and E. R. Altman. DAISY: Dynamic compilation for 100% architectural compatibility. In ISCA, pages 26–37, 1997.
[21] M. F. Fernández. Simple and effective link-time optimization of Modula-3 programs. ACM SIGPLAN Notices, 30(6):103–115, 1995.
[22] M. Franz and T. Kistler. Slim binaries. Communications of the ACM, 40(12), 1997.
[23] D. Grossman, G. Morrisett, T. Jim, M. Hicks, Y. Wang, and J. Cheney. Region-based memory management in cyclone. In PLDI, Berlin, Germany, June 2002.
[24] D. L. Heine and M. S. Lam. A practical flow-sensitive and context-sensitive c and c++ memory leak detector. In PLDI, pages 168–181, 2003.
[25] M. Hind. Which pointer analysis should i use? In Int’l Symp. on Software Testing and Analysis, 2000.
[26] IBM Corp. XL FORTRAN: Eight Ways to Boost Performance. White Paper, 2000.
[27] T. Kistler and M. Franz. Continuous program optimization: A case study. ACM Trans. on Prog. Lang. and Sys., 25(4):500–548, Jul 2003.
[28] S. Kowshik, D. Dhurjati, and V. Adve. Ensuring code safety without runtime checks for real-time control systems. In Compilers, Architecture and Synthesis for Embedded Systems (CASES), Grenoble, Oct 2002.
[29] C. Lattner and V. Adve. LLVM Language Reference Manual. http://llvm.cs.uiuc.edu/docs/LangRef.html.
[30] C. Lattner and V. Adve. Automatic Pool Allocation for Disjoint Data Structures. In Proc. ACM SIGPLAN Workshop on Memory System Performance, Berlin, Germany, Jun 2002.
[31] C. Lattner and V. Adve. Data Structure Analysis: A Fast and Scalable Context-Sensitive Heap Analysis. Tech. Report UIUCDCS-R-2003-2340, Computer Science Dept., Univ. of Illinois at Urbana-Champaign, Apr 2003.
[32] T. Lindholm and F. Yellin. The Java Virtual Machine Specification. Addison-Wesley, Reading, MA, 1997.
[33] E. Meijer and J. Gough. A technical overview of the Common Language Infrastructure, 2002. http://research.microsoft.com/emeijer/Papers/CLR.pdf.
[34] Microsoft Corp. Managed extensions for c++ specification. .NET Framework Compiler and Language Reference.
[35] G. Morrisett, D. Walker, K. Crary, and N. Glew. From System F to typed assembly language. Trans. Prog. Lang. and Systems, 21(3):528–569, May 1999.
[36] R. Muth. Alto: A Platform for Object Code Modification. Ph.d. Thesis, Department of Computer Science, University of Arizona, 1999.
[37] T. Romer, G. Voelker, D. Lee, A. Wolman, W. Wong, H. Levy, B. Bershad, and B. Chen. Instrumentation and optimization of Win32/Intel executables using Etch. In Proc. USENIX Windows NT Workshop, August 1997.
[38] Z. Shao, C. League, and S. Monnier. Implementing Typed Intermediate Languages. In Int’l Conf. on Functional Prog., pages 313–323, 1998.
[39] A. Shukla. Lightweight, cross-procedure tracing for runtime optimization. Master’s thesis, Comp. Sci. Dept., Univ. of Illinois at Urbana-Champaign, Urbana, IL, Aug 2003.
[40] J. E. Smith, T. Heil, S. Sastry, and T. Bezenek. Achieving high performance via co-designed virtual machines. In Int’l Workshop on Innovative Architecture (IWIA), 1999.
[41] A. Srivastava and D. W. Wall. A practical system for intermodule code optimization at link-time. Journal of Programming Languages, 1(1):1–18, Dec. 1992.
[42] T. Steel. Uncol: The myth and the fact. Annual Review in Automated Programming 2, 1961.
[43] D. Ungar and R. B. Smith. Self: The power of simplicity. In OOPSLA, 1987.
[44] D. Wall. Global register allocation at link-time. In Proc. SIGPLAN ’86 Symposium on Compiler Construction, Palo Alto, CA, 1986.
