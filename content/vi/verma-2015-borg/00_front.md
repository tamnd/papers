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
content_sha256: e402e0bd2d8aa22adecddafac87f7c828520f7cbf3a39d76554d41bbe3a66a91
translated_from: content/en/verma-2015-borg/00_front.md
source_content_sha256: a937cc16e80316f35130faeae6a89689c69ae67f13203bd2a3c47bbd330e8f64
translation_model: gpt-5
translation_run: 20260914T163737Z
glossary_version: 6
glossary_terms_sha256: afc6de5d010821f75553a129f8b55d5fbabc0d9d7af198021ca9a5a496de4088
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
roundtrip: same
roundtrip_run: 20260914T214350Z
---

Quản lý cụm quy mô lớn tại Google với Borg

Abhishek Verma†    Luis Pedrosa‡    Madhukar Korupolu
David Oppenheimer    Eric Tune    John Wilkes
Google Inc.

Tóm tắt
Hệ thống Borg của Google là một bộ quản lý cụm chạy hàng trăm nghìn công việc, từ hàng nghìn ứng dụng khác nhau, trên một số cụm, mỗi cụm có tới hàng chục nghìn máy.

Hệ thống đạt mức sử dụng cao bằng cách kết hợp kiểm soát tiếp nhận, đóng gói tác vụ hiệu quả, over-commitment và chia sẻ máy với cô lập hiệu năng ở cấp tiến trình. Hệ thống hỗ trợ các ứng dụng có tính sẵn sàng cao với các tính năng thời gian chạy giúp giảm thiểu thời gian khôi phục sau sự cố, cùng các chính sách lập lịch làm giảm xác suất xảy ra các sự cố tương quan. Borg đơn giản hóa công việc của người dùng bằng cách cung cấp một ngôn ngữ đặc tả công việc khai báo, tích hợp dịch vụ tên, giám sát công việc theo thời gian thực và các công cụ để phân tích và mô phỏng hành vi của hệ thống.

Chúng tôi trình bày tóm tắt về kiến trúc và các tính năng của hệ thống Borg, những quyết định thiết kế quan trọng, phân tích định lượng một số quyết định chính sách của hệ thống, và khảo sát định tính những bài học rút ra từ một thập kỷ vận hành hệ thống.
