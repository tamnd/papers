---
paper: mccarthy-1960-lisp
title: Recursive Functions of Symbolic Expressions and Their Computation by Machine, Part I
authors:
  - John McCarthy
year: 1960
venue: Communications of the ACM
field: languages
section: "5"
section_title: Another Formalism for Functions of Symbolic Expressions
tag: "0252"
kind: section
lang: en
source: http://www-formal.stanford.edu/jmc/recursive.pdf
pdf_sha256: 3d981849e59505eff3f14397a177b409f5d978d43d114bdd67c956e74320fc92
pdf_pages: 30-31
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: f446791b43e563b4a0397ff6bd78f375e618fff009605b2c37bc5552bcc6b137
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

There are a number of ways of defining functions of symbolic expressions which are quite similar to the system we have adopted. Each of them involves three basic functions, conditional expressions, and recursive function definitions, but the class of expressions corresponding to S-expressions is different, and so are the precise definitions of the functions. We shall describe one of these variants called linear LISP.

The L-expressions are defined as follows:
1. A finite list of characters is admitted.
2. Any string of admitted characters in an L-expression. This includes the null string denoted by $\Lambda$.

There are three functions of strings:
1. $first[x]$ is the first character of the string $x$.
$first[\Lambda]$ is undefined. For example: $first[ABC] = A$
2. $rest[x]$ is the string of characters which remains when the first character of the string is deleted.
$rest[\Lambda]$ is undefined. For example: $rest[ABC] = BC$.
3. $combine[x; y]$ is the string formed by prefixing the character $x$ to the string $y$. For example: $combine[A; BC] = ABC$

There are three predicates on strings:
1. $char[x]$, $x$ is a single character.
2. $null[x]$, $x$ is the null string.
3. $x = y$, defined for $x$ and $y$ characters.
The advantage of linear LISP is that no characters are given special roles, as are parentheses, dots, and commas in LISP. This permits computations with all expressions that can be written linearly. The disadvantage of linear LISP is that the extraction of subexpressions is a fairly involved, rather than an elementary, operation. It is not hard to write, in linear LISP, functions that correspond to the basic functions of LISP, so that, mathematically, linear LISP includes LISP. This turns out to be the most convenient way of programming, in linear LISP, the more complicated manipulations. However, if the functions are to be represented by computer routines, LISP is essentially faster.
