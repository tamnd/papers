---
paper: graefe-1994-volcano
title: Volcano - An Extensible and Parallel Query Evaluation System
authors:
  - Goetz Graefe
year: 1994
venue: IEEE Transactions on Knowledge and Data Engineering
field: databases
section_title: Front Matter
kind: front
lang: en
source: http://daslab.seas.harvard.edu/reading-group/papers/volcano.pdf
pdf_sha256: 61e9ce81f84d66797c95db711fb593adcf1dbbf95fea53eba44a9b9e2239d6ca
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: f3f5216d0b9ee8e1b96dbdbc385a4acb4d80a53b9dc3b71ce8d91c9a06d95e85
prompt_sha256: 329630a0b9175a55e4af1b8e281a3e67eeab250f8d643953b7dcde99743c7628
---

Volcano—An Extensible and Parallel Query Evaluation System

Goetz Graefe

Abstract—To investigate the interactions of extensibility and parallelism in database query processing, we have developed a new dataflow query execution system called Volcano. The Volcano effort provides a rich environment for research and education in database systems design, heuristics for query optimization, parallel query execution, and resource allocation.

Volcano uses a standard interface between algebra operators, allowing easy addition of new operators and operator implementations. Operations on individual items, e.g., predicates, are imported into the query processing operators using support functions. The semantics of support functions is not prescribed; any data type including complex objects and any operation can be realized. Thus, Volcano is extensible with new operators, algorithms, data types, and type-specific methods.

Volcano includes two novel meta-operators. The choose-plan meta-operator supports dynamic query evaluation plans that allow delaying selected optimization decisions until run-time, e.g., for embedded queries with free variables. The exchange meta-operator supports intra-operator parallelism on partitioned datasets and both vertical and horizontal inter-operator parallelism, translating between demand-driven dataflow within processes and data-driven dataflow between processes.

All operators, with the exception of the exchange operator, have been designed and implemented in a single-process environment, and parallelized using the exchange operator. Even operators not yet designed can be parallelized using this new operator if they use and provide the interator interface. Thus, the issues of data manipulation and parallelism have become orthogonal, making Volcano the first implemented query execution engine that effectively combines extensibility and parallelism.
