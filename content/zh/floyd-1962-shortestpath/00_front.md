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
lang: zh
source: https://web.archive.org/web/20200531072111id_/https://dl.acm.org/doi/pdf/10.1145/367766.368168?download=true
pdf_sha256: fd7424d2a47593223e2b490e841613bd900bc140944cb4eb590cff0e529886a2
pdf_pages: "2"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: d1e2088eef14a92d4f40b95067d8cb03417b7d48398101c9d6530bd9410683ec
translated_from: content/en/floyd-1962-shortestpath/00_front.md
source_content_sha256: 04f30dab59a71d7a283f24b36d558f2574d62d8850b1b9bcf3c3800fa097fada
translation_model: gpt-5
translation_run: 20260915T022550Z
glossary_version: 6
glossary_terms_sha256: efacc7653691a9b863e3c4cb746743abfecf7d31e7791764c13a541e1906db0f
prompt_sha256: da0c2696badfbe5d93fdc534847b1b0ca3b25ec37e0ce29843665f6e701c278e
---

ALGORITHM 97

最短路径

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

本部门的投稿必须采用《算法部门政策声明》（Communications，1960年2月）中规定的形式，但应使用ALGOL 60表示法（参见Communications，1960年5月）。投稿应一式两份寄送至J. H. Wegstein，Computation Laboratory，National Bureau of Standards，Washington 25, D. C.。算法应采用ALGOL 60的Reference形式，并以本部门最近发表的算法所采用的风格撰写。
