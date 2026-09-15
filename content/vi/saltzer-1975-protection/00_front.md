---
paper: saltzer-1975-protection
title: The Protection of Information in Computer Systems
authors:
  - Jerome H. Saltzer
  - Michael D. Schroeder
year: 1975
venue: Proceedings of the IEEE
field: security
section_title: Front Matter
tag: 005E
kind: front
lang: vi
source: https://cgi.cse.unsw.edu.au/~cs9242/24/papers/Saltzer_Schroeder_75.pdf
pdf_sha256: d33039c90c05dc2db4a1ea8f27bd710353bed271224e41bc76c2a42e89539dc1
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 07784ac9f410a67ba7ae735cbecd0e6c6d9196d399fc2d2c77892f4d9b24b4cc
translated_from: content/en/saltzer-1975-protection/00_front.md
source_content_sha256: 284c197a1cf82c0e4873faac3fc6fa63cbf250449b5e5d66b63a43ad958c79cd
translation_model: gpt-5
translation_run: 20260915T013833Z
glossary_version: 6
glossary_terms_sha256: 363c21723d588ca6b8032fd3e2b0aa8dc6ab225b1f9ca1b6e98d75976e8b0d0a
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Bảo vệ thông tin trong các hệ thống máy tính

JEROME H. SALTZER, SENIOR MEMBER, IEEE, AND
MICHAEL D. SCHROEDER, MEMBER, IEEE

Về bài báo này

Bản thảo nhận ngày 11 tháng 10 năm 1974; sửa đổi ngày 17 tháng 4 năm 1975.
Bản quyền © 1975 thuộc về J. H. Saltzer.

Hội nghị chuyên đề ACM lần thứ tư về các nguyên lý hệ điều hành (tháng 10 năm 1973).
Phiên bản sửa đổi trong Communications of the ACM 17, 7 (tháng 7 năm 1974).

Phiên bản web ban đầu do Norman Hardy tạo.

Bài báo được mời

Tóm tắt

Bài báo hướng dẫn này khảo sát cơ chế bảo vệ thông tin được lưu trữ trong máy tính khỏi việc sử dụng hoặc sửa đổi trái phép. Bài báo tập trung vào những cấu trúc kiến trúc--dù là phần cứng hay phần mềm--cần thiết để hỗ trợ việc bảo vệ thông tin. Bài báo được triển khai trong ba phần chính. Phần I mô tả các hàm mong muốn, các nguyên tắc thiết kế và các ví dụ về những cơ chế bảo vệ và xác thực cơ bản. Bất kỳ độc giả nào quen thuộc với máy tính đều có thể tiếp cận phần đầu tương đối dễ dàng. Phần II đòi hỏi một mức độ quen thuộc nhất định với kiến trúc máy tính dựa trên descriptor. Phần này xem xét chuyên sâu các nguyên tắc của các kiến trúc bảo vệ hiện đại và mối quan hệ giữa các hệ thống capability và các hệ thống danh sách kiểm soát truy cập, đồng thời kết thúc bằng một phân tích ngắn về các phân hệ được bảo vệ và các đối tượng được bảo vệ. Độc giả cảm thấy nản lòng bởi các kiến thức tiên quyết hoặc mức độ chi tiết của phần thứ hai có thể muốn bỏ qua Phần III, phần này tổng quan về hiện trạng và các dự án nghiên cứu hiện tại, đồng thời đưa ra các gợi ý để đọc thêm.
