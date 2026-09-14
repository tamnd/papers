---
paper: dean-2004-mapreduce
title: 'MapReduce: Simplified Data Processing on Large Clusters'
authors:
  - Jeffrey Dean
  - Sanjay Ghemawat
year: 2004
venue: OSDI
field: systems
section: "1"
section_title: Giới thiệu
kind: section
lang: vi
source: https://www.usenix.org/legacy/events/osdi04/tech/full_papers/dean/dean.pdf
pdf_sha256: 9cfef3ef1b8fe1a1b66c7221f56c2eeca0b15d6608ea68b0c85a38bfbffd8ce5
pdf_pages: 1-2
extraction: vision
extraction_model: gpt-5
content_sha256: aa990e5a78e6ccc2958076fc7ea8a7216a7b48b1ee9f0b388230a07f3dfd6503
translated_from: content/en/dean-2004-mapreduce/01_introduction.md
source_content_sha256: ecd74842b3eddb127d86aec0b3f6588f7aaffeaf23a4676b745e58c293a81f7f
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: afc6de5d010821f75553a129f8b55d5fbabc0d9d7af198021ca9a5a496de4088
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Trong năm năm qua, các tác giả và nhiều người khác tại Google đã triển khai hàng trăm phép tính chuyên dụng xử lý lượng lớn dữ liệu thô, chẳng hạn như các tài liệu được thu thập, nhật ký yêu cầu web, v.v., để tính toán nhiều loại dữ liệu dẫn xuất khác nhau, chẳng hạn như các chỉ mục đảo, nhiều biểu diễn khác nhau của cấu trúc đồ thị của các tài liệu web, các bản tóm tắt về số lượng trang được thu thập trên mỗi máy chủ, tập hợp các truy vấn thường xuyên nhất trong một ngày cụ thể, v.v. Hầu hết các phép tính như vậy đều đơn giản về mặt khái niệm. Tuy nhiên, dữ liệu đầu vào thường rất lớn và các phép tính phải được phân phối trên hàng trăm hoặc hàng nghìn máy để hoàn thành trong khoảng thời gian hợp lý. Các vấn đề về cách song song hóa phép tính, phân phối dữ liệu và xử lý các sự cố kết hợp lại làm che khuất phép tính đơn giản ban đầu bằng một lượng lớn mã phức tạp để giải quyết các vấn đề này.

Để phản ứng với độ phức tạp này, chúng tôi đã thiết kế một trừu tượng hóa mới cho phép biểu diễn các phép tính đơn giản mà chúng tôi đang cố gắng thực hiện nhưng ẩn đi các chi tiết lộn xộn của việc song song hóa, khả năng chịu lỗi, phân phối dữ liệu và cân bằng tải trong một thư viện. Trừu tượng hóa của chúng tôi được lấy cảm hứng từ các nguyên thủy *map* và *reduce* có trong Lisp và nhiều ngôn ngữ lập trình hàm khác. Chúng tôi nhận ra rằng hầu hết các phép tính của mình đều liên quan đến việc áp dụng thao tác *map* cho mỗi “bản ghi” logic trong đầu vào của chúng tôi để tính toán một tập hợp các cặp khóa/giá trị trung gian, sau đó áp dụng thao tác *reduce* cho tất cả các giá trị dùng chung cùng một khóa, nhằm kết hợp dữ liệu dẫn xuất một cách thích hợp. Việc sử dụng mô hình hàm với các thao tác map và reduce do người dùng đặc tả cho phép chúng tôi dễ dàng song song hóa các phép tính lớn và sử dụng việc thực thi lại làm cơ chế chính để chịu lỗi.

Những đóng góp chính của công trình này là một giao diện đơn giản và mạnh mẽ cho phép tự động song song hóa và phân phối các phép tính quy mô lớn, kết hợp với một triển khai của giao diện này đạt hiệu năng cao trên các cụm lớn gồm các PC thông dụng.

Section 2 mô tả mô hình lập trình cơ bản và đưa ra một số ví dụ. Section 3 mô tả một triển khai của giao diện MapReduce được điều chỉnh cho môi trường tính toán dựa trên cụm của chúng tôi. Section 4 mô tả một số cải tiến của mô hình lập trình mà chúng tôi nhận thấy hữu ích. Section 5 trình bày các phép đo hiệu năng của triển khai của chúng tôi cho nhiều loại tác vụ khác nhau. Section 6 khảo sát việc sử dụng MapReduce trong Google, bao gồm các kinh nghiệm của chúng tôi khi sử dụng nó làm nền tảng để viết lại hệ thống lập chỉ mục sản xuất của chúng tôi. Section 7 thảo luận về các công trình liên quan và công việc trong tương lai.
