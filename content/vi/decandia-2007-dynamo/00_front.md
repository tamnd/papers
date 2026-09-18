---
paper: decandia-2007-dynamo
title: 'Dynamo: Amazon''s Highly Available Key-value Store'
authors:
  - Giuseppe DeCandia
  - Deniz Hastorun
  - Madan Jampani
  - Gunavardhan Kakulapati
  - Avinash Lakshman
  - Alex Pilchin
  - Swaminathan Sivasubramanian
  - Peter Vosshall
  - Werner Vogels
year: 2007
venue: SOSP
field: systems
section_title: Front Matter
tag: 016F
kind: front
lang: vi
source: https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf
pdf_sha256: 5cacd624cd7bfd37e3d22e04d8c2e347a49579d2927dbb06f40a89c0bcd40bd4
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 602b6530762460afe68274cd104a2d63a01eb2f1428e115b84c1fa393e804b45
translated_from: content/en/decandia-2007-dynamo/00_front.md
source_content_sha256: 3e7585ff4857227fc81ac03c4bc0d4eebe47159e5348aa581115bb7876b7aa4d
translation_model: gpt-5
translation_run: 20260918T122832Z
glossary_version: 7
glossary_terms_sha256: f834761938c11bca59f7cb79948997ed0706af48cd70392678452699c034a7ad
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Dynamo: Kho lưu trữ khóa-giá trị có tính sẵn sàng cao của Amazon

Giuseppe DeCandia, Deniz Hastorun, Madan Jampani, Gunavardhan Kakulapati, Avinash Lakshman, Alex Pilchin, Swaminathan Sivasubramanian, Peter Vosshall và Werner Vogels  
Amazon.com

TÓM TẮT
Độ tin cậy ở quy mô khổng lồ là một trong những thách thức lớn nhất mà chúng tôi phải đối mặt tại Amazon.com, một trong những hoạt động thương mại điện tử lớn nhất thế giới; ngay cả sự cố gián đoạn nhỏ nhất cũng gây ra những hậu quả tài chính đáng kể và ảnh hưởng đến niềm tin của khách hàng. Nền tảng Amazon.com, cung cấp dịch vụ cho nhiều website trên toàn thế giới, được triển khai trên một cơ sở hạ tầng gồm hàng chục nghìn server và các thành phần mạng nằm trong nhiều trung tâm dữ liệu trên khắp thế giới. Ở quy mô này, các thành phần nhỏ và lớn liên tục gặp sự cố, và cách trạng thái bền vững được quản lý khi đối mặt với các sự cố này quyết định độ tin cậy và khả năng mở rộng của các hệ thống phần mềm.

Bài báo này trình bày thiết kế và triển khai của Dynamo, một hệ thống lưu trữ khóa-giá trị có tính sẵn sàng cao mà một số dịch vụ cốt lõi của Amazon sử dụng để cung cấp trải nghiệm “luôn hoạt động”. Để đạt được mức độ sẵn sàng này, Dynamo hy sinh tính nhất quán trong một số kịch bản sự cố nhất định. Nó sử dụng rộng rãi việc phiên bản hóa đối tượng và giải quyết xung đột có sự hỗ trợ của ứng dụng theo một cách cung cấp một giao diện mới lạ cho các nhà phát triển sử dụng.

Phân loại và Mô tả chủ đề
D.4.2 [Operating Systems]: Quản lý lưu trữ; D.4.5 [Operating Systems]: Độ tin cậy; D.4.2 [Operating Systems]: Hiệu năng;

Thuật ngữ chung
Thuật toán, Quản lý, Đo lường, Hiệu năng, Thiết kế, Độ tin cậy.
