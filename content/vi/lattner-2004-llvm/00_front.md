---
paper: lattner-2004-llvm
title: 'LLVM: A Compilation Framework for Lifelong Program Analysis & Transformation'
authors:
  - Chris Lattner
  - Vikram Adve
year: 2004
venue: CGO
field: languages
section_title: Front Matter
tag: "0169"
kind: front
lang: vi
source: https://doi.org/10.1109/cgo.2004.1281665
pdf_sha256: 0352543b42fca1c88c3a74b3223a9da68f686435a64d3321450bda4655e4965c
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: f5761e2e7a4b10acb1141e808b3b26f335d0c3f9870df507cfa7e9be914cc3e0
translated_from: content/en/lattner-2004-llvm/00_front.md
source_content_sha256: 1cb970ecf7c43be6d9cf59da18e9d2e109e77f5f2e90024a3d15c1b16a400ff3
translation_model: gpt-5
translation_run: 20260915T013833Z
glossary_version: 6
glossary_terms_sha256: e18583cfd8910711c2e3aa00f134fd0de9487b97e78e37da9096be4297760e66
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

LLVM: Một Khung Trình Biên Dịch cho Phân tích & Biến đổi Chương trình Suốt Vòng đời

Chris Lattner

Vikram Adve
University of Illinois at Urbana-Champaign
{lattner,vadve}@cs.uiuc.edu
http://llvm.cs.uiuc.edu/

TÓM TẮT
Bài báo này mô tả LLVM (Low Level Virtual Machine), một khung trình biên dịch được thiết kế để hỗ trợ phân tích và biến đổi chương trình minh bạch, suốt vòng đời cho các chương trình tùy ý, bằng cách cung cấp thông tin cấp cao cho các biến đổi của trình biên dịch tại thời điểm biên dịch, thời điểm liên kết, thời gian chạy và trong thời gian rỗi giữa các lần chạy. LLVM định nghĩa một biểu diễn mã chung, cấp thấp ở dạng Static Single Assignment (SSA), với một số tính năng mới: một hệ thống kiểu đơn giản, độc lập với ngôn ngữ, làm lộ ra các nguyên thủy thường được dùng để triển khai các tính năng của ngôn ngữ cấp cao; một lệnh cho phép tính toán địa chỉ có kiểu; và một cơ chế đơn giản có thể được dùng để triển khai các tính năng xử lý ngoại lệ của các ngôn ngữ cấp cao (và setjmp/longjmp trong C) một cách thống nhất và hiệu quả. Khung trình biên dịch LLVM và biểu diễn mã cùng nhau cung cấp một tổ hợp các khả năng then chốt quan trọng cho việc phân tích và biến đổi chương trình thực tiễn, suốt vòng đời. Theo hiểu biết của chúng tôi, không có phương pháp biên dịch hiện có nào cung cấp tất cả các khả năng này. Chúng tôi mô tả thiết kế của biểu diễn LLVM và khung trình biên dịch, đồng thời đánh giá thiết kế theo ba cách: (a) kích thước và tính hiệu quả của biểu diễn, bao gồm thông tin kiểu mà nó cung cấp; (b) hiệu năng của trình biên dịch đối với một số vấn đề liên thủ tục; và (c) các ví dụ minh họa về lợi ích mà LLVM cung cấp cho một số vấn đề trình biên dịch đầy thách thức.
