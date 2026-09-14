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
content_sha256: eda8c943ba0974222a90a512a19904efb7478e1400359e351dcda281012fa8d5
translated_from: content/en/brin-1998-pagerank/00_front.md
source_content_sha256: bb9c52869a1fd932379f1b224b04320ef96bc48516321a848c2c0f71fd4093d0
translation_model: gpt-6-astra
translation_run: 20260914T155157Z
glossary_version: 6
glossary_terms_sha256: 51f62d367854beec600f51894702ad34dfcde96c993d5c00a2f7a9873047d13f
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Cấu trúc của một công cụ tìm kiếm web siêu văn bản quy mô lớn $^1$

Sergey Brin $^2$, Lawrence Page $^*,2$

Khoa Khoa học Máy tính, Đại học Stanford, Stanford, CA 94305, Hoa Kỳ

Tóm tắt

Trong bài báo này, chúng tôi giới thiệu Google, một nguyên mẫu công cụ tìm kiếm quy mô lớn tận dụng triệt để cấu trúc có trong siêu văn bản (hypertext). Google được thiết kế để thu thập dữ liệu và lập chỉ mục (indexing) web một cách hiệu quả, đồng thời tạo ra các kết quả tìm kiếm thỏa đáng hơn nhiều so với các hệ thống hiện có. Nguyên mẫu với cơ sở dữ liệu toàn văn và siêu liên kết của ít nhất 24 triệu trang có tại http://google.stanford.edu/

Xây dựng một công cụ tìm kiếm là một nhiệm vụ đầy thách thức. Các công cụ tìm kiếm lập chỉ mục hàng chục đến hàng trăm triệu trang web với số lượng từ ngữ phân biệt ở mức tương đương. Chúng trả lời hàng chục triệu truy vấn mỗi ngày. Mặc dù các công cụ tìm kiếm quy mô lớn có vai trò quan trọng trên web, vẫn có rất ít nghiên cứu học thuật về chúng. Hơn nữa, do sự tiến bộ nhanh chóng của công nghệ và sự phát triển mạnh mẽ của web, việc xây dựng một công cụ tìm kiếm web ngày nay rất khác so với ba năm trước. Bài báo này mô tả chuyên sâu về công cụ tìm kiếm web quy mô lớn của chúng tôi — bản mô tả công khai chi tiết đầu tiên như vậy mà chúng tôi biết cho đến nay.

Ngoài các vấn đề mở rộng những kỹ thuật tìm kiếm truyền thống để xử lý dữ liệu ở quy mô này, còn có những thách thức kỹ thuật mới khi sử dụng thông tin bổ sung có trong siêu văn bản để tạo ra kết quả tìm kiếm tốt hơn. Bài báo này giải quyết câu hỏi làm thế nào để xây dựng một hệ thống quy mô lớn có tính thực tiễn, có thể khai thác thông tin bổ sung có trong siêu văn bản.
