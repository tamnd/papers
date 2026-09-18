---
paper: hoare-1969-axiomatic
title: An Axiomatic Basis for Computer Programming
authors:
  - C. A. R. Hoare
year: 1969
venue: Communications of the ACM
field: languages
section: "4"
section_title: General Reservations
tag: "0319"
kind: section
lang: en
source: https://www.cs.cmu.edu/~crary/819-f09/Hoare69.pdf
pdf_sha256: f9b85de3537c0f1239cbe767cfd26ad49f2be07f0cc9021a6e46adfffb81dc12
pdf_pages: 3-4
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 4f721cd20e528e6c61d50b5aa92d32a8b2c8967d929f792101aa6cf476181acb
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The axioms and rules of inference quoted in this paper have implicitly assumed the absence of side effects of the evaluation of expressions and conditions. In proving properties of programs expressed in a language permitting side effects, it would be necessary to prove their absence in each case before applying the appropriate proof technique. If the main purpose of a high level programming language is to assist in the construction and verification of correct programs, it is doubtful whether the use of functional notation to call procedures with side effects is a genuine advantage.

Another deficiency in the axioms and rules quoted above is that they give no basis for a proof that a program successfully terminates. Failure to terminate may be due to an infinite loop; or it may be due to violation of an implementation-defined limit, for example, the range of numeric operands, the size of storage, or an operating system time limit. Thus the notation “$P\{Q\}R$” should be interpreted “provided that the program successfully terminates, the properties of its results are described by $R$.” It is fairly easy to adapt the axioms so that they cannot be used to predict the “results” of nonterminating programs; but the actual use of the axioms would now depend on knowledge of many implementation-dependent features, for example, the size and speed of the computer, the range of numbers, and the choice of overflow technique. Apart from proofs of the avoidance of infinite loops, it is probably better to prove the “conditional” correctness of a program and rely on an implementation to give a warning if it has had to abandon execution of the program as a result of violation of an implementation limit.

Finally it is necessary to list some of the areas which have not been covered: for example, real arithmetic, bit and character manipulation, complex arithmetic, fractional arithmetic, arrays, records, overlay definition, files, input/output, declarations, subroutines, parameters, recursion, and parallel execution. Even the characterization of integer arithmetic is far from complete. There does not appear to be any great difficulty in dealing with these points, provided that the programming language is kept simple. Areas which do present real difficulty are labels and jumps, pointers, and name parameters. Proofs of programs which made use of these features are likely to be elaborate, and it is not surprising that this should be reflected in the complexity of the underlying axioms.
