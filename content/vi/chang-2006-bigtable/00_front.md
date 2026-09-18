---
paper: chang-2006-bigtable
title: 'Bigtable: A Distributed Storage System for Structured Data'
authors:
  - Fay Chang
  - Jeffrey Dean
  - Sanjay Ghemawat
  - Wilson C. Hsieh
  - Deborah A. Wallach
  - Mike Burrows
  - Tushar Chandra
  - Andrew Fikes
  - Robert E. Gruber
year: 2006
venue: OSDI
field: databases
section_title: Front Matter
tag: 017A
kind: front
lang: vi
source: http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.101.9822
pdf_sha256: 9126cf3b930fd7be2de6248f82565c9b970482eb063bdc30be8c1b29c86b2167
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: d8c962b65cae07810460991bef26a089c02353186cf54caa460278336350d84c
translated_from: content/en/chang-2006-bigtable/00_front.md
source_content_sha256: 10f83ffe57dd267fa9152712dff6d5f7703ecd26d43a0e95ff05243955652dc8
translation_model: gpt-5
translation_run: 20260918T153717Z
glossary_version: 7
glossary_terms_sha256: 8d6365491a62bf683f227b4ec25e6ea4a6b206a0b00009512875972be95a0002
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Bigtable: Một hệ thống lưu trữ phân tán cho dữ liệu có cấu trúc

Fay Chang, Jeffrey Dean, Sanjay Ghemawat, Wilson C. Hsieh, Deborah A. Wallach
Mike Burrows, Tushar Chandra, Andrew Fikes, Robert E. Gruber
{fay,jeff,sanjay,wilsonh,kerr,m3b,tushar,fikes,gruber}@google.com

Google, Inc.

Tóm tắt

Bigtable là một hệ thống lưu trữ phân tán để quản lý dữ liệu có cấu trúc, được thiết kế để mở rộng đến kích thước rất lớn: petabyte dữ liệu trên hàng nghìn server phổ thông. Nhiều dự án tại Google lưu trữ dữ liệu trong Bigtable, bao gồm lập chỉ mục web, Google Earth và Google Finance. Các ứng dụng này đặt ra những yêu cầu rất khác nhau đối với Bigtable, cả về kích thước dữ liệu (từ URL đến trang web và ảnh vệ tinh) lẫn các yêu cầu về độ trễ (từ xử lý hàng loạt ở backend đến cung cấp dữ liệu theo thời gian thực). Mặc dù có những yêu cầu đa dạng này, Bigtable đã cung cấp thành công một giải pháp linh hoạt, hiệu năng cao cho tất cả các sản phẩm này của Google. Trong bài báo này, chúng tôi mô tả mô hình dữ liệu đơn giản do Bigtable cung cấp, cho phép các máy khách kiểm soát động bố cục và định dạng dữ liệu, đồng thời chúng tôi mô tả thiết kế và triển khai của Bigtable.
