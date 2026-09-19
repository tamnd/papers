---
paper: aho-1975-corasick
title: 'Efficient String Matching: An Aid to Bibliographic Search'
authors:
  - Alfred V. Aho
  - Margaret J. Corasick
year: 1975
venue: Communications of the ACM
field: algorithms
section: "7"
section_title: An Application to Bibliographic Search
tag: "0343"
kind: section
lang: en
source: https://cr.yp.to/bib/1975/aho.pdf
pdf_sha256: f04940c07d2a12726bce4147fd4217e876cd969ddf44094ad90c866893deed34
pdf_pages: 7-8
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 350346c30d9c4a502a4319bf40c5fa0d5a86a28f1a5f1ca5574d406e8091aa5d
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Algorithm 1 is attractive in pattern matching applications involving large numbers of keywords, since all keywords can be simultaneously matched against the text string in just one pass through the text string. One such application in which this algorithm has been successfully used arose in a library bibliographic search program which locates in a cumulative citation index all citations satisfying some Boolean function of keywords.

The data base used for this retrieval system is the cumulated machine-readable data used for Current Technical Papers, a fortnightly citation bulletin produced for internal use by the technical libraries of Bell Laboratories. These citations are gathered from journals, covering a broad classification of technical interests. In the summer of 1973 there were three years of cumulated data, representing about 150,000 citations with a total length of about $10^7$ characters.

With this search system a bibliographer can retrieve from the data base all titles satisfying some Boolean combination of keywords. For example, the bibliographer can ask for all titles in the data base containing both the keywords “ion” and “bombardment.” The bibliographer can also specify whether a keyword is required to be preceded and/or followed by a punctuation character such as space, comma, semicolon, etc. A specification of this nature can explicitly deny matching on keywords embedded in the text. For example, it is often reasonable to accept the word “ions” as a match for the substring “ion.” However, it is usually unreasonable to accept a word such as “motion” as a match on that keyword. The implementation permits specification of acceptance with full embedding, left embedding, right embedding, or none at all. This provision creates no difficulty for Algorithm 1 although the use of a class of punctuation characters in the keyword syntax creates some states with a large number of goto transitions. This may make the deterministic finite automaton implementation of Algorithm 1 more space consuming and less attractive for some applications.

An early version of this bibliographic search program employed a direct pattern matching algorithm in which each keyword in the search prescription was successively matched against each title. A second version of this search program was implemented, also in FORTRAN, in which the only difference was the substitution of Algorithms 1, 2 and 3 for the direct pattern matching scheme. The following table shows two sample runs of the two programs on a Honeywell 6070 computer. The first run involved a search prescription containing 15 keywords, the second a search prescription containing 24 keywords.

|  | 15 keywords | 24 keywords |
| --- | --- | --- |
| old | .79 | 1.27 |
| new | .18 | .21 |

CPU Time in Hours

With larger numbers of keywords the improvement in performance became even more pronounced. The figures tend to bear out the fact that with Algorithm 1 the cost of a search is roughly independent of the number of keywords. The time spent in constructing the pattern matching machine and making state transitions was insignificant compared to the time spent reading and unpacking the text string.
