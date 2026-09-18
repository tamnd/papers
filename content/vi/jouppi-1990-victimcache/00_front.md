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
content_sha256: 6f3950b3792a15ae0a68e30f5013e76b8aa7c04c4c805904bcb2d81a87ddf6c0
translated_from: content/en/jouppi-1990-victimcache/00_front.md
source_content_sha256: 4f20da9dbbbde5fb61779b2fb8c0d14e56fc98442283ee94440f3aa9f9357ef9
translation_model: gpt-5
translation_run: 20260918T153717Z
glossary_version: 7
glossary_terms_sha256: cb514473400f65abfd1e5d09e5f82163f246175d67293cbba8eac7dbb7d7b890
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Cải thiện hiệu năng Cache ánh xạ trực tiếp bằng cách bổ sung một Cache kết hợp đầy đủ nhỏ và các Bộ đệm nạp trước

Norman P. Jouppi

Digital Equipment Corporation Western Research Lab

100 Hamilton Ave., Palo Alto, CA 94301

Tóm tắt

Các dự báo về công nghệ máy tính cho thấy các bộ xử lý với hiệu năng đỉnh 1,000 MIPS trong tương lai tương đối gần. Các bộ xử lý này có thể dễ dàng mất một nửa hoặc nhiều hơn hiệu năng của chúng trong hệ thống phân cấp bộ nhớ nếu thiết kế của hệ thống phân cấp dựa trên các kỹ thuật cache truyền thống. Bài báo này trình bày các kỹ thuật phần cứng để cải thiện hiệu năng của cache.

Miss caching đặt một cache kết hợp đầy đủ nhỏ giữa một cache và đường nạp lại của nó. Các lỗi cache trúng trong miss cache chỉ có chi phí lỗi một chu kỳ, trái ngược với chi phí lỗi nhiều chu kỳ khi không có miss cache. Các miss cache nhỏ có từ 2 đến 5 mục nhập được cho thấy là rất hiệu quả trong việc loại bỏ các lỗi xung đột ánh xạ trong các cache ánh xạ trực tiếp cấp đầu tiên.

Victim caching là một cải tiến của miss caching, trong đó cache kết hợp đầy đủ nhỏ được nạp với nạn nhân của một lỗi thay vì dòng được yêu cầu. Các victim cache nhỏ có từ 1 đến 5 mục nhập thậm chí còn hiệu quả hơn miss caching trong việc loại bỏ các lỗi xung đột.

Các bộ đệm luồng nạp trước các dòng cache bắt đầu từ một địa chỉ lỗi cache. Dữ liệu được nạp trước được đặt trong bộ đệm chứ không phải trong cache. Các bộ đệm luồng hữu ích trong việc loại bỏ các lỗi cache do dung lượng và bắt buộc, cũng như một số lỗi xung đột cache lệnh.
