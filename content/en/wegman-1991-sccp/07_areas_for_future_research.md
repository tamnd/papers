---
paper: wegman-1991-sccp
title: Constant Propagation with Conditional Branches
authors:
  - Mark N. Wegman
  - F. Kenneth Zadeck
year: 1991
venue: ACM TOPLAS
field: languages
section: "7"
section_title: AREAS FOR FUTURE RESEARCH
tag: 05D6
kind: section
lang: en
source: https://www.cs.utexas.edu/users/lin/cs380c/wegman.pdf
pdf_sha256: 40929436cdf1c477f2318221df5d0aa71488db4a01cc448b184e0aba8bf95ddb
pdf_pages: 27-28
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: e52b1c622c8ed819348177c2d6d4defe16a72ffbc5e13470c99fd038c9e16d5e
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

In Figure 14, a very simple form of type determination was performed. In LISP, it is thought sufficient to propagate the type of any assignment node forward: The information can be propagated in the same way as in the constant propagation problem. To get good information in SETL, the problem is somewhat harder. The goal is to infer the type of the object from the way in which it is used (this problem was originally defined by Tenenbaum [41]). SETL has only one primitive data type to program with, the set. Since sets are rather inefficient to implement, the SETL compiler attempts to pick a more efficient representation of an object on the basis of the way the object is used.

The problem is bidirectional, since the information about how a variable is used must be propagated backward as well as forward. Tenenbaum’s algorithm for doing this requires alternating forward and backward passes, with each pass done in a method similar to that of Kildall [26]. It may be possible to use a variation of the SSA graph to represent the propagation space. The chains must be bidirectional, that is, they must contain an edge from the use to the definition in addition to an edge from the definition to the use. There are many other details to be worked out, but this appears to be a straightforward extension of the ideas presented here.

In the range propagation problem [22, 24], the goal is to propagate ranges of values in an attempt to fix the upper and lower bounds of variables, so as to remove subscript range checking from areas of programs that can be proven safe. This problem differs from simple constant propagation in that the lattice may have an infinite number of levels, rather than just three. There are, however, subsets of this problem in which the number of lattice levels is small. For instance, in the problem of determining the possible values of a label variable in FORTRAN, the number of labels in a program is small and fixed. This type of problem should be easily solved by modifications to the algorithms presented here.

Arrays are difficult for almost any data flow analysis problem. The simple solution that is used in almost all implementations of optimizing compilers is to treat any assignment to an array as an assignment of $\perp$ unless that array is always indexed by constants. It may be possible to do something more sophisticated.

It is almost always desirable to integrate a function if all of the parameters are constant and the function references no global or free variables. Where only some parameters are constant, however, the decision is not so clear. Some benefit can be gained by unrolling loops and recursion if the space and time can be controlled by good heuristics. This problem has been investigated by Wegbreit [42], Ershov [18], Wegman [43], Appel and Jim [6], and Richardson and Ganapathi [36].

In this paper we have managed to combine constant propagation with unreachable code elimination and procedure integration. One of the open questions in compiler optimization is the proper order in which to apply the various optimizations. Some optimizations expose opportunities for other optimization techniques. We have eliminated the need to be concerned about the order of the optimizations we have combined and in the process have created a more powerful algorithm. It would be interesting to see if other techniques can be integrated in a similar manner.
