---
paper: aho-1975-corasick
title: 'Efficient String Matching: An Aid to Bibliographic Search'
authors:
  - Alfred V. Aho
  - Margaret J. Corasick
year: 1975
venue: Communications of the ACM
field: algorithms
section: "2"
section_title: A Pattern Matching Machine
tag: "0338"
kind: section
lang: en
source: https://cr.yp.to/bib/1975/aho.pdf
pdf_sha256: f04940c07d2a12726bce4147fd4217e876cd969ddf44094ad90c866893deed34
pdf_pages: 1-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: c96b1fbe5faa588c3d81ccdf3261471f4cf9418b5839a0edc71bcd58439b8cf8
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

This section describes a finite state string pattern matching machine that locates keywords in a text string. The next section describes the algorithms to construct such a machine from a given finite set of keywords.

In this paper a string is simply a finite sequence of symbols. Let $K = \{ y_1, y_2, \ldots, y_k \}$ be a finite set of strings which we shall call keywords and let $x$ be an arbitrary string which we shall call the text string. Our problem is to locate and identify all substrings of $x$ which are keywords in $K$. Substrings may overlap with one another.

A pattern matching machine for $K$ is a program which takes as input the text string $x$ and produces as output the locations in $x$ at which keywords of $K$ appear as substrings. The pattern matching machine consists of a set of states. Each state is represented by a number. The machine processes the text string $x$ by successively reading the symbols in $x$, making state transitions and occasionally emitting output. The behavior of the pattern matching machine is dictated by three functions: a goto function $g$, a failure function $f$, and an output function $output$.

Figure 1 shows the functions used by a pattern matching machine for the set of keywords {he, she, his, hers}.

Fig. 1. Pattern matching machine. {#aho-1975-corasick-fig-1 .figure tag=0339}

Figure.

(a) Goto function.

$$
\begin{array}{cccccccccc}
i & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 \\
f(i) & 0 & 0 & 0 & 1 & 2 & 0 & 3 & 0 & 3
\end{array}
$$

(b) Failure function.

$$
\begin{array}{ll}
i & output(i) \\
2 & \{he\} \\
5 & \{she, he\} \\
7 & \{his\} \\
9 & \{hers\}
\end{array}
$$

(c) Output function.

One state (usually 0) is designated as a start state. In Figure 1 the states are 0, 1, ..., 9. The goto function $g$ maps a pair consisting of a state and an input symbol into a state or the message fail. The directed graph in Figure 1(a) represents the goto function. For example, the edge labeled h from 0 to 1 indicates that $g(0, h) = 1$. The absence of an arrow indicates fail. Thus, $g(1, \sigma) = fail$ for all input symbols $\sigma$ that are not e or i. All our pattern matching machines have the property that $g(0, \sigma) \neq fail$ for all input symbols $\sigma$. We shall see that this property of the goto function on state 0 ensures that one input symbol will be processed by the machine in every machine cycle.

The failure function $f$ maps a state into a state. The failure function is consulted whenever the goto function reports fail. Certain states are designated as output states which indicate that a set of keywords has been found. The output function formalizes this concept by associating a set of keywords (possibly empty) with every state.

An operating cycle of a pattern matching machine is defined as follows. Let $s$ be the current state of the machine and $a$ the current symbol of the input string $x$.

1. If $g(s, a) = s'$, the machine makes a goto transition. It enters state $s'$ and the next symbol of $x$ becomes the current input symbol. In addition, if $output(s') \neq empty$, then the machine emits the set $output(s')$ along with the position of the current input symbol. The operating cycle is now complete.

2. If $g(s, a) = fail$, the machine consults the failure function $f$ and is said to make a failure transition. If $f(s) = s'$, the machine repeats the cycle with $s'$ as the current state and $a$ as the current input symbol.

Initially, the current state of the machine is the start state and the first symbol of the text string is the current input symbol. The machine then processes the text string by making one operating cycle on each symbol of the text string.

For example, consider the behavior of the machine $M$ that uses the functions in Figure 1 to process the text string "ushers." Figure 2 indicates the state transitions made by $M$ in processing the text string.

Fig. 2. Sequence of state transitions. {#aho-1975-corasick-fig-2 .figure tag=033A}

Consider the operating cycle when $M$ is in state 4 and the current input symbol is e. Since $g(4, e) = 5$, the machine enters state 5, advances to the next input symbol and emits $output(5)$, indicating that it has found the keywords "she" and "he" at the end of position four in the text string.

In state 5 on input symbol r, the machine makes two state transitions in its operating cycle. Since $g(5, r) = fail$, $M$ enters state $2 = f(5)$. Then since $g(2, r) = 8$, $M$ enters state 8 and advances to the next input symbol. No output is generated in this operating cycle.

The following algorithm summarizes the behavior of a pattern matching machine.

Algorithm 1. Pattern matching machine. {#aho-1975-corasick-alg-1 .code tag=033B}
Input. A text string $x = a_1 a_2 \cdots a_n$ where each $a_i$ is an input symbol and a pattern matching machine $M$ with goto function $g$, failure function $f$, and output function $output$, as described above.
Output. Locations at which keywords occur in $x$.
Method.
begin
state \leftarrow 0
for $i \leftarrow 1$ until $n$ do
begin
while $g(state, a_i) = fail$ do $state \leftarrow f(state)$
state \leftarrow $g(state, a_i)$
if $output(state) \neq empty$ then
begin
print $i$
print $output(state)$
end
end
end

Each pass through the for-loop represents one operating cycle of the machine.

Algorithm 1 is patterned after the Knuth-Morris-Pratt algorithm for finding one keyword in a text string [13] and can be viewed as an extension of the “trie” search discussed in [11]. Hopcroft and Karp (unpublished) have suggested a scheme similar to Algorithm 1 for finding the first occurrence of any of a finite set of keywords in a text string [13]. Section 6 of this paper discusses a deterministic finite automaton version of Algorithm 1 that avoids all failure transitions.
