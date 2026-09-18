---
paper: aho-1975-corasick
title: 'Efficient String Matching: An Aid to Bibliographic Search'
authors:
  - Alfred V. Aho
  - Margaret J. Corasick
year: 1975
venue: Communications of the ACM
field: algorithms
section: "3"
section_title: Construction of Goto, Failure, and Output Functions
tag: 033C
kind: section
lang: en
source: https://cr.yp.to/bib/1975/aho.pdf
pdf_sha256: f04940c07d2a12726bce4147fd4217e876cd969ddf44094ad90c866893deed34
pdf_pages: 3-4
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: fc5ea43f41fcab80bb49c2dfcf46c4957c39801edd3a9c06a96f1cefd750b1a3
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

We say that the three functions $g, f,$ and output are valid for a set of keywords if with these functions Algorithm 1 indicates that keyword $y$ ends at position $i$ of text string $x$ if and only if $x = uyv$ and the length of $uy$ is $i$.

We shall now show how to construct valid goto, failure and output functions from a set of keywords. There are two parts to the construction. In the first part we determine the states and the goto function. In the second part we compute the failure function. The computation of the output function is begun in the first part of the construction and completed in the second part.

To construct the goto function, we shall construct a goto graph. We begin with a graph consisting of one vertex which represents the state 0. We then enter each keyword $y$ into the graph, by adding a directed path to the graph that begins at the start state. New vertices and edges are added to the graph so that there will be, starting at the start state, a path in the graph that spells out the keyword $y$. The keyword $y$ is added to the output function of the state at which the path terminates. We add new edges to the graph only when necessary.

For example, suppose {he, she, his, hers} is the set of keywords. Adding the first keyword to the graph, we obtain:

Figure.

The path from state 0 to state 2 spells out the keyword “he”; we associate the output "he" with state 2. Adding the second keyword “she,” we obtain the graph:

Figure.

The output “she” is associated with state 5. Adding the keyword “his,” we obtain the following graph. Notice that when we add the keyword “his” there is already an edge labeled h from state 0 to state 1, so we do not need to add another edge labeled h from state 0 to state 1. The output “his” is associated with state 7.

Adding the last keyword “hers,” we obtain:

Figure.

The output “hers” is associated with state 9. Here we have been able to use the existing edge labeled h from state 0 to 1 and the existing edge labeled e from state 1 to 2.

Up to this point the graph is a rooted directed tree. To complete the construction of the goto function we add a loop from state 0 to state 0 on all input symbols other than h or s. We obtain the directed graph shown in Figure 1(a). This graph represents the goto function.

The failure function is constructed from the goto function. Let us define the depth of a state $s$ in the goto graph as the length of the shortest path from the start state to $s$. Thus in Figure 1(a), the start state is of depth 0, states 1 and 3 are of depth 1, states 2, 4, and 6 are of depth 2, and so on.

We shall compute the failure function for all states of depth 1, then for all states of depth 2, and so on, until the failure function has been computed for all states (except state 0 for which the failure function is not defined). The algorithm to compute the failure function $f$ at a state is conceptually quite simple. We make $f(s) = 0$ for all states $s$ of depth 1. Now suppose $f$ has been computed for all states of depth less than $d$. The failure function for the states of depth $d$ is computed from the failure function for the states of depth less than $d$. The states of depth $d$ can be determined from the nonfail values of the goto function of the states of depth $d-1$.

Specifically, to compute the failure function for the states of depth $d$, we consider each state $r$ of depth $d-1$ and perform the following actions.

1. If $g(r, a) = fail$ for all $a$, do nothing.
2. Otherwise, for each symbol $a$ such that $g(r, a) = s$, do the following:

(a) Set $state = f(r)$.

(b) Execute the statement $state \leftarrow f(state)$ zero or more times, until a value for $state$ is obtained such that $g(state, a) \neq fail$. (Note that since $g(0, a) \neq fail$ for all $a$, such a state will always be found.)

(c) Set $f(s) = g(state, a)$.

For example, to compute the failure function from Figure 1(a), we would first set $f(1) = f(3) = 0$ since 1 and 3 are the states of depth 1. We then compute the failure function for 2, 6, and 4, the states of depth 2. To compute $f(2)$, we set $state = f(1) = 0$; and since $g(0, e) = 0$, we find that $f(2) = 0$. To compute $f(6)$, we set $state = f(1) = 0$; and since $g(0, i) = 0$, we find that $f(6) = 0$. To compute $f(4)$, we set $state = f(3) = 0$; and since $g(0, h) = 1$, we find that $f(4) = 1$. Continuing in this fashion, we obtain the failure function shown in Figure 1(b).

During the computation of the failure function we also update the output function. When we determine $f(s) = s'$, we merge the outputs of state $s$ with the outputs of state $s'$.

For example, from Figure 1(a) we determine $f(5) = 2$. At this point we merge the output set of state 2, namely {he}, with the output set of state 5 to derive the new output set {he, she}. The final nonempty output sets are shown in Figure 1(c).

The algorithms to construct the goto, failure and output functions from $K$ are summarized below.

Algorithm 2. Construction of the goto function. {#aho-1975-corasick-alg-2 .code tag=033D}
Input. Set of keywords $K = \{y_1, y_2, \ldots, y_k\}$.
Output. Goto function $g$ and a partially computed output function $output$.
Method. We assume $output(s)$ is empty when state $s$ is first created, and $g(s, a) = fail$ if $a$ is undefined or if $g(s, a)$ has not yet been defined. The procedure $enter(y)$ inserts into the goto graph a path that spells out $y$.

begin
    newstate \leftarrow 0
    for $i \leftarrow 1$ until $k$ do $enter(y_i)$
        for all $a$ such that $g(0, a) = fail$ do $g(0, a) \leftarrow 0$
end procedure $enter(a_1 a_2 \cdots a_m)$:
begin
    state \leftarrow 0; j \leftarrow 1
    while $g(state, a_j) \neq fail$ do
        begin
            state \leftarrow g(state, a_j)
            j \leftarrow j + 1
        end
    for $p \leftarrow j$ until $m$ do
        begin
            newstate \leftarrow newstate + 1
            $g(state, a_p) \leftarrow newstate$
            state \leftarrow newstate
        end
    output(state) \leftarrow \{a_1 a_2 \cdots a_m\}
end

The following algorithm, whose inner loop is similar to Algorithm 1, computes the failure function.

Algorithm 3. Construction of the failure function. {#aho-1975-corasick-alg-3 .code tag=033E}
Input. Goto function $g$ and output function $output$ from Algorithm 2.
Output. Failure function $f$ and output function $output$.
Method.
begin
    queue \leftarrow empty
    for each $a$ such that $g(0, a) = s \neq 0$ do
        begin
            queue \leftarrow queue \cup \{s\}
            $f(s) \leftarrow 0$
        end
    while $queue \neq empty$ do
        begin
            let $r$ be the next state in $queue$
            $queue \leftarrow queue - \{r\}$
            for each $a$ such that $g(r, a) = s \neq fail$ do
                begin
                    queue \leftarrow queue \cup \{s\}
                    state \leftarrow f(r)
                    while $g(state, a) = fail$ do $state \leftarrow f(state)$
                    $f(s) \leftarrow g(state, a)$
                    $output(s) \leftarrow output(s) \cup output(f(s))$
                end
        end
end

The first for-loop computes the states of depth 1 and enters them in a first-in first-out list denoted by the variable $queue$. The main while-loop computes the set of states of depth $d$ from the set of states of depth $d-1$.

The failure function produced by Algorithm 3 is not optimal in the following sense. Consider the pattern matching machine $M$ of Figure 1. We see $g(4, e) = 5$. If $M$ is in state 4 and the current input symbol $a_i$ is not an e, then $M$ would enter state $f(4) = 1$. Since $M$ has already determined that $a_i \neq e$, $M$ does not then need to consider the value of the goto function of state 1 on e. In fact, if the keyword "his" were not present, then $M$ could go directly from state 4 to state 0, skipping an unnecessary intermediate transition to state 1.

To avoid making unnecessary failure transitions we can use $f'$, a generalization of the next function from [13], in place of $f$ in Algorithm 1. Specifically, define $f'(1) = 0$. For $i > 1$, define $f'(i) = f'(f(i))$ if, for all input symbols $a$, $g(f(i), a) \neq fail$ implies $g(i, a) \neq fail$; define $f'(i) = f(i)$, otherwise. However, to avoid making any failure transitions at all, we can use the deterministic finite automaton version of Algorithm 1 given in Section 6.
