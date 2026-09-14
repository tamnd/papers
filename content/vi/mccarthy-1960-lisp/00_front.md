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
content_sha256: db78e6ce9dbe3fb1153dc33148628c574a261c70440296b57b7868fc8d093b8c
translated_from: content/en/mccarthy-1960-lisp/00_front.md
source_content_sha256: 99ca45842e94baac0c4a8a87f87f893ac11b3ca331c2904346168b690e50dcd7
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: e18583cfd8910711c2e3aa00f134fd0de9487b97e78e37da9096be4297760e66
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Các Hàm Đệ quy của các Biểu thức Ký hiệu

và Tính toán Chúng bằng Máy, Phần I

John McCarthy, Massachusetts Institute of Technology, Cambridge, Mass. ∗

Tháng 4 năm 1960

1 Giới thiệu

Một hệ thống lập trình có tên LISP (viết tắt của LISt Processor) đã được nhóm Trí tuệ Nhân tạo tại M.I.T. phát triển cho máy tính IBM 704. Hệ thống được thiết kế nhằm tạo thuận lợi cho các thí nghiệm với một hệ thống được đề xuất có tên Advice Taker, theo đó một máy có thể được chỉ dẫn để xử lý cả các câu trần thuật lẫn câu mệnh lệnh và có thể thể hiện “common sense” khi thực hiện các lệnh của mình. Đề xuất ban đầu [1] về Advice Taker được đưa ra vào tháng 11 năm 1958. Yêu cầu chính là một hệ thống lập trình để thao tác trên các biểu thức biểu diễn các câu trần thuật và mệnh lệnh được hình thức hóa, để hệ thống Advice Taker có thể thực hiện các suy diễn.

Trong quá trình phát triển, hệ thống LISP đã trải qua nhiều giai đoạn đơn giản hóa và cuối cùng được xây dựng dựa trên một lược đồ biểu diễn các hàm đệ quy bộ phận của một lớp biểu thức ký hiệu nhất định. Biểu diễn này độc lập với máy tính IBM 704, cũng như với bất kỳ máy tính điện tử nào khác, và giờ đây có vẻ thích hợp khi trình bày hệ thống bằng cách bắt đầu với lớp các biểu thức được gọi là S-expressions và các hàm được gọi là S-functions.

∗ Đưa bài báo này vào L A được ARPA (ONR) tài trợ theo khoản trợ cấp N00014-94-1-0775

TEXmột phần cho Stanford University, nơi John McCarthy đã làm việc từ năm 1962. Sao chép với những thay đổi nhỏ về ký hiệu từ CACM, tháng 4 năm 1960. Nếu muốn xem kiểu chữ chính xác, hãy xem tài liệu đó.
