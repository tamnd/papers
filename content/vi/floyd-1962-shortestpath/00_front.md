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
content_sha256: 366da5561c78c97d3387d490fdd59c647640b234e3d6b581708911971272151d
translated_from: content/en/floyd-1962-shortestpath/00_front.md
source_content_sha256: f47988721e3f52c695a4436975c6c5a774afc02420dba6c78d793c8f8e5a7703
translation_model: gpt-5
translation_run: 20260915T053248Z
glossary_version: 6
glossary_terms_sha256: 51f62d367854beec600f51894702ad34dfcde96c993d5c00a2f7a9873047d13f
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

Các đóng góp cho bộ phận này phải ở dạng được nêu trong tuyên bố chính sách của Bộ phận Thuật toán (Communications, February, 1960), ngoại trừ việc phải sử dụng ký hiệu ALGOL 60 (xem Communications, May 1960). Các đóng góp phải được gửi thành hai bản đến J. H. Wegstein, Computation Laboratory, National Bureau of Standards, Washington 25, D. C. Các thuật toán phải ở dạng Tham chiếu của ALGOL 60 và được viết theo phong cách dựa trên các thuật toán gần đây nhất xuất hiện trong bộ phận này.
