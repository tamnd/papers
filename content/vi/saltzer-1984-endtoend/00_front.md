---
paper: saltzer-1984-endtoend
title: End-To-End Arguments in System Design
authors:
  - J. H. Saltzer
  - D. P. Reed
  - D. D. Clark
year: 1984
venue: ACM TOCS
field: systems
section_title: Front Matter
tag: "0050"
kind: front
lang: vi
source: https://doi.org/10.1145/357401.357402
pdf_sha256: 3204a1a562d9d3b72ba112f20caddfd34991d6e1e39939ace6a3e7c016519768
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 7ca71df11df57cc168f4bdde42425827e19b6dc965fc8e47c9556a38f3db0895
translated_from: content/en/saltzer-1984-endtoend/00_front.md
source_content_sha256: 5a38e3114bff08798d2d0cbd283c3deca3d00dd9fa9557b5948408e65f0e55e9
translation_model: gpt-5
translation_run: 20260918T122832Z
glossary_version: 7
glossary_terms_sha256: f834761938c11bca59f7cb79948997ed0706af48cd70392678452699c034a7ad
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

CÁC LẬP LUẬN ĐẦU-CUỐI TRONG THIẾT KẾ HỆ THỐNG

J.H. Saltzer, D.P. Reed and D.D. Clark*

M.I.T. Laboratory for Computer Science

Bài báo này trình bày một nguyên tắc thiết kế giúp định hướng việc đặt các hàm giữa các mô-đun của một hệ thống máy tính phân tán. Nguyên tắc này, được gọi là lập luận đầu-cuối, cho rằng các hàm được đặt ở các mức thấp của một hệ thống có thể là dư thừa hoặc có ít giá trị khi so sánh với chi phí cung cấp chúng ở mức thấp đó. Các ví dụ được thảo luận trong bài báo bao gồm khôi phục lỗi bit, bảo mật sử dụng mã hóa, loại bỏ thông điệp trùng lặp, khôi phục sau sự cố hệ thống và xác nhận phân phối. Các cơ chế mức thấp để hỗ trợ các hàm này chỉ được biện minh như những cải thiện về hiệu năng.
