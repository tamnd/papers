---
paper: knuth-1977-kmp
title: Fast Pattern Matching in Strings
authors:
  - Donald E. Knuth
  - James H. Morris Jr.
  - Vaughan R. Pratt
year: 1977
venue: SIAM Journal on Computing
field: algorithms
section_title: Front Matter
tag: "0044"
kind: front
lang: en
source: https://www.cs.jhu.edu/~misha/ReadingSeminar/Papers/Knuth77.pdf
pdf_sha256: cf3391d85e2456f8242a3dc4a88e7cdead9a419b52890bb4b8a31433e9659dcb
pdf_pages: 1-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 60ce63ba3d84477d570209bf28278eaed833668a8bc0ad505f60de5046d621c3
prompt_sha256: 329630a0b9175a55e4af1b8e281a3e67eeab250f8d643953b7dcde99743c7628
---

FAST PATTERN MATCHING IN STRINGS*

DONALD E. KNUTH†, JAMES H. MORRIS, JR.‡ AND VAUGHAN R. PRATT¶

Abstract. An algorithm is presented which finds all occurrences of one given string within another, in running time proportional to the sum of the lengths of the strings. The constant of proportionality is low enough to make this algorithm of practical use, and the procedure can also be extended to deal with some more general pattern-matching problems. A theoretical application of the algorithm shows that the set of concatenations of even palindromes, i.e., the language $\{\alpha\alpha^R\}^*$, can be recognized in linear time. Other algorithms which run even faster on the average are also considered.

Key words. pattern, string, text-editing, pattern-matching, trie memory, searching, period of a string, palindrome, optimum algorithm, Fibonacci string, regular expression

Text-editing programs are often required to search through a string of characters looking for instances of a given “pattern” string; we wish to find all positions, or perhaps only the leftmost position, in which the pattern occurs as a contiguous substring of the text. For example, $c a t e n a r y$ contains the pattern $t e n$, but we do not regard $c a n a r y$ as a substring.

The obvious way to search for a matching pattern is to try searching at every starting position of the text, abandoning the search as soon as an incorrect character is found.
