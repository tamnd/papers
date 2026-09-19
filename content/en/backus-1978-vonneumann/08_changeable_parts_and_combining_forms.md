---
paper: backus-1978-vonneumann
title: Can Programming Be Liberated from the von Neumann Style? A Functional Style and Its Algebra of Programs
authors:
  - John Backus
year: 1978
venue: Communications of the ACM (Turing Award lecture)
field: languages
section: "7"
section_title: Changeable Parts and Combining Forms
tag: "0565"
kind: section
lang: en
source: https://www.cs.cmu.edu/~crary/819-f09/Backus78.pdf
pdf_sha256: 2e412a7986c7fd1bdd060d90d035faa9ecc8a29675f99206c243da90954ca423
pdf_pages: 5-6
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 6734b979c77c3b645824facbdbb58d781e2e809de0b1c3384fda280d594582e4
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The second problem of von Neumann languages is that their changeable parts have so little expressive power. Their gargantuan size is eloquent proof of this; after all, if the designer knew that all those complicated features, which he now builds into the framework, could be added later on as changeable parts, he would not be so eager to build them into the framework.

Perhaps the most important element in providing powerful changeable parts in a language is the availability of combining forms that can be generally used to build new procedures from old ones. Von Neumann languages provide only primitive combining forms, and the von Neumann framework presents obstacles to their full use.

One obstacle to the use of combining forms is the split between the expression world and the statement world in von Neumann languages. Functional forms naturally belong to the world of expressions; but no matter how powerful they are they can only build expressions that produce a one-word result. And it is in the statement world that these one-word results must be combined into the overall result. Combining single words is not what we really should be thinking about, but it is a large part of programming any task in von Neumann languages. To help assemble the overall result from single words these languages provide some primitive combining forms in the statement world—the for, while, and if-then-else statements—but the split between the two worlds prevents the combining forms in either world from attaining the full power they can achieve in an undivided world.

A second obstacle to the use of combining forms in von Neumann languages is their use of elaborate naming conventions, which are further complicated by the substitution rules required in calling procedures. Each of these requires a complex mechanism to be built into the framework so that variables, subscripted variables, pointers, file names, procedure names, call-by-value formal parameters, call-by-name formal parameters, and so on, can all be properly interpreted. All these names, conventions, and rules interfere with the use of simple combining forms.
