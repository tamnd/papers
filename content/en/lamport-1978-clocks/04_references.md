---
paper: lamport-1978-clocks
title: Time, Clocks, and the Ordering of Events in a Distributed System
authors:
  - Leslie Lamport
year: 1978
venue: Communications of the ACM
field: systems
section_title: References
tag: 093D
kind: references
lang: en
source: https://lamport.azurewebsites.net/pubs/time-clocks.pdf
pdf_sha256: c55e7cab4230aa3d7126748a149b2db6f0d7a67296d5eccfdd50a210299a96b2
pdf_pages: "8"
extraction: vision
extraction_model: gpt-5
content_sha256: 4ecf7908452a85c8b22b0b2cbcbec61e0ad87567c7e1b588974e84fa61b3d899
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

1. Schwartz, J.T. Relativity in Illustrations. New York U. Press, New York, 1962.
2. Taylor, E.F., and Wheeler, J.A. Space-Time Physics, W.H. Freeman, San Francisco, 1966.
3. Lamport, L. The implementation of reliable distributed multiprocess systems. To appear in Computer Networks.
4. Ellingson, C., and Kulpinski, R.J. Dissemination of system-time. IEEE Trans. Comm. Com-23, 5 (May 1973), 605–624.

Programming Languages
J. J. Horning Editor
Shallow Binding in Lisp 1.5
Henry G. Baker, Jr.
Massachusetts Institute of Technology

Shallow binding is a scheme which allows the value of a variable to be accessed in a bounded amount of computation. An elegant model for shallow binding in Lisp 1.5 is presented in which context-switching is an environment tree transformation called rerooting. Rerooting is completely general and reversible, and is optional in the sense that a Lisp 1.5 interpreter will operate correctly whether or not rerooting is invoked on every context change. Since rerooting leaves assoc [v, a] invariant, for all variables v and all environments a, the programmer can have access to a rerooting primitive, shallow[], which gives him dynamic control over whether accesses are shallow or deep, and which affects only the speed of execution of a program, not its semantics. In addition, multiple processes can be active in the same environment structure, so long as rerooting is an indivisible operation. Finally, the concept of rerooting is shown to combine the concept of shallow binding in Lisp with Dijkstra’s display for Algol and hence is a general model for shallow binding.

Key Words and Phrases: Lisp 1.5, environment trees, FUNARG’s, shallow binding, deep binding, multiprogramming, Algol display
CR Categories: 4.13, 4.22, 4.32

General permission to make fair use in teaching or research of all or part of this material is granted to individual readers and to nonprofit libraries acting for them provided that ACM’s copyright notice is given and that reference is made to the publication, to its date of issue, and to the fact that reprinting privileges were granted by permission of the Association for Computing Machinery. To otherwise reprint a figure, table, other substantial excerpt, or the entire work requires specific permission as does republication, or systematic or multiple reproduction.

This research was supported by the Advanced Research Projects Agency of the Department of Defense and was monitored by the Office of Naval Research under contract number N00014-75-C-0522.

Author’s present address: Computer Science Department, University of Rochester, Rochester, NY 14627.
© 1978 ACM 0001-0782/78/0700-0565 \$00.75

Communications of the ACM
July 1978
Volume 21
Number 7
