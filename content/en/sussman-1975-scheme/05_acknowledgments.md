---
paper: sussman-1975-scheme
title: 'Scheme: An Interpreter for Extended Lambda Calculus'
authors:
  - Gerald Jay Sussman
  - Guy L. Steele Jr.
year: 1975
venue: MIT AI Memo 349
field: languages
section_title: Acknowledgments
kind: section
lang: en
source: https://dspace.mit.edu/server/api/core/bitstreams/70ab0fe6-0e7a-41ef-99fb-ac2c9481a05e/content
pdf_sha256: c2961e078943a26ae1f752b202290f561578b7ecf8b24b8929e3c1f99e6b2c52
pdf_pages: "41"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 2359256159b773615af15defc46cd022af6705809b42bdb2509b102344c38479
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

This paper would not have happened if Sussman had not been forced to think about lambda calculus by having to teach 6.031, nor would it have happened had not Steele been forced to understand PLASMA by morbid curiosity.

This work developed out of an initial attempt to understand the actorness of actors. Steele thought he understood it, but couldn't explain it; Sussman suggested the experimental approach of actually building an "ACTORS interpreter". This interpreter attempted to intermix the use of actors and LISP lambda expressions in a clean manner. When it was completed, we discovered that the "actors" and the lambda expressions were identical in implementation. Once we had discovered this, all the rest fell into place, and it was only natural to begin thinking about actors in terms of lambda calculus. The original interpreter was call-by-name for various reasons having to do with 6.031; we subsequently experimentally discovered how call-by-name screws iteration, and rewrote it to use call-by-value. Note well that we did not bring forth a clean implementation in one brilliant flash of understanding; we used an experimental and highly empirical approach to bootstrap our knowledge.

We wish to thank the staff of 6.031, Mike Dertouzos, and Steve Ward, for precipitating this intellectual adventure. Carl Hewitt spent many hours explaining the innards and outards of PLASMA to Steele over the course of several months; Marilyn McClennan was also helpful in this respect. Brian Smith and Richard Zippel helped a lot. We wish to thank Seymour Papert, Ben Kuipers, Marvin Minsky, and Vaughn Pratt for their excellent suggestions.
