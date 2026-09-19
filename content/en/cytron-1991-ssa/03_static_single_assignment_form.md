---
paper: cytron-1991-ssa
title: Efficiently Computing Static Single Assignment Form and the Control Dependence Graph
authors:
  - Ron Cytron
  - Jeanne Ferrante
  - Barry K. Rosen
  - Mark N. Wegman
  - F. Kenneth Zadeck
year: 1991
venue: ACM TOPLAS
field: languages
section: "3"
section_title: STATIC SINGLE ASSIGNMENT FORM
tag: "0587"
kind: section
lang: en
source: https://www.cs.utexas.edu/~pingali/CS380C/2010/papers/ssaCytron.pdf
pdf_sha256: 307512bb537628c2b326b23aa02109e7562bfc619509e942e015054ab58eb9ab
pdf_pages: 7-13
extraction: vision
extraction_model: gpt-5
content_sha256: e04f985c7e5d786576003192c0f32fb480e50cdc77cd7faec2afe5fa298f687c
edited: true
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

This section initially assumes that programs have been expanded to an intermediate form in which each statement evaluates some expressions and uses the results either to determine a branch or to assign to some variables. (Other program constructs are considered in Section 3.1.) An assignment statement $A$ has the form $LHS(A) \leftarrow RHS(A)$, where the left-hand side $LHS(A)$ is a tuple of distinct target variables $\langle U, V, \ldots \rangle$ and the right-hand side $RHS(A)$ is a tuple of expressions, with the same length as the $LHS$ tuple. Each target variable in $LHS(A)$ is assigned the corresponding value from $RHS(A)$. In the examples already discussed, all tuples are 1-tuples, and there is no need to distinguish between $V$ and $\langle V \rangle$. Section 3.1 sketches the use of longer tuples in expanding other program constructs (such as procedure calls) so as to make explicit the variables used and/or changed by the statements in the source program. Such explicitness is a prerequisite for most optimizations anyway. The only novelty in our use of tuples is the fact that they provide a simple and uniform way to fold the results of analysis into the intermediate text. Practical concerns about the size of the intermediate text are addressed in Section 3.1.

Translating a program into SSA form is a two-step process. In the first step, some trivial $\phi$-functions $V \leftarrow \phi(V, V, \ldots)$ are inserted at some of the join nodes in the program's control flow graph. In the second step, new variables $V_i$ (for $i = 0, 1, 2, \ldots$) are generated. Each mention of a variable $V$ in the program is replaced by a mention of one of the new variables $V_i$, where a *mention* may be in a branch expression or on either side of an assignment statement. Throughout this paper, an assignment statement may be either an ordinary assignment or a $\phi$-function. Figure 6 displays the result of translating a simple program to SSA form.

A $\phi$-function at entrance to a node $X$ has the form $V \leftarrow \phi(R, S, \ldots)$, where $V, R, S, \ldots$ are variables. The number of operands $R, S, \ldots$ is the number of control flow predecessors of $X$. The predecessors of $X$ are listed in some arbitrary fixed order, and the $j$th operand of $\phi$ is associated with the $j$th

```text
I ← 1
J ← 1
K ← 1
L ← 1
repeat
    I₁ ← 1
    J₁ ← 1
    K₁ ← 1
    L₁ ← 1
    repeat
        I₂ ← φ(I₃, I₁)
        J₂ ← φ(J₄, J₁)
        K₂ ← φ(K₅, K₁)
        L₂ ← φ(L₉, L₁)
        if (P)
            then do
                J ← I
                if (Q)
                    then L ← 2
                    else L ← 3
                K ← K + 1
            end
        else K ← K + 2
    print(I, J, K, L)
    repeat
        if (R)
            then L ← L + 4
        until (S)
        I ← I + 6
until (T)

I₁ ← 1
J₁ ← 1
K₁ ← 1
L₁ ← 1
repeat
    I₂ ← φ(I₃, I₁)
    J₂ ← φ(J₄, J₁)
    K₂ ← φ(K₅, K₁)
    L₂ ← φ(L₉, L₁)
    if (P)
        then do
            J₃ ← I₂
            if (Q)
                then L₃ ← 2
                else L₄ ← 3
            L₅ ← φ(L₃, L₄)
            K₃ ← K₂ + 1
        end
    else K₄ ← K₂ + 2
        J₄ ← φ(J₃, J₂)
        K₅ ← φ(K₃, K₄)
        L₆ ← φ(L₂, L₅)
    print(I₂, J₄, K₅, L₆)
    repeat
        L₇ ← φ(L₉, L₆)
        if (R)
            then L₈ ← L₇ + 4
            L₉ ← φ(L₈, L₇)
        until (S)
        I₃ ← I₂ + 6
    until (T)
```

Fig. 6  Simple program and its SSA form.

predecessor. If control reaches X from its jth predecessor, then the run-time support¹ remembers j while executing the φ-functions in X. The value of φ(R, S, ...) is just the value of the jth operand. Each execution of a φ-function uses only one of the operands, but which one depends on the flow of control just before entering X. Any φ-functions in X are executed before the ordinary statements in X. Some variants of φ-functions as defined here are useful for special purposes. For example, each φ-function can be tagged

¹When SSA form is used only as an intermediate form (Figure 1), there is no need actually to provide this support. For us, the semantics of φ are only important when assessing the correctness of intermediate steps in a sequence of program transformations beginning and ending with code that has no φ-functions. Others [6, 11, 52] have found it useful to give φ another parameter that incidentally encodes j, under various restrictions on the control flow.

with the node $X$ where it appears [5]. When the control flow of a language is suitably restricted, each $\phi$-function can be tagged with information about conditionals or loops [5, 6, 11, 52]. The algorithms in this paper apply to such variants as well.

SSA form may be considered as a property of a single program or as a relation between two programs. A single program is defined to be *in* SSA form if each variable is a target of exactly one assignment statement in the program text. Translation *to* SSA form replaces the original program by a new program with the same control flow graph. For every original variable $V$, the following conditions are required of the new program:

(1) If two nonnull paths $X \xrightarrow{+} Z$ and $Y \xrightarrow{+} Z$ converge at a node $Z$, and nodes $X$ and $Y$ contain assignments to $V$ (in the original program), then a trivial $\phi$-function $V \leftarrow \phi(V, \ldots, V)$ has been inserted at $Z$ (in the new program).
(2) Each mention of $V$ in the original program or in an inserted $\phi$-function has been replaced by a mention of a new variable $V_i$, leaving the new program in SSA form.
(3) Along any control flow path, consider any use of a variable $V$ (in the original program) and the corresponding use of $V_i$ (in the new program). Then $V$ and $V_i$ have the same value.

Translation to *minimal* SSA form is translation to SSA form with the proviso that the number of $\phi$-functions inserted is as small as possible, subject to Condition (1) above. The optimizations that depend on SSA form are still valid if there are some extraneous $\phi$-functions beyond those that would appear in minimal SSA form. However, extraneous $\phi$-functions can cause information to be lost, and they always add unnecessary overhead to the optimization process itself. Thus, it is important to place $\phi$-functions only where they are required. One variant of SSA form [52] would sometimes forego placing a $\phi$-function at a convergence point $Z$, so long as there are no more uses for $V$ in or after $Z$. The $\phi$-function could then be omitted without any risk of losing Condition (3). This has been called *pruned* SSA form [16], and it is sometimes preferable to our placement at all convergence points. However, as Figure 16 in Section 7 illustrates, our form is sometimes preferable to pruned form. When desired, pruned SSA form can be obtained by a simple adjustment of our algorithm [16, Section 5.1].

For any variable $V$, the nodes at which we should insert $\phi$-functions in the original program can be defined recursively by Condition (1) in the definition of SSA form. A node $Z$ *needs a $\phi$-function for* $V$ if $Z$ is a convergence point for two paths that originate at two different nodes, both nodes containing assignments to $V$ or needing $\phi$-functions for $V$. Nonrecursively, we may observe that a node $Z$ needs a $\phi$-function for $V$ because $Z$ is a convergence point for two nonnull paths $X \xrightarrow{+} Z$ and $Y \xrightarrow{+} Z$ that start at nodes $X$ and $Y$ already containing assignments to $V$. If $Z$ did not already contain an assignment to $V$, then the $\phi$-function inserted at $Z$ adds $Z$ to the set of nodes that contain assignments to $V$. With more nodes to consider as origins of paths, we may observe more nodes appearing as convergence points of nonnull paths originating at nodes with assignments to V. The set of nodes needing $\phi$-functions could thus be found by iterating an observation/insertion cycle.$^2$ The algorithm presented here obtains the same end results in much less time.

### 3.1 Other Program Constructs {#cytron-1991-ssa-s3-1 .section tag=0588}

If the source program computes expressions using constants and scalar variables to assign values to scalar variables, then it is straightforward to derive an intermediate text that is ready to be put into SSA form (or otherwise analyzed and transformed by an optimizing compiler). However, source programs commonly use other constructs as well: Some variables are not scalars, and some computations do not explicitly indicate which variables they use or change. This section sketches how to map some important constructs to an explicit intermediate text suitable for use in a compiler.

3.1.1 *Arrays.* It will suffice to consider one-dimensional arrays here. Arrays of higher dimension involve more notation but no more concerns.

If **A** and **B** are array variables, then array assignment statements like **A** \leftarrow **B** or **A** \leftarrow **0**, if allowed by the source language, can be treated just like assignments to scalar variables. Many of the mentions of **A(i)** for some index **i**, which may be taken to be an integer variable. Treating **A(i)** as a variable would be awkward, both because an assignment to **A(i)** may or may not change the value of **A(j)** and because the value of **A(i)** could be changed by assigning to **i** rather than to **A(i)**. An easier approach is illustrated in Figure 7. The entire array is treated like a single scalar variable, which may be one of the operands of **Access** or **Update**.$^3$ The expression **Access(A, i)** evaluates to the ith component of **A**; the expression **Update(A, j, V)** evaluates to an array value that is of the same size as **A** and has the same component values, except for **V** as the value of the jth component. Assigning a scalar value **V** to **A(j)** is equivalent to assigning an array value to the entire array **A**, where the new array value depends on the old one, as well as on the index **j** and on the new scalar value **V**. The translation to SSA form is unconcerned with whether the values of variables are large objects or what the operators mean.

As with scalars, translation of array references to SSA form removes some anti- and output-dependences [32]. In the program in Figure 7a, dependence analysis may prohibit reordering the use of **A(i)** by the first statement and the definition of **A(j)** by the second statement. After translation to SSA form, the two references to **A** have been renamed, and reordering is then possible. For example, the two statements can execute concurrently. Where optimization does not reorder the two references, Section 7.2 describes how translation out of SSA form reclaims storage that would otherwise be necessary to maintain distinct variables.

\footnotetext{
$^2$In typical cases, paths originating at $\phi$-functions add nothing beyond the contributions from paths originating at ordinary assignments. The straightforward iteration is still too slow, even in typical cases
$^3$This notation is similar to *Select* and *Update* [24], which, in turn, is similar to notation for referencing aggregate structures in a data flow language [23].
}

$$
\begin{array}{lll}
\leftarrow \mathbf{A}(i) & \leftarrow \operatorname{Access}(\mathbf{A}, i) & \leftarrow \operatorname{Access}(\mathbf{A}_8, i_7) \\
\mathbf{A}(j) \leftarrow V & \mathbf{A} \leftarrow \operatorname{Update}(\mathbf{A}, j, V) & \mathbf{A}_9 \leftarrow \operatorname{Update}(\mathbf{A}_8, j_6, V_5) \\
\leftarrow \mathbf{A}(k) + 2 & T \leftarrow \operatorname{Access}(\mathbf{A}, k) & T_1 \leftarrow \operatorname{Access}(\mathbf{A}_9, k_4) \\
\leftarrow T + 2 & \leftarrow T_1 + 2 &
\end{array}
$$

(a) (b) (c)

Fig. 7. Source code with array component references (a) is equivalent to code with explicit Access and Update operators that treat the array A just like a scalar (b). Transformation to SSA form proceeds as usual (c). {#cytron-1991-ssa-fig-7 .figure tag=0589}

Consider the loop shown in Figure 8a, which assigns to every component of array A. The value assigned to each component $\mathbf{A}(i)$ does not depend (even indirectly) on any of the values previously assigned to components of A. In terms of its effect on A, the whole loop is like an assignment of the form $\mathbf{A} \leftarrow (\ldots)$, where A is not used in (\ldots). Any assignment to a component of A that is not used before entering such an initialization loop is dead code that should be eliminated. With or without SSA form, the Update operator in Figure 8b makes A appear to be live at entry to the loop.

One reasonable response to the crudeness of the Update operator is to accept it. Address calculations and other genuine scalar calculations can still be optimized extensively. Another response is to perform dependence analysis [3, 10, 32, 51], which can sometimes determine that no subsequent accesses of A require values produced by any other assignment to A. Such is the case for each execution of the assignment to $\mathbf{A}(i)$ in Figure 8a. The assignment statement can then be viewed as an initialization of A. The problem for us, or for anyone who uses Update to make arrays look like scalars, is to communicate some of the results of dependence analysis to optimizations (like dead code elimination) that are usually formulated in terms of "scalar" variables. A simple solution to this formal problem is shown in Figure 8c, where the HiddenUpdate operator does not mention the assigned array operand. The actual code generated for an assignment from a HiddenUpdate expression is exactly the same as for an assignment from the corresponding Update expression, where the hidden operand is supplied by the target of the assignment.

3.1.2 Structures. A structure can be generally regarded as an array, where references to structure fields are treated as references to elements of the array. Thus, an assignment to a structure field is translated into an Update of the structure, and a use of a structure field is translated into an Access of the structure. In the prevalent case of simple structure field references, this treatment results in arrays whose elements are indexed by constants. Dependence analysis can often determine independence among such accesses, so that optimizations may move an assignment to one field far from an assignment to another field. If analysis or language semantics reveals a structure whose n fields are always accessed disjointly, then the structure can be decomposed into $n$ distinct variables. The elements of such structures are united in the source program only for organizational reasons, and the expression of the structure's decomposition in SSA form makes the program's actual use of the structure more apparent to subsequent optimization.

```text
integer A(1:100)
integer A₀(1:100)
integer A₁(1:100)
integer A₂(1:100)
i ← 1
repeat
    i₂ ← φ(i₁, i₃)
    A₁ ← φ(A₀, A₂)
    A₂ ← Update(A₁, i₂, i₂)
    i₃ ← i₂ + 1
    A(i) ← i
    i ← i + 1
until i ≥ 100
```

```text
(a)
integer A_0(1:100)
integer A_1(1:100)
integer A_2(1:100)
i_1 ← 1
repeat
    i_2 ← φ(i_1, i_3)
    A_1 ← φ(A_0, A_2)
    A_2 ← HiddenUpdate(i_2, i_2)
    i_3 ← i_2 + 1
until i_3 ≥ 100

(b)
integer A_0(1:100)
integer A_1(1:100)
integer A_2(1:100)
i_1 ← 1
repeat
    i_2 ← φ(i_1, i_3)
    A_1 ← φ(A_0, A_2)
    A_2 ← HiddenUpdate(i_2, i_2)
    i_3 ← i_2 + 1
until i_3 ≥ 100
(c)
```

Fig. 8. Source loop with array assignment (a) is equivalent to code with an Update operator that treats the array A just like a scalar (b). As Section 7.2 explains, the eventual translation out of SSA form will leave just one array here. Using HiddenUpdate (c) is a purely formal way to summarize some results of dependency analysis, if available. {#cytron-1991-ssa-fig-8 .figure tag=058A}

3.1.3 *Implicit References to Variables.* The construction of SSA form requires knowing those variables modified and used by a statement. In addition to those variables explicitly referenced, a statement may use or modify variables not mentioned by the statement itself. Examples of such *implicit* references are global variables modified or used by a procedure call, aliased variables, and dereferenced pointer variables. To obtain SSA form, we must account for implicit as well as explicit references, either by conservative assumptions or by analysis. Heap storage can be conservatively modeled by representing the entire heap as a single variable that is both modified and used by any statement that may change the heap. More refined modeling is also possible [15], but the conservative approach is already strong enough to support optimization of code that does not involve the heap but is interspersed with heap-dependent code.

For any statement $S$, three types of references affect translation into SSA form:

(1) *MustMod(S)* is the set of variables that *must* be modified by execution of $S$.
(2) *MayMod(S)* is the set of variables that *may* be modified by execution of $S$.
(3) *MayUse(S)* is the set of variables whose values prior to execution of $S$ *may* be used by $S$.

We represent implicit references for any statement $S$ by transformation to an assignment statement $A$, where all the variables in *MayMod(S)* appear in $LHS(A)$ and all the variables in $MayUse(S) \cup (MayMod(S) - MustMod(S))$ appear in $RHS(A)$.

An optimizing compiler may or may not have access to the bodies of all procedures called (directly or indirectly) or to summaries of their effects. If no specific information is available, it is customary to make conservative assumptions. A call might change any global variable or any parameter passed by reference, but it is reasonable to assume that variables local to the caller will *not* change. Such assumptions limit the extent that transformations can be performed. Techniques are available to extract more detailed information: To determine parameter aliasing and effects of procedures on global variables, see [7–9], [19], [37], and [42]; to determine pointer aliasing, see [14, 15, 27, 29, 33, 34], and [44].

When a sophisticated analysis technique is applied, the usual result is that there are few side effects and the tuples (both *LHS* and *RHS*) are small. Small tuples can be represented directly. Sophisticated analysis, however, is often unavailable. Many compilers do no interprocedural analysis at all. Consider a call to an external procedure that has not been analyzed. Both tuples for the call must contain all global variables. The compiler’s own representation of the tuples can still be compact. The representation can be a structure that includes a flag (set to indicate that all globals are in the tuple) plus a direct representation of the few local variables that are in the tuple because of parameter transmission. The intuitive explanations and theoretical analyses of optimization techniques (with or without SSA form) are conveniently formulated in terms of explicit tuples; compact representations can still be used in the implementations.

### 3.2 Overview of the SSA Algorithm {#cytron-1991-ssa-s3-2 .section tag=058B}

Translation to minimal SSA form is done in three steps:

(1) The *dominance frontier* mapping is constructed from the control flow graph (Section 4.2).
(2) Using the dominance frontiers, the locations of the $\phi$-functions for each variable in the original program are determined (Section 5.1).
(3) The variables are *renamed* (Section 5.2) by replacing each mention of an original variable $V$ by an appropriate mention of a new variable $V_t$.
