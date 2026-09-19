---
paper: backus-1978-vonneumann
title: Can Programming Be Liberated from the von Neumann Style? A Functional Style and Its Algebra of Programs
authors:
  - John Backus
year: 1978
venue: Communications of the ACM (Turing Award lecture)
field: languages
section: "1"
section_title: 'Conventional Programming Languages: Fat and Flabby'
tag: 041B
kind: section
lang: en
source: https://www.cs.cmu.edu/~crary/819-f09/Backus78.pdf
pdf_sha256: 2e412a7986c7fd1bdd060d90d035faa9ecc8a29675f99206c243da90954ca423
pdf_pages: "2"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: ae61093d0ac084da9238d0dcbc70e1915136e0fe210b010f6d90eae155298db6
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Programming languages appear to be in trouble. Each successive language incorporates, with a little cleaning up, all the features of its predecessors plus a few more. Some languages have manuals exceeding 500 pages; others cram a complex description into shorter manuals by using dense formalisms. The Department of Defense has current plans for a committee-designed language standard that could require a manual as long as 1,000 pages. Each new language claims new and fashionable features, such as strong typing or structured control statements, but the plain fact is that few languages make programming sufficiently cheaper or more reliable to justify the cost of producing and learning to use them.

Since large increases in size bring only small increases in power, smaller, more elegant languages such as Pascal continue to be popular. But there is a desperate need for a powerful methodology to help us think about programs, and no conventional language even begins to meet that need. In fact, conventional languages create unnecessary confusion in the way we think about programs.

For twenty years programming languages have been steadily progressing toward their present condition of obesity; as a result, the study and invention of programming languages has lost much of its excitement. Instead, it is now the province of those who prefer to work with thick compendia of details rather than wrestle with new ideas. Discussions about programming languages often resemble medieval debates about the number of angels that can dance on the head of a pin instead of exciting contests between fundamentally differing concepts.

Many creative computer scientists have retreated from inventing languages to inventing tools for describing them. Unfortunately, they have been largely content to apply their elegant new tools to studying the warts and moles of existing languages. After examining the appalling type structure of conventional languages, using the elegant tools developed by Dana Scott, it is surprising that so many of us remain passively content with that structure instead of energetically searching for new ones.

The purpose of this article is twofold; first, to suggest that basic defects in the framework of conventional languages make their expressive weakness and their cancerous growth inevitable, and second, to suggest some alternate avenues of exploration toward the design of new kinds of languages.
