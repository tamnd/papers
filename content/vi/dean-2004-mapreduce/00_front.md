---
paper: dean-2004-mapreduce
title: 'MapReduce: Simplified Data Processing on Large Clusters'
authors:
  - Jeffrey Dean
  - Sanjay Ghemawat
year: 2004
venue: OSDI
field: systems
section_title: Front Matter
tag: 006A
kind: front
lang: vi
source: https://www.usenix.org/legacy/events/osdi04/tech/full_papers/dean/dean.pdf
pdf_sha256: 9cfef3ef1b8fe1a1b66c7221f56c2eeca0b15d6608ea68b0c85a38bfbffd8ce5
pdf_pages: "1"
extraction: vision
extraction_model: gpt-5
content_sha256: 49fb05a89bc09a9b9d6caa973ea8822a50be109a60da0bce27c7598dc6ac345e
translated_from: content/en/dean-2004-mapreduce/00_front.md
source_content_sha256: 50e40e1d76bad207cd63412840af8cf2e0fc4432de8ad0628778084393f54a7f
translation_model: gpt-5
translation_run: 20260914T163737Z
glossary_version: 6
glossary_terms_sha256: afc6de5d010821f75553a129f8b55d5fbabc0d9d7af198021ca9a5a496de4088
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
roundtrip: same
roundtrip_run: 20260914T214350Z
---

**MapReduce: Xử lý dữ liệu đơn giản hóa trên các cụm lớn**

Jeffrey Dean and Sanjay Ghemawat jeff@google.com, sanjay@google.com

*Google, Inc.*

Tóm tắt

MapReduce là một mô hình lập trình và một triển khai đi kèm để xử lý và tạo ra các tập dữ liệu lớn. Người dùng đặc tả một hàm *map* xử lý một cặp khóa/giá trị để tạo ra một tập các cặp khóa/giá trị trung gian, và một hàm *reduce* hợp nhất tất cả các giá trị trung gian được liên kết với cùng một khóa trung gian. Nhiều tác vụ thực tế có thể được biểu diễn trong mô hình này, như được trình bày trong bài báo.

Các chương trình được viết theo kiểu hàm này được tự động song song hóa và thực thi trên một cụm lớn các máy phổ thông. Hệ thống thời gian chạy xử lý các chi tiết của việc phân vùng dữ liệu đầu vào, lập lịch thực thi chương trình trên một tập hợp các máy, xử lý các sự cố của máy, và quản lý việc giao tiếp liên máy cần thiết. Điều này cho phép các lập trình viên không có kinh nghiệm về các hệ thống song song và phân tán dễ dàng sử dụng các tài nguyên của một hệ thống phân tán lớn.

Triển khai MapReduce của chúng tôi chạy trên một cụm lớn các máy phổ thông và có khả năng mở rộng cao: một tính toán MapReduce điển hình xử lý nhiều terabyte dữ liệu trên hàng nghìn máy. Các lập trình viên nhận thấy hệ thống dễ sử dụng: hàng trăm chương trình MapReduce đã được triển khai và hơn một nghìn công việc MapReduce được thực thi trên các cụm của Google mỗi ngày.
