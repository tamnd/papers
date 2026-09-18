---
paper: ritchie-1974-unix
title: The UNIX Time-Sharing System
authors:
  - Dennis M. Ritchie
  - Ken Thompson
year: 1974
venue: Communications of the ACM
field: systems
section_title: Front Matter
tag: 016B
kind: front
lang: vi
source: https://dsf.berkeley.edu/cs262/unix.pdf
pdf_sha256: 96bc5caa11cc13925165b6d36b78c55cc61a61e65a628c375511683a97442b51
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: b33d9567b970da860ee7e553aa4566664d81c48207abebb75042e236491a5a22
translated_from: content/en/ritchie-1974-unix/00_front.md
source_content_sha256: 8e80835041117dfa0d815a9e053ee58ac82ef0ef109676723c0f682799ce74ee
translation_model: gpt-5
translation_run: 20260918T122832Z
glossary_version: 7
glossary_terms_sha256: f834761938c11bca59f7cb79948997ed0706af48cd70392678452699c034a7ad
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Hệ thống chia sẻ thời gian UNIX

Dennis M. Ritchie và Ken Thompson
Bell Laboratories

UNIX là một hệ điều hành tương tác, đa người dùng, mục đích chung dành cho các máy tính PDP-11/40 và 11/45 của Digital Equipment Corporation. Nó cung cấp một số tính năng hiếm thấy ngay cả trong các hệ điều hành lớn hơn, bao gồm: (1) một hệ thống file phân cấp kết hợp các volume có thể tháo lắp; (2) I/O file, thiết bị và liên tiến trình tương thích; (3) khả năng khởi tạo các tiến trình bất đồng bộ; (4) ngôn ngữ lệnh hệ thống có thể được lựa chọn theo từng người dùng; và (5) hơn 100 hệ thống con bao gồm một tá ngôn ngữ. Bài báo này thảo luận về bản chất và việc triển khai của hệ thống file và giao diện lệnh người dùng.

Từ khóa và cụm từ chính: chia sẻ thời gian, hệ điều hành, hệ thống file, ngôn ngữ lệnh, PDP-11

Phân loại CR: 4.30, 4.32

Bản quyền © 1974, Association for Computing Machinery, Inc. Cho phép tái bản toàn bộ hoặc một phần tài liệu này vì mục đích không lợi nhuận với điều kiện phải ghi thông báo bản quyền của ACM và dẫn chiếu đến ấn phẩm, ngày phát hành của ấn phẩm, cũng như việc quyền tái bản đã được cấp phép bởi Association for Computing Machinery.

Đây là phiên bản đã chỉnh sửa của một bài báo được trình bày tại Fourth ACM Symposium on Operating Systems Principles, IBM Thomas J. Watson Research Center, Yorktown Heights. New York, ngày 15–17 tháng 10 năm 1973. Địa chỉ của các tác giả: Bell Laboratories, Murray Hill, NJ 07974.

Phiên bản điện tử được tái tạo bởi Eric A. Brewer, University of California at Berkeley, brewer@cs.berkeley.edu. Vui lòng thông báo cho tôi về bất kỳ sai lệch nào so với bản gốc; tôi đã giữ nguyên các lỗi trong bản gốc.
