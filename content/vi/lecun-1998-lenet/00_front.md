---
paper: lecun-1998-lenet
title: Gradient-Based Learning Applied to Document Recognition
authors:
  - Yann LeCun
  - Leon Bottou
  - Yoshua Bengio
  - Patrick Haffner
year: 1998
venue: Proceedings of the IEEE
field: ai-ml
section_title: Front Matter
tag: 019F
kind: front
lang: vi
source: https://doi.org/10.1109/5.726791
pdf_sha256: 346d2a5b49eb759da050572c187b93e35b68bd6a3b9c5d68c88e6ed96da386b7
pdf_pages: 1-2
extraction: vision
extraction_model: gpt-5
content_sha256: 3a9311ed008c043fafcc08b38a412285068191675d5ee581c79e009f16ac75b4
translated_from: content/en/lecun-1998-lenet/00_front.md
source_content_sha256: e157b646b7848c77ee205db267a30b2eeef6bed8bf1a1222311095797fc08c17
translation_model: gpt-6-astra
translation_run: 20260915T022520Z
glossary_version: 6
glossary_terms_sha256: 0d0a9334a40352952769479a6ad339487dd551fe3d836bae9914ea196d2f4310
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Yann Lecun, Léon Bottou, Yoshua Bengio, Patrick Haffner. Gradient-based learning applied to document recognition. Proceedings of the IEEE, 1998, 86 (11), pp.2278-2324. <10.1109/5.726791>. <hal-03926082>

Mã định danh HAL: hal-03926082

https://hal.science/hal-03926082v1

Nộp ngày 6 tháng 1 năm 2023

HAL là kho lưu trữ truy cập mở đa ngành dành cho việc lưu trữ và phổ biến các tài liệu nghiên cứu khoa học, dù đã được công bố hay chưa. Các tài liệu có thể đến từ các cơ sở giảng dạy và nghiên cứu ở Pháp hoặc nước ngoài, hoặc từ các trung tâm nghiên cứu công lập hay tư nhân.

Kho lưu trữ mở đa ngành HAL dành cho việc lưu trữ và phổ biến các tài liệu khoa học ở cấp độ nghiên cứu, đã hoặc chưa được công bố, đến từ các cơ sở giảng dạy và nghiên cứu của Pháp hoặc nước ngoài, các phòng thí nghiệm công lập hay tư nhân.

Sự cho phép của HAL

YANN LECUN, THÀNH VIÊN IEEE, LÉON BOTTOU, YOSHUA BENGIO, VÀ PATRICK HAFFNER

*Mạng nơ-ron (neural network) nhiều lớp được huấn luyện bằng thuật toán lan truyền ngược (back-propagation) là ví dụ tiêu biểu nhất về một kỹ thuật học dựa trên gradient thành công. Với một kiến trúc mạng phù hợp, các thuật toán học dựa trên gradient có thể được dùng để tạo ra một mặt quyết định phức tạp có khả năng phân loại các mẫu nhiều chiều, chẳng hạn như các ký tự viết tay, với mức tiền xử lý tối thiểu. Bài báo này tổng quan các phương pháp khác nhau được áp dụng cho nhận dạng ký tự viết tay và so sánh chúng trên một tác vụ nhận dạng chữ số viết tay tiêu chuẩn. Mạng nơ-ron tích chập (convolutional neural network), được thiết kế riêng để xử lý sự biến thiên của các hình dạng hai chiều (2-D), được chứng minh là vượt trội hơn tất cả các kỹ thuật khác.*

*Các hệ thống nhận dạng tài liệu trong thực tế gồm nhiều mô-đun, bao gồm trích xuất trường, phân đoạn, nhận dạng và mô hình hóa ngôn ngữ.
