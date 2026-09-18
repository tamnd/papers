---
paper: brin-1998-pagerank
title: The Anatomy of a Large-Scale Hypertextual Web Search Engine
authors:
  - Sergey Brin
  - Lawrence Page
year: 1998
venue: Computer Networks and ISDN Systems
field: algorithms
section_title: Front Matter
tag: "0045"
kind: front
lang: vi
source: https://doi.org/10.1016/s0169-7552(98)00110-x
pdf_sha256: 3a155ade395c7789876a0bc08a1842f909486438c1b1739ae531fa5c797d93f0
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: ff267c8bf87b4f8cc13b856e5f89e4e83d2f6a91d8d8b6e8320a728f4706e6b2
translated_from: content/en/brin-1998-pagerank/00_front.md
source_content_sha256: bb9c52869a1fd932379f1b224b04320ef96bc48516321a848c2c0f71fd4093d0
translation_model: gpt-5
translation_run: 20260918T122832Z
glossary_version: 7
glossary_terms_sha256: d4043ebd5a5c828b0239f76956644bfb5bb815f3188dc3282d75521c97669214
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Giải phẫu của một công cụ tìm kiếm Web siêu văn bản quy mô lớn $^1$

Sergey Brin $^2$, Lawrence Page $^*,2$

Khoa Khoa học Máy tính, Đại học Stanford, Stanford, CA 94305, USA

Tóm tắt

Trong bài báo này, chúng tôi trình bày Google, một nguyên mẫu của một công cụ tìm kiếm quy mô lớn sử dụng nhiều cấu trúc hiện có trong siêu văn bản. Google được thiết kế để thu thập dữ liệu và lập chỉ mục Web một cách hiệu quả, đồng thời tạo ra các kết quả tìm kiếm thỏa mãn hơn nhiều so với các hệ thống hiện có. Nguyên mẫu với cơ sở dữ liệu văn bản đầy đủ và siêu liên kết gồm ít nhất 24 triệu trang có sẵn tại http://google.stanford.edu/

Việc xây dựng một công cụ tìm kiếm là một nhiệm vụ đầy thách thức. Các công cụ tìm kiếm lập chỉ mục từ hàng chục đến hàng trăm triệu trang Web liên quan đến một số lượng tương đương các thuật ngữ riêng biệt. Chúng trả lời hàng chục triệu truy vấn mỗi ngày. Mặc dù các công cụ tìm kiếm quy mô lớn trên Web có tầm quan trọng, rất ít nghiên cứu học thuật đã được thực hiện về chúng. Hơn nữa, do sự tiến bộ nhanh chóng của công nghệ và sự phát triển của Web, việc tạo ra một công cụ tìm kiếm Web ngày nay rất khác so với ba năm trước. Bài báo này cung cấp mô tả chuyên sâu về công cụ tìm kiếm Web quy mô lớn của chúng tôi — mô tả công khai chi tiết đầu tiên như vậy mà chúng tôi biết cho đến nay.

Ngoài các vấn đề về việc mở rộng các kỹ thuật tìm kiếm truyền thống lên dữ liệu có quy mô lớn như vậy, còn có những thách thức kỹ thuật mới liên quan đến việc sử dụng thông tin bổ sung hiện diện trong siêu văn bản để tạo ra các kết quả tìm kiếm tốt hơn. Bài báo này giải quyết câu hỏi về cách xây dựng một hệ thống quy mô lớn thực tế có thể khai thác thông tin bổ sung hiện diện trong siêu văn bản.
