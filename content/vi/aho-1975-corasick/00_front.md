---
paper: aho-1975-corasick
title: 'Efficient String Matching: An Aid to Bibliographic Search'
authors:
  - Alfred V. Aho
  - Margaret J. Corasick
year: 1975
venue: Communications of the ACM
field: algorithms
section_title: Front Matter
tag: "0043"
kind: front
lang: vi
source: https://cr.yp.to/bib/1975/aho.pdf
pdf_sha256: f04940c07d2a12726bce4147fd4217e876cd969ddf44094ad90c866893deed34
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 3b002a1bfa5c9a1bd1f0ee68f27e45743b4e416d7153048b831f1175ec452660
translated_from: content/en/aho-1975-corasick/00_front.md
source_content_sha256: 17d1d9c934a9c79dc1bf9969b26b2fdc40d089cc0cda4e05dff84776e249e10e
translation_model: gpt-5
translation_run: 20260918T122832Z
glossary_version: 7
glossary_terms_sha256: d4043ebd5a5c828b0239f76956644bfb5bb815f3188dc3282d75521c97669214
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Đối sánh chuỗi hiệu quả: Một công cụ hỗ trợ tìm kiếm thư mục tài liệu

Alfred V. Aho and Margaret J. Corasick
Bell Laboratories

Bài báo này mô tả một thuật toán đơn giản, hiệu quả để xác định tất cả các lần xuất hiện của bất kỳ số hữu hạn nào các từ khóa trong một chuỗi văn bản. Thuật toán bao gồm việc xây dựng một máy đối sánh mẫu trạng thái hữu hạn từ các từ khóa, sau đó sử dụng máy đối sánh mẫu để xử lý chuỗi văn bản trong một lần duyệt. Việc xây dựng máy đối sánh mẫu cần thời gian tỷ lệ với tổng độ dài của các từ khóa. Số phép chuyển trạng thái được thực hiện bởi máy đối sánh mẫu khi xử lý chuỗi văn bản không phụ thuộc vào số lượng từ khóa. Thuật toán đã được sử dụng để cải thiện tốc độ của một chương trình tìm kiếm thư mục tài liệu trong thư viện lên một hệ số từ 5 đến 10.

Từ khóa và Cụm từ: từ khóa và cụm từ, đối sánh mẫu chuỗi, tìm kiếm thư mục tài liệu, truy hồi thông tin, chỉnh sửa văn bản, máy trạng thái hữu hạn, độ phức tạp tính toán.

Phân loại CR: 3.74, 3.71, 5.22, 5.25
