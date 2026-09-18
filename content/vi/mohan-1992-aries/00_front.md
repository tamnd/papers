---
paper: mohan-1992-aries
title: 'ARIES: A Transaction Recovery Method Supporting Fine-Granularity Locking and Partial Rollbacks Using Write-Ahead Logging'
authors:
  - C. Mohan
  - Don Haderle
  - Bruce Lindsay
  - Hamid Pirahesh
  - Peter Schwarz
year: 1992
venue: ACM TODS
field: databases
section_title: Front Matter
tag: "0057"
kind: front
lang: vi
source: https://people.eecs.berkeley.edu/~brewer/cs262/Aries2.pdf
pdf_sha256: 1007fcedb6b8b465f97ee1c4e4d88420450b50b18ff5ad400a130b21e4961817
pdf_pages: 1-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 8dbe52b37ed9a88a5b343e9adabb4981b7f0b1aa03f944eab7e4b15e8c6d0230
translated_from: content/en/mohan-1992-aries/00_front.md
source_content_sha256: e5fd430824f0caa0de71802b05c5b5fbf989c4d3acee1f86c8879cb76afc15c2
translation_model: gpt-5
translation_run: 20260918T153717Z
glossary_version: 7
glossary_terms_sha256: 8d6365491a62bf683f227b4ec25e6ea4a6b206a0b00009512875972be95a0002
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

ARIES: Một Phương pháp Khôi phục Giao dịch Hỗ trợ Khóa Hạt mịn và Quay lui Một phần Sử dụng Ghi nhật ký Trước khi Ghi

C. MOHAN

IBM Almaden Research Center

và

DON HADERLE

IBM Santa Teresa Laboratory

và

BRUCE LINDSAY, HAMID PIRAHESH và PETER SCHWARZ

IBM Almaden Research Center

Trong bài báo này, chúng tôi trình bày một phương pháp đơn giản và hiệu quả, được gọi là ARIES (Algorithm for Recovery and Isolation Exploiting Semantics), hỗ trợ quay lui một phần của các giao dịch, khóa với độ hạt mịn (ví dụ, bản ghi) và khôi phục bằng cách sử dụng ghi nhật ký trước khi ghi (WAL). Chúng tôi đưa ra mô hình lặp lại lịch sử để thực hiện lại tất cả các cập nhật bị thiếu trước khi thực hiện các thao tác quay lui của các giao dịch thua trong quá trình khởi động lại sau một sự cố hệ thống. ARIES sử dụng một số thứ tự nhật ký trong mỗi trang để tương quan trạng thái của một trang với các cập nhật đã được ghi nhật ký của trang đó. Tất cả các cập nhật của một giao dịch đều được ghi nhật ký, bao gồm cả những cập nhật được thực hiện trong quá trình quay lui. Bằng cách liên kết thích hợp các bản ghi nhật ký được ghi trong quá trình quay lui với các bản ghi được ghi trong quá trình tiến triển, một lượng ghi nhật ký bị giới hạn được đảm bảo trong quá trình quay lui ngay cả khi xảy ra các sự cố lặp lại trong quá trình khởi động lại hoặc các lần quay lui lồng nhau. Chúng tôi xử lý nhiều tính năng khác nhau rất quan trọng trong việc xây dựng và vận hành một hệ thống xử lý giao dịch có cấp độ công nghiệp. ARIES hỗ trợ các điểm kiểm tra mờ, khởi động lại có chọn lọc và trì hoãn, các bản sao ảnh mờ, khôi phục phương tiện, và các chế độ khóa có tính đồng thời cao (ví dụ, tăng/giảm), trong đó khai thác ngữ nghĩa của các thao tác và yêu cầu khả năng thực hiện ghi nhật ký thao tác. ARIES linh hoạt đối với các loại chính sách quản lý bộ đệm có thể được triển khai.
