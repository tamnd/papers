---
paper: verma-2015-borg
title: Large-scale cluster management at Google with Borg
authors:
  - Abhishek Verma
  - Luis Pedrosa
  - Madhukar Korupolu
  - David Oppenheimer
  - Eric Tune
  - John Wilkes
year: 2015
venue: EuroSys
field: systems
section_title: Background
kind: appendix
lang: en
source: https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/43438.pdf
pdf_sha256: 2fdacd3b69f8af91477412fc91d1d858a43e764929a4edb646bd517ededdad94
pdf_pages: "18"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: a2f123b138aadcca88f269d9d84f8a553960959f7c31b811d93e4426c6d6e532
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Borg leveraged much from its internal predecessor, the Global Work Queue system, which was initially developed by Jeff Dean, Olcan Sercinoglu, and Percy Liang.

Condor [1] has been widely used for aggregating collections of idle resources, and its ClassAds mechanism [2] supports declarative statements and automated attribute/property matching.
