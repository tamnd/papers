---
paper: mccarthy-1960-lisp
title: Recursive Functions of Symbolic Expressions and Their Computation by Machine, Part I
authors:
  - John McCarthy
year: 1960
venue: Communications of the ACM
field: languages
section: "6"
section_title: Flowcharts and Recursion
tag: "0253"
kind: section
lang: en
source: http://www-formal.stanford.edu/jmc/recursive.pdf
pdf_sha256: 3d981849e59505eff3f14397a177b409f5d978d43d114bdd67c956e74320fc92
pdf_pages: 31-33
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 782374634ba1a8a672a9b0ef14d14502e136175f724817ad77e43a64fec6711f
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Since both the usual form of computer program and recursive function definitions are universal computationally, it is interesting to display the relation between them. The translation of recursive symbolic functions into computer programs was the subject of the rest of this report. In this section we show how to go the other way, at least in principle.

The state of the machine at any time during a computation is given by the values of a number of variables. Let these variables be combined into a vector $\xi$. Consider a program block with one entrance and one exit. It defines and is essentially defined by a certain function $f$ that takes one machine configuration into another, that is, $f$ has the form $\xi' = f(\xi)$. Let us call $f$ the associated function of the program block. Now let a number of such blocks be combined into a program by decision elements $\pi$ that decide after each block is completed which block will be entered next. Nevertheless, let the whole program still have one entrance and one exit.

Figure 5

We give as an example the flowcart of figure 5. Let us describe the function $r[\xi]$ that gives the transformation of the vector $\xi$ between entrance and exit of the whole block. We shall define it in conjunction with the functions s($\xi$), and t[$\xi$], which give the transformations that $\xi$ undergoes between the points S and T, respectively, and the exit. We have

$$
r[\xi] = [\pi_1 1[\xi] \rightarrow S[f_1[\xi]]; T \rightarrow S[f_2[\xi]]]
$$

$$
S[\xi] = [\pi_2 1[\xi] \rightarrow r[\xi]; T \rightarrow t[f_3[\xi]]]
$$

$$
t[\xi] = [\pi 3I[\xi] \rightarrow f_4[\xi]; \pi_3 2[\xi] \rightarrow r[\xi]; T \rightarrow t[f_3[\xi]]]
$$

Given a flowchart with a single entrance and a single exit, it is easy to write down the recursive function that gives the transformation of the state vector from entrance to exit in terms of the corresponding functions for the computation blocks and the predicates of the branch. In general, we proceed as follows.

In figure 6, let $\beta$ be an n-way branch point, and let $f_1, \cdots, f_n$ be the computations leading to branch points $\beta_1, \beta_2, \cdots, \beta_n$. Let $\phi$ be the function that transforms $\xi$ between $\beta$ and the exit of the chart, and let $\phi_1, \cdots, \phi_n$ be the corresponding functions for $\beta_1, \cdots, \beta_n$. We then write

$$
\phi[\xi] = [p_1[\xi] \rightarrow \phi_1[f_1[\xi]] ; \cdots ; p_n[\xi] \rightarrow \phi_n[\xi]]
$$

Figure.

Figure 6
