---
paper: aho-1975-corasick
title: 'Efficient String Matching: An Aid to Bibliographic Search'
authors:
  - Alfred V. Aho
  - Margaret J. Corasick
year: 1975
venue: Communications of the ACM
field: algorithms
section: "5"
section_title: Time Complexity of Algorithms 1, 2, and 3
tag: "0340"
kind: section
lang: en
source: https://cr.yp.to/bib/1975/aho.pdf
pdf_sha256: f04940c07d2a12726bce4147fd4217e876cd969ddf44094ad90c866893deed34
pdf_pages: 5-6
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 11bff1496ab7583c745413dafd8015ebfa2741ddcdb80f3b061f34e9df54b1f7
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

We now examine the time complexity of Algorithms 1, 2, and 3. We shall show that using the goto, failure and output functions created by Algorithms 2 and 3, the number of state transitions made by Algorithm 1 in processing a text string is independent of the number of keywords. We shall also show that Algorithms 2 and 3 can be implemented to run in time that is linearly proportional to the sum of the lengths of the keywords in $K$.

THEOREM 2. *Using the goto, failure and output functions created by Algorithms 2 and 3, Algorithm 1 makes fewer than $2n$ state transitions in processing a text string of length $n$.*

PROOF. In each operating cycle Algorithm 1 makes zero or more failure transitions followed by exactly one goto transition. From a state $s$ of depth $d$ Algorithm 1 can never make more than $d$ failure transitions in one operating cycle.\footnote{As many as $d$ failure transitions can be made. [13] shows that, if there is only one keyword in $K$, $O(\log d)$ is the maximum number of failure transitions which can be made in one operating cycle.} Thus the total number of failure transitions must be at least one less than the total number of goto transitions. In processing an input of length $n$ Algorithm 1 makes exactly $n$ goto transitions. Therefore the total number of state transitions is less than $2n$. □

The actual time complexity of Algorithm 1 depends on how expensive it is:

1. to determine $g(s, a)$ for each state $s$ and input symbol $a$,

Communications June 1975
of Volume 18
the ACM Number 6

2. to determine $f(s)$ for each state $s$,
3. to determine whether $output(s)$ is empty, and
4. to emit $output(s)$.

We could store the goto function in a two-dimensional array, which would allow us to determine the value of $g(s, a)$ in constant time for each $s$ and $a$. If the size of the input alphabet and the keyword set are large, however, then it is far more economical to store only the nonfail values in a linear list [1,11] for each state. Such a representation would make the cost of determining $g(s, a)$ proportional to the number of nonfail values of the goto function for state $s$. A reasonable compromise, and one which we have employed, is to store the most frequently used states (such as state 0) as direct access tables in which the next state can be determined by directly indexing into the table with the current input symbol. Then for the most frequently used states we can determine $g(s, a)$ for each $a$ in constant time. Less frequently used states and states with few nonfail values of the goto function can be encoded as linear lists.

Another approach would be to store the goto values for each state in the form of a binary search tree [1, 12].

The failure function can be stored as a one-dimensional array so that $f(s)$ can be determined in constant time for each $s$.

Thus, the non-printing portion of Algorithm 1 can be implemented to process a text string of length $n$ in $cn$ steps, where $c$ is a constant that is independent of the number of keywords.

Let us now consider the time required to print the output. A one-dimensional array can be used to determine whether $output(s)$ is empty in constant time for each $s$. The cost of printing the output in each operating cycle is proportional to the sum of the lengths of the keywords in $output(s)$ where $s$ is the state in which Algorithm 1 is at the end of the operating cycle. In many applications $output(s)$ will usually contain at most one keyword, so the time required to print the output at each input position is constant.

It is possible, however, that a large number of keywords occur at every position of the text string. In this case Algorithm 1 will spend a considerable amount of time printing out the answer. In the worst case we may have to print all keywords in $K$ at virtually every position of the text string. (Consider an extreme case where $K = \{a, a^2, a^3, \ldots, a^k\}$ and the text string is $a^n$. Here $a^i$ denotes the string of $i$ $a$'s.) Any other pattern matching algorithm, however, would also have to print out the same number of keywords at each position of the text string so it is reasonable to compare pattern matching algorithms on the basis of the time spent in recognizing where the keywords occur.

We should contrast the performance of Algorithm 1 with a more straightforward way of locating all keywords in $K$ that are substrings of a given text string. One such way would be to take in turn each keyword in $K$ and successively match that keyword against all character positions in the text string. The running time of this technique is at best proportional to the product of the number of keywords in $K$ times the length of the text string. If there are many keywords, the performance of this algorithm will be considerably worse that that of Algorithm 1. In fact it was the time complexity of the straightforward algorithm that prompted the development of Algorithm 1. (The reader may wish to compare the performance of the two algorithms when $K = \{a, a^2, \ldots, a^k\}$ and the text string is $a^n$.)

Finally let us consider the cost of computing the goto, failure, and output functions using Algorithms 2 and 3.

THEOREM 3. Algorithm 2 requires time linearly proportional to the sum of the lengths of the keywords.

PROOF. Straightforward. □

THEOREM 4. Algorithm 3 can be implemented to run in time proportional to the sum of the lengths of the keywords.

PROOF. Using an argument similar to that in Theorem 2, we can show that the total number of executions of the statement $state \leftarrow f(state)$ made during the course of Algorithm 3 is bounded by the sum of the lengths of the keywords. Using linked lists to represent the output set of a state, we can execute the statement $output(s) \leftarrow output(s) \cup output(f(s))$ in constant time. Note that $output(s)$ and $output(f(s))$ are disjoint when this statement is executed. Thus the total time needed to implement Algorithm 3 is dominated by the sum of the lengths of the keywords. □
