---
paper: floyd-1962-shortestpath
title: 'Algorithm 97: Shortest Path'
authors:
  - Robert W. Floyd
year: 1962
venue: Communications of the ACM
field: algorithms
section_title: Front Matter
tag: 003F
kind: front
lang: en
source: https://web.archive.org/web/20200531072111id_/https://dl.acm.org/doi/pdf/10.1145/367766.368168?download=true
pdf_sha256: fd7424d2a47593223e2b490e841613bd900bc140944cb4eb590cff0e529886a2
pdf_pages: "2"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: f47988721e3f52c695a4436975c6c5a774afc02420dba6c78d793c8f8e5a7703
edited: true
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

ALGORITHM 97

SHORTEST PATH

ROBERT W. FLOYD

Armour Research Foundation, Chicago, Ill.

```algol
procedure shortest path (m, n); value n; integer n; array m;
comment Initially m[i, j] is the length of a direct link from point i of a network to point j. If no direct link exists, m[i, j] is initially 1010. At completion, m[i, j] is the length of the shortest path from i to j. If none exists, m[i, j] is 1010. Reference: Warshall, S. A theorem on Boolean matrices. J.ACM 9(1962), 11-12;
begin
  integer i, j, k; real inf, s; inf := 1010;
  for i := 1 step 1 until n do
    for j := 1 step 1 until n do
      if m[j, i] < inf then
        for k := 1 step 1 until n do
          if m[i, k] < inf then
            begin s := m[j, i] + m[i, k];
              if s < m[j, k] then m[j, k] := s
            end
end shortest path
```

Contributions to this department must be in the form stated in the Algorithms Department policy statement (Communications, February, 1960) except that ALGOL 60 notation should be used (see Communications, May 1960). Contributions should be sent in duplicate to J. H. Wegstein, Computation Laboratory, National Bureau of Standards, Washington 25, D. C. Algorithms should be in the Reference form of ALGOL 60 and written in a style patterned after the most recent algorithms appearing in this department.
