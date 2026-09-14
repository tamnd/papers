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
content_sha256: deb244b34caedb0e343012e32b1b56f4baab4f1dbbad5bf60d097b41bbd66d5d
translated_from: content/en/mohan-1992-aries/00_front.md
source_content_sha256: e5fd430824f0caa0de71802b05c5b5fbf989c4d3acee1f86c8879cb76afc15c2
translation_model: gpt-5
translation_run: 20260914T163737Z
glossary_version: 6
glossary_terms_sha256: a534ae50d60bff0e03804fd3c150e37d1876484531ab87df9c72dc4d0c455eb2
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

ARIES: Một Phương pháp Phục hồi Giao dịch Hỗ trợ Khóa Độ hạt Mịn và Quay lui từng phần Sử dụng Ghi nhật ký Trước khi Ghi

C. MOHAN

IBM Almaden Research Center

và

DON HADERLE

IBM Santa Teresa Laboratory

và

BRUCE LINDSAY, HAMID PIRAHESH và PETER SCHWARZ

IBM Almaden Research Center

Trong bài báo này, chúng tôi trình bày một phương pháp đơn giản và hiệu quả, được gọi là ARIES (Algorithm for Recovery and Isolation Exploiting Semantics), hỗ trợ quay lui từng phần của các giao dịch, khóa độ hạt mịn (ví dụ, bản ghi) và phục hồi sử dụng ghi nhật ký trước khi ghi (WAL). Chúng tôi đưa ra mô hình lặp lại lịch sử để thực hiện lại tất cả các cập nhật bị thiếu trước khi thực hiện các thao tác quay lui của các giao dịch thua trong quá trình khởi động lại sau một sự cố hệ thống. ARIES sử dụng một số thứ tự nhật ký trong mỗi trang để tương quan trạng thái của một trang với các cập nhật được ghi nhật ký của trang đó. Tất cả các cập nhật của một giao dịch đều được ghi nhật ký, bao gồm cả những cập nhật được thực hiện trong quá trình quay lui. Bằng cách liên kết chuỗi thích hợp các bản ghi nhật ký được ghi trong quá trình quay lui với các bản ghi được ghi trong quá trình tiến triển về phía trước, một lượng ghi nhật ký bị giới hạn được đảm bảo trong quá trình quay lui ngay cả khi xảy ra các sự cố lặp lại trong quá trình khởi động lại hoặc khi có các thao tác quay lui lồng nhau. Chúng tôi xử lý nhiều tính năng đa dạng rất quan trọng trong việc xây dựng và vận hành một hệ thống xử lý giao dịch cấp công nghiệp. ARIES hỗ trợ các điểm kiểm tra mờ, khởi động lại có chọn lọc và trì hoãn, các bản sao ảnh mờ, phục hồi phương tiện, và các chế độ khóa đồng thời cao (ví dụ, tăng/giảm) khai thác ngữ nghĩa của các thao tác và yêu cầu khả năng thực hiện ghi nhật ký thao tác. ARIES linh hoạt đối với các loại chính sách quản lý bộ đệm có thể được triển khai.
