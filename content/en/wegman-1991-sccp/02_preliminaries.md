---
paper: wegman-1991-sccp
title: Constant Propagation with Conditional Branches
authors:
  - Mark N. Wegman
  - F. Kenneth Zadeck
year: 1991
venue: ACM TOPLAS
field: languages
section: "2"
section_title: PRELIMINARIES
tag: "0425"
kind: section
lang: en
source: https://www.cs.utexas.edu/users/lin/cs380c/wegman.pdf
pdf_sha256: 40929436cdf1c477f2318221df5d0aa71488db4a01cc448b184e0aba8bf95ddb
pdf_pages: 2-5
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 444ec46236c0093f91818f78d7c602e135d4cad47f8beb367851f8e92edf3f6c
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

In this section we introduce the mathematical notation used to represent programs and values.

### 2.1 Graph Definitions {#wegman-1991-sccp-s2-1 .section tag=0426}

Since an algorithm's performance is usually specified in terms of the size of its input, it is necessary to define some common measures of program size:

$N$ is the number of assignment statements plus the number of expressions whose value is branched on in the program. For notational convenience, each node in the program flow graph contains one expression. This number also closely approximates the number of definition sites in the program since most statements assign a value.
$E$ is the number of edges in the program flow graph. A reasonable approximation for $E$ is twice $N$, since conditional statements typically have only two successors.$^1$
$V$ is the number of variables in the program.

We say that a program consist of three types of nodes: *conditional nodes*, *assignment nodes*, and a unique *start node*.$^2$ Conditional nodes are potential deviations in control flow through a program. An expression is evaluated at a conditional node and control is subsequently transferred to another node; for simplicity, assume that such expressions have no side effects. Assignment nodes are sites at which variables are defined in terms of other variables and constants; for simplicity, assume that only scalar (i.e., nonsubscripted) variables participate in assignment nodes (see Section 7). In procedures with multiple entry points, the start node has out-edges to any entry node of the procedure.

### 2.2 The Lattice for Constant Propagation {#wegman-1991-sccp-s2-2 .section tag=0427}

The output of a constant propagation algorithm is an *output assignment* of lattice values to variables at each node in the program. Let all variables defined or used within a given assignment or conditional node be characterized by a *lattice element* that represents compile-time knowledge about the value of such variables during execution of the algorithm. As depicted in Figure 1, the lattice element can be one of three types: the highest element is *top*, $\top$, the lowest is *bottom*, $\bot$, and all elements in the middle are *constant*, $c_i$. There is an infinite number of $c_i$ lattice elements, each corresponding to a different constant $i$. In the lattice-theoretic sense, no constant is higher or lower than any other. Each node of the program has cells, called *LatticeCells*, to hold the lattice elements; the values stored in these elements change as the algorithm progresses. The LatticeCells are associated with the results and operands of the expressions; the details of the association depend on the particular algorithm.

\footnotetext{
$^1$ This has been experimentally verified by Pratt [31] and Allen [4], and is true because most structured programming constructs give rise to programs with binary branches. One common exception is the computed goto statement in Fortran, which can give rise to graphs with up to $N^2$ edges if the targets of the goto's are all of the other statements in the program; such programs are very rare.
$^2$ It is possible that the start node could have a branch to every other statement in the program, giving rise to a program in which the number of edges was three times the number of nodes. Such a program would, however, be extremely rare.
}

Fig. 1. The three-level lattice. {#wegman-1991-sccp-fig-1 .figure tag=05B9}

Fig. 2. Rules for $\sqcap$. {#wegman-1991-sccp-fig-2 .figure tag=05BA}

$$
\begin{align*}
\text{any} \sqcap \top &= \text{any} \\
\text{any} \sqcap \bot &= \bot \\
\mathcal{C}_i \sqcap \mathcal{C}_j &= \mathcal{C}_i \text{ if } i = j \\
\mathcal{C}_i \sqcap \mathcal{C}_j &= \bot \text{ if } i \neq j
\end{align*}
$$

At the end of constant propagation, assigning a constant $\mathcal{C}$ to a LatticeCell means that on all possible executions of the program, the associated result or operand always has the same value when that node is exited. Assigning $\bot$ means that a constant value cannot be guaranteed and assigning $\top$ means that the variable may be some (as yet) undetermined constant. Upon termination of a constant propagation algorithm, all LatticeCells are either $\mathcal{C}$ or $\bot$ at executable nodes.

The algorithms start with the optimistic assignment of $\top$ to the LatticeCell of all operands of expressions at all nodes except the start node. If the variable has an explicit initializer or if the language specifies an implicit initializer (e.g., in LISP, all cells are initialized to nil), then that value is used at the start node. The algorithms may obtain better information if $\top$, rather than $\bot$, is assigned to the values of uninitialized variables at the entry of the program. In languages in which the use of an uninitialized variable is allowed but undefined (as in FORTRAN), the use of $\top$ may make the analysis yield an incorrect result. Thus, each uninitialized variable must be assigned $\bot$. On the other hand, if the language forbids such uses, the uninitialized variables may be assigned $\top$.

The algorithms proceed by lowering (in the lattice-theoretic sense) the LatticeCells of the operands and results at each node as more information is discovered, a process that continues until a fixed point is achieved. The additional information is inserted by applying the meet ($\sqcap$) rules shown in Figure 2, where each of the operand values at a node corresponds to the conditions prior to the execution of the statement. These rules ensure that the value at the join point is no higher than the value entering from any of the predecessors.

any $\vee$ true = true
any $\wedge$ false = false

Fig. 3. Special rules for $\wedge$ and $\vee$. {#wegman-1991-sccp-fig-3 .figure tag=05BB}

```text
j ← 5
if i = j then i ← i + 1
```

Fig. 4. A conditional branch where information about i can be derived. {#wegman-1991-sccp-fig-4 .figure tag=05BC}

If a variable is not the target of an assignment statement in a node, its value is unchanged by the node. If the node is an assignment statement, the value of the result and the value of operands of other nodes may change and are reevaluated according to the *expression evaluation rules*: the value of the operands of an expression corresponds to the value of the variables at the entrance to the node, and the result corresponds to the value of variables that change during the execution of the node.

Usually, if the node is an assignment and any of the variables used in its expression portion has a value of $\perp$, the value exiting the assignment statement for that variable is $\perp$. If all values used in its expression portion are constant, the value of the assigned variable is the value of the expression when evaluated with those constant values. Otherwise the value assigned is $\perp$.

For certain operators, however, we can give special expression rules that yield better information. For example, if the operator is an $\vee$ and one of the operands is known to be true, then the value of the expression is true whether or not the other operand is $\perp$. These rules are given in Figure 3.

Information can sometimes be derived from the equality tests that control conditional branches [2]. On entrance to the then branch in Figure 4, the value of i is 5. We can modify the program so that we can derive this information by inserting extra nodes containing assignments between the conditional and the entrance to the then branch. The variable i is assigned the join of the LatticeCells of i and j (a similar assignment to j is also added). These are not assignment statements in the ordinary sense, because they are not used to cause changes in the program’s state and need not be executed; rather, they are used to model changes in the assertions about the program state and, thus, are in the intermediate code.

In the algorithms below, the changes in the LatticeCells associated with the operands may require an expression to be reevaluated many times. In Section 5.4, we show how to do all of the reevaluations of a given expression in time proportional to the size of the expression.
