---
paper: cytron-1991-ssa
title: Efficiently Computing Static Single Assignment Form and the Control Dependence Graph
authors:
  - Ron Cytron
  - Jeanne Ferrante
  - Barry K. Rosen
  - Mark N. Wegman
  - F. Kenneth Zadeck
year: 1991
venue: ACM TOPLAS
field: languages
section_title: Front Matter
tag: 004B
kind: front
lang: vi
source: https://www.cs.utexas.edu/~pingali/CS380C/2010/papers/ssaCytron.pdf
pdf_sha256: 307512bb537628c2b326b23aa02109e7562bfc619509e942e015054ab58eb9ab
pdf_pages: 2-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: f9728092de86422eda424c45eb22344ccefe734cca4078022d5d50290a4df1b1
translated_from: content/en/cytron-1991-ssa/00_front.md
source_content_sha256: cb78a10f4d23a546d27c2bc0b9089d4c80ae88412348f20f31845a48fa971fc6
translation_model: gpt-5
translation_run: 20260918T153717Z
glossary_version: 7
glossary_terms_sha256: 61df191034dbc0d2b4fd3d0e6780a45e637697c607e59ad493d8021ee078cd25
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Thuật ngữ chung: Thuật toán, Ngôn ngữ  
Các từ khóa và cụm từ bổ sung: Phụ thuộc điều khiển, đồ thị luồng điều khiển, chuỗi def-use, nút chi phối, các trình biên dịch tối ưu hóa

Trong các trình biên dịch tối ưu hóa, lựa chọn cấu trúc dữ liệu ảnh hưởng trực tiếp đến sức mạnh và hiệu quả của tối ưu hóa chương trình thực tế. Một lựa chọn cấu trúc dữ liệu kém có thể cản trở tối ưu hóa hoặc làm chậm quá trình biên dịch đến mức các tính năng tối ưu hóa nâng cao trở nên không mong muốn. Gần đây, dạng gán đơn tĩnh (static single assignment) (SSA) [5, 43] và đồ thị phụ thuộc điều khiển (control dependence graph) [24] đã được đề xuất để biểu diễn các thuộc tính luồng dữ liệu và luồng điều khiển của các chương trình. Mỗi kỹ thuật trước đây không liên quan này đều mang lại hiệu quả và sức mạnh cho một lớp hữu ích các tối ưu hóa chương trình. Mặc dù cả hai cấu trúc này đều hấp dẫn, khó khăn trong việc xây dựng chúng và kích thước tiềm năng của chúng đã cản trở việc sử dụng chúng [4]. Chúng tôi trình bày các thuật toán mới có thể tính toán hiệu quả các cấu trúc dữ liệu này cho các đồ thị luồng điều khiển tùy ý. Các thuật toán sử dụng các biên chi phối (dominance frontiers), một khái niệm mới có thể có các ứng dụng khác. Chúng tôi cũng đưa ra bằng chứng phân tích và thực nghiệm rằng tổng kích thước của tất cả các biên chi phối thường là tuyến tính theo kích thước của chương trình ban đầu. Do đó, bài báo này đưa ra bằng chứng mạnh mẽ rằng dạng SSA và các phụ thuộc điều khiển có thể có ích trong thực tế cho tối ưu hóa.
