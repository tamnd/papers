---
paper: dijkstra-1968-the
title: The Structure of the "THE"-Multiprogramming System
authors:
  - Edsger W. Dijkstra
year: 1968
venue: Communications of the ACM
field: systems
section_title: Conclusion
kind: section
lang: en
source: https://www.cs.utexas.edu/users/EWD/ewd01xx/EWD196.PDF
pdf_sha256: 05061e836d9d7834f57f85cb06ed5fbea6c5726b0fd4ed2c4ca38d78ac1802d0
pdf_pages: "11"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 6edd00f51991d5baac886c227b148cd93dd896a46802af8d40d182b5e23a35b0
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

As far as program verification is concerned I present nothing essentially new. In testing a general purpose object (be it a piece of hardware, a program, a machine or a system) one cannot subject it to all possible cases: for a computer this would imply that one feeds it with all possible programs! Therefore one must test it with a set of relevant test cases. What is relevant or not, cannot be decided as long as one regards the mechanism as a black box, in other words it has to follow from the internal structure of the mechanism to be tested. It seems the designer's responsibility to construct his mechanism in such a way - i.e. so highly structured - that at each stage of the testing procedure the number of relevant test cases is so small that he can try them all and that what is being tested is so perspicuous that it is clear that he has not overlooked a situation. I have presented a survey of our system because I think it a nice example of the form such a structure might take.

In my experience, I am sorry to say, industrial software makers tend to react to it with mixed feelings. On the one hand they are inclined to judge that we have done a kind of model job, on the other hand they express doubts whether the techniques used are applicable outside the sheltered atmosphere of a University Department and express the opinion that we could only do it this way thanks to the modest scope of the whole project. It is not my intention to underestimate the organizing ability needed for a much bigger job with ten or more times as many people, but I should like to venture the opinion that the larger the project, the more essential the structuring! A hierarchy of five logical levels might then very well turn out to be of modest depth, in particular when one designs the system more consciously than we have done with the aim that the software can be smoothly adapted to (perhaps drastic) configuration expansions.
