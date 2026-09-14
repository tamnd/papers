---
paper: corbett-2012-spanner
title: 'Spanner: Google''s Globally-Distributed Database'
authors:
  - James C. Corbett
  - Jeffrey Dean
  - Michael Epstein
  - Andrew Fikes
  - Christopher Frost
  - J. J. Furman
  - Sanjay Ghemawat
  - Andrey Gubarev
  - Christopher Heiser
  - Peter Hochschild
year: 2012
venue: OSDI
field: databases
section_title: Front Matter
tag: 009F
kind: front
lang: vi
source: http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.258.9924
pdf_sha256: 61875779e75f603d21aefba6d9bd9816d4dd0c18cf41089f43707249e24bbf88
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 203db0dc8a4b493a87123fd7d8b1bf22e366484d5fd25ff25b1c5f03dfed9409
translated_from: content/en/corbett-2012-spanner/00_front.md
source_content_sha256: 68098eadaf65622855b7119b7a6daeca60c4123bebc9c5d67503da7aa7b00a01
translation_model: gpt-5
translation_run: 20260914T163737Z
glossary_version: 6
glossary_terms_sha256: a534ae50d60bff0e03804fd3c150e37d1876484531ab87df9c72dc4d0c455eb2
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
roundtrip: same
roundtrip_run: 20260914T214350Z
---

Spanner: Cơ sở dữ liệu phân tán toàn cầu của Google

James C. Corbett, Jeffrey Dean, Michael Epstein, Andrew Fikes, Christopher Frost, JJ Furman, Sanjay Ghemawat, Andrey Gubarev, Christopher Heiser, Peter Hochschild, Wilson Hsieh, Sebastian Kanthak, Eugene Kogan, Hongyi Li, Alexander Lloyd, Sergey Melnik, David Mwaura, David Nagle, Sean Quinlan, Rajesh Rao, Lindsay Rolig, Yasushi Saito, Michal Szymaniak, Christopher Taylor, Ruth Wang, Dale Woodford

Google, Inc.

Tóm tắt

Spanner là cơ sở dữ liệu có khả năng mở rộng, đa phiên bản, phân tán toàn cầu và được sao chép đồng bộ của Google. Đây là hệ thống đầu tiên phân phối dữ liệu ở quy mô toàn cầu và hỗ trợ các giao dịch phân tán có tính nhất quán bên ngoài. Bài báo này mô tả cách Spanner được cấu trúc, tập tính năng của nó, cơ sở lý luận đằng sau các quyết định thiết kế khác nhau, và một API thời gian mới cung cấp khả năng hiển thị độ không chắc chắn của đồng hồ. API này cùng với việc triển khai của nó là yếu tố then chốt để hỗ trợ tính nhất quán bên ngoài và một loạt tính năng mạnh mẽ: đọc không chặn trong quá khứ, các giao dịch chỉ đọc không khóa, và các thay đổi lược đồ nguyên tử, trên toàn bộ Spanner.
