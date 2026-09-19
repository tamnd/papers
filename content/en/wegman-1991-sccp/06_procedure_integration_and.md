---
paper: wegman-1991-sccp
title: Constant Propagation with Conditional Branches
authors:
  - Mark N. Wegman
  - F. Kenneth Zadeck
year: 1991
venue: ACM TOPLAS
field: languages
section: "6"
section_title: PROCEDURE INTEGRATION AND INTERPROCEDURAL CONSTANT PROPAGATION
tag: 05CF
kind: section
lang: en
source: https://www.cs.utexas.edu/users/lin/cs380c/wegman.pdf
pdf_sha256: 40929436cdf1c477f2318221df5d0aa71488db4a01cc448b184e0aba8bf95ddb
pdf_pages: 19-27
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 30be115443d6e571459607ffbc063c56814580451d455b620e383aa9be98f1db
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Code optimization techniques are useful because it is desirable to program at a high level of abstraction and use automatic techniques to specialize the generic routines implementing the abstractions. Generic routines are usually implemented by procedures. The techniques discussed here are also applicable to generic methods in object-oriented programs.

Two techniques can be used to specialize generic procedures; the first is based on procedure integration and the second on interprocedural analysis. The distinctions between procedure integration and interprocedural analysis are important because

(1) at any particular call site, the full power of a generic routine may be unnecessary. Procedure integration provides separate copies of the procedure, each of which may be specialized differently for their respective call sites. Interprocedural analysis allows specialization of the procedure only in ways that are simultaneously appropriate to all sites.

(2) procedure integration breaks down the barrier between the call site and the called procedure. More powerful specialization techniques are available after procedure integration than after interprocedural analysis. For example, if the call site is inside a loop, a code motion algorithm may be able to move some of the code in the generic routine to a point outside the loop.

Fig. 13. Case missed if information is associated with nodes. {#wegman-1991-sccp-fig-13 .figure tag=05D0}

(setq i 1)
loop
    (cond ((greaterp i 10) (go out)))
    ...
    (setq i (plus i 1))
    (go loop)
out ; plus is a macro which expands in line to the following. It replaces
; x with the first argument to the macro and y with the second.

(cond
    ((and (integer x) (integer y))
        (integeradd x y))
    ;The result of integeradd is an integer.
    ...
)

Fig. 14. Removal of conditional type check. {#wegman-1991-sccp-fig-14 .figure tag=05D1}

(3) procedure integration may require an unacceptably large amount of space. In the case of recursion, a naive procedure integration algorithm may require an infinite amount of space.

To gain some intuition about kinds of code that might be integrated and the kinds of problems that might be encountered, consider the code fragment in Figure 14. Here the plus routine is a macro expanded by the compiler. We view the type field of a variable as a variable in its own right and perform constant propagation on the type field. This is a form of type inference. At compile time, the conditional expression for the execution-time type check can be eliminated. Our analysis proves that I is always an integer. However, to determine this, the branches of code producing floating point results must be eliminated. This can only be done when analysis shows that only integer values are passed in from the call site. Of course the analysis must optimistically assume that the arguments are integers.

In Section 6.1 we describe how to represent the semantics of procedure calls using SSA form. In Section 6.2 we show how constant propagation can be profitably combined with procedure integration. In Section 6.3 we give an algorithm to perform interprocedural constant propagation without encountering the space problems arising from procedure integration.

### 6.1 Procedure Calls in SSA Form {#wegman-1991-sccp-s6-1 .section tag=05D2}

Procedure calls have two effects. One is to transfer control to a procedure and the subsequent return; the other is to create instances of and to change the names of variables. SSA form easily models the control flow aspects of a procedure call, but changes may be required to model the passing of parameters to procedures.

The value returned from a function call is used as a normal expression value in the called procedure.

Each call-by-value parameter is modeled in SSA form by a single assignment statement. The actual parameters are simply assigned to the formal

```text
a ← 1
    a ← 1
        if IsAliased(a,b)
            then b ← a
b ← 2
    b ← 2
        if IsAliased(a,b)
            then a ← b
?← a
    ?← a
```

Fig. 15. Effect of potential alias (a, b) and insertion of resulting conditional assignments. {#wegman-1991-sccp-fig-15 .figure tag=05D3}

parameters, which are new variables in the called procedure. No variables at the call site can be affected.

Each call-by-value-return parameter is modeled in SSA form by two assignment statements. The first assigns the actual parameter to the formal parameter, and the second assigns the formal parameter back to the actual parameter; because we are using SSA form, this second assignment is implemented as an assignment to a new variable.

Each call-by-reference parameter is modeled as a call-by-value-return parameter, with one change: We must deal with problems caused by potential aliasing. Aliasing occurs when it is possible to generate two or more names for the same memory location. In many programming languages, aliasing limits where and to what extent certain optimizations can be performed. Storing into memory by way of one name may affect the value referenced by the other name. (The term “aliasing” can also mean the use of two expressions that, because of pointers, can refer to the same location. This problem is not addressed here.) The remainder of this section describes how to deal with aliasing.

Several program constructs involving procedure calls may give rise to potential aliases:

(1) A variable may be passed by reference in two or more parameter positions of a single call to a subroutine.
(2) A variable that is global to a procedure may be used by its name and also by a reference parameter in the call to the procedure.
(3) Any variable that is aliased to an argument to a procedure is also aliased to the parameter.

Aliasing information can be represented as a list of pairs of variable names for each procedure. If a pair (a, b) is a must-alias, then on all possible executions of the program, a and b must refer to the same storage location. Must-aliasing of (a, b) implies that any assignment to either a or b is an assignment to both a and b. If a pair (a, b) is a may-alias, then on some execution of the program, a and b may refer to the same storage location. Aliasing is not necessarily transitive: The existence of may-alias pairs (a, b) and (b, c) does not imply the existence of (a, c). May-aliasing of (a, b) means that when a store to b occurs along a path from a store into A to a use of a, the value of b may reach the use of a (see the left side of Figure 15). On some executions, a may have the value 1 and on others it may have the value 2. (The detection of potential aliases for a single procedure depends on the semantics of the particular language, and is beyond the scope of this paper.

For example, in some languages two variables cannot be aliased if they are of different types.)

Without some sort of interprocedural analysis, the number of potential aliases in a program is quite large, even though the number of actual aliases is small in practice. Banning [8] gives a simple procedure for computing a conservative estimate of the potential aliases. A variable can be viewed as aliased to itself. A formal parameter that is passed using call-by-reference can be aliased to any variable to which the actual parameter is aliased. One need only keep track of variables that are visible. Banning has created a worklist algorithm that is linear in the number of aliased pairs. Since aliasing is rare in real programs, this algorithm can be assumed to be efficient. Other algorithms exist; see Barth [9], Rosen [37], Myers [29], Cooper [15], and Burke [10].

Aliasing information may be represented in SSA form by inserting if - then structures after each assignment to a variable that is either may- or must-aliased, as shown on the right side of Figure 15. The statement on the then side is an assignment statement from the variable just defined to the variable to which it is aliased. This has the effect of joining the two aliased variables with a $\phi$-function. Once these additional if - then structures have been inserted, the SSA graph can be built as before. In Figure 15, two SSA edges would exist; each of these edges would go to a $\phi$-function that merges the potentially aliased variables.

The variable IsAliased(a,b) is evaluated as true if the pair is must-aliased. The assignment blocks any values of the aliased variable from reaching beyond the assignment of the first variable. The variable IsAliased(a,b) is evaluated as $\perp$ if the pair is may-aliased. Both values for the second variable are merged in the $\phi$-function that is inserted after the if - then. Such a definition is conservative; it is correct under all possible executions, whether or not the alias actually occurs.

The advantage of representing aliasing by if - then structures is that, as other types of analysis (such as constant propagation combined with procedure integration) proceed, the value of the IsAliased variables can often be determined to be true or false. Hence, if procedure Q with parameters a and b is integrated in procedure P from a call Q(x,x), then IsAliased(a,b) is true. If Q is integrated in procedure P from a call Q(x,y), then IsAliased(x,y) is assigned to IsAliased(a,b). In Sections 6.2 and 6.3, we discuss two techniques for refining the aliasing information as other analysis proceeds.

In the worst case, every variable in the original program may be aliased to every other variable. Each assignment statement in such a program would be followed by V if - then structures, swelling the program by a factor proportional to the number of variables. If the number of aliases is large, it is correct (although pessimistic) simply to assign $\perp$ to any variables involved in a large number of alias pairs and not insert the if - then structures. (Pointers can also be modeled as assignments from $\perp$.)

### 6.2 Procedure Integration {#wegman-1991-sccp-s6-2 .section tag=05D4}

The constant propagation techniques we have discussed seem to be well suited to performing some of the specializations needed when procedures are integrated. The specialized routines thus derived may be considerably smaller, as well as more efficient, than their generic progenitors. Moreover, we show how the techniques used in the SCC algorithm cause constant propagation to take time linear in the size of the resulting specialized procedure rather than the size of the generic one.

SCC has an advantage over SSC because the SCC algorithm can skip sections of the program that are inaccessible at execution time. In the compilers for languages such as Ada, C++, and PL.8 where procedure integration is performed, or in compilers for variants of C or LISP where macro expansion is performed, or when code is created by a program generator, this may provide a significant improvement in both compile-time and execution-time performance.

Aliasing information can be improved by performing procedure integration. The aliasing information for a procedure is computed on the conservative assumption that the procedure can be called from any of its call sites. Any procedure that has been integrated can, by definition, be called from only one call site. The number of aliases passed through this one call site is typically less than the number passed through a common instance of the procedure. Once a procedure has been integrated, the parameter binding through that call site can be determined and many of the potential aliases can be ignored.

The benefit derived by combining constant propagation and procedure integration varies depending on the style of programming, the size of the program being compiled, the level of programming language being used, the other optimizations performed by the compiler, and how well those optimizations are integrated. If the programming style is to perform many optimizations by hand (such as procedure integration and constant propagation), many of the opportunities the compiler would have found may well have already been taken. If, however, the program is large, or has been frequently modified, then the programmer often loses track of opportunities for optimization. Higher-level languages, for example, LISP, ML, and SETL, inhibit the programmer from making too many low-level decisions. In languages such as C, FORTRAN, or Pascal, however, the programmer is free, and often required, to make many low-level decisions. This allows a programmer to write programs in such a way that the optimizer finds few opportunities for optimization other than those associated with arrays or register allocation. If the input to the compiler is fairly high level, a compiler that implements an aggressive set of well integrated optimizations is likely to find more opportunities to improve the program than one that does not.

It is therefore difficult to say whether one optimization is good or bad, and it is unlikely that any single study will provide a definitive result. Reports in the area are mixed.

Allen et al. [4], looking at a large sample of programs, have found that over 24 percent of all parameters to subroutines in PL/I are lexically constants. Presumably any global constant propagation algorithm would find additional ones. Moreover, in languages that make heavy use of generics or where runtime type information is needed, constant propagation has even more potential to be helpful.

Scheifler [39] studied procedure integration in CLU but did not consider performing any subsequent optimizations. He reported that procedure integration alone improved the performance of the resulting program, but at a considerable expense in the program size.

On the positive side, Ball [7] considered the effects of procedure integration on optimization, doing a form of ad hoc data flow analysis to estimate the effects of passing a constant parameter to a procedure. He reports positive results on the size and execution time of the compiled code, even though his constant propagation technique discovers only the simple constants. The ECS compiler at IBM [4] by design relied heavily on the use of procedure integration and subsequent tailoring of the code. Appel and Tim [6] used procedure integration (called beta-reduction in the LISP community) along with many optimizations in their ML compiler, and they report positive results.

On the negative side, Richardson and Ganapathi [35] studied the effects of optimization and procedure integration on five programs averaging 1200 lines each. They found that both procedure integration and optimization were of benefit separately, but their combined benefit was in general no more than the product of their separate benefits.

6.2.1 *The Procedure Integration Algorithm.* Procedure integration can be combined with constant propagation to achieve a better result than either separately. A prepass can create the SSA graph for each procedure. We can integrate only those statements that are executable based on constant propagation through the SSA graph of the procedure.

Time and space are saved by combining procedure integration with constant propagation rather than the more naive approach of integrating and then doing constant propagation. If one integrates first, one must expend both time and space in copying parts of the code not relevant for that execution, and then these irrelevant parts must be thrown away. In many compilers that perform procedure integration, the data flow information is not collected until after the integration.

The space explosion can be controlled by limiting the number of procedures that are inlined. There are three general strategies for choosing what to inline:

— Compiler directives. The programmer chooses some procedures that are inlined by the compiler or a preprocessor.
— Static analysis. The compiler analyzes the program and chooses some set of procedures to integrate. Common choices include integrating only leaf procedures or procedure calls nested within loops.
— Performance measurement. The program is compiled and run using some test data. Instrumentation is added to the program to count either the number of times each procedure is called or the number of times each procedure call is made.7

7 The latter produces more precise information, since a single procedure may be called from many different locations and the frequency of each call may be different.

Constant Propagation With Conditional Branches

The first two strategies are easy to implement but do not generally inline the best set of procedures. The last produces better results but is cumbersome, since good test data is required and the program must be compiled several times.

Some modifications to SCC are necessary to perform procedure integration as described above, since procedure integration requires copying the code rather than simply marking it as executable. As the code is copied, edges must be updated so that the branches in the copied code point into the copied code rather than into the uninstantiated internal representation of the subroutine.

The problem is how to determine whether a node has been instantiated and, if so, where it resides. The solution is a global hash table that contains one entry for each instantiated node. The key in the hash table is constructed by concatenating two items: the name of the call site from which the procedure is being instantiated and the name of the node in the uninstantiated version (the place from which the code is being copied). The data in the hash table is the location at which the node was instantiated. Each newly instantiated node needs to record the name of the call site so that its branches can in turn be looked up in the hash table.

When a control flow graph edge is taken from the FlowWorkList, its target is looked up in the hash table. If a match is found, the algorithm looks at the data field to find the instantiated block. If a match if not found, the block has not yet been instantiated, and it must then be instantiated and added to the hash table. The hash table replaces the ExecutableFlag found in the single-procedure version of SCC.

SCC requires that all LatticeCells be initialized to $\top$ and that all ExecutableFlags are initialized to false. A naive implementation would require a pass over the entire procedure (even parts that would not be integrated) to perform this initialization. Instead, each LatticeCell and ExecutableFlag can be initialized as their defining nodes are copied. LatticeCells also reside in the hash table indexed by their name and the name of the instantiating call site.

### 6.3 Interprocedural Constant Propagation {#wegman-1991-sccp-s6-3 .section tag=05D5}

The algorithm described in Section 6.2 can be viewed as a good, but sometimes unreasonably expensive, form of interprocedural constant propagation. The expense is a result of making explicit all possible paths through the program by expanding all of the procedures inline. If the program has recursive procedures, then the inlining process can be unbounded; otherwise, it may be exponential.

Where no procedure integration is performed, a variant of the procedure integration algorithm can perform interprocedural constant propagation. The statements in the procedure being integrated are not copied but are simply marked as being executable. This marking indicates that the statement may be executable along some path in the full program. Each call site to a given procedure jumps to the location where the procedure starts. The aliasing information at the entrance of the procedure is the meet of the aliasing

ACM Transactions on Programming Languages and Systems, Vol. 13, No. 2, April 1991.

information at each of the call sites. In effect, the SSA graph for the entire program looks like the interprocedural def-use chains described by Allen in [3].

This algorithm has the advantage that the amount of work required for constant propagation over the entire program is linear in the sum of the sizes of the SSA graph for each procedure; however, it has the disadvantage that the number of constants found may be small, since the only constants propagated across a procedure boundary are those having the same constant value at all call sites. This algorithm finds a class of aliases closely related to those found by Banning [8]. Our algorithm is more precise because it takes advantage of knowledge discovered during constant propagation.

Myers [29] describes two frameworks for performing several forms of interprocedural analysis. In his flow-sensitive framework, all paths through all procedures are examined. It is not surprising that the problems he investigated are intractable in this framework. In his flow-insensitive framework, the data-flow information for each procedure is summarized and the interprocedural information is created from this summary information and the call graph of the program. While Myers did not consider constant propagation, he did consider alias analysis. Our algorithm discovers many facts that, in Myers’ terms, require flow-sensitive analysis, and yet the cost of our algorithm is linear in the size of the full program. Our algorithm is more precise because it takes advantage of knowledge discovered during constant propagation.

Two algorithms for interprocedural constant propagation have been published based on research done around the time of our conference paper [44]. The works by Callahan, Cooper, Kennedy, and Torczon [12], and Burke and Cytron [11] are motivated by two concerns: The amount of space may still be prohibitively large, since the entire program must be in memory at one time for the analysis, and any change in one procedure may force re-analysis of the entire program.8 The algorithms in [11] and [12] can both be broken down into four steps. The details of each step differ between the two algorithms and the interested reader should see each paper for further information.

(1) Compute the interprocedural aliasing information.
(2) Compute the intraprocedural constants.
(3) Summarize each procedure to determine the effects of interprocedural constants.
(4) Propagate the interprocedural constants along the paths in the call graph.

The novel aspect of these algorithms is how they summarize the functions and propagate the summarized results. While they address the time and space problems of our algorithm, they miss many of the constants that our

8Some people believe that even with large virtual memories, a worklist algorithm such as ours with fairly random access patterns over a large space will perform poorly. No hard data is available to resolve this.

algorithm finds. In addition, these algorithms are primarily intended for use in FORTRAN compilers, a program base in which data abstraction is rarely used; many of the interprocedural constants found by our algorithm are introduced by the use of data abstraction.

The weakness of the algorithms in [11, 12] is that there is no feedback between the steps. Discovering that certain values are constant may allow the discovery that some call is not executed. Discovering that some call is not executed may improve the aliasing information (yield fewer aliases into the called procedure) and may make more constants available into that routine, since the parameters are joined along fewer paths.
