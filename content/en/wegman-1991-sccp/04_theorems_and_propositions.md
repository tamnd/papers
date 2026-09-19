---
paper: wegman-1991-sccp
title: Constant Propagation with Conditional Branches
authors:
  - Mark N. Wegman
  - F. Kenneth Zadeck
year: 1991
venue: ACM TOPLAS
field: languages
section: "4"
section_title: THEOREMS AND PROPOSITIONS
tag: 05C6
kind: section
lang: en
source: https://www.cs.utexas.edu/users/lin/cs380c/wegman.pdf
pdf_sha256: 40929436cdf1c477f2318221df5d0aa71488db4a01cc448b184e0aba8bf95ddb
pdf_pages: 14-15
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 7ff6b511be83b53ed3624120689493cc47c69d4f162c07819e7fb50c82a929af
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

In this section we first show that SCC is conservative, that is, it does not label as constant variables that are not constant. We then show that SCC is at least as powerful as CC and finds all the constants that CC does. Wegbreit’s Algorithm 3.2 and Holley’s and Rosen’s algorithm [23] are more powerful than CC but may require exponential time.

Before we define “conservative” more formally, we need the concept of an executable sequence.

Definition. An executable sequence is a sequence of tuples in which each tuple consists of a node in the flow graph and a lattice element for each variable. The first tuple contains the start node, and each subsequent tuple is derived by evaluating the expression at the node and changing values as appropriate. The next tuple is determined by deriving values of expressions and branching appropriately.

Definition. An output assignment is conservative if the values of variables at each node are no higher in the lattice-theoretic sense than the values when that node is reached on any executable sequence.6

Theorem. The output assignment derived from SCC is conservative and an execution sequence traverses only those edges SCC labels as executable.

Proof. Suppose the contrary. Then there must be a shortest execution sequence that either traverses an edge not labeled executable or has a value lower than the output assignment to a variable at that node. If an edge not labeled executable is on the path, it must be the first such edge or else there is a shorter such path. The preceding node on the path must be a conditional and the values of the variables used in the condition must be different in the sequence from those in the output assignment, since otherwise the edge would have been labeled executable. But then there is a shorter path.

Thus, there must be a value which is higher in the output assignment than on the sequence. That value is used at the last node in the shortest sequence. Therefore there must be a preceding assignment node to the variable, and at the assignment node the values agree with the output of SCC. There must be an SSA edge from that assignment node to the last node in the sequence, since there are no intervening assignment nodes. Thus the value at the last node must be correct. □

6This notion is very similar to Graham and Wegman’s safe assignment [21]. In [21], an executable sequence can be any path, even one that takes branches contrary to provably constant branches. Thus, a safe assignment is conservative, but a conservative assignment is not necessarily safe.

Now that we have shown that no more constants are found than is correct, we wish to show that we find as many constants as other algorithms. We compare our algorithm to CC, which finds more constants than SC. CC is identical to SC except that CC does not propagate values along branches from conditions until it shows that the branch may be taken.

Theorem. *The output assignment derived by SCC gives each variable at each node a value which in the lattice-theoretic sense is at least as large as CC’s output assignment.*

Proof. Suppose the contrary. There must be a lower value at an executable node, since if the two algorithms agree on which way branches can go, they must agree on which nodes are executable.

Then SCC has a shortest execution in which it evaluates an expression whose value is lower than CC’s value or a point at which a variable is assigned a lower value. If the assignment is a normal assignment (does not use a $\phi$-function), then one of the variables involved in the expression must have a lower value; hence there is an earlier assignment. If the assignment is from a $\phi$-function, then either (1) one of its arguments is lower than it would be in the preceding node in CC or (2) the argument is flagged as executable but the entering edge is not executable in CC.

In case (1), there must be an earlier assignment to the variable. In case (2), there must be an edge that we say is executable but CC does not. If so, we must have evaluated the expression controlling the condition to a lower value than CC. But that evaluation takes place earlier, and hence there is a shorter path. □
