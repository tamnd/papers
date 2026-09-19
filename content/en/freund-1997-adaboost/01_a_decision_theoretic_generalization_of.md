---
paper: freund-1997-adaboost
title: A Decision-Theoretic Generalization of On-Line Learning and an Application to Boosting
authors:
  - Yoav Freund
  - Robert E. Schapire
year: 1997
venue: Journal of Computer and System Sciences
field: ai-ml
section_title: A Decision-Theoretic Generalization of On-Line Learning and an Application to Boosting[^1]
kind: section
lang: en
source: https://doi.org/10.1006/jcss.1997.1504
pdf_sha256: 01f49de027c4c2c146869da85f8e8482d6b723344cb80ce957d11e93c615e7cc
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 4b99af66fc4766a1f8483232335ba5deadfdecfb2fe53b09cf1f67270924a191
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Yoav Freund and Robert E. Schapire[^2]

*AT&T Labs, 180 Park Avenue, Florham Park, New Jersey 07932*

Received December 19, 1996

In the first part of the paper we consider the problem of dynamically apportioning resources among a set of options in a worst-case on-line framework. The model we study can be interpreted as a broad, abstract extension of the well-studied on-line prediction model to a general decision-theoretic setting. We show that the multiplicative weight-update Littlestone–Warmuth rule can be adapted to this model, yielding bounds that are slightly weaker in some cases, but applicable to a considerably more general class of learning problems. We show how the resulting learning algorithm can be applied to a variety of problems, including gambling, multiple-outcome prediction, repeated games, and prediction of points in $\mathbb{R}^n$. In the second part of the paper we apply the multiplicative weight-update technique to derive a new boosting algorithm. This boosting algorithm does not require any prior knowledge about the performance of the weak learning algorithm. We also study generalizations of the new boosting algorithm to the problem of learning functions whose range, rather than being binary, is an arbitrary finite set or a bounded segment of the real line. © 1997 Academic Press
