---
paper: hoare-1969-axiomatic
title: An Axiomatic Basis for Computer Programming
authors:
  - C. A. R. Hoare
year: 1969
venue: Communications of the ACM
field: languages
section: "6"
section_title: Formal Language Definition
tag: 031B
kind: section
lang: en
source: https://www.cs.cmu.edu/~crary/819-f09/Hoare69.pdf
pdf_sha256: f9b85de3537c0f1239cbe767cfd26ad49f2be07f0cc9021a6e46adfffb81dc12
pdf_pages: "5"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 272d30131ccc8ace798dd1a74e9241b9c99dd65be6898b210f75d4122e6e3d6b
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

A high level programming language, such as Algol, Fortran, or Cobol, is usually intended to be implemented on a variety of computers of differing size, configuration, and design. It has been found a serious problem to define these languages with sufficient rigour to ensure compatibility among all implementors. Since the purpose of compatibility is to facilitate interchange of programs expressed in the language, one way to achieve this would be to insist that all implementations of the language shall "satisfy" the axioms and rules of inference which underlie proofs of the properties of programs expressed in the language, so that all predictions based on these proofs will be fulfilled, except in the event of hardware failure. In effect, this is equivalent to accepting the axioms and rules of inference as the ultimately definitive specification of the meaning of the language.

Apart from giving an immediate and possibly even provable criterion for the correctness of an implementation, the axiomatic technique for the definition of programming language semantics appears to be like the formal syntax of the Algol 60 report, in that it is sufficiently simple to be understood both by the implementor and by the reasonably sophisticated user of the language. It is only by bridging this widening communication gap in a single document (perhaps even provably consistent) that the maximum advantage can be obtained from a formal language definition.

Another of the great advantages of using an axiomatic approach is that axioms offer a simple and flexible technique for leaving certain aspects of a language undefined, for example, range of integers, accuracy of floating point, and choice of overflow technique. This is absolutely essential for standardization purposes, since otherwise the language will be impossible to implement efficiently on differing hardware designs. Thus a programming language standard should consist of a set of axioms of universal applicability, together with a choice from a set of supplementary axioms describing the range of choices facing an implementor. An example of the use of axioms for this purpose was given in Section 2.

Another of the objectives of formal language definition is to assist in the design of better programming languages. The regularity, clarity, and ease of implementation of the Algol 60 syntax may at least in part be due to the use of an elegant formal technique for its definition. The use of axioms may lead to similar advantages in the area of "semantics," since it seems likely that a language which can

(Continued on p. 583)
