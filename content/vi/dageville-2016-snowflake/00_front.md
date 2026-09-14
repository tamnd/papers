---
paper: dageville-2016-snowflake
title: The Snowflake Elastic Data Warehouse
authors:
  - Benoit Dageville
  - Thierry Cruanes
  - Marcin Zukowski
  - Vadim Antonov
  - Artin Avanes
  - Jon Bock
  - Jonathan Claybaugh
  - Daniel Engovatov
  - Martin Hentschel
  - Jiansheng Huang
  - Allison W. Lee
  - Ashish Motivala
  - Abdul Q. Munir
  - Steven Pelley
  - Peter Povinec
  - Greg Rahn
  - Spyridon Triantafyllis
  - Philipp Unterbrunner
year: 2016
venue: SIGMOD
field: databases
section_title: Front Matter
tag: 017B
kind: front
lang: vi
source: https://info.snowflake.net/rs/252-RFO-227/images/Snowflake_SIGMOD.pdf
pdf_sha256: b635081104c3647561a476ab5947f5782b2a5c4be5af43b48cea90dba1b9e332
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 3e479857ae6e2f68093f7a9a684a4a52729accecde71af1a19bb2da500c3aace
translated_from: content/en/dageville-2016-snowflake/00_front.md
source_content_sha256: 66823427cd44cd97c9ffbfee566383087ec71d7f2ce8ba659eefd226c3e9a3a4
translation_model: gpt-5
translation_run: 20260914T201546Z
glossary_version: 6
glossary_terms_sha256: a534ae50d60bff0e03804fd3c150e37d1876484531ab87df9c72dc4d0c455eb2
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Kho dữ liệu đàn hồi Snowflake

Benoit Dageville, Thierry Cruanes, Marcin Zukowski, Vadim Antonov, Artin Avanes,

Jon Bock, Jonathan Claybaugh, Daniel Engovatov, Martin Hentschel,

Jiansheng Huang, Allison W. Lee, Ashish Motivala, Abdul Q. Munir, Steven Pelley,

Peter Povinec, Greg Rahn, Spyridon Triantafyllis, Philipp Unterbrunner

Snowflake Computing

TÓM TẮT

Chúng ta đang sống trong kỷ nguyên vàng của tính toán phân tán. Các nền tảng đám mây công cộng hiện cung cấp gần như không giới hạn các tài nguyên tính toán và lưu trữ theo nhu cầu. Đồng thời, mô hình Software-as-a-Service (SaaS) mang các hệ thống cấp doanh nghiệp đến với những người dùng trước đây không thể chi trả cho các hệ thống như vậy do chi phí và độ phức tạp của chúng. Tuy nhiên, các hệ thống kho dữ liệu truyền thống đang gặp khó khăn trong việc thích ứng với môi trường mới này. Một mặt, chúng được thiết kế cho các tài nguyên cố định và do đó không thể tận dụng tính đàn hồi của đám mây. Mặt khác, sự phụ thuộc của chúng vào các đường ống ETL phức tạp và việc tinh chỉnh vật lý đi ngược lại với các yêu cầu về tính linh hoạt và tính mới của các loại dữ liệu bán cấu trúc mới của đám mây cũng như các tải công việc phát triển nhanh chóng.

Chúng tôi quyết định cần có một thiết kế lại mang tính nền tảng. Sứ mệnh của chúng tôi là xây dựng một giải pháp kho dữ liệu sẵn sàng cho doanh nghiệp dành cho đám mây. Kết quả là Kho dữ liệu đàn hồi Snowflake, hay gọi tắt là “Snowflake”. Snowflake là một hệ thống đa người thuê, giao dịch, an toàn, có khả năng mở rộng cao và đàn hồi với hỗ trợ SQL đầy đủ cùng các mở rộng tích hợp sẵn cho dữ liệu bán cấu trúc và dữ liệu không có lược đồ. Hệ thống được cung cấp dưới dạng một dịch vụ trả tiền theo mức sử dụng trong đám mây Amazon. Người dùng tải dữ liệu của họ lên đám mây và có thể ngay lập tức quản lý và truy vấn dữ liệu đó bằng các công cụ và giao diện quen thuộc.
