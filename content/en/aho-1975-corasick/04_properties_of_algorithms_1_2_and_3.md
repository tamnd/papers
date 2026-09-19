---
paper: aho-1975-corasick
title: 'Efficient String Matching: An Aid to Bibliographic Search'
authors:
  - Alfred V. Aho
  - Margaret J. Corasick
year: 1975
venue: Communications of the ACM
field: algorithms
section: "4"
section_title: Properties of Algorithms 1, 2, and 3
tag: 033F
kind: section
lang: en
source: https://cr.yp.to/bib/1975/aho.pdf
pdf_sha256: f04940c07d2a12726bce4147fd4217e876cd969ddf44094ad90c866893deed34
pdf_pages: 4-5
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 40a248d94e9dc6d44ae0934593810d456b34f7d3429804628aac0a909b4a0237
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

This section shows that the goto, failure, and output functions constructed by Algorithms 2 and 3 from a given set of keywords $K$ are indeed valid for $K$.

We say that $u$ is a prefix and $v$ is a suffix of the string $uv$. If $u$ is not the empty string, then $u$ is a proper prefix. Likewise, if $v$ is not empty, then $v$ is a proper suffix.

We say that string $u$ represents state $s$ of a pattern matching machine if the shortest path in the goto graph from the start state to state $s$ spells out $u$. The start state is represented by the empty string.

Our first lemma characterizes the failure function constructed by Algorithm 3.

LEMMA 1. *Suppose that in the goto graph state $s$ is represented by the string $u$ and state $t$ is represented by the string $v$. Then, $f(s) = t$ if and only if $v$ is the longest proper suffix of $u$ that is also a prefix of some keyword.*

PROOF. The proof proceeds by induction on the length of $u$ (or equivalently the depth of state $s$). By Algorithm 3 $f(s) = 0$ for all states $s$ of depth 1. Since each state of depth 1 is represented by a string of length 1, the statement of the lemma is trivially true for all strings of length 1.

For the inductive step, assume the statement of Lemma 1 is true for all strings of length less than $j, j > 1$. Suppose $u = a_1 a_2 \cdots a_j$ for some $j > 1$, and $v$ is the longest proper suffix of $u$ that is a prefix of some keyword. Suppose $u$ represents state $s$ and $a_1 a_2 \cdots a_{j-1}$ represents state $r$. Let $r_1, r_2, \cdots, r_n$ be the sequence of states such that

1. $r_1 = f(r)$,
2. $r_{i+1} = f(r_i)$ for $1 \leq i < n$,
3. $g(r_i, a_j) = fail$ for $1 \leq i < n$, and
4. $g(r_n, a_j) = t \neq fail$.

(If $g(r_1, a_j) \neq fail$, then $r_n = r_1$.) The sequence $r_1, r_2, \cdots, r_n$ is the sequence of values assumed by the variable *state* in the inner while-loop of Algorithm 3. The statement following that while-loop makes $f(s) = t$. We claim that $t$ is represented by the longest proper suffix of $u$ that is a prefix of some keyword.

To prove this, suppose $v_i$ represents state $r_i$ for $1 \leq i \leq n$. By the inductive hypothesis $v_1$ is the longest proper suffix of $a_1 a_2 \cdots a_{j-1}$ that is a prefix of some keyword; $v_2$ is the longest proper suffix of $v_1$ that is a prefix of some keyword; $v_3$ is the longest proper suffix of $v_2$ that is a prefix of some keyword, and so on.

Thus $v_n$ is the longest proper suffix of $a_1 a_2 \cdots a_{j-1}$ such that $v_n a_j$ is a prefix of some keyword. Therefore $v_n a_j$ is the longest proper suffix of $u$ that is a prefix of some keyword. Since Algorithm 3 sets $f(s) = g(r_n, a_j) = t$, the proof is complete. □

The next lemma characterizes the output function constructed by Algorithms 2 and 3.

LEMMA 2. *The set output$(s)$ contains $y$ if and only if $y$ is a keyword that is a suffix of the string representing state $s$.*

PROOF. In Algorithm 2 whenever we add to the goto graph a state $s$ that is represented by a keyword $y$ we make $output(s) = \{y\}$. Given this initialization, we shall show by induction on the depth of state $s$ that $output(s) = \{y \mid y \text{ is a keyword that is a suffix of the string representing state } s\}$.

This statement is certainly true for the start state which is of depth 0. Assuming this statement is true for all states of depth less than $d$, consider a state $s$ of depth $d$. Let $u$ be the string that represents state $s$.

Consider a string $y$ in $output(s)$. If $y$ is added to $output(s)$ by Algorithm 2, then $y = u$ and $y$ is a keyword. If $y$ is added to $output(s)$ by Algorithm 3, then $y$ is in $output(f(s))$. By the inductive hypothesis, $y$ is a keyword that is a suffix of the string representing state $f(s)$. By Lemma 1, any such keyword must be a suffix of $u$.

Conversely, suppose $y$ is any keyword that is a suffix of $u$. Since $y$ is a keyword, there is a state $t$ that is represented by $y$. By Algorithm 2, $output(t)$ contains $y$. Thus if $y = u$, then $s = t$ and $output(s)$ certainly contains $y$. If $y$ is a proper suffix of $u$, then from the inductive hypothesis and Lemma 1 we know $output(f(s))$ contains $y$. Since Algorithm 3 considers states in order of increasing depth, the last statement of Algorithm 3 adds $output(f(s))$ and hence $y$ to $output(s)$. □

The following lemma characterizes the behavior of Algorithm 1 on a text string $x = a_1 a_2 \cdots a_n$.

LEMMA 3. *After the $j$th operating cycle, Algorithm 1 will be in state $s$ if and only if $s$ is represented by the longest suffix of $a_1 a_2 \cdots a_j$ that is a prefix of some keyword.*

PROOF. Similar to Lemma 1. □

THEOREM 1. *Algorithms 2 and 3 produce valid goto, failure, and output functions.*

PROOF. By Lemmas 2 and 3. □
