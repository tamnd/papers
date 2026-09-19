---
paper: aho-1975-corasick
title: 'Efficient String Matching: An Aid to Bibliographic Search'
authors:
  - Alfred V. Aho
  - Margaret J. Corasick
year: 1975
venue: Communications of the ACM
field: algorithms
section: "6"
section_title: Eliminating Failure Transitions
tag: "0341"
kind: section
lang: en
source: https://cr.yp.to/bib/1975/aho.pdf
pdf_sha256: f04940c07d2a12726bce4147fd4217e876cd969ddf44094ad90c866893deed34
pdf_pages: 6-7
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 5c092ee8035d2f40bb391276106bac31a03b083027b3d54af2be5f6516278aa6
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

This section shows how to eliminate all failure transitions from Algorithm 1 by using the next move function of a deterministic finite automaton in place of the goto and failure functions.

A deterministic finite automaton [15] consists of a finite set of states $S$ and a next move function $\delta$ such that for each state $s$ and input symbol $a$, $\delta(s, a)$ is a state in $S$. That is to say, a deterministic finite automaton makes exactly one state transition on each input symbol.

By using the next move function $\delta$ of an appropriate deterministic finite automaton in place of the goto function in Algorithm 1, we can dispense with all failure transitions. This can be done by simply replacing the first two statements in the for-loop of Algorithm 1 by the single statement $state \leftarrow \delta(state, a_i)$. Using $\delta$, Algorithm 1 makes exactly one state transition per input character.

We can compute the required next move function $\delta$ from the goto and failure functions found by Algorithms 2 and 3 using Algorithm 4. Algorithm 4 just precomputes the result of every sequence of possible failure transitions. The time taken by Algorithm 4 is linearly proportional to the size of the keyword set. In practice, Algorithm 4 would be evaluated in conjunction with Algorithm 3.

The next move function computed by Algorithm 4 from the goto and failure functions shown in Figure 1 is tabulated in Figure 3.

The next move function is encoded in Figure 3 as follows. In state 0, for example, we have a transition on h to state 1, a transition on s to state 3, and a transition on any other symbol to state 0. In each state, the dot stands for any input character other than those above it. This method of encoding the next move function is more economical than storing δ as a two-dimensional array. However, the amount of memory required to store δ in this manner is somewhat larger than the corresponding representation for the goto function from which δ was constructed since many of the states in δ each contain transitions from several states of the goto function.

Algorithm 4. Construction of a deterministic finite automaton. {#aho-1975-corasick-alg-4 .code tag=0342}

```text
Input. Goto function g from Algorithm 2 and failure function f from Algorithm 3.
Output. Next move function δ.
Method.
begin
    queue ← empty
    for each symbol a do
        begin
            δ(0, a) ← g(0, a)
            if g(0, a) ≠ 0 then queue ← queue ∪ {g(0, a)}
        end
    while queue ≠ empty do
        begin
            let r be the next state in queue
            queue ← queue - {r}
            for each symbol a do
                if g(r, a) = s ≠ fail do
                    begin
                        queue ← queue ∪ {s}
                        δ(r, a) ← s
                    end
                else δ(r, a) ← δ(f(r), a)
        end
end
```

Using the next move function in Figure 3, Algorithm 1 with input “ushers” would make the sequence of state transitions shown in the first line of states of Figure 2.

Using a deterministic finite automaton in Algorithm 1 can potentially reduce the number of state transitions by 50%. This amount of saving, however, would virtually never be achieved in practice because in typical applications Algorithm 1 will spend most of its time in state 0 from which there are no failure transitions. Calculating the expected saving is difficult, however, because meaningful definitions of “average” set of keywords and “average” text string are not available.
