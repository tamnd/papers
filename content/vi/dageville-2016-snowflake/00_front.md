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
content_sha256: 02ca3d2b01ef01eba46263dbce775cd7b7395ab82099f460db0896125c979cea
translated_from: content/en/dageville-2016-snowflake/00_front.md
source_content_sha256: 66823427cd44cd97c9ffbfee566383087ec71d7f2ce8ba659eefd226c3e9a3a4
translation_model: gpt-5
translation_run: 20260918T153717Z
glossary_version: 7
glossary_terms_sha256: 8d6365491a62bf683f227b4ec25e6ea4a6b206a0b00009512875972be95a0002
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Kho lưu trữ dữ liệu đàn hồi Snowflake

Benoit Dageville, Thierry Cruanes, Marcin Zukowski, Vadim Antonov, Artin Avanes,

Jon Bock, Jonathan Claybaugh, Daniel Engovatov, Martin Hentschel,

Jiansheng Huang, Allison W. Lee, Ashish Motivala, Abdul Q. Munir, Steven Pelley,

Peter Povinec, Greg Rahn, Spyridon Triantafyllis, Philipp Unterbrunner

Snowflake Computing

TÓM TẮT

Chúng ta đang sống trong kỷ nguyên vàng của tính toán phân tán. Các nền tảng đám mây công cộng hiện cung cấp gần như không giới hạn các tài nguyên tính toán và lưu trữ theo nhu cầu. Đồng thời, mô hình Software-as-a-Service (SaaS) mang các hệ thống cấp doanh nghiệp đến với những người dùng trước đây không thể chi trả cho các hệ thống như vậy do chi phí và độ phức tạp của chúng. Tuy nhiên, các hệ thống kho dữ liệu truyền thống đang gặp khó khăn trong việc thích nghi với môi trường mới này. Một mặt, chúng được thiết kế cho các tài nguyên cố định và do đó không thể tận dụng tính đàn hồi của đám mây. Mặt khác, sự phụ thuộc của chúng vào các đường ống ETL phức tạp và việc tinh chỉnh vật lý mâu thuẫn với các yêu cầu về tính linh hoạt và tính mới của các loại dữ liệu bán cấu trúc mới của đám mây và các tải công việc phát triển nhanh chóng.

Chúng tôi quyết định cần một thiết kế lại cơ bản. Nhiệm vụ của chúng tôi là xây dựng một giải pháp kho dữ liệu sẵn sàng cho doanh nghiệp dành cho đám mây. Kết quả là Kho dữ liệu đàn hồi Snowflake, hay gọi ngắn gọn là “Snowflake”. Snowflake là một hệ thống đa người dùng, hỗ trợ giao dịch, an toàn, có khả năng mở rộng cao và đàn hồi với đầy đủ hỗ trợ SQL cùng các phần mở rộng tích hợp sẵn cho dữ liệu bán cấu trúc và dữ liệu không có lược đồ. Hệ thống được cung cấp dưới dạng một dịch vụ trả tiền theo mức sử dụng trong đám mây Amazon. Người dùng tải dữ liệu của họ lên đám mây và có thể ngay lập tức quản lý và truy vấn dữ liệu đó bằng các công cụ và giao diện quen thuộc.
