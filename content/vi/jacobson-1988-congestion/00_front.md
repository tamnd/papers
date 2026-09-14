---
paper: jacobson-1988-congestion
title: Congestion Avoidance and Control
authors:
  - Van Jacobson
year: 1988
venue: SIGCOMM
field: networks
section_title: Front Matter
tag: "0172"
kind: front
lang: vi
source: https://ee.lbl.gov/papers/congavoid.pdf
pdf_sha256: 9ca88dfa60f98d5cf736c3917df45420eb91861dd1de453a3dedf3d91c1836eb
pdf_pages: 1-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: f279eac2ca8029ba28799b3f57bb7d13f517d0033046d50a77ce8751f1512d97
translated_from: content/en/jacobson-1988-congestion/00_front.md
source_content_sha256: d532acb68f191ab0f4414948b7093016f52d315efb6dd404a657c139d62c8967
translation_model: gpt-5
translation_run: 20260914T163737Z
glossary_version: 6
glossary_terms_sha256: 3a5b9dd3cd6211761c92d70db4c4910c364b1cae9e5e732eea77349f449c860b
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Tránh tắc nghẽn và Điều khiển*

Van Jacobson†
Lawrence Berkeley Laboratory

Michael J. Karels‡
University of California at Berkeley

Tháng 11, 1988

Các mạng máy tính đã phát triển bùng nổ trong vài năm qua, và cùng với sự tăng trưởng đó là những vấn đề tắc nghẽn nghiêm trọng. Chẳng hạn, hiện nay việc thấy các gateway Internet loại bỏ 10% số gói tin đến do tràn bộ đệm cục bộ là điều phổ biến. Nghiên cứu của chúng tôi về một số vấn đề này cho thấy phần lớn nguyên nhân nằm ở các cài đặt giao thức truyền tải (không phải bản thân các giao thức): Những cách ‘hiển nhiên’ để cài đặt một giao thức truyền tải dựa trên cửa sổ có thể dẫn đến chính xác hành vi sai trong phản ứng với tắc nghẽn mạng. Chúng tôi đưa ra các ví dụ về hành vi ‘sai’ và mô tả một số thuật toán đơn giản có thể được sử dụng để khiến mọi thứ diễn ra đúng đắn. Các thuật toán này dựa trên ý tưởng đạt được sự ổn định của mạng bằng cách buộc kết nối truyền tải tuân theo một nguyên lý ‘bảo toàn gói tin’. Chúng tôi chỉ ra cách các thuật toán được suy ra từ nguyên lý này và tác động của chúng lên lưu lượng qua các mạng bị tắc nghẽn.
