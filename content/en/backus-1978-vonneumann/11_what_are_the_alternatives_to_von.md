---
paper: backus-1978-vonneumann
title: Can Programming Be Liberated from the von Neumann Style? A Functional Style and Its Algebra of Programs
authors:
  - John Backus
year: 1978
venue: Communications of the ACM (Turing Award lecture)
field: languages
section: "10"
section_title: What Are the Alternatives to von Neumann Languages?
tag: "0568"
kind: section
lang: en
source: https://www.cs.cmu.edu/~crary/819-f09/Backus78.pdf
pdf_sha256: 2e412a7986c7fd1bdd060d90d035faa9ecc8a29675f99206c243da90954ca423
pdf_pages: "7"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: f5296bef2bf7a321a2962bcf1d32ce6d7e9c691fa15b5c315aed8f9cd3a4a56c
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Before discussing alternatives to von Neumann languages, let me remark that I regret the need for the above negative and not very precise discussion of these languages. But the complacent acceptance most of us give to these enormous, weak languages has puzzled and disturbed me for a long time. I am disturbed because that acceptance has consumed a vast effort toward making von Neumann languages fatter that might have been better spent in looking for new structures. For this reason I have tried to analyze some of the basic defects of conventional languages and show that those defects cannot be resolved unless we discover a new kind of language framework.

In seeking an alternative to conventional languages we must first recognize that a system cannot be history-sensitive (permit execution of one program to affect the behavior of a subsequent one) unless the system has some kind of state (which the first program can change and the second can access). Thus a history-sensitive model of a computing system must have a state-transition semantics, at least in this weak sense. But this does not mean that every computation must depend heavily on a complex state, with many state changes required for each small part of the computation (as in von Neumann languages).

To illustrate some alternatives to von Neumann languages, I propose to sketch a class of history-sensitive computing systems, where each system: a) has a loosely coupled state-transition semantics in which a state transition occurs only once in a major computation; b) has a simply structured state and simple transition rules; c) depends heavily on an underlying applicative system both to provide the basic programming language of the system and to describe its state transitions.

These systems, which I call applicative state transition (or AST) systems, are described in Section 14. These simple systems avoid many of the complexities and weaknesses of von Neumann languages and provide for a powerful and extensive set of changeable parts. However, they are sketched only as crude examples of a vast area of non-von Neumann systems with various attractive properties. I have been studying this area for the past three or four years and have not yet found a satisfying solution to the many conflicting requirements that a good language must resolve. But I believe this search has indicated a useful approach to designing non-von Neumann languages.

This approach involves four elements, which can be summarized as follows.

a) *A functional style of programming without variables.* A simple, informal functional programming (FP) system is described. It is based on the use of combining forms for building programs. Several programs are given to illustrate functional programming.

b) *An algebra of functional programs.* An algebra is described whose variables denote FP functional programs and whose “operations” are FP functional forms, the combining forms of FP programs. Some laws of the algebra are given. Theorems and examples are given that show how certain function expressions may be transformed into equivalent infinite expansions that explain the behavior of the function. The FP algebra is compared with algebras associated with the classical applicative systems of Church and Curry.

c) *A formal functional programming system.* A formal (FFP) system is described that extends the capabilities of the above informal FP systems. An FFP system is thus a precisely defined system that provides the ability to use the functional programming style of FP systems and their algebra of programs. FFP systems can be used as the basis for applicative state transition systems.

d) *Applicative state transition systems.* As discussed above. The rest of the paper describes these four elements, gives some brief remarks on computer design, and ends with a summary of the paper.
