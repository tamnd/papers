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
content_sha256: 18e96c5e55d4dda4de78fb03e74d6a8e4f0dcd41613aa875a9284d7746691e12
translated_from: content/en/mccarthy-1960-lisp/00_front.md
source_content_sha256: 62a9d2f18f4beaa77a8b0146e72d94b83ed43bab924361cde21b921469a6e98b
translation_model: gpt-6-astra
translation_run: 20260914T155130Z
glossary_version: 6
glossary_terms_sha256: e18583cfd8910711c2e3aa00f134fd0de9487b97e78e37da9096be4297760e66
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Các hàm đệ quy của biểu thức ký hiệu

và việc tính toán chúng bằng máy, Phần I

John McCarthy, Viện Công nghệ Massachusetts, Cambridge, Massachusetts. ∗

Tháng 4 năm 1960

1 Giới thiệu

Một hệ thống lập trình có tên LISP (viết tắt của LISt Processor, bộ xử lý danh sách) đã được nhóm Trí tuệ nhân tạo tại M.I.T. phát triển cho máy tính IBM 704. Hệ thống được thiết kế nhằm tạo thuận lợi cho các thử nghiệm với một hệ thống được đề xuất mang tên Advice Taker, trong đó máy có thể được chỉ dẫn để xử lý cả câu trần thuật lẫn câu mệnh lệnh và có thể thể hiện “lẽ thường” khi thực hiện các lệnh. Đề xuất ban đầu [1] về Advice Taker được đưa ra vào tháng 11 năm 1958. Yêu cầu chính là một hệ thống lập trình để thao tác các biểu thức biểu diễn những câu trần thuật và câu mệnh lệnh đã được hình thức hóa, nhờ đó hệ thống Advice Taker có thể thực hiện các phép suy diễn.

Trong quá trình phát triển, hệ thống LISP đã trải qua nhiều giai đoạn đơn giản hóa và cuối cùng dựa trên một phương thức biểu diễn các hàm đệ quy bộ phận (partial recursive functions) của một lớp biểu thức ký hiệu (symbolic expressions) nhất định. Biểu diễn này độc lập với máy tính IBM 704 cũng như với mọi máy tính điện tử khác, và giờ đây có vẻ thích hợp để trình bày hệ thống bắt đầu từ lớp biểu thức được gọi là biểu thức S và các hàm được gọi là hàm S.

∗ Việc chuyển bài báo này sang LaTeX được hỗ trợ một phần từ khoản tài trợ ARPA (ONR) N00014-94-1-0775 dành cho Đại học Stanford, nơi John McCarthy công tác từ năm 1962. Sao chép từ CACM, tháng 4 năm 1960, với một vài thay đổi nhỏ về ký hiệu. Có thể xem bản đó để biết cách trình bày chữ chính xác.
