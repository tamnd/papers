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
lang: ja
source: https://web.archive.org/web/20200531072111id_/https://dl.acm.org/doi/pdf/10.1145/367766.368168?download=true
pdf_sha256: fd7424d2a47593223e2b490e841613bd900bc140944cb4eb590cff0e529886a2
pdf_pages: "2"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: a9c03f37269112c2b6d3c8dddc02e5d3913d917df36932d274e6db925cb61899
translated_from: content/en/floyd-1962-shortestpath/00_front.md
source_content_sha256: 04f30dab59a71d7a283f24b36d558f2574d62d8850b1b9bcf3c3800fa097fada
translation_model: gpt-5
translation_run: 20260915T022550Z
glossary_version: 6
glossary_terms_sha256: 81be60ea3284bdc3129ecda2524a99e799d0b3ec06fd0a74a1fb3922eda78382
prompt_sha256: 28abc9ae7c2a46d63213afc528700760d76ff5866e775238c90c95b3052a886f
---

アルゴリズム 97

最短経路

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

この部門への投稿は、ALGOL 60の表記法を使用することを除き、Algorithms Department policy statement (Communications, February, 1960) に記載された形式でなければならない（Communications, May 1960を参照）。投稿は2部を J. H. Wegstein, Computation Laboratory, National Bureau of Standards, Washington 25, D. C. に送付する必要がある。アルゴリズムはALGOL 60のReference形式であり、この部門に掲載された直近のアルゴリズムを手本としたスタイルで記述されなければならない。
