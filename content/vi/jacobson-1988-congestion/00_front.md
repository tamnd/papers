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
content_sha256: 9ab9125bac0a874d28e4bf0fb994b41bda2e840d823adf5f93ac163082055daf
translated_from: content/en/jacobson-1988-congestion/00_front.md
source_content_sha256: d532acb68f191ab0f4414948b7093016f52d315efb6dd404a657c139d62c8967
translation_model: gpt-5
translation_run: 20260918T122832Z
glossary_version: 7
glossary_terms_sha256: 5bfb74d0e4b3e9a8237f78ceae59e221549684c174791655271c5455f7fd5e4e
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Tránh tắc nghẽn và điều khiển*

Van Jacobson†
Lawrence Berkeley Laboratory

Michael J. Karels‡
University of California at Berkeley

Tháng 11, 1988

Các mạng máy tính đã trải qua sự tăng trưởng bùng nổ trong vài năm qua và cùng với sự tăng trưởng đó đã xuất hiện các vấn đề tắc nghẽn nghiêm trọng. Ví dụ, hiện nay việc thấy các gateway internet loại bỏ 10% các gói tin đầu vào do tràn bộ đệm cục bộ là điều phổ biến. Nghiên cứu của chúng tôi về một số vấn đề này đã chỉ ra rằng phần lớn nguyên nhân nằm trong các triển khai giao thức truyền tải (không phải trong bản thân các giao thức): Những cách ‘hiển nhiên’ để triển khai một giao thức truyền tải dựa trên cửa sổ có thể dẫn đến đúng kiểu hành vi sai trong phản ứng với tắc nghẽn mạng. Chúng tôi đưa ra các ví dụ về hành vi ‘sai’ và mô tả một số thuật toán đơn giản có thể được sử dụng để khiến những điều đúng xảy ra. Các thuật toán bắt nguồn từ ý tưởng đạt được sự ổn định của mạng bằng cách buộc kết nối truyền tải tuân theo một nguyên lý ‘bảo toàn gói tin’. Chúng tôi chỉ ra cách các thuật toán được suy ra từ nguyên lý này và ảnh hưởng của chúng đối với lưu lượng trên các mạng bị tắc nghẽn.
