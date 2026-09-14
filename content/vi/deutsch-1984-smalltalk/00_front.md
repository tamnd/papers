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
content_sha256: f754d072ee0818d95540be7e79dc926a89701e4f65457069d252030d0bcf2006
translated_from: content/en/deutsch-1984-smalltalk/00_front.md
source_content_sha256: 64032bbbb8fd182a69fb8ac6e35b65d90ee769ed62ed7b817d5f46f08accd2c1
translation_model: gpt-5
translation_run: 20260914T155157Z
glossary_version: 6
glossary_terms_sha256: e18583cfd8910711c2e3aa00f134fd0de9487b97e78e37da9096be4297760e66
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
roundtrip: differs-in-wording
roundtrip_run: 20260914T214350Z
---

Triển khai hiệu quả hệ thống Smalltalk-80

L. Peter Deutsch  
Xerox PARC, Software Concepts Group

Allan M. Schiffman  
Fairchild Laboratory for Artificial Intelligence Research

TÓM TẮT

Ngôn ngữ lập trình Smalltalk-80* bao gồm cấp phát bộ nhớ động, các funarg hướng lên đầy đủ, và các thủ tục đa hình toàn phần; hệ thống lập trình Smalltalk-80 có tính năng thực thi tương tác với biên dịch gia tăng, và khả năng di động trong triển khai. Những tính năng này của các hệ thống lập trình hiện đại nằm trong số những tính năng khó triển khai hiệu quả nhất, ngay cả khi xét riêng lẻ. Một triển khai mới của hệ thống Smalltalk-80, được lưu trữ trên một máy tính nhỏ dựa trên bộ vi xử lý, đạt hiệu năng cao trong khi vẫn duy trì khả năng tương thích hoàn toàn (mã đối tượng) với các triển khai hiện có. Bài báo này thảo luận về các kỹ thuật tối ưu hóa quan trọng nhất được phát triển trong quá trình thực hiện dự án, nhiều kỹ thuật trong số đó có thể áp dụng cho các ngôn ngữ khác. Ý tưởng then chốt là biểu diễn một số trạng thái thời gian chạy (cả mã và dữ liệu) dưới nhiều dạng khác nhau, và chuyển đổi giữa các dạng khi cần thiết.

*Smalltalk-80 là nhãn hiệu thương mại của Xerox Corporation.
