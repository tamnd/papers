---
paper: dean-2004-mapreduce
title: 'MapReduce: Simplified Data Processing on Large Clusters'
authors:
  - Jeffrey Dean
  - Sanjay Ghemawat
year: 2004
venue: OSDI
field: systems
section: "8"
section_title: Kết luận
tag: 008A
kind: section
lang: vi
source: https://www.usenix.org/legacy/events/osdi04/tech/full_papers/dean/dean.pdf
pdf_sha256: 9cfef3ef1b8fe1a1b66c7221f56c2eeca0b15d6608ea68b0c85a38bfbffd8ce5
pdf_pages: "12"
extraction: vision
extraction_model: gpt-5
content_sha256: 23bacfef15a97c67d97b11748c5639ae190741550a0b928a275f8014716e5956
translated_from: content/en/dean-2004-mapreduce/08_conclusions.md
source_content_sha256: 6cef7d05c2cafe6cad8e3800f5d512de3afaaa82a0184648136a5fd042b8ab09
translation_model: gpt-5
translation_run: 20260914T163737Z
glossary_version: 6
glossary_terms_sha256: afc6de5d010821f75553a129f8b55d5fbabc0d9d7af198021ca9a5a496de4088
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Mô hình lập trình MapReduce đã được sử dụng thành công tại Google cho nhiều mục đích khác nhau. Chúng tôi quy thành công này cho một số lý do. Thứ nhất, mô hình này dễ sử dụng, ngay cả đối với các lập trình viên không có kinh nghiệm về các hệ thống song song và hệ thống phân tán, vì nó che giấu các chi tiết của việc song song hóa, khả năng chịu lỗi, tối ưu hóa tính cục bộ và cân bằng tải. Thứ hai, rất nhiều bài toán có thể dễ dàng được biểu diễn dưới dạng các tính toán MapReduce. Ví dụ, MapReduce được sử dụng để tạo dữ liệu cho dịch vụ tìm kiếm web đang vận hành của Google, để sắp xếp, khai phá dữ liệu, học máy và nhiều hệ thống khác. Thứ ba, chúng tôi đã phát triển một triển khai MapReduce có khả năng mở rộng tới các cụm máy lớn gồm hàng nghìn máy. Triển khai này sử dụng hiệu quả các tài nguyên máy và do đó phù hợp để giải quyết nhiều bài toán tính toán quy mô lớn gặp phải tại Google.

Chúng tôi đã rút ra một số điều từ công trình này. Thứ nhất, việc hạn chế mô hình lập trình giúp dễ dàng song song hóa và phân phối các tính toán, đồng thời làm cho các tính toán đó có khả năng chịu lỗi. Thứ hai, băng thông mạng là một tài nguyên khan hiếm. Do đó, một số tối ưu hóa trong hệ thống của chúng tôi hướng tới việc giảm lượng dữ liệu được gửi qua mạng: tối ưu hóa tính cục bộ cho phép chúng tôi đọc dữ liệu từ các đĩa cục bộ, và việc ghi một bản sao duy nhất của dữ liệu trung gian vào đĩa cục bộ giúp tiết kiệm băng thông mạng. Thứ ba, thực thi dư thừa có thể được sử dụng để giảm tác động của các máy chậm, cũng như để xử lý các sự cố máy và mất dữ liệu.
