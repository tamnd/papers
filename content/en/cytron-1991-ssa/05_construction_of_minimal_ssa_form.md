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
section: "5"
section_title: CONSTRUCTION OF MINIMAL SSA FORM
tag: 059A
kind: section
lang: en
source: https://www.cs.utexas.edu/~pingali/CS380C/2010/papers/ssaCytron.pdf
pdf_sha256: 307512bb537628c2b326b23aa02109e7562bfc619509e942e015054ab58eb9ab
pdf_pages: 19-26
extraction: vision
extraction_model: gpt-5
content_sha256: 42dc6bc519d236ece29e96f2e80d71d97b4e6a662a30c729e846329c9db827e1
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

### 5.1 Using Dominance Frontiers to Find Where $\phi$-Functions Are Needed {#cytron-1991-ssa-s5-1 .section tag=059B}

The algorithm in Figure 11 inserts trivial $\phi$-functions. The outer loop of this algorithm is performed once for each variable $V$ in the program. Several data structures are used:

— $W$ is the worklist of $CFG$ nodes being processed. In each iteration of this algorithm, $W$ is initialized to the set $\mathcal{A}(V)$ of nodes that contain assignments to $V$. Each node $X$ in the worklist ensures that each node $Y$ in $DF(X)$ receives a $\phi$-function. Each iteration terminates when the worklist becomes empty.
— $Work(*)$ is an array of flags, one flag for each node, where $Work(X)$ indicates whether $X$ has ever been added to $W$ during the current iteration of the outer loop.
— $HasAlready(*)$ is an array of flags, one for each node, where $HasAlready(X)$ indicates whether a $\phi$-function for $V$ has already been inserted at $X$.

The flags $Work(X)$ and $HasAlready(X)$ are independent. We need two flags because the property of assigning to $V$ is independent of the property of needing a $\phi$-function for $V$. The flags could have been implemented with just the values true and false, but this would require additional record keeping to reset any true flags between iterations, without the expense of looping over all the nodes. It is simpler to devote an integer to each flag and to test flags by comparing them with the current iteration count.

Let each node $X$ have $A_{orig}(X)$ original assignments to variables, where each ordinary assignment statement $LHS \leftarrow RHS$ contributes the length of the tuple $LHS$ to $A_{orig}(X)$. Counting assignments to variables is one of

```text
IterCount ← 0
for each node X do
    HasAlready(X) ← 0
    Work(X) ← 0
end
W ← ∅
for each variable V do
    IterCount ← IterCount + 1
    for each X ∈ A(V) do
        Work(X) ← IterCount
        W ← W ∪ {X}
    end
while W ≠ ∅ do
    take X from W
    for each Y ∈ DF(X) do
        if HasAlready(Y) < IterCount
            then do
                place ⟨ V ← φ(V, ..., V) ⟩ at Y
                HasAlready(Y) ← IterCount
                if Work(Y) < IterCount
                    then do
                        Work(Y) ← IterCount
                        W ← W ∪ {Y}
                    end
                end
            end
        end
    end
end
```

Fig. 11. Placement of $\phi$-functions. {#cytron-1991-ssa-fig-11 .figure tag=059C}

several measures of program size.$^5$ By this measure, the program expands from size $A_{orig} = \sum_X A_{orig}(X)$ to size $A_{tot} = \sum_X A_{tot}(X)$, where each $\phi$-function placed at $X$ contributes 1 to $A_{tot}(X) = A_{orig}(X) + A_\phi(X)$. There is a similar expansion in the number of mentions of variables, from $M_{orig} = \sum_X M_{orig}(X)$ to $M_{tot} = \sum_X M_{tot}(X)$, where each $\phi$-function placed at $X$ contributes 1 plus the indegree of $X$ to $M_{tot}(X) = M_{orig}(X) + M_\phi(X)$.

Placing a $\phi$-function at $Y$ in Figure 11 has cost linear in the indegree of $Y$, so there is an $O(\sum_X M_\phi(X))$ contribution to the running time from the work done when $HasAlready(Y) < IterCount$. Replacing mentions of variables will contribute at least $O(M_{tot})$ to the running time of any SSA translation algorithm, so the cost of placement can be ignored in analyzing the contribution of Figure 11 to the $O(...)$ bound for the whole process. The $O(N)$ cost of

$^5$The various measures relevant here are reviewed when the whole SSA translation process is summarized in Section 9.1.

initialization can be similarly ignored because it is subsumed by the cost of the dominance frontier calculation. What cannot be ignored is the cost of managing the worklist W. The statement take X from W in Figure 11 is performed $A_{tot}(X)$ times, and each time incurs a cost linear in $|DF(X)|$ because all $Y \in DF(X)$ are polled. The contribution of Figure 11 to the running time of the whole process is therefore $O(\sum_X (A_{tot}(X) \times |DF(X)|))$. Sizing the output in the natural way as $A_{tot}$, we can also describe the contribution as $O(A_{tot} \times avrgDF)$, where the weighted average

$$
avrgDF \overset{\text{def}}{=} \left( \sum_X (A_{tot}(X) \times |DF(X)|) \right) / \left( \sum_X A_{tot}(X) \right)
$$

emphasizes the dominance frontiers of nodes with many assignments. As Section 8 shows, the dominance frontiers are small in practice, and Figure 11 is effectively $O(A_{tot})$. This, in turn, is effectively $O(A_{orig})$.

### 5.2 Renaming {#cytron-1991-ssa-s5-2 .section tag=059D}

The algorithm in Figure 12 renames all mentions of variables. New variables denoted $V_i$, where $i$ is an integer, are generated for each variable $V$. Figure 12 begins a top-down traversal of the dominator tree by calling SEARCH at the root node Entry. The visit to a node processes the statements associated with the node in sequential order, starting with any $\phi$-functions that may have been inserted. The processing of a statement requires work for only those variables actually mentioned in the statement. In contrast with Figure 11, we need a loop over all variables only when we initialize two arrays among the following data structures:

—$S(*)$ is an array of stacks, one stack for each variable $V$. The stacks can hold integers. The integer $i$ at the top of $S(V)$ is used to construct the variable $V_i$ that should replace a use of $V$.
—$C(*)$ is an array of integers, one for each variable $V$. The counter value $C(V)$ tells how many assignments to $V$ have been processed.
—WhichPred($X, Y$) is an integer telling which predecessor of $Y$ in $CFG$ is $X$. The $j$th operand of a $\phi$-function in $Y$ corresponds to the $j$th predecessor of $Y$ from the listing of the inedges of $Y$.
—Each assignment statement $A$ has the form

$$
LHS(A) \leftarrow RHS(A)
$$

where the right-hand side $RHS(A)$ is a tuple of expressions and the left-hand side $LHS(A)$ is a tuple of distinct target variables. These tuples change as mentions of variables are renamed, but the original target tuple is still remembered as $oldLHS(A)$. To minimize notation, a conditional branch is treated as an ordinary assignment to a special variable whose value indicates which edge the branch should follow. A real implementation would recognize that a conditional branch involves a little less work than a genuine assignment: The $LHS$ part of the processing can be omitted.

```text
for each variable V do
    C(V) ← 0
    S(V) ← EmptyStack
end
call SEARCH(Entry)
```

SEARCH($X$) :
    for each statement $A$ in $X$ do
        if $A$ is an ordinary assignment
            then
                for each variable $V$ used in $RHS(A)$ do
                    replace use of $V$ by use of $V_i$, where $i = Top(S(V))$
                end
                for each $V$ in $LHS(A)$ do
                    $i \leftarrow C(V)$
                    replace $V$ by new $V_i$ in $LHS(A)$
                    push $i$ onto $S(V)$
                    $C(V) \leftarrow i + 1$
                end
            end /* of first loop */
        for each $Y \in Succ(X)$ do
            $j \leftarrow WhichPred(Y, X)$
            for each $\phi$-function $F$ in $Y$ do
                replace the $j$-th operand $V$ in $RHS(F)$ by $V_i$ where $i = Top(S(V))$
            end
        end
        for each $Y \in Children(X)$ do
            call SEARCH(Y)
        end
    end
    for each assignment $A$ in $X$ do
        for each $V$ in $oldLHS(A)$ do
            pop $S(V)$
        end
    end
end SEARCH

Fig. 12 Renaming mentions of variables. The list of uses of $V_i$ grows with each replacement of $V$ by $V_i$ in a $RHS$

The processing of an assignment statement $A$ considers the mentions of variables in $A$. The simplest case is that of a target variable $V$ in the tuple $LHS(A)$. We need a new variable $V_i$. By keeping a count $C(V)$ of the number of assignments to $V$ that have already been processed, we can find an appropriate new variable by using $i = C(V)$ and then incrementing $C(V)$. To facilitate renaming uses of $V$ in the future, we also push $i$ (which identifies $V_i$) onto a stack $S(V)$ of (integers that identify) new variables replacing $V$.

A subtler computation is needed for the right-hand side $RHS(A)$. Consider any variable $V$ used in $RHS(A)$; that is, $V$ appears in at least one of the expressions in the tuple. We want to replace $V$ by $V_i$, where $V_i$ is the target of the assignment that produces the value for $V$ actually used in $RHS(A)$. There are two subcases because $A$ may be either an ordinary assignment or a $\phi$-function. Both subcases get $V_i$ from the top of the stack $S(V)$, but they inspect $S(V)$ at different times in Figure 12. Lemma 10, introduced later in this section, shows that $V_i$ is correctly chosen in both subcases.

The correctness proof for renaming depends on results from Section 4 and on three more lemmas. We start by showing that it makes sense to speak of "the" assignment to a variable in the transformed program.

Lemma 8. *Each new variable $V_i$ in the transformed program is a target of exactly one assignment.* {#cytron-1991-ssa-lem-8 .statement tag=059E}

Proof. Because the counter $C(V)$ is incremented after processing each assignment to $V$, there can be at most one assignment to $V_i$. To show that there is at least one assignment to $V_i$, we consider the two ways $V_i$ can be mentioned. If $V_i$ is mentioned on the LHS on an assignment, then there is nothing more to show. If the value of $V_i$ is used, on the other hand, then $i = Top(S(V))$ was true at the time when the algorithm renamed the old use of $V$ to a use of $V_i$. At the earlier time when $i$ was pushed onto $S(V)$, it was pushed because an assignment to $V$ had just been changed to an assignment to $V_i$.

A node $X$ may contain assignments to the variable $V$ that appeared in the original program or were introduced to receive the value of a $\phi$-function for $V$. Let $TopAfter(V, X)$ denote the new variable in effect for $V$ after *all* statements in node $X$ have been considered by the first loop in Figure 12. Specifically, we consider the top of each stack $S(V)$ at the end of this loop and define

$$
TopAfter(V, X) \overset{\text{def}}{=} V_i \quad \text{where} \quad i = Top(S(V)).
$$

If there are no assignments to $V$ in $X$, then the top-down traversal ensures that $TopAfter(V, X)$ is inherited from the closest dominator of $X$ that assigns to $V$.

Lemma 9. *For any variable $V$ and any CFG edge $X \to Y$ such that $Y$ does not have a $\phi$-function for $V$,* {#cytron-1991-ssa-lem-9 .statement tag=059F}

$$
TopAfter(V, X) = TopAfter(V, idom(Y)).
\tag{8}
$$
{#cytron-1991-ssa-eq-8 .equation tag=05A0}

Proof. We may assume that $X \neq idom(Y)$. Because $Y$ does not have a $\phi$-function for $V$, if a node $Z$ has $Y \in DF(Z)$, then $Z$ does not assign to a new variable derived from $V$. We use this fact twice below.

By Lemma 2, $Y \in DF_{local}(X) \subseteq DF(X)$, and, thus, $X$ does not assign to a new variable derived from $V$. Let $U$ be the first node in the sequence $idom(X), idom(idom(X)), \ldots$ that assigns to such a variable. Then

$$
TopAfter(V, X) = TopAfter(V, U).
\tag{9}
$$
{#cytron-1991-ssa-eq-9 .equation tag=05A1}

Because $U$ assigns to a new variable derived from $V$, it follows that $Y \notin DF(U)$. But $U$ dominates a predecessor of $Y$, so $U$ strictly dominates $Y$. For any $Z$ with $U \gg Z \gg idom(Y)$, we get $Z \gg X$ because $Z \gg Y$ and there is an edge $X \to Y$. By the choice of $U, U \gg Z \gg X$ implies that $Z$ does not assign to a new variable derived from $V$. Therefore,

$$
TopAfter(V, U) = TopAfter(V, idom(Y)),
$$

and (8) follows from (9).

The preceding lemma helps establish Condition (3) in the definition of SSA form, but first we must extend $TopAfter$ so as to specify which new variable corresponds to $V$ just before and just after each statement $A$. There is one iteration of the first loop in Figure 12 for $A$. We consider the top of each stack just before and just after this iteration to define

$$
TopBefore(V, A) \overset{\mathrm{def}}{=} V_i \quad \text{where} \quad i = Top(S(V)) \text{ before processing } A;
$$

$$
TopAfter(V, A) \overset{\mathrm{def}}{=} V_i \quad \text{where} \quad i = Top(S(V)) \text{ after processing } A.
$$

In particular, if $A$ happens to be the last statement in block $X$, then $TopAfter(V, A) = TopAfter(V, X)$. If, on the other hand, $A$ is followed by another statement $B$, then $TopAfter(V, A) = TopBefore(V, B)$.

Lemma 10. *Consider any control flow path in the transformed program and the same path in the original program. Consider any variable $V$ and any occurrence of a statement $A$ along the path. If $A$ is from the original program, then the value of $V$ just before executing $A$ in the original program is the same as the value of $TopBefore(V, A)$ just before executing $A$ in the transformed program.* {#cytron-1991-ssa-lem-10 .statement tag=05A2}

Proof. We use induction along the path. We consider the $k$th statement executed along the path and assume that, for all $j < k$, the $j$th statement $T$ is either not from the original program$^6$ or has each variable $V$ agreeing with $TopBefore(V, T)$ just before $T$. We assume that the $k$th statement $A$ is from the original program and show that $V$ agrees with $TopBefore(V, A)$ just before $A$.

Case 1. Suppose that $A$ is not the first original statement in its basic block $Y$. Let $T$ be the statement just before $A$ in $Y$. By the induction hypothesis and the semantics of assignment, $V$ agrees with $TopAfter(V, T)$ just after $T$. Thus, $V$ agrees with $TopBefore(V, A)$ just before $A$.

Case 2. Suppose that $A$ is the first original statement in its basic block $Y$. Let $X \to Y$ be the edge followed by the control path. We claim that $V$ agrees with $TopAfter(V, X)$ when control flows along this edge.

If $X = \mathbf{Entry}$, then $TopAfter(V, X)$ is $V_0$ and does hold the entry value of $V$. If $X \neq \mathbf{Entry}$, let $T$ be the last statement in $X$. By the induction hypothesis and the semantics of assignment, $V$ agrees with $TopAfter(V, T)$

$^6$It could be a nominal Entry assignment or a $\phi$-function.

Fig. 13. In the proof of Lemma 10, the node Y may or may not have a $\phi$-function for V. {#cytron-1991-ssa-fig-13 .figure tag=05A3}

just after T and, hence, with TopAfter(V, X) when control flows along X → Y.

We must still bridge the gap between knowing that V agrees with TopAfter(V, X) along X → Y and knowing that V agrees with TopBefore(V, A) just before doing A in Y. As Figure 13 illustrates, there may or may not be a $\phi$-function for V ahead of A in the transformed program.

Case 2.1. Suppose that V has a $\phi$-function $V_i \leftarrow \phi(\ldots)$ in Y. The $\phi$ operand corresponding to X → Y is TopAfter(V, X), thanks to the loop over successors of X in Figure 12. This is the operand whose value is assigned to $V_i$, which is TopBefore(V, A). Thus, V agrees with TopBefore(V, A) just before doing A in Y.

Case 2.2. Suppose that V does not have a $\phi$-function in Y. By Lemma 9, V agrees with TopAfter(V, X) = TopAfter(V, idom(Y)) = TopBefore(V, A) just before doing A in Y. □

Theorem 3. Any program can be put into minimal SSA form by computing the dominance frontiers and then applying the algorithms in Figure 11 and Figure 12. Let $A_{tot}$ be the total number of assignments to variables in the resulting program.\footnote{Each ordinary assignment $LHS \leftarrow RHS$ contributes the length of the tuple $LHS$ to $A_{tot}$, and each $\phi$-function contributes 1 to $A_{tot}$.} Let $M_{tot}$ be the total number of mentions of variables in the resulting program. Let E be the number of edges in CFG. Let avrgDF be the weighted average (7) of dominance frontier sizes. Then the running time of the whole process is {#cytron-1991-ssa-thm-3 .statement tag=05A4}

$$
O\left( E + \sum_X |DF(X)| + (A_{tot} \times \text{avrgDF}) + M_{tot} \right).
$$

Proof. Figure 11 places the $\phi$-functions for V at the nodes in the iterated dominance frontier $DF^+(\mathcal{S})$, where $\mathcal{S}$ is the set of assignments to V in the original program. By Theorem 2, $DF^+(\mathcal{S})$ is the set of nodes that need ϕ-functions for V, so we have obtained Condition (1) in the definition of translation to SSA form with the fewest possible ϕ-functions. We must still show that renaming is done correctly by Figure 12. Condition (2) in the definition follows from Lemma 8. Condition (3) follows from Lemma 10.

Let N be the number of nodes in CFG. The dominator tree has O(N) edges, and Figure 12 runs in $O(N + E + M_{tot})$ time. The $N + E$ term is subsumed by the $O(E + \sum_X |DF(X)|)$ cost of computing the dominance frontiers, so Figure 12 contributes $O(M_{tot})$. As explained at the end of Section 5.1, Figure 11 contributes $O(A_{tot} \times avgDF)$.
