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
content_sha256: 01b3775fc062cf4ad97f8722020f02bb16661fa5e528485ed7d3166b5a1a4f00
translated_from: content/en/saltzer-1975-protection/00_front.md
source_content_sha256: 284c197a1cf82c0e4873faac3fc6fa63cbf250449b5e5d66b63a43ad958c79cd
translation_model: gpt-5
translation_run: 20260918T153717Z
glossary_version: 7
glossary_terms_sha256: d47d31b6ddf34c7530d92d8b1f78fa209e5f19447604dc674da31e96c6f9b120
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Bảo vệ thông tin trong các hệ thống máy tính

JEROME H. SALTZER, THÀNH VIÊN CAO CẤP, IEEE, VÀ
MICHAEL D. SCHROEDER, THÀNH VIÊN, IEEE

Về bài báo này

Bản thảo nhận ngày 11 tháng 10 năm 1974; sửa đổi ngày 17 tháng 4 năm 1975.
Bản quyền © 1975 thuộc về J. H. Saltzer.

Hội nghị chuyên đề ACM lần thứ tư về các nguyên lý hệ điều hành (tháng 10 năm 1973).
Phiên bản sửa đổi trong Communications of the ACM 17, 7 (tháng 7 năm 1974).

Phiên bản web gốc do Norman Hardy tạo.

Bài báo được mời

Tóm tắt

Bài báo hướng dẫn này khảo sát các cơ chế bảo vệ thông tin được lưu trữ trong máy tính khỏi việc sử dụng hoặc sửa đổi trái phép. Bài báo tập trung vào những cấu trúc kiến trúc đó, dù là phần cứng hay phần mềm, cần thiết để hỗ trợ việc bảo vệ thông tin. Bài báo được phát triển thành ba phần chính. Phần I mô tả các hàm mong muốn, các nguyên tắc thiết kế và các ví dụ về các cơ chế bảo vệ và xác thực cơ bản. Bất kỳ độc giả nào quen thuộc với máy tính cũng sẽ thấy phần đầu tiên có thể tiếp cận ở mức hợp lý. Phần II yêu cầu một số hiểu biết về kiến trúc máy tính dựa trên bộ mô tả. Phần này xem xét chuyên sâu các nguyên tắc của các kiến trúc bảo vệ hiện đại và mối quan hệ giữa các hệ thống khả năng và các hệ thống danh sách kiểm soát truy cập, đồng thời kết thúc bằng một phân tích ngắn về các hệ thống con được bảo vệ và các đối tượng được bảo vệ. Độc giả cảm thấy nản lòng bởi các yêu cầu tiên quyết hoặc mức độ chi tiết của phần thứ hai có thể muốn bỏ qua đến Phần III, phần này xem xét tình trạng hiện tại của lĩnh vực và các dự án nghiên cứu hiện nay, đồng thời đưa ra các gợi ý cho việc đọc thêm.
