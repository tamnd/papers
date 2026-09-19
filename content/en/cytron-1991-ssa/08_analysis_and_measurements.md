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
section: "8"
section_title: ANALYSIS AND MEASUREMENTS
tag: 05AE
kind: section
lang: en
source: https://www.cs.utexas.edu/~pingali/CS380C/2010/papers/ssaCytron.pdf
pdf_sha256: 307512bb537628c2b326b23aa02109e7562bfc619509e942e015054ab58eb9ab
pdf_pages: 32-36
extraction: vision
extraction_model: gpt-5
content_sha256: d115d9748ff00bad25550f0166677029e355395680cbaaf7257a4c9e6468fc2a
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The number of nodes that contain $\phi$-functions for a variable $\mathbf{V}$ is a function of the program control flow structure and the assignments to $\mathbf{V}$. Program structure alone determines dominance frontiers and the number of control dependences. It is possible that dominance frontiers may be larger than necessary for computing $\phi$-function locations for some programs, since the actual assignments are not taken into account. In this section we prove that the size of the dominance frontiers is linear in the size of the program when control flow branching is restricted to **if-then-else** constructs and **while-do** loops. (We assume that expressions and predicates perform no internal branching.) Such programs can be described by the grammar given in Figure 19. We also give experimental results that suggest that the behavior is linear for actual programs.

**THEOREM 4.** *For programs comprised of straight-line code, if-then-else, and while-do constructs, the dominance frontier of any CFG node contains at most two nodes.*

**PROOF.** Consider a top-down parse of a program using the grammar shown in Figure 19. Initially, we have a single $\langle \text{program} \rangle$ node in the parse tree and a control flow graph $CFG$ with two nodes and one edge: **Entry \rightarrow Exit**. The initial dominance frontiers are $DF(\text{Entry}) = \varnothing = DF(\text{Exit})$. For each production, we consider the associated changes to $CFG$ and to the dominance frontiers of nodes. When a production expands a nonterminal parse tree node $S$, a new subgraph is inserted into $CFG$ in place of $S$. In this new subgraph, each node corresponds to a symbol on the right-hand side of the production.

We will show that applying any of the productions preserves the following invariants:

—Each $CFG$ node $S$ corresponding to an unexpanded $\langle \text{statement} \rangle$ symbol has at most one node in its dominance frontier.

```text
<program> ::= <statement>
<statement> ::= <statement><statement>
<statement> ::= if <predicate>
    then <statement>
    else <statement>
<statement> ::= while <predicate>
    do <statement>
<statement> ::= <variable> ← <expression>
```

Fig. 19. Grammar for control structures. {#cytron-1991-ssa-fig-19 .figure tag=05AF}

—Each $CFG$ node $T$ corresponding to a terminal symbol has at most two nodes in its dominance frontier.

We consider the productions in turn.

(1) This production adds a $CFG$ node $S$ and edges Entry $\rightarrow$ $S$ $\rightarrow$ Exit, yielding $DF(S) = \{\textbf{Exit}\}$.

(2) When this production is applied, a $CFG$ node $S$ is replaced by two nodes $S_1$ and $S_2$. Edges previously entering and leaving $S$ now enter $S_1$ and leave $S_2$. A single edge is inserted from $S_1$ to $S_2$. Although the control flow graph has changed, consider how this production affects the dominator tree: Nodes $S_1$ and $S_2$ dominate all nodes that were dominated by $S$; additionally, $S_1$ dominates $S_2$. Thus, we have $DF(S_1) = DF(S) = DF(S_2)$.

(3) When this production is applied, a $CFG$ node $S$ is replaced by nodes $T_{if}$, $S_{then}$, $S_{else}$, and $T_{endif}$. Edges previously entering and leaving $S$ now enter $T_{if}$ and leave $T_{endif}$. Edges are inserted from $T_{if}$ to both $S_{then}$ and $S_{else}$; edges are also inserted from $S_{then}$ and $S_{else}$ to $T_{endif}$. In the dominator tree, $T_{if}$ and $T_{endif}$ both dominate all nodes that were dominated by $S$. Additionally, $T_{if}$ dominates $S_{then}$ and $S_{else}$. By the argument made for production (2), we have $DF(T_{if}) = DF(S) = DF(T_{endif})$. Now consider nodes $S_{then}$ and $S_{else}$. From the definition of a dominance frontier, we obtain $DF(S_{then}) = DF(S_{else}) = \{T_{endif}\}$.

(4) When this production is applied, a $CFG$ node $S$ is replaced by nodes $T_{while}$ and $S_{do}$. All edges previously associated with node $S$ are now associated with node $T_{while}$. Edges are inserted from $T_{while}$ to $S_{do}$ and from $S_{do}$ to $T_{while}$. Node $T_{while}$ dominates all nodes that were dominated by node $S$. Additionally, $T_{while}$ dominates $S_{do}$. Thus, we have $DF(T_{while}) = DF(S) \cup \{T_{while}\}$ and $DF(S_{do}) = \{T_{while}\}$.

(5) After application of this production, the new control flow graph is isomorphic to the old graph. $\Box$

Corollary 2. For programs comprised of straight-line code, if-then-else, and while-do constructs, every node is control dependent on at most two nodes. {#cytron-1991-ssa-cor-2 .statement tag=05B0}

Proof. Consider a program $P$ composed of the allowed constructs and its associated control flow graph $CFG$. The reverse control flow graph $RCFG$ is

Table I. Summary Statistics of Our Experiment

```text
Package name  Statements in all procedures  Statements per procedure  Description
Min  Median  Max
EISPACK  7,034  22  89  327  Dense matrix eigenvectors and values
FLO52  2,054  9  54  351  Flow past an airfoil
SPICE  14,093  8  43  753  Circuit simulation
Totals  23,181  8  55  753  221 FORTRAN procedures
```

itself a structured control flow graph for some program $P'$. For all $Y$ in $RCFG, DF(Y)$ contains at most two nodes by Theorem 4. By Corollary 1, $Y$ is then control dependent on at most two nodes. □

Unfortunately, these linearity results do not hold for all program structures. In particular, consider the nest of repeat-until loops illustrated in Figure 5. For each loop, the dominance frontier of the entrance to that loop includes each of the entrances to surrounding loops. For $n$ nested loops, this leads to a dominance frontier mapping whose total size is $\Theta(n^2)$, yet each variable needs at most $O(n)$ $\phi$-functions. Most of the dominance frontier mapping is not actually used in placing $\phi$-functions, so it seems that the computation of dominance frontiers might take excessive time with respect to the resulting number of actual $\phi$-functions. We therefore wish to measure the number of dominance frontier nodes as a function of program size over a diverse set of programs.

We implemented our algorithms for constructing dominance frontiers and placing $\phi$-functions in the PTRAN system, which already offered the required local data flow and control flow analysis [2]. We ran these algorithms on 61 library procedures from EISPACK [46] and 160 procedures from two "Perfect" [39] benchmarks. Some summary statistics of these procedures are shown in Table I. These FORTRAN programs were chosen because they contain irreducible intervals and other unstructured constructs. As the plot in Figure 20 shows, the size of the dominance frontier mapping appears to vary linearly with program size. The ratio of these sizes ranged from 0.6 (the Entry node has an empty dominance frontier) to 2.1.

For the programs we tested, the plot in Figure 21 shows that the number of $\phi$-functions is also linear in the size of the original program. The ratio of these sizes ranged from 0.5 to 5.2. The largest ratio occurred for a procedure of only 12 statements, and 95 percent of the procedures had a ratio under 2.3. All but one of the remaining procedures contained fewer than 60 statements. Finally, the plot in Figure 22 shows that the size of the control dependence graph is linear in the size of the original program. The ratio of these sizes ranged from 0.6 to 2.4, which is very close to the range of ratios for dominance frontiers.

The ratio $avrgDF$ (defined by (7) in Section 5.1) measures the cost of placing $\phi$-functions relative to the number of assignments in the resulting

Fig. 20. Size of dominance frontier mapping versus number of program statements. {#cytron-1991-ssa-fig-20 .figure tag=05B1}

Fig. 21. Number of $\phi$-functions versus number of program statements. {#cytron-1991-ssa-fig-21 .figure tag=05B2}

SSA form program. This ratio varied from 1 to 2, with median 1.3. There was no correlation with program size.

We also measured the expansion $A_{tot}/A_{orig}$ in the number of assignments when translating to SSA form. This ratio varied from 1.3 to 3.8. Finally, we measured the expansion $M_{tot}/M_{orig}$ in the number of mentions (assignments or uses) of variables when translating to SSA form. This ratio varied from 1.6 to 6.2. For both of these ratios, there was no correlation with program size.

Fig. 22. Size of control dependence graph versus number of program statements. {#cytron-1991-ssa-fig-22 .figure tag=05B3}
