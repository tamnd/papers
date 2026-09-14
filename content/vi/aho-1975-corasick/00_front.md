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
content_sha256: b2aa9f9d25413ec21aa0a388ee5fce4ebba17239d0ec1fc9268ca8582f04cd98
translated_from: content/en/aho-1975-corasick/00_front.md
source_content_sha256: 17d1d9c934a9c79dc1bf9969b26b2fdc40d089cc0cda4e05dff84776e249e10e
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: 51f62d367854beec600f51894702ad34dfcde96c993d5c00a2f7a9873047d13f
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Đối sánh chuỗi hiệu quả: Hỗ trợ tìm kiếm thư mục

Alfred V. Aho và Margaret J. Corasick
Bell Laboratories

Bài báo này mô tả một thuật toán đơn giản, hiệu quả để xác định tất cả các lần xuất hiện của bất kỳ từ khóa nào trong một số hữu hạn từ khóa trong một chuỗi văn bản. Thuật toán bao gồm việc xây dựng một máy đối sánh mẫu trạng thái hữu hạn từ các từ khóa, sau đó sử dụng máy đối sánh mẫu để xử lý chuỗi văn bản trong một lượt duy nhất. Việc xây dựng máy đối sánh mẫu cần thời gian tỷ lệ với tổng độ dài của các từ khóa. Số chuyển trạng thái do máy đối sánh mẫu thực hiện khi xử lý chuỗi văn bản độc lập với số lượng từ khóa. Thuật toán đã được sử dụng để cải thiện tốc độ của một chương trình tìm kiếm thư mục của thư viện lên một hệ số từ 5 đến 10.

Từ khóa và cụm từ: từ khóa và cụm từ, đối sánh mẫu chuỗi, tìm kiếm thư mục, truy hồi thông tin, soạn thảo văn bản, máy trạng thái hữu hạn, độ phức tạp tính toán.

Các phân loại CR: 3.74, 3.71, 5.22, 5.25
