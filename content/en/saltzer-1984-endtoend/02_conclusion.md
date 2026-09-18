---
paper: saltzer-1984-endtoend
title: End-To-End Arguments in System Design
authors:
  - J. H. Saltzer
  - D. P. Reed
  - D. D. Clark
year: 1984
venue: ACM TOCS
field: systems
section_title: Conclusion
kind: section
lang: en
source: https://doi.org/10.1145/357401.357402
pdf_sha256: 3204a1a562d9d3b72ba112f20caddfd34991d6e1e39939ace6a3e7c016519768
pdf_pages: "9"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 9d08616cc31d8636249d8f67b6d5ff931e5662a8434f120a1ca3e27cb32c8008
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

End-to-end arguments are a kind of "Occam's razor" when it comes to choosing the functions to be provided in a communication subsystem. Because the communication subsystem is frequently specified before applications that use the subsystem are known, the designer may be tempted to "help" the users by taking on more function than necessary. Awareness of end-to-end arguments can help to reduce such temptations.

It is fashionable these days to talk about "layered" communication protocols, but without clearly defined criteria for assigning functions to layers. Such layerings are desirable to enhance modularity. End-to-end arguments may be viewed as part of a set of rational principles for organizing such layered systems. We hope that our discussion will help to add substance to arguments about the "proper" layering.
