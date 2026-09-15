---
paper: royce-1970-lifecycle
title: Managing the Development of Large Software Systems
authors:
  - Winston W. Royce
year: 1970
venue: IEEE WESCON
field: software
section_title: Front Matter
tag: "0209"
kind: front
lang: vi
source: https://github.com/tpn/pdfs
pdf_sha256: 9f7db065bd1c911a8d17590eec548478f944c8b05c408f101911cde57d815a78
pdf_pages: 1-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 4196476a387d691cb21b1277a90d6964fcd384b6e45e691f18f508802352336b
translated_from: content/en/royce-1970-lifecycle/00_front.md
source_content_sha256: afcafc9b2ff5326495d53c47190251222232d6d9bc8df97ea471d22326944dd9
translation_model: gpt-5
translation_run: 20260915T033315Z
glossary_version: 6
glossary_terms_sha256: e6d7d95c10a297b8398386447b5f0424f8ccda78f5063d550f1f6b9aef300c33
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

QUẢN LÝ VIỆC PHÁT TRIỂN CÁC HỆ THỐNG PHẦN MỀM LỚN

Dr. Winston W. Royce

GIỚI THIỆU

Tôi sẽ mô tả các quan điểm cá nhân của mình về việc quản lý các dự án phát triển phần mềm lớn. Trong chín năm qua, tôi đã đảm nhận nhiều nhiệm vụ khác nhau, phần lớn liên quan đến việc phát triển các gói phần mềm cho lập kế hoạch nhiệm vụ tàu vũ trụ, điều khiển và phân tích sau chuyến bay. Trong các nhiệm vụ này, tôi đã trải qua những mức độ thành công khác nhau liên quan đến việc đạt được trạng thái vận hành, đúng thời hạn và trong phạm vi chi phí. Những kinh nghiệm của tôi đã tạo nên những định kiến nhất định, và tôi sẽ trình bày một số định kiến đó trong bài thuyết trình này.

CÁC CHỨC NĂNG PHÁT TRIỂN CHƯƠNG TRÌNH MÁY TÍNH

Có hai bước thiết yếu chung cho mọi hoạt động phát triển chương trình máy tính, không phụ thuộc vào kích thước hay độ phức tạp. Trước hết là bước phân tích, tiếp theo là bước viết mã như được minh họa trong Figure 1. Khái niệm triển khai rất đơn giản này thực tế là tất cả những gì cần thiết nếu nỗ lực đủ nhỏ và nếu sản phẩm cuối cùng được vận hành bởi chính những người đã xây dựng nó — như thường được thực hiện với các chương trình máy tính dùng cho mục đích nội bộ. Đây cũng là loại nỗ lực phát triển mà hầu hết khách hàng sẵn sàng chi trả, vì cả hai bước đều bao gồm công việc sáng tạo thực sự, trực tiếp đóng góp vào tính hữu ích của sản phẩm cuối cùng. Tuy nhiên, một kế hoạch triển khai để sản xuất các hệ thống phần mềm lớn hơn, chỉ dựa trên các bước này, chắc chắn sẽ thất bại.
