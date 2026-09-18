---
paper: astrahan-1976-systemr
title: 'System R: Relational Approach to Database Management'
authors:
  - M. M. Astrahan
  - M. W. Blasgen
  - D. D. Chamberlin
  - K. P. Eswaran
  - J. N. Gray
  - P. P. Griffiths
  - W. F. King
  - R. A. Lorie
  - P. R. McJones
  - J. W. Mehl
  - G. R. Putzolu
  - I. L. Traiger
  - B. W. Wade
  - V. Watson
year: 1976
venue: ACM TODS
field: databases
section_title: Front Matter
tag: "0056"
kind: front
lang: vi
source: https://www.cs.princeton.edu/courses/archive/fall11/cos518/papers/system-R.pdf
pdf_sha256: e66b9412f77f7dc2599908c627e49e92e2949832e64a94f12652ab0915a8a1b5
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 2759db4ba3cbac6b20cebed40bf9749e01daef036b2cf874ff1306f04ef26207
translated_from: content/en/astrahan-1976-systemr/00_front.md
source_content_sha256: 1b22b54193ecc4e2dd2e8ba8daa11408a82861c8a8d49655273f9c452dc0978b
translation_model: gpt-5
translation_run: 20260918T153717Z
glossary_version: 7
glossary_terms_sha256: 8d6365491a62bf683f227b4ec25e6ea4a6b206a0b00009512875972be95a0002
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

System R: Phương pháp quan hệ đối với quản lý cơ sở dữ liệu

M. M. ASTRAHAN, M. W. BLASGEN, D. D. CHAMBERLIN,
K. P. ESWARAN, J. N. GRAY, P. P. GRIFFITHS,
W. F. KING, R. A. LORIE, P. R. McJONES, J. W. MEHL,
G. R. PUTZOLU, I. L. TRAIGER, B. W. WADE, AND V. WATSON

IBM Research Laboratory

System R là một hệ thống quản lý cơ sở dữ liệu cung cấp một giao diện dữ liệu quan hệ cấp cao. Hệ thống cung cấp tính độc lập dữ liệu cấp cao bằng cách tách người dùng cuối khỏi các cấu trúc lưu trữ bên dưới nhiều nhất có thể. Hệ thống cho phép định nghĩa nhiều dạng khung nhìn quan hệ trên cùng một dữ liệu cơ sở bên dưới. Các tính năng kiểm soát dữ liệu được cung cấp, bao gồm quyền hạn, các khẳng định toàn vẹn, các giao dịch được kích hoạt, một hệ thống con ghi nhật ký và phục hồi, cùng các tiện ích để duy trì tính nhất quán dữ liệu trong môi trường cập nhật dùng chung.

Bài báo này chứa mô tả về kiến trúc tổng thể và thiết kế của hệ thống. Hiện tại hệ thống đang được triển khai và thiết kế đang được đánh giá. Chúng tôi nhấn mạnh rằng System R là một phương tiện cho nghiên cứu về kiến trúc cơ sở dữ liệu, và không được lên kế hoạch như một sản phẩm.

Từ khóa và cụm từ: cơ sở dữ liệu, mô hình quan hệ, ngôn ngữ phi thủ tục, quyền hạn, khóa, phục hồi, cấu trúc dữ liệu, cấu trúc chỉ mục  
Phân loại CR: 3.74, 4.22, 4.33, 4.35
