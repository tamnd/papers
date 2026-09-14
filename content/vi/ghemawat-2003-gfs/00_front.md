---
paper: ghemawat-2003-gfs
title: The Google File System
authors:
  - Sanjay Ghemawat
  - Howard Gobioff
  - Shun-Tak Leung
year: 2003
venue: SOSP
field: systems
section_title: Front Matter
tag: 016D
kind: front
lang: vi
source: https://doi.org/10.1145/945445.945450
pdf_sha256: 108ced8f084131ae6241b2c43c0b8f8bee01a8427c2527cbc204c87f1fdfce33
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 1539c2d7bd9a7158c38cc804dac88acfe7ee8033c04e0bc4a52004ec2c0ca869
translated_from: content/en/ghemawat-2003-gfs/00_front.md
source_content_sha256: 2ea03b1f6c85fd99dcc1132574367d7e4beae3285a8520e2a66c075e0894e0c7
translation_model: gpt-5
translation_run: 20260914T163737Z
glossary_version: 6
glossary_terms_sha256: afc6de5d010821f75553a129f8b55d5fbabc0d9d7af198021ca9a5a496de4088
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Hệ thống tệp Google

Sanjay Ghemawat, Howard Gobioff, và Shun-Tak Leung

Google*

TÓM TẮT

Chúng tôi đã thiết kế và triển khai Hệ thống tệp Google, một hệ thống tệp phân tán có khả năng mở rộng cho các ứng dụng lớn phân tán sử dụng nhiều dữ liệu. Nó cung cấp khả năng chịu lỗi trong khi chạy trên phần cứng phổ thông giá rẻ, đồng thời cung cấp hiệu năng tổng hợp cao cho một số lượng lớn máy khách.

Mặc dù chia sẻ nhiều mục tiêu giống với các hệ thống tệp phân tán trước đây, thiết kế của chúng tôi được thúc đẩy bởi các quan sát về tải công việc ứng dụng và môi trường công nghệ của chúng tôi, cả hiện tại và dự kiến, phản ánh sự khác biệt đáng kể so với một số giả định trước đây về hệ thống tệp. Điều này đã khiến chúng tôi xem xét lại các lựa chọn truyền thống và khám phá những điểm thiết kế hoàn toàn khác biệt.

Hệ thống tệp đã đáp ứng thành công các nhu cầu lưu trữ của chúng tôi. Nó được triển khai rộng rãi trong Google như nền tảng lưu trữ cho việc tạo và xử lý dữ liệu được sử dụng bởi dịch vụ của chúng tôi, cũng như cho các nỗ lực nghiên cứu và phát triển yêu cầu các tập dữ liệu lớn. Cụm lớn nhất cho đến nay cung cấp hàng trăm terabyte dung lượng lưu trữ trên hàng nghìn đĩa trên hơn một nghìn máy, và được truy cập đồng thời bởi hàng trăm máy khách.

Trong bài báo này, chúng tôi trình bày các mở rộng giao diện hệ thống tệp được thiết kế để hỗ trợ các ứng dụng phân tán, thảo luận về nhiều khía cạnh trong thiết kế của chúng tôi, và báo cáo các phép đo từ cả các phép đo chuẩn vi mô và việc sử dụng trong thế giới thực.

Các danh mục và mô tả chủ đề

D [4]: 3—Các hệ thống tệp phân tán

Các thuật ngữ chung

Thiết kế, độ tin cậy, hiệu năng, phép đo

Từ khóa

Khả năng chịu lỗi, khả năng mở rộng, lưu trữ dữ liệu, lưu trữ theo cụm

*Có thể liên hệ với các tác giả tại các địa chỉ sau: {sanjay,hgobioff,shuntak}@google.com.
