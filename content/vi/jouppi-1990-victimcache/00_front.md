---
paper: jouppi-1990-victimcache
title: Improving Direct-Mapped Cache Performance by the Addition of a Small Fully-Associative Cache and Prefetch Buffers
authors:
  - Norman P. Jouppi
year: 1990
venue: ISCA
field: architecture
section_title: Front Matter
tag: 005C
kind: front
lang: vi
source: https://doi.org/10.1145/325164.325162
pdf_sha256: 0077ca65ae80ad9d11024aea044515225281980a2dd542f6c04cdece03ed3f86
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: f84f971d00ace2a56b05c5ae4be79b9e5c7fa3f9e70c35921964402587e72040
translated_from: content/en/jouppi-1990-victimcache/00_front.md
source_content_sha256: 4f20da9dbbbde5fb61779b2fb8c0d14e56fc98442283ee94440f3aa9f9357ef9
translation_model: gpt-5
translation_run: 20260914T201546Z
glossary_version: 6
glossary_terms_sha256: 1f83355a83baacb04f1185b8bd47b133f28d2f764f5d7ae919d5d9d0d7e083ee
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Cải thiện hiệu năng của Cache Ánh xạ Trực tiếp bằng cách Bổ sung một Cache Liên kết Đầy đủ Nhỏ và các Bộ đệm Prefetch

Norman P. Jouppi

Digital Equipment Corporation Western Research Lab

100 Hamilton Ave., Palo Alto, CA 94301

Tóm tắt

Các dự báo về công nghệ máy tính cho thấy các bộ xử lý với hiệu năng cực đại 1,000 MIPS trong tương lai tương đối gần. Các bộ xử lý này có thể dễ dàng mất một nửa hoặc hơn hiệu năng của chúng trong hệ thống phân cấp bộ nhớ nếu thiết kế hệ thống phân cấp dựa trên các kỹ thuật caching truyền thống. Bài báo này trình bày các kỹ thuật phần cứng để cải thiện hiệu năng của cache.

Miss caching đặt một cache liên kết đầy đủ nhỏ giữa một cache và đường nạp lại của nó. Các lỗi cache chạm tới miss cache chỉ có chi phí phạt lỗi một chu kỳ, trái ngược với chi phí phạt lỗi nhiều chu kỳ khi không có miss cache. Các miss cache nhỏ có từ 2 đến 5 mục nhập được chứng minh là rất hiệu quả trong việc loại bỏ các lỗi xung đột ánh xạ trong các cache ánh xạ trực tiếp cấp một.

Victim caching là một cải tiến của miss caching, trong đó cache liên kết đầy đủ nhỏ được nạp bằng nạn nhân của một lỗi thay vì dòng được yêu cầu. Các victim cache nhỏ có từ 1 đến 5 mục nhập thậm chí còn hiệu quả hơn miss caching trong việc loại bỏ các lỗi xung đột.

Các bộ đệm dòng (stream buffers) thực hiện prefetch các dòng cache bắt đầu từ một địa chỉ lỗi cache. Dữ liệu được prefetch được đặt trong bộ đệm thay vì trong cache. Các bộ đệm dòng hữu ích trong việc loại bỏ các lỗi cache do dung lượng và bắt buộc, cũng như một số lỗi xung đột cache lệnh.
