---
paper: deutsch-1984-smalltalk
title: Efficient Implementation of the Smalltalk-80 System
authors:
  - L. Peter Deutsch
  - Allan M. Schiffman
year: 1984
venue: POPL
field: languages
section_title: Front Matter
tag: 004A
kind: front
lang: vi
source: https://doi.org/10.1145/800017.800542
pdf_sha256: 300584e302ee0fa5a006ee363d9e3f1b0df043c3259580e32dcd409e9a09871d
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 189e99a37525d3a0026659826ce80d621433205302f0898f87282f62012f7cf6
translated_from: content/en/deutsch-1984-smalltalk/00_front.md
source_content_sha256: 64032bbbb8fd182a69fb8ac6e35b65d90ee769ed62ed7b817d5f46f08accd2c1
translation_model: gpt-5
translation_run: 20260918T122832Z
glossary_version: 7
glossary_terms_sha256: 61df191034dbc0d2b4fd3d0e6780a45e637697c607e59ad493d8021ee078cd25
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Triển khai hiệu quả hệ thống Smalltalk-80

L. Peter Deutsch
Xerox PARC, Software Concepts Group

Allan M. Schiffman
Fairchild Laboratory for Artificial Intelligence Research

TÓM TẮT

Ngôn ngữ lập trình Smalltalk-80* bao gồm cấp phát lưu trữ động, full upward funargs và các thủ tục đa hình toàn cục; hệ thống lập trình Smalltalk-80 có thực thi tương tác với biên dịch tăng dần và khả năng chuyển đổi triển khai. Những đặc điểm này của các hệ thống lập trình hiện đại thuộc số những đặc điểm khó triển khai hiệu quả nhất, ngay cả khi xét riêng lẻ. Một triển khai mới của hệ thống Smalltalk-80, được lưu trữ trên một máy tính dựa trên bộ vi xử lý nhỏ, đạt được hiệu năng cao trong khi vẫn duy trì khả năng tương thích hoàn toàn (mã đối tượng) với các triển khai hiện có. Bài báo này thảo luận về các kỹ thuật tối ưu hóa quan trọng nhất được phát triển trong quá trình của dự án, nhiều kỹ thuật trong số đó có thể áp dụng cho các ngôn ngữ khác. Ý tưởng then chốt là biểu diễn một số trạng thái thời gian chạy nhất định (cả mã và dữ liệu) dưới nhiều dạng, và chuyển đổi giữa các dạng khi cần thiết.

*Smalltalk-80 là một nhãn hiệu của Xerox Corporation.
