---
paper: graefe-1994-volcano
title: Volcano - An Extensible and Parallel Query Evaluation System
authors:
  - Goetz Graefe
year: 1994
venue: IEEE Transactions on Knowledge and Data Engineering
field: databases
section: V
section_title: DYNAMIC QUERY EVALUATION PLANS
tag: "0473"
kind: section
lang: en
source: http://daslab.seas.harvard.edu/reading-group/papers/volcano.pdf
pdf_sha256: 61e9ce81f84d66797c95db711fb593adcf1dbbf95fea53eba44a9b9e2239d6ca
pdf_pages: "10"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 653100896927b5bfe1781a297487439b0da2fb1169490e1df80dba57c470eb28
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

In most database systems, a query embedded in a program written in a conventional programming language is optimized when the program is compiled. The query optimizer must make assumptions about the values of the program variables that appear as constants in the query and the data in the database. These assumptions include that the query can be optimized realistically using guessed "typical" values for the program variables and that the database will not change significantly between query optimization and query evaluation. The optimizer must also anticipate the resources that can be committed to query evaluation, e.g., the size of the buffer or the number of processors. The optimality of the resulting query evaluation plan depends on the validity of these assumptions. If a query evaluation plan is used repeatedly over an extended period of time, it is important to determine when reoptimization is necessary. We are working on a scheme in which reoptimization can be avoided by using a new technique called dynamic query evaluation plans [17].¹

Volcano includes a choose-plan operator that allows realization of both multiplan access modules and dynamic plans. In some sense, it is not an operator as it does not perform any data manipulations. Since it provides control for query execution it is a meta-operator. This operator provides the same open-next-close protocol as the other operators and can therefore be inserted into a query plan at any location. The open operation decides which of several equivalent query plans to use and invokes the open operation for this input. Open calls upon a support function for this policy decision, passing it the bindings parameter described above. The next and close operations simply call the appropriate operation for the input chosen during open.

Fig. 4 shows a very simple dynamic plan. Imagine a selection predicate controlled by a program variable. The

¹This section is a brief summary of [17].

Print
|
Choose-Plan
/

\
Functional Join      File Scan
    |
Index Scan index scan and functional join can be much faster than the file scan, but not when the index is nonclustering and a large number of items must be retrieved. Using the plan of Fig. 4, however, the optimizer can prepare effectively for both cases, and the application program using this dynamic plan will perform well for any predicate value.

Fig. 4. A dynamic query evaluation plan. {#graefe-1994-volcano-fig-4 .figure tag=0474}

The choose-plan operator allows considerable flexibility. If only one choose-plan operator is used as the top of a query evaluation plan, it implements a multiplan access module. If multiple choose-plan operators are included in a plan, they implement a dynamic query evaluation plan. Thus, all forms of dynamic plans identified in [17] can be realized with one simple and effective mechanism. Note that the choose-plan operator does not make the policy decision concerning which of several plans to execute; it only provides the mechanism. The policy is imported using a support function. Thus, the decision can be made depending on bindings for query variables (e.g., program variables used as constants in a query predicate), on the resource and contention situation (e.g., the availability of processors and memory), other considerations such as user priority, or all of the above.

The choose-plan operator provides significant new freedom in query optimization and evaluation with an extremely small amount of code. Since it is compatible with the query processing paradigm, its presence does not affect the other operators at all, and it can be used in a very flexible way. The operator is another example for Volcano's design principle to provide mechanisms to implement a multitude of policies. We used the same philosophy when designing and implementing a scheme for parallel query evaluation.
