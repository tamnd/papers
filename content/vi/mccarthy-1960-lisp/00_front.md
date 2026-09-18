---
paper: mccarthy-1960-lisp
title: Recursive Functions of Symbolic Expressions and Their Computation by Machine, Part I
authors:
  - John McCarthy
year: 1960
venue: Communications of the ACM
field: languages
section_title: Front Matter
tag: "0001"
kind: front
lang: vi
source: http://www-formal.stanford.edu/jmc/recursive.pdf
pdf_sha256: 3d981849e59505eff3f14397a177b409f5d978d43d114bdd67c956e74320fc92
pdf_pages: 1-3
extraction: native
extraction_model: pdftotext version 26.09.0
content_sha256: 6cbbbad11d2b42200f0db59ccd318f3fc76c2725476dbe9fffbdd26a47210309
translated_from: content/en/mccarthy-1960-lisp/00_front.md
source_content_sha256: 62a9d2f18f4beaa77a8b0146e72d94b83ed43bab924361cde21b921469a6e98b
translation_model: gpt-5
translation_run: 20260918T122832Z
glossary_version: 7
glossary_terms_sha256: 61df191034dbc0d2b4fd3d0e6780a45e637697c607e59ad493d8021ee078cd25
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Các hàm đệ quy của biểu thức ký hiệu

và phép tính toán của chúng bằng máy, Phần I

John McCarthy, Massachusetts Institute of Technology, Cambridge, Mass. ∗

Tháng 4 năm 1960

1 Giới thiệu

Một hệ thống lập trình được gọi là LISP (viết tắt của LISt Processor) đã được phát triển cho máy tính IBM 704 bởi nhóm Trí tuệ nhân tạo tại M.I.T. Hệ thống được thiết kế để tạo thuận lợi cho các thí nghiệm với một hệ thống được đề xuất gọi là Advice Taker, theo đó một máy có thể được chỉ dẫn để xử lý cả các câu khai báo cũng như các câu mệnh lệnh và có thể thể hiện “common sense” trong việc thực hiện các lệnh của nó. Đề xuất ban đầu [1] cho Advice Taker được đưa ra vào tháng 11 năm 1958. Yêu cầu chính là một hệ thống lập trình để thao tác các biểu thức biểu diễn các câu khai báo và mệnh lệnh được hình thức hóa, sao cho hệ thống Advice Taker có thể thực hiện các suy luận.

Trong quá trình phát triển, hệ thống LISP đã trải qua một số giai đoạn đơn giản hóa và cuối cùng dựa trên một sơ đồ để biểu diễn các hàm đệ quy từng phần của một lớp biểu thức ký hiệu nhất định. Biểu diễn này độc lập với máy tính IBM 704, hoặc bất kỳ máy tính điện tử nào khác, và hiện nay có vẻ thích hợp khi trình bày hệ thống bằng cách bắt đầu với lớp các biểu thức được gọi là S-expressions và các hàm được gọi là S-functions.

∗ Việc đưa bài báo này vào LaTeX được hỗ trợ một phần bởi khoản tài trợ ARPA (ONR) N00014-94-1-0775 cho Stanford University, nơi John McCarthy đã làm việc từ năm 1962. Sao chép với những thay đổi nhỏ về ký hiệu từ CACM, tháng 4 năm 1960. Nếu muốn kiểu chữ chính xác, hãy xem tại đó.
