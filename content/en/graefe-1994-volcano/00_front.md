---
paper: graefe-1994-volcano
title: Volcano - An Extensible and Parallel Query Evaluation System
authors:
  - Goetz Graefe
year: 1994
venue: IEEE Transactions on Knowledge and Data Engineering
field: databases
section_title: Front Matter
tag: "0058"
kind: front
lang: en
source: http://daslab.seas.harvard.edu/reading-group/papers/volcano.pdf
pdf_sha256: 61e9ce81f84d66797c95db711fb593adcf1dbbf95fea53eba44a9b9e2239d6ca
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: d798ba7281ca1a5f0e11bf8ed68db355aec57a4e597700119d847a7058bf3e2f
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Volcano—An Extensible and Parallel Query Evaluation System

Goetz Graefe

Abstract—To investigate the interactions of extensibility and parallelism in database query processing, we have developed a new dataflow query execution system called Volcano. The Volcano effort provides a rich environment for research and education in database systems design, heuristics for query optimization, parallel query execution, and resource allocation.

Volcano uses a standard interface between algebra operators, allowing easy addition of new operators and operator implementations. Operations on individual items, e.g., predicates, are imported into the query processing operators using support functions. The semantics of support functions is not prescribed; any data type including complex objects and any operation can be realized. Thus, Volcano is extensible with new operators, algorithms, data types, and type-specific methods.

Volcano includes two novel meta-operators. The choose-plan meta-operator supports dynamic query evaluation plans that allow delaying selected optimization decisions until run-time, e.g., for embedded queries with free variables. The exchange meta-operator supports intra-operator parallelism on partitioned datasets and both vertical and horizontal inter-operator parallelism, translating between demand-driven dataflow within processes and data-driven dataflow between processes.

All operators, with the exception of the exchange operator, have been designed and implemented in a single-process environment, and parallelized using the exchange operator. Even operators not yet designed can be parallelized using this new operator if they use and provide the interator interface. Thus, the issues of data manipulation and parallelism have become orthogonal, making Volcano the first implemented query execution engine that effectively combines extensibility and parallelism.

Index Terms—Dynamic query evaluation plans, extensible database systems, iterators, operator model of parallelization, query execution.
