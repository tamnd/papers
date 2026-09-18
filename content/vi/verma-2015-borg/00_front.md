---
paper: verma-2015-borg
title: Large-scale cluster management at Google with Borg
authors:
  - Abhishek Verma
  - Luis Pedrosa
  - Madhukar Korupolu
  - David Oppenheimer
  - Eric Tune
  - John Wilkes
year: 2015
venue: EuroSys
field: systems
section_title: Front Matter
tag: "0171"
kind: front
lang: vi
source: https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/43438.pdf
pdf_sha256: 2fdacd3b69f8af91477412fc91d1d858a43e764929a4edb646bd517ededdad94
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: ef6381ff322bc1228495ad124533bd3f85086632f2ce496142245292027cf5d0
translated_from: content/en/verma-2015-borg/00_front.md
source_content_sha256: a937cc16e80316f35130faeae6a89689c69ae67f13203bd2a3c47bbd330e8f64
translation_model: gpt-5
translation_run: 20260918T122832Z
glossary_version: 7
glossary_terms_sha256: f834761938c11bca59f7cb79948997ed0706af48cd70392678452699c034a7ad
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Quản lý cụm quy mô lớn tại Google với Borg

Abhishek Verma†    Luis Pedrosa‡    Madhukar Korupolu
David Oppenheimer    Eric Tune    John Wilkes
Google Inc.

Tóm tắt
Hệ thống Borg của Google là một trình quản lý cụm chạy hàng trăm nghìn job, từ nhiều nghìn ứng dụng khác nhau, trên một số cụm, mỗi cụm có tới hàng chục nghìn máy.

Nó đạt được mức sử dụng cao bằng cách kết hợp kiểm soát tiếp nhận, đóng gói tác vụ hiệu quả, over-commitment và chia sẻ máy với sự cô lập hiệu năng ở mức tiến trình. Nó hỗ trợ các ứng dụng có tính sẵn sàng cao với các tính năng thời gian chạy giúp giảm thiểu thời gian khôi phục sau sự cố, và các chính sách lập lịch làm giảm xác suất xảy ra các sự cố tương quan. Borg đơn giản hóa công việc của người dùng bằng cách cung cấp ngôn ngữ đặc tả job khai báo, tích hợp dịch vụ tên, giám sát job theo thời gian thực, và các công cụ để phân tích và mô phỏng hành vi hệ thống.

Chúng tôi trình bày bản tóm tắt về kiến trúc và các tính năng của hệ thống Borg, các quyết định thiết kế quan trọng, một phân tích định lượng về một số quyết định chính sách của nó, và một khảo sát định tính về những bài học rút ra từ một thập kỷ kinh nghiệm vận hành với nó.
