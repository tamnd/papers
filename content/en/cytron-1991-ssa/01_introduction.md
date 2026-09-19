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
section: "1"
section_title: INTRODUCTION
tag: "0582"
kind: section
lang: en
source: https://www.cs.utexas.edu/~pingali/CS380C/2010/papers/ssaCytron.pdf
pdf_sha256: 307512bb537628c2b326b23aa02109e7562bfc619509e942e015054ab58eb9ab
pdf_pages: 2-5
extraction: vision
extraction_model: gpt-5
content_sha256: ce3b89fb9d432a1738d3b2120afad57c098c3eda441d2bcce5d44aca1a7d2367
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

In optimizing compilers, data structure choices directly influence the power and efficiency of practical program optimization. A poor choice of data structure can inhibit optimization or slow compilation to the point where advanced optimization features become undesirable. Recently, static single assignment (SSA) form [5, 43] and the control dependence graph [24] have been proposed to represent data flow and control flow properties of programs. Each of these previously unrelated techniques lends efficiency and power to a useful class of program optimizations. Although both of these structures are attractive, the difficulty of their construction and their potential size have discouraged their use [4]. We present new algorithms that efficiently compute these data structures for arbitrary control flow graphs. The algorithms use dominance frontiers, a new concept that may have other applications. We also give analytical and experimental evidence that the sum of the sizes of all the dominance frontiers is usually linear in the size of the original program. This paper thus presents strong evidence that SSA form and control dependences can be of practical use in optimization.

Figure 1 illustrates the role of SSA form in a compiler. The intermediate code is put into SSA form, optimized in various ways, and then translated back out of SSA form. Optimizations that can benefit from using SSA form include code motion [22] and elimination of partial redundancies [43], as well as the constant propagation discussed later in this section.

Variants of SSA form have been used for detecting program equivalence [5, 52] and for increasing parallelism in imperative programs [21]. The representation of simple data flow information (def-use chains) may be made more compact through SSA form. If a variable has $D$ definitions and $U$ uses, then there can be $D \times U$ def-use chains. When similar information is encoded in SSA form, there can be at most $E$ def-use chains, where $E$ is the number of edges in the control flow graph [40]. Moreover, the def-use information encoded in SSA form can be updated easily when optimizations are applied. This is important for a constant propagation algorithm that deletes branches to code proven at compile time to be unexecutable [50]. Specifically, the def-use information is just a list, for each variable, of the places in the program text that use that variable. Every use of V is indeed a use of the value provided by the (unique) assignment to V.

To see the intuition behind SSA form, it is helpful to begin with straight-line code. Each assignment to a variable is given a unique name (shown as a subscript in Figure 2), and all of the uses reached by that assignment are renamed to match the assignment’s new name.

Most programs, however, have branch and join nodes. At the join nodes, we add a special form of assignment called a $\phi$-function. In Figure 3, the

Original Intermediate Code
↓
$P_0 \rightarrow P_1 \rightarrow P_2 \rightarrow \ldots P_n$
Optimized Intermediate Code
↑

Fig. 1. Vertical arrows represent translation to/from static single assignment form. Horizontal arrows represent optimizations. {#cytron-1991-ssa-fig-1 .figure tag=0421}

$$
V \leftarrow 4 \\
\leftarrow V + 5 \\
V \leftarrow 6 \\
\leftarrow V + 7
$$

$$
V_1 \leftarrow 4 \\
\leftarrow V_1 + 5 \\
V_2 \leftarrow 6 \\
\leftarrow V_2 + 7
$$

Fig. 2. Straight-line code and its single assignment version. {#cytron-1991-ssa-fig-2 .figure tag=0422}

```text
if P
then V ← 4
else V ← 6
```

/* Use V several times. */

```text
if P
then V₁ ← 4
else V₂ ← 6
```

$V_3 \leftarrow \phi(V_1, V_2)$
/* Use V_3 several times. */

Fig. 3. if-then-else and its single assignment version. {#cytron-1991-ssa-fig-3 .figure tag=0423}

operands to the $\phi$-function indicate which assignments to $V$ reach the join point. Subsequent uses of $V$ become uses of $V_3$. The old variable $V$ is thus replaced by new variables $V_1, V_2, V_3, \ldots$, and each use of $V_i$ is reached by just one assignment to $V_i$. Indeed, there is only one assignment to $V_i$ in the entire program. This simplifies the record keeping for several optimizations. An especially clear example is constant propagation based on SSA form [50]; the next subsection sketches this application.

### 1.1 Constant Propagation {#cytron-1991-ssa-s1-1 .section tag=0583}

Figure 4 is a more elaborate version of Figure 3. The else branch includes a test of $Q$, and propagating the constant true to this use of $Q$ tells a compiler that the else branch never falls through to the join point. If $Q$ is the constant true, then all uses of $V$ after the join point are really uses of the constant 4. Such possibilities can be taken into account without SSA form, but the processing is either costly [48] or difficult to understand [49]. With SSA form, the algorithm is fast and simple.

Initially, the algorithm assumes that each edge is *unexecutable* (i.e., never followed at run time) and that each variable is constant with an as-yet unknown value (denoted $T$). Worklists are initialized appropriately, and the assumptions are corrected until they stabilize. Suppose the algorithm finds that variable $P$ is *not* constant (denoted $\perp$) and, hence, that either branch of

```text
if P
then do V ← 4
    end
else do V ← 6
    if Q then return
end
```

... ← V + 5

```text
if P
then do V₁ ← 4
    end
else do V₂ ← 6
    if Q then return
end
V₃ ← φ(V₁, V₂)
... ← V₃ + 5
```

Fig 4. Example of constant propagation.

the outer conditional may be taken. The outedges of the test of P are marked executable, and the statements they reach are processed. When V₁ ← 4 is processed, the assumption about V₁ is changed from T to 4, and all uses of V₁ are notified that they are uses of 4. (Each use of V₁ is indeed a use of this value, thanks to the single assignment property.) In particular, the φ-function combines 4 with V₂. The second operand of the φ-function, however, is associated with the inedge of the join point that corresponds to falling through the else branch. So long as this edge is considered unexecutable, the algorithm uses T for the second operand, no matter what is currently assumed about V₂. Combining 4 with T yields 4, so uses of V₃ are still tentatively assumed to be uses of 4. Eventually, the assumption about Q may change from T to a known constant or to ⊥. A change to either false or ⊥ would lead to the discovery that the second inedge of the join point can be followed, and then the 6 at V₂ combines with the 4 at V₁ to yield ⊥ at V₃. A change to true would have no effect on the assumption at V₃. Traditional constant propagation algorithms, on the other hand, would see that assignments of two different constants to V seem to “reach” all uses after the join point. They would thus decide that V is not constant at these uses.

The algorithm just sketched is linear in the size of the SSA program it sees [50], but this size might be nonlinear in the size of the original program. In particular, it would be safe but inefficient to place a φ-function for every variable at every join point. This paper shows how to obtain SSA form efficiently. When φ-functions are placed carefully, nonlinear behavior is still possible but is unlikely in practice. The size of the SSA program is typically linear in the size of the original program; the time to do the work is essentially linear in the SSA size.

### 1.2 Where to Place φ-Functions {#cytron-1991-ssa-s1-2 .section tag=0584}

At first glance, careful placement might seem to require the enumeration of pairs of assignment statements for each variable. Checking whether there are two assignments to V that reach a common point might seem to be intrinsically nonlinear. In fact, however, it is enough to look at the dominance frontier of each node in the control flow graph. Leaving the technicalities to later sections, we sketch the method here.

Suppose that a variable V has just one assignment in the original program, so that any use of V will be either a use of the value V₀ at entry to the program or a use of the value V₁ from the most recent execution of the assignment to V. Let X be the basic block of code that assigns to V, so X will determine the value of V when control flows along any edge X → Y to a basic block Y. When entered along X → Y, the code in Y will see V₁ and be unaffected by V₀. If Y ≠ X, but all paths to Y must still go through X (in which case X is said to strictly dominate Y), then the code in Y will always see V₁. Indeed, any node strictly dominated by X will always see V₁, no matter how far from X it may be. Eventually, however, control may be able to reach a node Z not strictly dominated by X. Suppose Z is the first such node on a path, so that Z sees V₁ along one inedge but may see V₀ along another inedge. Then Z is said to be in the dominance frontier of X and is clearly in need of a φ-function for V. In general, no matter how many assignments to V may appear in the original program and no matter how complex the control flow may be, we can place φ-functions for V by finding the dominance frontier of every node that assigns to V, then the dominance frontier of every node where a φ-function has already been placed, and so on.

The same concept of dominance frontiers used for computing SSA form can also be used to compute control dependences [20, 24], which identify those conditions affecting statement execution. Informally, a statement is control dependent on a branch if one edge from the branch definitely causes that statement to execute while another edge can cause the statement to be skipped. Such information is vital for detection of parallelism [2], program optimization, and program analysis [28].

### 1.3 Outline of the Rest of the Paper {#cytron-1991-ssa-s1-3 .section tag=0585}

Section 2 reviews the representation of control flow by a directed graph. Section 3 explains SSA form and sketches how to construct it. This section also considers variants of SSA form as defined here. Our algorithm can be adjusted to deal with these variants. Section 4 reviews the dominator tree concept and formalizes dominance frontiers. Then we show how to compute SSA form (Section 5) and the control dependence graph (Section 6) efficiently. Section 7 explains how to translate out of SSA form. Section 8 shows that our algorithms are linear in the size of programs restricted to certain control structures. We also give evidence of general linear behavior by reporting on experiments with FORTRAN programs. Section 9 summarizes the algorithms and time bounds, compares our technique with other techniques, and presents some conclusions.
