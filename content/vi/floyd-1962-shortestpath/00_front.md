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
lang: vi
source: https://web.archive.org/web/20200531072111id_/https://dl.acm.org/doi/pdf/10.1145/367766.368168?download=true
pdf_sha256: fd7424d2a47593223e2b490e841613bd900bc140944cb4eb590cff0e529886a2
pdf_pages: "2"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 1eac948a846b2617f5e619297b8ac6fd374b9ea6bd3ad8e22906c6aa24e29f99
translated_from: content/en/floyd-1962-shortestpath/00_front.md
source_content_sha256: f47988721e3f52c695a4436975c6c5a774afc02420dba6c78d793c8f8e5a7703
translation_model: gpt-5
translation_run: 20260918T122832Z
glossary_version: 7
glossary_terms_sha256: d4043ebd5a5c828b0239f76956644bfb5bb815f3188dc3282d75521c97669214
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

THUẬT TOÁN 97

ĐƯỜNG ĐI NGẮN NHẤT

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

Các đóng góp cho bộ phận này phải có dạng được nêu trong tuyên bố chính sách của Bộ phận Thuật toán (Communications, February, 1960), ngoại trừ việc phải sử dụng ký hiệu ALGOL 60 (xem Communications, May 1960). Các đóng góp phải được gửi thành hai bản cho J. H. Wegstein, Computation Laboratory, National Bureau of Standards, Washington 25, D. C. Các thuật toán phải ở dạng Reference của ALGOL 60 và được viết theo phong cách mô phỏng các thuật toán gần đây nhất xuất hiện trong bộ phận này.
