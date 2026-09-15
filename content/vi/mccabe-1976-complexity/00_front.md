---
paper: mccabe-1976-complexity
title: A Complexity Measure
authors:
  - Thomas J. McCabe
year: 1976
venue: IEEE Transactions on Software Engineering
field: software
section_title: Front Matter
tag: "0068"
kind: front
lang: vi
source: http://www.literateprogramming.com/mccabe.pdf
pdf_sha256: be2ac1035940dfc7fa231e23b33bfa3c2f3e3d8ef3112e20cf92a35a7af537f6
pdf_pages: "1"
extraction: vision
extraction_model: gpt-5
content_sha256: b20bf684d05a365eab81084458b09f62dbdd757616c546bfe12dc042914c2f3d
translated_from: content/en/mccabe-1976-complexity/00_front.md
source_content_sha256: de0c8f3f12115ce84af61d9a6d62f2192b1a75afb199b686166359d8f27c2ff4
translation_model: gpt-5
translation_run: 20260915T033315Z
glossary_version: 6
glossary_terms_sha256: e6d7d95c10a297b8398386447b5f0424f8ccda78f5063d550f1f6b9aef300c33
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Một Phép đo Độ phức tạp

THOMAS J. McCABE

*Chú thích—*Bài báo này mô tả một phép đo độ phức tạp theo lý thuyết đồ thị và minh họa cách nó có thể được sử dụng để quản lý và kiểm soát độ phức tạp của chương trình. Trước tiên, bài báo giải thích cách áp dụng các khái niệm lý thuyết đồ thị và đưa ra một giải thích trực quan về các khái niệm đồ thị theo các thuật ngữ lập trình. Các đồ thị điều khiển của một số chương trình Fortran thực tế sau đó được trình bày để minh họa mối tương quan giữa độ phức tạp trực quan và độ phức tạp theo lý thuyết đồ thị. Một số tính chất của độ phức tạp theo lý thuyết đồ thị sau đó được chứng minh, cho thấy, ví dụ, rằng độ phức tạp độc lập với kích thước vật lý (việc thêm hoặc bớt các câu lệnh hàm không làm thay đổi độ phức tạp) và độ phức tạp chỉ phụ thuộc vào cấu trúc quyết định của một chương trình.

Vấn đề sử dụng luồng điều khiển không có cấu trúc cũng được thảo luận. Một đặc trưng của các đồ thị điều khiển không có cấu trúc được đưa ra và một phương pháp đo lường “tính có cấu trúc” của một chương trình được phát triển. Mối quan hệ giữa cấu trúc và khả năng rút gọn được minh họa bằng một số ví dụ.

Phần cuối cùng của bài báo này đề cập đến một phương pháp luận kiểm thử được sử dụng kết hợp với phép đo độ phức tạp; một chiến lược kiểm thử được định nghĩa, trong đó quy định rằng một chương trình có thể đạt được một mức kiểm thử tối thiểu nhất định hoặc chương trình có thể được rút gọn về mặt cấu trúc.

*Thuật ngữ chỉ mục—*Cơ sở, phép đo độ phức tạp, luồng điều khiển, phân rã, lý thuyết đồ thị, tính độc lập, tuyến tính, mô-đun hóa, lập trình, rút gọn, phần mềm, kiểm thử.
