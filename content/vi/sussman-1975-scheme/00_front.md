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
content_sha256: 69f545388d59e93123105e5b1823e31b7dc94af5b07149e66e4f013fff1067fd
translated_from: content/en/sussman-1975-scheme/00_front.md
source_content_sha256: 326c3043a5d2c15ce603ddfd07ea950af19f0f9587bb0f8c53dce7b8a3d04f66
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: e18583cfd8910711c2e3aa00f134fd0de9487b97e78e37da9096be4297760e66
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

VIỆN CÔNG NGHỆ MASSACHUSETTS

PHÒNG THÍ NGHIỆM TRÍ TUỆ NHÂN TẠO

AI Memo No. 349

Tháng 12 năm 1975

SCHEME

MỘT BỘ THÔNG DỊCH CHO PHÉP TÍNH LAMBDA MỞ RỘNG

bởi

Gerald Jay Sussman và Guy Lewis Steele Jr.

Tóm tắt:

Lấy cảm hứng từ ACTORS [Greif and Hewitt] [Smith and Hewitt], chúng tôi đã triển khai một bộ thông dịch cho một ngôn ngữ giống LISP, SCHEME, dựa trên phép tính lambda [Church], nhưng được mở rộng để hỗ trợ các hiệu ứng phụ, xử lý đa tiến trình và đồng bộ hóa các tiến trình. Mục đích của triển khai này là phục vụ giảng dạy. Chúng tôi mong muốn:

(1) giảm bớt sự nhầm lẫn do Micro-PLANNER, CONNIVER, v.v. gây ra bằng cách làm rõ việc nhúng các cấu trúc điều khiển không đệ quy vào một ngôn ngữ chủ có đệ quy như LISP.

(2) giải thích cách sử dụng các cấu trúc điều khiển này, độc lập với những vấn đề như đối sánh mẫu và thao tác cơ sở dữ liệu.

(3) có một miền thực nghiệm cụ thể đơn giản cho một số vấn đề về ngữ nghĩa và phong cách lập trình.

Bài báo này được tổ chức thành các phần. Phần đầu tiên là một "sổ tay tham khảo" ngắn, chứa các đặc tả cho tất cả các tính năng khác thường của SCHEME. Tiếp theo, chúng tôi trình bày một chuỗi các ví dụ lập trình minh họa nhiều phong cách lập trình khác nhau và cách sử dụng chúng. Điều này sẽ đặt ra một số vấn đề về ngữ nghĩa mà chúng tôi sẽ cố gắng làm rõ bằng phép tính lambda trong phần thứ ba. Trong phần thứ tư, chúng tôi sẽ thảo luận tổng quát về các vấn đề mà người triển khai một bộ thông dịch cho một ngôn ngữ dựa trên phép tính lambda phải đối mặt.
