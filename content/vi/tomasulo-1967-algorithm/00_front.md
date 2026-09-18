---
paper: tomasulo-1967-algorithm
title: An Efficient Algorithm for Exploiting Multiple Arithmetic Units
authors:
  - R. M. Tomasulo
year: 1967
venue: IBM Journal of Research and Development
field: architecture
section_title: Front Matter
tag: "0059"
kind: front
lang: vi
source: https://doi.org/10.1147/rd.111.0025
pdf_sha256: b62a6bc6a0b22d9acf08415f9f95f89d6a0b5c9ce46ee9a42563eb9228695be7
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: be864e39945ab4145a17bed5dc680709d4f9671ee48f2770bf1da24be2975e59
translated_from: content/en/tomasulo-1967-algorithm/00_front.md
source_content_sha256: f477a5893c0dba3b63e120acb37e18273f7e2218be9f0270412523d1f0e09987
translation_model: gpt-5
translation_run: 20260918T153717Z
glossary_version: 7
glossary_terms_sha256: cb514473400f65abfd1e5d09e5f82163f246175d67293cbba8eac7dbb7d7b890
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Thuật toán Hiệu quả để Khai thác Nhiều Đơn vị Số học

Tóm tắt: Bài báo này mô tả các phương pháp được sử dụng trong vùng dấu phẩy động của System/360 Model 91 để khai thác sự tồn tại của nhiều đơn vị thực thi. Cơ sở của các kỹ thuật này là một sơ đồ bus dữ liệu chung và gắn thẻ thanh ghi đơn giản, cho phép thực thi đồng thời các lệnh độc lập trong khi vẫn duy trì các quan hệ trước sau thiết yếu vốn có trong luồng lệnh. Bus dữ liệu chung cải thiện hiệu năng bằng cách sử dụng hiệu quả các đơn vị thực thi mà không yêu cầu mã được tối ưu hóa đặc biệt. Thay vào đó, phần cứng, bằng cách "nhìn trước" khoảng tám lệnh, tự động tối ưu hóa việc thực thi chương trình trên cơ sở cục bộ.

Việc áp dụng các kỹ thuật này không bị giới hạn trong số học dấu phẩy động hoặc kiến trúc System/360. Nó có thể được sử dụng trong hầu hết mọi máy tính có nhiều đơn vị thực thi và một hoặc nhiều "bộ tích lũy". Cả hai đơn vị thực thi, cũng như các bộ đệm lưu trữ liên quan, nhiều bộ tích lũy và các bus đầu vào/đầu ra, đều được kiểm tra rộng rãi.
