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
section: "7"
section_title: TRANSLATING FROM SSA FORM
tag: 05AA
kind: section
lang: en
source: https://www.cs.utexas.edu/~pingali/CS380C/2010/papers/ssaCytron.pdf
pdf_sha256: 307512bb537628c2b326b23aa02109e7562bfc619509e942e015054ab58eb9ab
pdf_pages: 28-32
extraction: vision
extraction_model: gpt-5
content_sha256: 148f255c17043f1fed00517dde9bd9797232eab97a3c05b15921c337d1c05eaa
edited: true
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Many powerful analysis and transformation techniques can be applied to programs in SSA form. Eventually, however, a program must be executed. The $\phi$-functions have precise semantics, but they are generally not represented in existing target machines. This section describes how to translate out of SSA form by replacing each $\phi$-function with some ordinary assignments. Naive translation could yield inefficient object code, but efficient code can be generated if two already useful optimizations are applied: dead code elimination and storage allocation by coloring.

Naively, a $k$-input $\phi$-function at entrance to a node $X$ can be replaced by $k$ ordinary assignments, one at the end of each control flow predecessor of $X$. This is always correct, but these ordinary assignments sometimes perform a good deal of useless work. If the naive replacement is preceded by dead code elimination and then followed by coloring, however, the resulting code is efficient.

### 7.1 Dead Code Elimination {#cytron-1991-ssa-s7-1 .section tag=05AB}

The original source program may have *dead code* (i.e., code that has no effect on any program output). Some of the intermediate steps in compilation (such as procedure integration) may also introduce dead code. Code that once was live may become dead in the course of optimization. With so many possible sources for dead code, it is natural to perform (or repeat) dead code elimination late in the optimization process, rather than burden many intermediate steps with concerns about dead code.

Translation to SSA form is one of the compilation steps that may introduce dead code. Suppose that $V$ is assigned and then used along each branch of an if...then...else..., but that $V$ is never used after the join point. The original assignments to $V$ are live, but the added assignment by the $\phi$-function is dead. Often, such dead $\phi$-functions are useful, as in the equivalencing and redundancy elimination algorithms that are based on SSA form [5, 43]. One such use is shown in Figure 16. Although others have avoided placement of dead $\phi$-functions in translating to SSA form [16, 52], we prefer to include the dead $\phi$-functions to increase optimization opportunities.

There are many different definitions of dead code in the literature. Dead code is sometimes defined to be unreachable code and sometimes defined (as it is here) to be ineffectual code. In both cases, it is desirable to use the broadest possible definition, subject to the correctness condition that "dead" code really can be safely removed.\footnote{The definition used here is broader than the usual one [1, p 595] and similar to that of "faint" variables [25, p. 489].} A procedural version of the definition is more intuitive than a recursive version, so we prefer the procedural style.

Initially, all statements are tentatively marked dead. Some statements, however, need to be marked live because of the conditions listed below. Marking these statements live may cause others to be marked live. When the natural worklist eventually empties, any statements that are still marked dead are truly dead and can be safely removed from the code.

```text
if P₁
then do
    Y₁ ← 1
    use of Y₁
end
else do
    Y₂ ← X₁
    use of Y₂
end
Y₃ ← φ(Y₁, Y₂)
...
if P₁
    then Z₁ ← 1
    else Z₂ ← X₁
Z₃ ← φ(Z₁, Z₂)
use of Z₃ if P₁
then do
    Y₁ ← 1
    use of Y₁
end
else do
    Y₂ ← X₁
    use of Y₂
end
Y₃ ← φ(Y₁, Y₂)
...
use of Y₃
```

Fig. 16. On the left is an unoptimized program containing a dead φ-function that assigns to Y₃. The value numbering technique in [5] can determine that Y₃ and Z₃ have the same value. Thus, Z₃ and many of the computations that produce it can be eliminated. The dead φ-function is brought to life by using Y₃ in place of Z₃. {#cytron-1991-ssa-fig-16 .figure tag=05AC}

A statement is marked live iff at least one of the following holds:

(1) The statement is one that should be assumed to affect program output, such as an I/O statement, an assignment to a reference parameter, or a call to a routine that may have side effects.
(2) The statement is an assignment statement, and there are statements already marked live that use some of its outputs.
(3) The statement is a conditional branch, and there are statements already marked live that are control dependent on this conditional branch.

Several published algorithms eliminate dead code in the narrower sense that requires every conditional branch to be marked live [30, 31, 38].¹⁰ Our algorithm, given in Figure 17, goes one step further in eliminating dead conditional branches. (An unpublished algorithm by R. Paige does this also.)

¹⁰ The more readily accessible [31] contains a typographical error; the earlier technical report [30] should be consulted for the correct version.

```text
for each statement S do
    if S ∈ PreLive
        then Live(S) ← true
        else Live(S) ← false
    end
WorkList ← PreLive
```

while ($WorkList \neq \emptyset$) do
    take $S$ from WorkList

```text
for each D ∈ Definers(S) do
        if Live(D) = false
            then do
                Live(D) ← true
                WorkList ← WorkList ∪ { D }
            end
        end
    end

for each block B in CD⁻¹(Block(S)) do
        if Live(Last(B)) = false
            then do
                Live(Last(B)) ← true
                WorkList ← WorkList ∪ { Last(B) }
            end
        end
    end
end
```

for each statement $S$ do
    if $Live(S) =$ false
        then delete $S$ from $Block(S)$
end

Fig. 17   Dead code elimination

The following data structures are used:

—$Live(S)$ indicates that statement $S$ is live.
—$PreLive$ is the set of statements whose execution is initially assumed to affect program output. Statements that result in I/O or side effects outside the current procedure scope are typically included.
—$WorkList$ is a list of statements whose liveness has been recently discovered.
—$Definers(S)$ is the set of statements that provide values used by statement $S$.
—$Last(B)$ is the statement that terminates basic block $B$.
—$Block(S)$ is the basic block containing statement $S$.
—$ipdom(B)$ is the basic block that immediately postdominates block $B$.

—$CD^{-1}(B)$ is the set of nodes that are control dependence predecessors of the node corresponding to block $B$. This is the same as $RDF(B)$ in Figure 14.

After the algorithm discovers the live statements, all those still not marked live are deleted.$^{11}$ Other optimizations (such as code motion) may leave empty blocks, so there is already ample reason for a late optimization to remove them. The empty blocks left by dead code elimination can be removed along with any other empty blocks.

The fact that statements are considered dead until marked live is crucial for condition (2). Statements that depend (transitively) on themselves are never marked live unless required by some other live statement. Condition (3) is handled by the loop over $CD^{-1}(Block(S))$. A basic block whose termination controls a block with live statements is itself live.

### 7.2 Allocation by Coloring {#cytron-1991-ssa-s7-2 .section tag=05AD}

At first, it might seem possible simply to map all occurrences of $V_i$ back to $V$ and to delete all of the $\phi$-functions. However, the new variables introduced by translation to SSA form cannot always be eliminated, because optimizations may have capitalized on the storage independence of the new variables. The useful persistence of the new variables introduced by translation to SSA form can be illustrated by the code motion example in Figure 18. The source code (Figure 18a) assigns to $V$ twice and uses it twice. The SSA form (Figure 18b) can be optimized by moving the invariant assignment out of the loop, yielding a program with separate variables for separate purposes (Figure 18c). The dead assignment to $V_3$ will be eliminated. These optimizations leave a region in the program where $V_1$ and $V_2$ are simultaneously live. Thus, both variables are required: The original variable $V$ cannot substitute for both renamed variables.

Any graph coloring algorithm [12, 13, 17, 18, 21] can be used to reduce the number of variables needed and thereby can remove most of the associated assignment statements. The choice of coloring technique should be guided by the eventual use of the output. If the goal is to produce readable source code, then it is desirable to consider each original variable $V$ separately, coloring just the SSA variables derived from $V$. If the goal is machine code, then all of the SSA variables should be considered at once. In both cases, the process of coloring changes most of the assignments that were inserted to model the $\phi$-functions into identity assignments, that is, assignments of the form $V \leftarrow V$. These identity assignments can all be deleted.

Storage savings are especially noticeable for arrays. If optimization does not perturb the order of the first two statements in Figure 7, then arrays $A_8$ and $A_9$ can be assigned the same color and, hence, can share the same storage. The array $A_9$ is then assigned an Update from an identically colored array. Such operations can be implemented inexpensively by assigning to just one component if the arrays share storage. In particular, the actual operation performed by HiddenUpdate is always of this form.

$^{11}$A conditional branch can be deleted by transforming it to an unconditional branch to any one of its prior targets.

```text
while (...) do    while (...) do    while (...) do
    W₃ ← φ(W₀, W₂)
    V₃ ← φ(V₀, V₂)
read V
read V_1
W \leftarrow V + W   W_1 \leftarrow V_1 + W_3
V \leftarrow 6      V_2 \leftarrow 6
W \leftarrow V + W   W_2 \leftarrow V_2 + W_1
end               end               end
(a)                (b)                (c)
```

Fig 18. Program that really uses two instances for a variable after code motion. (a) Source program; (b) unoptimized SSA form; (c) result of code motion.
