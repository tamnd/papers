---
paper: shamir-1992-ippspace
title: IP = PSPACE
authors:
  - Adi Shamir
year: 1992
venue: Journal of the ACM
field: theory
section: "1"
section_title: Introduction
tag: 052E
kind: section
lang: en
source: http://crypto.cs.mcgill.ca/~crepeau/COMP647/2007/
pdf_sha256: 64e55264e8386142cd8821ddccb435579ecd13a50658047d488011145d5a405f
pdf_pages: 1-2
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 661a8c747c53fc6d30df1423b9466e07c9d5cb43b4e96e1dd1f24e7de547871f
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The class IP of languages that have efficient interactive proofs of membership was introduced by Goldwasser et al. [[goldwasser-1985-zk]], and in a slightly different form by Babai [1] (the equivalence between these models was established by Goldwasser and Sipser [7]). A language $L$ belongs to IP if a probabilistic polynomial time verifier $V$ can be convinced by some prover $P$ to accept any $x \in L$ with overwhelming probability, but cannot be convinced by any prover $P'$ to accept any $x \notin L$ with a nonnegligible probability. Goldreich et al. [6] showed that IP contains some languages believed not to be in NP, but its exact characterization remained a major open problem for several years. In a breakthrough paper, Lund et al. [10] made ingenious use of earlier results by Valiant [12], Toda [11] Beaver and Feigenbaum [2] and Lipton [9] to prove that IP contains the polynomial hierarchy PH. In this paper, we use surprisingly simple techniques to extend the previous results and prove that IP contains PSPACE. Since every IP language is trivially accepted by the PSPACE machine that traverses the tree of all the possible interactions, this result completely characterizes IP.

The interactive proofs introduced in this paper use only public coins, are accepted with probability 1 when the prover is honest, and require only logarithmic workspace when the verifier is given a 2-way access to his random

Author’s address: Applied Mathematics Department, The Weizmann Institute of Science, Rehovot, Israel.
Permission to copy without fee all or part of this material is granted provided that the copies are not made or distributed for direct commercial advantage, the ACM copyright notice and the title of the publication and its date appear, and notice is given that copying is by permission of the Association for Computing Machinery. To copy otherwise, or to republish, requires a fee and/or specific permission.
© 1992 ACM 0004-5411/92/1000–0869 \$01.50 tape. They can be turned into zero knowledge proofs under the sole assumption that one-way functions exist by using known techniques.
