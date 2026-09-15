---
paper: sussman-1975-scheme
title: 'Scheme: An Interpreter for Extended Lambda Calculus'
authors:
  - Gerald Jay Sussman
  - Guy L. Steele Jr.
year: 1975
venue: MIT AI Memo 349
field: languages
section_title: Front Matter
tag: "0047"
kind: front
lang: vi
source: https://dspace.mit.edu/server/api/core/bitstreams/70ab0fe6-0e7a-41ef-99fb-ac2c9481a05e/content
pdf_sha256: c2961e078943a26ae1f752b202290f561578b7ecf8b24b8929e3c1f99e6b2c52
pdf_pages: 1-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 9f90454658ca76ddf82a2eab6174ef2a40d23290afde59b0220bb6eadbe0b560
translated_from: content/en/sussman-1975-scheme/00_front.md
source_content_sha256: 3d6c1645013adada5ed8396c103bb95dcd22e4e3723d8c5352a4ba786fc9c140
translation_model: gpt-5
translation_run: 20260915T020405Z
glossary_version: 6
glossary_terms_sha256: e18583cfd8910711c2e3aa00f134fd0de9487b97e78e37da9096be4297760e66
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

SCHEME

MỘT BỘ THÔNG DỊCH CHO PHÉP TÍNH LAMBDA MỞ RỘNG bởi

Gerald Jay Sussman and Guy Lewis Steele Jr.

Tóm tắt:

Lấy cảm hứng từ ACTORS [Greif and Hewitt] [Smith and Hewitt], chúng tôi đã triển khai một bộ thông dịch cho một ngôn ngữ giống LISP, SCHEME, dựa trên phép tính lambda [Church], nhưng được mở rộng với các tác dụng phụ, đa xử lý và đồng bộ hóa tiến trình. Mục đích của triển khai này là hướng dẫn. Chúng tôi muốn:

(1) giảm bớt sự nhầm lẫn do Micro-PLANNER, CONNIVER, v.v. gây ra bằng cách làm rõ sự nhúng của các cấu trúc điều khiển không đệ quy trong một ngôn ngữ chủ đệ quy như LISP.

(2) giải thích cách sử dụng các cấu trúc điều khiển này, độc lập với các vấn đề như so khớp mẫu và thao tác cơ sở dữ liệu.

(3) có một miền thực nghiệm cụ thể đơn giản cho một số vấn đề về ngữ nghĩa lập trình và phong cách.

Bài báo này được tổ chức thành các phần. Phần đầu tiên là một "sổ tay tham khảo" ngắn chứa các đặc tả cho tất cả các tính năng bất thường của SCHEME. Tiếp theo, chúng tôi trình bày một chuỗi các ví dụ lập trình minh họa nhiều phong cách lập trình khác nhau và cách sử dụng chúng. Điều này sẽ nêu lên một số vấn đề về ngữ nghĩa mà chúng tôi sẽ cố gắng làm rõ bằng phép tính lambda trong phần thứ ba. Trong phần thứ tư, chúng tôi sẽ đưa ra một thảo luận tổng quát về các vấn đề mà người triển khai một bộ thông dịch cho một ngôn ngữ dựa trên phép tính lambda phải đối mặt. Cuối cùng, chúng tôi sẽ trình bày một bộ thông dịch SCHEME được chú thích hoàn toàn, được viết bằng MacLISP [Moon], nhằm giúp các lập trình viên làm quen với những thủ thuật trong việc triển khai các cấu trúc điều khiển không đệ quy trong một ngôn ngữ đệ quy như LISP.
