---
paper: backus-1978-vonneumann
title: Can Programming Be Liberated from the von Neumann Style? A Functional Style and Its Algebra of Programs
authors:
  - John Backus
year: 1978
venue: Communications of the ACM (Turing Award lecture)
field: languages
section: "16"
section_title: Summary
tag: "0581"
kind: section
lang: en
source: https://www.cs.cmu.edu/~crary/819-f09/Backus78.pdf
pdf_sha256: 2e412a7986c7fd1bdd060d90d035faa9ecc8a29675f99206c243da90954ca423
pdf_pages: 27-28
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 1f5534b66912fde37523d33b165da09a276d67653a27c767dc89de59fca7e540
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The fifteen preceding sections of this paper can be summarized as follows.

Section 1. Conventional programming languages are large, complex, and inflexible. Their limited expressive power is inadequate to justify their size and cost.

Section 2. The models of computing systems that underlie programming languages fall roughly into three classes: (a) simple operational models (e.g., Turing machines), (b) applicative models (e.g., the lambda calculus), and (c) von Neumann models (e.g., conventional computers and programming languages). Each class of models has an important difficulty: The programs of class (a) are inscrutable; class (b) models cannot save information from one program to the next; class (c) models have unusable foundations and programs that are conceptually unhelpful.

Section 3. Von Neumann computers are built around a bottleneck: the word-at-a-time tube connecting the CPU and the store. Since a program must make its overall change in the store by pumping vast numbers of words back and forth through the von Neumann bottleneck, we have grown up with a style of programming that concerns itself with this word-at-a-time traffic through the bottleneck rather than with the larger conceptual units of our problems.

Section 4. Conventional languages are based on the programming style of the von Neumann computer. Thus variables = storage cells; assignment statements = fetching, storing, and arithmetic; control statements = jump and test instructions. The symbol “:=” is the linguistic von Neumann bottleneck. Programming in a conventional—von Neumann—language still concerns itself with the word-at-a-time traffic through this slightly more sophisticated bottleneck. Von Neumann languages also split programming into a world of expressions and a world of statements; the first of these is an orderly world, the second is a disorderly one, a world that structured programming has simplified somewhat, but without attacking the basic problems of the split itself and of the word-at-a-time style of conventional languages.

Section 5. This section compares a von Neumann program and a functional program for inner product. It illustrates a number of problems of the former and advantages of the latter: e.g., the von Neumann program is repetitive and word-at-a-time, works only for two vectors named a and b of a given length n, and can only be made general by use of a procedure declaration, which has complex semantics. The functional program is nonrepetitive, deals with vectors as units, is more hierarchically constructed, is completely general, and creates “housekeeping” operations by composing high-level housekeeping operators. It does not name its arguments, hence it requires no procedure declaration.

Section 6. A programming language comprises a framework plus some changeable parts. The framework of a von Neumann language requires that most features must be built into it; it can accommodate only limited changeable parts (e.g., user-defined procedures) because there must be detailed provisions in the “state” and its transition rules for all the needs of the changeable parts, as well as for all the features built into the framework. The reason the von Neumann framework is so inflexible is that its semantics is too closely coupled to the state: every detail of a computation changes the state.

Section 7. The changeable parts of von Neumann languages have little expressive power; this is why most of the language must be built into the framework. The lack of expressive power results from the inability of von Neumann languages to effectively use combining forms for building programs, which in turn results from the split between expressions and statements. Combining forms are at their best in expressions, but in von Neumann languages an expression can only produce a single word; hence expressive power in the world of expressions is mostly lost. A further obstacle to the use of combining forms is the elaborate use of naming conventions.

Section 8. APL is the first language not based on the lambda calculus that is not word-at-a-time and uses functional combining forms. But it still retains many of the problems of von Neumann languages.

Section 9. Von Neumann languages do not have useful properties for reasoning about programs. Axiomatic and denotational semantics are precise tools for describing and understanding conventional programs, but they only talk about them and cannot alter their ungainly properties. Unlike von Neumann languages, the language of ordinary algebra is suitable both for stating its laws and for transforming an equation into its solution, all within the “language.”

Section 10. In a history-sensitive language, a program can affect the behavior of a subsequent one by changing some store which is saved by the system. Any such language requires some kind of state transition semantics. But it does not need semantics closely coupled to states in which the state changes with every detail of the computation. “Applicative state transition” (AST) systems are proposed as history-sensitive alternatives to von Neumann systems. These have: (a) loosely coupled state-transition semantics in which a transition occurs once per major computation; (b) simple states and transition rules; (c) an underlying applicative system with simple “reduction” semantics; and (d) a programming language and state transition rules both based on the underlying applicative system and its semantics. The next four sections describe the elements of this approach to non-von Neumann language and system design.

Section 11. A class of informal functional programming (FP) systems is described which use no variables. Each system is built from objects, functions, functional forms, and definitions. Functions map objects into objects. Functional forms combine existing functions to form new ones. This section lists examples of primitive functions and functional forms and gives sample programs. It discusses the limitations and advantages of FP systems.

Section 12. An “algebra of programs” is described whose variables range over the functions of an FP system and whose “operations” are the functional forms of the system. A list of some twenty-four laws of the algebra is followed by an example proving the equivalence of a nonrepetitive matrix multiplication program and a recursive one. The next subsection states the results of two “expansion theorems” that “solve” two classes of equations. These solutions express the “unknown” function in such equations as an infinite conditional expansion that constitutes a case-by-case description of its behavior and immediately gives the necessary and sufficient conditions for termination. These results are used to derive a “recursion theorem” and an “iteration theorem,” which provide ready-made expansions for some moderately general and useful classes of “linear” equations. Examples of the use of these theorems treat: (a) correctness proofs for recursive and iterative factorial functions, and (b) a proof of equivalence of two iterative programs. A final example deals with a “quadratic” equation and proves that its solution is an idempotent function. The next subsection gives the proofs of the two expansion theorems.

The algebra associated with FP systems is compared with the corresponding algebras for the lambda calculus and other applicative systems. The comparison shows some advantages to be drawn from the severely restricted FP systems, as compared with the much more powerful classical systems. Questions are suggested about algorithmic reduction of functions to infinite expansions and about the use of the algebra in various “lazy evaluation” schemes.

Section 13. This section describes formal functional programming (FFP) systems that extend and make precise the behavior of FP systems. Their semantics are simpler than that of classical systems and can be shown to be consistent by a simple fixed-point argument.

Section 14. This section compares the structure of Algol with that of applicative state transition (AST) systems. It describes an AST system using an FFP system as its applicative subsystem. It describes the simple state and the transition rules for the system. A small self-protecting system program for the AST system is described, and how it can be installed and used for file maintenance and for running user programs. The section briefly discusses variants of AST systems and functional naming systems that can be defined and used within an AST system.

Section 15. This section briefly discusses work on applicative computer designs and the need to develop and test more practical models of applicative systems as the future basis for such designs.

Acknowledgments. In earlier work relating to this paper I have received much valuable help and many suggestions from Paul R. McJones and Barry K. Rosen. I have had a great deal of valuable help and feedback in preparing this paper. James N. Gray was exceedingly generous with his time and knowledge in reviewing the first draft. Stephen N. Zilles also gave it a careful reading. Both made many valuable suggestions and criticisms at this difficult stage. It is a pleasure to acknowledge my debt to them. I also had helpful discussions about the first draft with Ronald Fagin, Paul R. McJones, and James H. Morris, Jr. Fagin suggested a number of improvements in the proofs of theorems.

Since a large portion of the paper contains technical material, I asked two distinguished computer scientists to referee the third draft. David J. Gries and John C. Reynolds were kind enough to accept this burdensome task. Both gave me large, detailed sets of corrections and overall comments that resulted in many improvements, large and small, in this final version (which they have not had an opportunity to review). I am truly grateful for the generous time and care they devoted to reviewing this paper.

Finally, I also sent copies of the third draft to Gyula A. Magó, Peter Naur, and John H. Williams. They were kind enough to respond with a number of extremely helpful comments and corrections. Geoffrey A. Frank and Dave Tolle at the University of North Carolina reviewed Magó’s copy and pointed out an important error in the definition of the semantic function of FFP systems. My grateful thanks go to all these kind people for their help.
