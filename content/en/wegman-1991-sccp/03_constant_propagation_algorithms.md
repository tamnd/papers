---
paper: wegman-1991-sccp
title: Constant Propagation with Conditional Branches
authors:
  - Mark N. Wegman
  - F. Kenneth Zadeck
year: 1991
venue: ACM TOPLAS
field: languages
section: "3"
section_title: CONSTANT PROPAGATION ALGORITHMS
tag: 05BD
kind: section
lang: en
source: https://www.cs.utexas.edu/users/lin/cs380c/wegman.pdf
pdf_sha256: 40929436cdf1c477f2318221df5d0aa71488db4a01cc448b184e0aba8bf95ddb
pdf_pages: 5-14
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 8bd50f3928242dd5f69dacecbb540f998e0e4a882cdf0152c41c40751919ac70
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

In this section we present four algorithms for determining constants. They are described in order of increasing power; each algorithm finds at least the constants found by the previous algorithm. These algorithms are among the simplest, fastest, and most powerful global constant propagation algorithms known. The first three algorithms are reformulations of the work of others;

the fourth is new and contains the best features of each of the previous three. Figure 5 shows the relationship among the four algorithms.

The first algorithm, *Simple Constant* (SC), was developed by Kildall [26] and is presented in Section 3.1. Kildall was among the first to describe the constant propagation problem and to give an algorithmic solution.

The second algorithm, *Sparse Simple Constant* (SSC), is an easily understood reformulation of an algorithm developed by Reif and Lewis [32] and is presented in Section 3.2. This algorithm uses a recently developed data structure called the *static single assignment* graph (SSA graph) [[cytron-1991-ssa]]. The SSA graph is a variant of the global value graph of Reif and Lewis [32], which in turn is based on the *p-graph* of Shapiro and Saint [40]. The SSA graph allows this algorithm to find a class of constants equivalent to those of SC, yet the algorithm is faster than SC by a factor proportional to the number of variables in the program. Indeed, the speedup can be proportional to the product of the number of variables in the program and the number of edges in the program flow graph. It is unfortunate that this algorithm was not recognized for many years, since it works in time linear in the size of the SSA graph.

The third algorithm, *Conditional Constant* (CC), is a variant of Wegbreit's Algorithm 3.1 [42] and is presented in Section 3.3. CC discovers all constants that can be found by evaluating all conditional branches with all constant operands, but it uses the same input data structures and is asymptotically as slow as SC. The attraction of CC is that it propagates the values in such a way that when conditional branches are found to have a constant conditional expression, the search for constants can ignore parts of the program that are never executed. The algorithm does unreachable code elimination in combination with constant propagation. The first benefit of this approach is that the algorithm may run faster than SC, since it need not evaluate the sections of the program that are never executed. A second benefit is that values created in the unreachable areas cannot possibly kill potential constants, and thus CC can find more constants than can SC.

The fourth algorithm, *Sparse Conditional Constant* (SCC), is new and is presented in Section 3.4. SCC finds the same class of constants as CC, yet has the same speedup over CC as SSC has over SC.

### 3.1 Simple Constant {#wegman-1991-sccp-s3-1 .section tag=05BE}

Kildall’s *Simple Constant* (SC) algorithm [26] uses the program flow graph for propagation of values. At each node in the program, two LatticeCells are associated with the value of every variable in the program, one with the value at entry to the node and the other with the exit. The process of visiting a node involves examination of every LatticeCell at that node. Initially the start node is placed on the worklist. A node is chosen from the worklist, removed from the worklist, and examined. The lattice value stored at the entry to the examined node becomes the meet of values at the exits of preceding nodes. The statement is evaluated on the basis of the new entering values. This may cause the value of a variable that it is assigned to in the node to differ from the value associated with the variable at the exit LatticeCell. In that case all nodes following the examined node must be examined, and they are added to the worklist. If no exit LatticeCells change, then no nodes are added to the worklist. The process repeats until the worklist is empty.

SC finds those constants that Kildall calls *simple constants*. Simple constants are all values that can be proved to be constant subject to two constraints: no information is assumed about which direction branches will take, and only one value for each variable is maintained along each path in the program.

Since the lattice value of each variable can only be lowered twice, each node may be visited at most $2 \times V \times I$ times, where $I$ is the number of in-edges into that node. Thus, the time required for Kildall’s algorithm is $O(E \times V)$ node visits and $V$ operations during each node visit. This results in a worst-case running time of $O(E \times V^2)$. The best-case running time may be $O(E \times V)$. It is our intuition that the worst case is rarely achieved. The space required is $O(N \times V)$.

We have described the problem in somewhat different terms from Kildall. In Kildall’s lattice, each lattice element corresponds to the state of all variables in the program. In our lattice, each state corresponds to the state of a single variable. By using our representation and a technique described in Section 5.4, it is possible to lower the time bound to $O(E \times V)$ changes to variable values, which is the best one can hope to get out of an approach like this. These optimizations are not obvious in the context presented by Kildall.

We have initialized the worklist with only the start node, where Kildall started with all of the nodes on the worklist. This is consistent with and required for the other algorithms presented in this paper, but does not affect SC in any significant way.

When SC visits a node, it applies a function that takes as input the value of all variables at the entrance of the node and produces the set of values for all variables at the exit of the node. In the next section we reformulate that notion in order to model more closely what Reif and Lewis [32, 33] did and what we do. This reformulation of SC allows the SSC algorithm to run faster than SC, but produces the same information as SC.

### 3.2 Sparse Simple Constant {#wegman-1991-sccp-s3-2 .section tag=05BF}

Reif's and Lewis's *Sparse Simple Constant* (SSC) algorithm [32, 33] finds all simple constants. It achieves a speedup over SC by using a sparse representation (in the presentation here, the SSA graph) to propagate the values through the program. The class of constants found is unchanged.

3.2.1 *The Static Single Assignment Graph.* In SSA form, the program is transformed so that only one assignment can reach each use. For straight-line programs, the transformation to SSA form is straightforward. Each assignment to a variable is given a unique name (shown as a subscript in Figure 6) and all of the uses reached by that assignment are renamed to match the assignment's new name. More complicated programs have branch and join nodes. At the join nodes, we must add a special form of assignment called a *φ-function*. A *φ*-function at the entrance to a node *X* has the form *V* ← *φ*(R, S, ...), where *V*, *R*, *S*, ... are variables. The number of operands *R*, *S*, ... is the number of control flow predecessors of *X*. The predecessors of *X* are listed in some arbitrary fixed order, and the *j*th operand of *φ* is associated with the *j*th predecessor. If control reaches *X* from its *j*th predecessor, then *V* is assigned the value of the *j*th operand. Each execution of a *φ*-function uses only one of the operands, but which one depends on the flow of control just before entering *X*. Any *φ*-functions at *X* are executed before the ordinary statements in the node that contributes *X* to the program flow graph. Figure 7 shows the use of *φ*-functions in SSA form and Figure 8 gives the SSA form of a simple program with loops.

In general, two separate steps are required to translate a program into SSA form. In the first step, some trivial *φ*-functions *V* ← *φ*(V, V, ...) are inserted at some of the join nodes in the program flow graph. In the second step, new variables *V*$_{i}$ (for *i* = 0, 1, 2, ...) are generated to serve as new names for each variable *V*. Each mention of *V* in the program is replaced by a mention of one of the new names *V*$_{i}$. (A *mention* may be on either side of an assignment statement and may be in an ordinary assignment or in a *φ*-function.) A program is defined to be *in SSA form* if, for every original variable *V*, trivial *φ*-functions for *V* have been inserted and each mention of *V* has been changed to a mention of a new name *V*$_{i}$ such that the following conditions hold:

(1) If a program flow graph node *Z* is the first node common to two nonnull paths *X* → *Z* and *Y* → *Z* that start at nodes *X* and *Y* containing assignments to *V*, then a *φ*-function for *V* has been inserted at *Z*.
(2) Each new name *V*$_{i}$ for *V* is the target of exactly one assignment statement in the program text.
(3) Along any program flow path, consider any use of a new name *V*$_{i}$ for *V* (in the transformed program) and the corresponding use of *V* (in the original program). Then *V* and *V*$_{i}$ have the same value.

```text
v ← 1
... ← v + 1
v ← 2
... ← v + 2

v₁ ← 1
... ← v₁ + 1
v₂ ← 2
... ← v₂ + 2
```

Fig. 6. Straight-line code and its single assignment version. {#wegman-1991-sccp-fig-6 .figure tag=05C0}

Fig. 7. An if–then–else and its single assignment version. {#wegman-1991-sccp-fig-7 .figure tag=05C1}

```text
if P
    then v ← 1
    else v ← 2
    ... ← v + 2

if P
    then v₁ ← 1
    else v₂ ← 2
    v₃ ← φ(v₁, v₂)
    ... ← v₃ + 2
```

Fig. 8. A simple program and its single assignment version. {#wegman-1991-sccp-fig-8 .figure tag=05C2}

```text
i₁ ← 1
j₁ ← 1
k₁ ← 1
while (P)
    J₂ ← φ(j₄, j₁)
    k₂ ← φ(k₅, k₁)
    if (Q)
        then do
            j ← i
            k ← k + 1
        end
    else k ← k + 2
end

j₃ ← i₁
k₃ ← k₂ + 1
if (Q)
    then do
        j₄ ← φ(j₃, j₂)
        k₅ ← φ(k₃, k₄)
    end
else k₄ ← k₂ + 2
```

Once a program is in SSA form, we add connections called SSA edges. Each connection goes from the unique point where a variable is given a value to a use of that variable. SSA edges are essentially def-use chains [1] in the SSA program.

A program is in minimal SSA form if it is in SSA form and if the number of φ-functions inserted is as small as possible, subject to Condition 1 above. The optimizations that depend on SSA form are still valid if there are some extraneous φ-functions beyond those that would appear in minimal SSA form. However, extraneous φ-functions sometimes inhibit other optimizations by concealing useful facts [5], and they always add unnecessary overhead to the optimization process itself. Thus it is important to place φ-functions only where they are required.

For any variable V, the program flow graph nodes at which we should insert φ-functions in the original program can be defined recursively by Condition 1 in the definition of SSA form. A node Z needs a φ-function for V if Z is the first node that two nonnull program flow paths have in common, when those two paths originate at two different nodes containing assignments to V or needing φ-functions for V. Nonrecursively, we may observe that a node Z needs a φ-function for V because Z is the first node common to two nonnull paths X ⇝ Z and Y ⇝ Z that start at nodes X and Y containing assignments to V. If Z does not already contain an assignment to V, then the $\phi$-function inserted at Z adds Z to the set of nodes that contain assignments to V. With more nodes to consider as origins of paths, we may observe that more nodes appear as the first node common to two nonnull paths originating at nodes with assignments to V. The set of nodes observed to need $\phi$-functions thus gradually increases until it stabilizes. When $\phi$-functions are placed in this way, minimal SSA form can be obtained by an easy adaptation of well-known def-use chaining. The algorithm presented in [[cytron-1991-ssa]] obtains the same end results as this brute-force approach, but it places the $\phi$-functions and performs the renaming in much less time than brute force would require.

Minimal SSA form is a refinement of Shapiro’s and Saint’s [40] notion of a pseudo-assignment. The *pseudo-assignment nodes* for V are exactly the nodes that need $\phi$-functions for V. For a program flow graph with E edges describing a program with V variables, one algorithm [34] requires $O(E\alpha(E))$ bit vector operations (where each vector is of length V) to find all the pseudo-assignments. A simpler algorithm [38] for reducible programs computes SSA form in time $O(E \times V)$. Both of these algorithms are effectively quadratic, and the algorithm in [38] sometimes uses extraneous $\phi$-functions. The method presented in [[cytron-1991-ssa]] is effectively linear in the size of the program although there are cases where it behaves nonlinearly.

3.2.2 *The Algorithm.* SSC works as follows:3

(1) Examine all expressions. If it is not possible that the value of an expression will be evaluated at compile time (for example, a read statement), then the corresponding LatticeCell is assigned $\bot$. If no variables appear in the expression, then the expression is evaluated and the LatticeCell is assigned an appropriate $c_v$. All other LatticeCells are assigned $\top$.
A worklist is initialized to contain all SSA edges where the definition is from an expression that has a LatticeCell that is not $\top$.

(2) The algorithm terminates when the worklist becomes empty.

(3) An SSA edge is taken off the worklist. We form the meet of the value of the LatticeCell at the definition end of the SSA edge and the value of the LatticeCell at the use end of the SSA edge. The meet is performed under the rules given in Section 2.2.

(4) If the meet of the values is different from the value at the use end, then the use end is replaced by the meet. The new value is used to recompute the value of the expression in which the previous value had been used, again according to the expression rules in Section 2.2. If the new value for the expression is lower than the value stored for the expression, then all SSA edges with their source at this node are added to the worklist.

3SSC as originally presented used a global value graph as its sparse representation; here we use the SSA graph, which is a variant. These two representations produce equivalent results when used with this algorithm.

3.2.3 Asymptotic Complexity. The time complexity of this algorithm is proportional to the size of the SSA graph. The SSC algorithm requires that each SSA edge be examined at least once and at most twice. The examinations occur when the value of its definition site is lowered to either $\mathcal{C}$ or $\perp$. In theory the size can be $O(E \times V)$, but empirical evidence indicates that the work required to compute the SSA graph is linear in the program size [[cytron-1991-ssa]]. Thus, we expect our algorithm to be linear in practice.

### 3.3 Conditional Constant {#wegman-1991-sccp-s3-3 .section tag=05C3}

Wegbreit’s Algorithm 3.1 [42] is a general algorithm for performing global flow analysis that takes conditional branches into account. In this section, we specialize Wegbreit’s general algorithm to perform constant propagation and call the result Conditional Constant (CC). CC is more powerful than SC because, whenever CC can assume that a conditional expression is always constant, it assumes that the branch it guards goes in only one direction.

Consider the example in Figure 9. Neither SC nor SSC is capable of discovering that $j = 1$ since they make no assumptions about the possible branch directions. Since $i$ is always 1, however, the condition always takes the true branch and $j$ is always equal to 1. Such code may be the result of procedure integration or abstract data type compilation.

To exploit this knowledge about conditional branches, we do not propagate values along all program flow graph edges, as in SC. Rather, CC defers the evaluation of any program flow graph edge until it is marked as executable. Each program flow graph edge is initially marked as not executable. Program flow graph edges are marked executable by symbolically executing the program, beginning with the start node. Whenever an assignment node is executed, the out-edge in the program flow graph leaving that node is marked as executable and added to the worklist. Whenever a conditional node is executed, the expression controlling the conditional is evaluated and we determine which branch(es) may be taken. If the expression evaluates to $\perp$, then all branches may be taken. The edges corresponding to these branches are added to the worklist. If the expression evaluates to $\mathcal{C}$, only one branch can be taken, and the associated edge is added to the worklist.

This algorithm is able to ignore any definition that reaches a use via a program flow graph edge that is never executed. Thus, this algorithm accomplishes a form of dead code elimination called unreachable code elimination.$^4$

This algorithm has the same asymptotic running time as SC, $O(E \times V^2)$ in the worst case in which no branches are found to be constant. This algorithm is expected to have better average-case complexity, however, since it can ignore parts of the program that will never be executed and since SC should behave better than $O(E \times V^2)$.

$^4$ Two classical techniques are called dead code elimination. The goal of the first, unreachable code elimination, is to eliminate code that can never be executed. The goal of the other, unused code elimination, is to delete sections of code whose results are never used (see Allen and Cocke [2]). Each of these techniques finds a different class of dead code, and neither subsumes the other.

$$
\begin{aligned}
& l \leftarrow 1 \\
& \ldots \\
& \text{if } l = 1 \\
& \quad \text{then } j \leftarrow 1 \\
& \quad \text{else } j \leftarrow 2
\end{aligned}
$$

Fig. 9. A conditional constant definition. {#wegman-1991-sccp-fig-9 .figure tag=05C4}

Many optimizing compilers repeatedly execute constant propagation and unreachable code elimination since each provides information that improves the other. CC solves this problem in an elegant way by combining the two optimizations. Additionally, the algorithm gets better results than are possible by repeated applications of the separate algorithms, as described in Section 5.1.

### 3.4 Sparse Conditional Constant {#wegman-1991-sccp-s3-4 .section tag=05C5}

We wish to derive a version of CC that also improves running time, just as SSC was derived from SC to improve running time. In order to do this, we must utilize some of the special properties of the SSA graph. We call this algorithm *Sparse Conditional Constant* or SCC.

When the SSA graph was constructed, $\phi$-functions were inserted at some join nodes. The meaning of a $\phi$-function is that if control reaches the node in the program flow graph along its *ith* in-edge, the result of the $\phi$-function is the value of its *ith* operand.

In the SSC algorithm, when the meet rule was applied to a $\phi$-function, the meet operator was applied to all of the operands of the $\phi$-function. In the SCC algorithm, the meet operator is applied only to those operands of the $\phi$-function that correspond to the program flow graph edges marked executable. Those that are not executable effectively have the value of $\top$.

This algorithm uses two worklists: *FlowWorkList* is a worklist of program flow graph edges and *SSAWorkList* is a worklist of SSA edges.

SCC works as follows:

(1) Initialize the FlowWorkList to contain the edges exiting the start node of the program. The SSAWorkList is initially empty.

Each program flow graph edge has an associated flag, the *ExecutableFlag*, that controls the evaluation of $\phi$-functions in the destination node of that edge. This flag is initially false for all edges.

Each LatticeCell is initially $\top$.

(2) Halt execution when both worklists become empty. Execution may proceed by processing items from either worklist.

(3) If the item is a program flow graph edge from the FlowWorkList, then examine the ExecutableFlag of that edge. If the ExecutableFlag is true do nothing; otherwise:
(a) Mark the ExecutableFlag of the edge as true.
(b) Perform Visit-$\phi$ for all of the $\phi$-functions at the destination node.
(c) If only one of the ExecutableFlags associated with the incoming program flow graph edges is true (i.e., if this is the first time this node has been evaluated), then perform VisitExpression for the expression in this node.
(d) If the node only contains one outgoing flow graph edge, add that edge to the FlowWorkList.
(4) If the item is an SSA edge from the SSAWorkList and the destination of that edge is a $\phi$-function, perform Visit-$\phi$.
(5) If the item is an SSA edge from the SSAWorkList and the destination of that edge is an expression, then examine ExecutableFlags for the program flow edges reaching that node. If any of them are true, perform VisitExpression. Otherwise do nothing.

The value of the LatticeCell associated with the output of a $\phi$-function is defined to be the meet of all arguments whose corresponding in-edge has been marked executable. It is computed by Visit-$\phi$. Visit-$\phi$ is called whenever the value of the LatticeCell associated with one of its operands is lowered or when the ExecutableFlag associated with one of the in-edges becomes true.

Visit-$\phi$ *is defined as follows*: The LatticeCells for each operand of the $\phi$-function are defined on the basis of the ExecutableFlag for the corresponding program flow edge.

executable   The LatticeCell has the same value as the LatticeCell at the definition end of the SSA edge.
not-executable   The LatticeCell has the value $\top$.

*VisitExpression is defined as follows*: Evaluate the expression obtaining the values of the operands from the LatticeCells where they are defined and using the expression rules defined in Section 2.2. If this changes the value of the LatticeCell of the output of the expression, do the following:

(1) If the expression is part of an assignment node, add to the SSAWorkList all SSA edges starting at the definition for that node.
(2) If the expression controls a conditional branch, some outgoing flow graph edges must be added to the FlowWorkList. If the LatticeCell has value $\bot$, all exit edges must be added to the FlowWorkList. If the value is $\mathcal{C}$, only the flow graph edge executed as the result of the branch is added to the FlowWorkList.$^5$

3.4.1 *Asymptotic Complexity.* As in SSC, each SSA edge can only be examined twice. Nodes in the program flow graph are visited once for each of their in-edges. The asymptotic running complexity of this algorithm is the number of edges in the flow graph plus the number of SSA edges and should be linear in practice.

CC may be impractically slow and, consequently, was ignored for a long time. Many workers in code optimization had tried to derive practical sparse algorithms that achieved CC’s results. However, they started from the sparse

$^5$ The value cannot be $\top$, since the earlier step in VisitExpression will have lowered the value.

representation then prevailing, def-use chains without SSA form. Def-use chains without SSA form do not determine the best information, as described in Section 5.2.
