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
content_sha256: 8547d0c18e2b165a467dd2699c02798b20b01fa9da8d706aca0a3d96cf824c59
translated_from: content/en/lattner-2004-llvm/00_front.md
source_content_sha256: 1cb970ecf7c43be6d9cf59da18e9d2e109e77f5f2e90024a3d15c1b16a400ff3
translation_model: gpt-5
translation_run: 20260914T163737Z
glossary_version: 6
glossary_terms_sha256: e18583cfd8910711c2e3aa00f134fd0de9487b97e78e37da9096be4297760e66
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
roundtrip: differs-materially
roundtrip_run: 20260914T214350Z
---

LLVM: Khung biên dịch cho Phân tích & Chuyển đổi Chương trình Suốt Vòng đời

Chris Lattner

Vikram Adve
University of Illinois at Urbana-Champaign
{lattner,vadve}@cs.uiuc.edu
http://llvm.cs.uiuc.edu/

TÓM TẮT
Bài báo này mô tả LLVM (Low Level Virtual Machine), một khung trình biên dịch được thiết kế để hỗ trợ phân tích và chuyển đổi chương trình minh bạch, suốt vòng đời đối với các chương trình tùy ý, bằng cách cung cấp thông tin cấp cao cho các phép chuyển đổi của trình biên dịch tại thời điểm biên dịch, thời điểm liên kết, thời gian chạy và thời gian nhàn rỗi giữa các lần chạy. LLVM định nghĩa một biểu diễn mã mức thấp, chung ở dạng Gán Đơn Tĩnh (Static Single Assignment, SSA), với một số đặc điểm mới: một hệ kiểu đơn giản, độc lập với ngôn ngữ, làm lộ các nguyên tố thường được sử dụng để hiện thực các đặc trưng của ngôn ngữ cấp cao; một lệnh cho phép tính địa chỉ có kiểu; và một cơ chế đơn giản có thể được sử dụng để hiện thực các đặc trưng xử lý ngoại lệ của các ngôn ngữ cấp cao (và setjmp/longjmp trong C) một cách thống nhất và hiệu quả. Khung trình biên dịch LLVM và biểu diễn mã cùng nhau cung cấp một tổ hợp các khả năng then chốt quan trọng đối với việc phân tích và chuyển đổi chương trình suốt vòng đời trong thực tế. Theo hiểu biết của chúng tôi, không có phương pháp biên dịch hiện có nào cung cấp tất cả các khả năng này. Chúng tôi mô tả thiết kế của biểu diễn LLVM và khung trình biên dịch, đồng thời đánh giá thiết kế theo ba phương diện: (a) kích thước và tính hiệu quả của biểu diễn, bao gồm thông tin kiểu mà nó cung cấp; (b) hiệu năng của trình biên dịch đối với một số vấn đề liên thủ tục; và (c) các ví dụ minh họa về những lợi ích mà LLVM mang lại cho một số vấn đề trình biên dịch đầy thách thức.
