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
content_sha256: 82e40da37620301c5ef465b5da2dfef3ca650b886378d991e1a524dd212bcfdc
translated_from: content/en/decandia-2007-dynamo/00_front.md
source_content_sha256: 3e7585ff4857227fc81ac03c4bc0d4eebe47159e5348aa581115bb7876b7aa4d
translation_model: gpt-5
translation_run: 20260914T163737Z
glossary_version: 6
glossary_terms_sha256: afc6de5d010821f75553a129f8b55d5fbabc0d9d7af198021ca9a5a496de4088
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
roundtrip: differs-in-wording
roundtrip_run: 20260914T214350Z
---

Dynamo: Kho lưu trữ khóa-giá trị có tính sẵn sàng cao của Amazon

Giuseppe DeCandia, Deniz Hastorun, Madan Jampani, Gunavardhan Kakulapati, Avinash Lakshman, Alex Pilchin, Swaminathan Sivasubramanian, Peter Vosshall and Werner Vogels
Amazon.com

TÓM TẮT
Độ tin cậy ở quy mô cực lớn là một trong những thách thức lớn nhất mà chúng tôi phải đối mặt tại Amazon.com, một trong những hoạt động thương mại điện tử lớn nhất thế giới; ngay cả sự gián đoạn nhỏ nhất cũng gây ra những hậu quả tài chính đáng kể và ảnh hưởng đến lòng tin của khách hàng. Nền tảng Amazon.com, cung cấp dịch vụ cho nhiều trang web trên toàn thế giới, được triển khai trên một cơ sở hạ tầng gồm hàng chục nghìn server và các thành phần mạng nằm tại nhiều trung tâm dữ liệu trên khắp thế giới. Ở quy mô này, các thành phần lớn và nhỏ liên tục gặp sự cố, và cách quản lý trạng thái lâu dài trước những sự cố này quyết định độ tin cậy và khả năng mở rộng của các hệ thống phần mềm.

Bài báo này trình bày thiết kế và triển khai Dynamo, một hệ thống lưu trữ khóa-giá trị có tính sẵn sàng cao mà một số dịch vụ cốt lõi của Amazon sử dụng để cung cấp trải nghiệm “always-on”. Để đạt được mức độ sẵn sàng này, Dynamo hy sinh tính nhất quán trong một số kịch bản sự cố nhất định. Hệ thống sử dụng rộng rãi việc phiên bản hóa đối tượng và giải quyết xung đột có sự hỗ trợ của ứng dụng, theo một cách thức cung cấp một giao diện mới để các nhà phát triển sử dụng.

Các danh mục và mô tả đối tượng
D.4.2 [Operating Systems]: Storage Management; D.4.5 [Operating Systems]: Reliability; D.4.2 [Operating Systems]: Performance;

Các thuật ngữ chung
Algorithms, Management, Measurement, Performance, Design, Reliability.
